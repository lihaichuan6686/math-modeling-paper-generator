# Run Artifact Index

Purpose: show the standard files and folders that a generation run should produce, including the stronger v1.2 planning artifacts.

This is the artifact map for the run lifecycle.

## Standard Run Artifacts

| Artifact | Produced when | What it means |
|---|---|---|
| `runs/current/problem-analysis.md` | intake | the problem has been summarized and split into subquestions |
| `runs/current/data-inventory.md` | intake | the available files, fields, and units have been recorded |
| `runs/current/model-candidates.md` | ideation | multiple route-level options have been proposed |
| `runs/current/model-plan.md` | model plan | one route has been chosen and formalized |
| `runs/current/method-depth-plan.md` | v1.2 model plan | major subquestions have support, result, and validation depth targets |
| `runs/current/verification-plan.md` | model plan | the model will be checked with a concrete validation plan |
| `runs/current/figure-plan.md` | model plan | the expected figure set has been planned before coding |
| `runs/current/section-budget.md` | v1.2 writing prep | the paper length is allocated by section role rather than filler |
| `runs/current/writing-style-plan.md` | v1.2 writing prep | the target human-team voice and paragraph density are fixed before drafting |
| `runs/current/artifact-ledger.md` | intake through implementation | the paper claims are connected to outputs and sources |
| `src/` outputs | implementation | the computation exists in runnable or reproducible form |
| `paper/figures/` | implementation | the paper's visual evidence has been generated |
| `paper/tables/` | implementation | the paper's table evidence has been generated |
| `paper/sections/` | writing | the paper body has been assembled by section |
| `paper/main.tex` | writing | the paper has a single main LaTeX entry point |
| `paper/main.pdf` | build | the paper has been compiled and rendered |
| `reviews/review-current.md` | review | the paper has been evaluated as a research artifact |
| `docs/v1.2-final-pass-guide.md` | final pass | the draft can be checked against one shorter handoff sequence before claiming readiness |

## Folder Roles

| Folder | Primary use |
|---|---|
| `paper/figures/` | final figures to cite in the paper |
| `paper/tables/` | final tables to cite in the paper |
| `paper/sections/` | section-level LaTeX source |
| `runs/current/` | run-specific planning, evidence, and traceability files |
| `reviews/` | review output and handoff status |
| `src/` | runnable scripts and reusable computation code |

## Run Stage Chain

```text
problem-analysis
-> data-inventory
-> model-candidates
-> model-plan
-> method-depth-plan
-> verification-plan
-> figure-plan
-> section-budget
-> writing-style-plan
-> artifact-ledger
-> src outputs
-> paper/figures and paper/tables
-> paper/sections and paper/main.tex
-> paper/main.pdf
-> review-current
```

## Completion Rule

A run is easier to trust when every stage leaves behind a file or folder that can be inspected later.

If a stage is skipped, explain why in the review and mark the missing evidence as `Unknown`.

## Best Use

Read this note together with:

- `workflow.md`
- `artifact-ledger-template.md`
- `prompts/flow-map.md`
- `knowledge/quality/evidence-family-index.md`
