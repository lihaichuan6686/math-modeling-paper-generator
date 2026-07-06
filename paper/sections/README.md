# Section Authoring Guide

This directory contains the body sections included by `paper/main.tex`.

When generating a CUMCM-style paper, follow the contract in:

```text
knowledge/latex/cumcm-section-contract.md
knowledge/cumcm/paper-generation-playbook.md
docs/figure-plan-template.md
docs/artifact-ledger-template.md
```

## Section Responsibilities

| File | Role | Typical pages |
|---|---|---:|
| `01_problem.tex` | Problem restatement, inputs, outputs, constraints | 1-2 |
| `02_analysis.tex` | Route selection and subquestion analysis | 2-4 |
| `03_assumptions.tex` | Assumptions and reasons | 0.5-1 |
| `04_symbols.tex` | Symbol table | 0.5-1 |
| `05_data.tex` | Data processing and exploratory analysis | 2-4 |
| `06_model.tex` | Mathematical model establishment | 5-9 |
| `07_solution.tex` | Algorithms, parameters, solver process | 3-5 |
| `08_results.tex` | Results for each subquestion | 3-5 |
| `09_validation.tex` | Robustness, sensitivity, error checks | 2-4 |
| `10_strengths_limitations.tex` | Strengths, limits, extensions | 1-2 |
| `11_conclusion.tex` | Final answers and recommendations | 0.5-1 |

## Figure Placement

- Route/workflow figures usually belong in `02_analysis.tex`.
- Explanatory schematics belong near the model they explain, usually `06_model.tex`.
- Data exploration figures belong in `05_data.tex`.
- Result figures belong in `08_results.tex`.
- Sensitivity, residual, and robustness figures belong in `09_validation.tex`.

All figures must be recorded in `runs/current/artifact-ledger.md`.

## LaTeX Rules

- Define every symbol before using it heavily.
- Use `\label{...}` for figures, tables, and equations that are referenced.
- Use stable figure filenames under `paper/figures/`.
- Use stable table files under `paper/tables/` when possible.
- Avoid hard-coded template identity fields in research copies.
- Do not insert a figure unless the text explains what it proves or clarifies.

## Review Before Build

Before compiling, check:

1. Every subquestion appears in analysis, model, results, and validation.
2. Every figure and table is cited in text.
3. Every result in the abstract is already present in `08_results.tex` or `09_validation.tex`.
4. No placeholder references, dates, names, or team fields remain.
5. The appendix points to runnable source files instead of being the only code location.
