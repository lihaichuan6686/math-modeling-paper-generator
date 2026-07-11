# Evaluation-to-Planning Paper Assembly

Purpose: show how an evaluation-to-planning draft should be assembled into one coherent v1.2 paper rather than a loose stack of sections.

## Question Map

Use one stable three-question map from abstract to conclusion:

1. How should the candidates be evaluated and screened?
2. How should the selected candidates be converted into an executable plan?
3. Is the recommended plan still acceptable under disturbed conditions?

If the paper uses different wording in different sections, the drift should still preserve this same logic.

## Assembly Chain

```text
problem analysis
-> normalized indicator logic
-> candidate screening result
-> executable planning model
-> plan table
-> feasibility/scenario checks
-> abstract and conclusion closure
```

## Section Rhythm

| Section | Main job in this family | Typical paper role | Main upstream inputs |
|---|---|---|---|
| `01_problem.tex` | define the evaluation-plus-decision burden | establish the full task early | `problem-analysis.md` |
| `02_analysis.tex` | justify route choice over ranking-only route | explain why planning must follow evaluation | `problem-analysis.md`, `model-candidates.md` |
| `03_assumptions.tex` | state procurement simplifications | keep later constraints readable | `model-plan.md` |
| `04_symbols.tex` | stabilize notation | prevent formula drift | `model-plan.md` |
| `05_data.tex` | normalize indicators and prepare demand/planning inputs | bridge evaluation variables to decision variables | `data-inventory.md`, `figure-plan.md` |
| `06_model.tex` | define the evaluation layer and planning layer | technical center of the paper | `model-plan.md`, `method-depth-plan.md` |
| `07_solution.tex` | explain the computational route | show ranking-to-plan execution path | `model-plan.md`, `artifact-ledger.md` |
| `08_results.tex` | show ranking, retained candidates, and executable plan | answer Q1 and Q2 with evidence | generated tables, `artifact-ledger.md` |
| `09_validation.tex` | show feasibility and disturbed-scenario evidence | answer Q3 and protect credibility | `verification-plan.md`, generated audits |
| `10_strengths_limitations.tex` | state what this route does well and where it is narrow | keep the paper sounding deliberate | review findings, route notes |
| `11_conclusion.tex` | close Q1-Q3 in order | give the final recommendation | `artifact-ledger.md`, `review-current.md` |

## Run-File To Paper Mapping

| Run file | What it contributes to the paper |
|---|---|
| `problem-analysis.md` | route logic, subquestion map, rejected route explanation |
| `model-candidates.md` | why ranking-only and planning-only routes are insufficient alone |
| `model-plan.md` | equations, constraints, and section-level technical emphasis |
| `method-depth-plan.md` | support layer, main model, result artifact, validation layer for each subquestion |
| `verification-plan.md` | scenario and feasibility evidence in `09_validation.tex` |
| `figure-plan.md` | where the first route/object figure and later evidence figures belong |
| `section-budget.md` | page rhythm and density control |
| `writing-style-plan.md` | paragraph rhythm and subquestion close-out pattern |
| `artifact-ledger.md` | which claims may legally appear in abstract and conclusion |

## Evidence Distribution

### Early

- one route figure or compact route table in analysis;
- one normalized-indicator or retained-candidate artifact before late results.

### Middle

- one equation block or compact algorithm description for evaluation;
- one equation block or constraint system for planning;
- one explanation of how candidate screening reduces the decision space.

### Late

- one ranking artifact;
- one executable plan artifact;
- one feasibility or scenario artifact.

The paper should not hide all evidence until the result section. The reader must already know what object is being modeled and why this route was selected before the final plan appears.

## Subquestion Close-Out Map

| Subquestion | Where the main answer closes | What the close-out sentence should do |
|---|---|---|
| Q1 screening | late in `08_results.tex` | say which suppliers remain credible and why they enter planning |
| Q2 executable plan | late in `08_results.tex` | say what the recommended plan is and what operational burden it resolves |
| Q3 robustness | late in `09_validation.tex` | say what stress the recommendation survives and what limit still remains |

## Abstract And Conclusion Gate

Only include a claim in the abstract or conclusion if:

1. it appears in a table, figure, or explicit model output;
2. it is listed in `artifact-ledger.md`;
3. the wording matches the stable question map.

## Typical Failure To Avoid

- score table appears, but no executable plan is ever shown;
- the plan table appears, but the reader cannot see how the candidate set was chosen;
- scenario analysis is mentioned, but no disturbed artifact appears;
- the conclusion repeats methods instead of final answers;
- evaluation and planning use inconsistent variable language.
