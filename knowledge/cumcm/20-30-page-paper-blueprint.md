# 20-30 Page CUMCM Paper Blueprint

Purpose: make paper length emerge from structure, figures, tables, formulas, validation, and appendix evidence rather than filler prose.

## Core Rule

A complete CUMCM paper should feel like a chain of deliverables:

```text
problem restatement -> route analysis -> assumptions/symbols -> data evidence -> model equations -> computation -> results -> validation -> limitations -> appendix
```

For a 20-30 page paper, do not ask "how do we add pages?" Ask "which required evidence is still missing?"

## Page Budget

| Section | Target pages | Minimum artifacts | Main job |
| --- | ---: | --- | --- |
| Abstract | 1 | method/result sentence for each subquestion | compress the whole solution |
| Problem restatement | 1-2 | subquestion table | translate the problem into tasks |
| Method overview | 1 | route diagram | show the full model chain early |
| Problem analysis | 2-4 | subquestion dependency diagram or route table | explain why each model is needed |
| Assumptions | 0.5-1 | assumption-impact table | make simplifications auditable |
| Symbol table | 0.5-1 | symbol/domain table | keep formulas and code consistent |
| Data processing | 2-4 | data inventory, cleaning table, 2-3 exploratory plots | turn raw data into model inputs |
| Model establishment | 6-10 | equations, constraints, algorithm definitions | provide mathematical substance |
| Solution process | 2-4 | algorithm steps, solver settings, data-flow figure | bridge model and code |
| Results | 2-4 | result tables, evidence figures | answer subquestions with outputs |
| Validation and sensitivity | 2-4 | residual/metric/feasibility/sensitivity artifacts | prove the answer is not accidental |
| Strengths and limitations | 1 | limitation-remedy table | show honest scope control |
| Conclusion | 0.5-1 | decision summary | state final recommendations |
| References | 0.5-1 | real sources only | support methods and background |
| Appendix | 3-8 | code inventory, extra tables, run notes | make results reproducible |

## Minimum Visual Density

For a full paper, plan at least:

- 1 route or workflow figure.
- 2 explanatory figures for model structure, geometry, mechanism, or process.
- 3-6 evidence figures generated from data, code, or model output.
- 3-8 result or parameter tables.
- 1-3 validation or sensitivity figures/tables.
- 1 appendix inventory table linking files to subquestions.

## Section Build Order

Recommended writing sequence:

1. Build `problem-analysis.md`.
2. Build `figure-plan.md` and `artifact-ledger.md`.
3. Write model plan and verification plan.
4. Implement code and generate tables/figures.
5. Draft model, solution, results, and validation sections.
6. Draft problem restatement, assumptions, symbols, and data sections.
7. Write strengths, limitations, conclusion, references, and appendix.
8. Write abstract last.
9. Compile and inspect PDF page by page.

## Per-Subquestion Contract

Every subquestion should appear in four places:

| Location | Required content |
| --- | --- |
| Problem analysis | what the subquestion asks and why the route fits |
| Model establishment | variables, formulas, constraints, or algorithm definition |
| Results | numerical or categorical answer, with table/figure |
| Validation | feasibility, error, sensitivity, baseline, or consistency check |

If a subquestion appears in only one or two places, the paper is structurally weak.

## E-Route Expansion Guide

When the problem is E-type, page length should emerge from route-specific evidence rather than generic narration.

### Production-route E paper

Recommended evidence chain:

```text
material screening
-> forecast evidence
-> service-level / safety-stock evidence
-> rolling production rule
-> executable production tables
-> scenario comparison
-> appendix file list and code
```

Good page growth sources:

- representative-material demand figures;
- actual-vs-forecast comparison tables;
- service-level and support-rate tables;
- coefficient-band or policy-parameter explanation tables;
- scenario comparison under different capacity assumptions.

Minimum route check:

- forecasting does not end the paper;
- at least one production table is executable;
- service-level or support metrics are shown for key materials.

### Monitoring-route E paper

Recommended evidence chain:

```text
data cleaning
-> relation analysis
-> seasonality / periodicity / abruptness diagnosis
-> forecast evidence
-> monitoring or policy decision model
-> intervention-effect comparison
-> long-horizon consequence analysis
-> support-material tree
```

Good page growth sources:

- diagnostic figures such as wavelet, abruptness, or seasonality evidence;
- forecast-versus-history comparison;
- monitoring-plan tables;
- intervention-effect figures;
- counterfactual or long-horizon consequence tables;
- multi-tool appendix traceability.

Minimum route check:

- diagnostics are tied to subquestions, not just method-dumped;
- prediction feeds a decision layer;
- appendix maps files to questions.

## Figure Chain Contract

Each planned figure must have:

```text
role -> data/source -> generation method -> output path -> caption -> section reference -> review status
```

Figure roles:

- Route figure: explains the whole workflow.
- Explanatory figure: explains a mechanism, geometry, system, or algorithm.
- Evidence figure: comes from data or model output.
- Validation figure: shows residuals, sensitivity, uncertainty, feasibility, or comparison.

AI-generated or hand-drawn figures may be used only for route or explanatory roles unless their inputs are reproducible data. They must be labeled and recorded in the artifact ledger.

## Anti-Filler Checks

Remove or rewrite a paragraph if:

- it repeats the problem statement without analysis;
- it names an algorithm without variables, equations, or validation;
- it describes a figure but the figure adds no evidence;
- it expands background that is not used later;
- it gives a conclusion that is not traceable to a result table or figure.

## Abstract Completion Gate

Do not finalize the abstract until:

- each subquestion has a verified method and result;
- all numbers in the abstract appear in results or validation tables;
- validation method is named;
- keywords match the actual model chain;
- the abstract does not promise unsupported generality.

## Final PDF Inspection Checklist

Before calling the paper complete:

- Page count comes from section roles and artifacts, not filler.
- Every figure is referenced in text and has a useful caption.
- Every table has a title, units when needed, and source path in the ledger.
- Equation numbering is consistent.
- Symbols used in formulas appear in the symbol table.
- Results in abstract, conclusion, tables, and code outputs agree.
- Appendix lists code files and output artifacts by subquestion.

## Route-Specific Completion Checks

For production-route E papers, confirm:

- key materials are justified;
- forecast outputs feed inventory, service-level, or production quantities;
- rolling rules or update equations are explained;
- at least one scenario or capacity comparison is visible.

For monitoring-route E papers, confirm:

- diagnostic methods are mapped to specific subquestions;
- forecast outputs feed monitoring or policy decisions;
- intervention or counterfactual evidence is visible when claimed;
- appendix traceability covers mixed tools and generated artifacts.
