# Claude Code Instructions

This repository is a research-only mathematical modeling paper generator and paper-quality assistant. It is intended for learning, post-contest review, authorized research, and human-AI writing comparison. Do not use it to support active contest rule violations, hidden AI participation, fabricated experiments, fake citations, or unverifiable claims.

## Current Project State

The project now has a v1.0 closed-loop demo:

```text
problem -> run scaffold -> model plan -> code/table/figure -> LaTeX draft -> PDF -> review
```

The demo is intentionally small, but it proves the chain works. Do not restart broad reading before preserving and extending this usable workflow.

## Read First

For every generation or review run, read these files first:

- `docs/v1-runbook.md`
- `docs/continuation-state.md`
- `knowledge/README.md`
- `prompts/README.md`
- `knowledge/cumcm/paper-generation-playbook.md`
- `knowledge/cumcm/20-30-page-paper-blueprint.md`
- `knowledge/cumcm/problem-type-paper-archetypes.md`
- `knowledge/algorithms/cumcm-routing-rules.md`
- `knowledge/algorithms/cards/README.md`
- `knowledge/algorithms/model-chain-patterns.md`
- `docs/visual-generation-pipeline.md`
- `docs/review-checklist.md`
- `docs/artifact-ledger-template.md`
- `docs/figure-plan-template.md`
- `knowledge/quality/reproducibility-and-ai-difference-framework.md`
- `knowledge/quality/quality-rubric-v2.md`
- `knowledge/latex/cumcm-section-contract.md`
- `knowledge/latex/section-writing-patterns.md`
- `knowledge/latex/figures-tables-equations-style.md`
- `knowledge/latex/snippets.md`

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

## Operating Boundaries

- Serve only learning, post-contest review, course research, authorized research, and writing-method experiments.
- Refuse requests for active contest cheating, hidden AI participation, fabricated data, fabricated citations, or disguised AI authorship.
- Do not invent data sources, citations, experimental results, theorem origins, or certainty.
- Keep code, figures, tables, and conclusions reproducible.
- Clearly mark synthetic or demonstration data as synthetic.

## Standard Workflow

1. Read `problems/problem.md` or the specified problem file.
2. Create or update a run scaffold under `runs/`.
3. Produce `problem-analysis.md`, `model-candidates.md`, and `model-plan.md`.
4. Select a model chain from the CUMCM knowledge base and algorithm cards.
5. Implement reproducible code under `src/`.
6. Generate tables under `paper/tables/` and figures under `paper/figures/`.
7. Write or update `paper/sections/`.
8. Compile `paper/main.tex`.
9. Render and visually inspect important PDF pages.
10. Record traceability in the artifact ledger.
11. Record issues and final status in `reviews/`.

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

1. Expand the v1-demo from a 6-page smoke test toward a full-length 20-30 page research draft.
2. Package the runbook into a Claude Code skill-style workflow.
3. Add a stronger CUMCM-style optimization/classification example.
4. Resume deep reading, starting with `2021 E014` for the spectral/classification route.
5. Convert the review checklist into a stricter reusable review prompt or script.
