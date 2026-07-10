# CUMCM Archetype Section Matrix

Purpose: connect CUMCM problem archetypes to the section emphasis, first artifact, and validation habit that should appear in the paper body.

This is a drafting bridge, not a full template.

## Archetype To Section Map

| Archetype | Section emphasis | First visible artifact | First core table | Validation habit |
|---|---|---|---|---|
| Type A: Evaluation and ranking | problem analysis, assumptions, results, validation | indicator or route overview figure | score/weight table | weight perturbation or rank stability |
| Type B: Evaluation to planning | problem analysis, model establishment, results, validation | evaluation-to-plan flow figure | candidate and decision table | feasibility and capacity audit |
| Type C: Forecast to decision | data processing, model establishment, results, validation | trend or fitted-vs-actual figure | forecast and scenario table | out-of-sample error and scenario propagation |
| Type C1: E-route production scheduling | data processing, model establishment, results, validation | representative-material or forecast figure | forecast-versus-actual table | service-level and capacity audit |
| Type C2: E-route monitoring and policy | data processing, model establishment, validation | diagnostic or workflow figure | monitoring or policy decision table | diagnostic check and intervention comparison |
| Type D: Classification or recognition | data processing, model establishment, validation | preprocessing or feature-flow figure | classifier comparison table | confusion matrix and leakage check |
| Type E: Physical or geometric optimization | problem analysis, model establishment, solution process, validation | object or coordinate schematic | parameter and result table | residual or physical feasibility check |
| Type F: Production scheduling or dynamic adjustment | model establishment, solution process, results, validation | baseline-to-update flow figure | before/after plan table | before-after comparison and stress test |
| Type G: Network, path, or coverage | problem analysis, model establishment, results, validation | network diagram | node/edge or route table | connectivity and capacity audit |
| Type H: Experiment factor and response surface | data processing, model establishment, validation | factor effect or contour plot | factor-level / response table | residual diagnostics and domain check |
| Type I: Rail transit timetable and service planning | problem analysis, data processing, model establishment, solution, results, validation | passenger-flow or route workflow figure | passenger/OD or timetable table | capacity, headway, and dwell audit |

## Drafting Rule

Use this order when a type is already known:

```text
archetype
-> section emphasis
-> first visible artifact
-> first core table
-> validation habit
```

If the paper still feels vague after route selection, this is the next layer to read.

## Type-Specific Reminders

### Type A

Do not stop at ranking; the paper must still make the recommendation consequence visible.

### Type B

The plan must be executable and auditable, not just ranked.

### Type C / C1 / C2

Forecasts are not the finish line. They must feed production, monitoring, or policy decisions.

### Type D

Preprocessing and split policy are part of the model.

### Type E

The coordinate frame or object must appear before optimization becomes meaningful.

### Type F

Show the update trigger and the before/after contrast.

### Type G

Make the node/edge construction reproducible before selecting routes or flows.

### Type H

Keep the fitted optimum inside the domain and justify it with evidence.

### Type I

Show the passenger flow, candidate pattern, and timetable recurrence before the final schedule is presented.

## Best Use

Read this note together with:

- `problem-type-paper-archetypes.md`
- `paper-family-matrix.md`
- `route-index.md`
- `latex/section-family-index.md`
- `20-30-page-paper-blueprint.md`
