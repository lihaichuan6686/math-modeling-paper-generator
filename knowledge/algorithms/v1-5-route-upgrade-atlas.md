# v1.5 Route Upgrade Atlas

Purpose: help Claude Code move from CUMCM problem signals to a route that looks like a serious team solution, not a shallow algorithm demo.

Use this after `route-selection-protocol.md` and before filling `runs/current/method-depth-plan.md`.

This atlas does not choose the fanciest method. It forces each route to name:

```text
support layer -> main model -> result artifact -> validation artifact -> paper highlight
```

## How To Use

1. Match the problem to one or two signal rows.
2. Copy the selected row into `route-decision.md`.
3. Convert the row into `method-depth-plan.md`.
4. Reject any route that cannot name both a result artifact and a validation artifact.
5. Use the paper highlight column to decide what the abstract and early model section should emphasize.

## Route Upgrade Matrix

| Problem signal | Shallow route to avoid | v1.5 upgraded route chain | Result artifact | Validation artifact | Paper highlight | Typical trap |
|---|---|---|---|---|---|---|
| experimental factors, temperature, concentration, yield, selectivity | regression -> optimum | factor diagnosis -> baseline fit -> response surface or constrained regression -> optimum search -> domain verification | optimal-condition table and response surface/contour figure | residual, holdout, domain-boundary, or proposed additional experiment | explain why the optimum is inside a credible experimental region | reporting an extrapolated mathematical optimum as if it were experimental truth |
| supplier, material, inventory, transporter, weekly capacity | score ranking -> recommendation | supply reliability diagnosis -> candidate screening -> ordering/transport planning -> capacity/inventory audit -> scenario comparison | supplier shortlist, order plan, transport plan | weekly capacity, two-week inventory, loss/cost, and sensitivity audit | show the chain from evaluation to executable plan | stopping at ranking while the task asks for quantities |
| abnormal event, online adjustment, rolling production, dynamic update | static optimization -> final plan | baseline plan -> event/trigger model -> rolling or dynamic update -> before/after comparison -> feasibility audit | baseline and adjusted plan tables | loss comparison, constraint-satisfaction audit, event-by-event check | show what was preserved, sacrificed, or improved after update | solving only the normal case and describing update logic verbally |
| spectra, images, many features, class labels, origin recognition | classifier -> accuracy | preprocessing and leakage check -> feature extraction or selection -> baseline classifier -> model comparison -> error/threshold analysis | comparison table, confusion matrix, feature-importance or dimension plot | split policy, class-balance check, cross-validation, error-case analysis | connect classification output to a usable judgment rule | one high accuracy number with no split or error meaning |
| coordinates, angles, surfaces, reflection, physical scene, positioning | nonlinear optimization -> parameters | scene diagram -> coordinate system -> geometric/physical constraints -> numerical solution -> residual or feasibility replay | coordinate/parameter table and design result table | residual map, physical feasibility check, sensitivity to measurement error | make the modeled object visible before formulas become dense | optimizing before defining the coordinate frame |
| network, nodes, paths, communication, reliability, coverage, routing | shortest path -> route | node/edge construction -> probability/capacity modeling -> graph/flow/coverage algorithm -> bottleneck audit -> robustness scenario | network diagram and route/flow table | connectivity, capacity, success-rate, bottleneck, or disruption sensitivity | show reproducible network construction before the answer | drawing a network figure without defining edges and weights |
| queue, service, congestion, arrival, waiting, dispatch | average queue formula -> staffing | arrival/service diagnosis -> queue or simulation model -> capacity/service policy -> peak stress test -> recommendation | utilization/waiting table and service policy table | peak-period waiting, stability, bottleneck, and scenario check | show why the recommendation survives peak conditions | using average load while ignoring peaks |
| population, breeding, space use, lifecycle, resource occupancy | simulation -> plan | lifecycle state model -> space/resource accounting -> production or allocation plan -> long-horizon simulation -> utilization audit | state-transition table and space-use plan | occupancy curve, sensitivity to cycle length, market or disease scenario | show how biological/process stages close into a feasible policy | describing stages but never producing a usable plan |
| forecast, trend, future demand, policy decision | forecast -> conclusion | exploration -> baseline forecast -> improved or selected forecast -> uncertainty interval -> downstream decision or policy | forecast plot and decision table | backtest, residual, high/low scenario, uncertainty propagation | show what the forecast changes in the final decision | treating forecast output as certain |
| evaluation, indicators, alternatives, ranking, grade | entropy/TOPSIS -> ranking | indicator construction -> weight comparison -> ranking -> stability/sensitivity -> decision closure | indicator table, weight table, ranking table | weight perturbation, method comparison, or rank stability | explain why the ranking supports the actual recommendation | decorative weights with no decision consequence |
| facility location, layout, coverage, allocation | location optimization -> coordinates | demand/coverage diagnosis -> candidate generation -> location/allocation optimization -> accessibility or coverage audit -> scenario comparison | selected location/allocation table and coverage map | coverage rate, distance/cost sensitivity, capacity audit | turn spatial output into a defensible service or layout decision | reporting coordinates without service meaning |
| multi-stage policy, monitoring, sampling, intervention | diagnostics -> advice | pattern diagnosis -> threshold/rule design -> intervention or monitoring policy -> long-horizon comparison -> limitation boundary | monitoring rule or intervention table | false alarm/miss risk, long-horizon effect, policy comparison | close diagnostics into an executable rule | stacking diagnostic plots without a policy |

## Required `method-depth-plan.md` Conversion

For each central subquestion, fill:

```text
Subquestion:
Problem signal:
Support layer:
Main model:
Result artifact:
Validation artifact:
Paper highlight:
Known trap:
Depth target:
```

Depth target should usually be Level 3 or Level 4 from `method-depth-ladder.md`.

## Abstract Claim Rule

Do not write an abstract sentence from a method name alone.

Use this shape:

```text
针对问题X，先通过<support layer>识别<关键结构>，再建立<main model>得到<result artifact>；
经<validation artifact>检验，结果表明<answer-level conclusion>。
```

If a subquestion cannot fill this shape, its route is not mature enough for v1.5.

## Paper Highlight Rule

Every route should contribute at least one visible highlight:

- a named route chain;
- an interpretable model-flow figure;
- a well-designed result table;
- a validation or sensitivity figure;
- a concise limitation boundary.

Avoid fake highlights:

- long algorithm lists;
- unexplained neural networks;
- optimization results with no feasibility audit;
- screenshots or default plots;
- appendix-only answers.

## Review Questions

Before drafting LaTeX, ask:

1. Which row in this atlas best matches the problem?
2. What is the final answer artifact, not just the method?
3. What validation artifact prevents the route from looking shallow?
4. What part of the route will become the abstract's strongest claim?
5. What trap is most likely to make the paper look like an AI draft?

If any answer is unknown, repair `route-decision.md` before writing.
