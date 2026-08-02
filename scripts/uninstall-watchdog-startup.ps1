# uninstall-watchdog-startup.ps1
# Remove persistent Watchdog from shell:startup (no admin required)

$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'

$STARTUP_DIR = Join-Path $env:APPDATA 'Microsoft\Windows\Start Menu\Programs\Startup'
$VBS_PATH = Join-Path $STARTUP_DIR 'aitoptools-mavis-watchdog.vbs'

# Kill running watchdog processes
$running = Get-Process powershell -ErrorAction SilentlyContinue | Where-Object {
    $_.CommandLine -like '*watchdog-loop.ps1*'
}
if ($running) {
    Write-Host "Killing running watchdog processes: $($running.Id -join ', ')"
    $running | Stop-Process -Force
} else {
    Write-Host "No running watchdog process found"
}

# Remove VBS launcher
if (Test-Path $VBS_PATH) {
    Remove-Item $VBS_PATH -Force
    Write-Host "VBS launcher removed: $VBS_PATH" -ForegroundColor Green
} else {
    Write-Host "VBS launcher not found: $VBS_PATH" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "=== Uninstall Complete ===" -ForegroundColor Cyan
Write-Host "  Re-run install-watchdog-startup.ps1 to re-install if needed"
