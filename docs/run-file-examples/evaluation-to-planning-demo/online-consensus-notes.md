# Online Consensus Notes

Run family: evaluation-to-planning-demo

This is an example shape. It demonstrates safe public-signal handling for an evaluation-to-planning route. Replace placeholder sources and queries during a live run.

## Search Scope

- General experience searched first:
  - `数学建模 评价规划 论文 写法`
  - `数学建模 指标体系 权重 敏感性分析`
  - `数学建模 规划模型 结果表`
- Exact-problem discussion would be searched only after `route-decision.md` and `model-plan.md` exist.
- Login-only pages, paid answer packages, and private discussion groups are not used.

## Source Table

| Source | Platform | Quality | Signal | Used? |
|---|---|---|---|---|
| University training note on evaluation models | university/public note | high | evaluation route should state indicator source, direction, weighting method, and validation | yes |
| Long public blog explaining evaluation-to-decision workflow | blog/CSDN-style public post | medium | many weak papers stop at ranking and do not turn the ranking into an executable plan | yes |
| Short social post with final ranking screenshot | Xiaohongshu/search snippet | low | shows that teams compare rank ranges, but gives no assumptions or data processing | weak signal only |
| Paid package claiming final answers | unknown/course seller | reject | answer dump and active-contest risk | no |

## Common Interpretations

- Stronger routes treat the task as `evaluation -> planning decision`, not as a pure scoring/ranking task.
- Public discussion often warns that indicator direction, normalization, and weight sensitivity must be visible.
- The decision object should be a plan, allocation, intervention, or recommendation table, not just a score list.

## Common Methods

- Baseline: normalize indicators, assign weights, calculate comprehensive score, rank objects.
- Stronger route: indicator source audit -> weighting comparison -> score/rank -> planning model -> feasibility/scenario validation.
- Risky decoration: stacking entropy weight, AHP, TOPSIS, PCA, clustering, and optimization without explaining what each layer contributes.

## Rough Result Ranges

- Public snippets sometimes show similar top-ranked objects, but no reliable numeric consensus is available.
- Treat public ranking screenshots as sanity prompts only. Do not target or copy their final order.

## Warnings And Traps

- Do not let evaluation score be the final answer if the problem asks for an action plan.
- Do not hide the final plan in appendix tables.
- Do not use a weight method without explaining why it fits data reliability and subjective criteria.
- Do not cite public answer dumps.

## Route Reflection

- The evaluation-to-planning route remains appropriate because it produces both an interpretable score layer and an executable planning decision.
- The run should strengthen the bridge from rank to plan: objective, decision variables, constraints, and feasibility table must appear in the body.
- Literature support belongs in `literature-notes.md`; this note only records public interpretation/trap signals.

## What Changed

| Signal type | Run file changed | Change made | Reason |
|---|---|---|---|
| interpretation | `route-decision.md` | State that final output is a planning decision, not only a ranking | Avoid pure-evaluation fake completion |
| trap | `model-plan.md` | Add explicit rank-to-plan bridge with objective and constraints | Public signals warn that ranking alone is thin |
| validation | `verification-plan.md` | Add weight sensitivity and scenario feasibility checks | Improve credibility of plan recommendation |
| artifact | `figure-plan.md` | Add rank-to-plan flow diagram and scenario comparison table | Make decision chain visible |
| writing | `writing-style-plan.md` | Warn against presenting the paper as a method catalogue | Avoid decorative algorithm stacking |

## What Was Rejected

- Rejected final ranking screenshots because they provide no assumptions, indicator processing, or validation.
- Rejected paid answer packages and answer-only posts.
- Rejected method popularity as proof; a method is used only when it changes evidence or explanation.

## Remaining Uncertainty

- Public sources do not settle the exact indicator set or final ranking.
- Human review should check whether the chosen indicators match the problem statement and available data.
- If exact-problem public discussion is searched later, it must be recorded after the initial route exists and must not overwrite model logic by popularity.

## v1.4 Search Order Check

- General contest-circle experience searched before exact problem discussion: yes.
- Exact-problem signals used only after initial route-decision: planned.
- Popularity was not treated as proof: yes.
