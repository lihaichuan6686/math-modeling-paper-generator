# Problem Profile

Run: example-evaluation-to-planning

## Problem Image

This is a layered decision problem. The paper begins with multi-indicator judgment over suppliers, but it cannot end there. The judged supplier set must feed an executable planning layer that survives feasibility and scenario checks.

## Task Family And Route Signals

- primary family: evaluation to planning
- support family: scenario robustness
- route signals: many indicators, different units, final executable decision required, planning feasibility matters more than a pure ranking

## Modeled Object

The modeled object is a supplier system with heterogeneous capability, reliability, and cost indicators, connected to a period-by-period demand satisfaction task.

## Decision Object

The final decision object is a selected supplier set plus an executable ordering/allocation plan, not only a score ranking.

## Question Map

- Q1: construct the evaluation layer and determine the candidate supplier set
- Q2: convert the candidate set into an executable planning model
- Q3: test whether the planning recommendation remains credible under disturbance

## Evidence Burden

- a score table alone is insufficient
- the paper needs at least one executable plan artifact
- feasibility and scenario evidence are required to make the recommendation credible

## Visual Burden

- one early object-first diagram or table explaining the evaluation-to-planning chain
- one score/ranking artifact
- one final-plan artifact
- one scenario or sensitivity artifact

## Thinness Risks

- Q1 may become too long and Q2 too short if the paper over-explains scoring
- Q3 may collapse into a token paragraph if scenario evidence is not planned early

## Fake-Completion Risks

- stopping at ranking
- showing a plan without feasibility checks
- calling a supplier choice “optimal” without scenario comparison
