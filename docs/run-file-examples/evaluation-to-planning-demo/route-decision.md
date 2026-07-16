# Route Decision

Run: example-evaluation-to-planning

## Selected Route Family

Evaluation to planning.

## Question Map

- Q1 builds the candidate layer
- Q2 converts the candidate layer into an executable plan
- Q3 checks whether the recommendation remains stable

## Route Chain By Subquestion

### Q1

indicator preprocessing -> weighting/evaluation -> ranking -> candidate threshold

### Q2

candidate set -> planning variables -> constrained optimization -> executable plan table

### Q3

baseline plan -> scenario perturbation -> recomputed outcomes -> comparison summary

## Why This Route Fits The Decision Object

The decision object is not a score, but an actionable supplier and ordering recommendation. Therefore the route must keep the evaluation layer, yet push beyond it into a constrained planning layer and then into a robustness layer.

## Why Rejected Routes Are Weaker

- ranking-only route: fails to answer the executable decision task
- planning-only route: hides why the chosen supplier set is credible
- complex prediction-heavy route: adds modeling burden without improving the final decision closure

## Required Evidence Chain

- supplier score artifact
- candidate selection artifact
- executable plan artifact
- feasibility status
- scenario comparison artifact

## Required Visuals

- object-first route figure showing evaluation feeding planning
- supplier score or ranking figure/table
- final plan table
- scenario comparison chart or table

## Expected Failure Modes

- unstable weights make the candidate set fragile
- cost-driven plans may ignore service stability
- scenario stress may reveal over-reliance on a small supplier set
