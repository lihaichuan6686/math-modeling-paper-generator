# CUMCM Paper Generation Playbook

Purpose: turn absorbed CUMCM paper patterns into an executable workflow for a research-only Claude Code agent. This playbook is not a contest submission shortcut. It is a controlled workflow for post-contest research, quality analysis, reproducibility studies, and writing-method experiments.

## Core Principle

A strong CUMCM paper is not an algorithm showcase. It is a closed chain:

```text
problem reading
-> task decomposition
-> model route selection
-> assumptions and variables
-> mathematical formulation
-> computation and figures
-> validation and sensitivity analysis
-> LaTeX paper
-> self review
```

Every important statement in the final paper should be traceable to one of:

- the problem statement
- a data file
- a model equation
- a code output
- a rendered figure/table
- a stated assumption

Use `knowledge/cumcm/official-style-vs-modern-draft-risk.md` as the cross-cutting standard for judging whether a draft is closing loops like an official paper or inflating length like a risky modern draft.

## Phase 0: Intake

Inputs:

- `problems/problem.md`
- attachments and data files
- user research notes
- contest type and year, if known

Required outputs:

- `runs/current/problem-analysis.md`
- `runs/current/data-inventory.md`

Checklist:

- Identify all subquestions.
- Identify decision variables, observed variables, constraints, and evaluation metrics.
- List all data files and their columns.
- Mark missing data, ambiguous units, inconsistent time ranges, and possible hidden constraints.
- Extract keywords that suggest a route: geometry, scheduling, prediction, evaluation, classification, supply chain, physics, simulation, communication, experiment design.

## Phase 1: Route Selection

The agent must propose at least three candidate model chains before choosing one.

Each candidate must include:

- problem type
- model chain
- required data
- expected figures/tables
- validation plan
- risk

Example format:

```text
Candidate A
Type: supply chain planning
Chain: supplier evaluation -> integer programming -> sensitivity analysis
Data needed: historical supply quantity, order quantity, loss rate, capacity
Figures/tables: supplier score table, order plan table, capacity curve
Validation: compare historical fulfillment and stress-test capacity constraints
Risk: supplier score may not transfer directly into optimization objective
```

Selection rule:

- Choose the chain with the best balance of mathematical fit, data support, interpretability, and reproducibility.
- Avoid choosing a complex algorithm only because it sounds advanced.
- Prefer interpretable models when data are small, noisy, or industry-rule-heavy.

Special route rule for E-type problems:

- Do not stop at generic `forecast -> decision`.
- First classify the route as either:
  - `production-route E`: forecast to inventory, service-level, batching, or production decisions;
  - `monitoring-route E`: diagnosis and forecast to monitoring, sampling, or policy decisions.
- Use `knowledge/cumcm/problem-type-paper-archetypes.md` to select `Type C1` or `Type C2` explicitly and record that choice in `runs/current/model-candidates.md`.
- Also consult `knowledge/cumcm/official-style-vs-modern-draft-risk.md` so the selected route inherits the correct evidence chain and fake-completion guards.

## Phase 2: Model Plan

Required outputs:

- `runs/current/model-plan.md`
- `runs/current/verification-plan.md`
- `runs/current/figure-plan.md`

The model plan must define:

- assumptions
- symbols
- variables
- parameters
- objective functions
- constraints
- solver or algorithm
- validation metrics
- expected artifacts
- required explanatory figures
- required result figures

Minimum modeling closure:

```text
For each subquestion:
question -> variables -> model -> code -> result -> validation -> paper paragraph
```

At this phase, figures must already be planned. CUMCM papers without figures usually look unfinished, and figure planning changes the modeling work itself. The agent should decide early which figures are needed to explain the model, which figures are needed to prove the result, and which figures are needed to validate robustness.

For E-type problems, the model plan must also declare the route family:

```text
E-route family:
- production-route E
or
- monitoring-route E
```

and explain why the selected route matches the subquestions better than the other E-route family.

## Phase 3: Implementation

Code structure:

```text
src/
  data/
  models/
  figures/
  tables/
  utils/
runs/current/
paper/figures/
paper/tables/
```

Requirements:

- One reproducible entry point should rebuild major outputs.
- Random methods must set or record seeds.
- Figure scripts must save files with stable names.
- Explanatory figures must be saved with stable names and recorded in the artifact ledger, even if they are manually drawn or generated from a prompt.
- Tables in the paper must come from saved CSV/Markdown/LaTeX table artifacts when possible.
- Results used in the abstract must be traceable to generated outputs.

Figure generation belongs inside the implementation chain, not after writing. Treat figures as first-class outputs:

```text
model idea -> figure plan -> code/image generation -> paper/figures -> caption -> text reference -> PDF inspection
```

Two figure classes are allowed:

- Evidence figures: generated from data, code, simulation, or model outputs. These must be reproducible.
- Explanatory figures: workflow diagrams, geometry sketches, mechanism diagrams, route diagrams, or conceptual layouts. These may be drawn, generated, or assembled, but their source/prompt/tool must be recorded.

## Phase 4: Paper Writing

Recommended section order:

```text
Abstract
1 Problem Restatement
2 Problem Analysis
3 Assumptions
4 Symbol Table
5 Data Processing and Exploratory Analysis
6 Model Establishment and Solution
7 Results and Validation
8 Sensitivity Analysis
9 Strengths, Limitations, and Extensions
10 Conclusion
References
Appendix
```

The actual writing order should usually be:

```text
problem analysis
-> assumptions
-> model sections
-> results
-> validation
-> limitations
-> conclusion
-> abstract
```

