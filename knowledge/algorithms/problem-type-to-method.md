# Problem Type to Method Map

Purpose: connect common CUMCM-style problem types to candidate method families, expected artifacts, and the first validation questions.

Use this file after route selection and before detailed card selection.

This is not a menu of algorithm names. It is a routing bridge from task shape to method family.

## How To Use

1. Identify the primary problem type from the statement.
2. Match it to one primary method family and one support family.
3. List the visible artifacts before coding.
4. Reject any method that cannot produce a reviewable validation step.

## Problem Type Map

| Problem type | Typical signals | Primary method family | Support family | Expected artifacts | First validation question |
|---|---|---|---|---|---|
| Evaluation and ranking | indicators, alternatives, screening, score comparison | multi-criteria evaluation | sensitivity / correlation analysis | indicator table, weight table, ranking table | does the ranking stay stable when weights move? |
| Evaluation to planning | ranking must become quantities, schedules, or assignments | evaluation plus optimization | feasibility audit / simulation | candidate table, plan table, feasibility table | does the score actually feed the final plan? |
| Forecast to decision | history, trend, seasonality, uncertainty, future planning | time-series or regression | scenario analysis / optimization | trend plot, forecast table, decision table | how does forecast uncertainty change the decision? |
| Classification and recognition | labels, spectra, many features, diagnosis, authenticity | feature extraction plus classifier comparison | error analysis | preprocessing table, model comparison table, confusion matrix | is there leakage or unstable class performance? |
| Geometry and engineering mechanics | coordinates, angles, coverage, reflection, constraints | geometric derivation plus constrained optimization | simulation / residual analysis | scene figure, parameter table, result table | is the result physically and geometrically feasible? |
| Production planning and scheduling | batches, capacities, rolling updates, machine or material constraints | linear/integer optimization | dynamic update / simulation | resource table, schedule table, adjusted-plan table | can the plan survive capacity or abnormal scenarios? |
| Graph and network | nodes, edges, paths, coverage, flows, connectivity | graph algorithm or network flow | sensitivity / optimization | network diagram, route table, bottleneck table | is the node-edge construction reproducible? |
| Queue and service systems | arrivals, waiting, service rate, congestion, peak periods | queuing analysis or simulation | capacity optimization | flow diagram, utilization table, waiting table | does the recommendation still work in peak conditions? |
| Experimental factor optimization | factors, levels, yield, selectivity, process conditions | regression / ANOVA / response surface | constrained optimization | factor table, coefficient table, response surface | is the optimum inside the valid experimental domain? |

## CUMCM-Focused Notes

### Evaluation and Ranking

Typical first cards:

- `entropy-weight.md`
- `ahp.md`
- `topsis.md`

Do not stop here if the problem asks for procurement, transport, production, or scheduling.

### Evaluation to Planning

Typical first cards:

- `linear-integer-programming.md`
- `dynamic-programming.md`
- `simulation.md`

This is a common CUMCM high-value route because it naturally produces longer, denser papers with executable tables.

### Forecast to Decision

Typical first cards:

- `time-series.md`
- `regression.md`
- `simulation.md`

For E-route problems, split early:

- production-route E: forecast -> inventory / support / production;
- monitoring-route E: diagnosis -> forecast -> monitoring / policy.

### Geometry and Engineering Mechanics

Typical first cards:

- `nonlinear-programming.md`
- `simulation.md`
- `response-surface.md`

The first figure should usually show the object, scene, or coordinate frame before any heavy derivation appears.

### Production Planning and Scheduling

Typical first cards:

- `linear-integer-programming.md`
- `dynamic-programming.md`
- `simulation.md`

If the problem contains rolling time windows or abnormal events, force an update-rule artifact rather than leaving adjustment in prose.

## Escalation Rule

Escalate from a simple method family to a richer chain when one of these is true:

- the question has multiple linked subproblems;
- the final answer must be executable rather than descriptive;
- uncertainty clearly affects the final decision;
- a single method cannot produce enough visible artifacts for a 20-30 page paper.

## Best Use

Read this note together with:

- `cumcm-routing-rules.md`
- `route-method-matrix.md`
- `model-chain-patterns.md`
- `../cumcm/problem-type-paper-archetypes.md`
- `../cumcm/official-paper-paradigms.md`
