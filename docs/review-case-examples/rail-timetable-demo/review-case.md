# Rail-Timetable Review Case

Purpose: show how to review a weak rail/timetable draft that has visible timetable artifacts but still lacks contest-grade operational credibility.

## Draft Situation

Assume the draft has these visible weaknesses:

- the paper includes a timetable figure and one selected-plan table;
- the overlap-zone burden is only lightly justified;
- capacity, tracking, and dwell checks are mentioned together but not separated clearly;
- the scenario discussion is brief and does not visibly support the final recommendation.

## Example Review Output

```markdown
# Paper Quality Review

Run: example-rail-timetable
Reviewed: example review case

## Overall Status

Needs revision

## Critical Findings

| ID | Location | Status | Evidence | Risk | Required repair |
|---|---|---|---|---|---|
| C01 | `05_data.tex`, `02_analysis.tex` | Fail | The overlap-zone burden is asserted, but the flow evidence is too thin to justify the later service-pattern choice confidently. | The selected operation plan may appear arbitrary. | Strengthen the flow audit with one clearer section-flow or OD-derived artifact and interpret the overlap-zone logic explicitly. |
| C02 | `09_validation.tex` | Fail | Capacity, tracking, and dwell feasibility are mentioned, but the draft does not keep them visibly distinct. | The timetable may look credible without actually proving operational feasibility. | Split the audit layer into separate capacity, tracking, and dwell evidence with explicit findings for each. |

## Important Findings

| ID | Location | Status | Evidence | Risk | Required repair |
|---|---|---|---|---|---|
| I01 | `08_results.tex` | Warn | The selected-plan table and timetable figure are present, but the prose does not fully explain how the selected plan materializes into the timetable structure. | The route between service design and timetable recurrence remains too implicit. | Add a clearer interpretation paragraph connecting the selected plan to the timetable consequence. |
| I02 | conclusion, `artifact-ledger.md` | Warn | The final recommendation sounds more definitive than the visible scenario evidence supports. | The paper may overstate robustness. | Rebuild the close-out against the claim map and scenario artifacts. |
| I03 | `09_validation.tex`, scenario outputs | Warn | The scenario section is present but thin relative to the strength of the final recommendation. | The paper does not yet look contest-grade in robustness. | Add a clearer scenario comparison artifact and interpret what remains feasible. |

## Warnings

| ID | Location | Status | Evidence | Risk | Suggested repair |
|---|---|---|---|---|---|
| W01 | abstract | Warn | The abstract mentions timetable feasibility, but the audit burden is not spelled out clearly enough. | The abstract may sound stronger than the visible evidence. | Rewrite the abstract using the rail claim map so the audit boundary is explicit. |
| W02 | figures/tables | Warn | The timetable figure is visually stronger than the flow evidence and audit evidence. | The visual emphasis may mislead the reader about what has actually been proven. | Rebalance the visuals so flow evidence and audits remain visible. |

## Evidence Checked

- route logic and question map
- flow evidence presence
- selected-plan and timetable artifacts
- validation separation
- abstract and conclusion claim support

## Evidence Missing Or Not Checked

- rendered PDF readability
- full machine-readable timetable output
- final machine gate result

## Required Repairs Before Pass

1. Strengthen the overlap-zone justification so the service pattern is visibly evidence-driven.
2. Separate capacity, tracking, and dwell audits into distinct validation evidence.
3. Rebuild abstract and conclusion claims against the claim map and scenario support.

## Human Verification Needed

- Confirm whether the operating assumptions are intended as illustrative simplifications or route-final constraints.

## Responsible-Use Notes

- This draft should remain a research draft until the operational feasibility evidence is made explicit and traceable.
```

## What This Case Teaches

1. A timetable figure is not enough; the flow burden and audit burden must both be visible.
2. The right review should attack missing operational evidence, not just ask for "more analysis".
3. Strong recommendations with thin scenario support should be downgraded until the evidence catches up.

