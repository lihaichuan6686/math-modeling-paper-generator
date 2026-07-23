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
    "docs\v1.6-design-plan.md",
    "docs\v1.6-paper-template-contract.md",
    "docs\v1.6-test-handoff.md",
    "docs\v1.6-readiness-report.md",
    "docs\v1.6-release-checklist.md",
    "docs\v1.6-user-test-feedback-template.md",
    "docs\v1.6-feedback-triage-matrix.md",
    "docs\knowledge-coverage-audit-v1.6.md",
    "docs\v1.6-calibration-roadmap.md",
    "docs\v1.6-calibration-log-template.md",
    "docs\concept-figure-helper.md",
    "knowledge\cumcm\v1-6-route-to-paper-structure-index.md",
    "knowledge\cumcm\v1-6-family-calibration-priority.md",
    "knowledge\algorithms\v1-6-method-chain-evidence-index.md",
    "knowledge\latex\v1-6-layout-rhythm-rules.md",
    "knowledge\latex\v1-6-section-rhythm-soft-metrics.md",
    "knowledge\latex\v1-6-award-feel-soft-rules.md",
    "knowledge\latex\v1-6-reference-and-citation-rhythm.md",
    "knowledge\latex\v1-6-award-paper-quantity-calibration.md",
    "knowledge\community\v1-6-excellent-paper-reader-lens.md",
    "knowledge\visuals\v1-6-nature-style-figure-rules.md",
    "knowledge\visuals\v1-6-visual-generation-decision.md",
    "knowledge\quality\v1-6-layout-hard-gates.md",
    "prompts\16_launch_v1_6.md",
    "paper\templates\cumcm_v16_main.tex",
    "paper\templates\table-safe-snippets.tex",
    "requirements-lite.txt",
    "environment-lite.yml",
    "pyproject.toml",
    "docs\environment-setup.md",
    "scripts\check-env.ps1",
    "scripts\check-v1.6-final.ps1",
    "scripts\check-v1.6-layout.py",
    "scripts\check-v1.6-layout.ps1",
    "scripts\check-v1.6-static.ps1",
    "scripts\generate-concept-figure.py",
    "scripts\new-run.ps1",
    "scripts\start-current.ps1",
    "START_HERE.md",
    "README.md",
    "CLAUDE.md",
    ".codex\skills\cumcm-paper-generator\SKILL.md",
    "docs\README.md",
    "prompts\README.md",
    "knowledge\latex\README.md",
    "knowledge\quality\README.md",
    "knowledge\visuals\README.md"
)

foreach ($file in $requiredFiles) {
    Test-RepoPath $file
}

