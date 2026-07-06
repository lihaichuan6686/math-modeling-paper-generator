# Nonlinear Programming Card

Purpose: support optimization problems where objective functions or constraints are nonlinear, often due to physics, geometry, economics, response curves, or risk functions.

## Use When

- The problem has continuous decisions with nonlinear cost, efficiency, distance, probability, or physical relations.
- Linearization would destroy important behavior.
- Decision variables have clear bounds and feasible regions.
- The paper can justify numerical solving and local/global optimality checks.

## Avoid When

- Nonlinearity is added only to look sophisticated.
- Constraints and variable ranges are not known.
- The objective has many local optima but no multi-start or global-search plan.
- Discrete decisions dominate and should be modeled as integer programming.

## Required Inputs

- Decision variables and bounds.
- Objective function with units or practical meaning.
- Nonlinear constraints and feasibility conditions.
- Initial points or sampling strategy.
- Solver, convergence criteria, and backup search method.

## Mathematical Objects

Typical form:

```text
minimize   f(x)
subject to g_i(x) <= 0
           h_j(x) = 0
           l <= x <= u
```

Possible solution strategy:

```text
multi-start local optimization -> feasibility audit -> sensitivity analysis
```

## Outputs

- Optimal variable values.
- Objective value and feasibility residuals.
- Convergence or search trace.
- Sensitivity of the optimum to starting points and parameters.
- Comparison with linearized or heuristic baseline.

## Figure and Table Expectations

- Feasible-domain or response-surface plot when dimension permits.
- Convergence curve.
- Optimal-solution table.
- Sensitivity heatmap or perturbation table.

## Validation

- Check constraint residuals.
- Run multiple starting points.
- Compare against grid search on reduced dimensions when possible.
- Test perturbations of important parameters.
- State whether the optimum is local or global.

## CUMCM Writing Pattern

1. Derive the nonlinear relation from problem logic.
2. Define variables, objective, and constraints.
3. Explain solver and initial-point strategy.
4. Present optimal result with feasibility audit.
5. Discuss local optimum risk and sensitivity.

## Common Risks

- Reporting a solver result without proving feasibility.
- Treating a local optimum as global without evidence.
- Missing variable bounds.
- Hiding numerical failure or convergence warnings.
- Objective function lacks real-world interpretation.

## Review Checks

- Is every nonlinear term justified?
- Are bounds and constraints complete?
- Is solver behavior reproducible?
- Are local-optimum risks addressed?
- Does the result remain feasible after rounding or implementation?
