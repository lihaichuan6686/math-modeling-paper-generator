# Prompts

Purpose: give Claude Code one stable path through the generation loop.

## Read This Layer In Order

1. `00_intake.md`
2. `01_ideation.md`
3. `02_model_plan.md`
4. `11_online_consensus_check.md`
5. `03_implementation.md`
6. `04_writing.md`
7. `05_review.md`
8. `06_quality_review.md`
9. `07_launch.md`
10. `08_launch_v1_2.md`
11. `09_revision_v1_2.md`
12. `10_launch_v1_3.md`
13. `12_launch_v1_4.md`
14. `13_platform_research.md`
15. `15_launch_v1_5.md`
16. `flow-map.md`

## What The Prompt Chain Does

The prompt chain turns a problem statement into a paper draft through staged control:

```text
intake -> ideation -> model plan -> Playwright public research -> online consensus -> implementation -> writing -> review -> quality audit -> revision if needed
```

Each stage should leave a file under `runs/current/` or the active run directory.

Use `10_launch_v1_3.md` when the work is not just "finish one stronger paper", but "improve the reusable thinking method behind future papers".
Use `12_launch_v1_4.md` when the work should produce a contest-feel draft with online consensus, recent award-paper visual rhythm, section proportions, and human-feel review.
Use `15_launch_v1_5.md` when the work should produce an award-paper-feel draft with method route depth, title candidates, a contest-style title, paragraph abstract with bold results, early concept figure, paper-ready figures/tables, appendix code, and hard-gate review.
Use `11_online_consensus_check.md` after the first route and model plan exist, before final paper writing, to check public contest-circle discussion without copying answers.
Use `13_platform_research.md` when the model plan exists and you need Playwright MCP to browse public online sources for community interpretation, traps, and result-range sanity checks before writing the final paper.
Use `flow-map.md` when you want the shortest path from stage to stage and need a quick reminder of what each step must leave behind.

## Stage Roles

| Stage | Main job | Main output |
|---|---|---|
| Intake | isolate the problem and inputs | `problem-profile.md`, `problem-analysis.md`, `data-inventory.md` |
| Ideation | propose route-level candidates | `model-candidates.md`, `route-decision.md` |
| Model plan | choose one route and formalize it | `model-plan.md`, `verification-plan.md`, `methodology-checklist.md` |
| Playwright public research | browse public sources with Playwright MCP for community signals and sanity checks | `online-consensus-notes.md` |
| Online consensus | reflect on public signals and convert them into run-file changes | `online-consensus-notes.md` updated run files |
| Implementation | generate code, tables, and figures | `src/`, `paper/tables/`, `paper/figures/` |
| Writing | assemble the LaTeX draft | `paper/sections/`, `paper/main.tex` |
| Review | audit paper quality | `reviews/review-*.md` |
| Quality audit | run the machine gate and record status | gate output plus review evidence |
| Revision | repair thinness, shallow chains, and machine-like phrasing | updated paper plus refreshed run files |

## v1.5 Level 0

For v1.5, do not read the whole repository first. Read only:

- `START_HERE.md`
- `docs/v1.5-paper-template-contract.md`
- `docs/v1.5-method-route-contract.md`
- `knowledge/latex/v1-5-front-matter-rhythm-rules.md`
- `knowledge/latex/v1-5-award-paper-style-rules.md`
- `knowledge/quality/v1-5-hard-gates.md`
- `prompts/15_launch_v1_5.md`

Then load extra files only when the current problem requires them.

## Key Rules

- Keep the route stable after ideation unless evidence forces a change.
- Do not write the full paper before the model plan is clear.
- Do not write the final paper before Playwright public research and the online consensus check are completed, or explicitly skipped with a reason.
- Do not treat implementation output as complete until it is traced in the artifact ledger.
- Do not treat a compile success as a final pass without a quality review.
- If the review still flags thin sections or shallow method chains, run `09_revision_v1_2.md` before treating the draft as a serious v1.2 trial.

## Status

This file is the operational doorway for the prompt chain. It should stay short and point directly to the staged workflow.
