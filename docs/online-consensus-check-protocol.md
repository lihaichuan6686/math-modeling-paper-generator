# Online Consensus Check Protocol

Purpose: define how Claude Code should use public online discussion before writing the final paper.

This protocol is for reflection and sanity checking, not answer copying.

## When To Use

Use after:

- the problem has been read;
- the route-decision file exists;
- the initial model plan exists.

Use before:

- final paper writing;
- abstract writing;
- conclusion writing.

## Where To Look

Search public, accessible sources such as:

- Bilibili explanation videos and comments;
- Xiaohongshu experience posts, when publicly accessible;
- Zhihu answers;
- public WeChat articles surfaced through search;
- CSDN or blog posts;
- GitHub/Gitee public repos;
- university training notes;
- public contest-solution summaries.

Do not require login-only scraping.
Do not bypass platform protections.
If a platform is inaccessible, record that and use accessible public sources or user-supplied links/screenshots.

## Search Order

Use two layers.

First search general contest-circle experience:

```text
数学建模 国赛 经验
数学建模 论文写作 摘要
数学建模 获奖论文 结构
数学建模 常见错误
B站 数学建模 论文写作
小红书 数学建模 经验分享
```

Then search the active problem only after the initial route exists.

This prevents the model from copying public answers before it has its own interpretation.

## What To Extract

Record only reusable signals:

- common interpretation of each subquestion;
- common traps or misunderstood words;
- typical model families people discuss;
- rough result ranges, if repeatedly mentioned;
- figure/table ideas;
- criticism of weak approaches;
- useful wording or structure advice.

Do not copy:

- final answers;
- full text;
- private materials;
- paid course content;
- unverified numeric claims without marking uncertainty.

## Source Quality Rubric

Classify each source:

- `high`: official note, university training, detailed post with reasoning and data;
- `medium`: contest veteran summary, detailed video, public solution with caveats;
- `low`: short post, unsupported screenshot, answer-only comment;
- `reject`: paid leak, cheating request, unverifiable answer dump, private material.

## Required Output

Save a run note:

```text
runs/current/online-consensus-notes.md
```

Use `online-consensus-example-template.md` if the run needs a concrete filled-shape example.
Use `knowledge/community/public-community-source-playbook.md` to decide what each public platform can and cannot safely provide.

Use this structure:

```text
searched sources
common interpretations
common methods
rough result ranges
warnings and traps
what changed in route-decision
what was rejected
remaining uncertainty
```

## Reflection Questions

After the check, answer:

1. Did our route miss a common interpretation?
2. Are our results in a plausible range?
3. Are we overusing a method that the community treats as weak or decorative?
4. Are we missing a figure, table, or validation that strong teams usually include?
5. Did online discussion create pressure to copy, and how did we avoid that?
6. Did online discussion create panic because another result differed from ours?
7. If the route changed, did it change because of problem logic rather than popularity?

## Conversion Rule

Every useful public signal should be converted into one or more run-file changes.

| Signal type | Allowed conversion |
|---|---|
| common interpretation | update `problem-analysis.md` or `route-decision.md` |
| common trap | add a warning to `route-decision.md`, `verification-plan.md`, or `review-current.md` |
| common route family | compare against `model-candidates.md`; do not auto-adopt |
| rough result range | add sanity check to `verification-plan.md`; mark uncertainty |
| missing figure/table idea | update `figure-plan.md` and `artifact-ledger.md` |
| validation expectation | update `verification-plan.md` and quality review checklist |
| wording taboo | update `writing-style-plan.md` |

If a public signal changes nothing, record why it was rejected or discounted.

## Safety Boundary

The check should make the paper more self-aware.
It must not make the paper a collage of online answers.
