# Methodology Checklist

Run: example-rail-timetable

## Stable Question Map

- Q1 flow and service candidates
- Q2 plan and timetable
- Q3 feasibility and recommendation

## Modeled Object

Rail service system linking demand, service pattern, timetable recurrence, and feasibility constraints.

## Decision Object

Selected operation plan plus feasible timetable and operating recommendation.

## Object-First Figure

- early service-system figure showing flow -> service pattern -> timetable -> audit chain

## Route Chain By Subquestion

| Subquestion | Route chain | Decision closure |
|---|---|---|
| Q1 | flow audit -> candidate patterns -> tradeoff summary | candidate service set |
| Q2 | selected pattern -> operation plan -> recurrence | executable timetable |
| Q3 | timetable -> audits -> scenario comparison | practical operating recommendation |

## Minimum Validation Artifacts

| Subquestion | Validation artifact | Comparison artifact |
|---|---|---|
| Q1 | flow consistency or demand summary check | alternate pattern comparison |
| Q2 | timetable completeness and recurrence check | baseline plan comparison |
| Q3 | capacity/tracking/dwell audits | scenario recommendation table |

## Abstract Claim Boundary

- may claim selected service pattern, timetable generation, and audited feasibility
- may not claim universal optimality outside the tested scenarios and constraints

## Conclusion Claim Boundary

- may recommend the tested operation plan under stated passenger-flow and recurrence assumptions
- must disclose the dependence on scenario range and audit assumptions

## Thinness Risks

- candidate-pattern reasoning may be too compact
- audit evidence may sit too late and feel detached from the route decision

## Machine-Like Rhythm Risks

- reporting artifacts without operational interpretation
- stacking audit outputs without closing them into a recommendation
