# Response Surface Methodology Card

Purpose: support experimental-factor optimization when the problem involves controllable factors, response values, and local optimal conditions.

## Use When

- The task asks for optimal experimental or process conditions.
- Factors are continuous and controllable within a known range.
- The data come from experiments or designed scenarios.
- The paper must explain factor effects and interactions.

## Avoid When

- The data are purely observational and not suitable for process optimization.
- The requested optimum lies outside the experimental range.
- Factor ranges are unknown or physically impossible.
- The response is noisy and no replication or residual check is available.

## Required Inputs

- Factors, levels, and valid ranges.
- Response variable definition.
- Experimental design table or observed factor-response table.
- Candidate quadratic model terms.
- Constraint or desirability definition for optimization.

## Mathematical Objects

Second-order response model:

```text
y = beta_0 + sum_i beta_i x_i + sum_i beta_ii x_i^2 + sum_{i<j} beta_ij x_i x_j + epsilon
```

Multi-response desirability:

```text
D = (d_1 d_2 ... d_m)^(1/m)
```

## Outputs

- ANOVA or coefficient significance table.
- Response-surface or contour plots.
- Optimal factor combination.
- Predicted response under optimum.
- Verification or supplementary experiment suggestion.

## Figure and Table Expectations

- Factor-level table.
- Regression/ANOVA table.
- 3D response surface or 2D contour for important factor pairs.
- Optimal-condition table.
- Residual diagnostic plot.

## Validation

- Check residuals and lack-of-fit when possible.
- Compare predicted optimum with observed nearby points.
- Keep optimum inside the experimental domain.
- Run sensitivity analysis around the optimum.
- If no actual verification experiment exists, state it as a proposed check.

## CUMCM Writing Pattern

1. Explain factors, response, and experimental domain.
2. Fit the response model and test significant terms.
3. Interpret main effects and interactions with plots.
4. Optimize under valid ranges.
5. Validate or propose verification experiments.

## Common Risks

- The optimum is outside the fitted domain.
- Quadratic model is used without residual diagnostics.
- Interaction terms are reported but not explained.
- The method is treated as black-box optimization rather than experimental analysis.
- Verification is missing.

## Review Checks

- Are factor ranges stated?
- Is the fitted model appropriate for the data size?
- Are response-surface figures tied to significant terms?
- Does the optimum respect all constraints?
- Is experimental verification or its absence explicit?
