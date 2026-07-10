# Math Modeling Paper Generator

A research-only Claude Code workspace for generating and reviewing CUMCM-style mathematical modeling paper drafts.

The near-term goal is a usable **v1.0 closed loop**:

```text
problem statement
-> run scaffold
-> problem analysis
-> model route selection
-> model plan
-> code-generated figures/tables
-> LaTeX paper draft
-> PDF build
-> self-review report
```

This v1.0 is intentionally small but complete. It should produce a full-length, plausible research draft that can be inspected and improved, even if later versions are stronger.

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

3. Ask Claude Code to follow:

```text
docs/v1-runbook.md
```

4. Claude Code should work through:

```text
prompts/README.md
prompts/00_intake.md
prompts/01_ideation.md
prompts/02_model_plan.md
prompts/03_implementation.md
prompts/04_writing.md
prompts/05_review.md
prompts/06_quality_review.md
```

5. Compile the paper:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\compile.ps1
```

## v1.0 Expected Outputs

A completed v1.0 run should contain:

- `runs/current/problem-analysis.md`
- `runs/current/data-inventory.md`
- `runs/current/model-candidates.md`
- `runs/current/model-plan.md`
- `runs/current/verification-plan.md`
- `runs/current/figure-plan.md`
- `runs/current/artifact-ledger.md`
- generated figures under `paper/figures/`
- generated tables under `paper/tables/`
- LaTeX source under `paper/`
- a compiled PDF when the local LaTeX environment is available
- `reviews/review-current.md` or `reviews/review-<run>.md`

## Important Knowledge Entry Points

Read these before generation or review:

- `knowledge/README.md`
- `knowledge/cumcm/README.md`
- `prompts/README.md`
- `docs/README.md`
- `inventory/README.md`
- `knowledge/quality/README.md`
- `docs/architecture.md`
- `knowledge/cumcm/paper-generation-playbook.md`
- `knowledge/cumcm/20-30-page-paper-blueprint.md`
- `knowledge/algorithms/model-chain-patterns.md`
- `knowledge/algorithms/cards/README.md`
- `docs/visual-generation-pipeline.md`
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

The next major step is not more reading. It is to prove the v1.0 loop by running a small demo:

```text
toy problem -> scaffold -> code figure/table -> LaTeX draft -> PDF -> review
```

After the demo works, continue deep-reading more official papers and use the findings to improve the v1.0 pipeline.
