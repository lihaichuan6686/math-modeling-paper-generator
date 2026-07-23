param(
    [string]$Pdf = "paper\main.pdf",
    [string]$Tex = "paper\main.tex",
    [string]$Log = "paper\main.log",
    [string]$Review = "reviews\review-current.md",
    [string]$Run = "runs\current",
    [string]$Out = "reviews\layout-v16-check.md",
    [switch]$NoFail
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$env:PYTHONIOENCODING = "utf-8"
$env:PYTHONUTF8 = "1"

function Resolve-RepoPath {
    param([string]$PathValue)
    if (-not $PathValue) {
        return $PathValue
    }
    if ([System.IO.Path]::IsPathRooted($PathValue)) {
        return $PathValue
    }
    return Join-Path $repoRoot $PathValue
}

$Pdf = Resolve-RepoPath $Pdf
$Tex = Resolve-RepoPath $Tex
$Log = Resolve-RepoPath $Log
$Review = Resolve-RepoPath $Review
$Run = Resolve-RepoPath $Run
$Out = Resolve-RepoPath $Out

$venvPython = Join-Path $repoRoot ".venv\Scripts\python.exe"
if (Test-Path -LiteralPath $venvPython) {
    $python = $venvPython
} else {
    $python = "python"
}

$checker = Join-Path $PSScriptRoot "check-v1.6-layout.py"
$scriptArgs = @($checker, "--pdf", $Pdf, "--tex", $Tex, "--log", $Log, "--review", $Review, "--run", $Run, "--out", $Out)
if ($NoFail) {
    $scriptArgs += "--no-fail"
}

& $python @scriptArgs
exit $LASTEXITCODE
