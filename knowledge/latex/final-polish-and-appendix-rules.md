# Final Polish and Appendix Rules

Purpose: capture the late-stage finishing rules that help a CUMCM paper feel complete at handoff time, especially around evaluation, references, appendix transition, support-file listing, and code appendix boundaries.

This note is about paper finishing behavior, not route selection.

## Sources

Primary local source:

```text
D:\2-各比赛Word模板及LaTeX模板\LATEX\model1.tex
D:\2-各比赛Word模板及LaTeX模板\LATEX\model1.pdf
```

Supporting rendered evidence:

```text
knowledge/_generated/model1_review/model1-31.png ... model1-38.png
```

Supporting review/risk notes:

- `knowledge/cumcm/official-style-vs-modern-draft-risk.md`
- `knowledge/quality/quality-rubric-v2.md`
- `docs/review-checklist.md`

## Why This Note Matters

Many generated drafts look acceptable until the final third of the paper.

That is where they often fail by:

- ending too abruptly after results;
- adding a weak limitations section;
- bloating appendix pages without first closing the body;
- mixing body evidence and code support without clear boundaries;
- letting page count come from late appendix expansion instead of completed argument.

The local awarded sample is useful because it shows a better order:

```text
results
-> model evaluation and extension
-> references
-> appendix note
-> support-file directory
-> code appendix
```

## What The Local Sample Teaches Well

### 1. The body closes before code begins

Observed from `model1.tex`:

- `模型评价与推广` appears before references and appendix;
- references are complete before code excerpts begin;
- `附录说明` explicitly tells the reader that only core code is shown and full files are elsewhere.

Generator rule:

```text
Do not enter appendix code until the body has already closed the result, evaluation, and conclusion logic.
```

### 2. A support-file directory improves trust

The local sample inserts a dedicated `支撑文件目录` section with a table of filenames and roles before the code blocks.

Generator rule:

```text
When appendix code is included, first give a support-file inventory table so the reader can map files to questions and outputs.
```

### 3. Appendix code is grouped by question and method role

The code appendix is not one undifferentiated dump. It is divided into entries such as:

- question 1 method 1;
- question 1 method 2;
- question 2 grid search;
- question 2 genetic algorithm;
- question 3 Monte Carlo proof;
- question 3 Bayesian solution;
- question 4 Monte Carlo proof;
- question 4 Bayesian solution;
- question 5 global judgment function.

Generator rule:

```text
If code excerpts appear in the PDF, group them by subquestion and role rather than by raw file order.
```

### 4. Evaluation and extension should be concise but real

The local paper includes a short but explicit `模型评价` and `模型推广` block before references.

The value is not that every sentence is perfect. The value is that the paper does not jump from results to appendix with no reflective closure.

Generator rule:

```text
Before references, include a short section that states strengths, weaknesses, and extension scope in direct problem-aware language.
```

## What Must Be Upgraded For v1.2

The local sample is a strong reference, but the generator should improve on it in several ways.

### 1. Evaluation must be less generic

The local evaluation language contains useful intent, but parts of it are broad and praise-heavy.

Upgrade rule:

```text
For v1.2, strengths and limitations should be tied to specific evidence, such as model depth, validation type, variable reduction, scenario handling, or artifact traceability.
```

### 2. Appendix pages must not be counted as body completion

Rendered pages 31-38 show how much space code can occupy once appendix begins.

This is legitimate only if the main body already stands on its own.

Upgrade rule:

```text
Treat appendix budget separately from body budget. A long appendix does not repair a thin result or validation section.
```

### 3. Code excerpts should confirm, not replace, the model explanation

The local sample works because the modeling logic is already in the body before the appendix code begins.

Upgrade rule:

```text
If the body still lacks variable definitions, solver logic, or interpretation, do not add more code blocks. Repair the body first.
```

## Late-Stage Finish Rules

Use these rules during final drafting or revision:

1. After the last result subsection, check whether evaluation and limitation closure is still missing.
2. Keep references before appendix code.
3. Add an appendix note when only core excerpts are shown in the PDF.
4. Add a support-file inventory before long code excerpts.
5. Group appendix code by question and method role.
6. Separate body evidence from appendix support when counting effective paper length.
7. If body pages are already sufficient, prefer shorter appendix excerpts plus stronger file inventory.

## Review Rules Added

At final review time, ask:

- does the paper close with evaluation before code?
- is the appendix boundary obvious?
- is the support-file directory present when appendix code is shown?
- are code excerpts traceable to specific subquestions?
- would the body still feel complete if appendix screenshots were removed?

If the answer to the last question is no, the draft is not handoff-ready.

## Best Use

Read this note together with:

- `local-awarded-paper-structure-rules.md`
- `local-figure-table-conventions.md`
- `long-paper-blueprint.md`
- `../../docs/review-checklist.md`
- `../../knowledge/cumcm/official-style-vs-modern-draft-risk.md`
