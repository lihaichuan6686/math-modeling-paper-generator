# Recent Award Paper Visual Rhythm

Purpose: record observable layout and length signals from recent local CUMCM award-paper PDFs.

This note supports v1.4 paper-feel control. It is not a content-copying source and should not be used to imitate any single paper.

## Sample Scope

Local source folder:

```text
国赛历年论文【公众号：竞赛资料网】整理
```

Machine-readable inventory:

- total files in the local paper folder: 217;
- PDF files: 79;
- recent 2021-2023 award-paper PDFs inspected for page count: 33.

Recent page-count statistics from the 33 inspected PDFs:

| Metric | Page count |
|---|---:|
| Minimum | 21 |
| Median | 38 |
| Mean | 39.5 |
| Maximum | 60 |

Interpretation:

- a credible national-award style paper is often longer than a minimal 20-30 page target;
- 20-30 pages can still be a usable v1 draft target, but it should not be treated as the mature award-paper ceiling;
- 30-45 pages better matches stronger award-paper feel when the evidence burden supports it;
- page count should be earned by evidence distribution, not by restatement padding.

## Opening Rhythm

Five 2023 award-paper PDFs were sampled by rendering the first two and last two pages:

| Paper | Page count | Opening/closing signal |
|---|---:|---|
| `A0127.pdf` | 50 | title plus dense abstract and keywords; page 2 enters restatement; tail contains appendix code |
| `B311.pdf` | 31 | title plus dense abstract; page 2 enters restatement; tail contains appendix code |
| `C050.pdf` | 41 | title plus dense abstract and keywords; page 2 enters restatement/analysis; tail contains code blocks |
| `D039.pdf` | 27 | title plus dense abstract and keywords; page 2 enters statement/analysis; tail contains code |
| `E176.pdf` | 50 | title plus dense abstract and keywords; page 2 enters restatement/analysis; tail contains code |

Observable pattern:

```text
title + near-full-page abstract + keywords
-> page 2 quickly enters problem restatement / analysis
-> middle pages carry model, results, figures, tables, validation
-> final pages often hold appendix code or supplementary implementation detail
```

## Front-12-Page Rhythm

Three 2023 papers with different total lengths were visually sampled through their first 12 pages.

| Paper | Total pages | Early-body signal |
|---|---:|---|
| `A0127.pdf` | 50 | page 4 includes symbol table and model/geometry figures; pages 5-12 alternate formulas, diagrams, and prose |
| `B311.pdf` | 31 | page 1 abstract includes formulas; page 4 has symbol table and model-establishment start; pages 6-12 include formulas, result tables, and schematics |
| `D039.pdf` | 27 | pages 4-5 include symbol table and data/result tables; pages 10-12 include curve figures and dense result tables |

Converted signal:

- by pages 4-6, a serious paper should usually show at least one of: symbol table, route/model diagram, data table, parameter table, or formal model block;
- by pages 8-12, the paper should no longer be pure prose; formulas, figures, tables, or model artifacts should visibly alternate with interpretation;
- a shorter paper can still feel strong if computational artifacts appear early and are interpreted.

## Middle-Body Rhythm

The same three papers were visually sampled through representative middle pages:

| Paper | Middle pages inspected | Middle-body signal |
|---|---|---|
| `A0127.pdf` | pages 13-24 | nearly every page contains tables, curves, diagrams, equations, or workflow blocks with nearby explanation |
| `B311.pdf` | pages 10-21 | result curves and surface/contour plots appear around pages 13-16; code and supporting tables begin appearing later |
| `D039.pdf` | pages 8-19 | formula derivation remains dense, with curve figures and result tables inserted around the model/result transition |

Converted signal:

- the model core should maintain visible mathematical or computational objects across the middle pages;
- result figures and tables should not be delayed until the very end of the paper;
- a page without a figure or table can still feel strong if it contains real formulas, definitions, case logic, or algorithm structure;
- code listings should usually appear after the main model/result explanation, not before the reader has seen the answer logic.

## Tail And Appendix Rhythm

Five 2023 papers were visually sampled through their final 12 pages.

