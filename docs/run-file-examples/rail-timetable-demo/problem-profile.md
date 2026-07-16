# Problem Profile

Run: example-rail-timetable

## Problem Image

This is a chained transport-service paper. Passenger-flow reading is only the first layer. The draft must turn demand structure into a service pattern, then into a timetable, and finally into audited operating advice.

## Task Family And Route Signals

- primary family: scheduling / timetable service planning
- support family: feasibility audit and scenario recommendation
- route signals: OD and section flow, route patterns, timetable recurrence, headway and dwell constraints, executable artifact burden

## Modeled Object

The modeled object is a rail transit service system consisting of passenger demand, service patterns, train operations, and station-level timing constraints.

## Decision Object

The final decision object is a selected operation plan and feasible timetable together with scenario-aware operating recommendations.

## Question Map

- Q1: audit flow and produce service-pattern candidates
- Q2: select the operation plan and generate the timetable
- Q3: verify feasibility and state the operating recommendation

## Evidence Burden

- descriptive flow charts alone are insufficient
- the paper needs a selected operation-plan artifact
- a machine-readable timetable is expected
- capacity, tracking, and dwell audits are mandatory for credibility

## Visual Burden

- early figure identifying the line/service object
- flow figure or section profile
- selected plan artifact
- timetable figure
- one or more audit artifacts

## Thinness Risks

- Q1 may stay descriptive and never feed the service decision tightly enough
- Q3 may look like an appendix check unless audit findings are integrated into recommendations

## Fake-Completion Risks

- generating a timetable plot without a real timetable artifact
- selecting a pattern by score only, without feasibility audits
- ending at “the timetable is feasible” without practical operating advice
