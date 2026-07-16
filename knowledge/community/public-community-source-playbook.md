# Public Community Source Playbook

Purpose: help Claude Code turn public contest-circle material into safe, useful modeling signals.

This file is for v1.4 online-consensus checks. It does not authorize scraping, copying, or using leaked/private materials.

## Core Rule

Public community material is a mirror, not a solution source.

Use it to ask:

```text
What might we be missing?
What interpretation is common?
What trap should we check?
What validation or figure would make the paper more credible?
```

Do not use it to ask:

```text
What answer should we copy?
Which route is popular enough to skip reasoning?
How can we mimic another team's paper?
```

## Platform Signal Map

| Source type | Useful signals | Common risks | How to use |
|---|---|---|---|
| Official contest pages | rules, format, problem wording, official data | may not explain solution strategy | high-trust factual boundary |
| University training notes | writing habits, validation expectations, route families | may be generic or dated | high-trust process guidance |
| Excellent-paper analyses | section rhythm, model/result closure, figure/table use | may overfit one paper | convert into style checks |
| Bilibili videos | common interpretations, common route families, traps viewers discuss | comments can be noisy; popularity bias | medium signal; verify with route logic |
| Xiaohongshu posts | practical experience, time management, taboo phrases, visible community concerns | snippets may be short; access may require login; answer-only posts | use public accessible soft rules only |
| Zhihu answers | longer route explanations, pros/cons, veteran reflection | can be opinionated or outdated | medium signal if reasoning is shown |
| CSDN/blog posts | code route, reproducibility hints, common implementation failures | code may be copied, wrong, or answer-dump-like | use for implementation traps, not text copying |
| GitHub/Gitee repos | file structure, code artifacts, reproducibility patterns | license/provenance uncertainty; route may be weak | inspect structure and validation habits |
| WeChat public articles surfaced by search | training notes, experience summaries | hard to revisit; promotional content | record title/source and treat as medium/low unless detailed |

## Signal Types To Extract

Extract only these reusable signals:

- interpretation: how people define the decision object and subquestion boundaries;
- route family: what model families are repeatedly considered;
- trap: common mistake, ignored constraint, or misunderstood term;
- validation: what comparison, sensitivity, or baseline seems expected;
- artifact: what figure/table makes the answer easier to judge;
- wording taboo: phrases or claims that sound naive or overconfident;
- rough range: approximate result range used only for sanity checking.

After extraction, convert each useful signal through `docs/community-signal-to-rule-pipeline.md`.
The signal is not considered absorbed until it changes a run file, prompt, stable knowledge note, or review gate.

## Signals To Reject

Reject or heavily discount:

- exact final answer without assumptions;
- screenshot-only answer dumps;
- paid solution packages;
- private group material;
- posts offering disguised authorship or rule violations;
- "everyone uses X" with no task-fit reasoning;
- method-name lists with no variables, data, result, or validation.

## Public Search Discipline

Use a small set of targeted queries first:

```text
<contest year/problem> + 题号 + 思路
<contest year/problem> + 数学建模 + 经验
<key domain words> + 国赛 + 建模
<key domain words> + 结果 + 论文
<key domain words> + 常见错误
<platform> + 数学建模 + 国赛 + 经验
<platform> + 数学建模 + 论文写作 + 摘要
```

For Bilibili and Xiaohongshu, prefer search-engine-visible public pages and public video/post metadata.
Do not use login walls, private comments, paid course groups, or screenshots of suspected leaked answers.

If sources are sparse:

- record that public sources were sparse;
- search broader domain keywords;
- use local knowledge and official/problem data;
- do not invent consensus.

If sources conflict:

- prefer detailed reasoning over popularity;
- prefer official/university/material with traceable data;
- record disagreement as uncertainty;
- make route changes only when the problem logic supports them.

## Route Reflection Pattern

After reading public signals, write:

```text
Our route remains stable because ...
Our route needs one repair because ...
We reject ... because ...
Remaining uncertainty is ...
```

The reflection should change:

- route-decision;
- model-plan;
- verification-plan;
- figure-plan;
- section-budget;

only when there is a concrete reason.

## Quality Gate

A useful online-consensus note has:

- searched queries or platform attempts;
- source-quality labels;
- at least one common interpretation or trap;
- at least one route reflection;
- at least one rejected or discounted signal;
- remaining uncertainty.

A weak note has:

- no sources;
- no quality labels;
- no rejected signal;
- no route reflection;
- exact answers copied into the plan;
- "popular method" used as proof.

## Public Platform Workflow

Use this sequence when public pages are available:

1. Search broad platform-level experience first, such as "数学建模 国赛 经验", before searching exact problem answers.
2. Search exact problem terms only after the initial route-decision exists.
3. Separate "contest soft rules" from "problem-specific consensus".
4. Convert soft rules into writing or review requirements.
5. Convert problem-specific signals only into interpretation checks, result-range sanity checks, validation ideas, or figure/table ideas.
6. Record at least one reason not to follow a public signal when the signal is shallow, unsafe, or unsupported.

Do not let platform popularity override the paper's own model logic.

## Promotion Discipline

Use maturity levels before hardening a rule:

- `observed`: one post, video, paper, or note mentions it; keep as a log signal.
- `repeated`: several independent sources or papers show it; allow it to guide run files.
- `stable`: local excellent papers and public experience agree; add it to prompts or quality gates.
- `tested`: a user-side Claude Code run shows the rule improves output; keep for v1.x or promote to v2.0.

This prevents one viral post, answer screenshot, or narrow topic example from becoming a permanent generator habit.
