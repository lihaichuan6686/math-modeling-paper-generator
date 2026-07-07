# v1.0 Runbook

Purpose: give Claude Code a direct, usable path from a problem statement to a complete first draft. This is the "small but complete" version of the project.

## v1.0 Philosophy

Do not wait until all local resources have been read.

For v1.0, produce a coherent full pipeline:

```text
understand -> choose route -> model -> compute -> draw -> write -> compile -> review
```

The draft may be imperfect, but it must be complete enough for the user to inspect and guide the next iteration.

## Required Inputs

Minimum:

- `problems/problem.md`

Optional:

- attachments under `problems/`
- data under `problems/data/`
- user notes

## Required Knowledge Files

Read first:

1. `knowledge/README.md`
2. `knowledge/cumcm/paper-generation-playbook.md`
3. `knowledge/cumcm/20-30-page-paper-blueprint.md`
4. `knowledge/algorithms/model-chain-patterns.md`
5. `knowledge/algorithms/cards/README.md`
6. relevant detailed algorithm cards under `knowledge/algorithms/cards/`
7. `docs/visual-generation-pipeline.md`
8. `knowledge/quality/quality-rubric-v2.md`

For train, metro, bus, OD-flow, headway, running-diagram, or timetable problems, also read:

- `knowledge/cumcm/problem-type-paper-archetypes.md`, Type I
- `knowledge/algorithms/cards/rail-timetable-operation.md`
- `knowledge/quality/mathorcup-2023B-v1-test-review.md`

## Step 1: Create Run Scaffold

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\new-run.ps1 -Name current -Problem "short label"
```

If `runs/current/` already exists, inspect it before overwriting. Use `-Force` only when intentionally restarting the run.

For the bundled synthetic demo, run:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\run-v1-demo.ps1 -Name current -Force
```

This creates the run scaffold and generates one demo table and one demo figure from `problems/demo-v1-supply.md`.

The demo script runs the minimum artifact gate automatically. Use `-SkipQualityGate` only while debugging an intentionally incomplete run.

If you intentionally want the demo to become the active problem statement, add:

```powershell
-InstallAsActiveProblem
```

For the bundled rail-timetable route demo, run:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\run-rail-demo.ps1 -Name rail-demo -Force
```

This creates Type I artifacts for operation-plan selection, full timetable output, capacity audit, tracking/dwell audit, scenario analysis, and Chinese-labeled figures.

The rail demo script also runs the minimum artifact gate automatically. Use `-SkipQualityGate` only while debugging an intentionally incomplete run.

To compile the rail-timetable demo paper, run:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\compile.ps1 -Main rail_demo.tex
```

## Step 2: Intake

Follow `prompts/00_intake.md`.

Must produce:

- problem summary;
- subquestion list;
- inputs/outputs/constraints/metrics;
- routing signals;
- data inventory.

## Step 3: Ideation

Follow `prompts/01_ideation.md`.

Must produce at least three route-level candidates.

Candidate examples:

- evaluation -> planning -> scenario audit
- forecast -> optimization -> robustness
- feature extraction -> classifier comparison -> error analysis
- physical/geometric derivation -> numerical optimization -> residual check

## Step 4: Model Plan

Follow `prompts/02_model_plan.md`.

For v1.0, choose a route that can be implemented quickly and visibly. Prefer:

- interpretable baseline models;
- clear equations;
- one or two strong figures;
- one concrete result table;
- validation that can be explained.

## Step 5: Implementation

Follow `prompts/03_implementation.md`.

Minimum v1.0 implementation:

- one runnable script or clearly documented run sequence;
- one generated evidence figure;
- one generated result table;
- stable output paths;
- artifact-ledger entries.

For timetable/service-planning problems, the minimum is higher: full timetable output, operation-plan output, capacity audit, tracking/dwell audit, and a scenario table are required before the run can pass review.

If real data are absent, create a clearly labeled synthetic or illustrative dataset only for demo/testing. Do not present synthetic results as real contest evidence.

## Step 6: Writing

Follow `prompts/04_writing.md`.

Minimum v1.0 paper structure:

- abstract;
- problem restatement;
- problem analysis;
- assumptions;
- symbols;
- data processing;
- model establishment;
- solution process;
- results;
- validation;
- strengths and limitations;
- conclusion;
- references;
- appendix.

The v1.0 paper should look structurally complete, even if later versions improve model depth.

## Step 7: Build

Run:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\compile.ps1
```

If unavailable or blocked, record the failure in the review and keep the LaTeX source coherent.

## Step 8: Review

Follow `prompts/05_review.md`.

Minimum review output:

- overall status;
- blocking issues;
- important issues;
- warnings;
- evidence checked;
- evidence missing;
- human verification needed.

Then run the machine artifact gate:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\check-run-quality.ps1 -Run current
```

For the rail-timetable demo:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\check-run-quality.ps1 -Run rail-demo -Paper rail_demo.tex
```

## v1.0 Definition of Done

The v1.0 toolchain is ready for user inspection when:

- a new problem can be scaffolded;
- Claude Code has a single runbook to follow;
- the paper sections can be filled in order;
- at least one figure/table can be generated and traced;
- LaTeX can be compiled or compile blockers are clearly recorded;
- review output exists.

## Next v1.1 Improvements

After v1.0 works:

- integrate the `rail_timetable` demo artifacts into a full LaTeX paper route;
- improve LaTeX template polish;
- add automated ledger update helpers;
- add demo problem and expected output;
- deepen method coverage by reading `2021 E014`;
- automate review checks where practical.
