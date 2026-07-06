# Phase 2 Prompt: Modeling Plan

Read:

- `runs/current/model-candidates.md`
- `knowledge/cumcm/paper-generation-playbook.md`
- `knowledge/algorithms/cumcm-routing-rules.md`
- relevant files under `knowledge/algorithms/cards/`
- `knowledge/latex/cumcm-section-contract.md`
- `knowledge/latex/figures-tables-equations-style.md`
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

## Artifact Ledger

Update the artifact ledger with planned:

- model artifacts
- code runs
- figures
- tables
- key results
- validation evidence
