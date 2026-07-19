# v1.5 Award-Paper Style Rules

Purpose: convert the v1.4 user test failure into concrete paper-surface rules. v1.5 is not mainly an algorithm release; it is an award-paper feel release.

Read this together with `v1-5-award-paper-visual-fingerprint.md` when judging whether the rendered PDF looks like a recent awarded paper rather than only a structurally complete draft.

## Failure Being Fixed

The v1.4 test produced a complete 20-page report, but it looked like an AI technical report:

- the title was a direct task label rather than a contest-paper title;
- the abstract was one block and left too much page-one whitespace;
- prompt/planning language leaked into the body;
- figures looked like script screenshots;
- section text was too short and checklist-like;
- the LaTeX structure had to be rebuilt by the running model;
- appendix code was missing;
- unreasonable model artifacts were not blocked.

## Title Patterns

Do not use the problem statement as the title.

Before selecting the final title, write `runs/current/title-candidates.md` with five options, rejection notes, and the selected pattern. A serious title is chosen, not improvised at the last minute.

Preferred CUMCM-style title patterns:

- `基于<核心模型/方法>的<对象><评价/预测/优化>模型`
- `考虑<关键因素>的<对象><决策/优化>研究`
- `融合<方法一>与<方法二>的<问题对象>建模与分析`
- `面向<应用场景>的<指标体系/优化策略/判定模型>`
- `<问题对象>的<建模、求解与灵敏度分析>`

For the NIPT-style test, a stronger title would look more like:

```text
考虑孕妇 BMI 差异的 NIPT 检测时点优化与胎儿异常判定模型
```

Avoid:

- bare task labels;
- "complete model chain" language;
- "intelligent" or "AI-assisted" wording;
- titles that sound like a prompt summary.

## Abstract Form

The abstract must be divided into paragraphs.

Default structure:

```text
Paragraph 1: background, difficulty, and total route.
Paragraph 2: 针对问题一..., method plus result.
Paragraph 3: 针对问题二..., method plus result.
Paragraph 4: 针对问题三/四..., method plus result.
Paragraph 5: validation, model advantages, limitations, and keywords.
```

Hard style rules:

- use `针对问题一`, `针对问题二`, etc. unless the contest style clearly calls for another wording;
- bold the most important numeric or decision results with `\textbf{...}`;
- expose the answer form: ranking, plan, predicted value, group boundary, selected time, threshold, or classification result;
- fill most of page one without exceeding page one;
- do not write the abstract as one uninterrupted block;
- do not list method names without final answers.

## Background And Concept Figure

A strong paper should usually include one early concept figure or mechanism figure before heavy results.

Accepted concept-figure types:

- problem mechanism diagram;
- data-to-decision flowchart;
- risk-window diagram;
- model pipeline diagram;
- variable relationship schematic.

This does not require an image-generation model. Use TikZ, matplotlib, graphviz, or generated SVG. The figure must be schematic and must not support numeric claims.

## Human-Like Exposition

Each major section needs explanatory paragraphs, not only bullets, formulas, and tables.

Minimum style expectations:

- after every body-critical table or figure, write one interpretation paragraph;
- before a model formula, explain what real-world mechanism it represents;
- after a result, explain whether it is intuitively reasonable;
- when a result is weak, say how it limits the conclusion;
- do not leave a subsection as a heading plus one sentence.

Forbidden body phrases when they expose prompt scaffolding:

- `问题信号识别`;
- `路线选择理由`;
- `模型链概述` as a standalone section title;
- `采用...路线` repeated mechanically;
- `完整的方法链` unless the paper proves the chain.

## Figure And Table Style

Figures must be paper figures, not notebook screenshots.

Requirements:

- Chinese captions and readable axes where possible;
- no tiny heatmap labels that cannot be read in PDF;
- no English default plot titles such as `Y Concentration Distribution`;
- each multi-panel figure should have a clear Chinese caption explaining the panels;
- each figure should be traceable to a script in `artifact-ledger.md`;
- a figure that shows impossible values, such as negative biological concentration, must trigger revision rather than be used as evidence.

Tables must make decisions visible:

- result tables should include final answer columns;
- small-sample or penalty rows must not be silently included in a recommended optimum;
- use notes to explain sample limits, but do not let a note excuse an invalid recommendation.

## Appendix Code

v1.5 papers must include appendix code or a clear reason why code is not applicable.

The appendix should contain:

- core scripts by question;
- figure/table generation code pointers;
- enough code to reproduce final results;
- no giant raw dump that replaces body explanation.

## Length Target

v1.5 should aim for a 25-40 page serious draft when the problem supports it. Local and official excellent-paper samples often exceed 30 pages because each subquestion carries a full evidence loop.

Length must come from:

- fuller abstract;
- concept figure;
- data-quality analysis;
- route comparison;
- model derivation;
- result interpretation;
- validation/sensitivity;
- appendix code.

Do not add pages through copied background, empty section headings, or oversized appendix output.
