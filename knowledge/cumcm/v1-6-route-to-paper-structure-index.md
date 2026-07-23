# v1.6 Route To Paper Structure Index

Purpose: turn a selected CUMCM route family into a paper-shaped plan: title signal, abstract claim shape, early artifacts, section emphasis, method chain, validation, and common first-look failure.

Use this after `national-problem-family-methodology-matrix.md` and `v1-5-route-upgrade-atlas.md`, before writing `paper/main.tex`.

## How To Use

1. Pick one primary route family and, if needed, one secondary route family.
2. Copy the selected row into `runs/current/route-decision.md`.
3. Convert the `Paper spine` and `First-12-page signal` into `section-rhythm-budget.md`.
4. Convert `Abstract claim shape` into the abstract draft.
5. Convert `Validation close` into `method-depth-plan.md`.

If a route cannot fill the abstract claim, result artifact, and validation close, the paper is not ready to draft.

## Route Structure Matrix

| Route family | Title signal | Paper spine | First-12-page signal | Abstract claim shape | Validation close | First-look failure to avoid |
|---|---|---|---|---|---|---|
| Evaluation and ranking | indicator system + decision object | indicators -> weights -> ranking -> stability -> recommendation | indicator route figure, weight table, ranking table | `针对评价筛选问题，构建...指标体系并结合...权重得到...排序；经权重扰动/方法对比检验，...保持稳定。` | weight perturbation, method comparison, rank stability | only producing a ranking list with no decision consequence |
| Evaluation to planning | evaluation plus executable plan | screening -> candidate set -> planning model -> feasibility -> scenarios | evaluation-to-plan figure, candidate table, first plan table | `针对方案制定问题，先筛选...，再建立...规划模型得到...计划；经容量/需求/成本约束检验，方案满足...。` | capacity, inventory, demand, or cost audit | ranking and final plan feel disconnected |
| Forecast to decision | forecast variable + downstream decision | data audit -> forecast comparison -> chosen forecast -> decision -> uncertainty | trend plot, fit plot, forecast table, scenario table | `针对预测决策问题，比较...模型后选取...预测...；进一步将预测结果输入...决策模型，得到...。` | backtest, residual, high/medium/low scenario propagation | forecast is treated as a certain final answer |
| Classification or recognition | feature system + judgment rule | data/split -> preprocessing -> feature extraction -> model comparison -> threshold/error | preprocessing figure, split table, comparison table, confusion matrix | `针对识别判定问题，经过...预处理和...特征构造，比较...分类器并确定...判定规则；交叉验证/混淆矩阵表明...。` | split policy, leakage check, confusion/error analysis | one accuracy number with no split or error meaning |
| Geometry or engineering mechanics | object/scene + parameter/design | scene -> coordinate frame -> relations -> optimization/solution -> residual | object schematic, coordinate table, derivation block, result table | `针对几何/工程设计问题，建立...坐标系并推导...约束，求得...参数；残差/可行性检验显示...。` | residual map, physical feasibility, sensitivity to measurement | formulas appear before object and coordinate frame are clear |
| Production scheduling or rolling update | baseline + adjustment rule | resources -> baseline plan -> trigger/update -> adjusted plan -> comparison | workflow figure, resource table, baseline schedule, update rule | `针对生产调度问题，建立...基准计划并设计...滚动调整规则；异常场景下调整后...优于/满足...。` | before/after loss, constraint audit, scenario stress test | dynamic update is only described verbally |
| Graph, network, path, coverage | node-edge construction + route/coverage decision | network construction -> algorithm -> selected routes/flows -> bottleneck | network figure, node/edge table, route table, bottleneck table | `针对网络路径问题，构造...节点边权网络并采用...算法得到...路径/覆盖方案；瓶颈和扰动检验表明...。` | connectivity, capacity, coverage, edge-weight sensitivity | drawing a network without reproducible edge weights |
| Queue and service systems | arrival/service process + service recommendation | arrival diagnosis -> queue/simulation -> policy -> peak stress | service-flow figure, utilization table, waiting plot, policy table | `针对服务拥堵问题，估计...到达与服务参数，建立...排队/仿真模型并提出...配置；峰值压力测试表明...。` | utilization, waiting, peak condition, bottleneck | average waiting result hides peak-period failure |
| Experimental factor optimization | factors + response/optimum | factor table -> regression/ANOVA -> response surface -> optimum -> verification | factor table, effect plot, contour/surface, optimum table | `针对工艺优化问题，建立...因素响应模型并绘制响应面，得到...最优条件；残差和边界检验说明...。` | residual diagnostics, domain bound, verification proposal | optimum lies outside credible experimental region |
| Rail or timetable service planning | passenger flow + timetable/service plan | flow audit -> route pattern -> objective/constraints -> timetable -> audits | passenger-flow figure, OD/table, route-pattern table, timetable sample | `针对运营组织问题，基于...客流构建...服务方案和时刻表；容量、追踪间隔和停站时间检验表明...。` | section capacity, headway, dwell, baseline comparison | timetable figure exists but recurrence/audits are missing |

## Page Rhythm Conversion

For v1.6, each route should convert into this visible rhythm:

```text
page 1: contest-style title + structured abstract + keywords
page 2: problem restatement and route-oriented analysis
pages 3-4: assumptions, symbols, route or object figure
pages 4-6: first core table or formal model block
pages 7-12: model chain, early results, and at least one validation-aware artifact
middle body: result artifact -> interpretation -> validation artifact loop
tail: model evaluation, conclusion, references, appendix code/script index
```

Do not let pages 2-6 become generic background. A serious CUMCM paper should show its modeling object early.

## Abstract Claim Templates

Use one claim per subquestion:

```text
针对问题一，先通过<support layer>识别<关键结构>，再建立<main model>得到<result artifact>；经<validation artifact>检验，结果表明<answer-level conclusion>。
```

For planning or decision routes:

```text
针对问题二，在<evaluation/forecast/diagnosis>结果基础上建立<decision model>，得到<executable plan/table/rule>；容量、约束或情景检验显示<feasibility conclusion>。
```

For geometry or mechanism routes:

```text
针对问题三，构建<scene/coordinate/mechanism>模型并推导<core relation>，求得<parameter/design result>；通过<residual/feasibility/replay>检验说明结果满足<physical or task requirement>。
```

## Route Selection Warnings

- If the problem asks for quantities, schedules, policies, routes, or rules, the result artifact must be executable.
- If the problem uses forecasts, prediction error must affect the final decision.
- If the problem uses classifiers, error type matters more than a single accuracy value.
- If the problem uses geometry, the scene diagram and coordinate frame must appear before formulas become dense.
- If the problem uses optimization, constraints and feasibility audits are part of the result, not appendix decoration.
- If the problem uses figures, the figure must support route, mechanism, result, or validation.

## Review Questions

Before drafting, answer:

1. Which route family row is primary?
2. What is the paper spine in one line?
3. What result artifact will appear in the abstract?
4. What validation artifact will appear before the conclusion?
5. What first-12-page signal proves this is not generic prose?
6. What fake-completion failure is most likely?
