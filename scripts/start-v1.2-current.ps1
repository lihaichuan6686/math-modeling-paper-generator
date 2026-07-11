param(
    [string]$Name = "current",
    [string]$ProblemFile = "",
    [switch]$InstallAsActiveProblem,
    [switch]$Force
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot

$argsList = @(
    "-ExecutionPolicy", "Bypass",
    "-File", (Join-Path $PSScriptRoot "start-current.ps1"),
    "-Name", $Name
)

if ($ProblemFile) {
    $argsList += @("-ProblemFile", $ProblemFile)
}

if ($InstallAsActiveProblem) {
    $argsList += "-InstallAsActiveProblem"
}

if ($Force) {
    $argsList += "-Force"
}

powershell @argsList

Write-Host ""
Write-Host "v1.2 quick path is prepared."
Write-Host "Next read: docs\v1.2-quickstart.md"
Write-Host "Launch prompt file: prompts\08_launch_v1_2.md"
Write-Host "Core planning files:"
Write-Host "- runs\$Name\method-depth-plan.md"
Write-Host "- runs\$Name\section-budget.md"
Write-Host "- runs\$Name\writing-style-plan.md"

