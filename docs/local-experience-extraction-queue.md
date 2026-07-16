# Local Experience Extraction Queue

Purpose: make the remaining local modeling-experience materials absorbable in a repeatable way.

Source folder:

```text
D:\2-各比赛Word模板及LaTeX模板\9.数学建模经验分享（36篇）
```

This queue focuses on older `.doc` and `.ppt` files that need separate extraction. The goal is not to copy source text. The goal is to convert stable experience into reusable rules, prompts, templates, and review checks.

## Extraction Rule

For each source file, produce at least one of:

- a community soft rule;
- a paper-structure or section-duty rule;
- a route/method selection rule;
- a figure/table/evidence rule;
- a run scaffold field;
- a quality-review question;
- a roadmap item when the material is useful but not yet operational.

Do not count a file as absorbed if it only produced a note saying it exists.

## Safe Extraction Protocol

1. Copy the source temporarily to an ASCII-named file under `tmp/`.
2. Extract a small readable sample first. For old binary `.doc` and `.ppt` files, use `scripts/probe-binary-office-text.py` on the temporary ASCII directory.
3. Record whether the extraction is readable, partial, garbled, or blocked.
4. Convert only durable rules into `knowledge/`, `docs/`, `prompts/`, or scaffold templates.
5. Delete temporary copied source files before finishing the work turn.
6. Update `knowledge/community/local-experience-absorption-log.md`.

If a file is old binary Word or PowerPoint and cannot be read reliably, do not invent its content. Mark it as extraction-blocked and revisit with a better converter or manual sampling.

## Priority 1: Writing And Contest Workflow

These files are most likely to improve v1.4 paper feel directly.

| Source file | Format | Expected signal | Target output |
|---|---|---|---|
| `全国大学生数学建模竞赛论文格式规范 (2).doc` | doc | format, title, abstract, references, appendix conventions | `knowledge/latex/v1-4-paper-composition-rules.md`, `knowledge/community/section-duty-soft-rules.md` |
| `研读数学建模优秀论文心得体会.doc` | doc | how excellent-paper readers judge section duties and weaknesses | `knowledge/community/paper-polish-and-feel.md`, `knowledge/quality/v1-4-human-feel-review-gate.md` |
| `数学建模竞赛+自学指导建议.doc` | doc | preparation rhythm, learning order, practical contest tactics | `knowledge/community/contest-workflow-and-team-execution.md`, `docs/run-start-checklist.md` |
| `大学生数学建模竞赛活动的一些问题.ppt` | ppt | competition organization, common preparation problems, team execution | `knowledge/community/contest-workflow-and-team-execution.md` |
| `我的学科竞赛之路.ppt` | ppt | contest learning path, motivation, preparation habits | `knowledge/community/math-modeling-soft-rules.md`, roadmap notes |

## Priority 2: Problem Families And Method Routing

These files should improve route selection without overfitting one rare topic.

| Source file | Format | Expected signal | Target output |
|---|---|---|---|
| `历年全国数学建模试题及解法归纳.doc` | doc | historical problem families, method families, common routes | `knowledge/cumcm/national-problem-family-methodology-matrix.md`, `knowledge/algorithms/route-selection-protocol.md` |
| `历年数学建模赛题题目.doc` | doc | task-family coverage and recurring answer forms | `knowledge/cumcm/problem-understanding-framework.md`, `knowledge/cumcm/national-problem-family-methodology-matrix.md` |
| `数学建模知识及常用方法P54.doc` | doc | common algorithms and when they are used | `knowledge/algorithms/method-family-index.md`, `knowledge/algorithms/route-method-matrix.md` |
| `数学建模入门基本知识.doc` | doc | beginner-friendly route taxonomy and workflow | `knowledge/algorithms/route-selection-protocol.md`, `knowledge/community/math-modeling-soft-rules.md` |
| `结构主义建模.ppt` | ppt | structural modeling ideas and abstraction pattern | `knowledge/cumcm/problem-understanding-framework.md` |

## Priority 3: Case-Based Paper Feel

