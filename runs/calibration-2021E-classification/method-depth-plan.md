# Method Depth Plan

Run: calibration-2021E-classification

Read knowledge/algorithms/method-depth-ladder.md and prompts/02_model_plan.md before completing this file.

## Depth Target

- target version: v1.2
- minimum target depth for major subquestions: Level 3
- preferred target for award-competitive sections: Level 4 when the route supports it

## Subquestion Depth Map

| Subquestion | Support layer | Main model | Result artifact | Validation/comparison layer | Current depth |
|---|---|---|---|---|---|
| Q1 | attachment schema, labels, feature audit | descriptive feature and data-risk analysis | data inventory, raw feature overview | missing/outlier/leakage check | Planned Level 3 |
| Q2 | preprocessing candidates | preprocessing plus representation selection | preprocessing comparison, feature-reduction figure | same-split metric comparison | Planned Level 3-4 |
| Q3 | feature representation and baseline | classifier comparison | classifier table, final model settings | macro-F1/per-class recall, confusion matrix | Planned Level 4 |
| Q4 | final prediction table if required | final identification rule | class-level reliability summary | claim-boundary and sensitivity check | Planned Level 3-4 |

## Upgrade Triggers

- If a row still reads like single method -> single result, upgrade it.
- If a decision artifact has no feasibility or scenario check, upgrade it.
- If final identification has no class-level error analysis, upgrade it.
- If preprocessing changes the final winner, report that sensitivity instead of hiding it.

## Thinness Risks

- Subquestion most likely to stop too early: final identification, if the draft reports only one score.
- Subquestion most needs a comparison or baseline: classifier selection.
- Support layer easiest to forget: preprocessing and feature-representation justification.
