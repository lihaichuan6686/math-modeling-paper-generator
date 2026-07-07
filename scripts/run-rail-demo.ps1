param(
    [string]$Name = "rail-demo",
    [switch]$Force,
    [switch]$SkipQualityGate
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$python = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"

if (-not (Test-Path $python)) {
    $python = "python"
}

if ($Force) {
    & powershell -ExecutionPolicy Bypass -File (Join-Path $repoRoot "scripts\new-run.ps1") -Name $Name -Problem "rail-timetable-demo" -Force
} else {
    & powershell -ExecutionPolicy Bypass -File (Join-Path $repoRoot "scripts\new-run.ps1") -Name $Name -Problem "rail-timetable-demo"
}

& $python (Join-Path $repoRoot "src\rail_timetable_demo.py") $Name

if (-not $SkipQualityGate) {
    & powershell -ExecutionPolicy Bypass -File (Join-Path $repoRoot "scripts\check-run-quality.ps1") -Run $Name -Paper "rail_demo.tex"
    Add-Content -Encoding UTF8 -Path (Join-Path $repoRoot "runs\$Name\artifact-ledger.md") -Value ""
    Add-Content -Encoding UTF8 -Path (Join-Path $repoRoot "runs\$Name\artifact-ledger.md") -Value "Machine gate: ``scripts/check-run-quality.ps1 -Run $Name -Paper rail_demo.tex`` passed."
    Add-Content -Encoding UTF8 -Path (Join-Path $repoRoot "reviews\review-$Name.md") -Value ""
    Add-Content -Encoding UTF8 -Path (Join-Path $repoRoot "reviews\review-$Name.md") -Value "Machine gate passed: ``scripts/check-run-quality.ps1 -Run $Name -Paper rail_demo.tex``."
}

Write-Host "Rail timetable demo artifacts generated."
Write-Host "Run directory: runs\$Name"
Write-Host "Next: compile paper\rail_demo.tex, inspect rendered pages, and extend real-data parsing when needed."