Do not write the abstract before results exist.

## Abstract Pattern

A CUMCM abstract should be a compressed version of the full solution, not a generic introduction.

Template:

```text
This paper addresses [problem target]. For problem 1, we [model/method] and obtain [key result]. For problem 2, we [model/method] and obtain [key result]. For problem 3, we [model/method] and obtain [key result]. We validate the models using [validation method]. Results show [most important quantified conclusion]. Keywords: ...
```

Rules:

- Mention each subquestion.
- Include methods and results together.
- Include numbers when they are verified.
- Do not include unsupported claims.
- Do not list algorithms without saying what they solved.

## Page-Length Plan

Target body: 20-30 pages for a full research-quality paper, depending on the problem and data.

The page count should come from the natural CUMCM structure, not from padding. A long paper is easy to reach when each required section has its own role: abstract, problem restatement, analysis, assumptions, symbols, data, model, solution, validation, evaluation, references, and appendix.

Recommended allocation for a 20-30 page body:

| Section | Pages | Notes |
|---|---:|---|
| Abstract | 1 | problem-by-problem methods and results |
| Problem restatement | 1-2 | concise rewriting of background, tasks, constraints |
| Method overview | 1-2 | route map and model chain before details |
| Problem analysis | 2-4 | subquestion-level route explanation |
| Assumptions | 0.5-1 | justified simplifications |
| Symbol table | 0.5-1 | compact but complete |
| Data processing | 2-4 | cleaning, plots, feature construction |
| Modeling and solution | 8-14 | main mathematical content |
| Results and validation | 3-5 | tables, figures, robustness |
| Strengths and limitations | 1-2 | honest and specific |
| Conclusion | 0.5-1 | decisions and findings |
| References | 0.5-1 | real, relevant sources |
| Appendix | 3-8 | code excerpts, extra tables, run notes |

Structural rule:

- Each section must earn its pages by doing a different job.
- Do not merge method overview, problem analysis, and model establishment into one vague block.
- Do not stretch problem restatement by copying the problem statement.
- Do not stretch references with irrelevant citations.
- Use figures and tables to carry real content instead of adding prose filler.

Route-specific writing rule for E papers:

- production-route E papers must continue from forecast outputs to service-level, inventory, or production actions;
- monitoring-route E papers must continue from diagnosis and forecast outputs to monitoring or policy actions;
- do not write both as if they were the same `time-series paper`.

## Figure and Table Expectations

Minimum target for a full paper:

- 1 route or method-overview figure
- 2-4 explanatory figures
- 3-6 data/process/result figures
- 3-8 tables
- 1 validation, sensitivity, or error analysis figure/table

Preferred artifacts by problem type:

- geometry/engineering: coordinate diagrams, before-after surfaces, error maps, parameter sensitivity tables
- data analysis/prediction: distribution plots, correlation heatmaps, residual plots, prediction curves, feature importance
- optimization: decision tables, convergence curves, scenario comparison tables, constraint-satisfaction checks
- scheduling: Gantt charts, time-resource usage plots, adjustment logs
- classification: confusion matrix, metric table, feature projection, ablation comparison
- supply chain: score table, order/transport plan table, capacity boundary curve
- E production-route: representative-material figures, forecast-vs-actual tables, service-level tables, rolling production tables, capacity-scenario comparison
- E monitoring-route: diagnostic figures, forecast-vs-history plots, monitoring-decision tables, intervention-effect comparisons, long-horizon consequence tables

Figure source rules:

- Data-driven figures should be generated by scripts under `src/figures/` or an equivalent reproducible path.
- Conceptual diagrams may be generated by a drawing tool, Mermaid, LaTeX/TikZ, Python, or an image-generation tool.
- AI-generated explanatory images must not invent data. They can illustrate structure, geometry, workflow, or mechanism only when labeled as schematic.
- Every figure must be recorded in `runs/current/artifact-ledger.md` with file path, source tool, input data or prompt, paper section, and status.
- Captions should explain what the reader should learn from the figure, not only name the object.

## Validation Requirements

Every paper needs at least one validation strategy:

- residual or error analysis
- sensitivity analysis
- baseline comparison
- historical backtest
- constraint satisfaction audit
- scenario stress test
- cross-validation or holdout testing
- physical or business sanity check

Validation is not optional decoration. It is evidence that the model is not only formatted correctly.

E-route validation rule:

- production-route E papers should validate forecast usefulness through service-level, support-rate, inventory, or capacity consequences;
- monitoring-route E papers should validate diagnostics and show that forecast outputs actually feed the monitoring or policy model.

## Self-Review Gate

Before final PDF output, answer:

1. Does every subquestion have a model, result, and validation?
2. Are all symbols defined before or near first use?
3. Do code outputs match paper tables and figures?
4. Are all figures and tables cited in text?
5. Are assumptions plausible and connected to model simplification?
6. Does the abstract contain verified results rather than placeholders?
7. Are references real and relevant?
8. Does the LaTeX PDF compile without missing figures, broken references, or font issues?
9. Are contest-cover, team identity, and stale template fields removed or handled for research use?
10. Does the paper clearly distinguish evidence, assumptions, and inference?

## Responsible-Use Gate

The agent must refuse or redirect requests that ask for:

- active contest cheating
- hiding AI involvement in a prohibited context
- fabricating data, citations, experiments, or official results
- making a paper appear human-written for dishonest submission

Allowed use:

- post-contest reconstruction
- research comparison between human and AI papers
- quality checking
- reproducibility analysis
- authorized educational or methodological experiments
