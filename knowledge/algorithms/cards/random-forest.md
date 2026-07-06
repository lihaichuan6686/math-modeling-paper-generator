# Random Forest Card

Purpose: support robust nonlinear prediction, classification, and variable-importance analysis when interpretability is still needed.

## Use When

- Data contain nonlinear relations and feature interactions.
- The task needs classification or regression with moderate tabular data.
- Variable importance can help explain key factors.
- A stronger baseline than linear regression or single decision tree is needed.

## Avoid When

- The sample size is very small and validation would be unstable.
- The paper needs transparent formulas as the primary contribution.
- Time-series order, spatial dependence, or experimental grouping would be broken by random splitting.
- Feature leakage is likely.

## Required Inputs

- Feature matrix and target labels or response values.
- Train/test split or cross-validation plan.
- Hyperparameters such as number of trees, max depth, minimum leaf size.
- Class-balance treatment when classes are imbalanced.
- Baseline models for comparison.

## Mathematical Objects

Core idea:

```text
bootstrap samples -> decision trees -> majority vote or averaged prediction
```

For classification:

```text
y_hat = mode(T_1(x), T_2(x), ..., T_B(x))
```

For regression:

```text
y_hat = (1/B) sum_b T_b(x)
```

## Outputs

- Accuracy, F1, AUC, RMSE, or MAE depending on task.
- Confusion matrix for classification.
- Variable importance ranking.
- Prediction table for target samples.
- Error analysis by class or scenario.

## Figure and Table Expectations

- Model comparison table.
- Confusion matrix heatmap.
- Feature-importance bar chart.
- Partial-dependence or sensitivity plot for top features when useful.
- Error distribution plot.

## Validation

- Use stratified split for classification.
- Report multiple metrics, not only accuracy.
- Compare with logistic regression, SVM, or decision tree when appropriate.
- Repeat with fixed random seed and record it.
- Inspect misclassified or high-error samples.

## CUMCM Writing Pattern

1. Explain why nonlinear interactions may exist.
2. State preprocessing and split policy.
3. Present baseline models before the random forest result.
4. Use performance metrics and confusion matrix as evidence.
5. Interpret important variables carefully as association, not causality.

## Common Risks

- Treating feature importance as causal proof.
- Reporting only one random split.
- Ignoring class imbalance.
- Using test data during feature selection or normalization.
- No comparison with simpler models.

## Review Checks

- Is the validation split reproducible?
- Are class imbalance and leakage checked?
- Are metrics matched to the problem objective?
- Are important variables interpreted within domain limits?
- Does the model output answer a concrete subproblem?
