# LaTeX

Purpose: give the generator one stable entry point for turning a modeling plan into a complete CUMCM-style paper structure.

## Read This Layer In Order

1. `cumcm-section-contract.md`
2. `section-writing-patterns.md`
3. `figures-tables-equations-style.md`
4. `snippets.md`
5. `section-map.md`
6. `visual-family-index.md`
7. `table-family-index.md`
8. `equation-family-index.md`
9. `paper-style-plan.md`
10. `long-paper-blueprint.md`

## What This Layer Does

This layer answers four questions:

1. What must each section do?
2. What should the next paragraph or artifact look like?
3. How should figures, tables, and equations be formatted?
4. How do we keep the paper structurally credible while it grows to 20-30 pages?

The goal is not decorative formatting. The goal is a paper that reads like a complete modeling result.

## Section Chain

Use the section contract as the default path:

```text
problem restatement
-> analysis
-> assumptions
-> symbols
-> data processing
-> model establishment
-> solution process
-> results
-> validation
-> strengths and limitations
-> conclusion
```

## Artifact Chain

Use this rule when writing or checking the paper:

```text
claim -> evidence artifact -> interpretation -> limitation or transition
```

Every major section should contribute at least one visible artifact:

- route figure or dependency table;
- data summary or feature table;
- model equation block;
- solver or algorithm steps;
- result table or figure;
- validation artifact.

## Minimum Evidence Contract

Before drafting LaTeX, confirm:

- the section purpose is clear;
- the evidence artifact exists or is planned;
- symbols are defined once and reused;
- figure and table filenames are stable;
- abstract and conclusion wait until results are stable.

## Status

This file is the top-level doorway for the LaTeX knowledge base. It should stay short and should point the generator toward structure before style.
