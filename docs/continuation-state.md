# Continuation State

Last updated: 2026-07-06.

Purpose: make long-running unattended work resumable without rereading the entire conversation.

## Current Focus

The project is currently prioritizing CUMCM official excellent papers and converting them into:

- paper-structure rules;
- model-chain patterns;
- algorithm cards;
- LaTeX section contracts;
- visual-generation and artifact-tracing rules;
- quality-review rubrics.

## Completed Deep Reads

| Sample | Route learned | Output |
| --- | --- | --- |
| User awarded paper `LATEX/model1.pdf` | complete LaTeX paper structure | `knowledge/latex/model1-case-study.md` |
| 2021 D017 | online scheduling and industrial adjustment | `knowledge/cumcm/deep-reading-2021D017.md` |
| 2021 A028 | geometry and engineering mechanics | `knowledge/cumcm/deep-reading-2021A028.md` |
| 2021 C066 | supply-chain evaluation and planning | `knowledge/cumcm/deep-reading-2021C066.md` |

## Strong Entry Points

Read these first for generation/review tasks:

1. `knowledge/README.md`
2. `knowledge/cumcm/paper-generation-playbook.md`
3. `knowledge/cumcm/20-30-page-paper-blueprint.md`
4. `knowledge/algorithms/model-chain-patterns.md`
5. `knowledge/algorithms/cards/README.md`
6. `docs/visual-generation-pipeline.md`
7. `knowledge/quality/quality-rubric-v2.md`

## Next Reading Queue

Next P0 papers:

1. `2021 E014`: spectral classification route; extract preprocessing, feature extraction, classifier comparison, confusion/error analysis.
2. `2022 B030`: geometry/spatial engineering route; compare with A028 for formula-to-figure pattern.
3. `2022 C155`: decision/planning route; compare with C066 for planning and robustness.
4. `2023 C050`: dynamic pricing/supply-chain bridge.
5. `2023 D039`: spatial optimization and visualization.
6. `2023 E176`: monitoring/data-analysis route.

## Operating Rules

- Do not upload to GitHub more than once per day unless the user explicitly requests an immediate upload.
- Prefer local commits during unattended learning.
- If GitHub push is needed and direct network fails, use the local proxy route already verified:

```text
git -C .\math-modeling-paper-generator -c http.proxy=http://127.0.0.1:7890 -c https.proxy=http://127.0.0.1:7890 push origin master
```

- Stop before the final 10% of the five-hour work window. If exact account quota is not visible, use 4.5 hours of visible goal time as the conservative stop point.

## Current Method Lessons

Geometry/engineering route:

- coordinate frame before optimization;
- target surface or physical relation before solver;
- deviation metric plus final physical-performance metric;
- explanatory schematics plus evidence plots;
- node/control-result table;
- appendix code inventory.

Supply-chain route:

- data preprocessing before scoring;
- indicator hierarchy before TOPSIS;
- evaluation result must feed supplier selection;
- selected suppliers must feed executable order and transport plans;
- validation should include inventory stability and capacity feasibility;
- artifact ledger should separate evaluation, decision, and validation results.

## Git State Rule

Before stopping a work block:

1. run a status check;
2. commit local progress if coherent;
3. do not push unless daily sync is due or user asks;
4. update this file when the next best action changes.
