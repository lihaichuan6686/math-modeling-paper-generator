# Table Family Index

Purpose: map common CUMCM table types to their first job in the paper.

This note helps table planning before writing and formatting.

## Table Families At A Glance

| Table family | First job | Typical section | Common source | Typical caption focus |
|---|---|---|---|---|
| Task / output table | show how the problem is decomposed | problem restatement or analysis | manually structured from the problem statement | tasks, inputs, outputs, and constraints |
| Assumption table | make simplifications auditable | assumptions | manually structured | reason for simplification and impact |
| Symbol table | define variables once | symbols | manually structured | variable meaning, unit, domain |
| Data inventory table | show data fields and cleaning logic | data processing | manual or code-assisted | file, field, unit, missingness, use |
| Parameter table | record model settings | model establishment or solution process | code or manual extraction | parameter meaning and value |
| Result table | present the main output | results | code-generated or manually assembled from code outputs | decision meaning and key values |
| Validation table | show feasibility or robustness | validation | code-generated or manual audit summary | test setup, outcome, and implication |
| Comparison table | compare scenarios or methods | results or validation | code-generated | relative effect or improvement |
| Review table | support PDF/layout inspection | review | screenshot or render-based notes | readability, clipping, or residue status |

## First Table Rule

The first strong table should usually do one of these jobs:

1. decompose the task;
2. define assumptions;
3. define symbols;
4. summarize the data;
5. present the decision variables or parameters.

Do not spend the first strong table on a decorative summary that does not help the model.

## Table-Role Pairing Rule

Where possible, pair each family with its usual figure companion:

- task table -> route/workflow figure;
- assumption table -> object or route schematic;
- symbol table -> coordinate or variable schematic if needed;
- data inventory table -> data exploration figure;
- parameter table -> model structure figure or flowchart;
- result table -> result figure;
- validation table -> validation figure;
- comparison table -> scenario or baseline comparison figure;
- review table -> PDF screenshot or layout comparison image.

## Planning Rule

When building `runs/current/figure-plan.md` and `runs/current/artifact-ledger.md`, choose table families in this order:

```text
task -> assumption -> symbol -> data -> parameter -> result -> validation -> comparison -> review
```

## Best Use

Read this note together with:

- `figures-tables-equations-style.md`
- `section-map.md`
- `visual-family-index.md`
- `../docs/artifact-ledger-template.md`

