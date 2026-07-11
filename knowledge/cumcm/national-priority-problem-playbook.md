# National Priority Problem Playbook

Purpose: compress the most reusable CUMCM-first paper tactics into one fast playbook for Claude Code.

Use this when a new national-contest-style problem arrives and you need the shortest path from problem signal to paper strategy.

This file sits between the broad route index and the deep-reading notes.

## Fast Use

Read in this order:

1. identify the primary family below;
2. copy the corresponding paper rhythm into `runs/current/model-plan.md`;
3. copy the first-figure and first-table rule into `runs/current/figure-plan.md` and `runs/current/section-budget.md`;
4. check the linked official or deep-reading note before writing the full draft.

## Priority Families

| Family | Typical national-contest signals | Best paper rhythm | First strong figure | First core table | Must-have validation |
|---|---|---|---|---|---|
| Evaluation to planning | supplier/material/site screening followed by quantities, assignment, procurement, transport | screening -> scoring -> executable plan -> feasibility -> scenario | decision-flow or network overview | score-to-plan bridge table | feasibility and baseline comparison |
| Forecast to decision | historical demand, traffic, sales, load, hydrology, future planning | trend diagnosis -> forecast -> decision -> uncertainty propagation | trend or fitted-vs-actual figure | model comparison or forecast table | backtest plus scenario audit |
| Geometry / spatial design | coordinates, coverage, positioning, angle-only measurement, scene adjustment | scene setup -> derivation -> computed design -> replay/feasibility | object-first scene figure | symbol/parameter table | geometric consistency plus scene replay |
| Dynamic scheduling / update | cutting, rolling plan, capacity change, disruption, abnormal event | baseline plan -> update rule -> adjusted plan -> before/after loss | baseline-to-update workflow | baseline schedule table | constraint audit plus abnormal scenario comparison |
| Classification / recognition | spectra, labels, quality inspection, diagnosis, authenticity | preprocessing -> features -> model comparison -> error interpretation | preprocessing or feature-flow figure | classifier comparison table | split policy and confusion evidence |
| Rail / timetable service planning | passenger flow, OD, headway, timetable, large/small route, stop plan | passenger-flow audit -> service design -> objective system -> timetable -> feasibility -> scenario | section-flow or OD figure | operation-pattern table | capacity, tracking, dwell, scenario |

## Family Tactics

### 1. Evaluation to Planning

Most important habit:

```text
do not let the ranking table become the ending
```

What makes this family feel like a strong human team paper:

- the evaluation section is short but credible;
- the planning model is the true center of gravity;
- results are not one table but a chain of candidate -> selected -> executable -> audited artifacts.

Read next:

- `problem-type-paper-archetypes.md` Type B
- `official-paper-paradigms.md`
- `2021C-comparison-C066-C085-C169-C283.md`

### 2. Forecast to Decision

Most important habit:

```text
forecast uncertainty must enter the decision layer
```

What makes this family feel complete:

- the forecast is compared, not just announced;
- the final decision changes across scenarios or confidence ranges;
- the conclusion names both the decision and its uncertainty boundary.

Read next:

- `problem-type-paper-archetypes.md` Type C
- `e-route-comparison-2022-2023.md`
- `deep-reading-2022E014.md`
- `deep-reading-2022E029.md`
- `deep-reading-2023E176.md`

### 3. Geometry / Spatial Design

Most important habit:

```text
build one stable symbol world and extend it through every subquestion
```

What makes this family feel award-level:

- the opening figure immediately shows the scene;
- later subquestions extend the same coordinate logic rather than restarting;
- the final section converts formulas into a visible design, location, or coverage decision.

Read next:

- `problem-type-paper-archetypes.md` Type E and Type E1
- `deep-reading-2022B030.md`
- `spatial-measurement-comparison-B030-B086-B311.md`
- `official-paper-paradigms.md`

### 4. Dynamic Scheduling / Update

Most important habit:

```text
show the initial plan and the revised plan as separate evidence layers
```

What makes this family feel real:

- the update trigger is explicit;
- the revised plan is executable;
- the paper compares losses, delays, or utilization before and after the disturbance.

Read next:

- `problem-type-paper-archetypes.md` Type F
- `deep-reading-2021D017.md`

### 5. Classification / Recognition

Most important habit:

```text
preprocessing and feature construction are part of the model, not a warm-up
```

What makes this family feel trustworthy:

- the split policy is clear;
- comparison happens at class level, not only by one accuracy number;
- error cases are interpreted instead of hidden.

Read next:

- `problem-type-paper-archetypes.md` Type D
- `deep-reading-2021E014.md`

### 6. Rail / Timetable Service Planning

Most important habit:

```text
the operation plan must visibly drive the timetable
```

What makes this family feel complete:

- passenger-flow and service-pattern logic appear before timetable recurrence;
- the timetable is machine-readable, not just drawn;
- feasibility is checked through capacity, tracking, and dwell audits.

Read next:

- `problem-type-paper-archetypes.md` Type I
- `route-example-matrix.md`
- `next-iteration-action-matrix.md`

## Soft Rule For 20-30 Pages

A national-contest paper reaches full length naturally when each active family closes:

```text
question -> setup -> model -> result artifact -> interpretation -> validation
```

If the draft is short, first ask which loop is missing. Do not pad with generic prose.

## Best Use

Read this note together with:

- `route-index.md`
- `paper-family-matrix.md`
- `problem-type-paper-archetypes.md`
- `official-paper-paradigms.md`
- `../algorithms/problem-type-to-method.md`
