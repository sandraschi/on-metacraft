param([switch]$NoBrowser, [switch]$SkipBuild)
$ErrorActionPreference = "Stop"
$ScriptRoot = Split-Path -Parent $PSCommandPath
$Port = 11026

$Host.UI.RawUI.WindowTitle = "on-metacraft - reader :$Port"

if (-not $SkipBuild) {
    Write-Host "Building reader site + EPUB..." -ForegroundColor Yellow
    & py -3 (Join-Path $ScriptRoot "tools\build_site.py")
}

# Port zombie clearing
Get-NetTCPConnection -LocalPort $Port -ErrorAction SilentlyContinue |
    ForEach-Object { Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }

# Start static server in the background
$Job = Start-Job -Name "on-metacraft-reader" -ScriptBlock {
    param($Root, $ServePort)
    Set-Location $Root
    & py -3 -m http.server $ServePort --bind 127.0.0.1 --directory site
} -ArgumentList $ScriptRoot, $Port

# Readiness poll
$Ready = $false
for ($i = 0; $i -lt 30; $i++) {
    try {
        $r = Invoke-WebRequest -Uri "http://127.0.0.1:$Port/" -TimeoutSec 2 -UseBasicParsing -ErrorAction SilentlyContinue
        if ($r.StatusCode -eq 200) { $Ready = $true; break }
    } catch {}
    Start-Sleep 1
}

if ($Ready) {
    Write-Host "Reader ready on http://127.0.0.1:$Port/" -ForegroundColor Green
    if (-not $NoBrowser) { Start-Process "http://127.0.0.1:$Port/" }
} else {
    Write-Host "Reader did not become ready within 30s. Check job output:" -ForegroundColor Red
    Receive-Job $Job
    exit 1
}

# Keep-alive: follow the server log until Ctrl+C
try {
    while ($true) {
        if ($Job.State -eq "Completed" -or $Job.State -eq "Failed") {
            Receive-Job $Job; break
        }
        Receive-Job $Job | Out-Null
        Start-Sleep 2
    }
} finally {
    Stop-Job $Job -ErrorAction SilentlyContinue
    Remove-Job $Job -ErrorAction SilentlyContinue
}
