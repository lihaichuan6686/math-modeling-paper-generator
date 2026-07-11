# Human Style Soft Rules

Purpose: capture the soft structural rules that make a CUMCM paper feel like it was written by a strong human team rather than by a shallow draft generator.

These are soft rules, not fixed laws. They should guide proportion, density, and paragraph feel.

## Core Principle

A human-team paper usually feels credible because each section is proportioned with intent.

The question is not only "is the section present?"

The question is:

```text
does the section feel like the amount a serious team would naturally write here?
```

## Global Soft Rules

1. The abstract should usually fill about one dense page.
2. Problem analysis should feel like route justification, not restatement padding.
3. Model establishment should be the longest technical section.
4. Results and validation should both be visible; validation should not be hidden in one sentence.
5. Conclusion should be shorter than results but still answer every task.
6. Appendix should support reproducibility, not rescue a thin body.

## Abstract Soft Rules

The abstract should usually contain:

- one opening sentence for the full task;
- one method-result closure for each subquestion;
- one sentence on validation or comparison;
- one closing sentence on the overall recommendation or result pattern;
- keywords that match the actual method chain.

Signs the abstract is too thin:

- it ends in half a page;
- it lists methods without results;
- it gives background but not subquestion closure;
- it promises a conclusion that never appears in the paper body.

## Problem Analysis Soft Rules

A strong human-written analysis section usually does four jobs:

- translate the task into modelable parts;
- explain route choice;
- distinguish similar but rejected routes;
- preview the evidence artifacts that will appear later.

Signs the section is too weak:

- it repeats the problem statement with light paraphrase;
- it jumps to formulas before explaining why the route fits;
- it has no route table, dependency diagram, or artifact preview.

## Model Section Soft Rules

This is where serious teams earn paper length.

Expected content:

- variables and assumptions with real modeling purpose;
- equations and constraints grouped by subquestion;
- explanation of why the chosen model is appropriate;
- solver or algorithm description;
- transition from model definition to executable outputs.

Signs the section is too shallow:

- only one named method with almost no support layer;
- equations are present but not interpreted;
- there is no bridge from model to later result table or figure.

## Result Section Soft Rules

Each major result should be followed by interpretation.

Good rhythm:

```text
artifact
-> what it answers
-> why the pattern matters
-> how it supports the recommendation
```

Bad rhythm:

```text
artifact
-> next artifact
-> next artifact
```

## Validation Soft Rules

Human teams often show that they know where the answer may fail.

Useful validation forms:

- sensitivity to weights, parameters, or assumptions;
- baseline comparison;
- scenario stress test;
- residual or error analysis;
- feasibility or audit table;
- ablation or model comparison.

If the paper has a sophisticated method but no visible check layer, it still feels machine-thin.

## Paragraph Soft Rules

Prefer compact analytical paragraphs over repeated micro-bullets.

Useful paragraph rhythm:

```text
topic sentence
-> model or artifact reference
-> interpretation
-> transition
```

Avoid:

- four consecutive one-sentence paragraphs;
- repeated "first/second/third" lists where prose would be more natural;
- generic praise of the method;
- announcing that a figure exists without saying what it proves.

## Human-Team Voice Rules

The paper should sound deliberate rather than inflated.

Prefer:

- explicit tradeoffs;
- route-aware explanations;
- method limitations stated calmly;
- quantified conclusions;
- sentence-level transitions between tasks.

Avoid:

- empty claims such as "the model is scientific and effective";
- method name stacking for prestige;
- dramatic wording that does not add evidence;
- long bullet-heavy prose inside the main body.

## Best Use

Read this note together with:

- `section-writing-patterns.md`
- `style-variant-index.md`
- `local-template-variant-index.md`
- `../cumcm/20-30-page-paper-blueprint.md`
- `../../docs/v1.2-runbook.md`