$checks = @(
    @{ File = "docs\v1.6-design-plan.md"; Patterns = @("26-32 pages", "900-1150", "Nature-style", "table overflow", "v1-6-section-rhythm-soft-metrics.md", "layout-v16-check.md") },
    @{ File = "docs\v1.6-paper-template-contract.md"; Patterns = @("cumcm_v16_main.tex", "cumcm_v15_main.tex", "tabular{lll}", "structured abstract", "route-to-paper fields", "visible TODO", "concept-figure fallback text") },
    @{ File = "docs\v1.6-test-handoff.md"; Patterns = @("16_launch_v1_6.md", "section-rhythm-budget.md", "figure-style-spec.md", "check-v1.6-final.ps1", "v1.6-user-test-feedback-template.md") },
    @{ File = "docs\v1.6-readiness-report.md"; Patterns = @("Static Evidence", "Calibration On The v1.5 User Test PDF", "5 fail, 9 warn", "rendered-page or screenshot inspection", "Known Tooling Risk", "Dependency Gate", "check-v1.6-final.ps1", "Next Repair Loop") },
    @{ File = "docs\v1.6-release-checklist.md"; Patterns = @("check-v1.6-static.ps1", "check-v1.6-final.ps1", "Required v1.6 Entry Files", "v1.6-readiness-report.md", "final-v16-check.md", "layout-v16-check.md", "Stop Rule") },
    @{ File = "docs\v1.6-user-test-feedback-template.md"; Patterns = @("First-Look Score", "Required Artifact Check", "Layout Findings", "Visual Notes", "Failure Classification") },
    @{ File = "docs\v1.6-feedback-triage-matrix.md"; Patterns = @("Repair Layer Rule", "Triage Table", "page rhythm", "Table overflows", "checker repair") },
    @{ File = "docs\knowledge-coverage-audit-v1.6.md"; Patterns = @("Coverage Matrix", "Local CUMCM materials", "Excellent-paper paradigms", "Algorithm and problem-type index", "LaTeX writing and layout norms", "Visual generation workflow", "v1-6-award-paper-quantity-calibration.md", "v1-6-excellent-paper-reader-lens.md", "Evidence Standard For Future Completion") },
    @{ File = "docs\v1.6-calibration-roadmap.md"; Patterns = @("v1.6 Calibration Roadmap", "release-candidate hardening phase", "Calibration Batch", "Visual-generation helper decision", "Reference rhythm calibration", "Excellent-paper reader lens", "Award-paper quantity calibration", "v1-6-visual-generation-decision.md", "v1-6-reference-and-citation-rhythm.md", "v1-6-award-paper-quantity-calibration.md", "v1-6-excellent-paper-reader-lens.md", "concept-figure-helper.md", "v1.6-calibration-log-template.md", "Stop Rule") },
    @{ File = "docs\v1.6-calibration-log-template.md"; Patterns = @("Route And Method Evidence Audit", "Section Rhythm Audit", "Visual And Layout Audit", "References", "Section reader lens", "Quantity calibration", "concept-figure-spec.json", "visual_generation_path_wrong", "reference_decorative", "citation_gap", "section_ceremonial", "assumption_not_reused", "result_not_interpreted", "page_band_misclassified", "solution_note_confused_with_paper", "Failure Buckets", "Write-Back Decision", "Calibration Verdict") },
    @{ File = "docs\concept-figure-helper.md"; Patterns = @("scripts/generate-concept-figure.py", "Path B", "concept-figure-spec.json", "New v1.6 run scaffolds", "concept_route.png", "concept_route.svg", "artifact-ledger.md") },
    @{ File = "knowledge\cumcm\v1-6-route-to-paper-structure-index.md"; Patterns = @("Route Structure Matrix", "Paper spine", "First-12-page signal", "Abstract Claim Templates", "Validation close", "First-look failure to avoid") },
    @{ File = "knowledge\cumcm\v1-6-family-calibration-priority.md"; Patterns = @("Priority Families", "Calibration Batch Design", "Route Selection Guard", "Paper-Structure Implication", "Missing-Card Watchlist", "Review Questions") },
    @{ File = "knowledge\algorithms\v1-6-method-chain-evidence-index.md"; Patterns = @("Evidence-Oriented Method Chain Matrix", "support diagnosis", "main model", "result artifact", "validation artifact", "Route Rejection Rules") },
    @{ File = "knowledge\latex\v1-6-layout-rhythm-rules.md"; Patterns = @("Page Rhythm Targets", "Abstract Page Target", "Symbol Section Compaction", "Table Safety Rules", "Overfull Box Policy") },
    @{ File = "knowledge\latex\v1-6-section-rhythm-soft-metrics.md"; Patterns = @("Section Soft Metrics", "Per-Subquestion Loop Target", "Page Economy Rules", "first 12 pages", "route choice", "result artifact", "validation or limitation") },
    @{ File = "knowledge\latex\v1-6-award-feel-soft-rules.md"; Patterns = @("Title Naming Rules", "Abstract Shape", "Section Duty Rules", "Human Team Prose Rules", "Model Depth Without Fake Complexity", "Self-Review Questions") },
    @{ File = "knowledge\latex\v1-6-reference-and-citation-rhythm.md"; Patterns = @("Reference Count Soft Targets", "Required Citation Roles", "Citation Placement Rhythm", "Decorative Reference Warnings", "Literature Notes Conversion", "Self-Review Questions") },
    @{ File = "knowledge\latex\v1-6-award-paper-quantity-calibration.md"; Patterns = @("Source And Reliability", "Key Calibration Rule", "Page Target Interpretation", "Quantity Soft Indicators", "Scanned-PDF Limitation Rule", "Planning Use", "Review Questions") },
    @{ File = "knowledge\community\v1-6-excellent-paper-reader-lens.md"; Patterns = @("Core Reader Lens", "Section Acceptance Signals", "Human-Team Writing Transfer", "Result And Error Analysis Rule", "Assumption Reuse Rule", "Figure And Table Reader Rule", "Review Questions") },
    @{ File = "knowledge\visuals\v1-6-nature-style-figure-rules.md"; Patterns = @("Nature-Style", "figure-style-spec.md", "grouped zones", "deterministic", "first six pages") },
    @{ File = "knowledge\visuals\v1-6-visual-generation-decision.md"; Patterns = @("Tool Decision Matrix", "Path A", "Path B", "Path C", "External Image Model Polish", "Review Gates") },
    @{ File = "knowledge\quality\v1-6-layout-hard-gates.md"; Patterns = @("Page Rhythm Gate", "Abstract Fill Gate", "Blank Space Gate", "Table Width Gate", "Figure Readability And Style Gate", "Final Source Cleanup Gate", "Resource Link Gate", "Artifact Ledger Consistency Gate", "Title Abstract Consistency Gate", "Unknown verdicts are not allowed", "reviews/layout-v16-check.md", "v1.6 Layout Gate Verdict") },
    @{ File = "prompts\16_launch_v1_6.md"; Patterns = @("Level 0 required reading", "v1.6-design-plan.md", "v1.6-paper-template-contract.md", "v1-6-route-to-paper-structure-index.md", "v1-6-family-calibration-priority.md", "v1-6-method-chain-evidence-index.md", "v1-6-layout-rhythm-rules.md", "v1-6-section-rhythm-soft-metrics.md", "v1-6-award-feel-soft-rules.md", "v1-6-reference-and-citation-rhythm.md", "v1-6-award-paper-quantity-calibration.md", "v1-6-excellent-paper-reader-lens.md", "v1-6-nature-style-figure-rules.md", "v1-6-visual-generation-decision.md", "v1-6-layout-hard-gates.md", "section-rhythm-budget.md", "figure-style-spec.md", "concept-figure-spec.json", "award-feel-checklist.md", "artifact-ledger.md", "cumcm_v16_main.tex", "check-v1.6-final.ps1", "final-v16-check.md", "v1.6 Layout Gate Verdict") },
    @{ File = "paper\templates\cumcm_v16_main.tex"; Patterns = @("cumcm_v16 neutral paper skeleton", "tabularx", "adjustbox", "IfFileExists", "Nature-style", "concept_route.png", "lstlisting") },
    @{ File = "paper\templates\table-safe-snippets.tex"; Patterns = @("tabularx", "adjustbox", "max width", "p{0.24") },
    @{ File = "requirements-lite.txt"; Patterns = @("pypdf", "openpyxl", "seaborn", "scikit-learn", "statsmodels") },
    @{ File = "environment-lite.yml"; Patterns = @("python=3.11", "pypdf", "openpyxl", "seaborn", "statsmodels") },
    @{ File = "pyproject.toml"; Patterns = @("pypdf", "openpyxl", "seaborn", "statsmodels") },
    @{ File = "docs\environment-setup.md"; Patterns = @("scripts\setup.ps1", "scripts\check-env.ps1", ".venv\Scripts\python.exe", "Do not create a new temporary environment") },
    @{ File = "scripts\check-env.ps1"; Patterns = @("PYTHONIOENCODING", "pypdf", "openpyxl", "Environment check passed", "scripts/setup.ps1") },
    @{ File = "scripts\check-v1.6-final.ps1"; Patterns = @("check-env.ps1", "check-v1.5-pdf.ps1", "check-v1.6-layout.ps1", "final-v16-check.md", "PYTHONIOENCODING", "NoFail", "SkipEnv") },
    @{ File = "scripts\check-v1.6-layout.py"; Patterns = @("Page Rhythm Gate", "Abstract Fill Gate", "Blank Space Gate", "Table Width Gate", "Nature-Style Concept Figure Gate", "Raster Figure Manual Review Gate", "Final Source Cleanup Gate", "Resource Link Gate", "Artifact Ledger Consistency Gate", "Title Abstract Consistency Gate", "V16_REQUIRED_REVIEW_GATES", "reviews/layout-v16-check.md", "Concept Figure Placeholder Gate", "Reference Cleanup Gate", "Default English figure text detected", "Dependency Gate", "Required Review Gate") },
    @{ File = "scripts\check-v1.6-layout.ps1"; Patterns = @("PYTHONIOENCODING", "check-v1.6-layout.py", "--pdf", "--tex", "--log", "--review", "--run") },
    @{ File = "scripts\generate-concept-figure.py"; Patterns = @("DEFAULT_SPEC", "write_example", "draw_svg", "figure-style-spec.md", "schematic only", "matplotlib") },
    @{ File = "START_HERE.md"; Patterns = @("prompts/16_launch_v1_6.md", "docs/v1.6-design-plan.md", "v1.6-paper-template-contract.md", "v1-6-route-to-paper-structure-index.md", "v1-6-family-calibration-priority.md", "v1-6-method-chain-evidence-index.md", "cumcm_v16_main.tex", "scripts\check-env.ps1", "v1-6-layout-rhythm-rules.md", "v1-6-section-rhythm-soft-metrics.md", "v1-6-reference-and-citation-rhythm.md", "v1-6-award-paper-quantity-calibration.md", "v1-6-excellent-paper-reader-lens.md", "v1-6-nature-style-figure-rules.md", "v1-6-layout-hard-gates.md", "check-v1.6-static.ps1", "check-v1.6-final.ps1", "v1.6 Layout Gate Verdict") },
    @{ File = "README.md"; Patterns = @("v1.6 layout-and-visual gate layer", "prompts/16_launch_v1_6.md", "docs/v1.6-design-plan.md", "docs/knowledge-coverage-audit-v1.6.md", "docs/v1.6-calibration-roadmap.md", "docs/v1.6-calibration-log-template.md", "docs/concept-figure-helper.md", "v1-6-route-to-paper-structure-index.md", "v1-6-family-calibration-priority.md", "v1-6-method-chain-evidence-index.md", "cumcm_v16_main.tex", "v1-6-layout-rhythm-rules.md", "v1-6-section-rhythm-soft-metrics.md", "v1-6-nature-style-figure-rules.md", "v1-6-visual-generation-decision.md", "v1-6-reference-and-citation-rhythm.md", "v1-6-award-paper-quantity-calibration.md", "v1-6-excellent-paper-reader-lens.md", "concept-figure-spec.json", "v1-6-layout-hard-gates.md", "reviews/final-v16-check.md", "reviews/layout-v16-check.md", "check-v1.6-static.ps1", "check-v1.6-final.ps1") },
    @{ File = "CLAUDE.md"; Patterns = @("v1.6 layout-and-visual gate layer", "prompts/16_launch_v1_6.md", "docs/v1.6-design-plan.md", "v1.6-paper-template-contract.md", "v1-6-route-to-paper-structure-index.md", "v1-6-family-calibration-priority.md", "v1-6-method-chain-evidence-index.md", "cumcm_v16_main.tex", "scripts/check-env.ps1", "v1-6-layout-rhythm-rules.md", "v1-6-section-rhythm-soft-metrics.md", "v1-6-reference-and-citation-rhythm.md", "v1-6-award-paper-quantity-calibration.md", "v1-6-excellent-paper-reader-lens.md", "v1-6-nature-style-figure-rules.md", "v1-6-visual-generation-decision.md", "v1-6-layout-hard-gates.md", "reviews/final-v16-check.md", "reviews/layout-v16-check.md", "check-v1.6-final.ps1", "v1.6 Layout Gate Verdict") },
    @{ File = ".codex\skills\cumcm-paper-generator\SKILL.md"; Patterns = @("Default to v1.6", "prompts/16_launch_v1_6.md", "docs/v1.6-design-plan.md", "v1.6-paper-template-contract.md", "v1-6-route-to-paper-structure-index.md", "v1-6-family-calibration-priority.md", "v1-6-method-chain-evidence-index.md", "cumcm_v16_main.tex", "scripts/check-env.ps1", "v1-6-layout-rhythm-rules.md", "v1-6-section-rhythm-soft-metrics.md", "v1-6-reference-and-citation-rhythm.md", "v1-6-award-paper-quantity-calibration.md", "v1-6-excellent-paper-reader-lens.md", "v1-6-nature-style-figure-rules.md", "v1-6-visual-generation-decision.md", "v1-6-layout-hard-gates.md", "reviews/final-v16-check.md", "reviews/layout-v16-check.md", "v1.6 Layout Gate Verdict") },
    @{ File = "scripts\new-run.ps1"; Patterns = @("v1-6-route-to-paper-structure-index.md", "v1-6-family-calibration-priority.md", "v1-6-method-chain-evidence-index.md", "v1-6-section-rhythm-soft-metrics.md", "concept-figure-spec.json", "Priority family", "Non-human failure to catch", "Support diagnosis", "Paper-visible highlight", "Per-Subquestion Loop Budget", "Paragraph target", "Formula target", "Figure/table target", "Paper spine", "First-12-page signal", "Abstract claim shape", "Validation close", "section-rhythm-budget.md", "figure-style-spec.md", "award-feel-checklist.md", "cumcm_v16_main.tex", "Final Source Cleanup Gate", "Resource Link Gate", "Artifact Ledger Consistency Gate", "Title Abstract Consistency Gate", "v1.6 Layout Gate Verdict", "reviews/layout-v16-check.md", "prompts\16_launch_v1_6.md") },
    @{ File = "scripts\start-current.ps1"; Patterns = @("v1.6 layout-and-visual-gated draft", "prompts/16_launch_v1_6.md", "section-rhythm-budget.md", "figure-style-spec.md", "concept-figure-spec.json", "cumcm_v16_main.tex") }
    @{ File = "docs\README.md"; Patterns = @("v1.6-design-plan.md", "v1.6-paper-template-contract.md", "16_launch_v1_6.md", "v1-6-route-to-paper-structure-index.md", "v1-6-family-calibration-priority.md", "v1-6-method-chain-evidence-index.md", "v1-6-layout-rhythm-rules.md", "v1-6-section-rhythm-soft-metrics.md", "v1-6-reference-and-citation-rhythm.md", "v1-6-award-paper-quantity-calibration.md", "v1-6-excellent-paper-reader-lens.md", "v1-6-nature-style-figure-rules.md", "v1-6-visual-generation-decision.md", "v1-6-layout-hard-gates.md", "v1.6-test-handoff.md", "v1.6-readiness-report.md", "v1.6-release-checklist.md", "v1.6-user-test-feedback-template.md", "v1.6-feedback-triage-matrix.md", "knowledge-coverage-audit-v1.6.md", "v1.6-calibration-roadmap.md", "v1.6-calibration-log-template.md", "concept-figure-helper.md", "check-v1.6-static.ps1", "check-v1.6-final.ps1") },
    @{ File = "prompts\README.md"; Patterns = @("16_launch_v1_6.md", "v1.6 Level 0", "v1.6-paper-template-contract.md", "v1.6 Layout Gate Verdict", "v1-6-route-to-paper-structure-index.md", "v1-6-layout-rhythm-rules.md", "v1-6-nature-style-figure-rules.md", "v1-6-layout-hard-gates.md") },
    @{ File = "knowledge\latex\README.md"; Patterns = @("v1-6-layout-rhythm-rules.md", "v1-6-section-rhythm-soft-metrics.md", "v1-6-award-feel-soft-rules.md", "v1-6-reference-and-citation-rhythm.md", "v1-6-award-paper-quantity-calibration.md", "page-count control", "unsafe tables") },
    @{ File = "knowledge\quality\README.md"; Patterns = @("v1-5-hard-gates.md", "v1-6-layout-hard-gates.md", "page rhythm", "figure readability") },
    @{ File = "knowledge\visuals\README.md"; Patterns = @("v1-6-nature-style-figure-rules.md", "v1-6-visual-generation-decision.md", "code-generated", "externally polished") }
)

foreach ($check in $checks) {
    Test-FileContains -RelativePath $check.File -Patterns $check.Patterns
}

$env:PYTHONIOENCODING = "utf-8"
$env:PYTHONUTF8 = "1"
$venvPython = Join-Path $repoRoot ".venv\Scripts\python.exe"
if (Test-Path -LiteralPath $venvPython) {
    $python = $venvPython
} else {
    $python = "python"
}

& $python -m py_compile (Join-Path $repoRoot "scripts\check-v1.6-layout.py")
if ($LASTEXITCODE -ne 0) {
    Add-Failure "Python syntax check failed for scripts\check-v1.6-layout.py"
}

if ($failures.Count -gt 0) {
    Write-Host "v1.6 static check failed:"
    foreach ($failure in $failures) {
        Write-Host "FAIL: $failure"
    }
    exit 1
}

Write-Host "v1.6 static check passed."
exit 0
