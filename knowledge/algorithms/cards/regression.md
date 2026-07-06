# Regression Card

Purpose: support explanatory and predictive modeling when a response variable is driven by measurable factors.

## Use When

- The task asks for factor influence, trend explanation, prediction, calibration, or relationship estimation.
- Data include a dependent variable and candidate explanatory variables.
- The paper needs interpretable coefficients, residual checks, and uncertainty discussion.
- Regression will feed a later optimization or evaluation model.

## Avoid When

- The sample size is too small for the number of candidate variables.
- Variables are strongly collinear and no dimension reduction or regularization is planned.
- The response is categorical and should be modeled by classification.
- The relationship is purely mechanistic and a physical equation is available.

## Required Inputs

- Clean response vector.
- Feature matrix with units and transformations.
- Train/test or cross-validation design when sample size permits.
- Candidate nonlinear terms, interaction terms, or regularization settings.
- Domain-valid value ranges.

## Mathematical Objects

Linear baseline:

```text
y = beta_0 + beta_1 x_1 + ... + beta_p x_p + epsilon
```

Common extensions:

```text
polynomial regression
log or Box-Cox transformed regression
ridge / lasso / elastic net
logistic regression for binary outcomes
partial least squares when predictors are collinear
```

## Outputs

- Coefficient table with sign and significance or stability.
- Fitted-vs-observed plot.
- Residual plot.
- Prediction table with error metrics.
- Variable importance or sensitivity summary.

## Figure and Table Expectations

- Scatterplot or factor-effect plot for important variables.
- Residual diagnostic figure.
- Coefficient or standardized-effect table.
- Prediction-error comparison table if multiple models are compared.
- If used for optimization, response curve or contour plot.

## Validation

- Residual normality and heteroscedasticity checks when using inference.
- Multicollinearity check such as VIF or correlation heatmap.
- Outlier influence check.
- Cross-validation or holdout error when prediction matters.
- Domain sanity check for extrapolated predictions.

## CUMCM Writing Pattern

1. Explain why the response variable is central to the problem.
2. State preprocessing and feature construction.
3. Build an interpretable baseline before complex variants.
4. Compare models by error and interpretability.
5. Use regression outputs to support later planning, optimization, or evaluation.

## Common Risks

- Coefficients are interpreted causally without experiment design.
- High R-squared is reported without residual checks.
- The model extrapolates outside the data range.
- Too many variables are fitted to too few samples.
- Prediction results are not connected back to the original question.

## Review Checks

- Are units and transformations clear?
- Is the sample size adequate for the model complexity?
- Are residuals and outliers discussed?
- Is validation separated from fitting?
- Does the regression serve the paper's decision chain?
