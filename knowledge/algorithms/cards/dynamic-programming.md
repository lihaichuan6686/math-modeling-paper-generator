# Dynamic Programming Card

Purpose: support staged decisions where current choices affect future states, such as inventory, scheduling, resource allocation, path planning, and sequential replacement.

## Use When

- The problem has stages, states, actions, transition rules, and cumulative reward/cost.
- Future feasibility depends on current decisions.
- A recursive relation can be defined clearly.
- State space is small enough or can be approximated.

## Avoid When

- There is no natural stage structure.
- State variables are unclear or too high-dimensional.
- Constraints are easier to express as linear or integer programming.
- The paper cannot explain the recurrence and boundary conditions.

## Required Inputs

- Stage index.
- State definition.
- Action set.
- State-transition equation.
- Stage cost/reward.
- Initial and terminal conditions.

## Mathematical Objects

Canonical recurrence:

```text
V_t(s) = min_a { c_t(s, a) + V_{t+1}(T(s, a)) }
```

or for maximization:

```text
V_t(s) = max_a { r_t(s, a) + V_{t+1}(T(s, a)) }
```

## Outputs

- Optimal policy by stage and state.
- Optimal value.
- Decision path for the given initial state.
- State-transition table or diagram.
- Complexity and state-space notes.

## Figure and Table Expectations

- Stage-state-action diagram.
- Policy table.
- Value-function table or heatmap.
- Decision-path timeline.

## Validation

- Check boundary conditions.
- Verify recurrence on small hand-computable cases.
- Compare with greedy baseline.
- Audit state transitions for feasibility.
- Report state-space size and computational cost.

## CUMCM Writing Pattern

1. Explain why the task is sequential.
2. Define stages, states, actions, and transition.
3. Write the recurrence and boundary conditions.
4. Compute policy and decision path.
5. Compare against a simple baseline and discuss complexity.

## Common Risks

- Stages are artificial and do not match the problem.
- The state omits a needed constraint.
- Boundary conditions are missing.
- State explosion is ignored.
- Only final value is reported, not the policy.

## Review Checks

- Are stage, state, action, and transition unambiguous?
- Is the recurrence dimensionally and logically correct?
- Is the policy recoverable from outputs?
- Is the state space computationally feasible?
- Does the method beat a simpler route?
