# Linear and Integer Programming Card

Purpose: support CUMCM problems where decisions, resources, capacities, routes, schedules, purchases, or assignments must be converted into an executable plan.

## Use When

- The problem asks for allocation, ordering, scheduling, routing, batching, selection, or capacity planning.
- Decision variables and constraints can be stated explicitly.
- The result must be a plan table, not only an evaluation score.
- Objectives are cost, profit, loss, time, risk, coverage, or weighted combinations of these.

## Avoid When

- The main uncertainty is prediction rather than planning.
- Key constraints are unknown and would be invented only to make a solver work.
- Data are too vague to support variable bounds, capacities, or coefficients.
- The planned decision is continuous but the real task requires discrete feasibility checks.

## Required Inputs

- Decision set and time/stage indices.
- Objective coefficient definitions.
- Capacity, demand, precedence, budget, coverage, or balance constraints.
- Integer or binary requirements.
- Solver choice and fallback heuristic if the exact model is too large.

## Mathematical Objects

Typical variables:

```text
x_i       continuous quantity decision
y_i       binary selection decision
z_ij      assignment or transport decision
t_k       time-stage decision
```

Typical model:

```text
min or max  f(x, y, z)
subject to  A x + B y + C z <= b
            balance equations
            logical constraints
            x >= 0
            y in {0, 1}
            z integer or binary when required
```

## Outputs

- Decision table with row-level feasibility meaning.
- Objective value and major cost/loss components.
- Constraint satisfaction audit.
- Scenario comparison table.
- Sensitivity table for key coefficients.

## Figure and Table Expectations

- Flowchart or decision-route diagram before formulas.
- Plan table as the central result.
- Capacity-utilization or cost-breakdown bar chart.
- If time is involved, Gantt-style timeline or stage diagram.
- If online updates are involved, initial-vs-adjusted plan table.

## Validation

- Check every hard constraint after solving.
- Compare with a greedy or historical baseline.
- Run stress tests for demand, capacity, cost, and loss-rate changes.
- Report infeasible cases and the relaxation strategy.
- If using heuristic search, repeat runs and show stability.

## CUMCM Writing Pattern

1. Explain the real-world decision process.
2. Define indices, variables, and parameters in a symbol table.
3. Write objective and constraints with one sentence of practical meaning per constraint group.
4. Describe solver or search strategy.
5. Present plan tables and feasibility audit before interpretation.
6. Add sensitivity or abnormal-scenario analysis.

## Common Risks

- A ranking result is mistaken for a planning result.
- Binary variables are defined but not linked to continuous quantities.
- Capacity, loss, or integer rounding constraints are omitted.
- Objective weights are arbitrary and not stress-tested.
- The solver returns a plan that is mathematically optimal but operationally impossible.

## Review Checks

- Does every variable have a real operational meaning?
- Does each constraint correspond to a sentence in the problem?
- Are all tables reproducible from code outputs?
- Are infeasibility and rounding handled explicitly?
- Is the final recommendation a concrete plan?
