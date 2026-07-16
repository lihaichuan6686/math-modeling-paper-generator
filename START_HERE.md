# Start Here

This repository is ready for both a simple Claude Code trial and a stronger methodology-guided paper run.

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
12. `docs/v1.4-definition.md`
13. `docs/v1.4-community-learning-plan.md`
14. `docs/community-signal-to-rule-pipeline.md`
15. `docs/local-experience-extraction-queue.md`
16. `docs/local-experience-extraction-status.md`
17. `docs/v1.4-runbook.md`
18. `docs/playwright-mcp-public-research.md`
19. `docs/online-consensus-check-protocol.md`
20. `prompts/13_platform_research.md`
21. `prompts/12_launch_v1_4.md`
22. `docs/v1.4-release-notes.md`
23. `docs/v1.4-readiness-report.md`
24. `docs/v1.4-test-handoff.md`
25. `docs/v1.4-user-test-protocol.md`
26. `docs/v1.4-user-test-feedback-template.md`
27. `docs/v1.4-feedback-triage-matrix.md`
28. `docs/v1.3-methodology-runbook.md`
29. `docs/v1-runbook.md`
30. `docs/v1.2-runbook.md`
31. `docs/v1.2-draft-contract.md`
32. `docs/v1.2-definition.md`
33. `docs/v1.2-quickstart.md`
34. `docs/sample-run-packages/README.md`

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
Then use problems/problem.md to produce a v1.4 methodology-guided mathematical modeling paper draft with contest-circle soft rules, stronger section density, deeper method chains, code-generated tables and figures, online consensus reflection before final writing, LaTeX, PDF build, and review.
Use prompts/12_launch_v1_4.md as the main launch instruction, then run prompts/09_revision_v1_2.md if the review still says the paper is thin, shallow, or too machine-like.
Use docs/v1.4-runbook.md, docs/playwright-mcp-public-research.md, prompts/13_platform_research.md, docs/community-signal-to-rule-pipeline.md, prompts/11_online_consensus_check.md, docs/v1.3-methodology-runbook.md, and docs/v1.2-draft-contract.md to keep method choice, abstract length, section rhythm, evidence distribution, Playwright MCP public research, external sanity checking, community-signal conversion, and paper feel under control.
```

For the shortest v1.4 handoff, use `docs/v1.4-test-handoff.md`.
After the run, evaluate it with `docs/v1.4-user-test-protocol.md`, record feedback with `docs/v1.4-user-test-feedback-template.md`, then map failures to repairs with `docs/v1.4-feedback-triage-matrix.md`.

Before publishing, syncing, or handing off v1.4, run:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\check-v1.4-static.ps1
```

## Current Reality

This repository has a working v1.0 closed loop, a stronger v1.2 drafting path, a v1.3 methodology layer, and an emerging v1.4 contest-feel layer. It is not yet a polished 2.0 production system.

Use only for learning, post-contest review, authorized research, and quality-checking experiments.
