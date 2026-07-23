param(
    [string]$Pdf = "paper\main.pdf",
    [string]$Tex = "paper\main.tex",
    [string]$Log = "paper\main.log",
    [string]$Run = "runs\current",
    [string]$Review = "reviews\review-current.md",
    [string]$PdfReport = "reviews\pdf-v15-check.md",
    [string]$LayoutReport = "reviews\layout-v16-check.md",
    [string]$FinalReport = "reviews\final-v16-check.md",
    [string]$Venv = ".venv",
    [switch]$SkipEnv,
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

function Format-Status {
    param([int]$ExitCode)
    if ($ExitCode -eq 0) {
        return "PASS"
    }
    return "FAIL"
}

function Invoke-CheckScript {
    param(
        [string]$Name,
        [string]$ScriptPath,
        [string[]]$Arguments
    )

    Write-Host ""
    Write-Host "== $Name =="

    $powershell = Join-Path $env:SystemRoot "System32\WindowsPowerShell\v1.0\powershell.exe"
    $commandArgs = @("-NoProfile", "-ExecutionPolicy", "Bypass", "-File", $ScriptPath) + $Arguments
    & $powershell @commandArgs
    $exitCode = $LASTEXITCODE

    [PSCustomObject]@{
        Name = $Name
        ExitCode = $exitCode
        Status = Format-Status $exitCode
    }
}

$Pdf = Resolve-RepoPath $Pdf
$Tex = Resolve-RepoPath $Tex
$Log = Resolve-RepoPath $Log
$Run = Resolve-RepoPath $Run
$Review = Resolve-RepoPath $Review
$PdfReport = Resolve-RepoPath $PdfReport
$LayoutReport = Resolve-RepoPath $LayoutReport
$FinalReport = Resolve-RepoPath $FinalReport

$finalReportDir = Split-Path -Parent $FinalReport
if ($finalReportDir -and (-not (Test-Path -LiteralPath $finalReportDir))) {
    New-Item -ItemType Directory -Force -Path $finalReportDir | Out-Null
}

$results = New-Object System.Collections.Generic.List[object]

if ($SkipEnv) {
    $results.Add([PSCustomObject]@{
        Name = "Environment Gate"
        ExitCode = 0
        Status = "SKIP"
    }) | Out-Null
} else {
    $results.Add((Invoke-CheckScript `
        -Name "Environment Gate" `
        -ScriptPath (Join-Path $PSScriptRoot "check-env.ps1") `
        -Arguments @("-Venv", $Venv))) | Out-Null
}

$pdfArgs = @(
    "-Pdf", $Pdf,
    "-Out", $PdfReport,
    "-Run", $Run,
    "-Tex", $Tex,
    "-Review", $Review
)
$results.Add((Invoke-CheckScript `
    -Name "v1.5 PDF And Source Gate" `
    -ScriptPath (Join-Path $PSScriptRoot "check-v1.5-pdf.ps1") `
    -Arguments $pdfArgs)) | Out-Null

$layoutArgs = @(
    "-Pdf", $Pdf,
    "-Tex", $Tex,
    "-Log", $Log,
    "-Run", $Run,
    "-Review", $Review,
    "-Out", $LayoutReport
)
$results.Add((Invoke-CheckScript `
    -Name "v1.6 Layout And Award-Feel Gate" `
    -ScriptPath (Join-Path $PSScriptRoot "check-v1.6-layout.ps1") `
    -Arguments $layoutArgs)) | Out-Null

$failed = @($results | Where-Object { $_.Status -eq "FAIL" })
$overall = "PASS"
if ($failed.Count -gt 0) {
    $overall = "FAIL"
}

$lines = @(
    "# v1.6 Final Check Report",
    "",
    "- Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')",
    "- Overall: $overall",
    "- PDF: $Pdf",
    "- TeX: $Tex",
    "- Run: $Run",
    "- Review: $Review",
    "",
    "## Gate Results",
    "",
    "| Gate | Status | Exit Code |",
    "| --- | --- | --- |"
)

foreach ($result in $results) {
    $lines += "| $($result.Name) | $($result.Status) | $($result.ExitCode) |"
}

$lines += @(
    "",
    "## Reports To Read",
    "",
    "- $PdfReport",
    "- $LayoutReport",
    "",
    "## Rule",
    "",
    "Do not hand off a v1.6 paper until this report is PASS, both child reports are read, and the final review records v1.5 Hard Gate Verdict, Method Route Verdict, and v1.6 Layout Gate Verdict."
)

Set-Content -LiteralPath $FinalReport -Value $lines -Encoding UTF8

Write-Host ""
Write-Host "== v1.6 Final Check Summary =="
foreach ($result in $results) {
    Write-Host "$($result.Status): $($result.Name)"
}
Write-Host "Report: $FinalReport"

if (($overall -eq "FAIL") -and (-not $NoFail)) {
    exit 1
}

exit 0
