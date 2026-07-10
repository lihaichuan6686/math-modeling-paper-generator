# Official Paper Paradigms

Purpose: distill the recurring structures from the official excellent-paper first-pass readings into generator-ready patterns.

## Corpus Behind This Note

- `2021-official-first-pass.md`
- `2022-official-first-pass.md`
- `2023-official-first-pass.md`
- `official-style-vs-modern-draft-risk.md`
- `2021C-comparison-C066-C085-C169-C283.md`
- `2021D-comparison-D017-D026-D034.md`
- `deep-reading-2022E014.md`
- `deep-reading-2022E029.md`
- `deep-reading-2023E176.md`

## Shared Shape Across Official Papers

Official excellent papers are usually not long because they are verbose. They are long because each subproblem closes a full loop:

```text
problem map
-> object / data / geometry setup
-> method or model
-> result table or figure
-> interpretation
-> validation / comparison
```

The strongest papers keep that loop visible in the abstract, body, figures, and conclusion.

## Route Family Table

| Route family | Main signal | Typical closure |
|---|---|---|
| Geometry and engineering | coordinate frame, physical object, constraints | schematic figure -> formula -> numeric closure -> feasibility check |
| Evaluation and ranking | indicators, screening, recommendation | indicator table -> weights or scores -> ranking -> sensitivity check |
| Evaluation to planning | screening then executable decision | ranking -> decision model -> plan table -> feasibility audit |
| Forecast to decision | historical data and uncertainty | trend figure -> forecast -> policy or plan -> scenario comparison |
| Classification or recognition | labels and feature engineering | preprocessing -> features -> model comparison -> confusion-level evidence |
| Online optimization and process update | baseline then abnormal update | initial plan -> trigger -> adjusted plan -> before/after comparison |

## What The Official Papers Repeatedly Do

### 1. They name the object early

The first figure or early paragraph usually shows the modeled object, not the final score.

### 2. They keep the question map stable

The abstract, section titles, tables, and conclusion refer to the same numbered tasks.

### 3. They show at least one visible result per subproblem

Each subproblem gets a result table, figure, or decision consequence. Lists of methods without outputs are rare.

### 4. They use multiple methods, but only where the route needs them

Combined methods appear often, but the combination is functional, not decorative. Common patterns are:

- data processing -> model building -> solve -> validate;
- screening -> optimization -> executable plan;
- prediction -> decision;
- preprocessing -> classification -> evaluation.

### 5. They keep appendix material subordinate

Appendix code and support material help traceability, but the paper body already tells the full story.

## Abstract Pattern

The best reusable abstract shape is:

```text
background and goal
-> subproblem 1 method + key result
-> subproblem 2 method + key result
-> subproblem 3 method + key result
-> validation or extension
-> final conclusion
```

The abstract should already expose the route, not just the topic.

## Figure And Table Paradigms

- first figure: identify the object, network, geometry, or data structure;
- next figures: show comparison, change, or sensitivity;
- tables: keep variable names, units, and output roles aligned;
- captions: explain what the figure proves, not just what it shows.

## Generator Rules

1. Start from the route family, not from a random algorithm list.
2. Keep one stable question map across abstract, body, figure captions, and conclusion.
3. Make every method produce a visible artifact.
4. Use appendix material for traceability, not to fake length.
5. Budget page count through repeated evidence loops, not through code screenshots or empty shells.

## Status

This note is the official-paper counterpart to the risk-reading notes. It should be treated as the positive template for future generation prompts and review checklists.
