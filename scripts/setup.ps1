param(
    [string]$Venv = ".venv"
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$venvPath = Join-Path $repoRoot $Venv
$requirements = Join-Path $repoRoot "requirements-lite.txt"

if (-not (Test-Path -LiteralPath $requirements)) {
    throw "Missing requirements-lite.txt"
}

$env:PYTHONIOENCODING = "utf-8"
$env:PYTHONUTF8 = "1"

Push-Location $repoRoot
try {
    $uv = Get-Command uv -ErrorAction SilentlyContinue
    if ($uv) {
        if (-not (Test-Path -LiteralPath $venvPath)) {
            uv venv $Venv
        }
        uv pip install -r requirements-lite.txt
    } else {
        $python = Get-Command python -ErrorAction SilentlyContinue
        if (-not $python) {
            throw "Python was not found. Install Python or uv first."
        }
        if (-not (Test-Path -LiteralPath $venvPath)) {
            python -m venv $Venv
        }
        $pip = Join-Path $venvPath "Scripts\pip.exe"
        & $pip install -r requirements-lite.txt
    }

    Write-Host "Environment ready: $venvPath"
    Write-Host "Use this Python: $venvPath\Scripts\python.exe"
}
finally {
    Pop-Location
}
