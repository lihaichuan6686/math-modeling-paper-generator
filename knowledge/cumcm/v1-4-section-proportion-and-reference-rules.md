# v1.4 Section Proportion And Reference Rules

Purpose: turn recent award-paper visual sampling and local format guidance into practical section-budget, reference, and appendix rules.

This file supplements `20-30-page-paper-blueprint.md` and `recent-award-paper-visual-rhythm.md`.

## Core Position

v1.4 should distinguish three different lengths:

| Tier | Typical use | Length meaning |
|---|---|---|
| 20-30 pages | early closed-loop v1 draft | usable, complete, but not necessarily strong award feel |
| 30-45 pages | stronger award-feel draft | enough room for data, model, results, validation, and appendix support |
| 45+ pages | heavy-data or multi-method problem | only acceptable when evidence and appendix burden justify it |

Do not judge quality by page count alone. Judge whether the body closes the problem before appendix support begins.

## Body-To-Appendix Rule

For v1.4 planning, separate:

- effective body pages;
- reference pages;
- appendix/code/support pages.

The body must contain:

- problem interpretation;
- model route;
- assumptions and symbols;
- formulas or algorithms;
- main result tables and figures;
- validation or sensitivity evidence;
- conclusion with direct answers.

Appendix may contain:

- code excerpts;
- long intermediate tables;
- supplementary figures;
- run logs;
- support-file inventory.

Fail the draft if appendix material is needed to understand the main answer.

## Suggested Proportions

Use these as soft ratios, not rigid law:

| Section group | 20-30 page closed-loop draft | 30-45 page award-feel draft | Warning sign |
|---|---:|---:|---|
| Abstract and keywords | about 1 page | about 1 page | half-page abstract for a multi-question problem |
| Restatement + analysis + route overview | 3-5 pages | 4-7 pages | long restatement, delayed route |
| Assumptions + symbols | 1-2 pages | 1.5-3 pages | unused assumptions or missing symbols |
| Data processing / feature construction | 2-4 pages | 3-6 pages | raw data jumps straight into model |
| Model + solution process | 7-12 pages | 10-18 pages | method names without formulas or solver logic |
| Results + interpretation | 3-6 pages | 5-9 pages | final answers only in conclusion or appendix |
| Validation + sensitivity + comparison | 2-4 pages | 3-7 pages | one ceremonial validation paragraph |
| Evaluation + limitations + conclusion | 1.5-3 pages | 2-4 pages | generic self-praise or vague ending |
| References | 0.5-1.5 pages | 0.5-2 pages | uncited padding or no method/data sources |
| Appendix/support | 3-8 pages | 5-15 pages when justified | appendix rescues a thin body |

## Reference Rules

References should be enough to support the paper, not enough to look academic by volume.

Required citation types:

- official contest data or official policy/standard sources when used;
- method sources for nontrivial algorithms, models, or metrics;
- domain sources for specialized background assumptions;
- software/package citations only when they materially support reproducibility or method choice.

Avoid:

- references that never appear in the body;
- generic textbook padding when a specific method/source is needed;
- web links used as decoration;
- fabricated or unresolved placeholders in a final draft.

Soft target:

- early v1 draft: at least the core method/data/domain sources are present, even if the list is short;
- stronger v1.4 draft: references should visibly support methods, data, and domain facts across the body.

## Figure/Table Proportion Rules

For v1.4, figures and tables should be distributed across the paper:

- early: route, object, symbol, parameter, or data table;
- middle: formulas, model diagrams, solver/process tables, evidence plots;
- result section: direct answer tables and result figures;
- validation section: sensitivity, residual, robustness, comparison, or feasibility artifacts;
- appendix: code inventory and supplementary outputs.

Minimum expectation for nontrivial multi-question problems:

- at least one early route/object/model artifact;
- at least one visible artifact per major subquestion;
- at least one validation or comparison artifact;
- final answer tables in the body.

## Review Questions

Before final handoff, ask:

1. Is the body complete without appendix code?
2. Does the first half of the paper contain enough model evidence, not only setup?
3. Are results and validation visible before references/appendix?
4. Are references cited where their claims appear?
5. Are appendix pages mapped to subquestions or files?
6. Does the paper explain why its length tier is appropriate?
