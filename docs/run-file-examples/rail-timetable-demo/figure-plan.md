# Figure Plan

Run: example-rail-timetable

## Figure Strategy

Planned family emphasis:

- 1 route/workflow figure;
- 1 explanatory figure for service-pattern logic;
- 2 evidence/result figures;
- 2 validation figures.

## Planned Figures

| ID | Role | Purpose | Paper section | Source type | Tool | Input data/source/prompt | Output path | Caption draft | Status |
|---|---|---|---|---|---|---|---|---|---|
| F01 | route | show the full flow-to-timetable route | Method overview | schematic | Mermaid/TikZ | route statement and subquestion flow | `paper/figures/rail_route_workflow.png` | Overall route from passenger-flow audit to timetable feasibility and scenario recommendation. | planned |
| F02 | explanatory | explain candidate service-pattern structure | Model establishment | schematic | Mermaid/TikZ | service-pattern design logic | `paper/figures/rail_service_pattern_logic.png` | Candidate service-pattern logic used before timetable generation. | planned |
| F03 | evidence | show section passenger-flow profile | Data processing | reproducible code | Python | OD or section-flow data | `paper/figures/rail_section_flow_profile.png` | Section passenger-flow profile that motivates the selected service pattern. | planned |
| F04 | evidence | show timetable or tradeoff output | Results | reproducible code | Python | selected plan and timetable outputs | `paper/figures/rail_timetable_or_tradeoff.png` | Selected operation plan and timetable consequence under the chosen service pattern. | planned |
| F05 | validation | show capacity or utilization check | Validation | reproducible code | Python | capacity audit outputs | `paper/figures/rail_capacity_validation.png` | Section-capacity validation for the selected operation plan. | planned |
| F06 | validation | show scenario effect on service-cost tradeoff | Validation | reproducible code | Python | scenario outputs | `paper/figures/rail_scenario_validation.png` | Scenario comparison of the selected service pattern under perturbed demand or interval assumptions. | planned |

## Review Questions

1. Does the first strong figure show the passenger-flow and service-pattern logic before timetable details dominate?
2. Does at least one evidence figure show a code-generated timetable or tradeoff consequence?
3. Do the validation figures separately cover feasibility and scenario robustness?
