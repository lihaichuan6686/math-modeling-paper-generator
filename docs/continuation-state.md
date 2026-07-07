# Continuation State

Last updated: 2026-07-07.

Purpose: make long-running unattended work resumable without rereading the entire conversation.

## Current Focus

The project has shifted from "read more first" to improving the v1.0 closed-loop toolchain through real generated-paper reviews:

```text
problem -> scaffold -> model plan -> code/table/figure -> LaTeX draft -> PDF/review
```

The bundled `v1-demo` now compiles and has rendered-PDF review evidence. A real MathorCup 2023 B test run showed that the tool can produce a complete draft and attachments, but the next priority is stronger contest-grade modeling, especially for rail-timetable optimization.

Latest local progress: the MathorCup 2023 B review has been converted into a reusable rail/timetable route. The repository now has a Type I archetype, a rail-timetable operation card, stricter model-plan/implementation/review gates, a runnable rail-timetable demo pipeline, a compiled 10-page `paper/rail_demo.tex` example, and an automatic minimum machine artifact gate for the demo scripts.

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
2. `docs/project-audit-2026-07-06.md`
3. `knowledge/cumcm/paper-generation-playbook.md`
4. `knowledge/cumcm/20-30-page-paper-blueprint.md`
5. `knowledge/cumcm/problem-type-paper-archetypes.md`
6. `knowledge/algorithms/model-chain-patterns.md`
7. `knowledge/algorithms/cards/README.md`
8. `docs/visual-generation-pipeline.md`
9. `knowledge/latex/section-writing-patterns.md`
10. `prompts/06_quality_review.md`
11. `knowledge/quality/quality-rubric-v2.md`
12. `knowledge/quality/mathorcup-2023B-v1-test-review.md`

## Next Reading Queue

Next P0 papers:

1. `2021 E014`: spectral classification route; extract preprocessing, feature extraction, classifier comparison, confusion/error analysis.
2. `2022 B030`: geometry/spatial engineering route; compare with A028 for formula-to-figure pattern.
3. `2022 C155`: decision/planning route; compare with C066 for planning and robustness.
4. `2023 C050`: dynamic pricing/supply-chain bridge.
5. `2023 D039`: spatial optimization and visualization.
6. `2023 E176`: monitoring/data-analysis route.

## v1.0 Demo Baseline

The first small closed-loop demo exists and has been compiled/reviewed:

- clone-ready entry: `START_HERE.md`
- repository skill: `.codex/skills/cumcm-paper-generator/SKILL.md`
- active-run starter: `scripts/start-current.ps1`
- `docs/v1-runbook.md`
- `problems/demo-v1-supply.md`
- `scripts/run-v1-demo.ps1`
- `src/demo_v1.py`
- generated demo table: `paper/tables/demo_v1_order_plan.csv`
- generated demo figure: `paper/figures/demo_v1_inventory.png`
- generated demo summary: `runs/v1-demo/demo-v1-summary.md`
- demo artifact ledger: `runs/v1-demo/artifact-ledger.md`
- demo review: `reviews/review-v1-demo.md`
- compiled PDF: `paper/main.pdf` (ignored by Git)

Do not treat this as final paper quality. It proves the loop; the next work is expansion, packaging, and stronger examples.

## Next Engineering Queue

1. Add automated checks for additional problem types beyond Type I rail/timetable cases.
2. Add real attachment parsing and OD assignment to the rail route.
3. Expand the compact rail demo toward a 20-30 page example only after adding real attachment parsing, OD assignment, and fleet/turnback constraints.
4. Expand generated papers toward 20-30 pages by requiring each subproblem to include model construction, algorithm, result table/figure, and validation.
5. Improve Chinese figure/table polish: Chinese labels, readable axes, richer captions, and method-specific references.

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
