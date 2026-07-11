# Model Plan

Run: example-rail-timetable

## Route Statement

This run uses the `rail / timetable service planning` family:

```text
OD and section-flow audit -> candidate service patterns -> selected operation plan -> timetable recurrence -> feasibility audit -> scenario recommendation
```

## Page Structure Plan

| Section | Target pages | Notes |
|---|---:|---|
| Abstract | 1.0 | flow -> service pattern -> timetable -> audit closure |
| Problem restatement | 1.0 | concise task rewrite |
| Problem analysis | 2.5-3.0 | explain why operation plan must drive timetable |
| Assumptions and symbols | 1.5 | operation variables must stay stable |
| Data processing | 2.5-3.5 | OD, section flow, and parameters |
| Model and solution | 8.0-9.5 | service design plus recurrence logic |
| Results and validation | 5.5-6.5 | plan output, timetable output, and audits |
| Strengths, limitations, conclusion | 1.5-2.0 | concise, operational ending |

## Subquestion Models

### Subquestion 1: Passenger Flow And Candidate Service Patterns

Model chain:

```text
OD/section-flow audit -> service-pattern candidates -> cost/service metric table
```

Variables:

- flow by section and time;
- candidate service-pattern indicators;
- cost/service metric components.

Objective/target:

- identify a service-pattern candidate set that reflects both demand and operating burden.

Constraints/equations:

- section flow aggregation;
- service-pattern definition rules;
- metric construction before selection.

Solver/algorithm:

- descriptive flow analysis plus multi-criteria or weighted comparison of candidate patterns.

Expected outputs:

- passenger-flow profile;
- candidate pattern table;
- objective-component summary table.

### Subquestion 2: Selected Operation Plan And Timetable Generation

Model chain:

```text
selected service pattern -> operation plan -> arrival/departure recurrence -> timetable artifact
```

Variables:

- selected operation pattern variables;
- arrival/departure times;
- headway and dwell control values.

Objective/target:

- generate a timetable that is consistent with the chosen operation plan.

Constraints/equations:

- recurrence equations for stations/trains;
- headway and dwell bounds;
- route-pattern consistency rules.

Solver/algorithm:

- weighted or Pareto selection for operation plan;
- deterministic timetable recurrence for station-by-station generation.

Expected outputs:

- selected operation-plan table;
- timetable sample and full timetable artifact;
- timetable figure.

### Subquestion 3: Feasibility And Operating Recommendation

Model chain:

```text
timetable output -> capacity/tracking/dwell audits -> scenario comparison -> final recommendation
```

Variables:

- section utilization metrics;
- tracking interval audit values;
- dwell-time audit values;
- scenario perturbation parameters.

Objective/target:

- show that the selected timetable is feasible and interpretable under tested scenarios.

Constraints/equations:

- audit rules derived from capacity, tracking, and dwell constraints;
- same service structure under perturbed scenarios.

Solver/algorithm:

- audit tables from generated timetable outputs;
- scenario reruns or parametric comparison.

Expected outputs:

- capacity audit;
- tracking audit;
- dwell audit;
- scenario recommendation table.

## Primary Validation Logic

- compare selected plan against at least one baseline candidate;
- audit every generated timetable through capacity, tracking, and dwell checks;
- summarize how scenario changes affect the recommendation.
