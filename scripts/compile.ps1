$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$paperDir = Join-Path $repoRoot "paper"

Push-Location $paperDir
try {
    xelatex -interaction=nonstopmode main.tex
    xelatex -interaction=nonstopmode main.tex
}
finally {
    Pop-Location
}
