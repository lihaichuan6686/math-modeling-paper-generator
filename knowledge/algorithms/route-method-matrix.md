# Route Method Matrix

Purpose: connect route families to the first method families, likely cards, and the evidence each route should produce.

This is a bridge from route selection to method selection.

## Route To Method Map

| Route family | First method family | First cards | Expected artifacts | Validation focus |
|---|---|---|---|---|
| Evaluation and ranking | multi-criteria evaluation | `entropy-weight.md`, `ahp.md`, `topsis.md` | indicator table, weight table, ranking table | rank stability, weight sensitivity |
| Evaluation to planning | evaluation plus optimization | `linear-integer-programming.md`, `dynamic-programming.md`, `simulation.md` | candidate table, plan table, feasibility audit | capacity, demand, and baseline comparison |
| Forecast to decision | time-series / regression plus planning | `time-series.md`, `regression.md`, `linear-integer-programming.md` | forecast plot, error table, scenario table | backtest, residuals, scenario propagation |
| Classification and recognition | feature extraction plus classifier comparison | `pca-lda.md`, `random-forest.md`, `svm.md` | preprocessing table, model comparison, confusion matrix | split policy, leakage, class balance |
| Geometry and engineering mechanics | geometry / physics plus constrained optimization | `nonlinear-programming.md`, `simulation.md`, `response-surface.md` | coordinate diagram, parameter table, residual figure | geometric residual, physical feasibility |
| Online optimization and update | dynamic / rolling optimization | `linear-integer-programming.md`, `dynamic-programming.md`, `simulation.md` | baseline plan, adjusted plan, loss comparison | update feasibility, per-event audit |
| Queue / service systems | queuing or simulation analysis | `queuing-models.md`, `simulation.md`, `linear-integer-programming.md` | flow diagram, utilization table, capacity curve | utilization, waiting, bottleneck check |
| Graph / network problems | graph algorithms and flow | `graph-algorithms.md`, `linear-integer-programming.md`, `simulation.md` | network diagram, edge/path table, bottleneck audit | connectivity, capacity, coverage |
| Experimental factor problems | regression and response surface | `regression.md`, `response-surface.md`, `nonlinear-programming.md` | factor table, contour plot, optimal-condition table | residuals, domain check, verification |

## Route To Card Rule

Use this order:

```text
problem signal
-> route family
-> route-method matrix
-> method family
-> card
-> expected artifact
-> validation
```

If a card cannot produce a visible artifact or a reviewable validation step, it should not be the first card.

## Route Notes

### Evaluation and Ranking

The score must feed a later decision or the paper is incomplete.

### Evaluation to Planning

The plan must be executable, not just ranked.

### Forecast to Decision

Forecast uncertainty must propagate into the decision layer.

### Classification and Recognition

Preprocessing and split policy are part of the model, not side notes.

### Geometry and Engineering Mechanics

The coordinate frame must exist before optimization becomes meaningful.

### Online Optimization and Update

The baseline and the update rule both need visible artifacts.

## Best Use

Read this note together with:

- `README.md`
- `cumcm-routing-rules.md`
- `method-family-index.md`
- `problem-type-to-method.md`
- `model-chain-patterns.md`
