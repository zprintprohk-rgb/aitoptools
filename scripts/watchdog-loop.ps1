# watchdog-loop.ps1
# Persistent Watchdog (no admin rights needed) for mavis cron
#
# Background (2026-07-30 user P0 request + 7/31 K3 follow-up):
#   mavis cron is in-app scheduler inside MiniMax Code Electron app.
#   7/25-7/27 affiliate-monitor missed 3 days + 7/29 daily-radar missed
#   = MiniMax Code app was not running.
#   Previous solution: scripts/watchdog-mavis.ps1 + register-watchdog.ps1
#   PROBLEM: register needs admin rights, user has not run it.
#   This file: loop version that auto-starts on user logon, no admin needed.
#
# Architecture:
#   shell:startup shortcut -> watchdog-loop.vbs (VBScript) -> watchdog-loop.ps1 (infinite loop)
#   The script loops forever with 5min interval checks. When user logs in, shell:startup
#   triggers the VBScript which spawns the PS1 in a hidden window. The PS1 keeps running
#   for the entire user session, checking MiniMax Code every 5min.
#   When user logs out, the loop dies. When user logs in again, shell:startup re-triggers.
#
# Install (no admin needed):
#   powershell -NoProfile -ExecutionPolicy Bypass -File F:\aitoptools\scripts\install-watchdog-startup.ps1
#
# Uninstall:
#   powershell -NoProfile -ExecutionPolicy Bypass -File F:\aitoptools\scripts\uninstall-watchdog-startup.ps1
#
# Status check (no admin needed):
#   Get-Process powershell -ErrorAction SilentlyContinue | Where-Object {
#       $_.CommandLine -like '*watchdog-loop.ps1*'
#   }

$ErrorActionPreference = 'Continue'
$ProgressPreference = 'SilentlyContinue'

# === Config ===
$WATCHDOG_NAME = 'aitoptools-mavis-watchdog-loop'
$PROCESS_NAME = 'MiniMax Code'
$MIN_PROCESS_COUNT = 1
$CHECK_INTERVAL_SEC = 300  # 5 minutes
$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Definition
$PROJECT_ROOT = Split-Path -Parent $SCRIPT_DIR
$LOG_DIR = Join-Path (Join-Path $PROJECT_ROOT '.hermes') 'logs'
$LOG_FILE = Join-Path $LOG_DIR "watchdog-loop-$(Get-Date -Format 'yyyy-MM-dd').log"

# Launcher candidates (in order of preference)
$LAUNCHERS = @(
    'shell:AppsFolder\MiniMaxCode_3t81txbwzhg4y!App',
    (Join-Path $env:LOCALAPPDATA 'Programs\MiniMax Code\MiniMax Code.exe')
)

# === Prepare log dir ===
if (-not (Test-Path $LOG_DIR)) {
    New-Item -ItemType Directory -Path $LOG_DIR -Force | Out-Null
}

function Write-Log {
    param([string]$Level, [string]$Message)
    $ts = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
    $line = "[$ts] [$WATCHDOG_NAME] [$Level] $Message"
    Add-Content -Path $LOG_FILE -Value $line -Encoding UTF8
    if ($Level -eq 'ERROR' -or $Level -eq 'WARN' -or $Level -eq 'ACTION') {
        Write-Host $line
    }
}

function Test-AndStart {
    $processes = Get-Process -Name $PROCESS_NAME -ErrorAction SilentlyContinue
    $count = if ($processes) { @($processes).Count } else { 0 }

    if ($count -ge $MIN_PROCESS_COUNT) {
        # Silent
        return $true
    }

    Write-Log 'WARN' "MiniMax Code process count: $count < $MIN_PROCESS_COUNT. Starting..."

    $started = $false
    $lastError = ''

    foreach ($launcher in $LAUNCHERS) {
        if ($started) { break }
        try {
            if ($launcher.StartsWith('shell:')) {
                Start-Process $launcher -ErrorAction Stop
            } elseif (Test-Path $launcher) {
                Start-Process $launcher -ErrorAction Stop
            } else {
                $lastError += "Launcher path missing: $launcher; "
                continue
            }
            $started = $true
            Write-Log 'ACTION' "MiniMax Code started via $launcher"
        } catch {
            $lastError += "Launcher $launcher failed: $($_.Exception.Message); "
        }
    }

    if (-not $started) {
        Write-Log 'ERROR' "All launchers failed. $lastError User must manually start MiniMax Code."
        return $false
    }

    # Verify after 5s
    Start-Sleep -Seconds 5
    $processes2 = Get-Process -Name $PROCESS_NAME -ErrorAction SilentlyContinue
    $count2 = if ($processes2) { @($processes2).Count } else { 0 }
    if ($count2 -ge $MIN_PROCESS_COUNT) {
        Write-Log 'ACTION' "MiniMax Code start verified: $count2 processes. mavis cron 5min window can fire."
        return $true
    } else {
        Write-Log 'ERROR' "MiniMax Code still 0 process after 5s. User check needed."
        return $false
    }
}

# === Main loop ===
Write-Log 'INFO' "Watchdog loop started (PID: $PID, interval: ${CHECK_INTERVAL_SEC}s)"

try {
    while ($true) {
        $result = Test-AndStart
        $exitCode = if ($result) { 0 } else { 1 }
        Write-Log 'INFO' "Tick done, exit_code=$exitCode. Sleeping ${CHECK_INTERVAL_SEC}s..."
        Start-Sleep -Seconds $CHECK_INTERVAL_SEC
    }
} catch {
    Write-Log 'ERROR' "Loop exception: $($_.Exception.Message)"
    exit 1
}
