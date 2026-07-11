# Evaluation-to-Planning Review Case

Purpose: show how to review a weak evaluation-to-planning draft that looks structurally complete but is still below v1.2.

## Draft Situation

Assume the draft has these visible weaknesses:

- the paper shows a ranking table but only a thin planning result;
- the abstract names methods but does not close all three subquestions;
- the scenario section exists but is only one short paragraph;
- the conclusion sounds stronger than the feasibility evidence allows.

## Example Review Output

```markdown
# Paper Quality Review

Run: example-evaluation-to-planning
Reviewed: example review case

## Overall Status

Needs revision

## Critical Findings

| ID | Location | Status | Evidence | Risk | Required repair |
|---|---|---|---|---|---|
| C01 | `08_results.tex`, `09_validation.tex` | Fail | The draft shows a ranking artifact and a thin plan artifact, but the feasibility and disturbed-scenario evidence are too small to support the final recommendation. | The paper may look complete while still ending at `screening -> partial plan`. | Expand the executable-plan evidence and add a real feasibility audit plus a non-token scenario artifact. |
| C02 | abstract, conclusion, `artifact-ledger.md` | Fail | The conclusion makes a strong final recommendation, but the corresponding validation boundary is not clearly listed in the ledger. | Abstract and conclusion claims may outrun artifact-backed evidence. | Rebuild the abstract and conclusion against the claim map and ledger entries before handoff. |

## Important Findings

| ID | Location | Status | Evidence | Risk | Required repair |
|---|---|---|---|---|---|
| I01 | `02_analysis.tex` | Warn | The route justification correctly rejects ranking-only logic, but the later sections do not fully earn that stronger route. | The paper promises a richer chain than the results actually deliver. | Make the plan layer and validation layer visibly stronger so the route promise is fulfilled. |
| I02 | `08_results.tex` | Warn | The ranking table is interpreted clearly, but the plan artifact is not given equal interpretive depth. | The screening layer visually dominates the decision layer. | Add a fuller interpretation paragraph after the plan artifact and state what operational question it resolves. |
| I03 | `09_validation.tex` | Warn | Validation is present but reads like a short add-on rather than a real credibility layer. | Contest-grade trust is weakened. | Split validation into feasibility audit and scenario comparison, and interpret both explicitly. |

## Warnings

| ID | Location | Status | Evidence | Risk | Suggested repair |
|---|---|---|---|---|---|
| W01 | abstract | Warn | Method names appear quickly, but result closure per subquestion is incomplete. | The draft sounds more advanced than it is. | Rewrite the abstract so each subquestion closes with method plus result. |
| W02 | figures/tables | Warn | The ranking artifact is more visible than the executable-plan artifact. | Visual balance reinforces the wrong center of gravity. | Add one stronger plan or feasibility visual and redistribute emphasis. |

## Evidence Checked

- route logic and question map
- ranking and plan result artifacts
- validation presence
- abstract and conclusion claim support

## Evidence Missing Or Not Checked

- compiled PDF page rendering
- full scenario output files
- final machine gate output

## Required Repairs Before Pass

1. Strengthen the plan and validation artifacts so the paper no longer ends effectively at ranking.
2. Rebuild abstract and conclusion claims against the ledger and claim map.
3. Make the decision layer and validation layer at least as visible as the screening layer.

## Human Verification Needed

- Confirm whether the scenario range is intended for research illustration or a real problem run.

## Responsible-Use Notes

- This draft is acceptable only as a research draft after the missing evidence is repaired and disclosed.
```

## What This Case Teaches

1. A paper can look orderly and still fail because the route closes too early.
2. The right review should target the missing decision and validation burden, not just ask for "more detail".
3. Abstract and conclusion overclaiming should be treated as an evidence problem, not merely a writing problem.

