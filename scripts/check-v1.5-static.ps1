param()

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$failures = New-Object System.Collections.Generic.List[string]

function Add-Failure {
    param([string]$Message)
    $failures.Add($Message) | Out-Null
}

function Test-RepoPath {
    param([string]$RelativePath)
    $path = Join-Path $repoRoot $RelativePath
    if (-not (Test-Path -LiteralPath $path)) {
        Add-Failure "Missing file: $RelativePath"
    }
}

function Test-FileContains {
    param(
        [string]$RelativePath,
        [string[]]$Patterns
    )

    $path = Join-Path $repoRoot $RelativePath
    if (-not (Test-Path -LiteralPath $path)) {
        Add-Failure "Cannot inspect missing file: $RelativePath"
        return
    }

    $text = Get-Content -LiteralPath $path -Raw
    foreach ($pattern in $Patterns) {
        if ($text -notmatch [regex]::Escape($pattern)) {
            Add-Failure "Missing expected text in ${RelativePath}: $pattern"
        }
    }
}

$requiredFiles = @(
    "docs\v1.5-paper-template-contract.md",
    "docs\v1.5-method-route-contract.md",
    "docs\v1.5-test-handoff.md",
    "docs\v1.5-readiness-report.md",
    "docs\v1.5-release-checklist.md",
    "docs\v1.5-user-test-feedback-template.md",
    "docs\v1.5-feedback-triage-matrix.md",
    "docs\title-candidates-template.md",
    "knowledge\latex\v1-5-front-matter-rhythm-rules.md",
    "knowledge\latex\v1-5-award-paper-style-rules.md",
    "knowledge\latex\v1-5-award-paper-visual-fingerprint.md",
    "knowledge\community\v1-5-local-experience-soft-rules.md",
    "knowledge\algorithms\v1-5-route-upgrade-atlas.md",
    "knowledge\quality\v1-5-hard-gates.md",
    "memory\v15-paper-generation-feedback.md",
    "prompts\15_launch_v1_5.md",
    "paper\templates\cumcm_v15_main.tex",
    "scripts\check-v1.5-pdf.py",
    "scripts\check-v1.5-pdf.ps1",
    "scripts\setup.ps1",
    "requirements-lite.txt"
)

foreach ($file in $requiredFiles) {
    Test-RepoPath $file
}

