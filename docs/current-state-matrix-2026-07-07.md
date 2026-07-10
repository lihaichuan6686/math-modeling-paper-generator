# Current State Matrix: 2026-07-07

Purpose: keep the long-running paper-generator project honest about what is actually done, what is verified, and what still needs deeper work.

## Objective Coverage

| Objective item | Status | Evidence | Notes |
|---|---|---|---|
| Long-term CUMCM knowledge base | Pass | `knowledge/README.md`, `knowledge/cumcm/*`, `knowledge/algorithms/*`, `knowledge/latex/*`, `knowledge/quality/*` | The repository now has structured entry points for generation, review, and style. |
| Excellent-paper范式 | Pass | `knowledge/cumcm/problem-type-paper-archetypes.md`, `knowledge/cumcm/20-30-page-paper-blueprint.md`, `knowledge/latex/section-writing-patterns.md` | Rail-timetable and other route archetypes are encoded as reusable contracts. |
| Algorithm /题型索引 | Pass | `knowledge/algorithms/cards/README.md`, `knowledge/algorithms/cards/rail-timetable-operation.md`, `knowledge/algorithms/model-chain-patterns.md` | Type I rail/timetable now has a dedicated card and review gate. |
| LaTeX writing规范 | Pass | `knowledge/latex/cumcm-section-contract.md`, `knowledge/latex/figures-tables-equations-style.md`, `paper/rail_demo.tex` | The compact rail demo compiles and uses generated tables/figures. |
| 后续迭代计划 | Pass | `docs/continuation-state.md`, `docs/v1-runbook.md` | The next steps are written as concrete routes rather than vague cleanup. |
| 真实 demo pipeline | Pass | `src/demo_v1.py`, `scripts/run-v1-demo.ps1`, `paper/main.tex`, `runs/v1-demo/*` | v1 demo generates artifacts and passes the machine gate. |
| 轨道时刻表示例 pipeline | Pass | `src/rail_timetable_demo.py`, `scripts/run-rail-demo.ps1`, `paper/rail_demo.tex`, `runs/rail-demo/*` | Rail demo generates operation plan, timetable, audits, scenario analysis, and compiles. |
| 自动质量门禁 | Pass | `scripts/check-run-quality.py`, `scripts/check-run-quality.ps1`, `docs/review-checklist.md` | Both demo scripts run the gate automatically by default. |
| Private GitHub sync | Pass | Git log and remote push history | Latest sync completed successfully to the private repository. |

## Verified Strengths

