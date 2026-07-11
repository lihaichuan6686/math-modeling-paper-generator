# Rail-Timetable Demo Bundle

Purpose: show the minimum complete reference package Claude should hold in mind when generating a rail/timetable v1.2 paper.

## Bundle Contents

### Planning Layer

- `docs/run-file-examples/rail-timetable-demo/problem-analysis.md`
- `docs/run-file-examples/rail-timetable-demo/model-plan.md`
- `docs/run-file-examples/rail-timetable-demo/verification-plan.md`
- `docs/run-file-examples/rail-timetable-demo/section-budget.md`
- `docs/run-file-examples/rail-timetable-demo/writing-style-plan.md`
- `docs/run-file-examples/rail-timetable-demo/figure-plan.md`
- `docs/run-file-examples/rail-timetable-demo/artifact-ledger.md`

### Writing Layer

- `docs/paper-section-examples/rail-timetable-demo/01_problem.tex`
- `docs/paper-section-examples/rail-timetable-demo/abstract.tex`
- `docs/paper-section-examples/rail-timetable-demo/02_analysis.tex`
- `docs/paper-section-examples/rail-timetable-demo/05_data.tex`
- `docs/paper-section-examples/rail-timetable-demo/06_model.tex`
- `docs/paper-section-examples/rail-timetable-demo/07_solution.tex`
- `docs/paper-section-examples/rail-timetable-demo/08_results.tex`
- `docs/paper-section-examples/rail-timetable-demo/09_validation.tex`
- `docs/paper-section-examples/rail-timetable-demo/10_strengths_limitations.tex`
- `docs/paper-section-examples/rail-timetable-demo/11_conclusion.tex`

### Assembly Layer

- `docs/paper-assembly-examples/rail-timetable-demo/paper-assembly.md`

## What Claude Should Learn From This Bundle

1. The route is not timetable-first.
2. Passenger-flow evidence must justify the service pattern before recurrence appears.
3. The selected operation plan and timetable are separate but linked artifacts.
4. Capacity, tracking, dwell, and scenario evidence should stay visibly distinct.
5. The abstract and conclusion can only report plan/timetable claims backed by generated artifacts.

## Minimum Artifact Set For A Real Run

The route is still incomplete unless a real run can show:

- one flow or overlap-zone artifact;
- one service-pattern comparison artifact;
- one selected-plan artifact;
- one timetable artifact;
- one capacity audit artifact;
- one tracking or dwell audit artifact;
- one scenario artifact.

## Writing Rhythm To Reuse

```text
flow burden
-> service-pattern justification
-> selected plan
-> timetable generation
-> audit evidence
-> scenario comparison
-> strengths/limits
-> close-out
```

## Common Failure Pattern

The most common weak draft in this family is:

```text
selected plan
-> timetable figure
-> recommendation
```

This bundle exists to prevent the paper from skipping the flow burden and the audit burden.

## Final Pre-Handoff Check

Before a real run is treated as usable, compare it against this bundle and ask:

1. Does the run show why the overlap zone exists before the timetable appears?
2. Are selected-plan, timetable, and audit artifacts all visible?
3. Do the validation artifacts remain separate enough to read operationally?
4. Does the conclusion answer the three-question map in order?
