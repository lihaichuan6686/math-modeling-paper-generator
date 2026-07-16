# First Calibration Batch Plan

Purpose: define the first practical batch of pressure tests after the v1.3 methodology layer and route run-file examples became available.

This file answers:

```text
Which route families should be pressure-tested first?
Why those families?
What should each pressure test prove or break?
What evidence should be written back?
```

## Batch Principle

The first batch should not try to cover every route.

It should cover the routes most likely to fail in different ways:

- forecast routes can fail by stopping at prediction;
- recognition routes can fail by reporting one metric;
- monitoring routes can fail by stopping at diagnosis;
- dynamic scheduling routes can fail by showing an update without comparison;
- geometry routes can fail by deriving formulas without a visible design.

Together, these families stress the main weak points of generated CUMCM papers:

```text
route closure
-> evidence burden
-> paragraph density
-> claim boundary
-> visual role
```

## Batch 1 Routes

| Priority | Route family | Why pressure-test it early | Nearest package | Main failure to look for |
|---:|---|---|---|---|
| 1 | monitoring-route E | E-type monitoring papers easily stack diagnostics without policy closure | `sample-run-packages/monitoring-route-e-demo/` | `decision_object_missing` |
| 2 | forecast-to-decision | forecast papers often look complete before producing a downstream decision | `sample-run-packages/forecast-to-decision-demo/` | `bridge_paragraph_missing` |
| 3 | classification-recognition | recognition papers often overclaim from one global score | `sample-run-packages/classification-recognition-demo/` | `claim_overreach` |
| 4 | dynamic-scheduling/update | update papers often show revised outputs without before/after meaning | `run-file-examples/dynamic-scheduling-demo/` | `validation_gap` |
| 5 | geometry/spatial-design | geometry papers often overfocus on formulas and under-explain scene meaning | `run-file-examples/geometry-spatial-demo/` | `visual_role_misfit` |

## Per-Route Test Targets

### 1. Monitoring-route E

Test target:

- Can the run produce a monitoring rule, sampling scheme, or policy artifact after diagnosis?

Required pressure evidence:

- diagnostic artifact;
- policy or monitoring table;
- consequence or intervention comparison;
- calibration log showing whether the policy bridge worked.

Write-back if it fails:

- strengthen `monitoring-route-e-demo/writing-style-plan.md`;
- add a review-checklist cue for missing policy artifacts;
- refine the claim-boundary row if conclusion wording is still too broad.

### 2. Forecast-to-decision

Test target:

- Can the run make the forecast alter a downstream decision instead of treating the forecast as the final output?

Required pressure evidence:

- forecast output with error evidence;
- decision table using forecast-derived parameters;
- scenario comparison;
- calibration log showing whether uncertainty reached the decision layer.

Write-back if it fails:

- strengthen `forecast-to-decision-demo/route-decision.md`;
- refine the paragraph-density playbook around forecast-to-decision bridges;
- add a review cue for forecast-only summaries.

### 3. Classification-recognition

Test target:

- Can the run produce class-level interpretation instead of a one-score classifier report?

Required pressure evidence:

- preprocessing and split policy;
- classifier comparison;
- confusion or class-level error artifact;
- calibration log showing whether conclusion stayed inside tested sample scope.

Write-back if it fails:

- strengthen `classification-recognition-demo/verification-plan.md`;
- tighten the evidence matrix row for recognition tasks;
- add a review finding for metric-only recognition claims.

### 4. Dynamic scheduling / update

Test target:

- Can the run explain what changed after disturbance and whether the revised schedule remains feasible?

Required pressure evidence:

- baseline schedule;
- revised schedule;
- before/after comparison;
- feasibility or stress audit;
- calibration log showing whether update value was interpreted.

Write-back if it fails:

- promote the dynamic scheduling package from run-file example to sample-run-package;
- add a review cue for revised-output-without-comparison;
- refine the section-budget example if the update block is too thin.

### 5. Geometry / spatial design

Test target:

- Can the run introduce the scene before formulas and close formulas into a visible design meaning?

Required pressure evidence:

- scene schematic;
- result/design artifact;
- replay, residual, or feasibility artifact;
- calibration log showing whether visual role and physical interpretation worked.

Write-back if it fails:

- promote geometry/spatial package from run-file example to sample-run-package;
- add stronger scene-first prompts;
- refine figure-plan guidance for geometry cases.

## Batch Output Standard

Each pressure test should produce:

- a filled run directory;
- a review note;
- a calibration log;
- at least one repo write-back or a written decision that no change is needed.

If no write-back is made, the calibration log must explain why the current guidance was sufficient.

## Candidate Selection Layer

Before starting the first Batch 1 run, use:

- `calibration-candidates/batch1-candidate-selection.md`

The current selection rule is:

1. keep monitoring-route E as the preferred methodology target because it best tests whether diagnosis and prediction close into a decision object;
2. do not start that full pressure test until the matching problem statement is available;
3. use 2021 E classification-recognition as the immediate executable fallback because the local problem statement, attachments, and excellent-paper anchors are available;
4. treat forecast-to-decision as the next route after one E-route pressure test unless both E-route candidates are blocked.

## Batch Completion Criteria

Batch 1 is complete when:

1. at least three route families have filled calibration logs;
2. at least one failure has been converted into a route or review improvement;
3. at least one route is confirmed as usable without immediate rule changes;
4. `objective-coverage-matrix.md` is updated with what the calibration proved.

## Best Use

Read this plan together with:

- `pressure-test-runbook.md`
- `calibration-log-template.md`
- `sample-run-packages/README.md`
- `run-file-examples/README.md`
- `../knowledge/cumcm/next-iteration-action-matrix.md`
