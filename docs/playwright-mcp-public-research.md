# Playwright MCP Public Research Entry

Purpose: tell Claude Code how to gather public contest-circle signals with Playwright MCP instead of custom platform crawlers.

This replaces the platform-specific Python crawler approach.
Use Playwright MCP as an interactive browser when public online information is needed.

## Core Rule

Browse like a human reviewer.

Do:

- use public search pages and public web pages;
- open visible results with Playwright MCP;
- read page title, visible text, captions, snippets, and accessible comments when normally visible;
- record source URL, platform, access status, signal type, and uncertainty;
- stop when a page requires login, captcha, payment, private group access, or unusual bypass steps.

Do not:

- bypass login walls;
- use cookies, hidden APIs, ZSE/internal endpoints, or anti-crawling workarounds;
- copy exact answers or solution text;
- treat screenshots, popularity, or short posts as proof;
- keep browsing forever when public sources are sparse.

## When To Use

Use after:

- `problem-profile.md` or `problem-analysis.md`;
- `route-decision.md`;
- `model-plan.md`.

Use before:

- final paper writing;
- final abstract writing;
- final conclusion writing.

## Where To Browse

Use Playwright MCP to search and inspect public pages from:

- general search engines;
- CSDN/blog pages;
- Bilibili public video pages and public descriptions;
- Zhihu public pages or search-result snippets;
- Xiaohongshu public search-result snippets or public pages when normally visible;
- university training pages;
- official contest pages;
- public GitHub/Gitee repos only for reproducibility habits.

## Search Order

Search general experience first:

```text
数学建模 国赛 经验
数学建模 国赛 论文写作 摘要
数学建模 国赛 常见错误 避坑
数学建模 获奖论文 结构
```

Then search domain or problem-specific terms after the route exists:

```text
<year> 国赛 <problem_id>题 思路
<year> 国赛 <problem_id>题 结果
<domain keywords> 数学建模 方法
<domain keywords> 国赛 建模
```

## Required Output

Write or update:

```text
runs/current/online-consensus-notes.md
```

Use this structure:

```text
# Online Consensus Notes

## Playwright Browsing Scope

## Source Table

| Source | Platform | Access | Quality | Signal | Used? |
|---|---|---|---|---|---|

## Common Interpretations

## Common Methods

## Rough Result Ranges

## Warnings And Traps

## Route Reflection

## What Changed

## What Was Rejected

## Remaining Uncertainty
```

## Source Quality

Use:

- `high`: official pages, university training notes, detailed public posts with reasoning and data;
- `medium`: public videos/posts with clear reasoning but incomplete evidence;
- `low`: short snippets, unsupported screenshots, result-only comments, vague experience posts;
- `reject`: paid packages, leaked/private materials, login-only content, answer dumps, copied text.

## Conversion Rule

Every useful signal must change something concrete:

| Signal type | Allowed conversion |
|---|---|
| interpretation | update `problem-analysis.md` or `route-decision.md` |
| trap | update `verification-plan.md` or review warnings |
| method | compare in `model-candidates.md`; do not auto-adopt |
| result range | add sanity check to `verification-plan.md`; mark uncertainty |
| missing artifact | update `figure-plan.md` and `artifact-ledger.md` |
| taboo wording | update `writing-style-plan.md` |

If a public signal changes nothing, record why it was rejected or discounted.

## Stop Conditions

Stop browsing when:

- four to six useful public sources have been recorded;
- three platforms have been attempted;
- public sources are sparse and the note records that limitation;
- sources start repeating the same weak answer-only content;
- access requires login, captcha, payment, private group material, or non-public workarounds.

## Relationship To Prompt 11

`prompts/13_platform_research.md` is the browsing phase.
`prompts/11_online_consensus_check.md` is the reflection phase.

Prompt 13 may create the first version of `online-consensus-notes.md`.
Prompt 11 should review the same file, preserve useful source rows, add route reflection, and convert signals into run-file changes.
