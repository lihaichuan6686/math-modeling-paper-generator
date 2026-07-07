param(
    [string]$Name = "current",
    [string]$ProblemFile = "",
    [switch]$InstallAsActiveProblem,
    [switch]$Force
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$problemPath = Join-Path $repoRoot "problems\problem.md"

if ($ProblemFile) {
    $resolvedProblem = Resolve-Path -LiteralPath $ProblemFile
    if ($InstallAsActiveProblem) {
        if ((Test-Path $problemPath) -and (-not $Force)) {
            throw "problems\problem.md already exists. Use -Force to replace it."
        }
        Copy-Item -LiteralPath $resolvedProblem -Destination $problemPath -Force
        Write-Host "Installed active problem: $problemPath"
    }
}

if (-not (Test-Path $problemPath)) {
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $problemPath) | Out-Null
    Set-Content -Path $problemPath -Encoding UTF8 -Value @"
# Problem Statement

Paste the problem statement here, then ask Claude Code to use `.codex/skills/cumcm-paper-generator/SKILL.md`.
"@
    Write-Host "Created placeholder problem file: $problemPath"
}

$problemLabel = if ($ProblemFile) {
    Split-Path -Leaf $ProblemFile
} else {
    "active problem"
}

$newRunArgs = @(
    "-ExecutionPolicy", "Bypass",
    "-File", (Join-Path $PSScriptRoot "new-run.ps1"),
    "-Name", $Name,
    "-Problem", $problemLabel
)

if ($Force) {
    $newRunArgs += "-Force"
}

powershell @newRunArgs

Write-Host ""
Write-Host "Clone-ready start is prepared."
Write-Host "Next prompt for Claude Code:"
Write-Host "Use .codex/skills/cumcm-paper-generator/SKILL.md and problems/problem.md to generate the v1.0 paper draft, then review it with prompts/06_quality_review.md."
