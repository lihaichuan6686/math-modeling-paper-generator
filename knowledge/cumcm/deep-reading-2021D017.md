# Deep Reading: 2021 D017 Continuous Cutting Online Optimization

Source:

```text
D:\2-各比赛Word模板及LaTeX模板\国赛历年论文【公众号：竞赛资料网】整理\2021年高教社全国大学生数学建模竞赛优秀论文【公众号：竞赛资料网】】\D017.pdf
```

Rendered pages:

```text
knowledge/_generated/deep_2021D017-01.png ... deep_2021D017-21.png
```

This is the first full-structure deep reading note for an official excellent paper. The goal is to learn how a compact 20-page CUMCM paper is organized, not to imitate its text.

## Basic Profile

- Year/problem: 2021 D
- Topic: continuous casting/cutting online optimization
- Pages: 21
- Problem type: online scheduling, industrial optimization, integer programming, abnormal-event adjustment
- Main methods:
  - sufficient-condition proof
  - discretization by cutting precision
  - integer linear programming
  - staged scenario analysis
  - online adjustment strategy
- Main evidence form:
  - process schematic figures
  - formula derivation
  - piecewise-function tables
  - repeated scenario result tables
  - appendix code inventory and code excerpts

## Page-Level Structure Map

| Pages | Role | Observed content | Generator lesson |
|---:|---|---|---|
| 1 | Abstract | Problem-by-problem compressed solution, including methods and numerical results | Abstract should be written after results and include actual numbers |
| 2 | Problem restatement | Background, process diagram, abnormal-segment diagram, numbered tasks | Put explanatory figures early when the industry process is unfamiliar |
| 3 | Assumptions, symbols, problem analysis | Six assumptions, compact symbol table, route analysis | Keep pre-model sections tight; reserve pages for model/result evidence |
| 4-7 | Model preparation and problem 1 model | Theorem/proof, tail-loss condition, discretization into 79 length specs, integer programming | Prove or derive structural properties before invoking optimization |
| 8 | Problem 1 results and problem 2 start | Optimal solution table, abnormal-connection type diagram | Results can bridge into the next subproblem when the logic is sequential |
| 9-12 | Problem 2 scenarios | Multiple abnormal-event cases, initial/adjusted cutting plans, loss totals | Scenario tables are primary evidence for online optimization |
| 13-18 | Problem 3 scenarios and results | Reuse problem 2 algorithm with changed target values, many repeated plan tables | Reuse should be explicit: state which conditions changed and which model remains |
| 18-19 | Model evaluation | Strengths, limitations, improvement and extension | A compact paper can use model evaluation instead of a long conclusion |
| 20-21 | Appendix | Support file list, MATLAB/LINGO code excerpts | Appendix begins with file inventory, then problem-specific code |

## Section Pattern

This paper uses a compact but complete structure:

```text
Abstract
1 Problem restatement
2 Model assumptions
3 Symbol table
4 Problem analysis
5 Model establishment and solution
  5.1 Model preparation
  5.2 Problem 1 solution
  5.3 Problem 2 solution
  5.4 Problem 3 solution
6 Model evaluation
Appendix
```

Notably, it does not spend many pages on generic background. The body grows from formulas, scenario tables, and solution evidence.

## Abstract Pattern

The abstract is a strong example of problem-by-problem compression:

- Opening: explains production context and optimization target.
- Problem 1: describes zero-loss condition, 0.1 m precision discretization, 79 length specifications, integer programming, and result ranges.
- Problem 2: describes abnormal scrap segments, three connection cases, adjustment counts, and total loss.
- Problem 3: reuses problem 2 conditions for two target values and reports total losses.
- Keywords: problem type and method terms.

Generator rule:

```text
For each subquestion in the abstract:
method + scenario/constraint + key numeric result
```

Avoid:

- abstract without numbers
- algorithm names without what they solve
- reporting results not shown later

## Figure Strategy

Only a few figures are used, but they are placed early and carry high explanatory value.

Observed figure roles:

- Figure 1: continuous casting process schematic.
- Figure 2: abnormal scrap-segment schematic.
- Figure 3 and later: abnormal segment connection cases.

