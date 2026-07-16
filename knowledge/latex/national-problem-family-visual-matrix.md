# National Problem-Family Visual Matrix

Purpose: map common CUMCM problem families to the visuals and tables they most likely need, in the order they should earn their place in the paper.

This note is the bridge between:

- family-level route selection;
- generic visual families;
- real figure/table planning for a contest-style paper.

Use it when `figure-plan.md` still feels too generic.

## How To Use

1. Identify the primary problem family.
2. Find the corresponding row below.
3. Plan the `must-have` figure and table first.
4. Add the `strongly recommended` artifacts next.
5. Avoid adding `nice-to-have` visuals before the must-have evidence exists.

## Matrix

| Problem family | Must-have first figure | Must-have first table | Strongly recommended visuals | Strongly recommended tables | Weak or misleading default |
|---|---|---|---|---|---|
| Evaluation and ranking | indicator relationship or route figure | weight/ranking table | ranking comparison chart, sensitivity plot | normalization table, sensitivity table | only one final ranking bar chart without weight logic |
| Evaluation to planning | route figure showing evaluation feeding planning | candidate-to-plan table | cost/capacity/service comparison figure, scenario figure | candidate table, executable plan table, feasibility table | stopping after a score heatmap or ranking figure |
| Forecast to decision | trend or fit-vs-actual figure | model comparison / forecast table | forecast interval plot, scenario decision figure | decision table under scenarios, error table | a smooth forecast curve with no error or decision artifact |
| Classification and recognition | feature/distribution figure or ROC family figure | model comparison table | confusion matrix, threshold curve, feature-importance figure | split-policy table, threshold summary table | only one ROC curve with no confusion or threshold logic |
| Geometry and engineering mechanics | object/scene schematic | parameter or symbol table | residual plot, feasible-vs-infeasible comparison | derived-parameter table, result summary table | optimization-result plot before the geometry is visible |
| Production planning and scheduling | workflow or resource-flow figure | schedule/production table | capacity timeline, scenario comparison figure | resource table, update-rule table, feasibility table | quantity table only, with no update logic or capacity evidence |
| Graph and network | network figure | node/edge/route table | bottleneck or coverage figure, comparison map | path table, bottleneck table | final route list without a reproducible network view |
| Queue and service systems | service-flow or queue diagram | utilization/waiting table | peak-vs-average comparison figure, bottleneck plot | intervention comparison table | only average waiting values with no congestion picture |
| Experimental factor optimization | factor-response plot or contour figure | coefficient/significance table | response surface, residual plot | optimum-condition table, domain-check table | a reported optimum without contour or domain evidence |
| Rail / timetable service planning | service-system or line figure | candidate-pattern or selected-plan table | passenger-flow figure, timetable figure, audit figure | full timetable sample, capacity/tracking/dwell audit tables | timetable picture only, without auditable tables |
| Production-route E | demand/forecast figure | production or service-level table | inventory/service figure, scenario capacity figure | forecast table, rolling production table, support-rate table | forecast chart only, with no production decision table |
| Monitoring-route E | process/diagnostic figure | monitoring or policy table | abruptness/periodicity figure, intervention-effect figure, long-horizon figure | comparison table, policy trigger table | diagnostic plots stacked together without a monitoring policy artifact |

## Planning Order By Family

### Evaluation and ranking

```text
indicator relation -> ranking table -> sensitivity figure/table
```

### Evaluation to planning

```text
route figure -> candidate table -> executable plan table -> feasibility figure/table -> scenario figure/table
```

### Forecast to decision

```text
trend/fit figure -> forecast table -> decision table -> uncertainty/scenario figure
```

### Classification and recognition

```text
feature/distribution figure -> comparison table -> confusion/threshold figure
```

### Geometry and engineering mechanics

```text
scene schematic -> parameter table -> result table -> residual/feasibility figure
```

### Production planning and scheduling

```text
workflow figure -> resource/schedule table -> capacity figure -> scenario comparison
```

### Graph and network

```text
network figure -> node/route table -> bottleneck/coverage figure
```

### Queue and service systems

```text
queue diagram -> waiting/utilization table -> peak comparison figure
```

### Experimental factor optimization

```text
factor-response figure -> coefficient table -> contour/response surface -> optimum table
```

### Rail / timetable service planning

```text
system figure -> flow figure -> selected-plan table -> timetable figure -> audit tables/figures
```

### Production-route E

```text
demand/forecast figure -> forecast table -> production table -> service/inventory figure -> scenario table
```

### Monitoring-route E

```text
process/diagnostic figure -> monitoring/policy table -> intervention comparison figure -> long-horizon consequence figure
```

## Review Questions

Before drafting, ask:

1. Does the first strong figure identify the object or route?
2. Does the first strong table support modeling, not decoration?
3. Does this family already have a visible decision artifact?
4. Does this family already have a visible validation artifact?
5. Am I drawing a visually pleasant figure that does not actually carry the family's evidence burden?

## Best Use

Read this note together with:

- `visual-family-index.md`
- `table-family-index.md`
- `section-family-index.md`
- `../cumcm/national-problem-family-methodology-matrix.md`
- `../../docs/figure-plan-template.md`
