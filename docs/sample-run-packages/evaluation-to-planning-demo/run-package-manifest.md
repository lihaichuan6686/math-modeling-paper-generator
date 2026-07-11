# Evaluation-to-Planning Run Package Manifest

Purpose: show what a near-real v1.2 run package should contain for an evaluation-to-planning route, even before a full contest-grade paper has been generated.

This manifest is a packaging checklist, not a review checklist.

## Minimum Package Contents

### Run Workspace

| Path | Role |
|---|---|
| `runs/<name>/problem-analysis.md` | route logic and subquestion map |
| `runs/<name>/data-inventory.md` | input fields, units, and preprocessing notes |
| `runs/<name>/model-candidates.md` | rejected and selected route options |
| `runs/<name>/model-plan.md` | score model and plan model structure |
| `runs/<name>/method-depth-plan.md` | support-model-result-validation depth per subquestion |
| `runs/<name>/verification-plan.md` | feasibility and scenario evidence plan |
| `runs/<name>/figure-plan.md` | planned route/evidence/validation visuals |
| `runs/<name>/section-budget.md` | page rhythm and artifact allocation |
| `runs/<name>/writing-style-plan.md` | paragraph rhythm and close-out style |
| `runs/<name>/artifact-ledger.md` | claim-to-artifact traceability |

### Generated Outputs

| Path family | Role |
|---|---|
| `paper/tables/` | indicator, ranking, candidate, plan, feasibility, and scenario artifacts |
| `paper/figures/` | route figure, score/plan evidence, validation evidence |
| `src/` entry points | reproducible generation path |

### Paper Layer

| Path | Role |
|---|---|
| `paper/sections/01_problem.tex` to `11_conclusion.tex` | full paper body sections |
| `paper/main.tex` | main LaTeX entry |
| `paper/main.pdf` | compiled research draft when available |

### Review Layer

| Path | Role |
|---|---|
| `reviews/review-<name>.md` | quality review with findings and required repairs |
| machine gate output | missing-artifact and placeholder check |

## Minimum Artifact Story

A run package is not yet worth testing unless it can tell this whole story:

```text
screening question
-> candidate set
-> executable plan
-> feasibility/scenario boundary
-> bounded recommendation
```

## Ready-For-Test Signals

Treat the package as ready for user testing only if:

1. the run files are filled rather than placeholder-like;
2. the paper sections can be drafted from those files without inventing a new route;
3. the abstract and conclusion can be rebuilt from the ledger and claim map;
4. the main figure/table captions can be rebuilt from the caption map;
5. the review can plausibly return either `Pass` or a sharp `Needs revision`, rather than a vague summary.
