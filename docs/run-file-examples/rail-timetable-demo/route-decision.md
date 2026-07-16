# Route Decision

Run: example-rail-timetable

## Selected Route Family

Rail / timetable service planning.

## Question Map

- Q1 flow audit and candidate service patterns
- Q2 operation-plan selection and timetable generation
- Q3 feasibility audit and operating recommendation

## Route Chain By Subquestion

### Q1

OD/section-flow audit -> service-pattern candidates -> cost/service tradeoff summary

### Q2

selected service pattern -> operation plan -> recurrence logic -> full timetable artifact

### Q3

timetable artifact -> capacity/tracking/dwell audits -> scenario comparison -> recommendation

## Why This Route Fits The Decision Object

The real decision object is not only “what the flow looks like,” but “what operation plan should be used and whether it can run safely and credibly.” Therefore the route must carry the paper from demand structure to executable timetable and audit evidence.

## Why Rejected Routes Are Weaker

- timetable-first route: skips service-pattern reasoning
- flow-only route: fails to produce an executable operating answer
- cost-only route: hides service feasibility and passenger burden

## Required Evidence Chain

- passenger-flow profile
- candidate-pattern comparison
- selected operation-plan artifact
- full timetable artifact
- capacity/tracking/dwell audit artifacts
- scenario recommendation artifact

## Required Visuals

- object-first service or line figure
- passenger-flow figure
- cost/service comparison figure
- timetable figure
- audit table or scenario figure

## Expected Failure Modes

- service pattern chosen without enough flow justification
- timetable recurrence looks elegant but fails headway or dwell checks
- recommendations ignore how scenario changes alter feasibility margins
