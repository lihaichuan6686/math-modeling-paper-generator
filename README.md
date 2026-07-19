# Math Modeling Paper Generator

A research-only Claude Code workspace for generating and reviewing CUMCM-style mathematical modeling paper drafts.

The near-term goal is a usable **v1.2 closed loop**, a **v1.3 methodology layer**, a **v1.4 contest-feel layer**, and a **v1.5 award-paper-feel hard-gate layer** built on top of the earlier v1.0 prototype:

```text
problem statement
-> run scaffold
-> problem profile
-> problem analysis
-> model route selection
-> model plan
-> Playwright MCP public research
-> online consensus reflection
-> code-generated figures/tables
-> v1.5 paper skeleton
-> LaTeX paper draft with hard gates
-> PDF build
-> self-review report
```

The repository already has a working v1.0 loop. The current targets are:

- v1.2: stronger section density, deeper method chains, more human-team writing feel, and stricter self-review;
- v1.3: a reusable methodology layer for problem understanding, route selection, paper composition, and self-audit;
- v1.4: contest-circle soft rules, award-paper feel controls, online consensus checking before final writing, and a signal-to-rule pipeline so learned experience becomes reusable behavior;
- v1.5: title/abstract/figure/template/code-appendix/result-sanity hard gates so the paper looks less like an AI technical report and more like a serious CUMCM team draft.

## Responsible Use

Use this project only for:

- learning;
- post-contest review;
- course or authorized research;
- writing-method experiments;
- paper-quality checking.

Do not use it for active contest rule violations, concealed prohibited AI participation, fabricated experiments, fabricated data, or fabricated citations.

## Quick Start

For the shortest clone-ready path, open:

```text
START_HERE.md
```

Then ask Claude Code to use:

```text
.codex/skills/cumcm-paper-generator/SKILL.md
```

1. Put the problem statement in:

```text
problems/problem.md
```

2. Create a run scaffold:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\start-current.ps1 -Name current -Force
```

3. Prepare the lightweight Python environment when needed:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\setup.ps1
```

4. Ask Claude Code to follow v1.5:

```text
prompts/15_launch_v1_5.md
docs/v1.5-paper-template-contract.md
docs/v1.5-method-route-contract.md
knowledge/latex/v1-5-front-matter-rhythm-rules.md
knowledge/latex/v1-5-award-paper-style-rules.md
knowledge/latex/v1-5-award-paper-visual-fingerprint.md
knowledge/algorithms/v1-5-route-upgrade-atlas.md
knowledge/quality/v1-5-hard-gates.md
docs/v1.5-test-handoff.md
docs/v1.5-readiness-report.md
docs/v1.5-release-checklist.md
docs/v1.5-user-test-feedback-template.md
docs/v1.5-feedback-triage-matrix.md
```

For older v1.4 runs, Claude Code can still work through:

```text
prompts/README.md
docs/v1.4-runbook.md
prompts/12_launch_v1_4.md
prompts/10_launch_v1_3.md
prompts/00_intake.md
prompts/01_ideation.md
prompts/02_model_plan.md
prompts/13_platform_research.md
prompts/11_online_consensus_check.md
prompts/03_implementation.md
prompts/04_writing.md
prompts/05_review.md
prompts/06_quality_review.md
prompts/09_revision_v1_2.md
```

`prompts/15_launch_v1_5.md` is the direct v1.5 launch prompt. `paper/templates/cumcm_v15_main.tex` is the neutral paper skeleton. `prompts/12_launch_v1_4.md` remains the v1.4 launch prompt. `prompts/13_platform_research.md` is the Playwright MCP public browsing entry before online consensus review.

5. Compile the paper:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\compile.ps1
```

6. When `paper/main.pdf` exists, run the visible v1.5 PDF check:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\check-v1.5-pdf.ps1 -Pdf .\paper\main.pdf -Run .\runs\current -Tex .\paper\main.tex -Review .\reviews\review-current.md
```

## v1.2 / v1.3 / v1.4 / v1.5 Expected Outputs

A completed methodology-guided run should contain:

