# Algorithm Card Index

Purpose: choose detailed method cards from problem signals before writing a model plan. Use this index together with `knowledge/algorithms/cumcm-routing-rules.md`.

## Fast Selection Table

| Problem signal | Likely route | Read these cards first | Expected paper artifacts |
| --- | --- | --- | --- |
| comprehensive evaluation, ranking, indicator weights, scheme selection | evaluation and ranking | `entropy-weight.md`, `ahp.md`, `topsis.md` | indicator direction table, weight table, distance/closeness table, ranking stability |
| allocation, purchase, capacity, scheduling, selection | planning and optimization | `linear-integer-programming.md`, `nonlinear-programming.md`, `dynamic-programming.md` | variable table, objective/constraint block, plan table, feasibility audit |
| online update, abnormal event, rolling adjustment | dynamic planning | `linear-integer-programming.md`, `dynamic-programming.md`, `simulation.md` | initial plan, update rule, scenario table, loss comparison |
| factor influence, relationship, prediction from variables | statistical explanation | `regression.md`, `response-surface.md` | coefficient table, residual plot, factor-effect plot, prediction table |
| experiment factors, process optimum, chemical/material settings | experimental optimization | `response-surface.md`, `regression.md`, `nonlinear-programming.md` | ANOVA/coefficient table, contour/surface plots, optimal-condition table |
| high-dimensional indicators, spectra, image features, many correlated variables | feature extraction | `pca-lda.md`, `regression.md`, `random-forest.md`, `svm.md` | explained-variance table, loading table, projection plot, classifier metrics |
| classification, recognition, diagnosis, grouping with labels | supervised learning | `random-forest.md`, `svm.md`, `pca-lda.md` | confusion matrix, metric table, feature importance, error analysis |
| future demand, price, traffic, production, monitoring sequence | forecasting | `time-series.md`, `regression.md`, `simulation.md` | train/test time plot, forecast plot, error table, uncertainty notes |
| production service level, rolling production, material support, inventory response | production-route E | `time-series.md`, `regression.md`, `linear-integer-programming.md`, `simulation.md` | forecast comparison, service-level table, rolling production table, scenario audit |
| monitoring, diagnosis, periodicity, policy effect, intervention comparison | monitoring-route E | `time-series.md`, `regression.md`, `simulation.md`, `graph-algorithms.md` | diagnosis figure, monitoring plan table, effect comparison, counterfactual plot |
| service windows, waiting, congestion, capacity of stations | queueing system | `queuing-models.md`, `simulation.md`, `linear-integer-programming.md` | system flow diagram, waiting/capacity table, utilization curve |
| train timetable, headway, large/small route, OD matrix, section passenger flow, running diagram | rail transit service planning | `rail-timetable-operation.md`, `topsis.md`, `linear-integer-programming.md`, `simulation.md` | route candidate table, cost-service table, timetable output, capacity/tracking audit |
| routes, networks, connectivity, flow, matching, coverage | graph/network | `graph-algorithms.md`, `linear-integer-programming.md`, `simulation.md` | network diagram, selected-edge/path table, bottleneck analysis |
| randomness, uncertainty, robustness, stochastic scenario | simulation and risk | `simulation.md`, `time-series.md`, `queuing-models.md` | simulation flowchart, distribution plot, confidence interval, stress table |

## Selection Procedure

1. Identify whether the subquestion is asking for explanation, prediction, optimization, classification, simulation, or evaluation.
2. Choose one primary card and one backup card for each subquestion.
3. Check required inputs before committing to a method.
4. Copy expected figures and tables into `runs/current/figure-plan.md` and `runs/current/artifact-ledger.md`.
5. Use the card's validation and review checks to build `runs/current/verification-plan.md`.

## Route Composition Patterns

Strong CUMCM papers usually combine cards:

- prediction -> optimization -> sensitivity
- entropy/AHP weighting -> TOPSIS ranking -> planning -> scenario audit
- feature extraction -> classification -> error analysis
- physical/geometric derivation -> numerical optimization -> residual check
- statistical factor analysis -> response-surface optimization -> verification proposal
- queueing or simulation -> capacity recommendation -> stress test

## Do Not Use a Card If

- Its required inputs are unavailable.
- Its validation cannot be performed.
- Its expected figures and tables would be decorative rather than evidential.
- A simpler card answers the subquestion with fewer assumptions.
- The method cannot be connected to a concrete paper section.

## Minimum Evidence Contract

Every selected algorithm card should contribute at least three things:

- one mathematical object: equation, recurrence, objective, transition, or classifier definition
- one evidence artifact: table, figure, residual check, feasibility audit, or metric matrix
- one review artifact: limitation, sensitivity check, baseline comparison, or reproducibility note
