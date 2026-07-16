param(
    [string]$Name = "current",
    [string]$Problem = "",
    [switch]$Force
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$runDir = Join-Path $repoRoot "runs\$Name"
$reviewsDir = Join-Path $repoRoot "reviews"
$figuresDir = Join-Path $repoRoot "paper\figures"
$tablesDir = Join-Path $repoRoot "paper\tables"
$srcDataDir = Join-Path $repoRoot "src\data"
$srcModelsDir = Join-Path $repoRoot "src\models"
$srcFiguresDir = Join-Path $repoRoot "src\figures"
$srcTablesDir = Join-Path $repoRoot "src\tables"

New-Item -ItemType Directory -Force -Path $runDir | Out-Null
New-Item -ItemType Directory -Force -Path $reviewsDir | Out-Null
New-Item -ItemType Directory -Force -Path $figuresDir | Out-Null
New-Item -ItemType Directory -Force -Path $tablesDir | Out-Null
New-Item -ItemType Directory -Force -Path $srcDataDir | Out-Null
New-Item -ItemType Directory -Force -Path $srcModelsDir | Out-Null
New-Item -ItemType Directory -Force -Path $srcFiguresDir | Out-Null
New-Item -ItemType Directory -Force -Path $srcTablesDir | Out-Null

function New-TextFileIfNeeded {
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [Parameter(Mandatory = $true)][string]$Content
    )

    if ((Test-Path $Path) -and (-not $Force)) {
        return
    }

    $parent = Split-Path -Parent $Path
    if ($parent) {
        New-Item -ItemType Directory -Force -Path $parent | Out-Null
    }

    Set-Content -Path $Path -Value $Content -Encoding UTF8
}

function Copy-TemplateIfNeeded {
    param(
        [Parameter(Mandatory = $true)][string]$Source,
        [Parameter(Mandatory = $true)][string]$Destination
    )

    if ((Test-Path $Destination) -and (-not $Force)) {
        return
    }

    Copy-Item -Path $Source -Destination $Destination -Force
}

$problemLine = if ($Problem) { $Problem } else { "Unknown" }
$createdAt = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

$problemProfile = @"
# Problem Profile

Run: $Name
Created: $createdAt
Problem: $problemLine

## Problem Image

Unknown.

## Task Family And Route Signals

- Unknown.

## Modeled Object

Unknown.

## Decision Object

Unknown.

## Question Map

- Unknown.

## Evidence Burden

- Unknown.

## Visual Burden

- Unknown.

## Thinness Risks

- Unknown.

## Fake-Completion Risks

- Unknown.
"@

$problemAnalysis = @"
# Problem Analysis

Run: $Name
Created: $createdAt
Problem: $problemLine

## Problem Summary

Unknown.

## Subquestions

1. Unknown.

## Inputs

- Unknown.

## Outputs

- Unknown.

## Constraints

- Unknown.

## Evaluation Metrics

- Unknown.

## Routing Signals

- Unknown.

## Team-Execution Reading

Read `knowledge/community/contest-workflow-and-team-execution.md` before filling this section.

| Role | What this run needs from the role | Evidence file or section |
|---|---|---|
| Modeling role | problem abstraction, route choice, assumptions, formulas, validation logic | Unknown |
| Programming role | data cleaning, numerical solution, generated figures/tables, reproducible scripts | Unknown |
| Writing role | section rhythm, abstract rewrite, result interpretation, final polish | Unknown |

## Risks and Missing Information

- Unknown.

## Questions for Human Confirmation

- None yet.
"@

$dataInventory = @"
# Data Inventory

Run: $Name
Created: $createdAt

| ID | File | Description | Fields | Units | Risks |
|---|---|---|---|---|---|
| D01 | Unknown | Unknown | Unknown | Unknown | Unknown |

## Cleaning Plan

- Unknown.

## Data Risks

- Unknown.
"@

$modelCandidates = @"
# Model Candidates

Run: $Name

