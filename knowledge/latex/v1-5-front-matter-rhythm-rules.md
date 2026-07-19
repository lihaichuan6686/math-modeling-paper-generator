# v1.5 Front-Matter Rhythm Rules

Purpose: make the first two pages look like a serious CUMCM team paper rather than an AI-generated report.

These rules are distilled from the local awarded LaTeX sample, existing official-paper deep reads, and the visible page-count scan of the 2021-2023 excellent-paper PDF folders.

## Evidence Behind The Rules

Observed anchors already in the repository:

- the local awarded sample has 38 pages, a nearly full first-page abstract, early object figure, five subquestion analysis loops, support-file inventory, and code appendix;
- 2023 excellent-paper samples show page counts of 27, 31, 41, 50, and 50 pages;
- 2022 excellent-paper samples scanned by page count mostly fall between 22 and 57 pages;
- prior v1.4 user test failed at the first glance: task-label title, thin one-block abstract, no early concept figure, prompt-language leakage.

Generator implication:

```text
v1.5 should not treat 20 compiled pages as success. The first two pages must already show route, result density, and human-team structure.
```

## Title Generation Protocol

Before writing `paper/main.tex`, create `runs/current/title-candidates.md`.

It must contain:

1. five candidate titles;
2. one-line rejection reason for weak candidates;
3. the selected title;
4. the title pattern used.

Preferred patterns:

- `基于<核心机制/模型>的<对象><预测/评价/优化/判定>模型`;
- `考虑<关键因素/约束>的<对象><决策/优化>研究`;
- `融合<方法一>与<方法二>的<对象><建模与分析>`;
- `面向<应用场景>的<策略/指标体系/判定模型>`;
- `<对象>的<建模、求解与灵敏度分析>`.

Reject titles when they:

- copy the task name or problem statement;
- use `方案研究`, `问题分析`, `综合模型` with no modeled object;
- contain AI/process words such as `智能`, `自动生成`, `完整链路`;
- sound like a section heading rather than a paper title;
- hide the final decision object.

## First Page Rhythm

The first page should contain:

```text
title
-> dense paragraph abstract
-> keywords
```

It should not contain:

- a half-blank lower page;
- a one-block abstract;
- only background and method names;
- generic claims such as `模型具有较好的科学性和有效性`.

Abstract paragraph target:

1. overall task and modeling route;
2. `针对问题一` method plus concrete result;
3. `针对问题二` method plus concrete result;
4. `针对问题三/四` extension plus concrete result;
5. validation, limitation, and final recommendation;
6. keywords.

At least three concrete result expressions should be bolded with `\textbf{...}` when the problem supports numerical or decision outputs.

## Second Page Rhythm

The second page should quickly make the modeled object visible.

Preferred content:

- short problem restatement;
- answer-form table or subquestion map;
- early concept/mechanism/model-flow/object figure;
- route paragraph explaining why the decomposition is natural.

Do not spend page two only paraphrasing the statement. A reviewer should know what object, data relation, geometry, network, or decision pipeline is being modeled before heavy formulas begin.

## Section Rhythm After The Front Matter

For each numbered subquestion, repeat a complete evidence loop:

```text
task interpretation
-> variable/object definition
-> model or algorithm
-> generated result figure/table
-> interpretation
-> sanity check or validation
-> bridge to the next question
```

This rhythm is why excellent papers become 25-50 pages without feeling padded.

## Review Rules

Fail the v1.5 run if:

- `runs/current/title-candidates.md` is missing;
- fewer than five real candidate titles are filled;
- the selected title is empty or still a placeholder;
- the selected title has no modeled object and no modeling action;
- page one extracted text is too thin or visually half blank;
- no early object/concept figure appears by the problem-analysis section;
- the abstract lacks problem-by-problem closure;
- the body uses prompt-planning section names.

Best use:

- read before `knowledge/latex/v1-5-award-paper-style-rules.md`;
- use together with `paper/templates/cumcm_v15_main.tex`;
- enforce through `knowledge/quality/v1-5-hard-gates.md` and `scripts/check-v1.5-pdf.ps1`.
