# Deep Reading: 2021 E014 Spectral Classification and Origin Identification

Source:

```text
2021-official-first-pass.md
```

This note deepens the first-pass reading for the 2021 E paper on traditional Chinese medicine classification and origin identification. The original PDF file is not separately stored in the current workspace, so this note synthesizes the available first-pass evidence into generator rules and review criteria.

## Basic Profile

- Year/problem: 2021 E
- Topic: spectral classification, preprocessing, feature extraction, origin identification
- Problem type: classification/recognition, high-dimensional signal processing, model comparison
- Main methods:
  - Savitzky-Golay smoothing
  - MSC correction
  - SNV normalization
  - PCA
  - LDA
  - SVM
  - random forest
  - feature selection
- Main evidence form:
  - preprocessing flow
  - feature-reduction figures
  - classifier comparison tables
  - accuracy/F1-style evaluation
  - confusion matrix or similar class-level diagnostics

## Why This Paper Matters

The paper is a good route example because it is not just "use a classifier." It shows the full classification chain:

```text
raw spectrum
-> preprocessing
-> dimensionality reduction / feature engineering
-> classifier comparison
-> final model selection
-> class-level evaluation
-> interpretation
```

For a generator, this is the canonical route for spectrum, image, text, or other high-dimensional labeled data problems.

## Section Structure

Observed first-pass structure:

1. Abstract
2. Problem restatement and analysis
3. Assumptions
4. Symbol explanation
5. Model establishment and solution
   - preprocessing
   - feature reduction / extraction
   - model comparison
   - classification/origin identification
6. Model evaluation or conclusion
7. References

Generator lesson:

- Classification papers need an explicit preprocessing section before any model formulas.
- A symbol table is still useful, but the key variables are dataset-level and feature-level, not only physical quantities.
- The model section should separate "candidate methods" from the final classifier selected for each task.

## Abstract Pattern

The abstract follows a compressed problem-by-problem pattern:

- state the data source and the classification task;
- name the preprocessing methods;
- name the feature extraction or dimensionality reduction methods;
- name the classifiers compared;
- report the final best-performing combination and the evaluation result.

Generator rule:

```text
For classification papers, each task in the abstract should contain:
data -> preprocessing -> model -> metric -> final winner
```

Avoid:

- only saying "we used machine learning";
- presenting accuracy without dataset context;
- collapsing all tasks into one vague summary.

## Model Chain

### Stage 1: Spectral Preprocessing

Observed preprocessing methods:

- Savitzky-Golay smoothing
- MSC
- SNV

Why this matters:

- raw spectra are noisy and subject to scatter/baseline effects;
- preprocessing is not optional because it changes the separability of classes;
- the paper compares preprocessing choices rather than assuming one universal fix.

Generator rule:

```text
For spectral or signal classification problems, preprocessing must be a first-class model choice, not an implementation detail.
```

### Stage 2: Feature Extraction and Reduction

Observed methods:

- PCA
- LDA
- feature selection

Generator rule:

```text
For high-dimensional data, always show which features or components are kept and why.
```

The paper uses reduction not just for compression, but to improve class separability and simplify later classifier choice.

### Stage 3: Classifier Comparison

Observed methods:

- SVM
- random forest
- LDA-based classification

Generator rule:

```text
Compare at least two classifiers and explain why the final winner matches the data structure.
```

This paper is especially useful because the best method may differ by task:

- species/category classification may favor one pipeline;
- origin identification may favor another.

That means a generator should not force one model to solve every task.

### Stage 4: Metric Reporting

Observed evaluation signals:

- accuracy
- F1 or similar class-sensitive metrics
- confusion-level diagnostics

Generator rule:

```text
Classification papers should report class-level performance, not only a single overall accuracy.
```

If class imbalance or confusable categories exist, confusion matrices are needed.

## Figure Inventory

Expected/observed figure types from the first-pass summary:

- spectrum preprocessing flow
- reduced-feature scatter or component plot
- class-separation or feature-importance visualization
- confusion matrix

Minimum generator requirement for similar problems:

- one preprocessing figure;
- one feature-reduction figure;
- one confusion-matrix or class-level diagnostic figure.

## Table Inventory

Observed table types:

- dataset or sample summary
- preprocessing comparison table
- classifier comparison table
- metric table for each task

Generator rule:

```text
If the paper compares classifiers, the comparison table must show the same dataset split and the same metric definitions.
```

## Validation and Review Signals

Strong signals:

- preprocessing is compared rather than assumed;
- feature reduction is visually or numerically justified;
- classifier choice is task-specific;
- metrics extend beyond accuracy;
- class-level diagnostics appear when categories are hard to separate.

Risk signals:

- accuracy reported without split policy;
- classifier comparison without consistent preprocessing;
- no confusion matrix or per-class diagnostics;
- the paper claims a "best model" but does not show the comparison basis.

## Generator Rules Added

1. For spectrum/signals/images/text classification, begin with preprocessing before model selection.
2. Keep preprocessing, feature reduction, and classifier choice on the same data split.
3. Use a comparison table for candidate classifiers and a confusion matrix for the final model.
4. Report class-sensitive metrics when categories are imbalanced or visually similar.
5. Do not merge multiple classification tasks into one ungrounded accuracy statement.

