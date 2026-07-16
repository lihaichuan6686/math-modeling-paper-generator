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
| Claude Code can use it directly | `START_HERE.md`, `.codex/skills/cumcm-paper-generator/SKILL.md`, `docs/run-start-checklist.md`, `docs/v1.4-runbook.md`, `prompts/12_launch_v1_4.md`, `scripts/start-current.ps1`, `scripts/new-run.ps1`, `docs/demo-bundles/README.md`, `docs/run-file-examples/README.md` | Mostly covered | The entry path is usable, but still benefits from more fresh-run pressure testing across real problems | Keep tightening the first-run path and add more run transcripts, bundles, and pressure-test logs |
| The model can ideate, plan, write, code, draw, lay out LaTeX, and self-review | `prompts/00_intake.md` through `prompts/06_quality_review.md`, `prompts/flow-map.md`, `docs/visual-generation-pipeline.md`, `docs/figure-plan-template.md`, `docs/artifact-ledger-template.md`, `docs/review-checklist.md`, `knowledge/quality/completion-gate.md`, `docs/demo-bundles/README.md`, `docs/v1.4-feedback-triage-matrix.md` | Mostly covered | The loop exists, but it needs more end-to-end examples and better failure repair | Keep expanding the demo path, bundles, review evidence, and triage-driven repairs |
| The output should become a full 20-30 page paper | `knowledge/cumcm/20-30-page-paper-blueprint.md`, `knowledge/cumcm/archetype-page-density-matrix.md`, `knowledge/latex/style-variant-index.md`, `knowledge/latex/section-family-index.md`, `knowledge/cumcm/paper-family-matrix.md`, `docs/paper-section-examples/README.md`, `docs/paper-assembly-examples/README.md` | Mostly covered | Page budgeting is defined, but needs more route-specific proof and more full-length end-to-end demonstrations | Add more complete sample structures, page-density examples, and assembled demo papers |
| The tool should learn and absorb the local competition materials deeply | `inventory/README.md`, `inventory/source-map.md`, `inventory/source-absorption-matrix.md`, `knowledge/cumcm/deep-reading-index.md`, `knowledge/cumcm/comparison-index.md`, `knowledge/cumcm/official-paper-index.md`, `knowledge/community/local-experience-absorption-log.md`, `docs/local-experience-extraction-queue.md`, `docs/local-experience-extraction-status.md`, `scripts/probe-binary-office-text.py` | Mostly covered | More official excellent papers, comparison notes, and old-format local materials still need stable extraction and conversion into structured knowledge | Continue queue-driven local extraction; use status files to avoid false absorption claims |
| Figures are essential and must join the pipeline | `docs/visual-generation-pipeline.md`, `docs/figure-plan-template.md`, `knowledge/latex/visual-family-index.md`, `knowledge/latex/figures-tables-equations-style.md`, generated demo figures in `paper/figures/` | Covered | Need more contest-style figure conventions and better captions/labels | Expand figure role notes by route family |
| LaTeX paper writing must be complete and reusable | `knowledge/latex/cumcm-section-contract.md`, `knowledge/latex/section-writing-patterns.md`, `knowledge/latex/section-family-index.md`, `knowledge/latex/style-variant-index.md`, `knowledge/latex/table-family-index.md`, `knowledge/latex/equation-family-index.md`, `knowledge/latex/snippets.md` | Covered | Some style notes still need more clean examples and fewer legacy artifacts | Continue replacing old rough notes with tighter indices |
| The system must self-check quality before handoff | `knowledge/quality/quality-rubric-v2.md`, `knowledge/quality/evidence-family-index.md`, `knowledge/quality/review-finding-index.md`, `knowledge/quality/finding-gate-matrix.md`, `knowledge/quality/completion-gate.md`, `docs/review-case-examples/README.md` | Covered | Quality gates are in place, but more failure examples would still strengthen them | Add more review cases and convert recurring failures into gates |
| The paper should reflect contest-circle soft rules and award-paper feel | `docs/v1.4-community-learning-plan.md`, `knowledge/community/math-modeling-soft-rules.md`, `knowledge/community/paper-polish-and-feel.md`, `knowledge/community/contest-workflow-and-team-execution.md`, `knowledge/community/section-duty-soft-rules.md`, `knowledge/community/visual-evidence-chain-rules.md`, `knowledge/community/award-paper-section-rhythm.md`, `knowledge/cumcm/recent-award-paper-visual-rhythm.md`, `knowledge/quality/v1-4-human-feel-review-gate.md` | Mostly covered | The soft-rule layer is broad, but needs more public examples and user-side generated-paper evidence | Keep adding public/community examples and use user-side tests to tighten gates |
| Online community signals should be used safely before final writing | `docs/online-consensus-check-protocol.md`, `prompts/11_online_consensus_check.md`, `docs/online-consensus-example-template.md`, `docs/online-consensus-weak-strong-examples.md`, `knowledge/community/public-community-source-playbook.md`, `knowledge/community/source-quality-rubric.md`, `runs/current/online-consensus-notes.md` scaffold | Mostly covered | Protocol is strong, but needs more real source examples across platforms and topics | Add source-quality examples and compare user-side tests for missing or unsafe online-consensus behavior |
| Literature search and citations should support methods instead of padding | `knowledge/community/literature-search-and-citation-rules.md`, `docs/literature-notes-template.md`, `runs/current/literature-notes.md` scaffold, `prompts/06_quality_review.md`, `docs/v1.4-feedback-triage-matrix.md` | Mostly covered | The scaffold exists, but needs real filled examples and citation-quality cases | Add filled literature-note examples and review cases where citations are decorative or missing |
| It should support long-term iteration instead of one-off generation | `knowledge/roadmap.md`, `knowledge/cumcm/next-iteration-plan.md`, `knowledge/cumcm/next-iteration-action-matrix.md`, `docs/continuation-state.md`, `docs/run-artifact-index.md`, `docs/pressure-test-runbook.md`, `docs/calibration-log-template.md`, `docs/first-calibration-batch-plan.md`, `docs/calibration-run-index.md` | Covered | The next-step logic exists, but it still needs repeated real-problem calibration evidence | Use the first calibration batch as the work queue and record every fresh pressure test in the calibration log and run index |
| The project should be suitable for research on human vs AI competition outputs | `knowledge/quality/reproducibility-and-ai-difference-framework.md`, `docs/review-checklist.md`, `knowledge/quality/quality-rubric-v2.md`, `knowledge/quality/completion-gate.md` | Mostly covered | The comparison lens exists, but it still needs more dedicated evaluation cases | Keep collecting review evidence that separates polished style from real modeling depth |
| The repository should remain private/local during active work | Operating rule in `docs/continuation-state.md` and the current user instruction not to upload | Covered | No functional gap; this is a coordination rule | Keep local-only until the user explicitly wants a sync |

