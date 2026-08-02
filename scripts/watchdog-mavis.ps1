# watchdog-mavis.ps1
# Cron Daemon Watchdog for aitoptools + togthr + zprintpro
#
# Background (2026-07-30 user request):
#   mavis cron is "in-app scheduler" mode, not OS crontab.
#   mavis daemon runs inside MiniMax Code Electron app. When app is not running, cron cannot fire.
#   7/25-7/27 affiliate-monitor missed 3 consecutive days + 7/29 daily-radar missed
#   = MiniMax Code app was not running (user PC was sleeping/off/rebooted)
#
# Function:
#   1. Check if MiniMax Code process is running (Process.Name match)
#   2. Process count < 1 -> start MiniMax Code (via shell:AppsFolder)
#   3. Process count >= 1 -> silent
#   4. All actions logged to .hermes/logs/watchdog-{date}.log
#   5. Sync with mavis cron: Watchdog runs every 5min, mavis cron fires in next 5min window
#
# Register (admin PowerShell):
#   powershell -NoProfile -ExecutionPolicy Bypass -File F:\aitoptools\scripts\register-watchdog.ps1
#
# Manual test:
#   powershell -NoProfile -ExecutionPolicy Bypass -File F:\aitoptools\scripts\watchdog-mavis.ps1
#
# Uninstall:
#   powershell -NoProfile -ExecutionPolicy Bypass -File F:\aitoptools\scripts\unregister-watchdog.ps1

$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'

# === Config ===
$WATCHDOG_NAME = 'aitoptools-mavis-watchdog'
$PROCESS_NAME = 'MiniMax Code'  # MiniMax Code Electron app
$MIN_PROCESS_COUNT = 1
$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Definition
$PROJECT_ROOT = Split-Path -Parent $SCRIPT_DIR
$LOG_DIR = Join-Path (Join-Path $PROJECT_ROOT '.hermes') 'logs'

# Launcher (shell:AppsFolder protocol, Windows 10+)
$LAUNCHER = 'shell:AppsFolder\MiniMaxCode_3t81txbwzhg4y!App'

# === Prepare log dir ===
if (-not (Test-Path $LOG_DIR)) {
    New-Item -ItemType Directory -Path $LOG_DIR -Force | Out-Null
}
$LOG_FILE = Join-Path $LOG_DIR "watchdog-$(Get-Date -Format 'yyyy-MM-dd').log"

function Write-Log {
    param([string]$Level, [string]$Message)
    $ts = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
    $line = "[$ts] [$WATCHDOG_NAME] [$Level] $Message"
    Add-Content -Path $LOG_FILE -Value $line -Encoding UTF8
    if ($Level -eq 'ERROR' -or $Level -eq 'WARN' -or $Level -eq 'ACTION') {
        Write-Host $line
    }
}

# === Main ===
try {
    Write-Log 'INFO' 'Watchdog tick start'

    # 1. Check process
    $processes = Get-Process -Name $PROCESS_NAME -ErrorAction SilentlyContinue
    $count = if ($processes) { @($processes).Count } else { 0 }

    if ($count -ge $MIN_PROCESS_COUNT) {
        # Process running -> silent
        Write-Log 'INFO' "MiniMax Code process count: $count >= $MIN_PROCESS_COUNT. Silent. (next mavis cron 5min window can fire)"
        exit 0
    }

    # 2. Process not running -> start
    Write-Log 'WARN' "MiniMax Code process count: $count < $MIN_PROCESS_COUNT. Starting..."
    Write-Log 'INFO' "  Launcher: $LAUNCHER"

    $started = $false
    $lastError = ''

    # Method 1: shell:AppsFolder
    try {
        Start-Process $LAUNCHER -ErrorAction Stop
        $started = $true
        Write-Log 'ACTION' 'MiniMax Code started successfully (shell:AppsFolder)'
    } catch {
        $lastError = "Method1 shell:AppsFolder: $($_.Exception.Message)"
    }

    # Method 2: direct .exe path
    if (-not $started) {
        $altExe = Join-Path $env:LOCALAPPDATA 'Programs\MiniMax Code\MiniMax Code.exe'
        if (Test-Path $altExe) {
            try {
                Start-Process $altExe -ErrorAction Stop
                $started = $true
                Write-Log 'ACTION' "MiniMax Code started successfully (Method 2: direct .exe path: $altExe)"
            } catch {
                $lastError += "; Method2 direct: $($_.Exception.Message)"
            }
        } else {
            $lastError += "; Method2 path missing: $altExe"
        }
    }

    # Method 3: shell:startup shortcut
    if (-not $started) {
        $startup = [Environment]::GetFolderPath('Startup')
        $shortcut = Join-Path $startup 'MiniMax Code.lnk'
        if (Test-Path $shortcut) {
            try {
                Start-Process $shortcut -ErrorAction Stop
                $started = $true
                Write-Log 'ACTION' "MiniMax Code started successfully (Method 3: shell:startup shortcut)"
            } catch {
                $lastError += "; Method3 shortcut: $($_.Exception.Message)"
            }
        } else {
            $lastError += "; Method3 no startup shortcut"
        }
    }

    if (-not $started) {
        Write-Log 'ERROR' "All start methods failed. $lastError. User must manually start MiniMax Code."
        exit 1
    }

    # 3. Verify start (after 5s)
    Start-Sleep -Seconds 5
    $processes2 = Get-Process -Name $PROCESS_NAME -ErrorAction SilentlyContinue
    $count2 = if ($processes2) { @($processes2).Count } else { 0 }
    if ($count2 -ge $MIN_PROCESS_COUNT) {
        Write-Log 'ACTION' "MiniMax Code start verified PASS: process count $count2. mavis cron 5min window can fire"
        exit 0
    } else {
        Write-Log 'ERROR' "MiniMax Code still 0 process after 5s. Start may have failed. User check needed."
        exit 1
    }
} catch {
    Write-Log 'ERROR' "Watchdog exception: $($_.Exception.Message)"
    exit 1
}
