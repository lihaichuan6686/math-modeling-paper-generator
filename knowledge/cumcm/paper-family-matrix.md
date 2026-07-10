# CUMCM Paper Family Matrix

Purpose: map common CUMCM paper families to section emphasis, early artifacts, and validation habits.

Use this note after route selection and before drafting the paper skeleton.

## Family Matrix

| Family | Section emphasis | First visible artifact | First core table | Validation habit |
|---|---|---|---|---|
| Evaluation and ranking | problem analysis, assumptions, results, validation | indicator or route overview figure | score/weight table | weight perturbation or rank stability |
| Evaluation to planning | problem analysis, model establishment, results, validation | evaluation-to-plan flow figure | candidate and decision table | feasibility and capacity audit |
| Forecast to decision | data processing, model establishment, results, validation | trend or fitted-vs-actual figure | forecast and scenario table | out-of-sample error and scenario propagation |
| Classification and recognition | data processing, model establishment, validation | preprocessing or feature-flow figure | classifier comparison table | confusion matrix and leakage check |
| Geometry and engineering mechanics | analysis, model establishment, solution process, validation | object or coordinate schematic | parameter and result table | residual or physical feasibility check |
| Online optimization and process update | model establishment, solution process, results, validation | baseline-to-update flow figure | before/after plan table | before-after comparison and stress test |

## Section Emphasis By Family

### Evaluation and Ranking

Lead with indicator design and why it matters. The body should show why the ranking is credible and why the top choices matter for the final recommendation.

### Evaluation to Planning

Lead with the bridge from scoring to executable decision. The paper must not stop at the ranking table.

### Forecast to Decision

Lead with time structure, uncertainty, and how prediction feeds the downstream decision. A forecast without scenario propagation is incomplete.

### Classification and Recognition

Lead with preprocessing, feature construction, and model comparison. The class evidence should include confusion-level analysis, not only accuracy.

### Geometry and Engineering Mechanics

Lead with the object or coordinate system. The math should close back to a measurable engineering quantity.

### Online Optimization and Process Update

Lead with the static baseline and the update trigger. The paper should show how the revised plan differs from the initial plan.

## Early Artifact Rule

Each family should produce an early figure and an early table before the model section grows large.

```text
family -> first figure -> first table -> first validation check
```

This keeps the paper from becoming method-first and object-last.

## Family Completion Check

A family is not ready for a final draft unless:

- the problem map is stable across abstract, body, and conclusion;
- the first figure shows the object, route, or data structure;
- the first table carries a modeling role, not just raw data;
- the validation artifact matches the family;
- the appendix supports traceability rather than padding.

## Best Use

Read this note together with:

- `route-index.md`
- `generation-loop.md`
- `problem-type-paper-archetypes.md`
- `official-paper-paradigms.md`
- `latex/section-map.md`

