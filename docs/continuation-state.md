# Continuation State

Last updated: 2026-07-11.

Purpose: make long-running unattended work resumable without rereading the entire conversation.

## Current Focus

The project has shifted again from "prove the v1.0 loop" to delivering a v1.2 paper path that repairs thin prose, weak section density, and shallow method chains:

```text
problem -> scaffold -> deeper model plan -> section budget -> code/table/figure -> LaTeX draft -> PDF/review
```

Newest 1.2-upgrade progress: the repository now has `docs/v1.2-runbook.md`, `knowledge/latex/human-style-soft-rules.md`, `knowledge/algorithms/method-depth-ladder.md`, `prompts/08_launch_v1_2.md`, and `prompts/09_revision_v1_2.md`. These files move the execution standard from "small but complete" toward "human-team style with stronger method depth and section density", and add a dedicated repair loop after review.

The bundled `v1-demo` now compiles and has rendered-PDF review evidence. A real MathorCup 2023 B test run showed that the tool can produce a complete draft and attachments, but the next priority is stronger contest-grade modeling, especially for rail-timetable optimization.

Latest local progress: the MathorCup 2023 B review has been converted into a reusable rail/timetable route. The repository now has a Type I archetype, a rail-timetable operation card, stricter model-plan/implementation/review gates, a runnable rail-timetable demo pipeline, a compiled 10-page `paper/rail_demo.tex` example, and an automatic minimum machine artifact gate for the demo scripts.

Newest runnable-demo progress: the old supply toy has now been replaced by a synthetic production-route E closed-loop demo. The active `v1-demo` now generates representative-material screening, short-term forecast checks, rolling production plans, service-level summaries, scenario comparison tables/figures, a compiled `paper/main.pdf`, and rendered-page inspection evidence.

Newest comparison-reading progress: the repository now has a same-problem comparison note for the 2021 C supply-chain cluster (`C066`, `C085`, `C169`, `C283`). That note isolates the stable route contract for supplier-evaluation-plus-planning papers from the variable rhetorical choices such as uncertainty-led, optimization-led, or heuristic-led framing.

Newest comparison-reading progress on the scheduling side: the repository now also has a same-problem comparison note for the 2021 D continuous-cutting cluster (`D017`, `D026`, `D034`). That note separates the stable online-optimization backbone from three valid writing voices: theorem-led, multiobjective-planning-led, and implementation-led.

Newest risk-reading progress: `knowledge/cumcm/2024B-modern-draft-risk-reading.md` records a visual and structural audit of three 2024 B complete-looking drafts. It adds hard gates for placeholder leakage, watermark residue, empty appendices, orphan equations, unsupported claims, and page-count padding.

The risk corpus now also includes `knowledge/cumcm/2024C-modern-draft-risk-reading.md`, which separates partial-paper coverage failure from 69-page code/appendix inflation and adds explicit gates for scenario evidence, code linkage, and printed-page offsets.

Newest knowledge-layer progress: `2022 E014`, `2022 E029`, and `2023 E176` now form an explicit E-route family set, and that split has been written into the shared archetype, paper-blueprint, review-rubric, playbook, and generation prompts so the generator can distinguish production-route E papers from monitoring-route E papers at ideation, modeling, writing, and review time.

Newest retrieval-layer progress: `knowledge/cumcm/route-example-matrix.md` now pairs each route family with its fastest positive sample, comparison note, deep-reading anchor, and risk gate so future runs can jump from problem signal to sample stack without guesswork.

Newest start-layer progress: `docs/run-start-checklist.md` now gives Claude Code a compact first-pass sequence for a new run, including route selection, sample pairing, and the first required outputs.

Newest prompt-layer progress: `prompts/07_launch.md` now gives a single copy-paste launch prompt that ties the start checklist, route matrix, and phase prompts into one execution entry.

Newest LaTeX-layer progress: `knowledge/latex/section-family-index.md` now gives a section-by-section writing and repair index so thin or generic sections can be expanded with the right kind of artifact.

Newest algorithm-layer progress: `knowledge/algorithms/route-method-matrix.md` now bridges route families to first method families, expected artifacts, and validation focus so the generator can move from route selection to card selection with less guesswork.

Newest quality-layer progress: `knowledge/quality/finding-gate-matrix.md` now bridges review findings to the gate they should trigger and the evidence that usually repairs them.

Newest drafting-layer progress: `knowledge/cumcm/archetype-section-matrix.md` now maps CUMCM problem archetypes to section emphasis, first artifacts, and validation habits so problem typing can flow straight into a paper skeleton.

