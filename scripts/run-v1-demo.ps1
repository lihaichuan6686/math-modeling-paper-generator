param(
    [string]$Name = "current",
    [switch]$Force,
    [switch]$InstallAsActiveProblem
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$python = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"

if (-not (Test-Path $python)) {
    $python = "python"
}

$problemSource = Join-Path $repoRoot "problems\demo-v1-supply.md"
$problemTarget = Join-Path $repoRoot "problems\problem.md"

if ($InstallAsActiveProblem -and ((-not (Test-Path $problemTarget)) -or $Force)) {
    Copy-Item -Path $problemSource -Destination $problemTarget -Force
}

if ($Force) {
    & powershell -ExecutionPolicy Bypass -File (Join-Path $repoRoot "scripts\new-run.ps1") -Name $Name -Problem "demo-v1-supply" -Force
} else {
    & powershell -ExecutionPolicy Bypass -File (Join-Path $repoRoot "scripts\new-run.ps1") -Name $Name -Problem "demo-v1-supply"
}
& $python (Join-Path $repoRoot "src\demo_v1.py") $Name

Write-Host "Demo v1 artifacts generated."
Write-Host "Demo problem source: problems\demo-v1-supply.md"
Write-Host "Next: fill paper sections using docs\v1-runbook.md, then compile and review."
