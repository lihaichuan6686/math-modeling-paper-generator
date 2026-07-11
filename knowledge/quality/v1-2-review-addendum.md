# v1.2 Review Addendum

Purpose: extend the standard paper review so it can detect the main failure modes of a thin machine-like draft.

This addendum focuses on paper feel, section density, and method-depth closure.

## Core Review Question

Do not ask only:

```text
Is the paper complete?
```

Also ask:

```text
Does the paper read like a serious human-team draft with enough density, method depth, and interpretation?
```

## v1.2 Failure Modes

Reviewers should actively look for:

- abstract too short to close the whole paper;
- sections present but too thin;
- method names without support layer or check layer;
- bullet-heavy main body;
- result artifacts dumped without interpretation;
- validation reduced to one sentence;
- page count that still depends on filler rather than evidence loops.

## Required v1.2 Checks

### 1. Abstract Density

Check:

- whether the abstract is close to one dense page;
- whether each major subquestion has method plus result closure;
- whether validation or comparison appears in the abstract;
- whether abstract claims are supported later.

Warn if:

- the abstract feels like a half-page executive note;
- method names appear without numerical or decision results.

### 2. Section Proportion

Check:

- whether problem analysis is long enough to justify the route;
- whether model establishment is the true technical center;
- whether results and validation are both visible;
- whether conclusion is short but still answers every task.

Warn if:

- the model section is shorter than the surrounding narration;
- validation is buried inside results with no distinct check layer.

### 3. Method Depth

For every major subquestion, check whether the chain reaches at least:

```text
support layer -> main model -> result -> validation/comparison
```

Warn if:

- the answer is only `method -> result`;
- a complex method is named but its support or comparison layer is missing.

### 4. Human-Team Prose Feel

Check:

- whether the body is paragraph-driven rather than bullet-driven;
- whether figures and tables are interpreted immediately after citation;
- whether the draft uses calm analytical prose instead of generic praise;
- whether each subquestion closes a full loop before the next begins.

Warn if:

- four or more short list-like paragraphs appear in a row;
- transitions feel mechanical rather than argumentative.

## Best Use

Read this note together with:

- `quality-rubric-v2.md`
- `../../docs/review-checklist.md`
- `../../docs/v1.2-runbook.md`
- `../latex/human-style-soft-rules.md`
- `../algorithms/method-depth-ladder.md`

