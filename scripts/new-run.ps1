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

## v1.6 Priority Family

Read `knowledge/cumcm/v1-6-family-calibration-priority.md` before filling this section.

- Primary priority family: Unknown.
- Support family: Unknown.
- Most likely non-human failure: Unknown.

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

Read `knowledge/algorithms/route-selection-protocol.md`, `knowledge/cumcm/v1-6-route-to-paper-structure-index.md`, `knowledge/cumcm/v1-6-family-calibration-priority.md`, and `prompts/01_ideation.md` before completing this file.

## Selected Route Family

Unknown.

## v1.6 Family Calibration

Priority family:

Required body artifact:

Required validation artifact:

Non-human failure to catch:

## v1.6 Paper Structure Conversion

Paper spine:

First-12-page signal:

Abstract claim shape:

Validation close:

First-look failure to avoid:

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

Read `docs/v1.5-method-route-contract.md`, `knowledge/cumcm/national-problem-family-methodology-matrix.md`, `knowledge/cumcm/v1-6-family-calibration-priority.md`, `knowledge/algorithms/v1-5-route-upgrade-atlas.md`, `knowledge/algorithms/v1-6-method-chain-evidence-index.md`, `knowledge/algorithms/route-selection-protocol.md`, and `knowledge/algorithms/method-depth-ladder.md` before completing this file.

## Depth Target

- target version: v1.6
- minimum target depth for major subquestions: Level 3
- preferred target for central decision subquestions: Level 4 when data and time support it

## Subquestion Depth Map

| Subquestion | Family | Support diagnosis | Main model | Result artifact | Validation artifact | Paper-visible highlight | Paper section | Depth |
|---|---|---|---|---|---|---|---|---|
| Q1 | fill | fill | fill | fill | fill | fill | fill | fill |
| Q2 | fill | fill | fill | fill | fill | fill | fill | fill |
| Q3 | fill | fill | fill | fill | fill | fill | fill | fill |

## Method Route Verdict Draft

| Subquestion | Depth Pass/Fail | Evidence artifact | Validation artifact | Repair |
|---|---|---|---|---|
| Q1 | Unknown | Unknown | Unknown | Unknown |

## Upgrade Triggers

- If a row still reads like `single method -> single result`, upgrade it.
- If a decision artifact has no feasibility or scenario check, upgrade it.
- If a forecast drives a later recommendation, record the propagation path.
- If a complex algorithm has no route role, remove it or downgrade the claim.
- If the abstract would claim optimal, stable, accurate, feasible, or robust, point to the validation artifact here first.
- If the route cannot name a body result artifact and validation artifact, reject it before coding.

## Thinness Risks

- Which subquestion is most likely to stop too early?
- Which subquestion most needs a comparison or baseline?
- Which support layer is easiest to forget?
"@

$titleCandidates = @"
# Title Candidates

Run: $Name
Created: $createdAt

Read `knowledge/latex/v1-5-front-matter-rhythm-rules.md` and `knowledge/latex/v1-6-award-feel-soft-rules.md` before completing this file.

Purpose: choose a contest-style paper title before writing `paper/main.tex`.

## Problem Object

- Modeled object:
- Decision object:
- Main method or mechanism:
- Final answer form:

## Candidate Titles

| ID | Candidate title | Pattern | Keep/Reject | Reason |
|---|---|---|---|---|
| T1 | Unknown | Unknown | Unknown | Unknown |
| T2 | Unknown | Unknown | Unknown | Unknown |
| T3 | Unknown | Unknown | Unknown | Unknown |
| T4 | Unknown | Unknown | Unknown | Unknown |
| T5 | Unknown | Unknown | Unknown | Unknown |

## Rejection Checklist

Reject a title if it:

- copies the problem statement;
- sounds like a section heading;
- lacks modeled object;
- lacks modeling action such as prediction, evaluation, optimization, decision, or classification;
- uses AI/process wording;
- hides the final decision object.

## Selected Title

Selected title:

Selected pattern:

Why this title fits:

Risk still to check:
"@

$awardFeelChecklist = @"
# Award Feel Checklist

Run: $Name
Created: $createdAt

Read `knowledge/latex/v1-6-award-feel-soft-rules.md` before completing this file.

Purpose: force the paper to pass the first-look human-team test before drafting.

## Title And Abstract

| Item | Decision | Evidence |
|---|---|---|
| Title names the object, modeling action, decision target, and strongest method signal | Unknown | See title-candidates.md |
| Title avoids generic AI-like naming and ASCII hyphens | Unknown | Unknown |
| Abstract uses opening + per-question + closing rhythm | Unknown | Unknown |
| Abstract reserves 900-1150 extracted Chinese characters | Unknown | Unknown |
| Each subquestion has method, result, and interpretation in the abstract | Unknown | Unknown |

