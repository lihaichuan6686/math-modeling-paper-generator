# Knowledge Coverage Audit v1.6

Purpose: audit the long-term objective against current repository evidence so future work does not drift into endless polishing.

Long-term objective:

```text
systematically absorb local mathematical-modeling resources, prioritize CUMCM, and build a long-term agent knowledge base covering excellent-paper paradigms, algorithm/problem-type indexes, LaTeX writing norms, and iteration plans.
```

## Coverage Matrix

| Objective area | Current evidence | Coverage state | Main gap | Next durable output |
|---|---|---|---|---|
| Local CUMCM materials | `knowledge/cumcm/*`, `recent-award-paper-visual-rhythm.md`, `v1-6-award-paper-quantity-calibration.md`, local awarded-paper structure notes | strong but still sample-limited | exact section/reference/figure counts remain weak for scanned PDFs | OCR/manual sampling pack for 2021-2023 samples |
| Excellent-paper paradigms | `local-awarded-paper-structure-rules.md`, `official-paper-paradigms.md`, `archetype-section-matrix.md`, `v1-6-section-rhythm-soft-metrics.md` | strong for paper feel and page rhythm | more same-problem comparisons needed outside current anchor families | one new same-problem comparison note per common family |
| Algorithm and problem-type index | `national-problem-family-methodology-matrix.md`, `v1-5-route-upgrade-atlas.md`, `v1-6-method-chain-evidence-index.md`, algorithm cards | strong for route selection | several niche recurring families still have shallow card support | v1.6 family calibration packs and missing-card list |
| LaTeX writing and layout norms | `cumcm_v16_main.tex`, `v1-6-layout-rhythm-rules.md`, `v1-6-award-paper-quantity-calibration.md`, `v1-6-layout-hard-gates.md`, `table-safe-snippets.tex`, final check script | strong for static handoff | generated PDFs still need real visual-test feedback and table/figure false-negative tuning | user-side v1.6 test triage and checker repair log |
| Visual generation workflow | `v1-6-nature-style-figure-rules.md`, `v1-6-visual-generation-decision.md`, `visual-generation-pipeline.md` | medium-strong for decision policy | actual high-quality concept-figure helper remains unproven | v1.6 visual helper prototype or documented external workflow |
| Community and soft rules | `v1-5-local-experience-soft-rules.md`, `v1-6-excellent-paper-reader-lens.md`, public source playbook, online-consensus protocol | medium-strong | older `.doc` and `.ppt` files remain partially blocked; public examples are still sparse; more reader-lens samples are needed across problem families | extraction status update and two filled public-signal examples |
| Iteration plan | v1.4/v1.5/v1.6 release, feedback, and triage files | strong up to v1.6 | current plan files do not yet name v1.6 calibration priorities | `docs/v1.6-calibration-roadmap.md` |

## What Is Now Reliable Enough

- Claude can start from a v1.6 launch prompt without reading the whole repository.
- New runs scaffold planning files for title, method depth, section rhythm, figure style, artifacts, and review.
- Route selection now requires support diagnosis, main model, result artifact, validation artifact, and paper-visible highlight.
- LaTeX handoff now has both static checks and a final check wrapper.
- The knowledge base has moved beyond a single demo route into reusable families.

## What Is Not Yet Proven

- v1.6 has not been proven by enough fresh user-side generated PDFs.
- Exact numerical norms for section word count, reference count, and figure/table count remain approximate because many local PDFs are scanned, watermarked, or extraction-hostile.
- Nature-style concept figures are specified, but the repository does not yet include a robust generation helper that consistently produces that visual quality.
- Public community research has safe protocols, but not enough filled examples across platforms and problem types.

## Evidence Standard For Future Completion

Do not claim this long-term objective is complete until the repository has:

- a coverage audit updated after at least one v1.6 user-side test;
- at least three family calibration packs from fresh or held-out problems;
- at least one same-problem comparison outside the already heavily used anchors;
- a stronger visual-generation helper or a clearly documented external-image workflow;
- a static check that proves v1.6 entry files, route evidence, layout gates, and final-check handoff remain wired together;
- a roadmap showing what remains for v2.0 rather than only v1.x repairs.

## Maintenance Rule

When adding new knowledge, always convert it into one of:

- route evidence rule;
- section rhythm rule;
- visual/table rule;
- quality gate;
- prompt instruction;
- scaffold field;
- or test feedback triage item.

Raw reading notes are not enough unless they change future agent behavior.
