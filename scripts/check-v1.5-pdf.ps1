param(
    [string]$Pdf = "paper\main.pdf",
    [string]$Out = "reviews\pdf-v15-check.md",
    [string]$Run = "runs\current",
    [string]$Tex = "paper\main.tex",
    [string]$Review = "reviews\review-current.md",
    [switch]$NoFail
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$env:PYTHONIOENCODING = "utf-8"
$env:PYTHONUTF8 = "1"

if (-not [System.IO.Path]::IsPathRooted($Pdf)) {
    $Pdf = Join-Path $repoRoot $Pdf
}

if (-not [System.IO.Path]::IsPathRooted($Out)) {
    $Out = Join-Path $repoRoot $Out
}

if ($Run -and (-not [System.IO.Path]::IsPathRooted($Run))) {
    $Run = Join-Path $repoRoot $Run
}

if ($Tex -and (-not [System.IO.Path]::IsPathRooted($Tex))) {
    $Tex = Join-Path $repoRoot $Tex
}

if ($Review -and (-not [System.IO.Path]::IsPathRooted($Review))) {
    $Review = Join-Path $repoRoot $Review
}

$venvPython = Join-Path $repoRoot ".venv\Scripts\python.exe"
if (Test-Path -LiteralPath $venvPython) {
    $python = $venvPython
} else {
    $python = "python"
}

$checker = Join-Path $PSScriptRoot "check-v1.5-pdf.py"
$scriptArgs = @($checker, "--pdf", $Pdf, "--out", $Out)
if ($Run) {
    $scriptArgs += @("--run", $Run)
}
if ($Tex) {
    $scriptArgs += @("--tex", $Tex)
}
if ($Review) {
    $scriptArgs += @("--review", $Review)
}
if ($NoFail) {
    $scriptArgs += "--no-fail"
}

& $python @scriptArgs
exit $LASTEXITCODE
