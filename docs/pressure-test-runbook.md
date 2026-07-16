# Pressure-Test Runbook

Purpose: define one repeatable way to pressure-test the current methodology stack on real or realistic contest problems, record where it fails, and convert those failures into reusable route, writing, or quality upgrades.

Use this file after the route skeletons exist and before claiming that the methodology layer is truly stable across problem families.

This runbook is not for one perfect demo. It is for repeated calibration.

## Why This Exists

The repository now has route-aware run scaffolds for several high-frequency families.

That is necessary, but not sufficient.

The next question is:

```text
When these scaffolds are used on fresh problems, where do they still break?
```

This runbook makes that question operational.

## When To Use

Use this runbook when:

- a new real problem is available;
- a route family has a scaffold but limited fresh-run evidence;
- the team wants to compare whether one route family is more brittle than another;
- a review finds that the paper looked complete but still felt thin, weak, or overclaimed.

## Pressure-Test Goal

A pressure test should answer four things:

1. Did the route selection land on the right family?
2. Did the scaffold produce enough evidence and the right evidence?
3. Did the writing controls prevent machine-thin sections and overclaiming?
4. What exact upgrade should be written back into the repo?

## Standard Sequence

For one pressure test, use this order:

```text
problem intake
-> family identification
-> scaffold fill
-> artifact plan
-> first paper attempt
-> review
-> failure classification
-> repo write-back
```

Do not skip the write-back step.

If the failure does not become a route, writing, or review improvement, the pressure test is incomplete.

## Minimum Inputs

Before starting, collect:

- problem statement;
- attachments or data if available;
- chosen route family;
- nearest run-file example;
- nearest demo bundle or sample run package if one exists.

## Required Run Outputs

Every pressure test should produce at least:

- `runs/<name>/problem-profile.md`
- `runs/<name>/problem-analysis.md`
- `runs/<name>/route-decision.md`
- `runs/<name>/model-plan.md`
- `runs/<name>/section-budget.md`
- `runs/<name>/writing-style-plan.md`
- `runs/<name>/verification-plan.md`
- `runs/<name>/figure-plan.md`
- `runs/<name>/artifact-ledger.md`
- one review note under `reviews/`
- one calibration log based on `calibration-log-template.md`

## Pressure-Test Questions

### 1. Route Fit

Check:

- Was the modeled object named correctly?
- Was the decision object named correctly?
- Did the route family match the real end task?
- Did the paper drift into a nearby but wrong family?

Typical failures:

- evaluation paper stops before planning;
- forecast paper never closes into decision;
- diagnosis paper never closes into policy;
- geometry paper derives formulas but does not show a feasible design.

### 2. Evidence Fit

Check:

- Does each major subquestion have a visible artifact?
- Does the family-specific evidence burden appear in the body?
- Is validation real, or just ceremonial?
- Are the first figures object-first rather than result-first when the family expects that?

Typical failures:

- one global result table replaces subquestion evidence;
- screenshots or code blocks stand in for missing artifacts;
- diagnostic plots appear without policy or decision artifacts;
- revised schedules or scenario outputs exist but are never interpreted.

### 3. Writing Fit

Check:

- Did the paragraph density match the family?
- Did the abstract close each major subquestion?
- Did the conclusion stay within the claim boundary?
- Did any section read like artifact dumping?

Typical failures:

- abstract lists methods but not results;
- conclusion says `effective` or `optimal` without scope;
- model bridge paragraphs are missing;
- long sections grow by repetition instead of evidence loops.

### 4. Repair Fit

Check:

- Is the problem a route gap, a method gap, a section-writing gap, a figure/table gap, or a review-gate gap?
- What is the smallest durable repo change that would prevent this failure next time?

Every pressure test should end with one or more of:

- route rule update;
- run-file example update;
- writing/playbook update;
- figure/table convention update;
- review checklist or gate update;
- new comparison or deep-reading note to fill a reasoning gap.

## Failure Buckets

Use these buckets in the calibration log:

- `route_misfit`
- `decision_object_missing`
- `artifact_gap`
- `validation_gap`
- `bridge_paragraph_missing`
- `claim_overreach`
- `paragraph_density_misfit`
- `visual_role_misfit`
- `appendix_inflation`
- `review_gate_miss`

If a failure does not fit a bucket, add a new bucket and explain why.

## Success Rule

A pressure test is successful if:

1. it exposes a real weakness or confirms a route works under stress;
2. the weakness is localized clearly;
3. the repo receives a concrete write-back.

Success does not mean the paper itself must pass on the first try.

## Write-Back Rule

After every pressure test, decide:

1. update an existing route file;
2. add or refine a run-file example;
3. tighten a writing or review control;
4. add a new sample-reading or comparison anchor.

Then record the exact files changed in the calibration log.

## Best Use

Read this note together with:

- `sample-run-packages/README.md`
- `review-case-examples/README.md`
- `review-checklist.md`
- `objective-coverage-matrix.md`
- `../knowledge/cumcm/next-iteration-action-matrix.md`
