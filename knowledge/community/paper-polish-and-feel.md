# Paper Polish And Award Feel

Purpose: describe the visible qualities that make a modeling paper look like a serious award-level submission.

This file focuses on feel, not hidden algorithm quality.

## First-Glance Signals

A strong paper usually signals quality before the reviewer reads every formula:

- dense but readable abstract;
- clean section hierarchy;
- early model-route figure or table;
- not too much problem-restatement padding;
- equations and symbols introduced before heavy use;
- figures and tables placed near interpretation;
- final answers easy to locate;
- references and appendix look deliberate.

## Abstract Feel

The abstract should feel like a compressed solution.

For multi-question CUMCM papers, aim for:

```text
background in one or two sentences
-> route overview
-> Q1 method and result
-> Q2 method and result
-> Q3 method and result
-> validation or sensitivity
-> final recommendation or conclusion
```

Soft rule:

- A half-page abstract often feels underdeveloped for a 20-30 page paper.
- A full dense page is normal when there are multiple subquestions.
- Method names without results feel weak.

## Problem Restatement Feel

Should be short and model-oriented.

It should answer:

- what is given;
- what must be solved;
- what outputs must appear;
- what constraints or uncertainties matter.

It should not become a paraphrase wall.

## Problem Analysis Feel

This is where the paper starts to look intelligent.

Good problem analysis:

- explains why the task decomposes into subproblems;
- names the modeled object and decision object;
- says why a route family fits;
- hints at validation and result form.

Weak problem analysis:

- repeats the background;
- lists methods before explaining the task;
- says "we establish a model" without saying what the model decides.

## Model Section Feel

Award-like model sections usually have layers:

```text
baseline or direct formulation
-> improvement or route-specific model
-> solving method
-> result artifact
-> interpretation
-> validation or comparison
```

The "advanced" part is useful only when the paper also shows:

- why the simple method is insufficient;
- what improved;
- what remained weak.

Local writing guidance adds a practical test:

```text
model idea
-> formula or algorithm basis
-> software or computation route
-> result table/figure
-> reasonableness check
-> concise conclusion
```

If a model section stops at formulas or code description, it still feels unfinished. If it jumps directly from method name to final claim, it feels untrustworthy.

## Figure And Table Feel

Figures:

- should reveal structure, route, trend, comparison, or validation;
- should not be inserted after writing as decoration;
- should have captions that explain argumentative role.

Tables:

- should carry result values, parameter choices, comparisons, or final answers;
- should be compact enough to read;
- should be interpreted immediately after citation.

Result display should be concentrated enough for comparison. Put main answer tables and decisive figures in the body even if detailed data are repeated in the appendix. Appendix-only results make the paper feel as if it is hiding the answer.

## Reference Feel

References should support:

- method definitions;
- data sources;
- domain facts;
- standards, policies, or official documents.

Too few references make the paper feel improvised.
Too many irrelevant references make it feel padded.

## Human-Team Signals

Add these signals deliberately:

- a route comparison or rejected-route sentence;
- a baseline before an improved method;
- one or two places where a limitation is specific;
- result interpretation after each major table or figure;
- final answers repeated cleanly in conclusion.

Another strong human-team signal is controlled self-correction: the paper can say that a simpler route was first used as a baseline, then improved because a specific error, constraint, or validation gap appeared. This feels stronger than announcing an advanced algorithm without showing why it was needed.

## Section-Duty Signals

Local writing guides emphasize that a contest paper is not only a model report; it is a complete answer document.

First-glance quality improves when:

- the abstract has route, method, validation, and results rather than slogans;
- keywords reveal the application object and method family;
- restatement is compact and task-oriented;
- problem analysis contains a route framework or subquestion logic;
- assumptions are few, necessary, and reused;
- symbol tables match later formulas;
- model sections show basic model, simplification basis, solution method, result, and interpretation;
- evaluation names real strengths and limits;
- appendix supports reproducibility after the body has already answered the task.

First-glance quality drops when:

- the paper is long because of copied background;
- assumptions are ceremonial;
- symbols never reappear;
- figures and tables are far from their explanation;
- the conclusion praises the model without repeating actual answers.

## Excellent-Paper Reading Transfer

When converting an excellent-paper reading note into generator behavior, keep four reusable observations:

- the abstract should expose method and key conclusions before the reader reaches the body;
- problem analysis should show the route, required conditions, and rough solving path;
- assumptions should simplify the problem in a way that later formulas actually use;
- error analysis should focus on the most debatable modeling choice, not list generic uncertainty.

This is more valuable than copying the topic-specific algorithm from the sample paper.