Newest page-layer progress: `knowledge/cumcm/archetype-page-density-matrix.md` now maps problem archetypes to page emphasis, visual density, and validation weight so the 20-30 page target can grow from evidence instead of filler.

Newest style-layer progress: `knowledge/latex/style-variant-index.md` now turns the old style-plan idea into a usable choice between official concise closure, local awarded-paper style, route-heavy analytical style, and evidence-dense research style.

Newest local-template progress: `knowledge/latex/local-template-variant-index.md` now turns the `LATEX/` sample family into a concrete decision aid for template shell choice, density, and compile workflow.

Newest synthesis-layer progress: `knowledge/full-stack-execution-map.md` now ties the route, archetype, method, section, and quality bridges into one shortest path from problem signal to review-ready draft.

Newest source-layer progress: `inventory/source-absorption-matrix.md` now maps raw source buckets to the structured notes they have already become and the next conversion targets that are still thin.

Newest iteration-layer progress: `knowledge/cumcm/next-iteration-action-matrix.md` now turns roadmap items into concrete work items with evidence and follow-up decisions.

Newest objective-layer progress: `docs/objective-coverage-matrix.md` now maps the original long-term goal to the evidence already present in the repo and the gaps that still deserve work.
Newest v1.2-guidance progress: the repository now has route-specific `demo-bundles`, `claim-map` notes, `caption-map` notes, and `review-case-examples`. Together these turn the v1.2 path from a rule stack into a stronger route package covering planning shape, section drafting, paper assembly, abstract/conclusion evidence boundaries, caption/interpretation patterns, and realistic `Needs revision` review tone.

## Completed Deep Reads

| Sample | Route learned | Output |
| --- | --- | --- |
| User awarded paper `LATEX/model1.pdf` | complete LaTeX paper structure | `knowledge/latex/model1-case-study.md` |
| 2021 D017 | online scheduling and industrial adjustment | `knowledge/cumcm/deep-reading-2021D017.md` |
| 2021 A028 | geometry and engineering mechanics | `knowledge/cumcm/deep-reading-2021A028.md` |
| 2021 C066 | supply-chain evaluation and planning | `knowledge/cumcm/deep-reading-2021C066.md` |
| 2022 E014 | conservative production scheduling with service-level-first rolling rules | `knowledge/cumcm/deep-reading-2022E014.md` |
| 2023 C050 | dynamic pricing and supply-chain bridge | `knowledge/cumcm/deep-reading-2023C050.md` |
| 2023 D039 | spatial optimization and cycle planning | `knowledge/cumcm/deep-reading-2023D039.md` |
| 2022 E029 | production planning via demand forecasting, service level, and rolling inventory logic | `knowledge/cumcm/deep-reading-2022E029.md` |
| 2023 E176 | monitoring design, hydrology analysis, and forecast-to-decision chaining | `knowledge/cumcm/deep-reading-2023E176.md` |

## Strong Entry Points

Read these first for generation/review tasks:

1. `knowledge/README.md`
2. `knowledge/learning-status.md`
3. `docs/project-audit-2026-07-06.md`
4. `knowledge/cumcm/paper-generation-playbook.md`
5. `knowledge/cumcm/20-30-page-paper-blueprint.md`
6. `knowledge/cumcm/problem-type-paper-archetypes.md`
7. `knowledge/algorithms/model-chain-patterns.md`
8. `knowledge/algorithms/cards/README.md`
9. `docs/visual-generation-pipeline.md`
10. `knowledge/latex/section-writing-patterns.md`
11. `prompts/06_quality_review.md`
12. `knowledge/quality/quality-rubric-v2.md`
13. `knowledge/quality/mathorcup-2023B-v1-test-review.md`
14. `docs/current-state-matrix-2026-07-07.md`

## Next Reading Queue

Next P0 papers:

1. `monitoring-route demo scaffold`: prepare a future demo path for hydrology/monitoring style E papers.
2. `production-route realism lift`: replace more synthetic assumptions in the current production-route demo with stronger scenario tension or attachment-like inputs.
3. `recent-draft risk reading`: compare 2024 complete drafts against official concise styles to extract generator-risk patterns.

## v1.0 Demo Baseline

The first small closed-loop demo exists and has been compiled/reviewed:

