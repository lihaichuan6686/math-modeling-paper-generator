# Online Consensus Example Template

Purpose: give Claude Code a concrete example shape for `runs/current/online-consensus-notes.md`.

This is a template, not a filled real run.

## Example

```text
# Online Consensus Notes

Run: current
Problem: <contest/year/problem>

## Search Scope

- searched Bilibili for: <problem keywords> + 数学建模 + 思路
- searched Xiaohongshu for: <problem keywords> + 国赛 + 经验
- searched Zhihu/CSDN/blogs for: <problem keywords> + 结果 + 论文
- searched GitHub/Gitee for: <problem keywords> + code / paper

Blocked or low-access platforms:

- Xiaohongshu results were sparse from public search; no login-only scraping was attempted.

## Source Table

| Source | Platform | Quality | Signal | Used? |
|---|---|---|---|---|
| university training note on similar route | university/public PDF | high | validation should compare baseline and improved model | yes |
| Bilibili explanation video | Bilibili | medium | many teams treat Q2 as forecast-to-decision, not pure forecast | yes |
| short post with only final number | Xiaohongshu | low | rough result range only | weak signal |
| paid answer dump | unknown | reject | answer-only material | no |

## Common Interpretations

- Most serious sources read the task as <decision object>, not just <intermediate calculation>.
- A common mistake is <misinterpretation>.

## Common Methods

- Baseline methods: <method family>.
- Stronger routes: <method family with validation>.
- Decorative but risky routes: <method family, if unsupported>.

## Rough Result Ranges

- Reported range for <key output>: about <range>, from low/medium-quality public sources.
- Treat as sanity check only.

## Warnings And Traps

- Do not ignore <constraint>.
- Do not hide <required final answer>.
- Do not treat <metric> as the only result.

## Route Reflection

- Current route still fits because ...
- Current route may need repair because ...

## What Changed

- Added <validation/comparison/figure/table>.
- Revised <route-decision/model-plan> to address <trap>.
- Updated <figure-plan/artifact-ledger/writing-style-plan> when the signal affected evidence or prose.

## What Was Rejected

- Rejected <source/method> because it was answer-only, unsupported, or copied.

## Remaining Uncertainty

- Public discussion did not settle <issue>.
- Human review should check <item>.
```

## Use Rule

The note should be short enough to read during a contest workflow.

It should not become a scraped-content dump.
