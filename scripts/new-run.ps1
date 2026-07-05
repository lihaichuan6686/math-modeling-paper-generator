param(
    [string]$Name = "current"
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$runDir = Join-Path $repoRoot "runs\$Name"

New-Item -ItemType Directory -Force -Path $runDir | Out-Null
New-Item -ItemType File -Force -Path (Join-Path $runDir "problem-analysis.md") | Out-Null
New-Item -ItemType File -Force -Path (Join-Path $runDir "model-candidates.md") | Out-Null
New-Item -ItemType File -Force -Path (Join-Path $runDir "model-plan.md") | Out-Null

Write-Host "Created run directory: $runDir"