- clone-ready entry: `START_HERE.md`
- repository skill: `.codex/skills/cumcm-paper-generator/SKILL.md`
- active-run starter: `scripts/start-current.ps1`
- `docs/v1-runbook.md`
- `problems/demo-v1-supply.md`
- `scripts/run-v1-demo.ps1`
- `src/demo_v1.py`
- generated demo tables: `paper/tables/demo_v1_material_summary.*`, `paper/tables/demo_v1_forecast_check.*`, `paper/tables/demo_v1_production_plan.*`, `paper/tables/demo_v1_service_levels.*`, `paper/tables/demo_v1_scenario_compare.*`
- generated demo figures: `paper/figures/demo_v1_forecast_compare.png`, `paper/figures/demo_v1_service_levels.png`, `paper/figures/demo_v1_scenario_compare.png`
- generated demo summary: `runs/v1-demo/demo-v1-summary.md`
- demo artifact ledger: `runs/v1-demo/artifact-ledger.md`
- demo review: `reviews/review-v1-demo.md`
- compiled PDF: `paper/main.pdf` (ignored by Git)

Do not treat this as final paper quality. It proves the loop; the next work is expansion, packaging, and stronger examples.

## Next Engineering Queue

1. Add automated checks for additional problem types beyond Type I rail/timetable cases.
2. Add a monitoring-route E demo so the new E-family split is exercised on both sides.
3. Add real attachment parsing and OD assignment to the rail route.
4. Expand the compact rail demo toward a 20-30 page example only after adding real attachment parsing, OD assignment, and fleet/turnback constraints.
5. Expand generated papers toward 20-30 pages by requiring each subproblem to include model construction, algorithm, result table/figure, and validation.
6. Improve Chinese figure/table polish: Chinese labels, readable axes, richer captions, and method-specific references.
7. Build one fuller v1.2 example run package that ties a realistic run scaffold to a near-complete paper draft and review output.

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

Monitoring/data-analysis route:

- show the data-cleaning and aggregation path before modeling;
- give each subproblem one clear method family and one result loop;
- use descriptive, test-based, and scale-based evidence together for periodicity and abruptness;
- connect forecasting outputs to a decision model instead of stopping at prediction;
- keep mixed-tool appendices traceable by question and by artifact role.

E-route family split:

