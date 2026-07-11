# Evaluation-to-Planning Claim Map

Purpose: show how abstract and conclusion claims should be tied to artifacts for an evaluation-to-planning v1.2 paper.

## Claim Rule

No sentence belongs in the abstract or conclusion unless it can be traced to:

1. a generated table, figure, or machine-readable output;
2. an entry in `artifact-ledger.md`;
3. a stable subquestion in the paper question map.

## Abstract Claim Map

| Claim slot | Claim type | What the sentence should do | Expected evidence source | Ledger tie |
|---|---|---|---|---|
| A1 | task framing | state that the paper solves screening plus executable planning | `problem-analysis.md`, route note | optional narrative tie |
| A2 | Q1 evaluation | state how suppliers were scored or screened and what retained set emerged | ranking table, candidate table | K01 or equivalent evaluation entry |
| A3 | Q2 plan result | state that the retained set was converted into an executable plan and summarize the main plan outcome | plan table, cost/service summary | K02 or equivalent decision entry |
| A4 | Q3 validation | state what feasibility or scenario evidence supports the recommendation | feasibility audit, scenario table, sensitivity figure | K03 or validation entries |
| A5 | final recommendation | state the final recommendation boundary in one sentence | conclusion-ready synthesis from plan plus audit | combined ledger references |

## Conclusion Claim Map

| Claim slot | Claim type | What the sentence should do | Expected evidence source | Ledger tie |
|---|---|---|---|---|
| C1 | Q1 close-out | restate which suppliers remain credible and why they enter planning | ranking and candidate artifacts | evaluation entries |
| C2 | Q2 close-out | restate the executable plan and its operational meaning | plan table and summary outputs | decision entries |
| C3 | Q3 close-out | restate the robustness boundary of the plan | feasibility audit, scenario outputs | validation/scenario entries |
| C4 | limitation boundary | name the main scope limit without inventing new evidence | strengths/limitations section | no unsupported numbers |

## Safe Sentence Pattern

Use this rhythm:

```text
artifact-backed result
-> what it means for the subquestion
-> why the recommendation is credible or bounded
```

Avoid this rhythm:

```text
method name
-> method praise
-> recommendation with no cited artifact
```

## Common Failure Checks

Fail the draft if:

- the abstract names methods but gives no result closure;
- the conclusion states a recommendation not listed in the ledger;
- the recommendation sounds stronger than the feasibility/scenario evidence allows;
- one of the three subquestions disappears between abstract and conclusion.
