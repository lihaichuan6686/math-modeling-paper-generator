# v1.5 Hard Gates

Purpose: make the next paper fail loudly when it has the same weaknesses as the v1.4 test output.

These are hard gates. A compiled PDF is not enough.

## Gate 1: Title Gate

Fail if:

- `runs/current/title-candidates.md` is missing;
- the title is only the problem statement shortened;
- the title sounds like a task label rather than a paper title;
- the title lacks method, object, or decision focus.

Pass when the title follows an award-paper pattern such as:

```text
考虑<关键因素>的<对象><优化/评价/预测/判定>模型
```

## Gate 2: Abstract Gate

Fail if:

- the abstract is one unbroken block;
- page one has large whitespace after keywords;
- no `针对问题一/二/三` style structure appears;
- key numeric or decision results are not bolded;
- fewer than three concrete result expressions are highlighted when the problem has at least three output questions;
- any major subquestion has method without result.

Pass only when the abstract is paragraph-structured, result-bearing, and visually close to a full page.

## Gate 3: Concept Figure Gate

Fail if no early concept/mechanism/model-flow figure exists and no explicit reason is recorded.

The concept figure should appear in the problem analysis or model overview zone, before dense result figures.

## Gate 4: Prompt-Language Leak Gate

Fail if body section titles or repeated phrases expose internal planning vocabulary:

- `问题信号识别`;
- `路线选择理由`;
- `模型链概述`;
- `支撑层/验证层` when used as prompt scaffolding rather than a natural paper table;
- generic checklist language without domain discussion.

Rewrite these as natural paper sections.

## Gate 5: Figure Readability Gate

Fail if:

- axes or legends are unreadable in the PDF;
- default English plot titles remain;
- heatmap labels are too small to inspect;
- a plot shows impossible values and is still used as evidence;
- a figure caption only names the plot without interpreting its role.

## Gate 6: Result Sanity Gate

Fail if any recommended result violates obvious reasonableness:

- biological concentration is negative in a fitted curve used for decision making;
- a recommended optimal group contains sample-size penalty rows as if they were normal evidence;
- a low-explanation model is described as strong without qualification;
- classification results ignore imbalance or unstable cross-validation;
- the final recommendation contradicts the result table.

The run must either repair the model or explicitly downgrade the conclusion.

## Gate 6B: Method Route Depth Gate

Fail if:

- `runs/current/method-depth-plan.md` is missing;
- a central subquestion is only `method -> result`;
- the method-depth plan does not name a result artifact and validation artifact for each major subquestion;
- the final recommendation has no feasibility, sensitivity, comparison, or sanity-check evidence;
- a complex method is named but its role in the route is unclear.

Use `docs/v1.5-method-route-contract.md` and `knowledge/algorithms/method-depth-ladder.md` as the standard.

The executable PDF check also inspects this gate when `-Run .\runs\current` is provided.

## Gate 7: Data Trap Gate

`data-inventory.md` must contain a `Data Traps` section.

Fail if:

- suspicious labels, missing columns, duplicated rows, repeated measurements, garbled extraction, or inconsistent fields are not recorded;
- the paper uses a column as ground truth without checking its meaning;
- a recorded data trap does not appear in the review.

## Gate 8: Plan-To-Paper Gate

Planning files must affect the paper.

Fail if:

- `section-budget.md` says the abstract should fill page one but the PDF does not;
- `figure-plan.md` lists a concept figure but none appears;
- `artifact-ledger.md` does not trace final tables/figures to scripts;
- `method-depth-plan.md` names validation or comparison that is absent from the body.

## Gate 9: Appendix Code Gate

Fail if:

- there is no appendix code or script index;
- body-critical figures/tables cannot be traced to code;
- appendix code is a raw dump unrelated to the paper's numbered results.

## Gate 10: PDF Density Gate

Fail if:

- page one has obvious blank lower half;
- any normal body page has a single small table/figure and no explanatory paragraph;
- consecutive pages are mostly plots with minimal interpretation;
- the paper reaches length through blank space, oversized plots, or appendix inflation.

## Gate 11: LaTeX Heading Safety Gate

Fail if any `\section`, `\subsection`, `\subsubsection`, `\paragraph`, or `\subparagraph` title contains an ASCII hyphen (`-`).

Reason: headings are written to `.toc`, `.out`, and PDF bookmark metadata. In Chinese XeLaTeX documents with `hyperref`, mixed heading tokens such as `Z-score基线` can trigger runaway bookmark arguments or silent downstream truncation even when the compiler still emits a PDF.

Repair:

- use `Zscore基线判定法`, `Z score基线判定法`, or a Chinese phrase such as `标准分数基线判定法`;
- keep hyphenated English terms in body text only, not in heading commands;
- rerun the PDF/source check after repair.

## Gate 12: Section Density Gate

Fail if a normal body section is only a skeleton and does not meet its first-draft minimum density.

Minimum source-level targets:

| Section family | Minimum paragraphs | Minimum formulas | Minimum figure/table evidence |
|---|---:|---:|---:|
| Problem restatement / analysis | 3 | 0 | 1 |
| Data preprocessing | 3 | 1 | 1 |
| Model construction | 3 | 2 | 1 |
| Solution / computation | 3 | 1 | 1 |
| Results analysis | 3 | 0 | 2 |
| Validation / sensitivity | 3 | 1 | 1 |

These are not page-padding targets. They force the first draft to contain real explanatory prose, mathematical structure, and visible evidence before the paper is compiled. If a section genuinely needs fewer formulas, record the reason in the review and compensate with stronger interpretation and artifact evidence.

Executable support:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\check-v1.5-pdf.ps1 -Pdf .\paper\main.pdf -Run .\runs\current -Tex .\paper\main.tex -Review .\reviews\review-current.md
```

This writes `reviews/pdf-v15-check.md`. Treat any `FAIL` item as a failed hard gate. The script screens PDF visibility, run files, LaTeX source, and review verdict completion; it does not replace human review.

## Required Review Language

The final review must include a `v1.5 Hard Gate Verdict` table:

| Gate | Pass/Fail | Evidence | Repair |
|---|---|---|---|

Any failed gate means the paper is not ready for user handoff.