- production-route E papers center on prediction to inventory/service-level or scheduling decisions;
- monitoring-route E papers center on diagnosis to monitoring or policy decisions;
- both need a visible action layer after forecasting, but their figures, tables, and appendix evidence differ.
- current production-route anchors: `2022 E014` and `2022 E029`;
- current monitoring-route anchor: `2023 E176`.
- shared generator docs updated: `knowledge/cumcm/problem-type-paper-archetypes.md`, `knowledge/cumcm/20-30-page-paper-blueprint.md`, and `knowledge/quality/quality-rubric-v2.md`.
- shared entry docs updated: `knowledge/cumcm/paper-generation-playbook.md`, `prompts/01_ideation.md`, `prompts/02_model_plan.md`, `prompts/04_writing.md`, and `prompts/06_quality_review.md`.
- new same-problem comparison note: `knowledge/cumcm/2021C-comparison-C066-C085-C169-C283.md`.
- new same-problem comparison note: `knowledge/cumcm/2021D-comparison-D017-D026-D034.md`.
- new modern-draft risk note: `knowledge/cumcm/2024B-modern-draft-risk-reading.md`.
- new modern-draft risk note: `knowledge/cumcm/2024C-modern-draft-risk-reading.md`.
- new modern-draft risk note: `knowledge/cumcm/2024D-modern-draft-risk-reading.md`.
- newest D-route lesson: physics/probability papers need geometry diagrams, distribution traceability, numeric closure, code provenance, effective body-page counting, and reference relevance checks.
- new modern-draft risk note: `knowledge/cumcm/2024E-modern-draft-risk-reading.md`.
- newest E-route lesson: traffic-control papers need road-network figures, a stable question map, method-to-output linkage, before-after policy evaluation, and code coverage beyond preprocessing screenshots.
- new synthesis note: `knowledge/cumcm/official-style-vs-modern-draft-risk.md`.
- new synthesis note: `knowledge/cumcm/official-paper-paradigms.md`.
- new synthesis bridge: `knowledge/cumcm/generation-loop.md`.
- new synthesis matrix: `knowledge/cumcm/paper-family-matrix.md`.
- new quality gate: `knowledge/quality/completion-gate.md`.
- new master map: `knowledge/master-map.md`.
- new comparison index: `knowledge/cumcm/comparison-index.md`.
- new algorithm method-family index: `knowledge/algorithms/method-family-index.md`.
- new prompt flow map: `prompts/flow-map.md`.
- new visual family index: `knowledge/latex/visual-family-index.md`.
- new table family index: `knowledge/latex/table-family-index.md`.
- new equation family index: `knowledge/latex/equation-family-index.md`.
- new roadmap: `knowledge/roadmap.md`.
- new evidence family index: `knowledge/quality/evidence-family-index.md`.
- new review finding index: `knowledge/quality/review-finding-index.md`.
- new official paper index: `knowledge/cumcm/official-paper-index.md`.
- new deep-reading index: `knowledge/cumcm/deep-reading-index.md`.
- new route example matrix: `knowledge/cumcm/route-example-matrix.md`.
- new run-start checklist: `docs/run-start-checklist.md`.
- new launch prompt: `prompts/07_launch.md`.
- new section family index: `knowledge/latex/section-family-index.md`.
- new route-method matrix: `knowledge/algorithms/route-method-matrix.md`.
- new finding-gate matrix: `knowledge/quality/finding-gate-matrix.md`.
- new archetype-section matrix: `knowledge/cumcm/archetype-section-matrix.md`.
- new archetype-page-density matrix: `knowledge/cumcm/archetype-page-density-matrix.md`.
- new style-variant index: `knowledge/latex/style-variant-index.md`.
- new full-stack execution map: `knowledge/full-stack-execution-map.md`.
- new source absorption matrix: `inventory/source-absorption-matrix.md`.
- new next-iteration action matrix: `knowledge/cumcm/next-iteration-action-matrix.md`.
- new run artifact index: `docs/run-artifact-index.md`.
- new learning-status panel: `knowledge/learning-status.md`.
- newest cross-cutting lesson: the generator should imitate official concise closure and use 2024 draft readings mainly as fake-completion risk gates.
- review standards updated: `knowledge/quality/quality-rubric-v2.md` and `docs/review-checklist.md` now explicitly check stable question mapping, effective body length, object-first figures, and the difference between reproducible results and screenshot-only evidence.
- new atlas index: `knowledge/cumcm/cumcm-atlas.md` now links problem types, algorithm cards, LaTeX rules, quality gates, and next-step iteration planning.
- new algorithm doorway: `knowledge/algorithms/README.md` now gives the generator a stable path from problem signal to route family to detailed method cards.
- new LaTeX doorway: `knowledge/latex/README.md` now gives the generator a stable path from section contract to writing patterns to figure/table/equation style.
- new LaTeX local-template bridge: `knowledge/latex/local-template-variant-index.md` now captures the local template family cues from `model1.tex`, `document.tex`, and the adjacent 2024 template bucket.
- new prompt doorway: `prompts/README.md` now gives the generator a stable path from intake through quality audit.
- new CUMCM doorway: `knowledge/cumcm/README.md` now gives the generator a stable path from atlas to paradigms to risk notes.
- new docs doorway: `docs/README.md` now gives the project a stable path from runbook to review, state, and roadmap files.
- new quality doorway: `knowledge/quality/README.md` now gives the generator a stable path from rubric to reproducibility to review notes.
- classification route anchor: `knowledge/cumcm/deep-reading-2021E014.md` now sits in the top route list for spectral and high-dimensional signal classification.
- classification method anchor: `knowledge/algorithms/cumcm-routing-rules.md` and `knowledge/algorithms/problem-type-to-method.md` now point spectral classification work toward preprocessing, feature reduction, and classifier comparison.
- E-route method anchors: `knowledge/algorithms/cumcm-routing-rules.md`, `knowledge/cumcm/problem-type-paper-archetypes.md`, and `knowledge/algorithms/cards/README.md` now distinguish production-route E from monitoring-route E at the route and card level.
- `START_HERE.md` now has a one-screen navigation map for the six doorway files and the runbook.
- `inventory/README.md` now gives the project a compact source-coverage ledger for what has been absorbed and what still needs tracking.
- `inventory/source-map.md` now maps the local source buckets to the structured notes that absorb them.
- `docs/architecture.md` now gives the project a short architecture map for the closed-loop paper-generation system.
- new execution plan: `knowledge/cumcm/next-iteration-plan.md` now names the next experiments and their success criteria.
- `docs/v1-runbook.md` now points the fresh-run path at the atlas and next-iteration plan before the old step-by-step scaffold.
- `knowledge/learning-status.md` now gives the project a compact absorb/queue panel for long-term maintenance.

## Git State Rule

Before stopping a work block:

1. run a status check;
2. commit local progress if coherent;
3. do not push unless daily sync is due or user asks;
4. update this file when the next best action changes.
