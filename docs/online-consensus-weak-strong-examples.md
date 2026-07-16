# Online Consensus Weak And Strong Examples

Purpose: show the difference between a useful online-consensus note and a useless or unsafe one.

Use this with `prompts/11_online_consensus_check.md`.

## Weak Example

```text
I searched online. People mostly use neural networks and optimization.
Some posts say the answer is around 1000.
We should use XGBoost because many people mention it.
```

Why this is weak:

- no search scope;
- no source quality labels;
- no separation between method signal and answer copying;
- no route reflection;
- no rejected signal;
- no uncertainty;
- method popularity is treated as authority.

## Strong Example

```text
## Search Scope
- Bilibili: 2023 C题 数学建模 思路, 2023 C题 结果
- Zhihu/CSDN/blogs: 蔬菜补货 定价 数学建模
- GitHub/Gitee: 2023 C题 code paper
- Xiaohongshu: public search sparse; no login-only scraping attempted

## Source Table

| Source | Platform | Quality | Signal | Used? |
|---|---|---|---|---|
| university training note on replenishment models | university PDF | high | forecast should feed an executable replenishment/price decision | yes |
| long blog solution with code and caveats | CSDN/blog | medium | many routes split demand prediction and pricing optimization | yes |
| short post with final profit number | Xiaohongshu/search snippet | low | rough sanity range only, not enough context | weak signal |
| paid solution package | unknown | reject | answer dump | no |

## Common Interpretations

- Serious sources treat the task as forecast-to-decision, not pure forecasting.
- The decision object is replenishment/price policy, not just next-day sales.

## Common Methods

- Baseline: regression/ARIMA-style forecast plus simple pricing rule.
- Stronger: demand forecast, category clustering, price elasticity, constrained optimization, scenario validation.
- Risky decoration: black-box model without explainable decision link.

## Warnings And Traps

- Do not stop after a demand forecast.
- Make final replenishment and price tables visible in the body.
- Validate decision sensitivity, not only prediction error.

## Route Reflection

- Our route already has forecast plus optimization, so the main direction is stable.
- We need to add a decision sensitivity table because public solutions often compare price/profit scenarios.

## What Changed

- Added a scenario comparison figure to `figure-plan.md`.
- Added sensitivity check to `verification-plan.md`.
- Marked the final replenishment and price tables as body-critical in `artifact-ledger.md`.
- Added a warning to `writing-style-plan.md` not to write the paper as a pure forecasting paper.

## What Was Rejected

- Rejected exact final profit numbers from answer-only posts because no assumptions or data processing were shown.

## Remaining Uncertainty

- Public sources disagree on exact aggregation level. Human review should check whether category-level and item-level claims are separated.
```

Why this is strong:

- records search attempts;
- classifies source quality;
- converts online material into route checks, not copied answers;
- updates the specific run files that must change;
- adds or rejects changes for reasons;
- keeps uncertainty visible.

## Review Rule

Fail the online-consensus note if it:

- copies final answers or full solution text;
- uses popularity as proof;
- has no source-quality labels;
- has no route reflection;
- records no rejected or discounted source;
- invents consensus when public sources are sparse.
