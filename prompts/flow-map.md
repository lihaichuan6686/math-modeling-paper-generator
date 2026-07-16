# Prompt Flow Map

Purpose: make the prompt chain easy to execute from a problem statement to a handoff-ready v1.4 draft.

This is the prompt-layer execution map.

## Main Prompt Chain

```text
intake
-> ideation
-> model plan
-> Playwright public research
-> online consensus check
-> implementation
-> writing
-> review
-> quality audit
-> revision if needed
```

## What Each Stage Must Leave Behind

| Stage | Main question | Main output | Next stage depends on |
|---|---|---|---|
| Intake | What is the problem and what is missing? | problem-analysis, data-inventory, initial artifact ledger | stable subquestions and route signals |
| Ideation | Which routes could solve it? | model-candidates | route-family candidates and risks |
| Model plan | Which route is best? | model-plan, verification-plan, figure-plan | one selected route and visible artifacts |
| Playwright public research | What do public online sources visibly say about this problem? | online-consensus-notes | public sources, access limits, common interpretations, traps, and rough ranges |
| Online consensus | What do public contest-circle signals suggest we may be missing? | online-consensus-notes (updated), run file changes | route sanity, traps, rough ranges, and external reflection |
| Implementation | How do we compute it? | code, tables, figures, run outputs | reproducible outputs and file paths |
| Writing | How do we explain it? | sectioned LaTeX draft | section order and evidence references |
| Review | What is weak or missing? | review file | fixes, warnings, and traceability gaps |
| Quality audit | Does the run meet the gate? | machine-gate result | pass/fail state and remaining repairs |
| Revision | How do we repair the flagged weak points? | updated draft and refreshed planning files | stronger density, method depth, and closure |

## Route To Prompt Rule

Use the route index and paper-family matrix before model planning, then let the prompt chain produce the artifacts in order:

```text
route index
-> paper family matrix
-> generation loop
-> prompt flow
-> section map
-> completion gate
```

## Stage Discipline

- Intake should identify problem signals, not choose a favorite algorithm.
- Ideation should offer more than one candidate route.
- Model plan should choose one route and explain the rejection of the others when needed.
- Playwright public research should browse normally accessible public pages; record access limits; never use cookies, hidden APIs, ZSE/internal endpoints, or login-wall bypasses.
- Online consensus should check public discussion after the initial plan and before final writing; use it for reflection, not answer copying.
- Implementation should generate visible artifacts before prose expands.
- Writing should follow the section map rather than freestyle order.
- Review should name concrete risks, not vague praise.
- Quality audit should decide whether the run is ready for research review.
- Revision should repair the highest-value weaknesses first rather than rewriting the whole paper.

## Best Use

Read this note together with:

- `README.md`
- `00_intake.md`
- `01_ideation.md`
- `02_model_plan.md`
- `11_online_consensus_check.md`
- `13_platform_research.md`
- `03_implementation.md`
- `04_writing.md`
- `05_review.md`
- `06_quality_review.md`
- `09_revision_v1_2.md`
- `../knowledge/cumcm/generation-loop.md`
- `../knowledge/master-map.md`
