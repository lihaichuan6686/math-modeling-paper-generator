# Visual Family Index

Purpose: map common CUMCM visual artifacts to their first job in the paper.

This note helps figure planning before implementation starts.

## Visual Families At A Glance

| Visual family | First job | Typical section | Common source | Typical caption focus |
|---|---|---|---|---|
| Route / workflow figure | show the full modeling chain | problem analysis or method overview | Mermaid, TikZ, vector drawing | route and decision logic |
| Object / geometry schematic | identify the modeled object early | problem analysis or model establishment | TikZ, plotting, vector drawing | object, frame, and key constraints |
| Data exploration figure | show what the data look like | data processing | code-generated plot | trend, distribution, or structure |
| Result figure | show the main model output | results | code-generated plot | output and decision meaning |
| Validation figure | test whether the result is credible | validation | code-generated plot | error, sensitivity, or feasibility |
| Comparison figure | compare baseline, scenario, or methods | results or validation | code-generated plot | relative effect or improvement |
| Review figure | inspect layout or PDF rendering | review | screenshot or render tool | readability and clipping status |

## First Figure Rule

The first strong figure should usually do one of these jobs:

1. identify the object;
2. show the route;
3. show the data structure.

Do not use the first strong figure for a late-stage result if the reader still does not know what is being modeled.

## First Table Rule

The first strong table should usually do one of these jobs:

1. list tasks and outputs;
2. define symbols or parameters;
3. summarize cleaned data or extracted features;
4. present the core decision variables.

Do not use the first strong table as a decorative summary with no modeling role.

## Figure-Table Pairing Rule

Where possible, pair each family with its usual table companion:

- route figure -> task decomposition table;
- object schematic -> symbol/parameter table;
- data exploration figure -> data inventory table;
- result figure -> result table;
- validation figure -> sensitivity or feasibility table;
- comparison figure -> scenario or baseline comparison table.

## Planning Rule

When building `runs/current/figure-plan.md`, choose figures in this order:

```text
route -> object -> data -> result -> validation -> comparison -> review
```

## Best Use

Read this note together with:

- `figures-tables-equations-style.md`
- `../docs/figure-plan-template.md`
- `../docs/visual-generation-pipeline.md`
- `../knowledge/cumcm/paper-family-matrix.md`

