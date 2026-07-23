# v1.6 Method Chain Evidence Index

Purpose: connect CUMCM problem families to method chains that produce paper-visible evidence, validation, and section rhythm. This file is not an algorithm encyclopedia. It is a drafting control sheet for making a route look like a serious team solution.

Use after:

- `knowledge/cumcm/national-problem-family-methodology-matrix.md`
- `knowledge/algorithms/v1-5-route-upgrade-atlas.md`
- `knowledge/latex/v1-6-section-rhythm-soft-metrics.md`

## Core Rule

Do not select a method chain unless it can fill all four slots:

```text
support diagnosis -> main model -> result artifact -> validation artifact
```

If a route cannot name its result artifact and validation artifact, it is not ready for LaTeX.

## Evidence-Oriented Method Chain Matrix

| Family | Support diagnosis | Main model chain | Result artifact | Validation artifact | Paper-visible highlight |
|---|---|---|---|---|---|
| Evaluation and ranking | indicator screening, normalization check, correlation or redundancy audit | entropy/AHP/CRITIC comparison -> TOPSIS/VIKOR/gray relation -> rank stability | indicator-weight-rank table | weight perturbation, method comparison, rank interval | one compact table showing weights, ranks, and stability |
| Evaluation to planning | candidate diagnosis, feasibility constraints, demand/capacity reading | evaluation shortlist -> integer/linear programming -> scenario comparison | candidate shortlist plus executable plan table | capacity, budget, service, or resource feasibility audit | route figure connecting scores to actual quantities |
| Forecast to decision | trend, seasonality, missingness, abnormal points | baseline forecast -> improved model or ensemble -> downstream decision model | forecast table and decision table | backtest, residual plot, high/low scenario, uncertainty propagation | a figure where forecast uncertainty visibly changes the decision |
| Classification and recognition | leakage check, class balance, feature distribution, preprocessing logic | baseline classifier -> feature selection/dimensionality reduction -> model comparison -> threshold decision | comparison table and judgment-rule table | split policy, confusion matrix, ROC/PR, error-case analysis | classifier becomes a usable screening rule, not just accuracy |
| Geometry and engineering mechanics | object sketch, coordinate frame, measurement reliability | geometric derivation -> constrained nonlinear solve -> residual replay | parameter/design result table | residual map, measurement perturbation, feasibility replay | early scene diagram plus residual evidence after solving |
| Production planning and scheduling | resource/demand audit, bottleneck identification | baseline plan -> optimization/simulation -> rolling or abnormal-event update | schedule/production plan table | before/after comparison, constraint satisfaction, capacity stress test | timeline or schedule artifact with audit table |
| Graph and network | node-edge definition, weight meaning, connectivity check | graph construction -> path/flow/coverage optimization -> bottleneck audit | network/path/flow table | disruption, capacity, connectivity, coverage sensitivity | reproducible network construction before final route |
| Queue and service systems | arrival/service distribution, peak diagnosis, utilization baseline | queue model or discrete-event simulation -> service policy -> peak stress test | staffing/dispatch/service policy table | peak waiting, utilization, bottleneck, scenario comparison | peak-period evidence, not only average-load formulas |
| Experimental factor optimization | factor-response exploration, outlier/domain check | regression/ANOVA -> response surface -> constrained optimum -> domain verification | optimum condition table | residual, holdout, confidence/domain-boundary, extra-experiment proposal | response surface with optimum visibly inside experimental domain |
| Monitoring and policy | pattern diagnosis, threshold candidates, false-alarm/miss framing | diagnostic model -> threshold/rule design -> policy simulation/comparison | monitoring or intervention rule table | false alarm/miss risk, long-horizon effect, policy comparison | diagnostic plots close into an executable rule |

## Method Chain Writing Pattern

For each central subquestion, convert the selected row into this paper paragraph structure:

```text
The support diagnosis identifies the key structure.
The main model transforms this structure into a solvable quantity.
The result artifact reports the answer in reviewer-readable form.
The validation artifact explains why the answer is credible.
The limitation sentence states where the result should not be overread.
```

This prevents a common AI-like failure:

```text
algorithm name -> output number -> generic praise
```

## Figure And Table Planning Rules

Every selected method chain should generate at least one body artifact:

- diagnosis figure or table;
- model/route diagram;
- result table;
- validation figure or table.

Central questions should usually have at least two of the four. If the route produces only code outputs, rewrite the route before drafting.

## Abstract Conversion Rule

Convert method chains into abstract sentences using evidence, not prestige:

```text
针对问题X，先通过<support diagnosis>识别<关键结构>，再构建<main model>得到<result artifact>；经<validation artifact>检验，结果表明<answer-level conclusion>。
```

Avoid:

- "采用随机森林、遗传算法等方法进行求解";
- "模型效果较好";
- "结果具有一定参考价值";
- method lists with no answer-level result.

## Route Rejection Rules

Reject a planned route before coding if:

- it only names one algorithm and no support diagnosis;
- the result artifact cannot appear as a table or figure in the body;
- the validation artifact is "compare with intuition" only;
- the method is more complex than the data can support;
- the abstract would have to hide behind vague words such as "较好", "合理", or "有效".

## Use In Run Files

Record the selected chain in:

- `runs/current/route-decision.md`
- `runs/current/method-depth-plan.md`
- `runs/current/section-rhythm-budget.md`
- `runs/current/artifact-ledger.md`

Before final writing, check that every central subquestion has:

```text
support diagnosis
main model
result artifact
validation artifact
paper-visible highlight
```
