param(
    [string]$Name = "rail-demo",
    [switch]$Force
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

Write-Host "Rail timetable demo artifacts generated."
Write-Host "Run directory: runs\$Name"
Write-Host "Next: insert generated tables/figures into paper sections, compile, and review."