## Body Feel

| Item | Decision | Evidence |
|---|---|---|
| Page 2 enters restatement or analysis without generic background padding | Unknown | Unknown |
| Problem analysis explains route choice and subquestion dependency | Unknown | Unknown |
| Assumptions are useful and tied to model simplification | Unknown | Unknown |
| Model sections include equations, variables, objectives, constraints, or algorithm logic | Unknown | Unknown |
| Result tables and figures are interpreted near where they appear | Unknown | Unknown |
| Validation tests the result instead of only praising the model | Unknown | Unknown |
| Appendix contains key code or a script index mapped to questions | Unknown | Unknown |

## Human-Team Prose Repairs

- Thin paragraph groups to expand:
- Bullet-only passages to convert into prose:
- Missing rejected-route comparisons:
- Missing intuition checks after result tables:
- Strong assumptions requiring risk explanation:
"@

$sectionRhythmBudget = @"
# Section Rhythm Budget

Run: $Name
Created: $createdAt

Read `knowledge/latex/v1-6-layout-rhythm-rules.md` and `knowledge/latex/v1-6-section-rhythm-soft-metrics.md` before completing this file.

Target: keep the full PDF near 26-32 pages while avoiding blank-page inflation.

| Section | Target pages | Paragraph target | Formula target | Figure/table target | Evidence file or section | Compression risk | Status |
|---|---:|---|---|---|---|---|---|
| Abstract | 1 | opening + one method-result paragraph per major question + closing value sentence | optional only if central result needs it | 3+ bold result fragments, 3+ keyword groups | paper/main.tex abstract | too short or spills | Unknown |
| Problem restatement | 1-1.5 | modeled object, decision outputs, constraints rewritten in paper language | optional definitions | object/variable map if complex | paper/main.tex section 1 | copied statement | Unknown |
| Problem analysis | 1.5-2.5 | subquestion dependency, route changes, data traps, output form | route definitions if useful | early concept/mechanism figure or route table | paper/figures/concept_route.png | generic background | Unknown |
| Assumptions and symbols | 1-1.5 | each assumption tied to simplification | symbol definitions only once | compact 2- or 3-column symbol table | paper/main.tex symbols section | half-empty symbol page | Unknown |
| Data preprocessing | 2-3 | source, cleaning, derived variables, traps, exploratory facts | cleaning or transformation formulas | data inventory table plus diagnostic artifact | src/ and paper/tables | field dump | Unknown |
| Model construction | 5-7 | per-question variable, objective, constraint, route justification | 1+ formal block per central subquestion | model route table if needed | model sections | formula pile without story | Unknown |
| Solution process | 3-5 | solver steps, parameter choices, reproducibility | algorithm or iteration definitions | parameter/convergence/decision table | src/ and artifact-ledger.md | code narrative | Unknown |
| Results and interpretation | 4-6 | result, comparison, interpretation for each question | derived result formulas when needed | main answer table or figure near each claim | paper/tables and paper/figures | raw outputs without interpretation | Unknown |
| Validation and sensitivity | 2-3 | perturbation, residual, split, capacity, or feasibility checks | metrics and sensitivity definitions | at least two validation artifacts when data permits | verification-plan.md | praise without evidence | Unknown |
| Evaluation, conclusion, references, appendix | 4-6 | concrete limits, mirrored conclusion, code-to-question mapping | none unless needed | 8-15 references if supported; script index | reviews and appendix | appendix inflation | Unknown |

## Per-Subquestion Loop Budget

| Subquestion | Route choice | Model/formula artifact | Result artifact | Interpretation paragraph | Validation or limitation | Status |
|---|---|---|---|---|---|---|
| Q1 | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown |

## Page Economy Decisions

- Sections to merge if sparse: Unknown.
- Tables that need `tabularx` or `adjustbox`: Unknown.
- Figures that may consume too much vertical space: Unknown.
- Appendix material to keep out of body: Unknown.
"@

$figureStyleSpec = @"
# Figure Style Spec

Run: $Name
Created: $createdAt

Read `knowledge/visuals/v1-6-nature-style-figure-rules.md`, `knowledge/visuals/v1-6-visual-generation-decision.md`, and `docs/concept-figure-helper.md` before generating the early concept/mechanism figure.

## Early Concept Figure