| Paper | Tail pages inspected | Tail signal |
|---|---|---|
| `A0127.pdf` | pages 39-50 | final 12 pages are almost entirely appendix code |
| `B311.pdf` | pages 20-31 | late pages contain result tables, then code/support material |
| `C050.pdf` | pages 30-41 | pages 30-35 still contain result tables and charts; pages 36-41 become code-heavy appendix |
| `D039.pdf` | pages 16-27 | model/result closure continues through pages 16-20; pages 23-27 are code-heavy appendix |
| `E176.pdf` | pages 39-50 | final 12 pages are code-heavy appendix |

Converted signal:

- appendix code can occupy a substantial tail block in award-paper PDFs;
- this is acceptable only if the body has already shown formulas, result tables, result figures, and interpretation;
- references and appendix transitions may be visually brief, but they should be deliberate and not omitted;
- code pages should support reproducibility, not replace the main explanation.

## Rules Converted For v1.4

### Abstract Page Rule

The first page should look like a serious compressed solution:

- title at top;
- dense abstract occupying most of the page;
- keywords at the bottom;
- method and result for every major subquestion;
- no long generic background paragraph.

A half-page abstract is a warning sign for multi-question CUMCM papers unless the problem is unusually small.

### Early Body Rule

The second page should already feel like the paper is solving the problem.

Good early rhythm:

```text
problem restatement
-> problem analysis
-> model assumptions / symbols
```

Weak early rhythm:

```text
long background
-> generic contest introduction
-> delayed modeling route
```

### First-12-Pages Artifact Rule

Before final writing, plan the first 12 pages deliberately:

- page 1: title, dense abstract, keywords;
- page 2: problem restatement and/or problem analysis begins;
- pages 3-4: assumptions, symbols, route overview, or model setup should appear;
- pages 4-6: at least one table, formal model block, diagram, or equation group should be visible;
- pages 8-12: model artifacts should be recurring, not delayed until late paper.

If the first 12 pages are mostly continuous prose, the paper will look unlike recent award samples.

### Middle-Body Evidence Rule

In the core model and result pages, avoid long artifact droughts.

Good middle-body rhythm:

```text
formula / algorithm / table / figure
-> interpretation
-> next formula / result artifact
-> validation or comparison
```

Warning signs:

- more than 2-3 consecutive pages of mostly prose in a model-heavy problem;
- result tables only appear in the conclusion or appendix;
- code appears before the main result logic is visible;
- figures are decorative and do not connect to the nearby paragraph.

### Effective Length Rule

For v1.4, aim for:

- minimum viable closed-loop draft: 20-30 pages;
- stronger award-feel draft: 30-45 pages when the problem has enough data, subquestions, figures, and validation;
- avoid claiming success from page count alone.

If the draft is under 25 pages, require an explicit reason. If the draft is over 45 pages, require evidence burden such as many subquestions, substantial appendix, multiple datasets, or rich validation.

### Appendix Rule

Appendix pages can support length but should not carry the main answer.

For v1.4 review:

- if code begins before the main result logic is visible, fail the paper;
- if final answer tables exist only inside code output or appendix screenshots, fail the paper;
- if the appendix is long, require a support-file inventory or a clear mapping from code blocks to subquestions;
- if references are visually short, still require real method/data/domain citations where claims appear.

## Extraction Limits

Many recent PDFs in the local folder are image/scanned PDFs. Text extraction did not reliably recover headings, reference counts, figure captions, or table captions.

Therefore:

- page-count statistics are reliable;
- first/last page visual rhythm is reliable for the sampled papers;
- first-12-page artifact timing is reliable for the sampled papers;
- middle-body evidence rhythm is reliable for the sampled papers;
- tail-body and appendix rhythm is reliable for the sampled papers;
- exact reference-count and figure/table-count rules still need OCR or broader manual sampling.

## Use In Generation

When Claude Code generates a v1.4 paper, it should:

1. write the abstract last and make it fill most of page one without exceeding one page;
2. start problem restatement and analysis immediately after the abstract page;
3. make symbols, model setup, tables, equations, or route diagrams visible by pages 4-6 when the problem supports them;
4. ensure pages 8-12 already show recurring model artifacts and interpretation;
5. avoid more than 2-3 consecutive middle-body pages without formulas, tables, figures, algorithm blocks, or result artifacts when the problem supports them;
6. keep main result tables and figures in the body before appendix code starts;
7. use section budgets to push the body toward evidence-rich length;
8. keep appendix code/support material clearly separated and mapped to subquestions;
9. record in review whether the paper is a 20-30 page early draft or a 30-45 page stronger award-feel draft.
