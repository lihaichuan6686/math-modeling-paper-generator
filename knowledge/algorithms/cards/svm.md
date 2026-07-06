# Support Vector Machine Card

Purpose: support classification or regression when the decision boundary is important and sample size is moderate.

## Use When

- The task is binary or multi-class classification with engineered numerical features.
- The sample size is not huge and feature scaling is feasible.
- A margin-based classifier is a good comparison to tree-based methods.
- Kernel selection can express nonlinear separation.

## Avoid When

- Features are unscaled.
- The dataset is too large for practical kernel training.
- The task requires direct feature-effect interpretation.
- Class labels are noisy and no robustness check is planned.

## Required Inputs

- Standardized feature matrix.
- Class labels or response variable for SVR.
- Kernel choice: linear, polynomial, RBF, or sigmoid.
- Hyperparameters: `C`, `gamma`, kernel degree, epsilon for SVR.
- Cross-validation plan.

## Mathematical Objects

Classification objective:

```text
min  1/2 ||w||^2 + C sum_i xi_i
s.t. y_i (w^T phi(x_i) + b) >= 1 - xi_i
     xi_i >= 0
```

Kernel decision:

```text
f(x) = sign(sum_i alpha_i y_i K(x_i, x) + b)
```

## Outputs

- Best kernel and hyperparameter table.
- Accuracy, precision, recall, F1, AUC, or RMSE for SVR.
- Confusion matrix.
- Support-vector count or margin explanation.
- Comparison with logistic regression, random forest, or LDA.

## Figure and Table Expectations

- Hyperparameter search table or heatmap.
- Confusion matrix.
- ROC curve when binary classification and probabilities/scores are available.
- 2D projection decision visualization only when it is faithful and clearly labeled.

## Validation

- Standardize using training statistics only.
- Use grid search or bounded search with cross-validation.
- Check class imbalance.
- Compare several kernels and a simpler baseline.
- Record random seeds and folds.

## CUMCM Writing Pattern

1. Explain the feature space and why separation matters.
2. State scaling and kernel candidates.
3. Present the optimization objective or kernel decision function.
4. Report cross-validation and test performance.
5. Interpret the model as a classifier, not as a causal explanation.

## Common Risks

- RBF kernel is used by habit without tuning.
- Accuracy is high because of leakage.
- Feature scaling is omitted.
- The decision boundary figure is decorative and based on unrelated dimensions.
- Multi-class strategy is not stated.

## Review Checks

- Is scaling explicit and reproducible?
- Are `C` and `gamma` justified by validation?
- Is the baseline comparison fair?
- Are class metrics reported beyond accuracy?
- Are final predictions traceable to input features?
