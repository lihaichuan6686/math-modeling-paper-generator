# Methodology Checklist

Run: calibration-2021E-classification

Read docs/v1.3-methodology-runbook.md and prompts/02_model_plan.md before completing this file.

## Stable Question Map

- Q1: data and label audit.
- Q2: preprocessing and representation selection.
- Q3: classifier comparison.
- Q4: final identification and claim-boundary review.

## Modeled Object

High-dimensional samples after controlled preprocessing and representation selection.

## Decision Object

Category or origin identification rule with class-level reliability evidence.

## Object-First Figure

- Required: raw feature/spectrum overview or feature-matrix schematic before final result figures.

## Route Chain By Subquestion

| Subquestion | Route chain | Decision closure |
|---|---|---|
| Q1 | attachment inventory -> label/feature audit -> data-risk diagnosis | decide valid data roles and split policy |
| Q2 | preprocessing candidates -> separability/stability evidence -> selected preprocessing | decide which representation is safe to model |
| Q3 | feature reduction/selection -> classifier baselines -> metric comparison | select final classifier for evidence-based reasons |
| Q4 | final prediction -> confusion/per-class review -> bounded interpretation | state reliable and weak classes without overclaiming |

## Minimum Validation Artifacts

| Subquestion | Validation artifact | Comparison artifact |
|---|---|---|
| Q1 | missing/outlier/duplicate audit | raw attachment inventory |
| Q2 | same-split preprocessing metric check | preprocessing comparison table/figure |
| Q3 | baseline and final-model comparison | classifier comparison table |
| Q4 | confusion matrix or per-class diagnostics | claim-boundary review |

## Abstract Claim Boundary

The abstract may report final identification performance only with dataset scope, metric type, and the strongest class-level caveat.

## Conclusion Claim Boundary

The conclusion must distinguish reliable categories from weak/confusable categories and must not imply universal recognition outside the supplied sample system.

## Thinness Risks

- one global score replacing class-level evidence;
- preprocessing described as implementation detail;
- no rejected baseline model;
- conclusion stronger than validation.

## Machine-Like Rhythm Risks

- stacked method names without explaining why each stage is needed;
- repeated "we establish a model" phrasing;
- bullet-heavy results without interpretation;
- generic validation paragraph that does not inspect errors.