- The knowledge base is now organized by generation workflow, problem archetype, algorithm card, LaTeX style, and review rubric.
- The rail timetable case has its own problem-type contract, algorithm card, demo pipeline, and paper entry point.
- The demo scripts produce machine-readable outputs and then run the quality gate automatically.
- The review system now distinguishes placeholder review files from actual evidence-backed reviews.
- The 2023 C050 deep read adds a full retail pricing and replenishment route with statistics, clustering, forecasting, optimization, and practical-factor analysis.
- The 2023 D039 deep read adds a cycle-based spatial/production optimization route with piecewise occupancy logic, fixed-cycle simplification, and stochastic loss analysis.
- The 2023 E176 deep read adds a monitoring and hydrology route with shared data preprocessing, multi-method diagnosis, forecast-to-decision chaining, and support-material traceability.
- The new `knowledge/cumcm/e-route-comparison-2022-2023.md` note separates E-type papers into production-route and monitoring-route families instead of treating E as a single template.
- The 2022 E029 deep read now anchors the production-route E family with ARIMA comparison, safety-stock/service-level reasoning, and rolling production planning.
- The 2022 E014 deep read complements that route with a more conservative service-level-first rolling-rule variant and explicit parameter-band interpretation.
- The new `knowledge/cumcm/2021C-comparison-C066-C085-C169-C283.md` note shows that same-problem supply-chain papers keep a stable evaluation-to-planning backbone while varying their lead rhetoric across uncertainty-led, optimization-led, and heuristic-led styles.
- The new `knowledge/cumcm/2021D-comparison-D017-D026-D034.md` note shows that same-problem online-optimization papers keep a stable baseline-to-abnormal-update backbone while varying across theorem-led, planning-led, and implementation-led writing styles.
- The new `knowledge/cumcm/2024B-modern-draft-risk-reading.md` note shows that 20-30 rendered pages can still hide template placeholders, watermarks, empty code appendices, and unsupported claims; page count must therefore be coupled to evidence and risk gates.
- The new `knowledge/cumcm/2024C-modern-draft-risk-reading.md` note adds a partial-versus-overlong comparison: question coverage, paper-body length, code linkage, and scenario evidence must be audited separately.
- The new `knowledge/cumcm/2024D-modern-draft-risk-reading.md` note adds D-type physics/probability risk checks: coordinate-frame evidence, distribution traceability, formula-to-number closure, code provenance, effective page count, and reference relevance.
- The new `knowledge/cumcm/2024E-modern-draft-risk-reading.md` note adds traffic-control E checks: road-network visualization, stable question mapping, method-to-output linkage, before-after policy evaluation, and code coverage beyond screenshots.
- The new `knowledge/cumcm/official-style-vs-modern-draft-risk.md` synthesis note connects the official excellent-paper readings to the 2024 draft-risk notes, clarifying which signals should be imitated and which should be rejected by the generator.
- The new `knowledge/cumcm/official-paper-paradigms.md` synthesis note turns the official excellent-paper readings into route-family tables, abstract patterns, and generator rules that can be reused directly in prompts and reviews.
- The quality standards layer now reflects those lessons too: `knowledge/quality/quality-rubric-v2.md` and `docs/review-checklist.md` explicitly audit question-map stability, effective body length, object-first figures, and screenshot-versus-evidence risks.
- The new `knowledge/cumcm/cumcm-atlas.md` file acts as the top-level navigation layer for routes, algorithms, LaTeX, risk gates, and next-step iteration planning.
- The new `knowledge/algorithms/README.md` file gives the algorithm layer a stable doorway from problem signal to route family to method cards.
- The new `knowledge/latex/README.md` file gives the LaTeX layer a stable doorway from section contract to writing patterns to figure/table/equation style.
- The new `prompts/README.md` file gives the staged prompt chain a stable doorway from intake through quality audit.
- The new `knowledge/cumcm/README.md` file gives the contest corpus a stable doorway from atlas to paradigms to risk notes.
- The new `docs/README.md` file gives the operational docs a stable doorway from runbook to review, state, and roadmap files.
- The new `knowledge/quality/README.md` file gives the quality corpus a stable doorway from rubric to reproducibility to review notes.
- The new `knowledge/cumcm/next-iteration-plan.md` file turns the atlas into an operational plan: fresh-run validation, same-problem comparison expansion, and LaTeX weak-spot drills.
- `docs/v1-runbook.md` now uses the atlas and next-iteration plan as the first decision layer for fresh runs.
- The new `knowledge/cumcm/next-iteration-plan.md` file turns the atlas into an operational plan: fresh-run validation, same-problem comparison expansion, and LaTeX weak-spot drills.

## Still Open

| Gap | Status | Why it still matters | Next step |
|---|---|---|---|
| Real contest attachment parsing for rail-timetable cases | Open | Current rail demo uses synthetic data, so it is only a structure exemplar. | Replace synthetic inputs with parsed problem attachments when working on a real rail problem. |
| OD assignment and fleet/turnback realism | Open | The current rail demo checks the route chain but simplifies operational realism. | Add OD passenger assignment and vehicle circulation constraints. |
| More problem routes | Open | The knowledge base still benefits from additional deep reads and comparison reading. | Add more same-problem comparisons and then test the strengthened prompts/review gates on a fresh paper run. |
| 20-30 page rail-quality expansion | Open | The current rail demo is a compact paper, not a full contest-quality draft. | Expand only after real-data parsing and richer validation are added. |

## Current Judgment

The project has achieved a usable v1.0 research prototype with a stronger than before maintenance layer.

It has not yet finished the full long-term objective because the knowledge base still needs more route coverage and the rail route still needs real-data and operational realism upgrades before it can be treated as a production-quality contest system.
