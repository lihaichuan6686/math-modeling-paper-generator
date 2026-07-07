# CUMCM Problem-Type Paper Archetypes

Purpose: map common CUMCM problem types to paper structure, model chains, figures, tables, validation evidence, and review risks. Use this file after identifying the problem route and before writing `paper/sections/`.

This is not a text template. It is a structure contract for a generated draft.

## How To Use

1. Identify the primary problem type and one secondary type.
2. Copy the relevant section contract into `runs/current/model-plan.md`.
3. List required tables and figures before writing results.
4. Reject any paper draft that lacks the validation artifact required by its type.
5. Use `knowledge/cumcm/20-30-page-paper-blueprint.md` for page budgeting.

## Type A: Evaluation And Ranking

Signals:

- rank suppliers, schools, cities, schemes, materials, routes, or policies;
- many indicators with different units;
- no direct physical law dominates the problem.

Paper rhythm:

```text
problem restatement -> indicator construction -> preprocessing and normalization -> weighting/evaluation -> ranking -> sensitivity of weights -> recommendation
```

Model chain:

```text
indicator system -> normalization -> entropy/AHP/TOPSIS or combined weighting -> ranking -> robustness check
```

Required tables:

- raw indicator table;
- normalization method table;
- weight table;
- ranking table;
- sensitivity or rank-stability table.

Required figures:

- indicator correlation or distribution plot;
- ranking comparison bar chart;
- weight sensitivity plot.

Validation:

- weight perturbation;
- comparison between at least two evaluation methods;
- explanation of why top-ranked choices remain stable or why instability matters.

Common failure:

- ranking is reported as the final answer even though the problem asks for a plan or policy.

## Type B: Evaluation To Planning

Signals:

- rank suppliers, carriers, factories, or sites, then make quantities, schedules, or allocations;
- final answer must be executable.

Paper rhythm:

```text
data preprocessing -> evaluation model -> candidate selection -> planning model -> executable table -> feasibility audit -> scenario/sensitivity
```

Model chain:

```text
indicator score -> selected candidates -> LP/IP/greedy baseline -> capacity/inventory/coverage audit -> sensitivity
```

Required tables:

- indicator and score table;
- selected candidate table;
- decision variable table;
- final plan table;
- feasibility audit table;
- sensitivity table.

Required figures:

- flowchart from evaluation to planning;
- inventory/capacity/coverage time curve;
- cost or loss comparison chart.

Validation:

- capacity constraints;
- demand or safety constraints;
- perturbation of weights, demand, or loss rates;
- compare baseline and optimized plan when possible.

Common failure:

- evaluation and planning are disconnected; the ranking table does not actually feed the plan.

## Type C: Forecast To Decision

Signals:

- future demand, price, traffic, load, risk, or population drives a decision;
- historical time series or panel data are available.

Paper rhythm:

```text
data audit -> trend/seasonality analysis -> forecast model comparison -> forecast result -> decision model -> uncertainty propagation -> stress test
```

Model chain:

```text
time-series/regression forecast -> error evaluation -> planning model -> high/medium/low scenario audit
```

Required tables:

- train/test split and feature table;
- model comparison table;
- forecast table;
- decision table under forecasts;
- scenario stress-test table.

Required figures:

- historical trend plot;
- fitted-vs-actual plot;
- forecast interval plot;
- decision sensitivity plot.

Validation:

- out-of-sample error;
- residual check;
- scenario comparison;
- explain how forecast uncertainty affects decisions.

Common failure:

- forecast is treated as certain input and no error or scenario is propagated.

## Type D: Classification Or Recognition

Signals:

- samples, spectra, images, texts, or high-dimensional indicators must be classified;
- labels, categories, or authenticity decisions matter.

Paper rhythm:

```text
data description -> preprocessing -> feature extraction -> model comparison -> final classifier -> error analysis -> interpretation
```

Model chain:

```text
cleaning/standardization -> PCA/LDA/features -> SVM/random forest/logistic baseline -> confusion matrix -> error-case analysis
```

Required tables:

- sample split table;
- preprocessing steps table;
- feature importance or component table;
- classifier comparison table;
- confusion matrix.

Required figures:

- feature distribution plot;
- dimension-reduction scatter plot;
- confusion matrix heatmap;
- error-case or residual plot.

Validation:

- train/test split or cross-validation;
- leakage check;
- class imbalance discussion;
- confusion-level interpretation, not only accuracy.

Common failure:

- high accuracy is reported without split policy, class distribution, or confusion matrix.

## Type E: Physical Or Geometric Optimization

Signals:

- coordinates, geometry, optics, mechanics, paths, surfaces, devices, or spatial layout;
- equations are tied to real physical quantities.

Paper rhythm:

```text
coordinate system -> physical/geometric relation -> objective and constraints -> numerical solution -> configuration/result table -> residual or performance check
```

Model chain:

```text
coordinate model -> physical equations -> nonlinear/linear/integer optimization -> residual map -> final engineering metric
```

Required tables:

- coordinate or parameter table;
- objective/constraint summary table;
- optimal configuration table;
- residual/performance table.

Required figures:

- coordinate or mechanism diagram;
- geometry/surface/path plot;
- residual or error map;
- sensitivity or final performance plot.

Validation:

- physical feasibility;
- residual distribution;
- engineering-performance metric, such as coverage, error reduction, energy, loss, or safety margin.

Common failure:

- formulas look mathematical but are not grounded in a coordinate frame or physical constraint.

## Type F: Production Scheduling Or Dynamic Adjustment

Signals:

- machines, orders, shifts, cutting, batching, disruptions, rolling updates, or abnormal scenarios;
- solution must change over time.

Paper rhythm:

```text
static baseline -> objective and constraints -> scheduling algorithm -> baseline result -> abnormal event/update rule -> adjusted plan -> loss comparison
```

Model chain:

```text
LP/IP/heuristic schedule -> rolling update or dynamic programming -> abnormal scenario -> comparison and recovery analysis
```

Required tables:

- task/resource table;
- baseline schedule table;
- abnormal scenario table;
- adjusted schedule table;
- loss or efficiency comparison table.

Required figures:

- Gantt-like schedule diagram;
- resource utilization curve;
- before/after loss comparison chart.

Validation:

- constraint audit;
- runtime or feasibility check;
- compare initial and adjusted plans;
- scenario stress test.

Common failure:

- only a static plan is solved while dynamic update is described verbally.

## Type G: Network, Path, Or Coverage

Signals:

- graph, nodes, edges, path, matching, flow, coverage, routing, or spatial connectivity.

Paper rhythm:

```text
network construction -> node/edge definition -> algorithm selection -> solution visualization -> bottleneck and feasibility audit -> sensitivity
```

Model chain:

```text
node-edge table -> shortest path / network flow / matching / covering model -> selected edges or routes -> bottleneck analysis
```

Required tables:

- node table;
- edge or distance table;
- selected route/flow/matching table;
- bottleneck table.

Required figures:

- network diagram;
- selected route or coverage map;
- bottleneck or sensitivity plot.

Validation:

- connectivity check;
- capacity or coverage constraints;
- perturb edge weights or capacities.

Common failure:

- graph image exists but node and edge construction is not reproducible.

## Type H: Experiment Factor And Response Surface

Signals:

- factor levels, yield, conversion, quality, selectivity, process optimization, or material preparation.

Paper rhythm:

```text
factor description -> exploratory analysis -> regression/ANOVA -> response surface -> constrained optimum -> verification proposal
```

Model chain:

```text
factor table -> regression or ANOVA -> response surface -> nonlinear optimum -> residual and verification check
```

Required tables:

- factor-level table;
- fitted coefficient or ANOVA table;
- optimal condition table;
- residual or verification table.

Required figures:

- factor effect plot;
- response surface or contour plot;
- residual plot.

Validation:

- residual diagnostics;
- domain-bound check for optimum;
- verification experiment proposal or holdout check.

Common failure:

- optimum lies outside the experimental domain or lacks verification discussion.

## Page-Budget Hint

For a 20-30 page paper, each active problem type should normally contribute:

| Component | Pages |
|---|---:|
| problem restatement and analysis | 2-4 |
| data processing and indicator/feature construction | 3-5 |
| model establishment and derivation | 5-9 |
| solution process and implementation | 3-5 |
| results with tables and figures | 4-6 |
| validation, sensitivity, and limitations | 3-5 |

If the paper is short, add missing evidence, derivation, validation, or appendix material. Do not add generic filler.

## Review Gate

Before accepting a generated draft, verify:

- every selected archetype has its required table set;
- every selected archetype has at least one required figure;
- every major conclusion has a ledger entry;
- validation matches the problem type;
- the paper does not stop at an intermediate artifact when the question asks for a decision, plan, or recommendation.