Read `prompts/01_ideation.md` before completing this file.

## Candidate 1

Problem type:
Model chain:
Expected figures:
Expected tables:
Validation:
Risks:

## Candidate 2

Problem type:
Model chain:
Expected figures:
Expected tables:
Validation:
Risks:

## Candidate 3

Problem type:
Model chain:
Expected figures:
Expected tables:
Validation:
Risks:

## Recommendation

Recommended route:
Why selected:
Rejected alternatives:
"@

$routeDecision = @"
# Route Decision

Run: $Name

Read `knowledge/algorithms/route-selection-protocol.md` and `prompts/01_ideation.md` before completing this file.

## Selected Route Family

Unknown.

## Question Map

- Unknown.

## Route Chain By Subquestion

### Subquestion 1

Chain:

## Why This Route Fits The Decision Object

- Unknown.

## Why Rejected Routes Are Weaker

- Unknown.

## Required Evidence Chain

- Unknown.

## Required Visuals

- Unknown.

## Expected Failure Modes

- Unknown.
"@

$modelPlan = @"
# Model Plan

Run: $Name

Read `prompts/02_model_plan.md` before completing this file.

## Team Execution Plan

Read `knowledge/community/contest-workflow-and-team-execution.md` before completing this section.

| Role | Planned contribution | Output artifact |
|---|---|---|
| Modeling | problem abstraction, route chain, equations, validation | `problem-analysis.md`, `route-decision.md`, model sections |
| Programming | data processing, solver scripts, generated tables/figures | `src/`, `paper/tables/`, `paper/figures/`, `artifact-ledger.md` |
| Writing | section rhythm, result interpretation, abstract rewrite, review response | `section-budget.md`, `writing-style-plan.md`, `paper/main.tex`, review |

## Page Structure Plan

| Section | Target pages | Notes |
|---|---:|---|
| Abstract | 1 | Write last |
| Problem restatement | 1-2 | |
| Problem analysis | 2-4 | |
| Assumptions and symbols | 1-2 | |
| Data processing | 2-4 | |
| Model and solution | 8-14 | |
| Results and validation | 3-5 | |
| Strengths, limitations, conclusion | 2-3 | |

## v1.4 Section Duty Notes

Read `knowledge/community/section-duty-soft-rules.md` and ensure every standard section has a real job before drafting.

| Section | Duty | Main evidence/artifact |
|---|---|---|
| Abstract | method-result closure for every major subquestion | |
| Problem analysis | route logic and output form | |
| Model/solution | formulas, code path, and result production | |
| Results/validation | answer artifacts and trust checks | |

## Subquestion Models

### Subquestion 1

Model chain:
Variables:
Objective/target:
Constraints/equations:
Solver/algorithm:
Expected outputs:
"@

$methodDepthPlan = @"
# Method Depth Plan

Run: $Name

Read `knowledge/algorithms/method-depth-ladder.md` and `prompts/02_model_plan.md` before completing this file.

## Depth Target

- target version: v1.2
- minimum target depth for major subquestions: Level 3
- preferred target for award-competitive sections: Level 4 when the route supports it

## Subquestion Depth Map

| Subquestion | Support layer | Main model | Result artifact | Validation/comparison layer | Current depth |
|---|---|---|---|---|---|
| Q1 | fill | fill | fill | fill | fill |
| Q2 | fill | fill | fill | fill | fill |
| Q3 | fill | fill | fill | fill | fill |

## Upgrade Triggers

- If a row still reads like `single method -> single result`, upgrade it.
- If a decision artifact has no feasibility or scenario check, upgrade it.
- If a forecast drives a later recommendation, record the propagation path.

## Thinness Risks

- Which subquestion is most likely to stop too early?
- Which subquestion most needs a comparison or baseline?
- Which support layer is easiest to forget?
"@

$verificationPlan = @"
# Verification Plan

Run: $Name

