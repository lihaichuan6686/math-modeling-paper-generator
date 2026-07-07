# Review Checklist

This checklist is used before a generated or analyzed paper is considered ready for research review. It is designed for CUMCM-style mathematical modeling papers.

Use the following labels:

```text
Pass: evidence is present and consistent.
Warn: issue exists but can be explained or repaired.
Fail: issue undermines correctness, reproducibility, or compliance.
Unknown: evidence is missing.
```

## 1. Problem Coverage

| Item | Status | Evidence |
|---|---|---|
| All subquestions are listed explicitly. | Unknown | |
| Each subquestion has a corresponding model or method. | Unknown | |
| Each subquestion has at least one result. | Unknown | |
| Each subquestion has validation or sanity checking. | Unknown | |
| The conclusion answers the original questions, not only the model tasks. | Unknown | |

Fail conditions:

- A subquestion is skipped.
- A result is asserted without a model, computation, or clear reasoning.
- The paper solves a different problem from the given statement.

## 2. Model Logic

| Item | Status | Evidence |
|---|---|---|
| Assumptions are stated and justified. | Unknown | |
| Variables and parameters are defined. | Unknown | |
| Objective functions match the problem goals. | Unknown | |
| Constraints match real-world or problem-stated limits. | Unknown | |
| Solution algorithms fit the data size and problem type. | Unknown | |
| Model limitations are acknowledged. | Unknown | |

Fail conditions:

- Variables appear in formulas but are never defined.
- Constraints are missing for a decision model.
- The chosen method is not suitable for the data or task.
- The model chain is a list of algorithms without mathematical connection.

## 3. Data and Code Reproducibility

| Item | Status | Evidence |
|---|---|---|
| Raw data files are listed. | Unknown | |
| Data cleaning steps are documented. | Unknown | |
| Code can be run from a clear entry point. | Unknown | |
| Random seeds or repeated-trial summaries are recorded. | Unknown | |
| Tables in the paper are traceable to code or calculations. | Unknown | |
| Figures are generated from known scripts or documented sources. | Unknown | |
| Abstract numbers match final result files. | Unknown | |

Fail conditions:

- Important numbers cannot be reproduced.
- Code and paper use different parameter values.
- Static images replace actual generated figures without explanation.
- Data columns or units are ambiguous.

## 4. Figures and Tables

| Item | Status | Evidence |
|---|---|---|
| Every figure has a title/caption. | Unknown | |
| Every table has a title/caption. | Unknown | |
| Axes and units are present when applicable. | Unknown | |
| Every figure/table is cited in the text. | Unknown | |
| Figure/table numbering is consistent. | Unknown | |
| Tables are readable after PDF rendering. | Unknown | |

Fail conditions:

- A figure is included but never discussed.
- A table is too wide or clipped.
- Units or labels are missing for quantitative axes.
- The same result appears with conflicting values.

## 5. Validation and Robustness

| Item | Status | Evidence |
|---|---|---|
| At least one validation strategy is used. | Unknown | |
| Sensitivity analysis is included when parameters matter. | Unknown | |
| Prediction models have error metrics. | Unknown | |
| Classification models have more than accuracy. | Unknown | |
| Optimization results have feasibility checks. | Unknown | |
| Physical/business sanity checks are included where relevant. | Unknown | |
| Timetable/service-planning outputs include full machine-readable schedules when required. | Unknown | |
| Timetable/service-planning drafts include capacity, headway/tracking, and dwell audits. | Unknown | |

Fail conditions:

- The paper only reports optimal results and no verification.
- Accuracy is reported without data split details.
- Optimization solutions violate stated constraints.
- Sensitivity analysis has no perturbation range.
- A timetable figure is shown but the full timetable artifact or feasibility audit is missing.

## 6. Writing Quality

| Item | Status | Evidence |
|---|---|---|
| Abstract follows problem-by-problem structure. | Unknown | |
| Abstract includes verified results. | Unknown | |
| Problem analysis explains why each model is chosen. | Unknown | |
| Sections are ordered logically. | Unknown | |
| Claims distinguish evidence, assumption, and inference. | Unknown | |
| Limitations are concrete rather than generic. | Unknown | |

Fail conditions:

- Abstract is only background and method names.
- Conclusion repeats abstract without decision value.
- Writing uses generic template filler.
- The paper overclaims beyond data support.

## 7. LaTeX and PDF Quality

| Item | Status | Evidence |
|---|---|---|
| PDF compiles successfully. | Unknown | |
| No missing figures or broken references. | Unknown | |
| Chinese fonts render correctly. | Unknown | |
| Tables do not overflow pages. | Unknown | |
| Equations are readable and numbered when referenced. | Unknown | |
| References render correctly. | Unknown | |
| Research copy removes team identity and stale template metadata when required. | Unknown | |

Fail conditions:

- PDF cannot be compiled.
- Font missing or unreadable text appears.
- Cover/number page appears in a research copy when it should not.
- Template default names, dates, or school fields remain.

## 8. Responsible-Use Review

| Item | Status | Evidence |
|---|---|---|
| Use case is research, post-contest review, education, or authorized quality checking. | Unknown | |
| No fabricated data, citations, or experiments. | Unknown | |
| No instruction to hide prohibited AI involvement. | Unknown | |
| No attempt to produce an active contest submission. | Unknown | |
| Limitations and uncertainty are visible to reviewers. | Unknown | |

Fail conditions:

- The request is for active competition cheating.
- The output fabricates evidence or citations.
- The user asks to conceal AI authorship in a prohibited setting.
- The paper is framed as verified when key evidence is missing.

## Required Review Output

Each review should produce:

```text
Summary:
Major risks:
Required fixes:
Warnings:
Evidence checked:
Unchecked evidence:
Final status: Pass / Needs revision / Reject for research use
```

## Machine Gate

Before accepting a run, execute the minimum artifact gate:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\check-run-quality.ps1 -Run current
```

For a named run and paper source:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\check-run-quality.ps1 -Run rail-demo -Paper rail_demo.tex
```

This does not replace human review. It only catches missing ledgers, placeholder reviews, missing Type I timetable artifacts, empty CSV outputs, and failing audit status fields.

## Minimum Pass Criteria

A paper can pass research review only if:

1. All subquestions are answered.
2. Main results are reproducible or explicitly marked as illustrative.
3. The PDF compiles and renders correctly.
4. There are no known fabricated citations or data.
5. Responsible-use constraints are satisfied.
6. Remaining limitations are clearly disclosed.
