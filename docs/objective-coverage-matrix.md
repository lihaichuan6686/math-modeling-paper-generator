# Objective Coverage Matrix

Purpose: map the original long-term goal to the knowledge base, runbook, prompt, and quality layers that now support it.

This is a living coverage sheet. It is meant to show what is already strong, what is still partial, and what the next concrete gap is.

## Coverage Legend

- `Covered`: the repo already has a usable bridge for this need.
- `Mostly covered`: the bridge exists, but it still needs more examples, polish, or edge-case hardening.
- `Partial`: the idea is present, but the path is not yet reliable enough for unattended use.
- `Gap`: the work has not yet been grounded in a stable file or workflow.

## Objective-to-Evidence Map

| Objective part | Current evidence | Status | Remaining gap | Next move |
| --- | --- | --- | --- | --- |
| Long-term maintainable project | `knowledge/README.md`, `docs/README.md`, `knowledge/learning-status.md`, `docs/continuation-state.md`, `knowledge/master-map.md`, `knowledge/full-stack-execution-map.md` | Covered | Keep the maintenance panels short and current | Update the state files when the next strong bridge lands |
| Claude Code can use it directly | `START_HERE.md`, `docs/run-start-checklist.md`, `prompts/07_launch.md`, `docs/v1-runbook.md`, `scripts/start-current.ps1` | Mostly covered | The entry path is usable, but still benefits from more real run examples | Keep tightening the first-run path and add more run transcripts |
| The model can ideate, plan, write, code, draw, lay out LaTeX, and self-review | `prompts/00_intake.md` through `prompts/06_quality_review.md`, `prompts/flow-map.md`, `docs/visual-generation-pipeline.md`, `docs/figure-plan-template.md`, `docs/artifact-ledger-template.md`, `docs/review-checklist.md`, `knowledge/quality/completion-gate.md` | Mostly covered | The loop exists, but it needs more end-to-end examples and better failure repair | Keep expanding the demo path and review evidence |
| The output should become a full 20-30 page paper | `knowledge/cumcm/20-30-page-paper-blueprint.md`, `knowledge/cumcm/archetype-page-density-matrix.md`, `knowledge/latex/style-variant-index.md`, `knowledge/latex/section-family-index.md`, `knowledge/cumcm/paper-family-matrix.md` | Mostly covered | Page budgeting is defined, but needs more route-specific proof | Add more complete sample structures and page-density examples |
| The tool should learn and absorb the local competition materials deeply | `inventory/README.md`, `inventory/source-map.md`, `inventory/source-absorption-matrix.md`, `knowledge/cumcm/deep-reading-index.md`, `knowledge/cumcm/comparison-index.md`, `knowledge/cumcm/official-paper-index.md` | Mostly covered | More official excellent papers and comparison notes still need to be converted into structured knowledge | Keep turning important sources into route rules, cards, and indices |
| Figures are essential and must join the pipeline | `docs/visual-generation-pipeline.md`, `docs/figure-plan-template.md`, `knowledge/latex/visual-family-index.md`, `knowledge/latex/figures-tables-equations-style.md`, generated demo figures in `paper/figures/` | Covered | Need more contest-style figure conventions and better captions/labels | Expand figure role notes by route family |
| LaTeX paper writing must be complete and reusable | `knowledge/latex/cumcm-section-contract.md`, `knowledge/latex/section-writing-patterns.md`, `knowledge/latex/section-family-index.md`, `knowledge/latex/style-variant-index.md`, `knowledge/latex/table-family-index.md`, `knowledge/latex/equation-family-index.md`, `knowledge/latex/snippets.md` | Covered | Some style notes still need more clean examples and fewer legacy artifacts | Continue replacing old rough notes with tighter indices |
| The system must self-check quality before handoff | `knowledge/quality/quality-rubric-v2.md`, `knowledge/quality/evidence-family-index.md`, `knowledge/quality/review-finding-index.md`, `knowledge/quality/finding-gate-matrix.md`, `knowledge/quality/completion-gate.md` | Covered | Quality gates are in place, but more failure examples would strengthen them | Add more review cases and convert recurring failures into gates |
| It should support long-term iteration instead of one-off generation | `knowledge/roadmap.md`, `knowledge/cumcm/next-iteration-plan.md`, `knowledge/cumcm/next-iteration-action-matrix.md`, `docs/continuation-state.md`, `docs/run-artifact-index.md` | Covered | The next-step logic exists, but it should keep absorbing new routes and demos | Use the next-iteration matrix as the work queue |
| The project should be suitable for research on human vs AI competition outputs | `knowledge/quality/reproducibility-and-ai-difference-framework.md`, `docs/review-checklist.md`, `knowledge/quality/quality-rubric-v2.md`, `knowledge/quality/completion-gate.md` | Mostly covered | The comparison lens exists, but it still needs more dedicated evaluation cases | Keep collecting review evidence that separates polished style from real modeling depth |
| The repository should remain private/local during active work | Operating rule in `docs/continuation-state.md` and the current user instruction not to upload | Covered | No functional gap; this is a coordination rule | Keep local-only until the user explicitly wants a sync |

## What This Means Right Now

The project is no longer just a folder of sources. It now has a working spine:

problem signal -> route selection -> method selection -> section planning -> figure/table planning -> LaTeX writing -> review gates -> iteration queue

The main remaining work is not to invent another spine, but to keep feeding this one with better papers, better demos, and better failure cases.

## Near-Term Gaps

1. More route-specific comparison notes for excellent papers.
2. More complete end-to-end run examples for Claude Code.
3. Better contest-style figure and table conventions.
4. Stronger late-stage LaTeX polish for dense Chinese academic writing.
5. More route-specific examples that show how to reach 20-30 pages without padding.

## Where To Read Next

If you are resuming after a pause, start with:

1. `knowledge/README.md`
2. `knowledge/learning-status.md`
3. `docs/continuation-state.md`
4. `docs/run-start-checklist.md`
5. `prompts/07_launch.md`
6. `knowledge/cumcm/next-iteration-action-matrix.md`

