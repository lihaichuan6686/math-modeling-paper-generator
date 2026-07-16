# Community Signal To Rule Pipeline

Purpose: convert contest-circle posts, videos, local experience notes, and award-paper observations into reusable generator behavior.

This file is the missing middle layer between "read more material" and "write a better paper".
It prevents community learning from becoming scattered notes or answer hunting.

## Core Principle

Every learned signal must become one of four things:

| Input signal | Output artifact | Example conversion |
|---|---|---|
| soft writing rule | `writing-style-plan.md` or `knowledge/community/*.md` | "Do not make the abstract a method list" becomes an abstract closeout check |
| paper-structure observation | `section-budget.md` or `knowledge/cumcm/*.md` | "Excellent papers put result artifacts early" becomes a body-page rhythm rule |
| modeling-route warning | `route-decision.md`, `model-plan.md`, or `verification-plan.md` | "Ranking alone is thin" becomes rank-to-decision planning |
| review failure pattern | `reviews/review-current.md` or `knowledge/quality/*.md` | "Figures are decorative" becomes a fail condition |

If a note cannot be converted into one of these outputs, do not treat it as absorbed knowledge.

## Source Intake

Use this order during static learning:

1. Local experience files, especially writing, contest workflow, and common-mistake materials.
2. Local excellent papers and user-provided strong papers.
3. University or official public training materials.
4. Public long-form posts or videos with visible reasoning.
5. Short social posts, comments, or screenshots only as weak soft-rule signals.

Use this order during a concrete run:

1. General contest-circle experience and writing rules.
2. Domain background and method references.
3. Initial route-decision and model-plan.
4. Public exact-problem discussion only for sanity checking.
5. Final route reflection before code, figures, tables, and paper writing.

## Absorption Card

For each source batch, write a small absorption card before editing rules.

```text
Source:
Type:
Access:
Trust level:
Reusable signals:
Rejected signals:
Converted files:
Follow-up test:
```

The card can live in `knowledge/community/local-experience-absorption-log.md`, a run note, or a calibration log.

## Conversion Checklist

Before saying a source has been learned, verify:

- at least one reusable signal was extracted;
- the signal is not just a method name;
- the signal affects a run file, review gate, prompt, or stable knowledge file;
- any exact numeric answer or final ranking from public discussion was rejected or downgraded;
- the rule is phrased generally enough to help future problems;
- the rule does not overfit one topic family.

## Soft-Rule Categories

Map each useful signal into exactly one primary category:

| Category | Meaning | Typical destination |
|---|---|---|
| section duty | what a section must visibly accomplish | `section-budget.md`, `section-duty-soft-rules.md` |
| abstract density | what page one must answer | `v1-4-abstract-closeout-rules.md` |
| route discipline | how to avoid template forcing | `route-decision.md`, `route-selection-protocol.md` |
| evidence chain | how figures, tables, code, and text support claims | `figure-plan.md`, `artifact-ledger.md` |
| human-team feel | how modeling, programming, and writing roles show up | `contest-workflow-and-team-execution.md` |
| public consensus | how online discussion changes or does not change the route | `online-consensus-notes.md` |
| taboo wording | phrases, tone, and claims that sound naive | `writing-style-plan.md`, `common-mistakes-and-taboo-phrases.md` |
| review gate | how a weak paper should fail | `v1-4-human-feel-review-gate.md` |

## Public Platform Handling

For Xiaohongshu, Bilibili, Zhihu, CSDN, and public blogs:

- prefer public pages visible without login;
- record platform attempts even when search results are sparse;
- do not bypass login walls or platform protections;
- use short posts as weak signals unless they include reasoning;
- never copy final answers;
- record whether the signal changes the route, validation, figure plan, wording plan, or nothing.

If a platform is inaccessible, write:

```text
Platform attempt: inaccessible or sparse.
Fallback: use accessible public sources, local experience notes, and user-supplied links/screenshots.
Effect on route: none until a checkable signal appears.
```

## Rule Maturity Levels

| Level | Meaning | Allowed use |
|---|---|---|
| observed | one source mentions it | note only; do not enforce |
| repeated | several sources or papers show it | may guide a run file |
| stable | local papers and public experience agree | add to prompt or review gate |
| tested | user-side Claude Code run confirms impact | keep for v1.x or promote to v2.0 |

Do not put an `observed` rule directly into a hard fail gate.

## Anti-Overfitting Rule

A signal is too narrow if it depends on:

- one historical problem statement;
- one data column name;
- one domain such as spectral recognition, rail scheduling, or carbon accounting;
- one public answer screenshot;
- one algorithm preference without route logic.

Generalize it before adding it to the v1.4 layer.

Examples:

| Too narrow | Better reusable rule |
|---|---|
| "For this spectral problem, use PCA before clustering" | "For high-dimensional measurements, explain feature compression and validate that it preserves class or ranking information" |
| "This year's C problem top answer is X" | "Use public result ranges only as sanity checks, never as target answers" |
| "Everyone used entropy weight" | "Weighting methods need data-fit and sensitivity explanation; popularity is not proof" |

## Review Questions

After conversion, ask:

1. Would this rule help a future CUMCM problem from a different family?
2. Does it change what Claude writes, checks, or produces?
3. Can a reviewer see the effect in the final paper?
4. Does it improve human-team feel rather than only adding terminology?
5. Is the rule safe for research use and non-copying behavior?

If the answer to any question is no, keep the signal in the absorption log instead of promoting it.
