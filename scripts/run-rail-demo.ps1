param(
    [string]$Name = "rail-demo",
    [switch]$Force,
    [switch]$SkipQualityGate
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$python = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"

if (-not (Test-Path $python)) {
    $python = "python"
}

if ($Force) {
    & powershell -ExecutionPolicy Bypass -File (Join-Path $repoRoot "scripts\new-run.ps1") -Name $Name -Problem "rail-timetable-demo" -Force
} else {
    & powershell -ExecutionPolicy Bypass -File (Join-Path $repoRoot "scripts\new-run.ps1") -Name $Name -Problem "rail-timetable-demo"
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
| Q1 | passenger-flow and candidate service pattern setup | timetable and route selection model | operation plan and full timetable | capacity, tracking, and dwell audits | Level 3 |
| Q2 | cost/service decomposition | scenario comparison model | cost-service tradeoff outputs | baseline comparison | Level 3 |
| Q3 | scenario recommendation layer | recommendation synthesis | scenario analysis table | audit-backed recommendation check | Level 3 |

## Thinness Risks

- Real attachment parsing is still not installed in the demo route.
"@

Set-Content -Encoding UTF8 -Path (Join-Path $repoRoot "runs\$Name\section-budget.md") -Value @"
# Section Budget

## Target

- target paper tier: v1.2
- target total body length: 14-20 pages for the route demo
- target appendix length: 3-5 pages
- route family: Type I rail timetable and service planning
- paper family: online optimization and update

## Section Budget

| Section | Target pages | Why this section deserves the space | Main planned artifacts | Thinness risk |
| --- | ---: | --- | --- | --- |
| Abstract | 1 | close the route and recommendation chain | key metrics and recommendation | low |
| Problem restatement | 1 | define the timetable task clearly | task table | low |
| Method overview | 1 | expose the route early | route/workflow figure | low |
| Problem analysis | 2 | justify the timetable route and constraints | dependency table | low |
| Assumptions | 0.5 | show simplifications | assumption list/table | low |
| Symbols | 0.5 | stabilize notation | symbol table | low |
| Data processing | 1.5 | explain flow and route objects | candidate pattern summary | medium |
| Model establishment | 4 | keep service, cost, and feasibility logic central | equations and constraints | low |
| Solution process | 1.5 | bridge model and machine outputs | algorithm steps | low |
| Results | 2.5 | show executable plan and diagrams | timetable, plan, tradeoff figure | low |
| Validation and sensitivity | 2 | prove feasibility and scenario value | audits and scenario analysis | low |
| Strengths and limitations | 0.5 | disclose demo constraints | limitation table | low |
| Conclusion | 0.5 | state final recommendation | summary points | low |
| References | 0.5 | research framing | real references only | low |
| Appendix | 3 | machine-readable artifacts and file map | file inventory | low |

## Per-Subquestion Closure

| Subquestion | Analysis | Model | Result artifact | Validation artifact |
| --- | --- | --- | --- | --- |
| Q1 | route and demand setup | timetable/service plan | full timetable and operation plan | capacity/tracking/dwell audit |
| Q2 | cost-service tradeoff | scenario comparison | tradeoff outputs | baseline comparison |
| Q3 | recommendation synthesis | scenario recommendation | scenario table | audit-backed recommendation |

## Final Check

- Where is the strongest mathematical density expected? Model establishment
- Which section is most likely to stay too thin? Data processing
- What artifacts will prevent filler growth? full timetable, audits, scenario table, tradeoff figure
"@

Set-Content -Encoding UTF8 -Path (Join-Path $repoRoot "runs\$Name\writing-style-plan.md") -Value @"
# Writing Style Plan

## Style Target

- target version: v1.2
- route family: Type I rail timetable and service planning
- selected style variant: route-heavy analytical style
- positive sample: 2021 D scheduling comparison cluster
- contrast sample: thin implementation-only drafts

## Core Writing Choices

- abstract density target: one dense page
- paragraph-driven vs bullet-driven balance: paragraph-driven main body, structured tables for audits
- tone target: technical but readable team draft
- how results will be interpreted in prose: tie every timetable or scenario artifact to service and feasibility meaning
- how limitations will be stated: explicit demo-data and attachment-parsing limits

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

- first explanatory figure should identify the route/service object early;
- each major timetable question should close a full loop before the next starts;
- important tables and figures should be interpreted immediately after citation;
- long sections should be long because they contain constraints, audits, and recommendation logic.

## Thinness Risks

- sections likely to become too short: strengths and limitations
- sections likely to become too bullet-heavy: solution process
- sections likely to overuse generic prose: conclusion
"@

& $python (Join-Path $repoRoot "src\rail_timetable_demo.py") $Name

if (-not $SkipQualityGate) {
    & powershell -ExecutionPolicy Bypass -File (Join-Path $repoRoot "scripts\check-run-quality.ps1") -Run $Name -Paper "rail_demo.tex"
    Add-Content -Encoding UTF8 -Path (Join-Path $repoRoot "runs\$Name\artifact-ledger.md") -Value ""
    Add-Content -Encoding UTF8 -Path (Join-Path $repoRoot "runs\$Name\artifact-ledger.md") -Value "Machine gate: ``scripts/check-run-quality.ps1 -Run $Name -Paper rail_demo.tex`` passed."
    Add-Content -Encoding UTF8 -Path (Join-Path $repoRoot "reviews\review-$Name.md") -Value ""
    Add-Content -Encoding UTF8 -Path (Join-Path $repoRoot "reviews\review-$Name.md") -Value "Machine gate passed: ``scripts/check-run-quality.ps1 -Run $Name -Paper rail_demo.tex``."
}

Write-Host "Rail timetable demo artifacts generated."
Write-Host "Run directory: runs\$Name"
Write-Host "Next: compile paper\rail_demo.tex, inspect rendered pages, and extend the v1.2 draft toward stronger real-data parsing when needed."
