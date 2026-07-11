# CUMCM Routing Rules

Purpose: provide stable, agent-readable rules for mapping a problem statement to a modeling route. The route is a chain, not a single method.

## Routing Schema

For each candidate route:

```yaml
route_id:
  trigger_terms:
    - terms likely to appear in the problem
  problem_type: short label
  model_chain:
    - step 1
    - step 2
    - step 3
  outputs:
    - expected table/figure/result
  validation:
    - how to check the route
  risks:
    - common failure mode
```

## Detailed Method Cards

Use these cards when a candidate route includes one of the following method families:

- `knowledge/algorithms/cards/linear-integer-programming.md`
- `knowledge/algorithms/cards/entropy-weight.md`
- `knowledge/algorithms/cards/ahp.md`
- `knowledge/algorithms/cards/topsis.md`
- `knowledge/algorithms/cards/regression.md`
- `knowledge/algorithms/cards/nonlinear-programming.md`
- `knowledge/algorithms/cards/dynamic-programming.md`
- `knowledge/algorithms/cards/time-series.md`
- `knowledge/algorithms/cards/pca-lda.md`
- `knowledge/algorithms/cards/random-forest.md`
- `knowledge/algorithms/cards/svm.md`
- `knowledge/algorithms/cards/response-surface.md`
- `knowledge/algorithms/cards/queuing-models.md`
- `knowledge/algorithms/cards/graph-algorithms.md`
- `knowledge/algorithms/cards/simulation.md`

## Route: Geometry and Engineering Mechanics

Trigger terms:

- coordinate
- reflection
- surface
- node
- angle
- trajectory
- focal point
- radius
- paraboloid
- spherical surface
- actuator
- FAST

Model chain:

```text
coordinate system -> geometric/physical relation -> constraint set -> numerical solution -> error/sensitivity analysis
```

Common methods:

- coordinate transform
- vector geometry
- curve/surface fitting
- trigonometric relation
- constrained optimization
- numerical simulation

Expected outputs:

- coordinate-system diagram
- object or scene schematic on the first strong analysis page
- core equation set
- parameter table
- symbol explanation table when variables are dense
- before-after comparison figure
- error or displacement heatmap

Validation:

- geometric residual
- constraint violation check
- sensitivity to angle/position/step size
- physical sanity check
- final physical-performance metric, such as reception efficiency, coverage, energy, displacement reduction, or operational loss

Risks:

- undefined coordinate frame
- formulas not tied to geometry
- optimization without physical constraints
- result figures not showing the actual spatial relation
- stopping at geometric fitting error while omitting the final engineering performance measure
- multiple subquestions forced into one opaque global model instead of using per-question local closure when the scene extends step by step

Additional route note:

- `knowledge/cumcm/spatial-measurement-comparison-B030-B086-B311.md` shows the CUMCM-style spatial measurement variant of this route: scene figure -> shared symbol world -> per-question derivation -> design/result -> feasibility or replay check.

## Route: Statistics plus Chemical or Material Optimization

Trigger terms:

- catalyst
- conversion rate
- selectivity
- yield
- temperature
- chemical component
- material
- experiment design
- reaction

Model chain:

```text
data exploration -> statistical test/regression -> mechanism explanation -> optimization -> experiment design
```

Common methods:

- correlation analysis
- ANOVA
- multiple regression
- partial least squares
- nonlinear fitting
- response surface
- uniform design
- constrained optimization

Expected outputs:

- factor-effect table
- regression or response-surface plot
- significant factor summary
- optimal condition table
- supplementary experiment plan

Validation:

- residual analysis
- significance test
- cross-check against known mechanism
- sensitivity to temperature or factor range

Risks:

- overfitting small experimental data
- reporting optimal conditions outside valid ranges
- using black-box models without chemical explanation
- missing experiment-design closure

## Route: Supply Chain Evaluation and Planning

Trigger terms:

- supplier
- order
- transport
- capacity
- loss rate
- procurement
- inventory
- production
- carrier

Model chain:

```text
indicator design -> supplier/carrier evaluation -> planning model -> scenario and capacity analysis
```

Common methods:

- TOPSIS
- entropy weight
- AHP
- linear programming
- integer programming
- multi-objective optimization
- sensitivity analysis

Expected outputs:

- supplier score table
- selected supplier list
- order quantity table
- carrier allocation table
- capacity boundary or cost curve
- inventory or production-capacity time curve

Validation:

- constraint satisfaction audit
- historical backtest
- stress test for supply shortage
- sensitivity to weights and demand
- inventory stability and capacity feasibility over the planning horizon

Risks:

- evaluation score not connected to planning objective
- ranking-only paper with no executable plan
- missing capacity or loss constraints
- unrealistic integer/rounding assumptions
- selected suppliers listed without week-by-week order and transport decisions

## Route: Online Scheduling and Industrial Optimization

Trigger terms:

- real-time
- online
- abnormal
- cutting
- scheduling
- adjustment
- sequence
- loss
- downtime
- batch