Generator rules:

- Industrial-process problems need explanatory figures before formulas.
- Online adjustment problems need scenario diagrams that show what changes.
- Schematic figures may be more valuable than decorative result plots when the core difficulty is process logic.
- Figure captions should name the operational situation, not just say "flowchart".

## Table Strategy

Tables dominate the evidence.

Observed table roles:

- Optimal cutting solution table for problem 1.
- Repeated initial-vs-adjusted cutting plan tables for abnormal events.
- Piecewise-function tables for loss functions.
- Scenario tables with total cutting loss.

Generator rules:

- For scheduling/online optimization, a result table should include:
  - event index or scenario
  - initial plan
  - adjusted plan
  - decision time
  - decision length/value
  - loss or objective value
- Repeated tables are acceptable when each table corresponds to a distinct scenario.
- Use tables to make the online update process auditable.

## Modeling Pattern

The paper does not jump directly to a solver. It follows a layered path:

```text
production rule
-> mathematical condition
-> theorem/proof
-> discretization
-> integer programming
-> scenario-specific online adjustment
-> tabular results
```

Key modeling moves:

1. Convert continuous length into discrete specifications using cutting precision.
2. Define tail loss and user-target deviation separately.
3. Build a first-stage model to minimize cutting loss.
4. Build a second-stage model to satisfy target length under minimal loss.
5. For abnormal segments, classify connection types before computing revised plans.
6. For later subquestions, reuse the previous model under changed target values.

Generator rule:

```text
When a problem is online/scheduling based:
baseline model -> event classification -> update rule -> adjusted result table
```

## Validation and Evidence

The paper's validation is mainly internal:

- feasibility is shown through plan tables
- loss is explicitly summed
- model evaluation discusses limitations such as adjustment time not being considered
- code appendix supports reproducibility

This is weaker than modern full validation, but still useful because the result tables are auditable.

Generator improvement:

- Add explicit constraint-satisfaction checks.
- Add sensitivity analysis for cutting precision or target range.
- Add runtime/update-time analysis for online adjustment.
- Record code and table provenance in artifact ledger.

## Appendix Pattern

The appendix starts with a support-file list:

```text
Problem 1 source code:
  fenduahanshu.m
  cutting-loss-minimum-model.lg4
  target-satisfaction-model.lg4
Problem 2 source code:
  main.m
Problem 3 source code:
  main.m
Notes:
  .m is MATLAB, .lg4 is LINGO
```

Then it includes selected code excerpts.

Generator rule:

- Appendix should begin with a file inventory.
- The paper should identify which file supports which subquestion.
- Code excerpts are useful, but runnable source must also exist in `src/`.

## Page Count Lessons

This 21-page paper reaches full length through:

- 1 page abstract
- 2 pages problem restatement/assumptions/symbols/analysis
- 4 pages theorem, derivation, and problem 1 model
- 10+ pages scenario tables and online adjustment results
- 2 pages model evaluation and appendix

It does not rely on long generic background.

Generator rule:

```text
For compact 20-page papers:
keep front matter short,
put explanatory figures early,
make model derivation dense,
use scenario/result tables as evidence,
end with concrete limitations and appendix inventory.
```

## Transfer to Agent Rules

1. For industrial process problems, create process diagrams during the figure-planning phase.
2. For online optimization, separate initial plan, abnormal trigger, adjustment rule, and adjusted plan.
3. For repeated event scenarios, tables are not redundancy if they show different updates.
4. Before using an optimizer, derive the business/mathematical condition that defines feasibility or loss.
5. If a later subquestion reuses an earlier model, state what changes and what remains fixed.
6. Result tables should contain enough columns to audit the decision, not only final objective values.
7. Model evaluation should name limitations tied to assumptions, such as ignored adjustment time.
8. Appendix should map files to subquestions and languages/tools.

## Quality-Checker Signals

For online optimization papers, flag risks when:

- no baseline plan is shown
- abnormal events are not classified
- adjusted plans are not compared with initial plans
- total loss is reported without per-event evidence
- update time or operational feasibility is ignored without disclosure
- code appendix has no file-to-subquestion mapping
- formulas define loss but results do not show loss by scenario
