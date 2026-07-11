# Local Awarded Paper Structure Rules

Purpose: convert the user's local awarded LaTeX paper into reusable structure and density rules for future CUMCM-style generation.

This note focuses on paper shape, density, and section behavior rather than on one specific algorithm route.

## Sources

Local source reviewed:

```text
D:\2-各比赛Word模板及LaTeX模板\LATEX\model1.tex
D:\2-各比赛Word模板及LaTeX模板\LATEX\model1.pdf
```

Rendered-page evidence used in this note:

```text
knowledge/_generated/model1_review/model1-01.png ... model1-06.png
knowledge/_generated/model1_review/model1-20.png ... model1-22.png
knowledge/_generated/model1_review/model1-36.png ... model1-38.png
```

Key source facts from the TeX file:

- 38 PDF pages;
- 5 subquestion analysis subsections;
- 5 subquestion solving subsections;
- explicit model evaluation, support-file directory, and code appendix;
- heavy figure and table usage throughout the body.

## Why This Note Matters

This paper is valuable because it shows one real way a strong team paper becomes long without feeling empty:

```text
dense abstract
-> object-first restatement
-> per-question analysis
-> per-question solving
-> visible results and interpretation
-> evaluation
-> support-file appendix
-> code appendix
```

The important lesson is not "copy this exact structure".

The important lesson is:

```text
length comes from repeated full subquestion loops, not from one giant method dump.
```

## Stable Structure Lessons

### 1. The abstract is a real page, not a placeholder

Observed from page 1:

- the abstract occupies essentially the whole first page;
- each question is closed with method plus result;
- the last line gives keywords that match the actual route;
- there is almost no empty background padding.

Generator rule:

```text
For a full v1.2 paper, the abstract should usually read like a compressed paper body: one overall task sentence, then one method-result closure per subquestion, then one final overall result sentence.
```

### 2. The body grows by question loops

Observed from the section tree in `model1.tex`:

- `问题分析` is split into five subquestion analyses;
- `模型的建立与求解` is split into five subquestion solving subsections;
- later sections still keep the same question map in view.

Generator rule:

```text
If the problem has several numbered subquestions, paper length should come from repeating the same loop for each question:
analysis -> model -> solving -> result -> interpretation
```

This is one of the strongest anti-machine rules in the whole repo.

### 3. The second page identifies the modeled object early

Observed from page 2:

- the paper gives a concrete scene description quickly;
- a 3D object figure appears before the paper becomes equation-heavy;
- the problem statement is rewritten as modelable quantities, not copied literally.

Generator rule:

```text
On the first two pages, show the modeled object or scene before the longest derivation begins.
```

### 4. Problem analysis does real route work

Observed from pages 3-6:

- each subquestion gets its own analysis paragraph block;
- the paper explains why optimization becomes harder in later questions;
- it justifies dimension reduction and method changes before solving.

Generator rule:

```text
Problem analysis should not just restate tasks. It should explain why later questions need different variable scopes, different search strategies, or different approximation moves.
```

### 5. Mid-paper density comes from method explanation plus constraints

Observed from pages 20-22:

- advanced methods are not named and abandoned;
- kernel choice, acquisition function, constraint ranges, and variable domains are spelled out;
- results sit next to convergence figures and parameter tables.

Generator rule:

```text
When using a stronger algorithm, explain the input range, constraints, parameterization, and why the algorithm is used here before claiming a result.
```

### 6. Appendix is used to support trust, not replace the body

Observed from pages 36-38 and the section tree:

- the paper includes a support-file directory section before code;
- the code appendix is organized by question and method role;
- the body has already explained the modeling route before appendix code appears.

Generator rule:

```text
Appendix code should confirm that the paper is executable, but the body must already carry the model logic, result logic, and interpretation.
```

## Page-Density Lessons

This sample suggests the following full-paper rhythm:

### Front matter

- page 1: dense abstract;
- page 2: problem restatement plus first object figure.

### Early body

- several pages of subquestion analysis before assumptions/symbols become central;
- route explanation continues even when formulas start appearing.

### Middle body

- the model section is the real core;
- equations, constraints, figures, tables, and method reasoning alternate;
- parameter ranges and simplification logic are written explicitly.

### Late body

- result figures and tables still receive interpretation;
- model evaluation and extension are separate from raw results;
- appendix gives support-file inventory and code by problem role.

## Reusable Soft Rules

1. A complete abstract should nearly fill one page.
2. The first real figure should appear early and identify the object or scene.
3. A multi-question paper should repeat full subquestion loops instead of hiding all reasoning in one monolithic model section.
4. If later questions increase dimensionality, the analysis section should explain why reduction, decomposition, or method switching is justified.
5. Advanced algorithms should be written with constraint ranges, variable domains, and parameter logic, not prestige-only naming.
6. Convergence plots, parameter tables, and result tables should appear inside the body, not only in the appendix.
7. Appendix code should be grouped by question and method role so the paper feels reproducible rather than padded.

## v1.2 Implications

For the generator, this paper suggests a reliable way to make output feel more human-team written:

```text
stable question map
-> early scene figure
-> per-question analysis
-> per-question solving
-> result interpretation
-> separate evaluation
-> support-file appendix
-> code appendix
```

This is especially useful when the first draft feels too thin. In many cases the missing piece is not "more words". It is one or more missing subquestion loops.

## Best Use

Read this note together with:

- `human-style-soft-rules.md`
- `long-paper-blueprint.md`
- `local-template-variant-index.md`
- `style-variant-index.md`
- `../../docs/v1.2-runbook.md`
