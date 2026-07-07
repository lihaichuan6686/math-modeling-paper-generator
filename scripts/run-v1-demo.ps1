param(
    [string]$Name = "current",
    [switch]$Force,
    [switch]$InstallAsActiveProblem,
    [switch]$SkipQualityGate
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

if (-not $SkipQualityGate) {
    & powershell -ExecutionPolicy Bypass -File (Join-Path $repoRoot "scripts\check-run-quality.ps1") -Run $Name
    Add-Content -Encoding UTF8 -Path (Join-Path $repoRoot "runs\$Name\artifact-ledger.md") -Value ""
    Add-Content -Encoding UTF8 -Path (Join-Path $repoRoot "runs\$Name\artifact-ledger.md") -Value "Machine gate: ``scripts/check-run-quality.ps1 -Run $Name`` passed."
    Add-Content -Encoding UTF8 -Path (Join-Path $repoRoot "reviews\review-$Name.md") -Value ""
    Add-Content -Encoding UTF8 -Path (Join-Path $repoRoot "reviews\review-$Name.md") -Value "Machine gate passed: ``scripts/check-run-quality.ps1 -Run $Name``."
}

Write-Host "Demo v1 artifacts generated."
Write-Host "Demo problem source: problems\demo-v1-supply.md"
Write-Host "Next: fill paper sections using docs\v1-runbook.md, then compile and review."
