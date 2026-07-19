# Algorithms

Purpose: give the generator one stable entry point for moving from a problem signal to a usable modeling route and then to detailed method cards.

## Read This Layer In Order

1. `cumcm-routing-rules.md`
2. `problem-type-to-method.md`
3. `route-method-matrix.md`
4. `model-chain-patterns.md`
5. `method-depth-ladder.md`
6. `v1-5-route-upgrade-atlas.md`
7. `method-family-index.md`
8. `cards/README.md`
9. the detailed cards under `cards/`

## What This Layer Does

This layer answers three questions:

1. What route family does the problem belong to?
2. What model chain should be built?
3. Which method family and method cards should be read first?
4. Which artifact and validation pattern should the route produce?

The goal is not to collect algorithm names. The goal is to produce a route that can survive review.

## Route Families

| Route family | Typical signals | First cards |
|---|---|---|
| Evaluation and ranking | indicators, alternatives, scheme selection | `entropy-weight.md`, `ahp.md`, `topsis.md` |
| Evaluation to planning | ranking plus executable decision | `linear-integer-programming.md`, `dynamic-programming.md`, `simulation.md` |
| Forecast to decision | historical data, trend, uncertainty | `time-series.md`, `regression.md`, `simulation.md` |
| Classification and recognition | labels, spectra, many features | `pca-lda.md`, `random-forest.md`, `svm.md` |
| Geometry and engineering mechanics | coordinates, surfaces, physical constraints | `nonlinear-programming.md`, `simulation.md`, `response-surface.md` |
| Online optimization and update | baseline plan, abnormal event, rolling adjustment | `linear-integer-programming.md`, `dynamic-programming.md`, `simulation.md` |

## Route To Card Rule

Use this rule when selecting a method:

```text
problem signal -> route family -> route-method matrix -> method card -> expected figure/table -> validation check
```

If a card cannot produce a visible artifact or a reviewable validation step, it is not the right card yet.

For v1.5 runs, use `v1-5-route-upgrade-atlas.md` before filling `method-depth-plan.md`. It maps problem signals to support layers, main models, result artifacts, validation artifacts, paper highlights, and traps.

## Minimum Evidence Contract

Every method choice should be able to answer:

- why this method fits the route;
- what input it expects;
- what output it produces;
- how the output enters the paper;
- how the result is checked.

## Best Use

Read this note together with:

- `cumcm-routing-rules.md`
- `problem-type-to-method.md`
- `route-method-matrix.md`
- `v1-5-route-upgrade-atlas.md`
- `method-family-index.md`
- `../cumcm/national-priority-problem-playbook.md`
- `cards/README.md`

## Status

This file is the top-level doorway for the algorithm knowledge base. It should stay short, stable, and easy to scan.