| Field | Plan |
|---|---|
| Figure role | concept / mechanism / model route / result explanation |
| Paper location | first six pages, usually problem analysis or model overview |
| Zones | Unknown |
| Nodes | Unknown |
| Edges | Unknown |
| Highlights | Unknown |
| Style | restrained palette, readable labels, grouped zones |
| Export target | at least 2400 px wide or vector output |
| PDF readability check | Unknown |
| Code-native spec | runs/$Name/concept-figure-spec.json |

## Node Map

| Node | Zone | Role | Label length risk |
|---|---|---|---|
| Unknown | Unknown | Unknown | Unknown |

## Edge Map

| Source | Target | Meaning | Label |
|---|---|---|---|
| Unknown | Unknown | Unknown | Unknown |

## Visual Review Notes

- Text remains readable after PDF insertion: Unknown.
- No default notebook titles remain: Unknown.
- Caption interprets the figure, not just names it: Unknown.
- Figure looks like a problem mechanism, not a project workflow: Unknown.
"@

$conceptFigureSpec = @"
{
  "title": "Model route concept figure",
  "subtitle": "schematic only; numeric evidence must come from code outputs",
  "zones": [
    {
      "id": "data",
      "title": "Data objects"
    },
    {
      "id": "model",
      "title": "Model chain"
    },
    {
      "id": "result",
      "title": "Result artifacts"
    },
    {
      "id": "review",
      "title": "Validation"
    }
  ],
  "nodes": [
    {
      "id": "input",
      "zone": "data",
      "label": "Problem data"
    },
    {
      "id": "features",
      "zone": "data",
      "label": "Derived variables"
    },
    {
      "id": "diagnosis",
      "zone": "model",
      "label": "Support diagnosis"
    },
    {
      "id": "main_model",
      "zone": "model",
      "label": "Main model"
    },
    {
      "id": "answer",
      "zone": "result",
      "label": "Answer table",
      "highlight": true
    },
    {
      "id": "figure",
      "zone": "result",
      "label": "Result figure"
    },
    {
      "id": "check",
      "zone": "review",
      "label": "Sensitivity check",
      "highlight": true
    }
  ],
  "edges": [
    {
      "source": "input",
      "target": "features",
      "label": "clean"
    },
    {
      "source": "features",
      "target": "diagnosis",
      "label": "screen"
    },
    {
      "source": "diagnosis",
      "target": "main_model",
      "label": "formulate"
    },
    {
      "source": "main_model",
      "target": "answer",
      "label": "solve"
    },
    {
      "source": "main_model",
      "target": "figure",
      "label": "visualize"
    },
    {
      "source": "answer",
      "target": "check",
      "label": "verify"
    },
    {
      "source": "figure",
      "target": "check",
      "label": "compare"
    }
  ]
}
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

## v1.5 Hard Gate Verdict

Use knowledge/quality/v1-5-hard-gates.md and reviews/pdf-v15-check.md.

| Gate | Pass/Fail | Evidence | Repair |
|---|---|---|---|
| Title Gate | Unknown | Check runs/$Name/title-candidates.md and PDF title | Unknown |
| Abstract Gate | Unknown | Check page 1, paper/main.tex, and bold result highlights | Unknown |
| Concept Figure Gate | Unknown | Check early problem-analysis/model-flow figure | Unknown |
| Prompt-Language Leak Gate | Unknown | Check `paper/main.tex` and PDF text | Unknown |
| Figure Readability Gate | Unknown | Check rendered PDF figures | Unknown |
| Result Sanity Gate | Unknown | Check result tables, fitted values, sample sizes, and conclusions | Unknown |
| Method Route Depth Gate | Unknown | Check runs/$Name/method-depth-plan.md | Unknown |
| Data Trap Gate | Unknown | Check runs/$Name/data-inventory.md | Unknown |
| Plan-To-Paper Gate | Unknown | Check figure plan, artifact ledger, section budget, and body | Unknown |
| Appendix Code Gate | Unknown | Check appendix code or script index | Unknown |
| PDF Density Gate | Unknown | Check reviews/pdf-v15-check.md | Unknown |
| LaTeX Heading Safety Gate | Unknown | Check paper headings for ASCII hyphens | Unknown |
| Section Density Gate | Unknown | Check source-level section density | Unknown |

## Method Route Verdict

Use docs/v1.5-method-route-contract.md and runs/$Name/method-depth-plan.md.

| Subquestion | Depth Pass/Fail | Evidence artifact | Validation artifact | Repair |
|---|---|---|---|---|
| Q1 | Unknown | Unknown | Unknown | Unknown |
| Q2 | Unknown | Unknown | Unknown | Unknown |
| Q3 | Unknown | Unknown | Unknown | Unknown |

## PDF / Source Check Evidence

