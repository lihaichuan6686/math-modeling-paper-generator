# CUMCM Archetype Page Density Matrix

Purpose: connect problem archetypes to page emphasis, artifact density, and validation weight so a 20-30 page paper grows from evidence rather than filler.

This is a page-planning bridge, not a body-length target by itself.

## Archetype To Page Map

| Archetype | Main page emphasis | Typical visual density | Validation weight | Common page-growth source |
|---|---|---|---|---|
| Type A: Evaluation and ranking | analysis, assumptions, results, validation | 1 route figure, 2-4 evidence/result figures, 3-5 tables | weight/rank stability | indicator design, ranking explanation, robustness |
| Type B: Evaluation to planning | analysis, model establishment, results, validation | 1 flow figure, 2-4 evidence figures, 4-6 tables | feasibility and capacity audit | candidate selection, executable plan, scenario comparison |
| Type C: Forecast to decision | data processing, model establishment, results, validation | 1 trend figure, 2-4 fit/forecast figures, 4-6 tables | backtest and scenario propagation | time series analysis, forecast comparison, decision scenarios |
| Type C1: E-route production scheduling | data processing, model establishment, results, validation | 1 material figure, 2-4 forecast/service figures, 5-7 tables | service-level and capacity audit | representative materials, forecast evidence, rolling rules |
| Type C2: E-route monitoring and policy | data processing, model establishment, validation | 1 diagnostic figure, 2-4 forecast/policy figures, 5-7 tables | diagnostic and intervention comparison | cleaning, periodicity or abruptness evidence, policy effects |
| Type D: Classification or recognition | data processing, model establishment, validation | 1 preprocessing figure, 2-4 model/comparison figures, 4-6 tables | split and leakage check | preprocessing, classifier comparison, error analysis |
| Type E: Physical or geometric optimization | problem analysis, model establishment, solution process, validation | 1 object diagram, 2-4 geometry/residual figures, 3-5 tables | physical feasibility | coordinate setup, residual analysis, performance metric |
| Type F: Production scheduling or dynamic adjustment | model establishment, solution process, results, validation | 1 baseline/update figure, 2-4 schedule figures, 4-6 tables | before/after comparison | baseline, abnormal event handling, recovery analysis |
| Type G: Network, path, or coverage | problem analysis, model establishment, results, validation | 1 network figure, 2-4 route/coverage figures, 3-5 tables | connectivity and capacity audit | node-edge construction, route choice, bottleneck checks |
| Type H: Experiment factor and response surface | data processing, model establishment, validation | 1 factor figure, 2-4 response surface figures, 3-5 tables | residual and domain check | exploratory analysis, response surface, optimal condition |
| Type I: Rail transit timetable and service planning | problem analysis, data processing, model establishment, solution, results, validation | 1 passenger-flow figure, 2-4 timetable/service figures, 5-8 tables | capacity/headway/dwell audit | OD matrix, timetable recurrence, scenario comparison |

## Page Emphasis Rule

Use the archetype to decide where pages should go:

```text
archetype
-> section emphasis
-> artifact density
-> validation weight
-> page-growth source
```

If the paper looks short, grow the page count by adding the missing evidence type, not by adding background.

## Fast Checks

- Type A should not stop at ranking.
- Type B should not stop at candidate screening.
- Type C should not stop at forecasting.
- Type C1 and C2 should not stop at generic time series writing.
- Type D should always show split and error evidence.
- Type E should show the object or coordinate frame early.
- Type F should show baseline and adjustment.
- Type G should show reproducible node/edge construction.
- Type H should keep the optimum inside the domain.
- Type I should show OD, timetable recurrence, and feasibility audits.

## Best Use

Read this note together with:

- `20-30-page-paper-blueprint.md`
- `archetype-section-matrix.md`
- `paper-family-matrix.md`
- `latex/section-family-index.md`
