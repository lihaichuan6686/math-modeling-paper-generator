# Model Candidates

Run: calibration-2021E-classification

Read prompts/01_ideation.md before completing this file.

## Candidate 1

Problem type: conservative spectral classification baseline.

Model chain:

```text
raw spectrum
-> basic correction / normalization
-> PCA representation
-> LDA or SVM classifier
-> confusion matrix and target answer tables
```

Expected figures:

- representative raw spectra;
- PCA score plot;
- confusion matrix.

Expected tables:

- preprocessing summary;
- PCA component-retention table;
- classifier comparison;
- Q2/Q3/Q4 answer tables.

Validation:

- stratified holdout or cross-validation on labeled rows;
- macro-F1 and per-class/per-origin recall;
- target rows excluded from fitting.

Risks:

- may underfit subtle origin differences;
- PCA components can be mathematically clean but weakly interpretable;
- may look too simple unless spectral interpretation is written carefully.

## Candidate 2

Problem type: award-style preprocessing plus feature-selection route.

Model chain:

```text
raw spectrum
-> smoothing / normalization / scatter correction
-> feature-band selection or variable-importance ranking
-> classifier comparison: LDA / SVM / random forest
-> final model by subquestion
-> error and sensitivity audit
```

Expected figures:

- preprocessing effect comparison;
- selected wave-number bands or feature-importance plot;
- reduced-feature separation plot;
- confusion matrix.

Expected tables:

- preprocessing-route comparison;
- classifier metric table;
- selected-band or component table;
- final target-ID answer tables.

Validation:

- same split for every preprocessing/classifier combination;
- macro-F1, per-origin recall, and confusion evidence;
- sensitivity to selected feature count.

Risks:

- feature selection can leak labels if done before splitting;
- method stack can become decorative if each stage is not tied to an evidence artifact;
- random forest importance can be unstable with high-dimensional small-sample spectra.

## Candidate 3

Problem type: two-band fusion and hierarchical recognition route.

Model chain:

```text
MIR route
-> NIR route
-> band-level confidence comparison
-> fusion or confidence-gated decision
-> class-first / origin-second hierarchy for Attachment 4
-> consistency and conflict audit
```

Expected figures:

- NIR versus MIR representative spectra;
- band-level metric comparison;
- conflict-case visualization;
- final confusion matrices.

Expected tables:

- NIR-only, MIR-only, and fused metrics for Attachment 3;
- class-first/origin-second results for Attachment 4;
- target answer tables with confidence or reliability flags.

Validation:

- compare single-band and fused decisions;
- inspect cases where bands disagree;
- for Attachment 4, separately validate `Class` and `OP` models.

Risks:

- fusion can overfit if the labeled sample count is too small;
- confidence scores may look precise without calibration;
- hierarchy can propagate class errors into origin prediction.

## Recommendation

Recommended route:

```text
Candidate 2 as the main route, with Candidate 1 as mandatory baseline and Candidate 3 only for Q3/Q4 where the problem structure requires fusion or hierarchy.
```

Why selected:

- Candidate 1 is too thin for an award-style paper if used alone, but it is necessary as a sanity baseline.
- Candidate 2 best matches the excellent-paper pattern: preprocessing, feature representation, classifier comparison, and class-level diagnosis.
- Candidate 3 should be used selectively because Q3 explicitly has near-infrared plus mid-infrared data, and Q4 asks for both class and origin.

Rejected alternatives:

- pure clustering: weaker because labeled `OP` and `Class` evidence exists;
- one-model-for-all-attachments route: weaker because each attachment has different spectral bands and target labels;
- deep learning route: risky because sample size is small relative to feature dimension and contest papers need interpretable evidence.
