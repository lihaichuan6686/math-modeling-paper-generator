# Verification Plan

Run: example-evaluation-to-planning

| ID | Target | Method | Metric | Evidence file | Status |
|---|---|---|---|---|---|
| V01 | supplier ranking stability | perturb weights and compare top set | rank change count / top-set overlap | `paper/tables/eval_rank_stability.tex` | Planned |
| V02 | plan feasibility | audit demand and capacity constraints | violation count, unmet demand | `paper/tables/plan_feasibility_audit.tex` | Planned |
| V03 | recommendation robustness | rerun under several scenarios | total cost / service change | `paper/tables/plan_scenario_compare.tex` | Planned |

## Sensitivity Analysis

- increase demand by 5%, 10%, and 15%;
- reduce one key supplier capacity by a fixed percentage;
- compare whether the selected candidate set or total plan structure changes materially.

## Baseline or Sanity Checks

- compare the optimized plan with a naive top-ranked-only allocation baseline;
- verify that the final recommendation still respects all hard constraints.
