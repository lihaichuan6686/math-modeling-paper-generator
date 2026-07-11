# Figure Plan

Run: example-evaluation-to-planning

## Figure Strategy

Planned family emphasis:

- 1 route/workflow figure;
- 1 explanatory figure for indicator-to-plan bridge;
- 2 evidence/result figures;
- 1 validation figure.

## Planned Figures

| ID | Role | Purpose | Paper section | Source type | Tool | Input data/source/prompt | Output path | Caption draft | Status |
|---|---|---|---|---|---|---|---|---|---|
| F01 | route | show the evaluation-to-planning chain clearly | Method overview | schematic | Mermaid/TikZ | route statement and subquestion flow | `paper/figures/eval_plan_route.png` | Overall route from indicator evaluation to executable planning and scenario audit. | planned |
| F02 | explanatory | explain how ranked candidates become plan inputs | Model establishment | schematic | Mermaid/TikZ | candidate-selection logic and planning inputs | `paper/figures/eval_plan_bridge.png` | Bridge from supplier ranking to planning decision variables. | planned |
| F03 | evidence | show the score distribution or ranking contrast | Results | reproducible code | Python | supplier score output table | `paper/figures/eval_score_compare.png` | Comprehensive score comparison of candidate suppliers before plan selection. | planned |
| F04 | evidence | show plan consequence or cost structure | Results | reproducible code | Python | final plan and cost/loss outputs | `paper/figures/eval_plan_result.png` | Executable plan outcome and its main cost/service implication. | planned |
| F05 | validation | show scenario sensitivity of the final recommendation | Validation | reproducible code | Python | scenario comparison results | `paper/figures/eval_plan_sensitivity.png` | Scenario comparison of the recommended plan under perturbed demand or loss assumptions. | planned |

## Review Questions

1. Does one figure make the evaluation-to-planning bridge visible before long equations appear?
2. Does at least one figure show a code-generated planning consequence instead of only ranking?
3. Does the validation figure explain what changes under scenario perturbation?
