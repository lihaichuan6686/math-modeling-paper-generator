# Phase 2 Prompt: Modeling Plan

Read:

- `runs/current/model-candidates.md`
- `knowledge/cumcm/paper-generation-playbook.md`
- `knowledge/algorithms/cumcm-routing-rules.md`
- `knowledge/algorithms/cards/README.md`
- `knowledge/algorithms/model-chain-patterns.md`
- relevant files under `knowledge/algorithms/cards/`
- if the problem involves trains, timetables, headways, OD flow, or large/small routes, also read `knowledge/algorithms/cards/rail-timetable-operation.md`
- `knowledge/latex/cumcm-section-contract.md`
- `knowledge/latex/figures-tables-equations-style.md`
- `docs/visual-generation-pipeline.md`
- `docs/figure-plan-template.md`
- `docs/artifact-ledger-template.md`

Create:

- `runs/current/model-plan.md`
- `runs/current/verification-plan.md`
- `runs/current/figure-plan.md` from `docs/figure-plan-template.md`
- update `runs/current/artifact-ledger.md`

## Model Plan Requirements

For each subquestion, define:

```text
Question:
Selected model chain:
Assumptions:
Variables:
Parameters:
Objective or target:
Constraints/equations:
Solver or algorithm:
Inputs:
Outputs:
Expected figures:
Expected tables:
Validation:
Failure modes:
```

If the problem matches `Type I: Rail Transit Timetable And Service Planning`, the model plan must also define:

```text
Passenger-flow objects:
Candidate route/service patterns:
Raw cost components:
Raw service-level components:
Feasibility constraints by group:
Timetable recurrence:
Required machine-readable outputs:
Capacity/tracking/dwell audit method:
Baseline plan for comparison:
Scenario parameters:
```

## Figure Plan Requirements

Plan figures before implementation:

- route/workflow figure
- explanatory model figures
- data exploration figures
- result figures
- validation or sensitivity figures

Each planned figure must include:

- type: route, explanatory, evidence, validation
- paper section
- source/tool
- input data or prompt
- output path
- whether it is reproducible evidence or schematic explanation

## Page-Structure Plan

Use `knowledge/latex/cumcm-section-contract.md` to allocate expected pages:

- abstract
- problem restatement
- problem analysis
- assumptions
- symbols
- data processing
- model establishment
- solution
- results
- validation
- strengths and limitations
- conclusion
- appendix

Do not use filler text to reach length. Page count must come from structure, equations, figures, tables, validation, and appendix material.

## Verification Plan

Define:

- validation method for each model
- metrics
- sensitivity parameters
- baseline or sanity checks
- code outputs needed to verify paper claims

For timetable/service-planning problems, the verification plan must include:

- capacity audit by section;
- headway and tracking-interval audit by station/train;
- dwell-time bound audit;
- check that full timetable output exists and matches the paper sample;
- baseline comparison and scenario table for recommendations.

## Artifact Ledger

Update the artifact ledger with planned:

- model artifacts
- code runs
- figures
- tables
- key results
- validation evidence