| ID | Target | Method | Metric | Evidence file | Status |
|---|---|---|---|---|---|
| V01 | Unknown | Unknown | Unknown | Unknown | Planned |

## Sensitivity Analysis

- Unknown.

## Baseline or Sanity Checks

- Unknown.
"@

$methodologyChecklist = @"
# Methodology Checklist

Run: $Name

Read `docs/v1.3-methodology-runbook.md` and `prompts/02_model_plan.md` before completing this file.

## Stable Question Map

- Unknown.

## Modeled Object

Unknown.

## Decision Object

Unknown.

## Object-First Figure

- Unknown.

## Route Chain By Subquestion

| Subquestion | Route chain | Decision closure |
|---|---|---|
| Q1 | fill | fill |

## Minimum Validation Artifacts

| Subquestion | Validation artifact | Comparison artifact |
|---|---|---|
| Q1 | fill | fill |

## Abstract Claim Boundary

- Unknown.

## Conclusion Claim Boundary

- Unknown.

## Thinness Risks

- Unknown.

## Machine-Like Rhythm Risks

- Unknown.

## v1.4 Team Execution Signals

Read `knowledge/community/contest-workflow-and-team-execution.md` before completing this section.

| Signal | Planned evidence |
|---|---|
| modeling role explains route fit before algorithm names | Unknown |
| programming role produces body-critical tables/figures | Unknown |
| writing role rewrites abstract after result artifacts stabilize | Unknown |
| final paper centralizes answers before appendix code | Unknown |
| each major subquestion closes with result plus credibility sentence | Unknown |
"@

$onlineConsensusNotes = @"
# Online Consensus Notes

Run: $Name
Created: $createdAt

Read `docs/online-consensus-check-protocol.md`, `docs/online-consensus-weak-strong-examples.md`, and `prompts/11_online_consensus_check.md` before completing this file.

Minimum quality gate:

- record searched queries or platform attempts;
- classify source quality;
- include route reflection;
- reject or discount at least one weak/unsafe signal when encountered;
- record remaining uncertainty;
- do not treat popularity as proof or copy final answers.

## Search Scope

- Not started.

## Source Table

| Source | Platform | Quality | Signal | Used? |
|---|---|---|---|---|
| Not started | Not started | Not started | Not started | Not started |

## Common Interpretations

- Not started.

## Common Methods

- Not started.

## Rough Result Ranges

- Not started.

## Warnings And Traps

- Not started.

## Route Reflection

- Not started.

## What Changed

- Not started.

| Signal type | Run file changed | Change made | Reason |
|---|---|---|---|
| interpretation/trap/artifact/validation/writing/result-range | Not started | Not started | Not started |

## What Was Rejected

- Not started.

## Remaining Uncertainty

- Not started.

## v1.4 Search Order Check

- General contest-circle experience searched before exact problem discussion: Unknown.
- Exact-problem signals used only after initial route-decision: Unknown.
- Popularity was not treated as proof: Unknown.
"@

$literatureNotes = @"
# Literature Notes

Run: $Name
Created: $createdAt

Read `knowledge/community/literature-search-and-citation-rules.md` before completing this file.

## Search Purpose

- domain vocabulary: Unknown.
- variable definitions: Unknown.
- method candidates: Unknown.
- data-source hints: Unknown.
- validation ideas: Unknown.
- citation requirements: Unknown.

Do not use this note to collect final answers or copied solution text.

## Source Table

| Source | Type | Role | Extracted idea | Used in run file | Citation needed? |
|---|---|---|---|---|---|
| Unknown | method/data/domain/validation/software | Unknown | Unknown | Unknown | Unknown |

## Depth-First Source Trail

| Anchor source | What it simplifies | Main variables | Method chain | Validation style | Follow-up references or method names |
|---|---|---|---|---|---|
| Unknown | Unknown | Unknown | Unknown | Unknown | Unknown |

## Run-File Conversions

| Signal | Run file changed | Change made | Reason |
|---|---|---|---|
| Unknown | Unknown | Unknown | Unknown |

