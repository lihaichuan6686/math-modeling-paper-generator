# Minimal EDA Baseline Results

This is a route-calibration baseline, not the final modeling result.

## Leave-One-Out Baseline

| Task | LOO accuracy | Notes |
|---|---:|---|
| Q2 OP MIR | 0.248 | nearest-centroid baseline |
| Q3 OP NIR | 0.396 | nearest-centroid baseline |
| Q3 OP MIR | 0.380 | nearest-centroid baseline |
| Q3 OP fused | 0.510 | concat NIR+MIR nearest-centroid baseline |
| Q4 Class NIR | 0.891 | nearest-centroid baseline |
| Q4 OP NIR | 0.258 | nearest-centroid baseline |

## Output Files

- `artifacts/baseline_summary.csv`
- `artifacts/target_row_baseline_predictions.csv`
- `artifacts/attachment2_mir_mean_by_op.svg`
- `artifacts/attachment4_nir_mean_by_class.svg`

## Calibration Reading

- A simple nearest-centroid baseline is intentionally weak but useful as a sanity check.
- Any later stronger route must beat this baseline under a comparable split and explain remaining weak classes or origins.
- Q3 must compare NIR-only, MIR-only, and fused routes before claiming fusion is useful.