These files should teach how a real case is narrated, not just what algorithm is used.

| Source file | Format | Expected signal | Target output |
|---|---|---|---|
| `全国大学生数学建模竞赛2009年D题-讲解-清华大学-姜启源.ppt` | ppt | expert case explanation, problem abstraction, narrative order | `knowledge/cumcm/route-example-matrix.md`, `knowledge/community/paper-polish-and-feel.md` |
| `数学建模案例分析-2008年B题“高等教育学费标准探讨”.ppt` | ppt | evaluation/planning case structure, result explanation | route examples, section-writing examples |
| `数学建模竞赛讲座(清华大学姜启源).ppt` | ppt | classic modeling process and contest expectations | `knowledge/community/math-modeling-soft-rules.md`, `knowledge/cumcm/problem-understanding-framework.md` |
| `数学模型与数学建模简介-校内竞赛讲座-郑洲顺.ppt` | ppt | introductory modeling workflow and examples | `knowledge/community/contest-workflow-and-team-execution.md` |
| `模型与数学建模.ppt` | ppt | broad modeling concepts and abstraction | `knowledge/cumcm/problem-understanding-framework.md` |
| `应用数学研究中的模型化方法.ppt` | ppt | research-style modeling method | `knowledge/algorithms/route-selection-protocol.md` |

## Priority 4: Tools, Code, And Selection

These are useful but should not dominate v1.4 paper-feel work.

| Source file | Format | Expected signal | Target output |
|---|---|---|---|
| `数学建模中常用的30个MATLAB程序和函数.doc` | doc | common computation snippets and tool roles | `docs/environment-setup.md`, algorithm/tool notes |
| `数学建模队员选拔_MATLAB拟合.doc` | doc | fitting workflow, programming expectations | route/tool notes, validation examples |
| `全国数学建模大赛简介.doc` | doc | contest overview and official-ish framing | responsible-use and contest overview notes |
| `初探大学生数学建模竞赛的深入开展.doc` | doc | large educational discussion; likely low operational density | roadmap only unless concrete rules appear |
| `数学建模与应用创新能力培养.ppt` | ppt | innovation ability and education framing | innovation soft rules if concrete |

## Completion Markers

For each extracted file, record:

| Field | Meaning |
|---|---|
| `status` | unread, sampled, absorbed, partial, blocked |
| `readability` | clean, partial, garbled, image-only, unsupported |
| `signals` | 2-5 reusable ideas found |
| `converted_to` | exact repository files changed |
| `next_action` | continue, revisit with converter, or no further action |

Record current attempts in `docs/local-experience-extraction-status.md`.

Probe command shape:

```powershell
python .\scripts\probe-binary-office-text.py .\tmp\local_experience_probe .\tmp\local_experience_probe\probe.csv
```

## Current Next Batch

Recommended next batch:

1. `全国大学生数学建模竞赛论文格式规范 (2).doc`
2. `研读数学建模优秀论文心得体会.doc`
3. `历年全国数学建模试题及解法归纳.doc`
4. `大学生数学建模竞赛活动的一些问题.ppt`

This batch balances paper format, excellent-paper feel, route taxonomy, and team/workflow soft rules.

## PDF-First Continuation Batch

When old `.doc` and `.ppt` extraction is blocked, continue with readable PDFs before returning to binary Office files.

Recommended PDF continuation:

1. `数学建模个人经验谈.pdf` only if a better converter/OCR path is available;
2. `数学中国—美赛经验总结.pdf` for time allocation, tool preparation, and team-role details;
3. `数学中国美赛培训之经验%28整理版%29.pdf` for additional first-phase reading and practical-route signals;
4. `全国大学生数学建模竞赛作用浅析.pdf` only for contest-purpose and judging-surface confirmation;
5. MCM-specific format files only when the extracted rule is generic and does not conflict with CUMCM layout.

Promotion rule:

- clean PDF extraction plus reusable signal can become `absorbed`;
- partial extraction can become `sampled` or `partial`;
- garbled extraction cannot become a stable rule without corroboration from another readable source.
