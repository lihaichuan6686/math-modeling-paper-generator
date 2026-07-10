# 2021 D Same-Problem Comparison: D017, D026, D034

Purpose: compare multiple official excellent papers for the same 2021 CUMCM D problem so the generator can learn the stable backbone of online cutting/scheduling papers and the acceptable variation in modeling voice, result organization, and appendix evidence.

## Corpus

Source folder:

```text
D:\2-各比赛Word模板及LaTeX模板\国赛历年论文【公众号：竞赛资料网】整理\2021年高教社全国大学生数学建模竞赛优秀论文【公众号：竞赛资料网】】
```

Samples used:

- `D017.pdf`
- `D026.pdf`
- `D034.pdf`

Page counts observed by `pdfinfo`:

- `D017`: 21 pages
- `D026`: 36 pages
- `D034`: 30 pages

Reading basis:

- `D017` already has a full deep read in `knowledge/cumcm/deep-reading-2021D017.md`.
- `D026` and `D034` were compared through rendered-page inspection of abstract pages, structure/analysis pages, mid-paper model/result pages, and appendix pages.

## Why This Comparison Matters

2021 D is a strong same-problem comparison target because all three papers solve the same online continuous-cutting problem, but they do not sound like copies of one another. They share the same industrial process and update logic, yet differ in how they enter the problem:

```text
process rule understanding
-> baseline cutting scheme
-> abnormal scrap-event handling
-> online adjustment
-> changed target-value reuse
-> appendix code / tables
```

This makes the batch ideal for generator training: the route is stable, but the writing voice can shift between theorem-led, multiobjective-planning-led, and algorithm-design-led styles.

## Stable Backbone Across All Three Papers

Across `D017`, `D026`, and `D034`, the following route elements are effectively fixed:

1. Explain the continuous casting and cutting process before serious modeling.
2. Solve a baseline cutting problem before dealing with abnormalities.
3. Treat abnormal scrap segments as event-driven updates rather than as ordinary noise.
4. Separate initial cutting plans from adjusted cutting plans.
5. Reuse the same basic route for changed user target values in later subquestions.
6. Put implementation evidence in an appendix, often with substantial code excerpts.

Reusable generator rule:

```text
For online cutting/scheduling papers, the generator should default to:
process explanation -> baseline plan -> event classification -> update rule -> adjusted plan -> changed-target reuse -> appendix evidence
```

## What Varies

Even with the same backbone, the lead style differs a lot:

- `D017`: proof-led and theorem-led, then integer programming and scenario updates.
- `D026`: multiobjective planning-led, with explicit staged objective stacking and many scheme tables.
- `D034`: algorithm-design-led, with stronger rule reasoning and direct program implementation.

Generator lesson:

```text
Keep the route fixed, but allow the dominant rhetorical mode to vary:
proof-first,
planning-first,
or algorithm-design-first.
```

## Abstract Comparison

### D017

Known from the deep read:

- highly compressed problem-by-problem summary;
- gives methods and key numbers;
- emphasizes zero-loss conditions, discretization, integer programming, and abnormal-event scenario results.

Signal:

```text
method + scenario + numeric result
```

### D026

Observed from page 1:

- abstract is very long and directly tied to the numbered subproblems;
- builds a three-objective model for problem 1 and then reuses it;
- emphasizes specific cutting lengths like `9.5 m` and target intervals like `9.0-10.0 m`;
- gives concrete table references as part of the abstract narrative.

Signal:

```text
multiobjective planning route with strong subproblem-by-subproblem decomposition
```

### D034

Observed from page 1:

- abstract explains the industrial process in words before heavy optimization;
- centers on reducing cutting loss first and user satisfaction second;
- emphasizes algorithm design and program implementation;
- mentions `Dev-C++` and `Excel` explicitly as solution support.

Signal:

```text
algorithm-design and implementation route with stronger engineering narration
```

## Structure Comparison

### D017

From the existing deep read:

- front matter is compact;
- derivation and theorem appear early;
- scenario tables dominate the middle;
- evaluation plus appendix finish the paper.

This is the most compact and contest-efficient structure of the three.

### D026

Observed from early and middle pages:

- abstract is longer than in `D017`;
- problem 2 and problem 3 are written through explicit model-establishment subsections;
- many formulas are stacked as multiobjective models;
- result evidence is strongly table-led, especially scheme-comparison tables;
- appendix contains long MATLAB/intlinprog-oriented code excerpts.

Structure lesson:

```text
D026 shows a "dense optimization notebook" style: more pages, more formal objective stacking, more direct scheme tables.
```

### D034

Observed from early and later pages:

- early pages spend more effort on problem analysis than on formal theorem statements;
- the paper frames each subproblem as an algorithm-design task;
- appendix is a full section with `Dev-C++` code, not just a short file list;
- the route is more rule-driven and implementation-explanatory.

Structure lesson:

```text
D034 is a good template when the generator needs a more procedural, engineering-algorithm style paper instead of a solver-heavy mathematical voice.
```

## How the Same Problem Produces Different Lengths

This batch is a great reminder that page count is not a direct proxy for quality style:

- `D017` reaches full compact-paper quality in 21 pages by using dense scenario evidence and limited exposition.
- `D026` expands to 36 pages by writing separate objective layers more explicitly and carrying more table detail.
- `D034` expands to 30 pages by explaining rules and implementation decisions more narratively.

Generator implication:

```text
To write a believable 20-30 page paper, the generator does not need to imitate the longest version. It needs to choose one valid depth strategy:
compact theorem-and-scenario,
expanded multiobjective planning,
or implementation-heavy algorithm design.
```

## Result Evidence Comparison

### D017

Main evidence form:

- repeated scenario tables;
- initial-vs-adjusted plan comparison;
- summed loss metrics;
- a few high-value schematics.

### D026

Observed evidence style:

- many explicit optimization models with target-specific formulations;
- cutting-scheme comparison tables showing initial and adjusted plans;
- stronger table density than figure density;
- appendix code for optimization subroutines.

This is the most table-forward of the three.

### D034

Observed evidence style:

- more explanatory analysis in prose;
- fewer visible stacked mathematical targets than `D026`;
- strong emphasis on executable algorithms and code;
- appendix code serves as proof of implementability.

This is the most implementation-forward of the three.

Generator rule:

```text
For online optimization papers, result evidence should usually be table-led. Figures are helpful for process explanation, but the core audit trail is the plan table.
```

## Modeling Route Comparison

### D017 Route

```text
structural condition
-> proof
-> discretization
-> integer programming
-> event-type scenarios
-> adjusted loss tables
```

### D026 Route

```text
multiobjective baseline model
-> target-count maximization layers
-> abnormal scrap integration
-> initial plan vs adjusted plan comparison
-> changed-target reuse
-> optimization code appendix
```

### D034 Route

```text
tail-length / target relation
-> cutting-rule algorithm
-> abnormal-event adjustment idea
-> changed-target reuse
-> direct program implementation
```

Comparison lesson:

```text
The same route can be justified by proof, by optimization layering, or by algorithmic construction. The generator should decide that voice early and keep it consistent.
```

## Stable Writing Contracts for 2021 D Style Papers

### 1. Process Contract

The paper should explain:

- what is being cast;
- where cutting happens;
- what counts as an abnormal scrap event;
- why online adjustment is needed.

Without this, formulas look detached from the industrial process.

### 2. Baseline-before-Abnormality Contract

Always solve:

- the normal cutting scheme first,
- then the first abnormal event,
- then repeated or later abnormal events,
- then changed target values.

This sequence is stable across the batch.

### 3. Update-Audit Contract

Each abnormal-event section should show:

- initial plan,
- abnormal trigger,
- adjusted plan,
- loss change or operational effect.

### 4. Reuse Contract

Later subquestions should explicitly state:

- which previous model is reused,
- what parameters changed,
- whether the update rule itself changed or remained fixed.

## What Creates Page Depth Here

This same-problem batch shows that page depth comes from:

1. baseline process explanation,
2. one model per subquestion,
3. repeated but auditable update tables,
4. interpretation of scheme differences,
5. appendix implementation evidence.

Reusable rule:

```text
For online scheduling papers, length should come from "scenario closure" rather than broad generic discussion.
```

## Appendix Comparison

All three papers treat the appendix as serious evidence, but the emphasis differs:

- `D017`: file inventory plus code excerpts grouped by subproblem.
- `D026`: long MATLAB/intlinprog-style code listings tied to the optimization route.
- `D034`: explicit `Dev-C++` implementation section with procedural code excerpts.

Generator implication:

```text
Appendix evidence can be solver-led or language-led, but it should map implementation back to subproblems.
```

## Review Signals for Future Quality Checking

Strong signals:

- baseline plan exists before abnormal scenarios;
- online adjustment is not described only in prose but shown in tables;
- changed target values reuse earlier logic instead of inventing a disconnected model;
- appendix code exists and matches the chosen modeling voice.

Risk signals:

- no industrial-process explanation;
- abnormal events are mentioned but not classified or operationalized;
- only final loss is reported without initial-vs-adjusted comparison;
- later target-value problems are solved by a fresh model with no reuse explanation;
- appendix is absent or disconnected from the main-text method.

## Best Use in the Repository

Use this note when:

- building an online optimization paper prompt;
- reviewing whether a generated 2021 D style paper has enough scenario evidence;
- choosing between a compact theorem-led route and a more procedural implementation-led route;
- deciding how much appendix code evidence is needed for scheduling papers.

## Suggested Next Reading

The next high-value comparison after this one is a modern same-problem batch from 2024 materials, because that can show how more recent drafts differ from official concise styles in code traceability, paper polish, and possible generated-draft weaknesses.
