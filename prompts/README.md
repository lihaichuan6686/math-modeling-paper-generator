# Prompts

Purpose: give Claude Code one stable path through the v1.0 generation loop.

## Read This Layer In Order

1. `00_intake.md`
2. `01_ideation.md`
3. `02_model_plan.md`
4. `03_implementation.md`
5. `04_writing.md`
6. `05_review.md`
7. `06_quality_review.md`
8. `07_launch.md`
9. `08_launch_v1_2.md`
10. `09_revision_v1_2.md`
11. `flow-map.md`

## What The Prompt Chain Does

The prompt chain turns a problem statement into a paper draft through staged control:

```text
intake -> ideation -> model plan -> implementation -> writing -> review -> quality audit -> revision if needed
```

Each stage should leave a file under `runs/current/` or the active run directory.

Use `flow-map.md` when you want the shortest path from stage to stage and need a quick reminder of what each step must leave behind.

## Stage Roles

| Stage | Main job | Main output |
|---|---|---|
| Intake | isolate the problem and inputs | `problem-analysis.md`, `data-inventory.md` |
| Ideation | propose route-level candidates | `model-candidates.md` |
| Model plan | choose one route and formalize it | `model-plan.md`, `verification-plan.md` |
| Implementation | generate code, tables, and figures | `src/`, `paper/tables/`, `paper/figures/` |
| Writing | assemble the LaTeX draft | `paper/sections/`, `paper/main.tex` |
| Review | audit paper quality | `reviews/review-*.md` |
| Quality audit | run the machine gate and record status | gate output plus review evidence |
| Revision | repair thinness, shallow chains, and machine-like phrasing | updated paper plus refreshed run files |

## Key Rules

- Keep the route stable after ideation unless evidence forces a change.
- Do not write the full paper before the model plan is clear.
- Do not treat implementation output as complete until it is traced in the artifact ledger.
- Do not treat a compile success as a final pass without a quality review.
- If the review still flags thin sections or shallow method chains, run `09_revision_v1_2.md` before treating the draft as a serious v1.2 trial.

## Status

This file is the operational doorway for the prompt chain. It should stay short and point directly to the staged workflow.
