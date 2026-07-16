# Baseline Observations: 2021E

Purpose: record what the first minimal baseline proves for route calibration.

The baseline uses a nearest-centroid classifier after z-score normalization. It is intentionally simple and should not be treated as the final model.

## Baseline Signals

| Task | Leave-one-out accuracy | Calibration meaning |
|---|---:|---|
| Q2 OP MIR | 0.248 | Single-band origin recognition is hard and needs stronger feature engineering. |
| Q3 OP NIR | 0.396 | Near-infrared alone is weak but carries signal. |
| Q3 OP MIR | 0.380 | Mid-infrared alone is also weak, similar to NIR for this attachment. |
| Q3 OP fused | 0.510 | Fusion improves the simple baseline and must be explicitly audited in a strong paper. |
| Q4 Class NIR | 0.891 | Category recognition is much easier than origin recognition. |
| Q4 OP NIR | 0.258 | Origin prediction remains the main weak link. |

## Methodology Lessons

1. Category and origin identification must be separated in the writing.
2. A generated paper should not use a single global accuracy to summarize all tasks.
3. Q3 requires a band-fusion comparison before making any claim about combined spectra.
4. Q2 and Q4 need stronger origin-level evidence, not just a more prestigious classifier name.
5. Final answer tables should include reliability language or at least a nearby error-analysis paragraph.

## Pressure-Test Failure Signals To Watch

- `claim_overreach`: claiming "accurate origin identification" from weak OP evidence.
- `validation_gap`: reporting Q4 Class accuracy while hiding Q4 OP weakness.
- `artifact_gap`: omitting band-level comparison for Q3.
- `paragraph_density_misfit`: treating all subquestions as equally easy.

## Next Modeling Route

Use the baseline as the floor, then test:

```text
spectral preprocessing
-> feature selection / dimensionality reduction
-> classifier comparison
-> per-origin diagnostics
-> target answer tables
```

The next route is useful only if it beats the baseline and explains why origin recognition remains difficult.
