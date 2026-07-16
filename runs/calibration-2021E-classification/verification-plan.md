# Verification Plan

Run: calibration-2021E-classification

| ID | Target | Method | Metric | Evidence file | Status |
|---|---|---|---|---|---|
| V01 | Split policy | Holdout or cross-validation plan with no leakage across same-source samples | train/test definition, folds, random seed | `runs/calibration-2021E-classification/data-inventory.md` | Planned |
| V02 | Preprocessing comparison | Compare raw or lightly cleaned features against at least two preprocessing routes | validation accuracy, macro-F1, class stability | future table under `paper/tables/` | Planned |
| V03 | Feature representation | Compare PCA/LDA/feature-selection style representations under the same split | retained components/features, separability, metric change | future figure under `paper/figures/` | Planned |
| V04 | Classifier baseline | Compare at least two candidate classifiers under the same preprocessing and split | accuracy, macro-F1, per-class recall | future classifier comparison table | Planned |
| V05 | Final class-level diagnosis | Inspect confusion matrix or per-class error table | confused pairs, weak classes, scope limits | future confusion-matrix figure/table | Planned |
| V06 | Claim-boundary check | Match abstract and conclusion claims to validated sample scope | unsupported claim count | `reviews/calibration-2021E-classification.md` | Planned |
| V07 | Target-row isolation | Ensure missing `OP`/`Class` rows are excluded from supervised fitting | leakage audit by target ID list | `data-schema-summary.md` plus model code | Planned |
| V08 | Band-fusion audit | For Attachment 3, compare NIR-only, MIR-only, and fused evidence | agreement rate, conflict cases, final OP stability | future band-fusion table | Planned |

## Sensitivity Analysis

- Vary preprocessing choice and report whether the final classifier choice changes.
- Vary feature count or component count when using dimensionality reduction.
- If class imbalance appears, compare overall accuracy with macro-F1 or per-class recall.
- For Q3, compare near-infrared-only, mid-infrared-only, and fused decisions.

## Baseline or Sanity Checks

- Majority-class or simple linear baseline if labels are imbalanced.
- Raw-feature baseline before stronger preprocessing.
- Same-split comparison for every candidate route.
- Confusion matrix must be reviewed before accepting any "best model" sentence.
