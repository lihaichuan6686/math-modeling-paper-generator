# Rail-Timetable Run Package Manifest

Purpose: show what a near-real v1.2 run package should contain for a rail/timetable route, even before a full contest-grade paper has been generated.

This manifest is a packaging checklist, not a review checklist.

## Minimum Package Contents

### Run Workspace

| Path | Role |
|---|---|
| `runs/<name>/problem-analysis.md` | flow-to-service-to-timetable route logic |
| `runs/<name>/data-inventory.md` | flow, station, and scenario input notes |
| `runs/<name>/model-candidates.md` | rejected and selected route options |
| `runs/<name>/model-plan.md` | service-pattern and timetable structure |
| `runs/<name>/method-depth-plan.md` | support-model-result-validation depth per subquestion |
| `runs/<name>/verification-plan.md` | capacity, tracking, dwell, and scenario evidence plan |
| `runs/<name>/figure-plan.md` | flow, timetable, and validation visuals |
| `runs/<name>/section-budget.md` | page rhythm and artifact allocation |
| `runs/<name>/writing-style-plan.md` | paragraph rhythm and route-aware transitions |
| `runs/<name>/artifact-ledger.md` | claim-to-artifact traceability |

### Generated Outputs

| Path family | Role |
|---|---|
| `runs/<name>/rail_operation_candidates.csv` | operation plan comparison artifact |
| `runs/<name>/rail_selected_operation_plan.csv` | chosen plan artifact |
| `runs/<name>/rail_full_timetable.csv` | machine-readable timetable artifact |
| `runs/<name>/rail_capacity_audit.csv` | capacity evidence |
| `runs/<name>/rail_tracking_audit.csv` | tracking evidence |
| `runs/<name>/rail_dwell_audit.csv` | dwell evidence |
| `runs/<name>/rail_scenario_analysis.csv` | scenario evidence |
| `paper/tables/` | selected-plan, timetable sample, and audit tables |
| `paper/figures/` | flow, timetable, and validation visuals |
| `src/` entry points | reproducible generation path |

### Paper Layer

| Path | Role |
|---|---|
| `paper/sections/01_problem.tex` to `11_conclusion.tex` | full paper body sections |
| `paper/rail_demo.tex` or `paper/main.tex` | main LaTeX entry |
| compiled PDF | research draft when available |

### Review Layer

| Path | Role |
|---|---|
| `reviews/review-<name>.md` | quality review with findings and required repairs |
| machine gate output | missing-artifact and audit-coverage check |

## Minimum Artifact Story

A run package is not yet worth testing unless it can tell this whole story:

```text
flow burden
-> service-pattern choice
-> timetable output
-> capacity/tracking/dwell audits
-> scenario boundary
-> bounded recommendation
```

## Ready-For-Test Signals

Treat the package as ready for user testing only if:

1. the run files are filled rather than placeholder-like;
2. the paper sections can be drafted from those files without inventing a new route;
3. the abstract and conclusion can be rebuilt from the ledger and claim map;
4. the main figure/table captions can be rebuilt from the caption map;
5. the review can explicitly distinguish missing flow evidence, missing timetable evidence, and missing audit evidence.