Expected command:

    powershell -ExecutionPolicy Bypass -File ./scripts/check-v1.5-pdf.ps1 -Pdf ./paper/main.pdf -Run ./runs/$Name -Tex ./paper/main.tex -Review ./reviews/review-$Name.md

Expected report:

- reviews/pdf-v15-check.md

## v1.6 Layout Gate Verdict

Use knowledge/quality/v1-6-layout-hard-gates.md and reviews/layout-v16-check.md.

| Gate | Pass/Fail | Evidence | Repair |
|---|---|---|---|
| Page Rhythm Gate | Unknown | Check page count and section-rhythm-budget.md | Unknown |
| Abstract Fill Gate | Unknown | Check page 1 extracted chars and visual fill | Unknown |
| Blank Space Gate | Unknown | Check low-density pages and symbol section | Unknown |
| Table Width Gate | Unknown | Check LaTeX log and rendered tables | Unknown |
| Figure Readability And Style Gate | Unknown | Check rendered figures for readability and boxes | Unknown |
| Nature-Style Concept Figure Gate | Unknown | Check figure-style-spec.md and first six pages | Unknown |
| Final Source Cleanup Gate | Unknown | Check paper/main.tex for placeholders and prompt leakage | Unknown |
| Resource Link Gate | Unknown | Check TeX input/include/includegraphics paths | Unknown |
| Artifact Ledger Consistency Gate | Unknown | Check runs/$Name/artifact-ledger.md against paper artifacts | Unknown |
| Title Abstract Consistency Gate | Unknown | Check title-candidates.md, abstract structure, bold results, and keywords | Unknown |

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
- reviews/pdf-v15-check.md.
- reviews/layout-v16-check.md.
- Artifact ledger consistency.
- Problem coverage.
- Model validation.

## Required Repairs Before Pass

1. Run prompts/06_quality_review.md after paper generation.
2. Run the v1.5 PDF/source/run-file check and copy failures into this review.
3. Run the v1.6 layout check and copy failures into this review.
4. Mark every v1.5 hard gate Pass or Fail with concrete evidence.
5. Mark every v1.6 layout gate Pass or Fail with concrete evidence.
6. Mark every central subquestion in Method Route Verdict.

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
New-TextFileIfNeeded -Path (Join-Path $runDir "award-feel-checklist.md") -Content $awardFeelChecklist
New-TextFileIfNeeded -Path (Join-Path $runDir "section-rhythm-budget.md") -Content $sectionRhythmBudget
New-TextFileIfNeeded -Path (Join-Path $runDir "figure-style-spec.md") -Content $figureStyleSpec
New-TextFileIfNeeded -Path (Join-Path $runDir "concept-figure-spec.json") -Content $conceptFigureSpec
New-TextFileIfNeeded -Path (Join-Path $runDir "verification-plan.md") -Content $verificationPlan
New-TextFileIfNeeded -Path (Join-Path $runDir "methodology-checklist.md") -Content $methodologyChecklist
New-TextFileIfNeeded -Path (Join-Path $runDir "online-consensus-notes.md") -Content $onlineConsensusNotes
New-TextFileIfNeeded -Path (Join-Path $runDir "literature-notes.md") -Content $literatureNotes

Copy-TemplateIfNeeded -Source (Join-Path $repoRoot "docs\artifact-ledger-template.md") -Destination (Join-Path $runDir "artifact-ledger.md")
Copy-TemplateIfNeeded -Source (Join-Path $repoRoot "docs\figure-plan-template.md") -Destination (Join-Path $runDir "figure-plan.md")
New-TextFileIfNeeded -Path (Join-Path $runDir "title-candidates.md") -Content $titleCandidates
Copy-TemplateIfNeeded -Source (Join-Path $repoRoot "docs\section-budget-template.md") -Destination (Join-Path $runDir "section-budget.md")
Copy-TemplateIfNeeded -Source (Join-Path $repoRoot "docs\writing-style-plan-template.md") -Destination (Join-Path $runDir "writing-style-plan.md")
New-TextFileIfNeeded -Path (Join-Path $reviewsDir "review-$Name.md") -Content $reviewCurrent

Write-Host "Created run scaffold: $runDir"
Write-Host "Next step: follow prompts\16_launch_v1_6.md, fill title-candidates.md, award-feel-checklist.md, section-rhythm-budget.md, figure-style-spec.md, and concept-figure-spec.json, then use paper\templates\cumcm_v16_main.tex before drafting."
Write-Host "Legacy v1.5 fallback: follow prompts\15_launch_v1_5.md when the user explicitly asks for the v1.5 award-paper-feel flow."
