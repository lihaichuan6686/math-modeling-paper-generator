param(
    [string]$Main = "main.tex"
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$paperDir = Join-Path $repoRoot "paper"

Push-Location $paperDir
try {
    xelatex -interaction=nonstopmode $Main
    xelatex -interaction=nonstopmode $Main
}
finally {
    Pop-Location
}
