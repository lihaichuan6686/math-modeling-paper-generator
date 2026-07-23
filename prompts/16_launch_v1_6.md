# Launch Prompt v1.6

Use this when the goal is to produce a v1.6 layout-stable, visually credible CUMCM-style draft.

v1.6 builds on v1.5. It does not primarily add more methods; it controls page rhythm, layout, figure quality, table safety, and final self-review.

```text
You are working in a research-only mathematical modeling paper generator.

Target: v1.6 layout-and-visual-gated draft.

Responsible-use boundary:
- use this only for learning, post-contest review, authorized research, and paper-quality checking;
- do not copy online answers, paid materials, private materials, or full solution text;
- do not fabricate data, experiments, citations, code outputs, or certainty.

Level 0 required reading:
- START_HERE.md
- docs/v1.6-design-plan.md
- docs/v1.6-paper-template-contract.md
- docs/v1.5-method-route-contract.md
- knowledge/cumcm/v1-6-route-to-paper-structure-index.md
- knowledge/cumcm/v1-6-family-calibration-priority.md
- knowledge/algorithms/v1-6-method-chain-evidence-index.md
- knowledge/latex/v1-6-layout-rhythm-rules.md
- knowledge/latex/v1-6-section-rhythm-soft-metrics.md
- knowledge/latex/v1-6-award-feel-soft-rules.md
- knowledge/latex/v1-6-reference-and-citation-rhythm.md
- knowledge/latex/v1-6-award-paper-quantity-calibration.md
- knowledge/community/v1-6-excellent-paper-reader-lens.md
- knowledge/visuals/v1-6-nature-style-figure-rules.md
- knowledge/quality/v1-5-hard-gates.md
- knowledge/quality/v1-6-layout-hard-gates.md
- memory/v15-paper-generation-feedback.md
- prompts/16_launch_v1_6.md

Then read only as needed:
- knowledge/latex/v1-5-front-matter-rhythm-rules.md
- knowledge/latex/v1-5-award-paper-style-rules.md
- knowledge/latex/v1-5-award-paper-visual-fingerprint.md
- knowledge/community/v1-5-local-experience-soft-rules.md
- knowledge/algorithms/v1-5-route-upgrade-atlas.md
- knowledge/cumcm/recent-award-paper-visual-rhythm.md
- knowledge/latex/national-problem-family-visual-matrix.md
- knowledge/visuals/v1-6-visual-generation-decision.md

Before writing:
1. Create or refresh the run scaffold.
2. Run `scripts/check-env.ps1`; if it fails, run `scripts/setup.ps1` once and reuse `.venv\Scripts\python.exe`.
3. Build problem-analysis.md with Data Traps and route choice.
4. Build method-depth-plan.md with support diagnosis, main model, result artifacts, validation artifacts, and paper-visible highlights.
5. Build route-decision.md from `v1-6-route-to-paper-structure-index.md` and `v1-6-family-calibration-priority.md`; record the priority family and the most likely non-human failure.
6. Build section-rhythm-budget.md using v1.6 page rhythm targets and section soft metrics.
6a. Classify the draft target as early-test, v1.6 handoff, stronger award-feel, or heavy-evidence before locking the page budget.
7. Build figure-style-spec.md for the early concept/mechanism figure.
8. Build title-candidates.md with five contest-style titles and a selected title.
9. Plan table widths before writing wide tables.
10. Build award-feel-checklist.md from `v1-6-award-feel-soft-rules.md`.
11. Keep artifact-ledger.md synchronized with every generated figure, table, code run, and key result.

Execution requirements:
- Keep the full paper in the 26-32 page target range unless the review justifies an exception.
- Use quantity calibration: 20-25 pages is an early-test warning band, 26-32 pages is the v1.6 handoff band, and 33-45 pages is often closer to stronger award-paper feel when evidence supports it.
- Page one should contain 900-1150 extracted characters and visually fill the abstract page without spilling.
- Use a structured abstract: opening route, `閽堝绗竴闂?绗簩闂?...`, concrete results, closing value, keywords.
- Select a contest-style title that names the object, modeling action, decision target, and strongest method signal.
- Do not write section headings with ASCII hyphens.
- Do not write thin skeleton sections. Meet first-draft density while writing.
- Use the excellent-paper reader lens: each section must have a visible duty, an evidence-bearing contribution, and at least one reader-facing repair when it feels ceremonial.
- For every central subquestion, plan a route-choice, model, result artifact, interpretation, and validation or limitation loop before drafting.
- Use family calibration priority to avoid overfitting a rare topic; prefer broad failures such as ranking-without-plan, forecast-without-decision, classifier-without-rule, or geometry-without-object.
- Reject method chains that name algorithms but cannot produce a body result artifact and a validation artifact.
- Add one early Nature-style concept/mechanism figure in the first six pages.
- Decide each figure's generation path: code evidence, code-native schematic, or externally polished schematic; never use image generation for numeric evidence.
- Generate figures with readable Chinese labels and non-default titles.
- Use `tabularx`, `adjustbox`, or fixed-width `p{}` columns for wide text tables, script indexes, and path tables.
- Do not leave symbol/assumption pages mostly blank; merge or compact them when needed.
- Treat table overflow, unreadable figure text, or severe overfull boxes as handoff blockers.
- Include appendix code or a script index, but do not let appendix inflate the page count.
- Keep references useful: prefer 8-15 role-bearing references when sources support it, cite them near method/data/domain/validation claims, and remove decorative bibliography items.

After paper/main.pdf exists:
1. Run the final v1.6 gate with `scripts/check-v1.6-final.ps1`.
2. Read `reviews/final-v16-check.md`, `reviews/pdf-v15-check.md`, and `reviews/layout-v16-check.md`.
3. If a child report fails, repair the source and rerun the final check.
4. Repair all FAIL items.
5. Fill `v1.5 Hard Gate Verdict`, `Method Route Verdict`, and `v1.6 Layout Gate Verdict` in the final review.

Minimum expected outputs:
- runs/current/problem-analysis.md
- runs/current/data-inventory.md with Data Traps
- runs/current/method-depth-plan.md
- runs/current/section-rhythm-budget.md
- runs/current/figure-style-spec.md
- runs/current/concept-figure-spec.json
- runs/current/award-feel-checklist.md
- runs/current/figure-plan.md
- runs/current/title-candidates.md
- runs/current/artifact-ledger.md
- paper/main.tex
- paper/main.tex should be copied from or mirror `paper/templates/cumcm_v16_main.tex`
- paper/main.pdf when local LaTeX is available
- reviews/final-v16-check.md
- reviews/pdf-v15-check.md
- reviews/layout-v16-check.md
- reviews/review-current.md with v1.6 Layout Gate Verdict

Do not hand off merely because the PDF compiled.
```
