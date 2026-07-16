# Claude Code Instructions

This repository is a research-only mathematical modeling paper generator and paper-quality assistant. It is intended for learning, post-contest review, authorized research, and human-AI writing comparison. Do not use it to support active contest rule violations, hidden AI participation, fabricated experiments, fake citations, or unverifiable claims.

## Current Project State

The project now has a working v1.0 closed-loop demo and is actively upgrading toward a v1.2 human-team-style paper workflow:

```text
problem -> run scaffold -> model plan -> code/table/figure -> LaTeX draft -> PDF -> review
```

The demo is intentionally small, but it proves the chain works. Do not restart broad reading before preserving and extending this usable workflow.

## Read First

For every generation or review run, read these files first:

- `docs/v1.2-runbook.md`
- `docs/v1-runbook.md`
- `docs/run-start-checklist.md`
- `docs/continuation-state.md`
- `knowledge/README.md`
- `knowledge/cumcm/README.md`
- `prompts/README.md`
- `prompts/07_launch.md`
- `docs/README.md`
- `inventory/README.md`
- `docs/architecture.md`
- `knowledge/quality/README.md`
- `knowledge/cumcm/paper-generation-playbook.md`
- `knowledge/cumcm/20-30-page-paper-blueprint.md`
- `knowledge/cumcm/problem-type-paper-archetypes.md`
- `knowledge/algorithms/cumcm-routing-rules.md`
- `knowledge/algorithms/cards/README.md`
- `knowledge/algorithms/model-chain-patterns.md`
- `knowledge/algorithms/method-depth-ladder.md`
- `docs/visual-generation-pipeline.md`
- `docs/review-checklist.md`
- `docs/artifact-ledger-template.md`
- `docs/figure-plan-template.md`
- `knowledge/quality/reproducibility-and-ai-difference-framework.md`
- `knowledge/quality/quality-rubric-v2.md`
- `docs/v1.2-draft-contract.md`
- `knowledge/latex/cumcm-section-contract.md`
- `knowledge/latex/section-writing-patterns.md`
- `knowledge/latex/human-style-soft-rules.md`
- `knowledge/latex/figures-tables-equations-style.md`
- `knowledge/latex/snippets.md`
- `docs/playwright-mcp-public-research.md`

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
3. Produce `problem-analysis.md`, `model-candidates.md`, and `model-plan.md`.
4. Select a model chain from the CUMCM knowledge base and algorithm cards.
5. Public research: use Playwright MCP to browse public pages for community signals, common interpretations, traps, and rough result ranges. Write the first public-research draft to `runs/current/online-consensus-notes.md`. Use `prompts/13_platform_research.md`, then use `prompts/11_online_consensus_check.md` to review and complete the same file.
6. Implement reproducible code under `src/`.
7. Generate tables under `paper/tables/` and figures under `paper/figures/`.
8. Write or update `paper/sections/`.
9. Compile `paper/main.tex`.
10. Render and visually inspect important PDF pages.
11. Record traceability in the artifact ledger.
12. Record issues and final status in `reviews/`.

## Paper Expectations

A complete CUMCM-style paper should include:

- abstract with method and result highlights;
- problem restatement;
- problem analysis;
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

## Review Rules

A run is not complete until:

- the PDF compiles;
- generated figures and tables appear in the rendered PDF;
- key abstract/conclusion claims are listed in the artifact ledger;
- code outputs match paper claims;
- review status is `Pass` or `Needs revision with explicit open items`;
- responsible-use limitations are recorded.

## Near-Term Priorities

1. Deliver a v1.2 paper path that repairs thin prose, weak section density, and shallow method chains.
2. Expand the active draft path from small-demo shape toward a full-length 20-30 page research draft.
3. Add stronger route-specific comparison notes and contest-style writing soft rules.
4. Add a stronger CUMCM-style optimization/classification example.
5. Convert the review checklist into a stricter reusable review prompt or script.
