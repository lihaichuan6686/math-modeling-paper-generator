# Forecast-to-Decision Run Package Manifest

Purpose: show what a near-real v1.2 run package should contain for a forecast-to-decision route before it is pressure-tested.

This manifest is a packaging checklist, not a review checklist.

## Minimum Package Contents

### Run Workspace

| Path | Role |
|---|---|
| `runs/<name>/problem-profile.md` | modeled object, decision object, and family fit |
| `runs/<name>/problem-analysis.md` | trend, uncertainty, and downstream decision burden |
| `runs/<name>/route-decision.md` | forecast -> decision -> scenario route choice |
| `runs/<name>/model-plan.md` | forecast model plus decision model structure |
| `runs/<name>/verification-plan.md` | residual/backtest and scenario evidence plan |
| `runs/<name>/figure-plan.md` | trend, forecast, decision, and scenario visuals |
| `runs/<name>/section-budget.md` | page rhythm and artifact allocation |
| `runs/<name>/writing-style-plan.md` | uncertainty-aware paragraph rhythm |
| `runs/<name>/artifact-ledger.md` | claim-to-artifact traceability |
| `runs/<name>/calibration-log.md` | pressure-test result when available |

### Generated Outputs

| Path family | Role |
|---|---|
| forecast table or plot | future parameter evidence |
| residual/backtest artifact | forecast credibility evidence |
| downstream decision table | final decision artifact |
| scenario comparison table | uncertainty propagation evidence |
| `paper/tables/` | forecast, decision, and scenario tables |
| `paper/figures/` | trend, forecast, and scenario visuals |
| `src/` entry points | reproducible generation path |

### Review Layer

| Path | Role |
|---|---|
| `reviews/review-<name>.md` | quality review with findings and required repairs |
| `reviews/calibration-<name>.md` | pressure-test log and write-back decision |

## Minimum Artifact Story

A run package is not yet worth testing unless it can tell this whole story:

```text
historical signal
-> forecast with error evidence
-> downstream decision
-> scenario/uncertainty boundary
-> bounded recommendation
```

## Ready-For-Test Signals

Treat the package as ready for pressure testing only if:

1. the forecast output is tied to decision parameters;
2. the decision artifact exists outside the forecast section;
3. at least one uncertainty or scenario artifact is planned;
4. the abstract and conclusion can be rewritten without certainty overreach;
5. the calibration log can classify failures into route, evidence, writing, or claim-boundary buckets.
