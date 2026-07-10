# Algorithm Method Family Index

Purpose: map common CUMCM route families to the first method families and cards worth reading.

This is a reuse index, not a full methods handbook.

## Method Families At A Glance

| Route family | First method family | First cards | Typical evidence |
|---|---|---|---|
| Evaluation and ranking | multi-criteria evaluation | `entropy-weight.md`, `ahp.md`, `topsis.md` | indicator table, weight table, ranking table |
| Evaluation to planning | evaluation plus optimization | `linear-integer-programming.md`, `dynamic-programming.md`, `simulation.md` | candidate table, decision table, feasibility audit |
| Forecast to decision | time-series / regression plus planning | `time-series.md`, `regression.md`, `linear-integer-programming.md` | forecast plot, error table, scenario table |
| Classification and recognition | feature extraction plus classifier comparison | `pca-lda.md`, `random-forest.md`, `svm.md` | preprocessing table, classifier comparison, confusion matrix |
| Geometry and engineering mechanics | geometry / physics plus constrained optimization | `nonlinear-programming.md`, `simulation.md`, `response-surface.md` | coordinate diagram, parameter table, residual figure |
| Online optimization and update | dynamic / rolling optimization | `linear-integer-programming.md`, `dynamic-programming.md`, `simulation.md` | baseline plan, adjusted plan, loss comparison |
| Queue / service systems | queuing or simulation analysis | `queuing-models.md`, `simulation.md`, `linear-integer-programming.md` | flow diagram, utilization table, capacity curve |
| Graph / network problems | graph algorithms and flow | `graph-algorithms.md`, `linear-integer-programming.md`, `simulation.md` | network diagram, edge/path table, bottleneck audit |
| Experimental factor problems | regression and response surface | `regression.md`, `response-surface.md`, `nonlinear-programming.md` | factor table, contour plot, optimal-condition table |

## How To Use

When a problem arrives:

1. identify the route family;
2. read the first method family row;
3. choose one primary card and one validation card;
4. write the figure/table plan before coding;
5. record the selected card names in the run files.

## Route-To-Card Notes

### Evaluation and Ranking

Use evaluation methods to produce a score that becomes a decision input. Do not stop at ranking.

### Evaluation to Planning

The planning model must consume the evaluation result. The plan should be executable and auditable.

### Forecast to Decision

Forecast uncertainty should flow into the downstream decision. Scenario or stress testing is not optional when the forecast drives a choice.

### Classification and Recognition

Feature reduction and classifier comparison matter as much as model choice. Confusion-level evidence is part of the route.

### Geometry and Engineering Mechanics

The coordinate frame and physical metric must appear before optimization becomes meaningful.

### Online Optimization and Update

The static baseline and the update rule both need visible artifacts.

## Good Default Pairings

- evaluation/ranking: `entropy-weight.md` + `topsis.md`
- evaluation/planning: `linear-integer-programming.md` + `simulation.md`
- forecast/decision: `time-series.md` + `linear-integer-programming.md`
- classification/recognition: `pca-lda.md` + `svm.md`
- geometry/engineering: `nonlinear-programming.md` + `simulation.md`
- online update: `dynamic-programming.md` + `simulation.md`
- queue/service: `queuing-models.md` + `simulation.md`
- graph/network: `graph-algorithms.md` + `linear-integer-programming.md`
- experimental factors: `regression.md` + `response-surface.md`

## Maintenance Rule

If a route family repeatedly uses a different card pair, update this file and the route rules together.

