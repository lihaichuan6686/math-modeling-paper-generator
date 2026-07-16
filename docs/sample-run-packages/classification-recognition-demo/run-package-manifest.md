# Classification-Recognition Run Package Manifest

Purpose: show what a near-real v1.2 run package should contain for a classification or recognition route before it is pressure-tested.

This manifest is a packaging checklist, not a review checklist.

## Minimum Package Contents

### Run Workspace

| Path | Role |
|---|---|
| `runs/<name>/problem-profile.md` | labeled sample object and recognition decision object |
| `runs/<name>/problem-analysis.md` | preprocessing, class structure, and recognition burden |
| `runs/<name>/route-decision.md` | preprocessing -> features -> classifier -> error route choice |
| `runs/<name>/model-plan.md` | feature route and classifier comparison structure |
| `runs/<name>/verification-plan.md` | split, leakage, and class-level validation plan |
| `runs/<name>/figure-plan.md` | workflow, feature, and confusion visuals |
| `runs/<name>/section-budget.md` | page rhythm and artifact allocation |
| `runs/<name>/writing-style-plan.md` | class-aware paragraph rhythm |
| `runs/<name>/artifact-ledger.md` | claim-to-artifact traceability |
| `runs/<name>/calibration-log.md` | pressure-test result when available |

### Generated Outputs

| Path family | Role |
|---|---|
| preprocessing summary | data cleaning and leakage-control evidence |
| feature artifact | usable input representation |
| classifier comparison table | model choice evidence |
| confusion or error artifact | class-level behavior evidence |
| recognition summary table | scoped final rule |
| `paper/tables/` | preprocessing, comparison, and recognition tables |
| `paper/figures/` | workflow, feature, and error visuals |
| `src/` entry points | reproducible generation path |

### Review Layer

| Path | Role |
|---|---|
| `reviews/review-<name>.md` | quality review with findings and required repairs |
| `reviews/calibration-<name>.md` | pressure-test log and write-back decision |

## Minimum Artifact Story

A run package is not yet worth testing unless it can tell this whole story:

```text
preprocessing and split policy
-> feature representation
-> classifier comparison
-> class-level error behavior
-> scoped recognition rule
```

## Ready-For-Test Signals

Treat the package as ready for pressure testing only if:

1. preprocessing is described as part of the model route;
2. classifier choice is backed by more than one global score;
3. confusion or class-level error evidence exists;
4. the conclusion can state both usable classes and remaining error risk;
5. the calibration log can distinguish metric dumping from real recognition evidence.
