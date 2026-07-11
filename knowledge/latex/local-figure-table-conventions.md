# Local Figure and Table Conventions

Purpose: extract practical contest-style figure and table conventions from the local awarded LaTeX paper while separating strong evidence habits from local formatting habits that should not always be copied literally.

This note is a figure/table behavior guide, not a template dump.

## Sources

Local source reviewed:

```text
D:\2-各比赛Word模板及LaTeX模板\LATEX\model1.tex
D:\2-各比赛Word模板及LaTeX模板\LATEX\model1.pdf
```

Supporting evidence used:

- caption and figure/table insertion patterns from `model1.tex`;
- rendered pages in `knowledge/_generated/model1_review/`.

## Why This Note Matters

The local sample is useful because it shows how a real awarded paper uses many figures and tables to keep five subquestions visually alive.

Its main lesson is not "copy every caption or table border style".

Its main lesson is:

```text
figures and tables should keep each subquestion visible as a complete evidence loop.
```

## What The Local Sample Does Well

### 1. Object-first early figure

On page 2, the first strong figure identifies the scene directly.

Generator rule:

```text
The first visible figure in a full paper should usually tell the reader what object, geometry, network, or scene is being modeled.
```

### 2. Figure chains support subquestion progression

The local paper does not rely on one final showcase figure.
It uses several figure families:

- scene and geometry figures;
- search/optimization process figures;
- convergence figures;
- Monte Carlo or distribution figures;
- final arrangement or interval figures.

Generator rule:

```text
For multi-question papers, each major subquestion should usually own at least one visible figure family rather than borrowing all visuals from one earlier section.
```

### 3. Tables are used as result carriers, not decorations

The sample repeatedly uses tables to hold:

- parameter combinations;
- result summaries;
- partial support-material displays.

Generator rule:

```text
Result tables should carry executable values, not only descriptive summary text.
```

### 4. Mid-paper figures are paired with nearby interpretation

From the rendered pages, result and convergence figures are usually surrounded by text that explains what the figure means for the current question.

Generator rule:

```text
Do not let a result figure sit alone. It should be followed by an interpretation paragraph or be introduced by one immediately before it.
```

### 5. Appendix code is preceded by support-file structure

The local sample includes a support-file directory before code excerpts.

Generator rule:

```text
If appendix code is included, first show the support-file structure so the reader knows what the code block belongs to.
```

## What To Learn, But Not Copy Blindly

### 1. Local sample uses many short or generic captions

Observed caption style includes labels such as:

- `结果示意图`
- `网格搜索示意图`
- `多图并排示例`

These captions are acceptable as local contest shorthand, but `v1.2` should usually be more explicit.

Upgrade rule:

```text
Prefer captions of the form:
object shown + modeling purpose + what the reader should notice
```

### 2. Local sample uses vertical-line tables

The awarded sample often uses bordered tables with vertical rules.

This is useful as a reminder that contest papers tolerate local style variation, but it is not the best default for the generator.

Upgrade rule:

```text
Default to booktabs-style tables for generated papers unless the local template or page pressure strongly favors bordered tables.
```

### 3. Raw filenames in the local project are not reusable naming practice

The local assets include names such as:

- `output3.png`
- `result33.png`
- `5-2.png`

These are understandable in a one-off team project, but they are weak for a long-term generator.

Upgrade rule:

```text
Keep stable English artifact filenames in the generator even when the source sample uses local shorthand names.
```

## Contest-Style Figure Families To Reuse

From the local sample, the most reusable families are:

1. scene identification figure;
2. geometry or relation figure;
3. search/process figure;
4. convergence figure;
5. stochastic or distribution figure;
6. final result arrangement figure.

These should map naturally into:

```text
problem restatement
-> model establishment
-> solving process
-> results
-> validation
```

## Contest-Style Table Families To Reuse

From the local sample, the most reusable table roles are:

1. parameter/result table for one question;
2. comparison table across strategies or agents;
3. partial support-material table inside the body;
4. support-file directory table before appendix code.

## v1.2 Upgrade Rules

Use the local sample as a behavioral model:

- figures appear early and often enough to keep the paper concrete;
- tables carry real values;
- appendix supports trust.

But upgrade the generated output beyond the local sample by requiring:

1. more specific captions;
2. stable artifact naming;
3. cleaner default table style;
4. stronger prose interpretation after each important figure or table;
5. clearer distinction between body evidence and appendix support material.

## Best Use

Read this note together with:

- `figures-tables-equations-style.md`
- `visual-family-index.md`
- `table-family-index.md`
- `local-awarded-paper-structure-rules.md`
- `../../docs/visual-generation-pipeline.md`
