# Workflow

This document describes the standard v1.0 workflow for a research-only CUMCM-style paper draft.

## Standard Run Setup

Create a new run:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\new-run.ps1 -Name current -Problem "problem label"
```

The script creates:

- `runs/current/problem-analysis.md`
- `runs/current/data-inventory.md`
- `runs/current/model-candidates.md`
- `runs/current/model-plan.md`
- `runs/current/verification-plan.md`
- `runs/current/figure-plan.md`
- `runs/current/artifact-ledger.md`
- `reviews/review-current.md`
- output folders for figures, tables, data, models, and generated artifacts

Then follow the phase prompts from `prompts/00_intake.md` through `prompts/05_review.md`.

## Phase 0: Intake

Input:

- `problems/problem.md`
- attachments under `problems/`

Output:

- `runs/current/problem-analysis.md`
- `runs/current/data-inventory.md`

Required work:

- restate the problem;
- identify subquestions;
- list inputs, outputs, constraints, metrics, and risks;
- record routing signals.

## Phase 1: Ideation

Output:

- `runs/current/model-candidates.md`

Required work:

- propose at least three route-level model chains;
- compare mathematical fit, data requirements, interpretability, implementation difficulty, figures/tables, validation, and risks;
- select one primary route and one backup route.

## Phase 2: Model Plan

Output:

- `runs/current/model-plan.md`
- `runs/current/verification-plan.md`
- `runs/current/figure-plan.md`
- update `runs/current/artifact-ledger.md`

Required work:

- define assumptions, variables, parameters, equations, constraints, solvers, expected outputs, validation, and failure modes;
- plan figures before implementation;
- allocate paper sections using the 20-30 page blueprint.

## Phase 3: Implementation

Output:

- code under `src/`
- generated figures under `paper/figures/`
- generated tables under `paper/tables/`
- intermediate outputs under `runs/current/`
- updated artifact ledger

Required work:

- keep a clear run sequence;
- record random seeds;
- generate at least one reproducible evidence figure and one result table for v1.0;
- record schematic or AI-generated figure prompts if used.

## Phase 4: Writing

Output:

- LaTeX section files under `paper/sections/`
- updated `paper/main.tex` only when needed

Required work:

- write a complete structured draft;
- keep abstract last;
- cite every figure/table in text;
- ensure important numbers are listed in the artifact ledger;
- do not pad with generic background.

## Phase 5: Build

Command:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\compile.ps1
```

If compilation fails, repair missing figures, broken references, table overflow, and LaTeX syntax.

## Phase 6: Review

Output:

- `reviews/review-current.md` or `reviews/review-<run>.md`

Required work:

- use `docs/review-checklist.md`;
- use `knowledge/quality/quality-rubric-v2.md`;
- check problem coverage, model logic, reproducibility, visual source classification, validation, PDF quality, and responsible use.

## v1.0 Completion Gate

A v1.0 run is acceptable when:

1. every subquestion has at least a draft model and draft answer;
2. at least one figure and one table are generated or explicitly planned;
3. the LaTeX paper has all major CUMCM sections;
4. every important claim is marked as verified, illustrative, or pending;
5. a review file exists with Pass/Warn/Fail/Unknown style findings.
