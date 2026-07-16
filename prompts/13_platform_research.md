# Prompt 13: Playwright MCP Public Research

Use this prompt after:

- `problem-profile.md` or `problem-analysis.md`;
- `route-decision.md`;
- `model-plan.md`.

Use it before final paper writing and before `prompts/11_online_consensus_check.md`.

This prompt is the public browsing phase. Prompt 11 is the reflection and signal-absorption phase.

## Purpose

Use Playwright MCP to browse public contest-circle information like a human reviewer.
Find soft rules, common interpretations, traps, and rough sanity signals.

Do not copy answers.
Do not bypass login walls.
Do not use cookies, hidden APIs, ZSE/internal endpoints, or platform-specific crawler workarounds.

## Required Reading

Read:

- `docs/playwright-mcp-public-research.md`;
- `knowledge/community/public-community-source-playbook.md`;
- `knowledge/community/source-quality-rubric.md`;
- `docs/online-consensus-check-protocol.md`;
- `docs/community-signal-to-rule-pipeline.md`;
- active run's `problem-analysis.md`;
- active run's `route-decision.md`;
- active run's `model-plan.md`.

## Playwright MCP Workflow

1. Use Playwright MCP to open a browser/search page.
2. Search broad contest experience first:

```text
数学建模 国赛 经验
数学建模 国赛 论文写作 摘要
数学建模 国赛 常见错误 避坑
数学建模 获奖论文 结构
```

3. After the route exists, search problem/domain terms:

```text
<year> 国赛 <problem_id>题 思路
<year> 国赛 <problem_id>题 结果
<domain keywords> 数学建模 方法
<domain keywords> 国赛 建模
```

4. Open only public, normally accessible pages.
5. If a page requires login, captcha, payment, private group access, app-only access, or unusual bypass steps, record it as inaccessible and move on.
6. Read visible content, not hidden endpoints.
7. Record source, access status, quality, signal type, and whether the signal changed the run.

## Platform Notes

- CSDN/blogs: useful for implementation ideas, but code posts may be copied or weak.
- Bilibili: useful for public titles, descriptions, visible comments, and interpretation trends when normally visible.
- Zhihu: use public pages or search snippets only; do not use hidden APIs or anti-crawling workarounds.
- Xiaohongshu: use public search snippets or normally visible pages only; treat as weak signal unless reasoning is visible.
- University/official pages: usually higher trust for writing rules and contest expectations.

## Required Output

Create or update:

```text
runs/current/online-consensus-notes.md
```

If the file already exists, revise it in place. Preserve useful public-source records and add a note explaining what changed.

Use this structure:

```markdown
# Online Consensus Notes

## Playwright Browsing Scope

List every query and platform/page attempted.

## Source Table

| Source | Platform | Access | Quality | Signal | Used? |
|---|---|---|---|---|---|

Quality: high / medium / low / reject
Signal: interpretation / method / trap / result_range / validation / taboo

## Common Interpretations

## Common Methods

## Rough Result Ranges

Mark clearly: sanity check only, never target answer.

## Warnings And Traps

## Route Reflection

Does the current route still fit? What public signals support or contradict it?

## What Changed

- {file}: {change} - {reason}

## What Was Rejected

- Rejected {source/method} because ...

## Remaining Uncertainty
```

## Signal Conversion Rule

Every useful signal should be converted into a concrete run-file change:

| Signal type | Allowed conversion |
|---|---|
| interpretation | update `problem-analysis.md` or `route-decision.md` |
| trap / warning | add to `verification-plan.md` or review warnings |
| method comparison | compare against `model-candidates.md`; do not auto-adopt |
| result range | add sanity check to `verification-plan.md`; mark uncertainty |
| missing artifact | update `figure-plan.md` and `artifact-ledger.md` |
| taboo wording | update `writing-style-plan.md` |

If a public signal changes nothing in the run files, record why it was rejected or discounted.

## Quality Gate

A useful Playwright research note has:

- at least four public browsing attempts, or a clear scarcity note;
- at least three platform/source attempts when practical;
- access status for every source;
- source quality labels;
- at least one route reflection;
- at least one rejected or discounted signal;
- at least one remaining uncertainty.

A weak note has:

- only copied search results;
- no source quality labels;
- no route reflection;
- no rejected signal;
- exact answers copied into the plan;
- login-only content treated as public consensus.

## Related Prompts

- `prompts/11_online_consensus_check.md` - formal consensus reflection after this prompt.
- `prompts/flow-map.md` - full pipeline overview.
