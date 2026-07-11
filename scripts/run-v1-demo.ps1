param(
    [string]$Name = "current",
    [switch]$Force,
    [switch]$InstallAsActiveProblem,
    [switch]$SkipQualityGate
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$python = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"

if (-not (Test-Path $python)) {
    $python = "python"
}

$problemSource = Join-Path $repoRoot "problems\demo-v1-supply.md"
$problemTarget = Join-Path $repoRoot "problems\problem.md"

if ($InstallAsActiveProblem -and ((-not (Test-Path $problemTarget)) -or $Force)) {
    Copy-Item -Path $problemSource -Destination $problemTarget -Force
}

if ($Force) {
    & powershell -ExecutionPolicy Bypass -File (Join-Path $repoRoot "scripts\new-run.ps1") -Name $Name -Problem "demo-v1-supply" -Force
} else {
    & powershell -ExecutionPolicy Bypass -File (Join-Path $repoRoot "scripts\new-run.ps1") -Name $Name -Problem "demo-v1-supply"
}

Set-Content -Encoding UTF8 -Path (Join-Path $repoRoot "runs\$Name\method-depth-plan.md") -Value @"
# Method Depth Plan

Run: $Name

## Depth Target

- target version: v1.2
- minimum target depth for major subquestions: Level 3

## Subquestion Depth Map

| Subquestion | Support layer | Main model | Result artifact | Validation/comparison layer | Current depth |
|---|---|---|---|---|---|
| Q1 | material screening and short-term forecast checks | rolling production planning | production plan table and service-level summary | scenario comparison and fulfillment check | Level 3 |

## Thinness Risks

- Demo data remain synthetic, so route realism is still limited.
"@

Set-Content -Encoding UTF8 -Path (Join-Path $repoRoot "runs\$Name\section-budget.md") -Value @"
# Section Budget

## Target

- target paper tier: v1.2
- target total body length: 12-16 pages for the synthetic demo
- target appendix length: 2-4 pages
- route family: production-route E
- paper family: forecast to decision

## Section Budget

| Section | Target pages | Why this section deserves the space | Main planned artifacts | Thinness risk |
| --- | ---: | --- | --- | --- |
| Abstract | 1 | summarize route and key outputs | summary metrics | low |
| Problem restatement | 1 | translate the task into production decisions | task table | low |
| Method overview | 1 | show forecast-to-decision chain early | workflow figure | low |
| Problem analysis | 2 | justify the production-route E choice | route explanation table | medium |
| Assumptions | 0.5 | make demo simplifications visible | assumption table | low |
| Symbols | 0.5 | keep variables stable | symbol table | low |
| Data processing | 2 | explain synthetic inputs and demand shaping | demand and material summary tables | low |
| Model establishment | 3 | keep the planning equations and rules central | equations and planning logic | low |
| Solution process | 1 | connect scripts to outputs | algorithm steps | low |
| Results | 2 | show the executable plan | production table and result figures | low |
| Validation and sensitivity | 1.5 | prove the plan is not arbitrary | scenario comparison and service checks | low |
| Strengths and limitations | 0.5 | disclose demo constraints | limitation table | low |
| Conclusion | 0.5 | give final recommendation | key result summary | low |
| References | 0.5 | keep research framing visible | real references only | low |
| Appendix | 2 | trace scripts and outputs | file inventory | low |

## Per-Subquestion Closure

| Subquestion | Analysis | Model | Result artifact | Validation artifact |
| --- | --- | --- | --- | --- |
| Q1 | material screening and demand pattern | rolling production rule | production plan and service levels | scenario comparison |

## Final Check

- Where is the strongest mathematical density expected? Model establishment
- Which section is most likely to stay too thin? Problem analysis
- What artifacts will prevent filler growth? production plan table, forecast comparison, service-level figure, scenario table
"@

Set-Content -Encoding UTF8 -Path (Join-Path $repoRoot "runs\$Name\writing-style-plan.md") -Value @"
# Writing Style Plan

## Style Target

- target version: v1.2
- route family: production-route E
- selected style variant: evidence-dense research style
- positive sample: 2022 E014 / 2022 E029 route family
- contrast sample: thin forecast-only drafts

## Core Writing Choices

- abstract density target: one dense page
- paragraph-driven vs bullet-driven balance: paragraph-driven main body, tables for structured evidence
- tone target: calm analytical team draft
- how results will be interpreted in prose: explain what each production or service artifact means for decisions
- how limitations will be stated: explicit demo-data limits and next realism steps

## Section Notes

| Section | Intended feel | What must not happen |
| --- | --- | --- |
| Abstract | dense, method-result closure | half-page summary, method names without results |
| Problem analysis | route-aware, comparative | restatement padding |
| Model establishment | technical and explanatory | prestige algorithm stacking |
| Results | evidence plus interpretation | artifact dumping |
| Validation | calm and explicit | one-sentence token check |
| Conclusion | concise and numeric | new methods or unsupported claims |

## Human-Team Soft Rules

- first explanatory figure should identify the production route early;
- the single demo subquestion should still close a full loop before conclusion;
- important tables and figures should be interpreted immediately after citation;
- long sections should be long because they contain equations, artifacts, and validation, not repeated narration.

## Thinness Risks

- sections likely to become too short: problem analysis
- sections likely to become too bullet-heavy: solution process
- sections likely to overuse generic prose: strengths and limitations
"@

& $python (Join-Path $repoRoot "src\demo_v1.py") $Name

if (-not $SkipQualityGate) {
    & powershell -ExecutionPolicy Bypass -File (Join-Path $repoRoot "scripts\check-run-quality.ps1") -Run $Name
    Add-Content -Encoding UTF8 -Path (Join-Path $repoRoot "runs\$Name\artifact-ledger.md") -Value ""
    Add-Content -Encoding UTF8 -Path (Join-Path $repoRoot "runs\$Name\artifact-ledger.md") -Value "Machine gate: ``scripts/check-run-quality.ps1 -Run $Name`` passed."
    Add-Content -Encoding UTF8 -Path (Join-Path $repoRoot "reviews\review-$Name.md") -Value ""
    Add-Content -Encoding UTF8 -Path (Join-Path $repoRoot "reviews\review-$Name.md") -Value "Machine gate passed: ``scripts/check-run-quality.ps1 -Run $Name``."
}

Write-Host "Demo v1.2-style artifacts generated."
Write-Host "Demo problem source: problems\demo-v1-supply.md"
Write-Host "Next: fill paper sections using docs\v1.2-runbook.md, then compile and review."
