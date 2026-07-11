# Evaluation-to-Planning Demo Bundle

Purpose: show the minimum complete reference package Claude should hold in mind when generating an evaluation-to-planning v1.2 paper.

## Bundle Contents

### Planning Layer

- `docs/run-file-examples/evaluation-to-planning-demo/problem-analysis.md`
- `docs/run-file-examples/evaluation-to-planning-demo/model-plan.md`
- `docs/run-file-examples/evaluation-to-planning-demo/verification-plan.md`
- `docs/run-file-examples/evaluation-to-planning-demo/section-budget.md`
- `docs/run-file-examples/evaluation-to-planning-demo/writing-style-plan.md`
- `docs/run-file-examples/evaluation-to-planning-demo/figure-plan.md`
- `docs/run-file-examples/evaluation-to-planning-demo/artifact-ledger.md`

### Writing Layer

- `docs/paper-section-examples/evaluation-to-planning-demo/01_problem.tex`
- `docs/paper-section-examples/evaluation-to-planning-demo/abstract.tex`
- `docs/paper-section-examples/evaluation-to-planning-demo/02_analysis.tex`
- `docs/paper-section-examples/evaluation-to-planning-demo/05_data.tex`
- `docs/paper-section-examples/evaluation-to-planning-demo/06_model.tex`
- `docs/paper-section-examples/evaluation-to-planning-demo/07_solution.tex`
- `docs/paper-section-examples/evaluation-to-planning-demo/08_results.tex`
- `docs/paper-section-examples/evaluation-to-planning-demo/09_validation.tex`
- `docs/paper-section-examples/evaluation-to-planning-demo/10_strengths_limitations.tex`
- `docs/paper-section-examples/evaluation-to-planning-demo/11_conclusion.tex`

### Assembly Layer

- `docs/paper-assembly-examples/evaluation-to-planning-demo/paper-assembly.md`
- `docs/demo-bundles/evaluation-to-planning-demo/claim-map.md`
- `docs/demo-bundles/evaluation-to-planning-demo/caption-map.md`

## What Claude Should Learn From This Bundle

1. The route is not ranking-only.
2. The candidate screen and executable plan are different layers.
3. The results section must show both screening evidence and decision evidence.
4. Validation must include both feasibility and disturbed-scenario logic.
5. The abstract and conclusion are only allowed to say what the artifact ledger can support.
6. Every abstract and conclusion sentence should be checkable against the claim map.
7. Every important figure/table caption and interpretation paragraph should be checkable against the caption map.

## Minimum Artifact Set For A Real Run

The route is still incomplete unless a real run can show:

- one route figure or route table;
- one ranking artifact;
- one candidate or retained-set artifact;
- one executable plan artifact;
- one feasibility or audit artifact;
- one scenario or sensitivity artifact.

## Writing Rhythm To Reuse

```text
route justification
-> indicator preparation
-> score model
-> plan model
-> ranking and plan results
-> feasibility and scenario evidence
-> strengths/limits
-> close-out
```

## Common Failure Pattern

The most common weak draft in this family is:

```text
indicators
-> ranking
-> recommendation
```

This bundle exists to prevent that collapse.

## Final Pre-Handoff Check

Before a real run is treated as usable, compare it against this bundle and ask:

1. Does the run show a real bridge from candidate screening to executable planning?
2. Do the results and validation sections own distinct artifacts?
3. Could the abstract be reconstructed directly from the artifact ledger?
4. Does the conclusion answer the three-question map in order?
