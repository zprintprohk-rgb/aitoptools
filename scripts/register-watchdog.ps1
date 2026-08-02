# register-watchdog.ps1
# 注册 Watchdog 到 Windows Task Scheduler (管理员权限)
#
# 用法 (管理员 PowerShell):
#   1. 打开 PowerShell (管理员): 右键开始菜单 → "Windows PowerShell (管理员)" 或 "终端 (管理员)"
#   2. cd F:\aitoptools
#   3. powershell -NoProfile -ExecutionPolicy Bypass -File scripts\register-watchdog.ps1
#
# 验证:
#   taskschd.msc → Task Scheduler Library → 找 "aitoptools-mavis-watchdog"
#   或 PowerShell: Get-ScheduledTask -TaskName "aitoptools-mavis-watchdog"
#
# 卸载:
#   powershell -NoProfile -ExecutionPolicy Bypass -File scripts\unregister-watchdog.ps1

$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# 检查管理员
$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
$isAdmin = $currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Host "ERROR: 需要管理员权限运行此脚本" -ForegroundColor Red
    Write-Host "  请右键开始菜单 → 选 'Windows PowerShell (管理员)' 或 '终端 (管理员)'"
    Write-Host "  然后重跑: powershell -NoProfile -ExecutionPolicy Bypass -File scripts\register-watchdog.ps1"
    exit 1
}

$TaskName = 'aitoptools-mavis-watchdog'
$ScriptPath = 'F:\aitoptools\scripts\watchdog-mavis.ps1'
$Description = 'Watchdog: keep MiniMax Code running so mavis cron can fire. Triggers every 5 minutes, auto-start on user logon.'

# 检查是否已注册
$existing = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
if ($existing) {
    Write-Host "Task '$TaskName' already exists. Removing old version..." -ForegroundColor Yellow
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
}

# Action: 跑 watchdog-mavis.ps1
$action = New-ScheduledTaskAction `
    -Execute 'powershell.exe' `
    -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$ScriptPath`"" `
    -WorkingDirectory 'F:\aitoptools'

# Trigger 1: 每 5min 重复 (1 次启动后无限期重复)
$trigger5min = New-ScheduledTaskTrigger `
    -Once `
    -At (Get-Date) `
    -RepetitionInterval (New-TimeSpan -Minutes 5) `
    -RepetitionDuration (New-TimeSpan -Days 3650)

# Settings
$settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -StartWhenAvailable `
    -RunOnlyIfNetworkAvailable:$false `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 2)

# Principal: 当前用户, 最高权限
$principal = New-ScheduledTaskPrincipal `
    -UserId ([Security.Principal.WindowsIdentity]::GetCurrent().Name) `
    -LogonType Interactive `
    -RunLevel Highest

# 注册
try {
    Register-ScheduledTask `
        -TaskName $TaskName `
        -Action $action `
        -Trigger $trigger5min `
        -Settings $settings `
        -Principal $principal `
        -Description $Description `
        -Force | Out-Null
    Write-Host "✓ Watchdog '$TaskName' registered" -ForegroundColor Green
} catch {
    Write-Host "✗ Register failed: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

# 验证
$verify = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
if ($verify) {
    Write-Host ""
    Write-Host "Task 状态:" -ForegroundColor Cyan
    Write-Host "  Name:    $($verify.TaskName)"
    Write-Host "  State:   $($verify.State)"
    Write-Host "  Path:    \Microsoft\Windows\$($verify.TaskPath)"
    Write-Host "  Action:  powershell.exe -NoProfile -ExecutionPolicy Bypass -File $ScriptPath"
    Write-Host ""
    Write-Host "下次触发: $(Get-Date).AddMinutes(5).ToString('yyyy-MM-dd HH:mm:ss') (按 5min 重复)"
    Write-Host ""
    Write-Host "手动跑一次测试:" -ForegroundColor Yellow
    Write-Host "  Start-ScheduledTask -TaskName '$TaskName'"
    Write-Host ""
    Write-Host "看 log:" -ForegroundColor Yellow
    Write-Host "  Get-Content F:\aitoptools\.hermes\logs\watchdog-$(Get-Date -Format 'yyyy-MM-dd').log"
} else {
    Write-Host "✗ Verify failed: task not found after register" -ForegroundColor Red
    exit 1
}
