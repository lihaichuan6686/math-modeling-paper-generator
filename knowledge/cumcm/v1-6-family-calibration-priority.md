# v1.6 Family Calibration Priority

Purpose: turn the broad CUMCM problem-family index into a practical v1.6 calibration queue. This note helps the agent choose what to test or strengthen next without overfitting one narrow topic.

Use after:

- `knowledge/cumcm/problem-understanding-framework.md`
- `knowledge/cumcm/national-problem-family-methodology-matrix.md`
- `knowledge/algorithms/v1-5-route-upgrade-atlas.md`
- `knowledge/algorithms/v1-6-method-chain-evidence-index.md`

## Source Signals

Local source inventory:

- CUMCM problem statements exist from 1992-2023 in the local national-contest problem archive.
- Recent 2021-2023 folders include PDF problem statements plus CSV/XLSX/RAR attachments, reinforcing that many modern tasks are data-and-artifact-heavy.
- Existing family notes already cover evaluation, prediction, optimization, classification, geometry, graph/network, queue/service, experimental optimization, production scheduling, monitoring/policy, and rail/timetable.

The missing v1.6 calibration layer is not a new encyclopedia. It is a calibration priority sheet:

```text
Which families should be tested first, and what failure should each test expose?
```

## Priority Families

| Priority | Family | Why it must be calibrated | Required body artifact | Required validation artifact | Non-human failure to catch |
|---:|---|---|---|---|---|
| 1 | evaluation to planning | many weak papers rank objects but never produce an executable decision | score-to-plan bridge table plus final decision table | feasibility, budget, capacity, or scenario audit | ranking paper pretending to be a planning paper |
| 2 | forecast to decision | forecasts are easy to generate but often do not affect a decision | forecast comparison plus downstream decision table | backtest, residual, scenario, or uncertainty propagation | forecast plot followed by generic recommendation |
| 3 | production/resource planning | recent CUMCM tasks often include large attachments and operational constraints | production/order/schedule table | constraint satisfaction and stress or disturbance audit | quantities listed without feasibility proof |
| 4 | classification/recognition | classifiers can look impressive with one accuracy number | comparison table plus decision or threshold rule | split policy, confusion matrix, ROC/PR, or error-case analysis | algorithm leaderboard with no usable judgment rule |
| 5 | geometry/engineering mechanics | strong papers depend on object definition before solving | scene/coordinate figure plus parameter result table | residual, perturbation, or physical feasibility replay | formulas before the physical object is visible |
| 6 | graph/network/service | route or service answers require reproducible construction | network/service graph plus route/flow/policy table | bottleneck, capacity, disruption, or peak stress check | network picture without edge definitions or audits |
| 7 | monitoring/policy | diagnostics are tempting but incomplete without intervention logic | diagnostic figure plus policy/rule table | false alarm/miss, long-horizon, or intervention comparison | many plots but no policy closure |
| 8 | experimental factor optimization | easy to overstate mathematical optima outside experimental regions | coefficient/optimum table plus response surface | residual, domain boundary, holdout, or sensitivity check | optimum outside credible experimental domain |

## Calibration Batch Design

For v1.6 calibration, do not claim route maturity until at least three different reasoning modes have been tested:

```text
data decision mode: evaluation-to-planning or production/resource planning
time/uncertainty mode: forecast-to-decision or monitoring/policy
structure/physics mode: geometry, graph/network/service, or classification/recognition
```

Each calibration run should fill:

- `runs/current/problem-profile.md`
- `runs/current/route-decision.md`
- `runs/current/method-depth-plan.md`
- `runs/current/section-rhythm-budget.md`
- `runs/current/artifact-ledger.md`
- `reviews/final-v16-check.md`
- `reviews/calibration-v16-<run-name>.md`

## Route Selection Guard

When a new problem arrives, first decide which family failure it most risks.

Examples:

- If the task asks for a plan but the first idea is a score, force `evaluation -> planning`.
- If the task asks for future action but the first idea is a forecast, force `forecast -> decision`.
- If the task has many labels/features, force `classification -> judgment rule`, not just accuracy.
- If the task has coordinates or physical constraints, force `object/coordinate frame -> solution -> residual replay`.
- If the task has nodes, flows, service, or congestion, force reproducible construction and bottleneck audit.

This prevents the route from becoming:

```text
method name -> output table -> generic conclusion
```

## Paper-Structure Implication

Each priority family should change the paper shape:

| Family group | Early section signal | Middle-body signal | Tail signal |
|---|---|---|---|
| evaluation/planning | indicator and decision object appear before weights | score becomes plan with feasibility audit | conclusion names executable recommendation |
| forecast/monitoring | uncertainty and downstream use appear before model choice | forecast/diagnosis becomes policy or action | limitations name risk under future shifts |
| resource/scheduling | constraints and capacity appear before optimization | plan tables alternate with audits | appendix maps scripts to each plan artifact |
| classification | split/leakage and feature diagnosis appear before classifier | error cases and thresholds appear near results | appendix provides code but body states the rule |
| geometry/network | object diagram and construction rules appear before algorithms | residual/bottleneck checks appear after solution | conclusion respects physical/network limits |

## Missing-Card Watchlist

The existing algorithm card layer is strongest for common planning, evaluation, and timetable-style routes. Future cards should be added only when a real calibration run exposes repeated weakness.

Watchlist:

- monitoring-policy with false alarm/miss tradeoff;
- experimental response-surface optimization with domain-boundary checks;
- geometry/engineering residual replay;
- graph/network bottleneck and disruption audit;
- classification threshold-to-policy conversion.

Do not create cards for rare one-off topics unless they generalize to one of these families.

## Review Questions

1. Which priority family is this problem closest to?
2. Which non-human failure is most likely if the agent writes too fast?
3. What artifact proves the final decision exists?
4. What validation artifact proves the result is not just a computation?
5. Which existing algorithm card or route note should be read next?
6. If no card exists, is the gap broad enough to deserve a new card?
