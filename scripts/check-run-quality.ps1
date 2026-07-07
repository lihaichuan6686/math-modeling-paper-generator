param(
    [string]$Run = "current",
    [string]$Paper = ""
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$python = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"

if (-not (Test-Path $python)) {
    $python = "python"
}

$argsList = @((Join-Path $repoRoot "scripts\check-run-quality.py"), "--run", $Run)

if ($Paper -ne "") {
    $argsList += @("--paper", $Paper)
}

& $python @argsList
exit $LASTEXITCODE