## Citation Duties

| Citation duty | Planned source | Paper location |
|---|---|---|
| method | Unknown | Unknown |
| data | Unknown | Unknown |
| domain | Unknown | Unknown |
| validation | Unknown | Unknown |
| software | Unknown | Unknown |

## Rejected Or Deferred Sources

| Source | Reason rejected or deferred |
|---|---|
| Unknown | Unknown |

## Review Gate

- no source is used as copied solution text: Unknown.
- method/data/domain/validation claims have citation support or are marked unsupported: Unknown.
- decorative references are removed: Unknown.
- unresolved placeholders remain visibly marked: Unknown.
- literature signals and online-consensus signals are not mixed together: Unknown.
"@

$reviewCurrent = @"
# Paper Quality Review

Run: $Name
Reviewed: $createdAt

## Overall Status

Needs revision

## Critical Findings

| ID | Location | Status | Evidence | Risk | Required repair |
|---|---|---|---|---|---|

## Important Findings

| ID | Location | Status | Evidence | Risk | Required repair |
|---|---|---|---|---|---|

## Warnings

| ID | Location | Status | Evidence | Risk | Suggested repair |
|---|---|---|---|---|---|

## Evidence Checked

- Not reviewed yet.

## Evidence Missing Or Not Checked

- PDF compile and rendered-page inspection.
- Artifact ledger consistency.
- Problem coverage.
- Model validation.

## Required Repairs Before Pass

1. Run `prompts/06_quality_review.md` after paper generation.

## Human Verification Needed

- Confirm research-only use context.

## Responsible-Use Notes

- Generated drafts must not be used for active contest rule violations or fabricated evidence.
"@

New-TextFileIfNeeded -Path (Join-Path $runDir "problem-profile.md") -Content $problemProfile
New-TextFileIfNeeded -Path (Join-Path $runDir "problem-analysis.md") -Content $problemAnalysis
New-TextFileIfNeeded -Path (Join-Path $runDir "data-inventory.md") -Content $dataInventory
New-TextFileIfNeeded -Path (Join-Path $runDir "model-candidates.md") -Content $modelCandidates
New-TextFileIfNeeded -Path (Join-Path $runDir "route-decision.md") -Content $routeDecision
New-TextFileIfNeeded -Path (Join-Path $runDir "model-plan.md") -Content $modelPlan
New-TextFileIfNeeded -Path (Join-Path $runDir "method-depth-plan.md") -Content $methodDepthPlan
New-TextFileIfNeeded -Path (Join-Path $runDir "verification-plan.md") -Content $verificationPlan
New-TextFileIfNeeded -Path (Join-Path $runDir "methodology-checklist.md") -Content $methodologyChecklist
New-TextFileIfNeeded -Path (Join-Path $runDir "online-consensus-notes.md") -Content $onlineConsensusNotes
New-TextFileIfNeeded -Path (Join-Path $runDir "literature-notes.md") -Content $literatureNotes

Copy-TemplateIfNeeded -Source (Join-Path $repoRoot "docs\artifact-ledger-template.md") -Destination (Join-Path $runDir "artifact-ledger.md")
Copy-TemplateIfNeeded -Source (Join-Path $repoRoot "docs\figure-plan-template.md") -Destination (Join-Path $runDir "figure-plan.md")
Copy-TemplateIfNeeded -Source (Join-Path $repoRoot "docs\section-budget-template.md") -Destination (Join-Path $runDir "section-budget.md")
Copy-TemplateIfNeeded -Source (Join-Path $repoRoot "docs\writing-style-plan-template.md") -Destination (Join-Path $runDir "writing-style-plan.md")
New-TextFileIfNeeded -Path (Join-Path $reviewsDir "review-$Name.md") -Content $reviewCurrent

Write-Host "Created run scaffold: $runDir"
Write-Host "Next step: follow prompts\00_intake.md and fill the v1.2/v1.3 planning files before drafting."
