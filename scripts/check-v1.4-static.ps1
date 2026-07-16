param(
    [switch]$SkipScaffold
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$failures = New-Object System.Collections.Generic.List[string]
$warnings = New-Object System.Collections.Generic.List[string]

function Add-Failure {
    param([string]$Message)
    $failures.Add($Message) | Out-Null
}

function Add-Warning {
    param([string]$Message)
    $warnings.Add($Message) | Out-Null
}

function Test-RepoPath {
    param([string]$RelativePath)
    $path = Join-Path $repoRoot $RelativePath
    if (-not (Test-Path -LiteralPath $path)) {
        Add-Failure "Missing file: $RelativePath"
        return $false
    }
    return $true
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

function Test-FileNotContainsRegex {
    param(
        [string]$RelativePath,
        [string]$Pattern
    )

    $path = Join-Path $repoRoot $RelativePath
    if (-not (Test-Path -LiteralPath $path)) {
        return
    }

    $matches = Select-String -Path $path -Pattern $Pattern -Encoding UTF8
    foreach ($match in $matches) {
        Add-Warning "Possible mojibake in ${RelativePath}:$($match.LineNumber)"
    }
}

$requiredFiles = @(
    "docs\v1.4-definition.md",
    "docs\v1.4-community-learning-plan.md",
    "docs\community-signal-to-rule-pipeline.md",
    "docs\playwright-mcp-public-research.md",
    "docs\local-experience-extraction-queue.md",
    "docs\local-experience-extraction-status.md",
    "docs\v1.4-runbook.md",
    "docs\v1.4-sync-manifest.md",
    "docs\v1.4-release-notes.md",
    "docs\v1.4-release-checklist.md",
    "docs\v1.4-readiness-report.md",
    "docs\v1.4-test-handoff.md",
    "docs\v1.4-user-test-protocol.md",
    "docs\v1.4-user-test-feedback-template.md",
    "docs\v1.4-feedback-triage-matrix.md",
    "docs\online-consensus-check-protocol.md",
    "docs\online-consensus-example-template.md",
    "docs\online-consensus-weak-strong-examples.md",
    "docs\literature-notes-template.md",
    "docs\figure-plan-template.md",
    "docs\artifact-ledger-template.md",
    "docs\section-budget-template.md",
    "scripts\probe-binary-office-text.py",
    "prompts\11_online_consensus_check.md",
    "prompts\12_launch_v1_4.md",
    "prompts\13_platform_research.md",
    "knowledge\community\math-modeling-soft-rules.md",
    "knowledge\community\contest-workflow-and-team-execution.md",
    "knowledge\community\literature-search-and-citation-rules.md",
    "knowledge\community\section-duty-soft-rules.md",
    "knowledge\community\visual-evidence-chain-rules.md",
    "knowledge\community\paper-polish-and-feel.md",
    "knowledge\community\award-paper-section-rhythm.md",
    "knowledge\community\public-community-source-playbook.md",
    "knowledge\community\common-mistakes-and-taboo-phrases.md",
    "knowledge\community\source-quality-rubric.md",
    "knowledge\community\local-experience-absorption-log.md",
    "knowledge\cumcm\recent-award-paper-visual-rhythm.md",
    "knowledge\cumcm\v1-4-section-proportion-and-reference-rules.md",
    "knowledge\latex\v1-4-paper-composition-rules.md",
    "knowledge\latex\v1-4-abstract-closeout-rules.md",
    "knowledge\quality\v1-4-human-feel-review-gate.md"
)

foreach ($file in $requiredFiles) {
    Test-RepoPath $file | Out-Null
}

$entryChecks = @(
    @{ File = "README.md"; Patterns = @("prompts/12_launch_v1_4.md", "prompts/13_platform_research.md", "docs/playwright-mcp-public-research.md", "Playwright MCP public research", "docs/community-signal-to-rule-pipeline.md", "docs/v1.4-release-notes.md", "docs/v1.4-readiness-report.md", "docs/v1.4-test-handoff.md", "docs/v1.4-user-test-protocol.md", "docs/v1.4-feedback-triage-matrix.md", "knowledge/community/visual-evidence-chain-rules.md", "knowledge/latex/v1-4-abstract-closeout-rules.md") },
    @{ File = "START_HERE.md"; Patterns = @("prompts/12_launch_v1_4.md", "prompts/13_platform_research.md", "docs/playwright-mcp-public-research.md", "Playwright MCP public research", "docs/v1.4-community-learning-plan.md", "docs/community-signal-to-rule-pipeline.md", "docs/local-experience-extraction-queue.md", "docs/local-experience-extraction-status.md", "docs/v1.4-release-notes.md", "docs/v1.4-readiness-report.md", "docs/v1.4-test-handoff.md", "docs/v1.4-user-test-feedback-template.md", "docs/v1.4-feedback-triage-matrix.md") },
    @{ File = "docs\README.md"; Patterns = @("v1.4-community-learning-plan.md", "community-signal-to-rule-pipeline.md", "playwright-mcp-public-research.md", "local-experience-extraction-queue.md", "local-experience-extraction-status.md", "v1.4-release-notes.md", "v1.4-readiness-report.md", "v1.4-test-handoff.md", "v1.4-user-test-protocol.md", "v1.4-feedback-triage-matrix.md") },
    @{ File = "docs\v1.4-community-learning-plan.md"; Patterns = @("docs/community-signal-to-rule-pipeline.md", "docs/local-experience-extraction-queue.md", "docs/local-experience-extraction-status.md", "Promote observations by maturity") },
    @{ File = "docs\community-signal-to-rule-pipeline.md"; Patterns = @("Every learned signal must become one of four things", "Absorption Card", "Rule Maturity Levels", "Anti-Overfitting Rule") },
    @{ File = "docs\playwright-mcp-public-research.md"; Patterns = @("Use Playwright MCP", "Browse like a human reviewer", "Do not", "hidden APIs", "Required Output", "Relationship To Prompt 11") },
    @{ File = "docs\local-experience-extraction-queue.md"; Patterns = @("Safe Extraction Protocol", "Priority 1: Writing And Contest Workflow", "Completion Markers", "Current Next Batch", "PDF-First Continuation Batch") },
    @{ File = "docs\local-experience-extraction-status.md"; Patterns = @("2026-07-13 Probe: First Queue Batch", "scripts/probe-binary-office-text.py", "partial", "blocked", "Do not treat these four files as fully absorbed", "PDF Batch: Contest Purpose And Preparation") },
    @{ File = "scripts\probe-binary-office-text.py"; Patterns = @("probe-binary-office-text.py INPUT_DIR OUTPUT_CSV", "readability", "weak-partial") },
    @{ File = "docs\literature-notes-template.md"; Patterns = @("Source Table", "Depth-First Source Trail", "Citation Duties", "literature signals and online-consensus signals are not mixed together") },
    @{ File = "docs\run-file-examples\evaluation-to-planning-demo\literature-notes.md"; Patterns = @("Run family: evaluation-to-planning-demo", "Depth-First Source Trail", "Run-File Conversions", "Citation Duties") },
    @{ File = "docs\run-file-examples\evaluation-to-planning-demo\online-consensus-notes.md"; Patterns = @("Run family: evaluation-to-planning-demo", "Source Table", "What Changed", "Popularity was not treated as proof") },
    @{ File = "docs\sample-run-packages\evaluation-to-planning-demo\package-map.md"; Patterns = @("literature-notes.md", "online-consensus-notes.md", "online-consensus reflection pattern") },
    @{ File = "docs\v1.4-feedback-triage-matrix.md"; Patterns = @("Triage Matrix", "Literature note is missing", "Literature search looks like answer hunting", "References feel padded or irrelevant", "When To Create v1.5 Work") },
    @{ File = "docs\v1.4-test-handoff.md"; Patterns = @("docs/v1.4-feedback-triage-matrix.md", "prompts/13_platform_research.md", "Playwright MCP public research", "do not use cookies") },
    @{ File = "docs\v1.4-readiness-report.md"; Patterns = @("docs/v1.4-feedback-triage-matrix.md") },
    @{ File = "docs\v1.4-user-test-feedback-template.md"; Patterns = @("docs/v1.4-feedback-triage-matrix.md", "Literature And Citation Check", "Triage Mapping") },
    @{ File = "docs\v1.4-user-test-protocol.md"; Patterns = @("literature-notes.md", "Did literature search change run files or citation duties", "prompts/13_platform_research.md", "Playwright MCP public research", "recorded and skipped rather than bypassed") },
    @{ File = "docs\v1.4-release-notes.md"; Patterns = @("prompts/13_platform_research.md", "Playwright MCP public research", "hidden APIs", "app-only content") },
    @{ File = "docs\objective-coverage-matrix.md"; Patterns = @("contest-circle soft rules and award-paper feel", "Literature search and citations", "online-consensus-notes.md", "literature-notes.md") },
    @{ File = "knowledge\cumcm\next-iteration-action-matrix.md"; Patterns = @("Run v1.4 user-side paper tests", "Fill literature-note examples", "Fill online-consensus examples", "Continue local old-format extraction") },
    @{ File = ".codex\skills\cumcm-paper-generator\SKILL.md"; Patterns = @("docs/v1.4-community-learning-plan.md", "docs/community-signal-to-rule-pipeline.md", "docs/playwright-mcp-public-research.md", "prompts/13_platform_research.md", "Playwright MCP", "Do not use cookies", "knowledge/community/contest-workflow-and-team-execution.md", "knowledge/community/literature-search-and-citation-rules.md", "knowledge/community/section-duty-soft-rules.md", "knowledge/community/visual-evidence-chain-rules.md") },
    @{ File = "prompts\12_launch_v1_4.md"; Patterns = @("online-consensus-notes.md", "docs/community-signal-to-rule-pipeline.md", "docs/playwright-mcp-public-research.md", "prompts/13_platform_research.md", "Playwright MCP public browsing phase", "Do not use cookies", "knowledge/community/contest-workflow-and-team-execution.md", "knowledge/community/literature-search-and-citation-rules.md", "knowledge/community/section-duty-soft-rules.md", "knowledge/community/visual-evidence-chain-rules.md", "knowledge/latex/v1-4-abstract-closeout-rules.md") },
    @{ File = "knowledge\community\contest-workflow-and-team-execution.md"; Patterns = @("modeling role", "programming role", "writing role", "abstract rewritten after final result tables are stable", "what/where/how/why", "cross-question dependencies", "file and tool discipline", "72-hour-style CUMCM simulation") },
    @{ File = "knowledge\community\local-experience-absorption-log.md"; Patterns = @("PDF Batch: Contest Purpose, Preparation, And Format Signals", "contest-purpose-analysis.pdf", "mathchina-mcm-training-experience-short.pdf", "DOCX/PPTX Re-Read", "prediction, optimization, and evaluation", "garbled/partial") },
    @{ File = "knowledge\cumcm\problem-understanding-framework.md"; Patterns = @("prediction", "optimization", "evaluation", "Typical answer form", "Evidence burden", "baseline forecast", "feasibility and scenario table", "indicator table and sensitivity table") },
    @{ File = "knowledge\algorithms\route-selection-protocol.md"; Patterns = @("Beginner training", "prediction", "optimization", "evaluation", "Strong route upgrade", "Anti-List Rule") },
    @{ File = "knowledge\community\literature-search-and-citation-rules.md"; Patterns = @("Search is not answer hunting", "Depth-First Search Rule", "Citation Discipline", "Relationship To Online Consensus") },
    @{ File = "prompts\13_platform_research.md"; Patterns = @("Playwright MCP", "public browsing phase", "online-consensus-notes.md", "Do not use cookies", "hidden APIs", "Signal Conversion Rule") },
    @{ File = "prompts\11_online_consensus_check.md"; Patterns = @("Conversion Rule", "figure-plan.md", "artifact-ledger.md", "writing-style-plan.md", "do not overwrite it from scratch") },
    @{ File = "prompts\06_quality_review.md"; Patterns = @("v1.4 Contest-Feel Review", "figure-plan.md", "artifact-ledger.md", "online-consensus", "literature-notes.md") },
    @{ File = "docs\figure-plan-template.md"; Patterns = @("Body-critical?", "Nearby interpretation", "AI-generated") },
    @{ File = "docs\artifact-ledger-template.md"; Patterns = @("Visual Evidence Chain", "Body-critical?", "Nearby interpretation") },
    @{ File = "docs\section-budget-template.md"; Patterns = @("Section Duty Check", "visual-evidence-chain-rules.md") },
    @{ File = "docs\run-start-checklist.md"; Patterns = @("knowledge/community/contest-workflow-and-team-execution.md", "modeling, programming, and writing roles", "abstract rewrite", "what/where/how/why", "cross-question dependency") },
    @{ File = "docs\methodology-checklist-template.md"; Patterns = @("knowledge/community/contest-workflow-and-team-execution.md", "v1.4 Team Execution Signals") },
    @{ File = "docs\writing-style-plan-template.md"; Patterns = @("knowledge/community/contest-workflow-and-team-execution.md", "abstract rewrite timing") },
    @{ File = "scripts\new-run.ps1"; Patterns = @("online-consensus-notes.md", "literature-notes.md", "v1.4 Section Duty Notes", "Signal type", "Team Execution Plan", "v1.4 Team Execution Signals") }
)

foreach ($check in $entryChecks) {
    Test-FileContains -RelativePath $check.File -Patterns $check.Patterns
}

$badChars = @(
    [char]0x93C1,
    [char]0x68F0,
    [char]0x93AC,
    [char]0x7F01,
    [char]0x7481,
    [char]0x70D8,
    [char]0x7359,
    [char]0x5F7F,
    [char]0x77FE,
    [char]0x7049,
    [char]0x59DD,
    [char]0x934F,
    [char]0x9225
)
$mojibakePattern = ($badChars | ForEach-Object { [regex]::Escape([string]$_) }) -join "|"
$filesToScan = @(
    "docs\v1.4-release-checklist.md",
    "docs\v1.4-sync-manifest.md",
    "docs\online-consensus-check-protocol.md",
    "docs\online-consensus-example-template.md",
    "docs\online-consensus-weak-strong-examples.md",
    "prompts\11_online_consensus_check.md",
    "prompts\12_launch_v1_4.md",
    "knowledge\community\local-experience-absorption-log.md",
    "knowledge\cumcm\recent-award-paper-visual-rhythm.md"
)

foreach ($file in $filesToScan) {
    Test-FileNotContainsRegex -RelativePath $file -Pattern $mojibakePattern
}

if (-not $SkipScaffold) {
    $runName = "codex-v14-static-check"
    $runDir = Join-Path $repoRoot "runs\$runName"
    $reviewPath = Join-Path $repoRoot "reviews\review-$runName.md"

    if (Test-Path -LiteralPath $runDir) {
        Add-Warning "Temporary run already exists and was not overwritten: runs\$runName"
    } else {
        & (Join-Path $PSScriptRoot "new-run.ps1") -Name $runName -Force | Out-Null

        $scaffoldChecks = @(
            @{ File = "runs\$runName\online-consensus-notes.md"; Patterns = @("Signal type", "General contest-circle experience", "Popularity was not treated as proof") },
            @{ File = "runs\$runName\literature-notes.md"; Patterns = @("Source Table", "Depth-First Source Trail", "Citation Duties", "online-consensus signals are not mixed together") },
            @{ File = "runs\$runName\figure-plan.md"; Patterns = @("Body-critical?", "Nearby interpretation") },
            @{ File = "runs\$runName\artifact-ledger.md"; Patterns = @("Visual Evidence Chain", "Body-critical?") },
            @{ File = "runs\$runName\section-budget.md"; Patterns = @("Section Duty Check") },
            @{ File = "runs\$runName\problem-analysis.md"; Patterns = @("Team-Execution Reading", "Modeling role", "Programming role", "Writing role") },
            @{ File = "runs\$runName\model-plan.md"; Patterns = @("Team Execution Plan", "v1.4 Section Duty Notes") },
            @{ File = "runs\$runName\methodology-checklist.md"; Patterns = @("v1.4 Team Execution Signals", "abstract after result artifacts stabilize") },
            @{ File = "runs\$runName\writing-style-plan.md"; Patterns = @("Abstract And Conclusion Closure", "artifact-ledger key results", "abstract rewrite timing") }
        )

        foreach ($check in $scaffoldChecks) {
            Test-FileContains -RelativePath $check.File -Patterns $check.Patterns
        }

        Remove-Item -Recurse -Force -LiteralPath $runDir
        if (Test-Path -LiteralPath $reviewPath) {
            Remove-Item -Force -LiteralPath $reviewPath
        }
    }
}

if ($warnings.Count -gt 0) {
    Write-Host "Warnings:"
    foreach ($warning in $warnings) {
        Write-Host "WARN: $warning"
    }
}

if ($failures.Count -gt 0) {
    Write-Host "v1.4 static check failed:"
    foreach ($failure in $failures) {
        Write-Host "FAIL: $failure"
    }
    exit 1
}

Write-Host "v1.4 static check passed."
exit 0
