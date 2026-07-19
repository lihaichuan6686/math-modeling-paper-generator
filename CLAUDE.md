# Claude Code Instructions

This repository is a research-only mathematical modeling paper generator and paper-quality assistant. It is intended for learning, post-contest review, authorized research, and human-AI writing comparison. Do not use it to support active contest rule violations, hidden AI participation, fabricated experiments, fake citations, or unverifiable claims.

## Current Project State

The project has a working v1.0 closed-loop demo, v1.2/v1.3 methodology layers, a v1.4 contest-feel release, and an emerging v1.5 award-paper-feel hard-gate layer:

```text
problem -> run scaffold -> model plan -> code/table/figure -> v1.5 paper skeleton -> PDF -> hard-gate review
```

Do not restart broad reading before preserving and extending the usable workflow. For v1.5, read the Level 0 files first and load extra references only when needed.

## Read First

For v1.5 generation or review runs, read these Level 0 files first:

- `START_HERE.md`
- `prompts/15_launch_v1_5.md`
- `docs/v1.5-paper-template-contract.md`
- `docs/v1.5-method-route-contract.md`
- `knowledge/latex/v1-5-front-matter-rhythm-rules.md`
- `knowledge/latex/v1-5-award-paper-style-rules.md`
- `knowledge/latex/v1-5-award-paper-visual-fingerprint.md`
- `knowledge/community/v1-5-local-experience-soft-rules.md`
- `knowledge/algorithms/v1-5-route-upgrade-atlas.md`
- `knowledge/quality/v1-5-hard-gates.md`

Then read additional files only when the active problem requires them.

## v1.0 Demo Entry Points

- Demo problem: `problems/demo-v1-supply.md`
- Demo runner: `scripts/run-v1-demo.ps1`
- Demo code: `src/demo_v1.py`
- Demo table: `paper/tables/demo_v1_order_plan.tex`
- Demo figure: `paper/figures/demo_v1_inventory.png`
- Demo ledger: `runs/v1-demo/artifact-ledger.md`
- Demo review: `reviews/review-v1-demo.md`

Use this command for the smoke test:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\run-v1-demo.ps1 -Name v1-demo -Force
```

Then compile with:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\compile.ps1
```

## Playwright MCP Public Research

Use Playwright MCP before final paper writing when public online information is needed.
The project no longer depends on platform-specific Python crawlers, cookies, hidden APIs, ZSE/internal endpoints, or anti-crawling workarounds.

- **Entry**: `docs/playwright-mcp-public-research.md`
- **Prompt**: `prompts/13_platform_research.md`
- **Output**: `runs/current/online-consensus-notes.md`

Core principle: browse public pages like a human reviewer, record access limits, do not copy answers, and do not bypass login walls.

## Operating Boundaries

1. Read `problems/problem.md` or the specified problem file.
2. Create or update a run scaffold under `runs/`.
3. Produce `problem-analysis.md`, `model-candidates.md`, and `model-plan.md`; include `Data Traps` in the data inventory.
4. Select a model chain from the CUMCM knowledge base and algorithm cards; for v1.5, use `docs/v1.5-method-route-contract.md` and `knowledge/algorithms/v1-5-route-upgrade-atlas.md` before locking `method-depth-plan.md`.
5. Public research: use Playwright MCP to browse public pages for community signals, common interpretations, traps, and rough result ranges. Write the first public-research draft to `runs/current/online-consensus-notes.md`. Use `prompts/13_platform_research.md`, then use `prompts/11_online_consensus_check.md` to review and complete the same file.
6. Implement reproducible code under `src/`.
7. Generate tables under `paper/tables/` and figures under `paper/figures/`.
8. For v1.5, create `runs/current/title-candidates.md`, then copy or mirror `paper/templates/cumcm_v15_main.tex` before writing `paper/main.tex`.
9. Compile `paper/main.tex`.
10. Render and visually inspect important PDF pages.
11. For v1.5, run `scripts/check-v1.5-pdf.ps1` after `paper/main.pdf` exists and read `reviews/pdf-v15-check.md`.
12. Record traceability in the artifact ledger.
13. Record issues and final status in `reviews/`, including `v1.5 Hard Gate Verdict` for v1.5.
14. After user-side testing, record visible failures with `docs/v1.5-user-test-feedback-template.md` and map repairs with `docs/v1.5-feedback-triage-matrix.md`.

## Paper Expectations

A complete CUMCM-style paper should include:

- contest-style title rather than a bare task label;
- recorded title candidates before the final title is selected;
- route depth plan with result and validation artifacts for each central subquestion;
- paragraph-structured abstract with method and bold result highlights;
- problem restatement;
- problem analysis;
- early concept/mechanism/model-flow figure when supported;
- assumptions;
- symbols;
- data preprocessing;
- model establishment;
- solution process;
- results;
- validation and sensitivity analysis;
- strengths and limitations;
- conclusion;
- references;
- appendix or code inventory when appropriate.

For the eventual 20-30 page target, length must come from real structure: formulas, model explanation, generated figures, tables, validation, and appendices. Do not pad with generic filler.

## Figure and Table Rules

- Every figure and table must have a stable source path, caption, paper label, and ledger entry.
- Evidence figures must be generated from data or code, not from decorative image generation.
- AI-generated images are allowed only for explanatory schematics or review artifacts, and the prompt/source must be recorded.
- Figures must be visually inspected in the rendered PDF.
- Captions should explain what the reader should learn, not merely repeat the filename.
- v1.5 figures must be paper-ready: readable axes, Chinese captions, no default notebook titles, and no impossible values used as evidence.

## Review Rules

A run is not complete until:

- the PDF compiles;
- generated figures and tables appear in the rendered PDF;
- key abstract/conclusion claims are listed in the artifact ledger;
- code outputs match paper claims;
- review status is `Pass` or `Needs revision with explicit open items`;
- responsible-use limitations are recorded.
- for v1.5, every gate in `knowledge/quality/v1-5-hard-gates.md` has a pass/fail verdict and failed gates block handoff.
- for v1.5, `reviews/review-current.md` includes `Method Route Verdict`.
- for v1.5, `reviews/pdf-v15-check.md` exists when a PDF exists, and any `FAIL` item blocks handoff.

## Near-Term Priorities

1. Deliver v1.5 hard gates that prevent AI-report-looking papers from being handed off.
2. Make the paper skeleton, title, abstract, concept figure, appendix code, and PDF review mandatory.
3. Use user-side tests to repair specific failed gates instead of broad open-ended polishing.
4. Route every disappointing generated paper through the v1.5 feedback template and triage matrix before adding new rules.
