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

### Type C1: E-Route Production Scheduling

Signals:

- material demand, order volume, inventory, service level, rolling production, support rate, or batch production;
- historical demand drives short-term production decisions;
- the problem usually asks for executable production quantities or support strategies.

Paper rhythm:

```text
material screening -> demand-pattern analysis -> forecast model -> service-level or safety-stock analysis -> rolling production rule/model -> scenario or capacity comparison -> execution tables
```

Model chain:

```text
key-material screening -> periodic/trend reading -> ARIMA or practical short-term forecast -> support/service calculation -> rolling production update rule or dynamic plan -> capacity-scenario audit
```

Required tables:

- key-material screening table;
- forecast-versus-actual table;
- service-level or support-rate table;
- safety-stock or inventory-gap table;
- rolling production plan table;
- scenario comparison table when multiple capacity assumptions exist.

Required figures:

- representative-material demand figure;
- fitted-vs-actual or forecast comparison figure;
- service-level or inventory consequence figure;
- scenario comparison figure when multiple production assumptions are tested.

Validation:

- actual-versus-forecast comparison;
- service-level audit;
- inventory nonnegativity or feasibility audit;
- compare at least two capacity or policy assumptions when possible;
- explain whether the route is conservative (`2022 E014`) or dynamic (`2022 E029`).

Common failure:

- forecast is presented without any production table;
- production quantities are listed without service-level or support interpretation;
- rolling rules use coefficients that are never explained.

### Type C2: E-Route Monitoring And Policy

Signals:

- monitoring scheme, sampling frequency, hydrology, reservoir, abruptness, periodicity, information value, or intervention effect;
- the problem asks for both future trend judgment and monitoring or policy design.

Paper rhythm:

```text
data cleaning and aggregation -> relation analysis -> seasonality/periodicity/abruptness diagnosis -> forecast model -> information-aware monitoring or policy model -> effect evaluation -> long-horizon consequence analysis
```

Model chain:

```text
cleaned monitoring series -> descriptive and regression analysis -> wavelet/M-K/Fisher/RS-style diagnosis -> forecast -> monitoring optimization or policy decision -> intervention-effect comparison -> counterfactual forecast
```

Required tables:

- data-cleaning or aggregation table;
- regression or feature-construction table;
- forecast comparison table;
- monitoring or policy decision table;
- intervention-effect comparison table;
- long-horizon consequence table when future impact is requested.

Required figures:

- route/workflow figure;
- periodicity or abruptness evidence figure;
- forecast-versus-history figure;
- monitoring-plan or policy-effect figure;
- long-horizon consequence figure.

Validation:

- descriptive evidence plus at least one formal diagnostic check;
- forecast evaluation or reasoned fit check;
- explicit path from forecast to monitoring/policy decision;
- intervention or counterfactual comparison when the problem asks for effect assessment;
- mixed-tool appendix traceability when the workflow spans Python, MATLAB, Excel, or solvers.

Common failure:

- many diagnostics are listed but never tied to a subquestion;
- prediction is the stopping point and no monitoring scheme is produced;
- policy conclusions are narrative and lack comparison evidence.

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

## Type I: Rail Transit Timetable And Service Planning

Signals:

- trains, metro, urban rail, bus frequency, timetable, headway, dwell time, running diagram, passenger flow, OD matrix, large/small route, stop plan, or service level;
- the answer must include an executable operation plan, schedule, timetable, or frequency plan;
- objectives usually combine operating cost and passenger service quality.

Paper rhythm:

```text
passenger-flow audit -> route/service pattern design -> objective and constraint system -> multi-objective solution -> timetable or frequency output -> feasibility audit -> operation suggestions
```

Model chain:

```text
section flow + OD matrix -> candidate service patterns -> cost/service objective decomposition -> Pareto or weighted/TOPSIS selection -> arrival/departure recurrence -> capacity/tracking/dwell audit -> scenario recommendations
```

Required tables:

- passenger-flow or OD summary table;
- parameter and unit table;
- objective-component table before normalization;
- candidate route/service-pattern table;
- selected operation-plan table;
- timetable sample table, with full timetable saved as an artifact;
- capacity audit table by section;
- tracking/dwell feasibility audit table;
- scenario or sensitivity recommendation table.

Required figures:

- section passenger-flow profile;
- OD heatmap or demand-distribution plot;
- model/solution workflow diagram;
- cost-service Pareto or tradeoff plot;
- running diagram or timetable plot;
- sensitivity or scenario comparison plot.

Validation:

- section capacity check for every selected service segment;
- headway and minimum tracking interval check across all relevant trains/stations;
- dwell-time bound check;
- comparison of selected plan against at least one baseline;
- sensitivity for demand, headway, route interval, or service-pattern changes;
- explicit link between Q1 operation plan and Q2 timetable output.

Common failure:

- a timetable figure is produced without a station-by-station recurrence or feasibility audit;
- normalized cost is reported without raw cost components;
- service level is compressed into one number without waiting, in-vehicle, transfer, or crowding interpretation;
- suggestions are narrative instead of backed by scenario tables;
- artifact ledger says the run passed while timetable, capacity, or tracking evidence is missing.

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

### E-Route Hint

When the identified route is E-type, do not leave it at generic `Type C`.

- Use `Type C1` when the task is forecast to production, inventory, batching, or service-level decisions.
- Use `Type C2` when the task is diagnosis and forecast to monitoring, sampling, or policy decisions.
- If the paper mixes both, declare one primary route and one secondary route in the model plan.

## Review Gate

Before accepting a generated draft, verify:

- every selected archetype has its required table set;
- every selected archetype has at least one required figure;
- every major conclusion has a ledger entry;
- validation matches the problem type;
- the paper does not stop at an intermediate artifact when the question asks for a decision, plan, or recommendation.
