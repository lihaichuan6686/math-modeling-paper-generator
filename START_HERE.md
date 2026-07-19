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
12. `docs/v1.5-paper-template-contract.md`
13. `docs/v1.5-method-route-contract.md`
14. `knowledge/latex/v1-5-front-matter-rhythm-rules.md`
15. `knowledge/latex/v1-5-award-paper-style-rules.md`
16. `knowledge/latex/v1-5-award-paper-visual-fingerprint.md`
17. `knowledge/algorithms/v1-5-route-upgrade-atlas.md`
18. `knowledge/quality/v1-5-hard-gates.md`
19. `prompts/15_launch_v1_5.md`
20. `docs/v1.5-test-handoff.md`
21. `docs/v1.5-readiness-report.md`
22. `docs/v1.5-release-checklist.md`
23. `docs/v1.5-user-test-feedback-template.md`
24. `docs/v1.5-feedback-triage-matrix.md`
25. `docs/v1.4-definition.md`
26. `docs/v1.4-runbook.md`
27. `docs/playwright-mcp-public-research.md`
28. `prompts/13_platform_research.md`
29. `prompts/12_launch_v1_4.md`
30. `docs/v1.4-test-handoff.md`
31. `docs/v1.4-feedback-triage-matrix.md`
32. `docs/v1.3-methodology-runbook.md`
33. `docs/v1.2-draft-contract.md`
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

For a fresh machine or clone, prepare the Python environment once:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\setup.ps1
```

3. Ask Claude Code:

```text
Use the repository skill at .codex/skills/cumcm-paper-generator/SKILL.md.
Read START_HERE.md and CLAUDE.md.
Then use problems/problem.md to produce a v1.5 award-paper-feel CUMCM-style mathematical modeling paper draft.
Use prompts/15_launch_v1_5.md as the main launch instruction.
Read only the v1.5 Level 0 files first: docs/v1.5-paper-template-contract.md, docs/v1.5-method-route-contract.md, knowledge/latex/v1-5-front-matter-rhythm-rules.md, knowledge/latex/v1-5-award-paper-style-rules.md, knowledge/latex/v1-5-award-paper-visual-fingerprint.md, knowledge/algorithms/v1-5-route-upgrade-atlas.md, and knowledge/quality/v1-5-hard-gates.md.
Use paper/templates/cumcm_v15_main.tex as the paper skeleton.
Create runs/current/title-candidates.md before writing paper/main.tex.
The final review must include a v1.5 Hard Gate Verdict and Method Route Verdict.
```

For the shortest v1.5 handoff, use `docs/v1.5-test-handoff.md`.
Before calling v1.5 ready for user testing, read `docs/v1.5-readiness-report.md` and run through `docs/v1.5-release-checklist.md`.
After a v1.5 run, record visible failures with `docs/v1.5-user-test-feedback-template.md`, then map them to repairs with `docs/v1.5-feedback-triage-matrix.md`.
For the older v1.4 handoff, use `docs/v1.4-test-handoff.md`.
After a v1.4 run, evaluate it with `docs/v1.4-user-test-protocol.md`, record feedback with `docs/v1.4-user-test-feedback-template.md`, then map failures to repairs with `docs/v1.4-feedback-triage-matrix.md`.

Legacy v1.4 references remain available:

- `docs/v1.4-community-learning-plan.md`
- `docs/community-signal-to-rule-pipeline.md`
- `docs/local-experience-extraction-queue.md`
- `docs/local-experience-extraction-status.md`
- `docs/v1.4-release-notes.md`
- `docs/v1.4-readiness-report.md`
- Playwright MCP public research: `docs/playwright-mcp-public-research.md`

Before publishing, syncing, or handing off v1.5, run:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\check-v1.5-static.ps1
```

When a v1.5 PDF exists, also run:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\check-v1.5-pdf.ps1 -Pdf .\paper\main.pdf -Run .\runs\current -Tex .\paper\main.tex -Review .\reviews\review-current.md
```

## Current Reality

This repository has a working v1.0 closed loop, a stronger v1.2 drafting path, a v1.3 methodology layer, a v1.4 contest-feel layer, and an emerging v1.5 award-paper-feel hard-gate layer. It is not yet a polished 2.0 production system.

Use only for learning, post-contest review, authorized research, and quality-checking experiments.