$checks = @(
    @{ File = "START_HERE.md"; Patterns = @("prompts/15_launch_v1_5.md", "docs/v1.5-paper-template-contract.md", "docs/v1.5-method-route-contract.md", "docs/v1.5-test-handoff.md", "docs/v1.5-readiness-report.md", "docs/v1.5-release-checklist.md", "docs/v1.5-user-test-feedback-template.md", "docs/v1.5-feedback-triage-matrix.md", "knowledge/latex/v1-5-front-matter-rhythm-rules.md", "knowledge/latex/v1-5-award-paper-style-rules.md", "knowledge/latex/v1-5-award-paper-visual-fingerprint.md", "knowledge/algorithms/v1-5-route-upgrade-atlas.md", "knowledge/quality/v1-5-hard-gates.md", "scripts\setup.ps1", "check-v1.5-pdf.ps1", "-Tex .\paper\main.tex", "-Review .\reviews\review-current.md", "Method Route Verdict") },
    @{ File = "README.md"; Patterns = @("prompts/15_launch_v1_5.md", "docs/v1.5-method-route-contract.md", "docs/v1.5-test-handoff.md", "docs/v1.5-readiness-report.md", "docs/v1.5-release-checklist.md", "docs/v1.5-user-test-feedback-template.md", "docs/v1.5-feedback-triage-matrix.md", "knowledge/latex/v1-5-front-matter-rhythm-rules.md", "knowledge/latex/v1-5-award-paper-visual-fingerprint.md", "knowledge/algorithms/v1-5-route-upgrade-atlas.md", "paper/templates/cumcm_v15_main.tex", "check-v1.5-static.ps1", "check-v1.5-pdf.ps1", "-Tex .\paper\main.tex", "-Review .\reviews\review-current.md", "reviews/pdf-v15-check.md", "title-candidates.md", "Method Route Verdict", "v1.5 Hard Gate Verdict") },
    @{ File = "CLAUDE.md"; Patterns = @("prompts/15_launch_v1_5.md", "Level 0", "v1.5-method-route-contract.md", "v1-5-front-matter-rhythm-rules.md", "v1-5-award-paper-visual-fingerprint.md", "v1-5-local-experience-soft-rules.md", "v1-5-route-upgrade-atlas.md", "paper/templates/cumcm_v15_main.tex", "title-candidates.md", "check-v1.5-pdf.ps1", "reviews/pdf-v15-check.md", "Method Route Verdict", "v1.5 Hard Gate Verdict", "v1.5-user-test-feedback-template.md", "v1.5-feedback-triage-matrix.md") },
    @{ File = ".codex\skills\cumcm-paper-generator\SKILL.md"; Patterns = @("prompts/15_launch_v1_5.md", "Level 0", "v1.5-method-route-contract.md", "v1-5-front-matter-rhythm-rules.md", "v1-5-award-paper-visual-fingerprint.md", "v1-5-local-experience-soft-rules.md", "v1-5-route-upgrade-atlas.md", "paper/templates/cumcm_v15_main.tex", "title-candidates.md", "v1.5 PDF check", "reviews/pdf-v15-check.md", "v1.5 Hard Gate Verdict", "v1.5-user-test-feedback-template.md", "v1.5-feedback-triage-matrix.md") },
    @{ File = "docs\README.md"; Patterns = @("v1.5-paper-template-contract.md", "v1.5-method-route-contract.md", "v1-5-front-matter-rhythm-rules.md", "v1-5-award-paper-visual-fingerprint.md", "v1-5-route-upgrade-atlas.md", "v1.5-test-handoff.md", "v1.5-readiness-report.md", "v1.5-release-checklist.md", "v1.5-user-test-feedback-template.md", "v1.5-feedback-triage-matrix.md", "15_launch_v1_5.md", "check-v1.5-static.ps1") },
    @{ File = "docs\title-candidates-template.md"; Patterns = @("Candidate Titles", "Selected Title", "Unknown", "check-v1.5-pdf.ps1", "v1-5-front-matter-rhythm-rules.md") },
    @{ File = "docs\v1.5-method-route-contract.md"; Patterns = @("Minimum v1.5 Route Shape", "Depth Gate", "Paper Evidence Gate", "Method Route Verdict", "check-v1.5-pdf.ps1", "-Tex .\paper\main.tex", "-Review .\reviews\review-current.md") },
    @{ File = "docs\v1.5-test-handoff.md"; Patterns = @("scripts\setup.ps1", "check-v1.5-static.ps1", "check-v1.5-pdf.ps1", "v1.5-readiness-report.md", "v1.5-release-checklist.md", "v1-5-award-paper-visual-fingerprint.md", "v1.5-user-test-feedback-template.md", "v1.5-feedback-triage-matrix.md", "-Run .\runs\current", "-Tex .\paper\main.tex", "-Review .\reviews\review-current.md", "title-candidates.md", "empty selected title", "review verdict tables", "v1.5-method-route-contract.md", "method-depth-plan.md", "paper/templates/cumcm_v15_main.tex", "v1.5 Hard Gate Verdict") },
    @{ File = "docs\v1.5-readiness-report.md"; Patterns = @("static test candidate", "What v1.5 Adds", "What v1.5 Still Does Not Prove", "User-Side Test Standard", "Next Repair Loop", "v1.5-user-test-feedback-template.md", "v1.5-feedback-triage-matrix.md") },
    @{ File = "docs\v1.5-release-checklist.md"; Patterns = @("Repository Checks", "Required v1.5 Entry Files", "Scaffold Check", "Generated-Paper Check", "Stop Rule", "v1.5-user-test-feedback-template.md", "v1.5-feedback-triage-matrix.md") },
    @{ File = "docs\v1.5-user-test-feedback-template.md"; Patterns = @("First-Look Score", "Required Artifacts", "v1.5 PDF Check Result", "Human Visual Notes", "Failure Classification", "Responsible-Use Confirmation", "v1.5-feedback-triage-matrix.md") },
    @{ File = "docs\v1.5-feedback-triage-matrix.md"; Patterns = @("Repair Layer Rule", "Triage Matrix", "v1.5-user-test-feedback-template.md", "scripts/check-v1.5-static.ps1", "prompt, template, checker", "Stop Rule") },
    @{ File = "prompts\README.md"; Patterns = @("15_launch_v1_5.md", "v1.5 Level 0", "v1.5-method-route-contract.md", "v1-5-front-matter-rhythm-rules.md", "method route depth", "title candidates", "award-paper-feel draft") },
    @{ File = "knowledge\latex\README.md"; Patterns = @("v1-5-front-matter-rhythm-rules.md", "v1-5-award-paper-style-rules.md", "first page") },
    @{ File = "prompts\15_launch_v1_5.md"; Patterns = @("Level 0 required reading only", "v1.5-method-route-contract.md", "v1-5-front-matter-rhythm-rules.md", "v1-5-award-paper-visual-fingerprint.md", "v1-5-local-experience-soft-rules.md", "v1-5-route-upgrade-atlas.md", "memory/v15-paper-generation-feedback.md", "method-depth-plan.md", "Method Route Verdict", "paper/templates/cumcm_v15_main.tex", "title-candidates.md", "check-v1.5-pdf.ps1", "v1.5 Hard Gate Verdict", "Abstract", "\textbf", "Section headings must not contain ASCII hyphens", "source-density target") },
    @{ File = "docs\v1.5-paper-template-contract.md"; Patterns = @("paper/templates/cumcm_v15_main.tex", "title-candidates.md", "Mandatory Early Concept Figure", "Appendix Contract", "PDF Review Contract", "check-v1.5-pdf.ps1") },
    @{ File = "knowledge\latex\v1-5-front-matter-rhythm-rules.md"; Patterns = @("Title Generation Protocol", "First Page Rhythm", "Second Page Rhythm", "title-candidates.md", "five real candidate titles") },
    @{ File = "knowledge\latex\v1-5-award-paper-style-rules.md"; Patterns = @("Title Patterns", "Abstract Form", "Background And Concept Figure", "Appendix Code", "v1-5-award-paper-visual-fingerprint.md") },
    @{ File = "knowledge\latex\v1-5-award-paper-visual-fingerprint.md"; Patterns = @("Visual Fingerprint", "Page One Is A Compressed Solution", "Pages Three To Six Must Show Modeling Objects", "Tail Pages Commonly Carry Code Or Support Files", "v1.5 Review Questions") },
    @{ File = "knowledge\community\v1-5-local-experience-soft-rules.md"; Patterns = @("The Paper Is The Only Scored Artifact", "Every Asked Question Must Be Answered Explicitly", "Simple Useful Models Beat Decorative Complexity", "Appendix Supports Trust But Does Not Carry The Main Answer", "Team Writing Should Have One Voice") },
    @{ File = "knowledge\algorithms\v1-5-route-upgrade-atlas.md"; Patterns = @("Route Upgrade Matrix", "support layer -> main model -> result artifact -> validation artifact -> paper highlight", "method-depth-plan.md", "Abstract Claim Rule", "Paper Highlight Rule") },
    @{ File = "knowledge\quality\v1-5-hard-gates.md"; Patterns = @("Title Gate", "Abstract Gate", "Concept Figure Gate", "Result Sanity Gate", "Method Route Depth Gate", "LaTeX Heading Safety Gate", "Section Density Gate", "v1.5-method-route-contract.md", "-Run .\runs\current", "-Tex .\paper\main.tex", "-Review .\reviews\review-current.md", "check-v1.5-pdf.ps1", "reviews/pdf-v15-check.md", "v1.5 Hard Gate Verdict") },
    @{ File = "memory\v15-paper-generation-feedback.md"; Patterns = @("LaTeX Heading Hyphen Truncation", "First Draft Section Density Was Too Low", "LaTeX Heading Safety Gate", "Section Density Gate") },
    @{ File = "paper\templates\cumcm_v15_main.tex"; Patterns = @("\begin{abstract}", "\textbf", "\appendix", "\begin{lstlisting}", "cumcm_v15") },
    @{ File = "scripts\new-run.ps1"; Patterns = @("Title Candidates", "title-candidates.md", "docs/v1.5-method-route-contract.md", "v1.5 Hard Gate Verdict", "Method Route Verdict", "reviews/pdf-v15-check.md", "-Review ./reviews/review-", "check-v1.5-pdf.ps1", "prompts\15_launch_v1_5.md") },
    @{ File = "scripts\start-current.ps1"; Patterns = @("v1.5 award-paper-feel", "title-candidates.md", "cumcm_v15_main.tex") },
    @{ File = "scripts\check-v1.5-pdf.py"; Patterns = @("Prompt-Language Leak Gate", "Concept Figure Gate", "PDF Density Gate", "Method Route Depth Gate", "LaTeX Source Gate", "Template Placeholder Gate", "LaTeX Heading Safety Gate", "Section Density Gate", "Review Verdict Gate", "Selected title is empty", "filled title candidate rows", "method-depth-plan.md", "Validation artifact", "title-candidates.md", "reviews/pdf-v15-check.md") },
    @{ File = "scripts\check-v1.5-pdf.ps1"; Patterns = @("PYTHONIOENCODING", "check-v1.5-pdf.py", "--run", "--tex", "--review") },
    @{ File = "scripts\setup.ps1"; Patterns = @("PYTHONIOENCODING", "requirements-lite.txt", "uv venv") },
    @{ File = "requirements-lite.txt"; Patterns = @("pandas", "matplotlib", "pypdf", "scikit-learn", "scipy") }
)

foreach ($check in $checks) {
    Test-FileContains -RelativePath $check.File -Patterns $check.Patterns
}

if ($failures.Count -gt 0) {
    Write-Host "v1.5 static check failed:"
    foreach ($failure in $failures) {
        Write-Host "FAIL: $failure"
    }
    exit 1
}

Write-Host "v1.5 static check passed."
exit 0
