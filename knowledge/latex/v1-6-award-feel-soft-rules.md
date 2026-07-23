# v1.6 Award-Feel Soft Rules

Purpose: convert local experience notes and award-paper visual sampling into writing rules that make a generated paper look like a serious CUMCM team draft, not a thin AI skeleton.

This file is a soft-rule layer. It should guide planning and writing before the hard gates run.

## Evidence Base

Local materials sampled:

- `9.数学建模经验分享（36篇）/如何写好一篇优秀的建模论文（经验谈）.pdf`
- `9.数学建模经验分享（36篇）/建模心得.pdf`
- `9.数学建模经验分享（36篇）/成为一个数学建模“高手”的八大奥秘.pdf`
- `9.数学建模经验分享（36篇）/大学毕业论文心得-研读数学建模优秀论文心得体会.txt`
- `knowledge/cumcm/recent-award-paper-visual-rhythm.md`
- `knowledge/latex/v1-5-award-paper-style-rules.md`
- `knowledge/latex/v1-5-front-matter-rhythm-rules.md`

Converted principles:

- contest judging cares about reasonable assumptions, model creativity, result reasonableness, and clear expression;
- a strong paper is not necessarily the paper with the most advanced algorithm;
- innovation can appear in modeling abstraction, simplification strategy, solving process, result inspection, validation, or model extension;
- every major question must receive method, result, and interpretation in the abstract and body;
- software and code are support evidence, not a substitute for mathematical reasoning.

## Title Naming Rules

The title should sound like a contest team named its own method after the actual problem.

Good title pattern:

```text
基于[核心机制/模型族]的[对象/任务]建模与[决策/优化]研究
面向[应用场景]的[关键变量]预测、评价与优化模型
[对象]的[识别/调度/评价/预测]模型及其稳健性分析
```

Avoid:

- generic titles such as `数学建模论文`, `某问题研究`, `问题求解报告`;
- AI-sounding titles that stack fashionable terms without connection to data;
- titles that expose only one algorithm when the paper has several subquestions;
- English punctuation, ASCII hyphen, or subtitle gimmicks.

Before writing, create five candidate titles. Select the one that names:

- the task object;
- the main modeling action;
- the decision or evaluation target;
- the paper's strongest method signal.

## Abstract Shape

The abstract should be a compressed full solution. It normally uses a total-branch-total rhythm:

```text
opening: problem context + overall route
针对第一问: method + key result
针对第二问: method + key result
针对第三问: method + key result
closing: robustness, practical value, and final answer scope
keywords
```

Rules:

- make page one visually dense, not half empty;
- answer every subquestion with at least one concrete result or result type;
- bold the most important numerical answers and final decisions when the template allows it;
- do not spend the abstract on generic background;
- do not use one undivided paragraph for a multi-question problem;
- write the abstract last, but reserve its page budget before writing the body.

Soft target:

- 900-1150 extracted Chinese characters for v1.6;
- if the PDF visually shows a half-page abstract, expand method/result descriptions instead of padding background.

## Section Duty Rules

Each section has a job. Do not let sections become ceremonial.

| Section | Must Do | Warning Sign |
|---|---|---|
| Problem restatement | translate the task into modeling objects and required answers | copied task text with no modeling focus |
| Problem analysis | explain route selection, constraints, and subquestion dependency | vague prose before the route appears |
| Assumptions | reduce real complexity with reason, not convenience only | unused assumptions or unjustified simplification |
| Symbols | help reading formulas and code outputs | half-empty symbol page or unexplained variables later |
| Model establishment | define model variables, objective, constraints, and algorithm logic | method names without equations |
| Solution process | show reproducible computation and intermediate evidence | final answer appears without calculation path |
| Results analysis | interpret tables/figures and check intuition | tables listed without explanation |
| Validation | prove the result is not self-comforting | one generic sensitivity paragraph |
| Evaluation | name real strengths and limits | empty praise or fake limitations |
| Appendix | map code and files to questions | code dump with no index |

## Human Team Prose Rules

A human contest team usually sounds like it has argued with the problem.

Add prose where it matters:

- before a formula, explain why this formula is needed;
- after a result table, explain what changed and whether it matches intuition;
- before choosing a model, compare at least one rejected route when the choice is non-obvious;
- after validation, say what the validation protects against;
- when an assumption is strong, name the risk and why the paper still proceeds.

Avoid:

- every paragraph being one or two short sentences;
- bullet-only solution sections;
- repeated generic claims such as `模型具有较好的鲁棒性`;
- unsupported superiority claims;
- decorative algorithms that do not change results.

## Model Depth Without Fake Complexity

Do not optimize for difficult names. Optimize for defensible modeling.

Preferred depth pattern:

```text
baseline model
-> upgraded model or corrected feature construction
-> result comparison
-> validation or sensitivity
-> final selected route
```

This creates award feel better than a single complicated model with no evidence.

Acceptable innovation sources:

- a sharper objective function;
- a domain-aware feature;
- a useful constraint or penalty term;
- a better evaluation index;
- a sanity-check benchmark;
- a visual mechanism diagram that clarifies the whole route.

## Figure And Concept Diagram Rules

The early concept figure should not be a decoration. It should make the paper easier to believe.

Good early figure jobs:

- object or scene abstraction;
- data-to-model route;
- mechanism or dependency diagram;
- decision flow with feedback and validation;
- multi-question relationship map.

The figure should appear in the first six pages when the problem supports it. It should use Chinese labels, grouped zones, clear arrows, and restrained color. If a raster image is used, render the PDF and inspect whether text became boxes or tiny unreadable glyphs.

## Table And White-Space Rules

Tables should be readable and contained.

- Use compact symbol tables; merge assumptions and symbols when either page becomes sparse.
- Use `tabularx`, `adjustbox`, or fixed-width `p{}` columns for text-heavy tables.
- Do not put long file paths or script descriptions in bare `lll` tables.
- If a table has 6+ columns, check the compiled log and rendered PDF before handoff.
- Do not allow the symbol page or assumption page to waste half a page unless the next section starts naturally on the same page.

## Self-Review Questions

Before final handoff, answer:

1. Would the title pass as a CUMCM team title?
2. Does the abstract visibly fill page one and answer every subquestion?
3. Does page 2 enter restatement or analysis without a long generic background?
4. By pages 4-6, is there a symbol table, route figure, model diagram, formula block, or data table?
5. Does every major result table have interpretation near it?
6. Does validation test the result, not merely praise it?
7. Are table width, blank space, and figure readability checked from the rendered PDF?
8. Does the appendix include key code or a script index mapped to questions?
