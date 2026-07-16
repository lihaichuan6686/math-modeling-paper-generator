# Methodology Checklist

Run: example-evaluation-to-planning

## Stable Question Map

- Q1 evaluation
- Q2 planning
- Q3 robustness

## Modeled Object

Supplier system under period demand and capability constraints.

## Decision Object

Selected supplier set plus executable ordering/allocation recommendation.

## Object-First Figure

- route figure: evaluation layer feeding planning layer and then scenario review

## Route Chain By Subquestion

| Subquestion | Route chain | Decision closure |
|---|---|---|
| Q1 | preprocess -> evaluate -> rank -> candidate set | credible supplier shortlist |
| Q2 | shortlist -> constrained plan -> audit | executable allocation plan |
| Q3 | baseline -> scenario rerun -> compare | stable practical recommendation |

## Minimum Validation Artifacts

| Subquestion | Validation artifact | Comparison artifact |
|---|---|---|
| Q1 | weight sensitivity | alternate weighting/ranking result |
| Q2 | feasibility audit | baseline candidate plan |
| Q3 | scenario table | pre/post disturbance comparison |

## Abstract Claim Boundary

- may claim supplier selection logic, executable plan, and scenario stability
- may not claim global optimality beyond tested scenarios

## Conclusion Claim Boundary

- may recommend the selected plan under stated assumptions
- must disclose sensitivity to weighting or scenario settings

## Thinness Risks

- planning interpretation may be too short if tables are not read in prose
- scenario section may become decorative if not connected back to the recommendation

## Machine-Like Rhythm Risks

- repeating “first, second, finally” scaffolding
- listing methods without closing them into decisions
