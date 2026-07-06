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

$modelPlan = @"
# Model Plan

Run: $Name

Read `prompts/02_model_plan.md` before completing this file.

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

## Subquestion Models

### Subquestion 1

Model chain:
Variables:
Objective/target:
Constraints/equations:
Solver/algorithm:
Expected outputs:
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

$reviewCurrent = @"
# Review

Run: $Name
Created: $createdAt

## Summary

Not reviewed yet.

## Blocking Issues

## Important Issues

## Minor Issues

## Evidence Checked

## Evidence Not Checked

## Required Fixes

## Human Verification Needed

## Final Status

Needs revision
"@

New-TextFileIfNeeded -Path (Join-Path $runDir "problem-analysis.md") -Content $problemAnalysis
New-TextFileIfNeeded -Path (Join-Path $runDir "data-inventory.md") -Content $dataInventory
New-TextFileIfNeeded -Path (Join-Path $runDir "model-candidates.md") -Content $modelCandidates
New-TextFileIfNeeded -Path (Join-Path $runDir "model-plan.md") -Content $modelPlan
New-TextFileIfNeeded -Path (Join-Path $runDir "verification-plan.md") -Content $verificationPlan

Copy-TemplateIfNeeded -Source (Join-Path $repoRoot "docs\artifact-ledger-template.md") -Destination (Join-Path $runDir "artifact-ledger.md")
Copy-TemplateIfNeeded -Source (Join-Path $repoRoot "docs\figure-plan-template.md") -Destination (Join-Path $runDir "figure-plan.md")
New-TextFileIfNeeded -Path (Join-Path $reviewsDir "review-$Name.md") -Content $reviewCurrent

Write-Host "Created run scaffold: $runDir"
Write-Host "Next step: follow prompts\00_intake.md"