## What This Means Right Now

The project is no longer just a folder of sources. It now has a working spine:

problem signal -> route selection -> method selection -> section planning -> figure/table planning -> LaTeX writing -> review gates -> iteration queue

The main remaining work is not to invent another spine, but to keep feeding this one with better papers, better demos, and better failure cases.

The new control question for the next stage is no longer only "what else could be improved?"

It is also:

```text
is v1.2 already test-ready under its own definition?
```

## Near-Term Gaps

1. More user-side v1.4 generated-paper tests, scored with the feedback template and triage matrix.
2. More route-specific comparison notes for excellent papers.
3. More filled `literature-notes.md` and `online-consensus-notes.md` examples from real tasks.
4. Better contest-style figure and table conventions.
5. Stronger late-stage LaTeX polish for dense Chinese academic writing.
6. More route-specific examples that show how to reach 20-30 pages without padding.

## Where To Read Next

If you are resuming after a pause, start with:

1. `knowledge/README.md`
2. `knowledge/learning-status.md`
3. `docs/continuation-state.md`
4. `docs/run-start-checklist.md`
5. `prompts/07_launch.md`
6. `docs/v1.4-runbook.md`
7. `docs/v1.4-feedback-triage-matrix.md`
8. `knowledge/cumcm/next-iteration-action-matrix.md`
