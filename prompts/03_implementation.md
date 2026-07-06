# Phase 3 Prompt: Implementation

Read:

- `runs/current/model-plan.md`
- `runs/current/verification-plan.md`
- `runs/current/figure-plan.md`
- `runs/current/artifact-ledger.md`
- `knowledge/latex/figures-tables-equations-style.md`

Create or update:

- source code under `src/`
- figures under `paper/figures/`
- tables under `paper/tables/`
- intermediate results under `runs/current/`
- update `runs/current/artifact-ledger.md`

## Requirements

- Keep one clear entry point or run sequence.
- Record random seeds.
- Save figures with stable English filenames.
- Save tables with stable filenames.
- Make data-driven figures reproducible from code.
- Record any schematic or AI-generated explanatory image source/prompt.
- Do not write non-reproducible manual numbers into the paper.

## Figure Generation Chain

For each planned figure:

```text
planned figure -> source/tool -> output file -> caption idea -> artifact ledger entry
```

Evidence figures must come from code and data.

Explanatory figures may come from Mermaid, TikZ, Python, vector drawing, or an image-generation tool, but must be marked as schematic when they are not data-derived.

## Table Generation Chain

For each planned table:

```text
source data/model output -> table file -> paper label -> artifact ledger entry
```

## Completion Gate

Implementation is not complete until:

1. required figures exist or are explicitly marked as pending
2. required tables exist or are explicitly marked as pending
3. key numerical results are saved
4. artifact ledger is updated
5. known failures are documented
