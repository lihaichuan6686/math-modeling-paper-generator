# Route Decision

Run: example-dynamic-scheduling

## Selected Route Family

Dynamic scheduling / update.

## Question Map

- Q1 builds the baseline schedule
- Q2 revises the schedule under disturbance
- Q3 compares the results and forms the final recommendation

## Route Chain By Subquestion

### Q1

task/resource reading -> baseline model -> feasible baseline schedule

### Q2

disturbance trigger -> updated constraints/objective -> revised schedule

### Q3

before/after metrics -> feasibility audit -> recommendation summary

## Why This Route Fits The Decision Object

The decision object is an updated operational plan. Therefore the route must preserve a credible baseline, explain the trigger for revision, and then show what the revised plan achieves relative to the baseline.

## Why Rejected Routes Are Weaker

- baseline-only route: fails to answer the disturbance task
- update-only route: hides what was changed or preserved
- narrative response route: produces no machine-readable schedule artifact

## Required Evidence Chain

- baseline schedule artifact
- disturbance or rolling-trigger explanation
- revised schedule artifact
- before/after comparison artifact
- feasibility audit artifact

## Required Visuals

- route workflow figure
- baseline schedule table or Gantt-like artifact
- revised schedule table or Gantt-like artifact
- comparison table/plot
- feasibility or stress artifact

## Expected Failure Modes

- the update rule is too implicit
- revised schedules improve one metric while silently violating another
- the comparison prose is weaker than the comparison artifacts
