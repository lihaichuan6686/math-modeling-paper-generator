# Prompt 11: Online Consensus Check

Use this prompt after:

- `problem-profile.md`
- `route-decision.md`
- `model-plan.md`

Use it before writing the final paper.

## Purpose

Check public contest-circle discussion for sanity signals, common traps, and rough result expectations.

Do not copy answers.

## Required Reading

Read:

- `docs/online-consensus-check-protocol.md`
- `docs/online-consensus-example-template.md` if you need a concrete note shape
- `docs/online-consensus-weak-strong-examples.md`
- `knowledge/community/source-quality-rubric.md`
- `knowledge/community/public-community-source-playbook.md`
- `knowledge/community/math-modeling-soft-rules.md`
- `knowledge/community/award-paper-section-rhythm.md`
- current run's `problem-profile.md`
- current run's `route-decision.md`
- current run's `model-plan.md`

## Search Plan

Before searching, read:

- `docs/playwright-mcp-public-research.md` — how to browse public pages with Playwright MCP and record access limits.

Search public accessible sources for:

```text
数学建模 国赛 经验
数学建模 论文写作 摘要
数学建模 获奖论文 结构
数学建模 常见错误
<contest/year/problem> + 题号 + 经验
<contest/year/problem> + 思路
<contest/year/problem> + 结果
<contest/year/problem> + 论文
<key domain words> + 数学建模
<key domain words> + 国赛 + 建模
```

**Minimum query requirement**: search at least 4 distinct queries across at least 3 platforms.

Useful public sources:

| Platform | Accessibility | Strategy |
|---|---|---|
| CSDN/blogs | Variable | Browse public pages with Playwright MCP |
| Bilibili | Variable | Browse public video pages, titles, descriptions, and visible comments when normally accessible |
| Zhihu | Partial | Use public pages or search snippets; do not use hidden APIs or login-wall workarounds |
| Xiaohongshu | Low/partial | Use public snippets or normally visible pages only; treat as weak signal unless reasoning is visible |
| public WeChat articles | Variable | Use search-discovered public pages |
| GitHub/Gitee | High — public repos | Direct inspection |

If a platform blocks access or requires login, captcha, payment, private-group access, or app-only access, record it as inaccessible and move on.

For structured public browsing with Playwright MCP, use `prompts/13_platform_research.md` before this prompt.
If `prompts/13_platform_research.md` has already produced `online-consensus-notes.md`, do not overwrite it from scratch. Review the existing platform records, preserve useful source rows, add missing reflection/conversion/rejection sections, and mark weak or inaccessible signals clearly.

## Output File

Create or update:

```text
runs/current/online-consensus-notes.md
```

Use this structure:

```text
# Online Consensus Notes

## Search Scope

## Source Table

| Source | Platform | Quality | Signal | Used? |
|---|---|---|---|---|

## Common Interpretations

## Common Methods

## Rough Result Ranges

## Warnings And Traps

## Route Reflection

## What Changed

## What Was Rejected

## Remaining Uncertainty
```

## Reflection Rule

After the search, revise only if there is a reason:

- route mismatch;
- missing validation;
- implausible result range;
- missing figure/table;
- misunderstood task.

Do not revise only because one post uses a fancier method.

## Conversion Rule

After the search, update run files only through concrete signals:

- interpretation signal -> `problem-analysis.md` or `route-decision.md`;
- trap signal -> `route-decision.md`, `verification-plan.md`, or review warning;
- missing artifact signal -> `figure-plan.md` and `artifact-ledger.md`;
- validation signal -> `verification-plan.md`;
- writing/taboo signal -> `writing-style-plan.md`;
- result-range signal -> sanity check in `verification-plan.md`, not a copied target.

If no run file changes, explain why the route remained stable.

## Minimum Quality Rule

The note must include at least:

- searched queries or platform attempts;
- source quality labels;
- one explicit route reflection;
- one rejected or discounted signal;
- one remaining uncertainty.

If public sources are sparse, write a skip/limitation note rather than inventing consensus.
