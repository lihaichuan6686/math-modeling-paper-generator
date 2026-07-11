# Verification Plan

Run: example-rail-timetable

| ID | Target | Method | Metric | Evidence file | Status |
|---|---|---|---|---|---|
| V01 | operation-plan rationality | compare selected pattern with baseline candidate | raw cost/service components | `paper/tables/rail_operation_compare.tex` | Planned |
| V02 | section capacity feasibility | audit each selected service segment | utilization status by section | `runs/current/rail_capacity_audit.csv` | Planned |
| V03 | tracking feasibility | audit minimum interval constraints | pass/fail status by train pair | `runs/current/rail_tracking_audit.csv` | Planned |
| V04 | dwell feasibility | audit dwell-time bounds | pass/fail status by stop | `runs/current/rail_dwell_audit.csv` | Planned |
| V05 | recommendation robustness | rerun under demand/headway scenarios | service-cost change summary | `runs/current/rail_scenario_analysis.csv` | Planned |

## Sensitivity Analysis

- increase demand under peak sections;
- change minimum headway within a realistic operating range;
- compare whether the selected pattern or timetable feasibility changes materially.

## Baseline or Sanity Checks

- compare the selected service pattern against one simpler all-stop or uniform-interval baseline;
- verify that the generated timetable is not only drawable but auditable station by station.
