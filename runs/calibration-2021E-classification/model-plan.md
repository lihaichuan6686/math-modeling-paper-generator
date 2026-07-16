# Model Plan

Run: calibration-2021E-classification

Read prompts/02_model_plan.md before completing this file.

## Page Structure Plan

| Section | Target pages | Notes |
|---|---:|---|
| Abstract | 1 | Write last |
| Problem restatement | 1-2 | |
| Problem analysis | 2-4 | |
| Assumptions and symbols | 1-2 | |
| Data processing | 2-4 | |
| Model and solution | 8-14 | |
| Results and validation | 3-5 | |
| Strengths, limitations, conclusion | 2-3 | |

## Subquestion Models

### Subquestion 1: Attachment 1 Category Recognition

Model chain:

```text
MIR spectral curve audit
-> preprocessing comparison
-> feature/band extraction
-> category-separation evidence
-> category-recognition rule
```

Variables:

- sample identifier `No`;
- MIR absorbance vector at 652-3999 `cm^-1`;
- inferred or provided category structure from the problem route;
- selected spectral features or components.

Objective/target:

- describe category-level spectral differences and establish a category-identification route.

Constraints/equations:

- no final category claim without visible separation evidence.

Solver/algorithm:

- spectral preprocessing;
- dimensionality reduction or feature selection;
- category-separation visualization and classifier baseline if labels are recoverable.

Expected outputs:

- MIR spectrum overview;
- category-separation evidence;
- category-identification explanation.

### Subquestion 2: Attachment 2 Origin Recognition

Model chain:

```text
MIR labeled/target split
-> preprocessing candidates
-> origin classifier comparison
-> fill 15 missing OP values
```

Variables:

- sample identifier `No`;
- origin label `OP`;
- MIR absorbance vector at 551-3998 `cm^-1`;
- target IDs: 3, 14, 38, 48, 58, 71, 79, 86, 89, 110, 134, 152, 227, 331, 618.

Objective/target:

- identify origin labels for target rows while reporting which origins are hard to separate.

Solver/algorithm:

- smoothing/normalization/correction routes as justified by spectra;
- PCA/LDA/feature-selection plus SVM, random forest, or LDA-style baselines.

Expected outputs:

- OP prediction table for 15 IDs;
- classifier comparison table;
- confusion or per-origin error evidence.

### Subquestion 3: Attachment 3 Two-Band Origin Recognition

Model chain:

```text
NIR route
-> MIR route
-> band-level comparison
-> fusion or agreement rule
-> fill 10 missing OP values
```

Variables:

- NIR absorbance vector at 4004-10000 `cm^-1`;
- MIR absorbance vector at 552-3999 `cm^-1`;
- origin label `OP`;
- target IDs: 4, 15, 22, 30, 34, 45, 74, 114, 170, 209.

Objective/target:

- decide whether NIR, MIR, or fused spectral evidence is more reliable for origin identification.

Solver/algorithm:

- band-specific classifiers;
- fusion by probability averaging, voting, stacked representation, or confidence-gated agreement.

Expected outputs:

- NIR-only, MIR-only, and fused comparison table;
- OP prediction table for 10 IDs;
- conflict-case note when bands disagree.

### Subquestion 4: Attachment 4 Category And Origin Recognition

Model chain:

```text
NIR partial-label split
-> category model
-> origin model
-> class-origin consistency audit
-> fill 7 target Class/OP pairs
```

Objective/target:

- identify both `Class` and `OP` for the target rows while naming the reliability boundary of each label type.

Expected outputs:

- prediction table for No 94, 109, 140, 278, 308, 330, 347;
- class-level and origin-level diagnostics;
- claim-boundary paragraph.
