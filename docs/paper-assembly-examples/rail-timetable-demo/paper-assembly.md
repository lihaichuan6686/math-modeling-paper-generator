# Rail-Timetable Paper Assembly

Purpose: show how a rail/timetable draft should be assembled into a coherent v1.2 paper with visible demand logic, operation logic, timetable logic, and feasibility logic.

## Question Map

Use one stable three-question map from abstract to conclusion:

1. Where is the effective passenger-flow burden concentrated and what service structure does it suggest?
2. Which large-small-route operation plan is preferred?
3. Can the selected plan be converted into a feasible timetable and does it remain credible under scenario changes?

## Assembly Chain

```text
flow audit
-> overlap-zone justification
-> service-pattern comparison
-> selected operation plan
-> timetable recurrence
-> capacity/tracking/dwell audits
-> scenario comparison
```

## Section Rhythm

| Section | Main job in this family | Typical paper role | Main upstream inputs |
|---|---|---|---|
| `01_problem.tex` | define the demand-to-timetable burden | stabilize the three-layer task early | `problem-analysis.md` |
| `02_analysis.tex` | reject timetable-first thinking | explain why flow evidence must come first | `problem-analysis.md`, `model-candidates.md` |
| `03_assumptions.tex` | state operating simplifications | keep recurrence and audit rules clear | `model-plan.md` |
| `04_symbols.tex` | define timetable and capacity notation | prevent drift across model blocks | `model-plan.md` |
| `05_data.tex` | convert OD or section data into planning inputs | bridge flow evidence to service decisions | `data-inventory.md`, `figure-plan.md` |
| `06_model.tex` | define service-pattern and timetable models | technical center of the paper | `model-plan.md`, `method-depth-plan.md` |
| `07_solution.tex` | explain how selected plan and timetable are generated | show operation-to-timetable execution path | `model-plan.md`, `artifact-ledger.md` |
| `08_results.tex` | show selected plan and timetable artifact | answer Q1 and Q2 with visible outputs | generated tables/figures |
| `09_validation.tex` | show capacity, tracking, dwell, and scenario evidence | answer Q3 with operational credibility | `verification-plan.md`, generated audits |
| `10_strengths_limitations.tex` | explain what this route captures and what it simplifies | keep the paper sounding mature | review findings, route notes |
| `11_conclusion.tex` | close Q1-Q3 in order | state the final operational recommendation | `artifact-ledger.md`, `review-current.md` |

## Run-File To Paper Mapping

| Run file | What it contributes to the paper |
|---|---|
| `problem-analysis.md` | overlap-zone logic, route justification, subquestion map |
| `model-candidates.md` | why timetable-first and service-only routes are incomplete |
| `model-plan.md` | service-pattern comparison logic, recurrence equations, feasibility checks |
| `method-depth-plan.md` | support layer, operation model, timetable artifact, audit layer for each subquestion |
| `verification-plan.md` | capacity/tracking/dwell/scenario evidence in `09_validation.tex` |
| `figure-plan.md` | flow figure, tradeoff figure, timetable figure placement |
| `section-budget.md` | page rhythm and visual distribution |
| `writing-style-plan.md` | paragraph rhythm and route-aware transitions |
| `artifact-ledger.md` | which plan/timetable claims may appear in abstract and conclusion |

## Evidence Distribution

### Early

- one section-flow or OD-based explanatory artifact in analysis or data;
- one statement that identifies the overlap zone before the timetable appears.

### Middle

- one operation-plan comparison artifact;
- one compact explanation of how the timetable recurrence is generated from the selected plan.

### Late

- one selected-plan artifact;
- one timetable artifact;
- separate or clearly distinguishable capacity, tracking, dwell, and scenario artifacts.

The timetable should never be the first serious artifact. The reader must first understand why that service structure exists.

## Subquestion Close-Out Map

| Subquestion | Where the main answer closes | What the close-out sentence should do |
|---|---|---|
| Q1 flow burden | late in `02_analysis.tex` or `05_data.tex` | say what overlap-zone pattern the evidence supports |
| Q2 operation plan | late in `08_results.tex` | say which service pattern is preferred and why |
| Q3 timetable credibility | late in `09_validation.tex` | say what operational checks are passed and what limitation remains |

## Abstract And Conclusion Gate

Only include a claim in the abstract or conclusion if:

1. it appears in a selected-plan table, timetable artifact, or audit/scenario output;
2. it is listed in `artifact-ledger.md`;
3. the wording matches the stable question map.

## Typical Failure To Avoid

- a timetable figure appears before the overlap-zone burden is justified;
- the selected operation plan is named, but no machine-readable timetable exists;
- capacity, tracking, and dwell are merged into one vague validation sentence;
- the paper compares only normalized scores and hides raw service burden;
- the conclusion states a service recommendation without timetable or scenario evidence.
