# Problem Profile

Run: example-dynamic-scheduling

## Problem Image

This is a disturbance-driven operational planning problem. The paper cannot stop at one static schedule, because the core value lies in how the plan is revised after an abnormal event or rolling update trigger appears.

## Task Family And Route Signals

- primary family: dynamic scheduling / update
- support family: stress comparison
- route signals: baseline schedule required, disturbance or rolling trigger appears later, updated plan must remain feasible, before/after comparison matters

## Modeled Object

The modeled object is a time-evolving production or service system with jobs, resources, capacities, and disturbance scenarios.

## Decision Object

The final decision object is an executable updated schedule or revised operational rule, not only a baseline optimization result.

## Question Map

- Q1: build the baseline schedule under normal conditions
- Q2: design the update or rolling adjustment rule after disturbance
- Q3: compare the revised schedule against the baseline and summarize the operational recommendation

## Evidence Burden

- a baseline schedule alone is insufficient
- the paper needs a revised schedule artifact
- before/after comparison evidence is required
- feasibility or constraint-audit evidence must stay visible after adjustment

## Visual Burden

- one early workflow figure showing baseline-to-update chain
- one baseline schedule artifact
- one revised schedule artifact
- one comparison artifact
- one feasibility or stress artifact

## Thinness Risks

- Q1 may become too dominant if the update layer is not planned early
- Q2 may collapse into an algorithm list if the trigger is not explained
- Q3 may become a token comparison sentence if differences are not quantified

## Fake-Completion Risks

- presenting only the baseline plan
- revising the schedule without stating what objective changed
- claiming robustness without abnormal-case evidence
