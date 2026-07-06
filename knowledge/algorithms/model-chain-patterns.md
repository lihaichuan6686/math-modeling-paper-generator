# CUMCM Model Chain Patterns

Purpose: capture reusable model chains that appear in strong CUMCM-style papers. A route is more than one algorithm; it is a sequence of analysis, modeling, computation, visualization, and validation artifacts.

## Pattern 1: Evaluation -> Planning -> Scenario Audit

Use when:

- alternatives, suppliers, carriers, locations, or schemes must be ranked and then selected;
- the final answer must be a plan, not only a score.

Typical chain:

```text
indicator system -> weighting/evaluation -> selected candidates -> linear/integer planning -> scenario/sensitivity audit
```

Cards:

- `cards/linear-integer-programming.md`
- `cards/regression.md` when scores depend on fitted relationships
- existing evaluation cards in `algorithm-cards.md` until they are migrated

Required artifacts:

- indicator table
- weight/source table
- ranking table
- plan table
- capacity/feasibility audit
- sensitivity table for weights or demand

Common failure:

- stopping after ranking and never producing an executable plan.

## Pattern 2: Forecast -> Optimization -> Robustness

Use when:

- future demand, price, traffic, load, production, or risk drives a decision.

Typical chain:

```text
time-series or regression forecast -> uncertainty interval -> planning model -> stress test
```

Cards:

- `cards/time-series.md`
- `cards/regression.md`
- `cards/linear-integer-programming.md`
- `cards/simulation.md`

Required artifacts:

- train/test forecast plot
- forecast error table
- decision table using forecasts
- stress-test table under high/low forecast scenarios
- explanation of uncertainty propagation

Common failure:

- using a single forecast as a certain input and ignoring forecast error.

## Pattern 3: Feature Extraction -> Classifier Comparison -> Error Analysis

Use when:

- samples have many variables, spectra, images, or high-dimensional indicators;
- labels or categories matter.

Typical chain:

```text
preprocessing -> feature extraction/dimension reduction -> classifier comparison -> confusion/error analysis
```

Cards:

- `cards/pca-lda.md`
- `cards/random-forest.md`
- `cards/svm.md`
- `cards/regression.md` for logistic or baseline models

Required artifacts:

- preprocessing table
- explained variance or feature importance
- classifier comparison table
- confusion matrix
- error-case analysis

Common failure:

- reporting accuracy without split policy, confusion matrix, or feature leakage check.

## Pattern 4: Physical or Geometric Derivation -> Numerical Optimization -> Residual Check

Use when:

- problem signals include coordinates, geometry, mechanics, optics, surfaces, paths, or engineering constraints.

Typical chain:

```text
coordinate/physical model -> constraints -> numerical optimization -> residual/error map -> sensitivity
```

Cards:

- `cards/nonlinear-programming.md`
- `cards/linear-integer-programming.md` when discrete decisions appear
- `cards/simulation.md` for physical scenario testing

Required artifacts:

- coordinate or mechanism diagram
- parameter table
- equation derivation
- optimal configuration table
- residual/error figure
- sensitivity table

Common failure:

- formulas look mathematical but are not tied to a coordinate frame or physical constraint.

## Pattern 5: Factor Analysis -> Response Surface -> Verification Proposal

Use when:

- experimental factors affect yield, conversion, selectivity, quality, or performance;
- the paper needs to recommend operating conditions.

Typical chain:

```text
exploratory factor analysis -> regression/ANOVA -> response surface -> constrained optimum -> verification proposal
```

Cards:

- `cards/regression.md`
- `cards/response-surface.md`
- `cards/nonlinear-programming.md`

Required artifacts:

- factor-level table
- coefficient or ANOVA table
- contour/surface plots
- optimal-condition table
- residual and verification discussion

Common failure:

- optimal conditions are outside the experimental domain or lack verification.

## Pattern 6: Queue/Simulation -> Capacity Recommendation -> Stress Test

Use when:

- the system includes waiting, congestion, service stations, random arrivals, machine failures, or uncertain operations.

Typical chain:

```text
arrival/service modeling -> queueing formula or simulation -> capacity plan -> stress test
```

Cards:

- `cards/queuing-models.md`
- `cards/simulation.md`
- `cards/linear-integer-programming.md`

Required artifacts:

- system flow diagram
- arrival/service statistics
- utilization/waiting table
- capacity-performance curve
- stress-test distribution

Common failure:

- average-case recommendation ignores peak-period or stability constraints.

## Pattern 7: Graph Construction -> Network Algorithm -> Feasibility Audit

Use when:

- the problem is about paths, matching, coverage, connectivity, flows, or spatial networks represented as edges.

Typical chain:

```text
node/edge construction -> graph algorithm or network flow -> solution visualization -> feasibility and sensitivity audit
```

Cards:

- `cards/graph-algorithms.md`
- `cards/linear-integer-programming.md`
- `cards/simulation.md`

Required artifacts:

- graph construction table
- network diagram
- selected path/edge/flow table
- bottleneck analysis
- sensitivity to edge weights or capacities

Common failure:

- graph diagram exists but node/edge construction is not reproducible.

## Pattern 8: Static Plan -> Online Update -> Abnormal Scenario

Use when:

- decisions must be adjusted after interruptions, abnormal events, changing data, or rolling time windows.

Typical chain:

```text
baseline plan -> update trigger -> rolling or dynamic model -> revised plan -> loss comparison
```

Cards:

- `cards/linear-integer-programming.md`
- `cards/dynamic-programming.md`
- `cards/simulation.md`

Required artifacts:

- baseline plan table
- update-rule description
- abnormal-scenario table
- initial-vs-adjusted plan table
- loss comparison chart

Common failure:

- solving only the static plan and describing updates verbally.

## Selection Rule

For each subquestion:

1. Pick one primary pattern.
2. Pick the required algorithm cards.
3. List required artifacts before implementation.
4. Define the validation artifact before writing results.
5. Reject a pattern if required data or validation evidence cannot be produced.
