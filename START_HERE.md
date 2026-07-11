# Start Here

This repository is ready for both a simple Claude Code trial and a stronger v1.2 paper run.

## Navigation Map

If you are just getting oriented, read these in order:

1. `README.md`
2. `CLAUDE.md`
3. `docs/README.md`
4. `knowledge/README.md`
5. `knowledge/learning-status.md`
6. `knowledge/cumcm/README.md`
7. `knowledge/algorithms/README.md`
8. `knowledge/latex/README.md`
9. `knowledge/quality/README.md`
10. `prompts/README.md`
11. `docs/run-start-checklist.md`
12. `docs/v1-runbook.md`
13. `docs/v1.2-runbook.md`
14. `docs/v1.2-draft-contract.md`
15. `docs/v1.2-quickstart.md`

## Fastest Demo

Run this from the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\run-v1-demo.ps1 -Name v1-demo -Force
powershell -ExecutionPolicy Bypass -File .\scripts\compile.ps1
```

Expected result:

- generated table: `paper/tables/demo_v1_order_plan.tex`
- generated figure: `paper/figures/demo_v1_inventory.png`
- paper source: `paper/main.tex`
- compiled PDF: `paper/main.pdf`
- review: `reviews/review-v1-demo.md`
- minimum artifact gate runs automatically unless `-SkipQualityGate` is passed

## Timetable Demo

For a rail/metro/timetable route demo, run:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\run-rail-demo.ps1 -Name rail-demo -Force
```

Expected result:

- operation candidates: `runs/rail-demo/rail_operation_candidates.csv`
- selected operation plan: `runs/rail-demo/rail_selected_operation_plan.csv`
- full timetable: `runs/rail-demo/rail_full_timetable.csv`
- capacity audit: `runs/rail-demo/rail_capacity_audit.csv`
- tracking and dwell audits: `runs/rail-demo/rail_tracking_audit.csv`, `runs/rail-demo/rail_dwell_audit.csv`
- scenario analysis: `runs/rail-demo/rail_scenario_analysis.csv`
- figures: `paper/figures/rail_section_flow.png`, `paper/figures/rail_cost_service_tradeoff.png`, `paper/figures/rail_timetable_diagram.png`
- paper source: `paper/rail_demo.tex`
- minimum artifact gate runs automatically unless `-SkipQualityGate` is passed

To compile the rail demo paper:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\compile.ps1 -Main rail_demo.tex
```

To run the minimum artifact gate:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\check-run-quality.ps1 -Run rail-demo -Paper rail_demo.tex
```

## Use A New Problem

1. Put the problem statement in `problems/problem.md`.
2. Create the active run scaffold:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\start-v1.2-current.ps1 -Name current -Force
```

3. Ask Claude Code:

```text
Use the repository skill at .codex/skills/cumcm-paper-generator/SKILL.md.
Read START_HERE.md and CLAUDE.md.
Then use problems/problem.md to produce a v1.2 mathematical modeling paper draft with stronger section density, deeper method chains, code-generated tables and figures, LaTeX, PDF build, and review.
Use prompts/08_launch_v1_2.md as the main launch instruction, then run prompts/09_revision_v1_2.md if the review still says the paper is thin, shallow, or too machine-like.
Use docs/v1.2-draft-contract.md to keep abstract length, section rhythm, and evidence distribution at v1.2 level.
```

## Current Reality

This repository has a working v1.0 closed loop and is now being upgraded toward a v1.2 human-team-style paper generator. It is not yet a polished 2.0 production system.

Use only for learning, post-contest review, authorized research, and quality-checking experiments.
