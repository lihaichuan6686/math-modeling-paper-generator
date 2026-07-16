# Route Selection Protocol

Purpose: choose reusable model routes by problem fit and evidence fit rather than by prestige algorithm names.

## Rule 1: Select A Route, Not A Buzzword

Weak selection:

```text
Use XGBoost.
Use neural network.
Use AHP.
```

Strong selection:

```text
data cleaning -> feature diagnosis -> baseline model -> decision model -> sensitivity / comparison
```

The chosen route should already imply:

- what data transformations are needed;
- what the main artifact will be;
- what the validation burden is;
- what the paper structure will look like.

## Rule 2: Use The Four-Fit Test

Before selecting a route, score each candidate on:

1. problem fit
2. data fit
3. evidence fit
4. writing fit

### Problem fit

Does the route answer the real question, not just part of it?

### Data fit

Can the available data support the parameters, splits, comparisons, and validation?

### Evidence fit

Can the route produce the figures, tables, diagnostics, and decision artifacts a reviewer would expect?

### Writing fit

Can the route naturally expand into a 20-30 page team-style paper without filler?

If a route scores badly on writing fit, it often becomes a short, machine-like draft even if the math is correct.

## Rule 3: Match Family To Route

Typical route patterns:

| Task family | Preferred route logic |
|---|---|
| evaluation | indicator design -> weighting / comparison -> ranking -> sensitivity |
| prediction | exploration -> baseline forecast -> improved forecast -> error analysis -> downstream use |
| planning / optimization | diagnostic or score layer -> optimization -> feasibility audit -> scenario comparison |
| classification | feature diagnosis -> baseline classifier -> threshold / policy layer -> confusion and robustness |
| scheduling / transport | demand or section diagnosis -> operation plan -> executable schedule -> feasibility audits -> scenario comparison |
| monitoring / policy | diagnosis -> threshold or forecast -> intervention rule -> effect comparison |

Beginner training often says mathematical modeling has three broad families: prediction, optimization, and evaluation. Treat this as a useful first sorting step, not as the final route decision.

Upgrade each broad family as follows:

| First-pass family | Strong route upgrade |
|---|---|
| prediction | exploratory pattern -> baseline forecast -> improved forecast -> error analysis -> decision or explanation use |
| optimization | object and constraints -> baseline feasible plan -> improved plan -> feasibility audit -> scenario or sensitivity comparison |
| evaluation | indicator system -> weighting or scoring comparison -> ranking or grade -> sensitivity -> decision recommendation |

If a route cannot name its final answer artifact after this upgrade, it is not ready for implementation.

## Rule 4: Guard Against Prestige Drift

Reject a complex route when:

- the data volume is too small;
- the explanation burden would overwhelm the paper;
- validation would be too weak;
- the route produces no extra decision value over a simpler model;
- the later writing would rely on naming the algorithm rather than explaining the chain.

## Route-Decision Record

`runs/current/route-decision.md` should include:

```text
Selected route family:
Question map:
Route chain by subquestion:
Why this route fits the decision object:
Why rejected routes are weaker:
Required evidence chain:
Required visuals:
Expected failure modes:
```

## Common Failure Patterns

1. `forecast -> end`
   - bad because no decision closure exists

2. `single regression -> recommendation`
   - bad because the recommendation lacks comparison or robustness

3. `complex model -> one AUC table`
   - bad because the route is method-first and evidence-thin

4. `sample grouping from prompt examples -> optimization`
   - bad because the grouping itself was never justified

5. `many methods listed -> only one used meaningfully`
   - bad because the paper grows by method naming rather than route logic

## Selection Output

A good final route decision should let a reviewer predict:

- the first explanatory figure;
- the main result table;
- the main validation artifact;
- the likely abstract claims;
- the likely weaknesses.

If the reviewer still cannot predict these, the route is not yet explicit enough.

## Anti-List Rule

Do not let route selection become a list like:

```text
prediction: neural network, gray model, time series
optimization: genetic algorithm, simulated annealing, ant colony
evaluation: AHP, entropy weight, PCA
```

The run may mention candidate algorithms, but the selected route must be written as a chain of work and evidence. Method names are allowed only after the modeled object, decision object, input data, output artifact, and validation burden are clear.
