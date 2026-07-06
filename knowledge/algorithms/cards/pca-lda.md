# PCA and LDA Card

Purpose: support dimensionality reduction, feature extraction, visualization, and interpretable classification in CUMCM data-analysis problems.

## Use PCA When

- Many indicators or spectral/features variables are correlated.
- The task needs compression before clustering, evaluation, regression, or classification.
- The paper must explain major variation directions.
- Visualization in two or three dimensions helps reveal sample groups.

## Use LDA When

- Class labels are available.
- The task needs supervised low-dimensional projection or classification.
- The goal is to maximize between-class separation while reducing within-class scatter.

## Avoid When

- Features have different scales and no standardization is planned.
- PCA components would replace meaningful physical variables without explanation.
- LDA class sample sizes are too small or covariance assumptions are fragile.
- The method is used only to make a decorative scatterplot.

## Required Inputs

- Standardized feature matrix.
- Indicator direction treatment when features are evaluation indicators.
- Class labels for LDA.
- Explained-variance threshold for PCA.
- Downstream model that uses the reduced features.

## Mathematical Objects

PCA:

```text
X_std -> covariance or correlation matrix -> eigenvectors -> principal component scores
```

LDA:

```text
maximize |W^T S_b W| / |W^T S_w W|
```

where `S_b` is between-class scatter and `S_w` is within-class scatter.

## Outputs

- Explained-variance table.
- Component loading table.
- Principal component score table.
- 2D or 3D projection plot.
- Downstream classification, clustering, or evaluation result.

## Figure and Table Expectations

- Scree plot or cumulative explained-variance curve.
- Loading heatmap or table for major components.
- Score scatterplot colored by class or cluster.
- Confusion matrix when LDA or classification is involved.

## Validation

- Check whether retained components explain enough variance.
- Interpret major loadings with domain meaning.
- Compare downstream performance before and after reduction.
- For LDA, use cross-validation and confusion matrix.
- Check class imbalance and possible leakage.

## CUMCM Writing Pattern

1. State the high-dimensional feature problem.
2. Standardize and justify indicator direction.
3. Derive components or discriminant directions.
4. Interpret retained dimensions.
5. Feed reduced features into classification, evaluation, or visualization.

## Common Risks

- PCA is confused with feature selection.
- Loadings are not interpreted.
- Cumulative variance threshold is arbitrary.
- LDA is applied without labels or without validation.
- The reduced dimensions do not connect to final conclusions.

## Review Checks

- Is standardization explicit?
- Are retained dimensions justified?
- Are component meanings explained?
- Does the projection support, rather than replace, quantitative validation?
- Are labels kept out of PCA fitting unless using supervised methods?
