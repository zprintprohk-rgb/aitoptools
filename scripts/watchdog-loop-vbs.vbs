' watchdog-loop-vbs.vbs
' Persistent mavis cron daemon watchdog (VBScript version, no PowerShell dependency)
'
' Background (2026-07-31 K3 7/30 user P0 follow-up):
'   7/30 register-watchdog.ps1 needed admin Token - user 没跑 = Watchdog 没真部署
'   7/31 install-watchdog-startup.ps1 (PowerShell while loop) deployed 跑 1 tick 后被 kill
'   hidden window + PowerShell long Start-Sleep 兼容性问题
'   VBScript 用 WScript.Sleep (native Win32 Sleep API) 稳
'
' Architecture:
'   shell:startup shortcut -> this VBScript (hidden window, infinite loop)
'   VBScript wakes every 5min, checks MiniMax Code process, starts if missing
'   VBScript is more stable than PowerShell in hidden window + long sleep scenario
'
' Log: F:\aitoptools\.hermes\logs\watchdog-vbs-{date}.log
'   Same format as PowerShell version for consistency
'
' Trigger: User logon via shell:startup (no admin required)
' Install: powershell -NoProfile -ExecutionPolicy Bypass -File F:\aitoptools\scripts\install-watchdog-startup.ps1

Option Explicit

Const PROCESS_NAME = "MiniMax Code"
Const MIN_PROCESS_COUNT = 1
Const CHECK_INTERVAL_MS = 300000  ' 5 minutes
Const LOG_DIR = "F:\aitoptools\.hermes\logs"
Const WATCHDOG_NAME = "aitoptools-mavis-watchdog-vbs"

' Launchers in order of preference
Dim launchers(2)
launchers(0) = "shell:AppsFolder\MiniMaxCode_3t81txbwzhg4y!App"
launchers(1) = ""
launchers(2) = ""

' Set up local exe path (VBScript has no built-in Environ, use WScript.Shell.ExpandEnvironmentStrings)
Dim localAppData
Dim wshEnv
Set wshEnv = CreateObject("WScript.Shell")
localAppData = wshEnv.ExpandEnvironmentStrings("%LOCALAPPDATA%")
launchers(1) = localAppData & "\Programs\MiniMax Code\MiniMax Code.exe"

' Get current date for log file
Function GetLogPath()
    Dim d, logFile
    d = DatePart("yyyy", Now) & "-" & Right("0" & DatePart("m", Now), 2) & "-" & Right("0" & DatePart("d", Now), 2)
    logFile = LOG_DIR & "\watchdog-vbs-" & d & ".log"
    GetLogPath = logFile
End Function

Sub WriteLog(level, message)
    Dim fso, logFile, ts, line
    Set fso = CreateObject("Scripting.FileSystemObject")
    logFile = GetLogPath()
    ' Ensure log dir exists
    If Not fso.FolderExists(LOG_DIR) Then fso.CreateFolder(LOG_DIR)
    ts = DatePart("yyyy", Now) & "-" & Right("0" & DatePart("m", Now), 2) & "-" & Right("0" & DatePart("d", Now), 2) & " " & Right("0" & DatePart("h", Now), 2) & ":" & Right("0" & DatePart("n", Now), 2) & ":" & Right("0" & DatePart("s", Now), 2)
    line = "[" & ts & "] [" & WATCHDOG_NAME & "] [" & level & "] " & message
    Dim stream
    Set stream = fso.OpenTextFile(logFile, 8, True)  ' 8 = ForAppending
    stream.WriteLine line
    stream.Close
    ' Only print to console for ERROR/WARN/ACTION
    If level = "ERROR" Or level = "WARN" Or level = "ACTION" Then
        WScript.Echo line
    End If
End Sub

Function CountProcesses()
    Dim sh, exec, count
    count = 0
    Set sh = CreateObject("WScript.Shell")
    Set exec = sh.Exec("tasklist /FI ""IMAGENAME eq " & PROCESS_NAME & ".exe"" /NH")
    Dim line
    Do While Not exec.StdOut.AtEndOfStream
        line = exec.StdOut.ReadLine
        If InStr(line, PROCESS_NAME) > 0 Then count = count + 1
    Loop
    CountProcesses = count
End Function

Function TryStart()
    Dim sh, i, errMsg
    Set sh = CreateObject("WScript.Shell")
    For i = 0 To UBound(launchers)
        If launchers(i) = "" Then
            errMsg = errMsg & "Launcher " & i & ": empty path; "
        ElseIf InStr(launchers(i), "shell:") = 1 Then
            ' shell:AppsFolder protocol
            On Error Resume Next
            sh.Run """" & launchers(i) & """", 1, False
            If Err.Number = 0 Then
                TryStart = True
                WriteLog "ACTION", "MiniMax Code started via " & launchers(i)
                Exit Function
            Else
                errMsg = errMsg & "Launcher " & i & " (" & launchers(i) & "): " & Err.Description & "; "
                Err.Clear
            End If
            On Error Goto 0
        Else
            ' Direct exe path - check exists first
            Dim fso
            Set fso = CreateObject("Scripting.FileSystemObject")
            If fso.FileExists(launchers(i)) Then
                On Error Resume Next
                sh.Run """" & launchers(i) & """", 1, False
                If Err.Number = 0 Then
                    TryStart = True
                    WriteLog "ACTION", "MiniMax Code started via direct path: " & launchers(i)
                    Exit Function
                Else
                    errMsg = errMsg & "Launcher " & i & " (" & launchers(i) & "): " & Err.Description & "; "
                    Err.Clear
                End If
                On Error Goto 0
            Else
                errMsg = errMsg & "Launcher " & i & ": path missing " & launchers(i) & "; "
            End If
        End If
    Next
    TryStart = False
    WriteLog "ERROR", "All launchers failed. " & errMsg & " User must manually start MiniMax Code."
End Function

' Main loop
Sub MainLoop
    Dim startMsg
    startMsg = "Watchdog VBS loop started (Wscript version, interval: " & (CHECK_INTERVAL_MS / 1000) & "s)"
    WriteLog "INFO", startMsg

    Do While True
        Dim count, started, exitCode
        count = CountProcesses()

        If count >= MIN_PROCESS_COUNT Then
            ' Silent - process running
            exitCode = 0
        Else
            WriteLog "WARN", "MiniMax Code process count: " & count & " < " & MIN_PROCESS_COUNT & ". Starting..."
            started = TryStart()
            If started Then
                ' Verify after 5s
                WScript.Sleep 5000
                count = CountProcesses()
                If count >= MIN_PROCESS_COUNT Then
                    WriteLog "ACTION", "MiniMax Code start verified: " & count & " processes. mavis cron 5min window can fire."
                    exitCode = 0
                Else
                    WriteLog "ERROR", "MiniMax Code still 0 process after 5s. Start may have failed."
                    exitCode = 1
                End If
            Else
                exitCode = 1
            End If
        End If

        WriteLog "INFO", "Tick done, exit_code=" & exitCode & ". Sleeping " & (CHECK_INTERVAL_MS / 1000) & "s..."

        ' Native Win32 sleep, stable in hidden window
        WScript.Sleep CHECK_INTERVAL_MS
    Loop
End Sub

MainLoop
