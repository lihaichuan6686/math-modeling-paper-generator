# Local Template Variant Index

Purpose: turn the local `LATEX/` examples and template families into a concrete decision aid for paper drafting.

This is a local-template bridge, not a full paper review.

## What We Have Already Seen

### `model1.tex`

This sample is a dense, full-paper-style demonstration. It is useful because it shows:

- a complete CUMCM paper skeleton rather than a toy fragment;
- explicit abstract-to-body-to-appendix flow;
- question-by-question exposition in the main body;
- heavy use of formulas, figures, and tables to carry the argument;
- a reproducibility-friendly style with visible symbols and section structure;
- practical package choices such as `withoutpreface`, `bwprint`, `booktabs`, `subcaption`, and `cleveref`;
- a compile workflow that assumes `xelatex` / `latexmk` rather than a bare minimal setup.

What it teaches the generator:

- the paper can feel long because each subquestion gets its own evidence chain;
- formulas should be explained in words, not dropped in alone;
- figures and tables are part of the argument, not decoration;
- symbols should be defined where they first matter and then reused.
- support-file and code appendices can strengthen trust when the body has already completed the reasoning loop.

### `document.tex`

This sample is a lighter template demonstration. It is useful because it shows:

- a minimal `cumcmthesis` project shell;
- package setup and template options;
- the usual top-level paper sections in compact form;
- how the template can serve as a clean starting point before route-specific expansion.

What it teaches the generator:

- the template family itself is stable;
- the real work is in filling the sections with route-specific evidence;
- the same shell can support very different paper voices.

### `2024国赛Word及LaTeX模板`

This bucket gives us an adjacent template family, including a Word standard template. It is useful as a comparison source for:

- front-matter layout;
- section density;
- title/abstract treatment;
- how different template families shape the feel of the same contest paper.

## Practical Style Takeaways

1. Choose the template family before drafting the body.
2. Match section density to the route, not to habit.
3. Use figures, tables, and equations as proof objects.
4. Keep the abstract and conclusion aligned with the actual body evidence.
5. Prefer the smallest template change that still supports the route.

## What Is Still Thin

- Route-specific comparison notes for the local 2023 excellent-paper set.
- More direct mapping from local template family to page-density targets.
- More concrete examples of how the same template shell produces different route voices.
- More polished guidance for dense Chinese academic phrasing at the paragraph level.
- More explicit page-feel rules for abstract density, early object figures, and subquestion-loop rhythm.

## Next Use

Read this note when you need to decide:

- which template shell to start from;
- how heavy the section evidence should be;
- whether the paper should feel official-concise, route-heavy, or evidence-dense.

## Best Use

Read this note together with:

- `style-variant-index.md`
- `local-awarded-paper-structure-rules.md`
- `cumcm-section-contract.md`
- `section-family-index.md`
- `archetype-page-density-matrix.md`
- `paper-style-plan.md`
