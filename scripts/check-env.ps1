param(
    [string]$Venv = ".venv"
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$venvPython = Join-Path $repoRoot "$Venv\Scripts\python.exe"

$env:PYTHONIOENCODING = "utf-8"
$env:PYTHONUTF8 = "1"

if (Test-Path -LiteralPath $venvPython) {
    $python = $venvPython
} else {
    $cmd = Get-Command python -ErrorAction SilentlyContinue
    if (-not $cmd) {
        Write-Host "Python not found. Run scripts/setup.ps1 after installing Python or uv."
        exit 1
    }
    $python = $cmd.Source
}

$code = @'
import importlib
import sys

required = {
    "numpy": "numpy",
    "pandas": "pandas",
    "matplotlib": "matplotlib",
    "seaborn": "seaborn",
    "sklearn": "scikit-learn",
    "scipy": "scipy",
    "statsmodels": "statsmodels",
    "networkx": "networkx",
    "pypdf": "pypdf",
    "openpyxl": "openpyxl",
    "PIL": "pillow",
    "yaml": "pyyaml",
    "pydantic": "pydantic",
}

print(f"Python: {sys.executable}")
print(f"Version: {sys.version.split()[0]}")

if sys.version_info < (3, 11):
    print("FAIL: Python 3.11+ is required.")
    sys.exit(1)

missing = []
for module, package in required.items():
    try:
        importlib.import_module(module)
    except Exception as exc:
        missing.append((package, str(exc)))

if missing:
    print("Missing packages:")
    for package, reason in missing:
        print(f"- {package}: {reason}")
    print("Run: powershell -ExecutionPolicy Bypass -File .\\scripts\\setup.ps1")
    sys.exit(1)

print("Environment check passed.")
'@

$tmp = New-TemporaryFile
$tmpPy = "$($tmp.FullName).py"
Move-Item -LiteralPath $tmp.FullName -Destination $tmpPy -Force

try {
    Set-Content -LiteralPath $tmpPy -Value $code -Encoding UTF8
    & $python $tmpPy
    exit $LASTEXITCODE
}
finally {
    if (Test-Path -LiteralPath $tmpPy) {
        Remove-Item -LiteralPath $tmpPy -Force
    }
}
