# Docs

Purpose: give the project one stable entry point for workflow, run state, review rules, and roadmap material.

## Read This Layer In Order

1. `v1.4-definition.md`
2. `v1.4-community-learning-plan.md`
3. `community-signal-to-rule-pipeline.md`
4. `playwright-mcp-public-research.md`
5. `local-experience-extraction-queue.md`
6. `local-experience-extraction-status.md`
7. `v1.4-runbook.md`
8. `online-consensus-check-protocol.md`
9. `online-consensus-example-template.md`
10. `online-consensus-weak-strong-examples.md`
11. `v1.4-release-notes.md`
12. `v1.4-readiness-report.md`
13. `v1.4-test-handoff.md`
14. `v1.4-user-test-protocol.md`
15. `v1.4-user-test-feedback-template.md`
16. `v1.4-feedback-triage-matrix.md`
17. `v1.4-sync-manifest.md`
18. `v1.4-release-checklist.md`
17. `v1.3-methodology-runbook.md`
17. `v1.2-runbook.md`
18. `v1.2-final-pass-guide.md`
19. `v1.2-draft-contract.md`
20. `v1.2-definition.md`
21. `v1.2-quickstart.md`
22. `v1-runbook.md`
23. `workflow.md`
24. `continuation-state.md`
25. `current-state-matrix-2026-07-07.md`
26. `review-checklist.md`
27. `visual-generation-pipeline.md`
28. `run-start-checklist.md`
29. `problem-profile-template.md`
30. `route-decision-template.md`
31. `methodology-checklist-template.md`
32. `literature-notes-template.md`
33. `artifact-ledger-template.md`
34. `figure-plan-template.md`
35. `section-budget-template.md`
36. `writing-style-plan-template.md`
36. `family-section-budget-examples.md`
37. `family-writing-style-examples.md`
38. `run-file-examples/README.md`
39. `paper-section-examples/README.md`
40. `paper-assembly-examples/README.md`
41. `demo-bundles/README.md`
42. `review-case-examples/README.md`
43. `sample-run-packages/README.md`
44. `pressure-test-runbook.md`
45. `calibration-log-template.md`
46. `first-calibration-batch-plan.md`
47. `calibration-run-index.md`
48. `calibration-candidates/batch1-candidate-selection.md`
49. `calibration-examples/monitoring-route-e-calibration-example.md`
50. `run-artifact-index.md`
51. `project-audit-2026-07-06.md`
52. `architecture.md`
53. `long-term-roadmap.md`
54. `research-agenda.md`
55. `objective-coverage-matrix.md`

## What This Layer Does

This layer answers four questions:

1. How does a run start and move forward?
2. What state do we believe the project is in right now?
3. How do we check quality and traceability?
4. What next work is worth doing?

## Navigation Rule

Use the v1.4 runbook when the goal is to add contest-circle soft rules, award-paper feel, and online consensus reflection on top of the v1.3 methodology layer.
Use the community signal pipeline when converting local experience, public posts, videos, or award-paper observations into stable prompts, run files, or review gates.
Use the Playwright MCP public research entry when public online information is needed; browse normally accessible pages and record access limits instead of using platform-specific crawlers.
Use the local experience extraction queue when continuing static absorption of older `.doc` and `.ppt` files from the local modeling-experience folder.
Use the local experience extraction status file to avoid counting partial or blocked old-format probes as full absorption.
Use `../prompts/12_launch_v1_4.md` when you want one direct prompt that launches a v1.4 production-style run.
Use the v1.3 runbook when the goal is to strengthen the reusable methodology layer, and the v1.2 runbook when the goal is to execute one stronger draft loop.
Use `../prompts/13_platform_research.md` for Playwright MCP public browsing after the model plan exists and before the online-consensus reflection phase.
Use the online-consensus protocol after the first model plan exists and before final paper writing, especially for current or recently discussed problems.
Use the online-consensus example template when Claude needs a concrete shape for `online-consensus-notes.md`.
Use the online-consensus weak/strong examples when the note looks like a search dump or answer-copying risk.
Use the v1.4 release notes to understand the version changes and boundaries.
Use the v1.4 readiness report to understand what the static release is ready to test and what it does not prove.
Use the v1.4 test handoff when the user wants the shortest practical instructions for testing v1.4 in Claude Code.
Use the v1.4 user test protocol and feedback template after a user-side Claude Code run to decide what needs repair.
Use the v1.4 feedback triage matrix to turn observed failures into the next concrete prompt, rule, template, or review-gate repair.
Use the v1.4 sync manifest when preparing to transfer or publish the v1.4 layer into another clone.
Use the v1.4 release checklist before handing the repository to the user for a v1.4 Claude Code production test.
Use `../scripts/check-v1.4-static.ps1` as the executable static check for the v1.4 release checklist.
Use the workflow for staged output, the continuation state for handoff, the current-state matrix for evidence status, and the review checklist plus visual/ledger templates for quality control.
Use the three v1.3 templates when the run needs explicit problem profiling, route-decision reasoning, and methodology claim boundaries before implementation starts.

Use the family example notes when the run files still feel too blank and Claude needs a concrete target shape for `section-budget.md` or `writing-style-plan.md`.
Use the draft contract when Claude needs a stricter v1.2 bar than the general runbook provides.
Use the v1.2 definition when deciding whether the version is ready for user testing or whether a task should be deferred to a later version.
Use the run-file examples when Claude needs to see what a non-placeholder `problem-analysis.md`, `model-plan.md`, or `verification-plan.md` should look like in practice.
The run-file examples now cover evaluation-to-planning, rail/timetable, forecast-to-decision, geometry/spatial-design, dynamic-scheduling, classification-recognition, and monitoring-route-E families, so use them as the first practical bridge from abstract rules into filled run artifacts.
Use the pressure-test runbook when the goal shifts from building scaffolds to proving whether those scaffolds survive fresh real problems across multiple route families.
Use the first calibration batch plan when choosing which route families to pressure-test first and what each run should prove.
Use the calibration run index to track which pressure tests are planned, running, reviewed, calibrated, or written back.
Use the Batch 1 candidate-selection note before launching the first pressure test, especially when a high-value route candidate lacks complete local materials.
Use the calibration example when Claude needs to see how a pressure-test finding should become failure buckets and repo write-back decisions.
Use the paper-section examples when Claude needs to see how route-aware prose, equations, and result interpretation should actually sound inside `paper/sections/`.
Use the paper-assembly examples when Claude has decent sections already, but still needs help stitching them into a complete paper with stable question mapping, evidence order, and abstract/conclusion control.
Use the demo bundles when Claude needs one nearest-thing-to-end-to-end reference package for a route family before starting a real run.
Use the claim maps inside the demo bundles when abstract or conclusion wording starts to outrun the actual evidence.
Use the caption maps inside the demo bundles when figure/table titles or nearby interpretation start sounding generic.
Use the review case examples when Claude is self-reviewing and needs to see what a sharp, evidence-based `Needs revision` review should sound like.
Use the sample run packages when Claude needs one shortest-path reading list for a route family before starting a real v1.2 attempt.
Use the community soft-rule files when a draft is structurally complete but still does not feel like a contest-circle or award-level paper.

The roadmap and research agenda explain why the project exists and what still deserves attention.

For late-stage tightening, prefer `v1.2-final-pass-guide.md` over re-reading the whole stack.

## Status

This file is the doorway for the docs corpus. It should stay short and should point to the operational files first.