- `runs/current/problem-profile.md`
- `runs/current/problem-analysis.md`
- `runs/current/data-inventory.md`
- `runs/current/model-candidates.md`
- `runs/current/route-decision.md`
- `runs/current/model-plan.md`
- `runs/current/method-depth-plan.md`
- `runs/current/verification-plan.md`
- `runs/current/figure-plan.md`
- `runs/current/title-candidates.md`
- `runs/current/section-budget.md`
- `runs/current/writing-style-plan.md`
- `runs/current/methodology-checklist.md`
- `runs/current/literature-notes.md`
- `runs/current/online-consensus-notes.md` when public discussion is relevant, or a reason for skipping it
- `runs/current/artifact-ledger.md`
- generated figures under `paper/figures/`
- generated tables under `paper/tables/`
- LaTeX source under `paper/`
- `paper/main.tex` based on `paper/templates/cumcm_v15_main.tex` for v1.5
- appendix code or script index for v1.5
- a compiled PDF when the local LaTeX environment is available
- `reviews/pdf-v15-check.md` when a v1.5 PDF exists
- `reviews/review-current.md` or `reviews/review-<run>.md`, with `v1.5 Hard Gate Verdict` and `Method Route Verdict` for v1.5

For user-side v1.4 testing, use:

- `docs/v1.4-release-notes.md`
- `docs/v1.4-readiness-report.md`
- `docs/v1.4-test-handoff.md`
- `docs/v1.4-user-test-protocol.md`
- `docs/v1.4-user-test-feedback-template.md`
- `docs/v1.4-feedback-triage-matrix.md`

For user-side v1.5 testing, use:

- `docs/v1.5-test-handoff.md`
- `docs/v1.5-readiness-report.md`
- `docs/v1.5-release-checklist.md`
- `docs/v1.5-user-test-feedback-template.md`
- `docs/v1.5-feedback-triage-matrix.md`

Before publishing or handing v1.5 to another Claude Code clone, run:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\check-v1.5-static.ps1
```

## Important Knowledge Entry Points

Read these before generation or review:

- `knowledge/README.md`
- `knowledge/community/math-modeling-soft-rules.md`
- `knowledge/community/paper-polish-and-feel.md`
- `knowledge/community/contest-workflow-and-team-execution.md`
- `knowledge/community/literature-search-and-citation-rules.md`
- `knowledge/community/section-duty-soft-rules.md`
- `knowledge/community/visual-evidence-chain-rules.md`
- `knowledge/cumcm/problem-understanding-framework.md`
- `knowledge/latex/v1-4-abstract-closeout-rules.md`
- `knowledge/algorithms/route-selection-protocol.md`
- `knowledge/algorithms/v1-5-route-upgrade-atlas.md`
- `knowledge/cumcm/README.md`
- `prompts/README.md`
- `docs/README.md`
- `inventory/README.md`
- `knowledge/learning-status.md`
- `knowledge/quality/README.md`
- `knowledge/quality/v1-2-quality-matrix.md`
- `knowledge/quality/v1-3-self-review-gate.md`
- `knowledge/quality/v1-4-human-feel-review-gate.md`
- `docs/v1.4-community-learning-plan.md`
- `docs/community-signal-to-rule-pipeline.md`
- `docs/playwright-mcp-public-research.md`
- `docs/local-experience-extraction-queue.md`
- `docs/local-experience-extraction-status.md`
- `docs/v1.4-runbook.md`
- `docs/online-consensus-check-protocol.md`
- `prompts/13_platform_research.md`
- `prompts/12_launch_v1_4.md`
- `docs/v1.4-user-test-protocol.md`
- `docs/architecture.md`
- `inventory/source-map.md`
- `knowledge/cumcm/paper-generation-playbook.md`
- `knowledge/cumcm/20-30-page-paper-blueprint.md`
- `docs/v1.2-draft-contract.md`
- `knowledge/latex/v1-5-award-paper-visual-fingerprint.md`
- `knowledge/algorithms/model-chain-patterns.md`
- `knowledge/algorithms/cards/README.md`
- `docs/visual-generation-pipeline.md`
- `docs/v1.2-final-pass-guide.md`
- `knowledge/quality/quality-rubric-v2.md`

## Project Structure

```text
CLAUDE.md                 Claude Code operating instructions
docs/                     workflow, runbooks, ledgers, review rules
knowledge/                extracted CUMCM knowledge and method rules
paper/                    LaTeX source, figures, tables
problems/                 active problem statement and attachments
prompts/                  phase prompts for the agent
reviews/                  review reports
runs/                     per-run planning and evidence records
scripts/                  scaffold, compile, render, inventory scripts
src/                      data processing, modeling, plotting code
```

## Development Priority

The next major step is not only more reading. It is to prove the v1.2 loop and strengthen the v1.3 methodology layer through stronger demos and real problem trials:

```text
problem -> problem profile -> route decision -> section budget and method depth plan -> code figure/table -> LaTeX draft -> PDF -> review
```

After each trial works, continue deep-reading more official papers and use the findings to improve both the v1.2 pipeline and the v1.3 methodology layer.
