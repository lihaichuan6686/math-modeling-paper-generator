# E-Route Comparison: 2022 to 2023

Purpose: compare multiple E-type excellent papers to learn which structural choices are stable, which are flexible, and how the route evolved from production-planning E papers in 2022 to monitoring-and-decision E papers in 2023.

Samples used:

- `2022高教社杯全国大学生数学建模竞赛E题论文展示（E014）.pdf`
- `2022高教社杯全国大学生数学建模竞赛E题论文展示（E029）.pdf`
- `2023年高教社全国大学生数学建模竞赛优秀论文【公众号：竞赛资料网】\E176.pdf`

Important note:

- The local 2023 official excellent-paper folder currently contains only one E sample, `E176`.
- So the strongest same-problem structural comparison available locally is:

```text
2022 E014 vs 2022 E029
```

- Then `E176` is used as the next-year route upgrade reference.

Status update:

- `2022 E014` and `2022 E029` have now both been deep-read in full and should be treated as the current production-route anchor pair.

## High-Level Contrast

### 2022 E014

Observed title theme: material-production scheduling based on time-series prediction.

Observed character:

- more compact and plan-oriented;
- stronger emphasis on stable inventory and service-level safeguards;
- abstract gives concrete stock and service quantities quickly;
- appendix is mainly support-material list rather than a long methodological appendix.
- full deep-read note: `knowledge/cumcm/deep-reading-2022E014.md`

Observed route:

```text
historical demand and inventory data
-> monthly or periodic pattern reading
-> prediction
-> safety-stock and service-level reasoning
-> production scheduling
-> attachment list
```

### 2022 E029

Observed title theme: dynamic production optimization based on time-series prediction.

Observed character:

- still production-planning centered, but more data-exploratory than E014;
- spends more effort on raw order-volume patterns and customer-material grouping;
- stronger dynamic flavor in the abstract and early figures;
- appendix includes concrete MATLAB program fragments.
- full deep-read note: `knowledge/cumcm/deep-reading-2022E029.md`

Observed route:

```text
historical order-volume statistics
-> material screening and grouping
-> time-pattern analysis
-> prediction
-> dynamic production optimization
-> support files and code appendix
```

### 2023 E176

Observed title theme: optimal reservoir monitoring scheme based on wavelet transform and knapsack-style optimization.

Observed character:

- much broader method stack;
- each subproblem forms its own mini paper;
- stronger evidence chain from diagnosis to prediction to decision;
- the appendix becomes a support-material tree with mixed Python, MATLAB, Excel, and optimization workflow evidence.

Observed route:

```text
data cleaning and aggregation
-> relation fitting
-> periodicity and abruptness diagnosis
-> future prediction
-> monitoring optimization
-> intervention-effect evaluation
-> long-horizon consequence forecast
```

## Stable Structural Signals Across E Papers

Even though the topics differ, the following signals are stable:

1. E papers are process papers, not single-model papers.
2. Forecasting is rarely the final stop; it usually feeds planning, scheduling, or monitoring.
3. Attachment and support-material traceability matter more than in many A/B-style geometry papers.
4. Abstracts are dense and quantitative.
5. Good E papers are naturally long because each subproblem carries data, model, and decision consequences.

Generator rule:

```text
Treat E-type papers as chain-of-decision papers: prediction should usually become a downstream action model.
```

## Flexible Structural Choices

### 1. How early to enter optimization

- `E014` enters planning logic early and reads like a scheduling paper with prediction support.
- `E029` spends more time on order statistics and grouping before optimization.
- `E176` delays the explicit optimization question until it has built a much richer time-series diagnosis.

Generator lesson:

```text
For E problems, the paper can enter optimization early or late, but only after the chosen data abstractions are credible.
```

### 2. How broad the method stack can be

- `E014` looks relatively compact.
- `E029` adds more exploratory grouping and code evidence.
- `E176` uses a wide method family but keeps it tied to subproblem boundaries.

Generator lesson:

```text
A broader method stack is acceptable only when each method has a clear question-level role.
```

### 3. Appendix style

- `E014`: support-material list is enough for the paper to feel complete.
- `E029`: code appendix begins to become a stronger credibility layer.
- `E176`: support-material tree plus mixed-tool chain makes the appendix part of the paper's argument.

Generator lesson:

```text
For stronger E papers, the appendix should map files to questions and not just dump code.
```

## Evolution From 2022 E to 2023 E

### 2022 Strength

The 2022 E route is strong at:

- prediction-to-production chaining;
- operational quantities like inventory, service level, and production amount;
- compact decision framing;
- business-style execution outputs.

### 2023 Upgrade

`E176` adds several upgrades:

- richer time-series diagnosis before prediction;
- explicit abruptness and periodicity evidence;
- clearer forecast-to-decision conversion;
- policy-effect and counterfactual analysis after the main optimization;
- stronger appendix traceability.

Practical interpretation:

```text
2022 E teaches how to turn prediction into production action.
2023 E teaches how to turn diagnosis and prediction into monitoring and policy action.
```

Inside the 2022 production route itself:

```text
E014 = conservative, service-level-first rolling rule
E029 = dynamic, ARIMA-comparison-first rolling production plan
```

## What This Means For The Generator

### E-Type Paper Archetype

The generator should recognize at least two E-route families:

1. production-and-scheduling E route
2. monitoring-and-policy E route

Both share:

- historical data preprocessing;
- trend or periodic analysis;
- forecasting;
- downstream decision model;
- attachment traceability.

But they differ in emphasis:

- production route prefers inventory, service level, batching, and scheduling outputs;
- monitoring route prefers diagnosis, information value, sampling design, and intervention assessment.

### Page Allocation Insight

Useful page-shape rule:

- compact production E papers can stay tighter in method breadth;
- monitoring E papers can become longer because each subproblem has a separate analytical lens;
- both still need the same stable backbone:

```text
data -> model -> result -> actionable conclusion
```

### Figure and Table Insight

Production-route E papers:

- order or demand statistics;
- grouping or classification support;
- inventory or service-level tables;
- production-plan output tables.

Monitoring-route E papers:

- seasonality and periodicity figures;
- regression and diagnostic figures;
- forecast comparison figures;
- monitoring-scheme decision tables;
- intervention-effect comparison figures.

## Immediate Generator Rules Added

1. Split E-type papers into at least two route families: production-scheduling and monitoring-policy.
2. Require forecasting outputs to feed a concrete action layer.
3. Keep the abstract quantitative and subproblem-bound.
4. Let appendix strength scale with route complexity.
5. For monitoring E papers, add diagnosis before prediction.
6. For production E papers, add service-level and feasibility language, not just predicted quantities.

## Follow-On Reading Priority

Best next local follow-up:

1. Update `problem-type-paper-archetypes.md` with a dedicated E-route split using `E014`, `E029`, and `E176`.
2. Then update the paper blueprint so E-type generation chooses the right route family and section allocation.
3. After that, update the review rubric so E-type papers are checked against the correct route-specific signals.