Model chain:

```text
static baseline plan -> online update rule -> abnormal scenario model -> revised plan -> loss comparison
```

Common methods:

- integer linear programming
- dynamic programming
- rolling horizon optimization
- heuristic search
- mean absolute deviation
- scenario analysis

Expected outputs:

- initial plan table
- adjustment log
- Gantt-style timeline
- loss comparison table
- scenario result table
- abnormal-event type diagram
- initial-vs-adjusted plan table

Validation:

- feasibility after each update
- total loss comparison
- target-deviation distribution
- stress test with multiple abnormal events
- per-event loss audit
- operational-time feasibility check

Risks:

- solving only a static version
- no trigger rule for abnormal events
- no distinction between fixed and adjustable variables
- result cannot be updated step by step
- reporting total loss without scenario-level evidence
- ignoring adjustment time or execution delay without disclosing it

Deep-reading evidence:

- `knowledge/cumcm/deep-reading-2021D017.md` shows a compact official excellent paper pattern for this route: process schematic -> assumptions/symbols -> feasibility theorem -> discretized integer model -> abnormal-event classification -> repeated initial/adjusted plan tables -> model evaluation -> appendix file inventory.

## Route: Machine Learning Classification or Identification

Trigger terms:

- image
- spectrum
- classification
- recognition
- origin
- category
- feature
- diagnosis
- clustering
- sample

Route anchor:

- `knowledge/cumcm/deep-reading-2021E014.md` shows the preprocessing-first route for spectral and high-dimensional classification.

Model chain:

```text
preprocessing -> feature extraction/selection -> model comparison -> evaluation -> interpretation
```

Common methods:

- PCA
- LDA
- SVM
- random forest
- logistic regression
- K-means
- neural network
- Savitzky-Golay smoothing
- normalization

Expected outputs:

- data preprocessing summary
- feature plot or projection
- model comparison table
- confusion matrix
- accuracy/F1/recall table
- feature importance or interpretation

Validation:

- train/test split or cross-validation
- confusion matrix
- F1 score
- ablation of preprocessing choices
- class-imbalance check

Risks:

- reporting only accuracy
- unclear data split
- leakage from preprocessing before split
- no explanation of high-dimensional features
- using one model for all tasks without comparison

## Route: Time Series Prediction plus Decision

Trigger terms:

- forecast
- time series
- trend
- demand
- price
- traffic
- flow
- production plan
- replenishment

Route anchors:

- `knowledge/cumcm/deep-reading-2022E014.md` for conservative production-route E;
- `knowledge/cumcm/deep-reading-2022E029.md` for dynamic production-route E;
- `knowledge/cumcm/deep-reading-2023E176.md` for monitoring-route E.

Model chain:

```text
time-series cleaning -> trend/seasonality analysis -> prediction -> decision model -> error and scenario analysis
```

Common methods:

- moving average
- ARIMA or exponential smoothing
- regression
- GM(1,1)
- random forest or boosting
- neural network
- integer programming for downstream decisions

Expected outputs:

- time-series plot
- prediction curve
- error metric table
- downstream decision table
- scenario comparison

Validation:

- rolling backtest
- MAE/RMSE/MAPE
- residual diagnostics
- comparison with naive baseline

Risks:

- prediction not connected to decision
- training on future data
- using MAPE with zero or near-zero values
- ignoring seasonality or structural breaks

## Route: Evaluation and Ranking

Trigger terms:

- evaluate
- rank
- comprehensive score
- indicator
- weight
- quality
- suitability
- priority

Model chain:

```text
indicator screening -> standardization -> weighting -> comprehensive score -> robustness check
```

Common methods:

- entropy weight
- AHP
- TOPSIS
- PCA
- grey relational analysis
- fuzzy comprehensive evaluation

Expected outputs:

- indicator system table
- standardized data table
- weight table
- ranking table
- robustness analysis

Validation:

- weight sensitivity
- rank stability
- comparison of two weighting schemes
- domain sanity check

Risks:

- arbitrary indicator selection
- no standardization direction
- subjective weights without explanation
- ranking not used to solve later subquestions

## Route Selection Rules

1. If the problem contains physical geometry and engineering constraints, define the coordinate system before choosing an optimizer.
2. If the problem contains small experimental data, prefer interpretable statistics before complex machine learning.
3. If evaluation results feed a decision problem, ensure the score becomes a parameter, constraint, or objective in the later model.
4. If the problem is online or abnormal-event driven, separate the baseline plan from the update rule.
5. If the problem uses classification, require a clear data split and at least two evaluation metrics.
6. If the problem uses prediction, connect prediction outputs to a decision or policy when the question requires action.
7. If an algorithm cannot be validated from available data, keep it as a candidate rather than the main route.

## Route Output Contract

After route selection, the agent must write:

```text
Selected route:
Why this route fits:
Rejected alternatives:
Data requirements:
Mathematical objects:
Expected code outputs:
Expected paper figures:
Validation plan:
Risks and mitigations:
```
