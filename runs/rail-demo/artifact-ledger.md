# Artifact Ledger

Run: rail-demo
Date: 2026-07-07
Purpose: synthetic rail-timetable route demo for the math-modeling paper generator.

## Run Metadata

| Field | Value |
|---|---|
| Run ID | rail-demo |
| Problem type | Type I: Rail Transit Timetable And Service Planning |
| Code entry point | `src/rail_timetable_demo.py` |
| Paper source | `paper/rail_demo.tex` |
| PDF output | `paper/rail_demo.pdf` after compile |
| Data | Synthetic line, section flow, and operating parameters embedded in script |
| Research status | Demo route, not contest evidence |

## Required Type I Artifacts

| Artifact | Path | Status |
|---|---|---|
| operation candidates | `runs/rail-demo/rail_operation_candidates.csv` | generated |
| selected operation plan | `runs/rail-demo/rail_selected_operation_plan.csv` | generated |
| full timetable | `runs/rail-demo/rail_full_timetable.csv` | generated |
| capacity audit | `runs/rail-demo/rail_capacity_audit.csv` | generated |
| tracking audit | `runs/rail-demo/rail_tracking_audit.csv` | generated |
| dwell audit | `runs/rail-demo/rail_dwell_audit.csv` | generated |
| scenario analysis | `runs/rail-demo/rail_scenario_analysis.csv` | generated |

## Figures

| ID | Role | File | Paper label | Status |
|---|---|---|---|---|
| F01 | evidence | `paper/figures/rail_section_flow.png` | `fig:rail-section-flow` | generated |
| F02 | evidence | `paper/figures/rail_cost_service_tradeoff.png` | `fig:rail-cost-service` | generated |
| F03 | evidence | `paper/figures/rail_timetable_diagram.png` | `fig:rail-timetable` | generated |

## Tables

| ID | File | Paper label | Status |
|---|---|---|---|
| T01 | `paper/tables/rail_operation_candidates.tex` | `tab:rail-operation-candidates` | generated |
| T02 | `paper/tables/rail_capacity_audit.tex` | `tab:rail-capacity-audit` | generated |
| T03 | `paper/tables/rail_timetable_sample.tex` | `tab:rail-timetable-sample` | generated |
| T04 | `paper/tables/rail_scenario_analysis.tex` | `tab:rail-scenario-analysis` | generated |

## Key Results

| ID | Statement | Value | Evidence |
|---|---|---:|---|
| K01 | selected small route start | 4 | candidate table |
| K02 | selected small route end | 10 | candidate table |
| K03 | big route train count | 12 | selected plan |
| K04 | small route train count | 13 | selected plan |
| K05 | minimum capacity margin | 4600 | capacity audit |
| K06 | minimum tracking gap | 144.0 | tracking audit |
| K07 | maximum dwell time | 20.4 | timetable and dwell audit |

## Review Summary

Generated-artifact status: Pass. `paper/rail_demo.tex` is the compact paper source; compile and rendered-page inspection remain separate verification steps.
Machine gate: `scripts/check-run-quality.ps1 -Run rail-demo -Paper rail_demo.tex` passed.
