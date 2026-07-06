# Simulation Card

Purpose: support stochastic, dynamic, spatial, or complex systems where closed-form analysis is difficult and repeated computational experiments provide evidence.

## Use When

- The system contains randomness, interactions, queues, movement, failures, or nonlinear feedback.
- Analytic formulas are unavailable or too restrictive.
- The paper needs scenario comparison or robustness evidence.
- Simulation is used as validation or decision support, not as a substitute for clear modeling.

## Avoid When

- Random distributions are invented with no justification.
- A deterministic optimization model can answer the task more cleanly.
- The simulation cannot be reproduced.
- Only one run is reported.

## Required Inputs

- System state variables.
- Event or time-step rules.
- Random variable distributions and seeds.
- Initial conditions.
- Number of runs and stopping criteria.
- Evaluation metrics.

## Mathematical Objects

Common forms:

```text
state_{t+1} = F(state_t, action_t, random_t)
metric = G(state_0, ..., state_T)
```

Monte Carlo estimate:

```text
E[g(X)] approx (1/N) sum_{i=1}^N g(X_i)
```

## Outputs

- Mean, variance, quantiles, and confidence intervals.
- Scenario comparison table.
- Distribution plots.
- Extreme-case probabilities.
- Recommended policy under uncertainty.

## Figure and Table Expectations

- Simulation flowchart.
- Distribution histogram or density plot.
- Scenario comparison table.
- Confidence-interval plot.
- Time-evolution plot when dynamic.

## Validation

- Run enough replications for stable estimates.
- Fix and record random seeds.
- Compare with analytic result on a simplified case.
- Conduct sensitivity analysis over distribution assumptions.
- Report uncertainty and extreme cases.

## CUMCM Writing Pattern

1. Explain why simulation is necessary.
2. Define state, event rules, distributions, and metrics.
3. Run replicated experiments.
4. Present distributions and confidence intervals.
5. Use simulation to compare decisions or validate another model.

## Common Risks

- Simulation rules are underspecified.
- No seed, no replication count, no uncertainty.
- Results are written as deterministic facts.
- Random assumptions dominate conclusions.
- Simulation is disconnected from the paper's main model.

## Review Checks

- Is the simulation reproducible?
- Are distributions justified?
- Are enough replications used?
- Are uncertainty intervals shown?
- Is there a baseline or simplified validation case?
