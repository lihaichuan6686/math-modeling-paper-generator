# Paper Quality Rubric v2

Purpose: support research review and future official-style paper-quality checking for CUMCM-style mathematical modeling papers. This rubric evaluates quality, traceability, and risk. It is not a detector for authorship and must not be used as a simple "human vs AI" classifier.

## Rating Labels

Use these labels for every check:

```text
Pass: evidence is present and consistent.
Warn: issue exists but can be repaired or disclosed.
Fail: issue undermines correctness, reproducibility, compliance, or trust.
Unknown: evidence is missing or cannot be inspected.
```

Each finding should include:

```text
item -> label -> evidence location -> risk -> repair suggestion
```

## Dimension 1: Problem Coverage

Pass indicators:

- All subquestions are listed.
- Each subquestion has a model, result, and validation path.
- Final conclusions answer the original problem, not only intermediate model tasks.

Fail indicators:

- Any subquestion is skipped.
- Subquestion numbering or naming drifts between abstract, body, and conclusion.
- A result is asserted without evidence.
- The paper solves a different or easier problem.

Required evidence:

- problem-analysis file
- model-plan file
- result tables
- conclusion section

## Dimension 2: Structure and Page Logic

Pass indicators:

- The paper follows a recognizable CUMCM structure.
- Page count comes from equations, figures, tables, validation, and appendix evidence.
- Method overview, problem analysis, model establishment, result, and validation sections have distinct roles.
- Effective body length remains credible after excluding blank pages, watermark-only pages, and screenshot-only inflation.

Fail indicators:

- Long background replaces modeling substance.
- Problem restatement copies the statement without analysis.
- Sections repeat each other.
- Abstract or conclusion contains unsupported numbers.
- PDF length looks complete only because of code screenshots, blank tail pages, or promotional residue.

Additional v1.2 warning indicators:

- the abstract is too short to close the subquestions properly;
- the model section is not the real technical center of the paper;
- validation is present only as a token add-on;
- section proportions still feel demo-sized instead of team-sized.

Required evidence:

- `knowledge/cumcm/20-30-page-paper-blueprint.md`
- rendered PDF
- section files

## Dimension 3: Model Credibility

Pass indicators:

- Variables, parameters, objective, constraints, and algorithms are defined.
- Method choice matches data size, problem type, and required outputs.
- Assumptions are used later and have stated impact.
- Every named method closes into a result artifact and a decision consequence.

Fail indicators:

- Algorithm names appear without mathematical formulation.
- Optimization models lack constraints or feasibility checks.
- Prediction/classification models lack validation.
- A complex method is used without data support.
- The model chain becomes a method list with no visible output or decision closure.

Additional v1.2 warning indicators:

- a major subquestion stays at `method -> result` depth;
- a complex method is named but support or comparison layers are missing;
- the paper looks algorithm-rich but route-thin.

Required evidence:

- model-plan
- algorithm cards
- equations in paper
- code implementation

Route-specific checks for E papers:

- production-route E papers should show how forecast outputs become inventory, service-level, or production decisions;
- monitoring-route E papers should show how diagnosis and forecast outputs become monitoring or policy decisions;
- coefficient bands, rolling rules, or information thresholds should be explained when they drive the final action layer.

## Dimension 4: Result Traceability

Pass indicators:

- Every important number in abstract and conclusion appears in the artifact ledger.
- Figures and tables map to code outputs, data files, equations, or documented schematic prompts.
- Paper values and code outputs agree.
- Main-text result claims are not outsourced to appendix-only screenshots.

Fail indicators:

- Important numbers cannot be traced.
- Figure/table values conflict with text.
- Static images replace evidence plots without source.
- Appendix code does not support the main paper.
- Code screenshots are used where the paper should provide a reproducible result table, figure, or output file.

Required evidence:

- artifact ledger
- code run records
- figure and table files
- key result registry

## Dimension 5: Visual and Table Quality

Pass indicators:

- Figures are classified as evidence, validation, explanatory, format, or review.
- Evidence and validation figures are reproducible from code.
- Schematic or AI-generated figures are disclosed as schematic.
- Captions explain what the reader should learn.
- Early explanatory figures identify the modeled object clearly before late-stage comparison graphics dominate the paper.

Fail indicators:

- AI-generated image implies data evidence.
- Figure is included but never interpreted.
- Tables overflow or are unreadable.
- Units, legends, or labels are missing.
- The paper jumps into algorithms or results without first showing the network, geometry, process, or system being modeled.

Required evidence:

- figure plan
- visual generation pipeline
- artifact ledger
- rendered PDF screenshots when layout is uncertain

## Dimension 6: Validation and Robustness

Pass indicators:

- Optimization has feasibility and sensitivity checks.
- Prediction has time-aware or holdout validation.
- Classification has confusion matrix and metrics beyond accuracy.
- Simulation has seeds, repeated runs, and uncertainty summaries.
- Physical/business sanity checks are included where relevant.

Fail indicators:

- The paper reports only best results.
- Sensitivity analysis has no perturbation range.
- A single stochastic run is treated as final truth.
- Baselines are missing when model performance matters.

Additional v1.2 warning indicators:

- validation exists, but is too brief to support the claimed confidence;
- sensitivity ranges are named but barely interpreted;
- a baseline is present only in passing and not compared explicitly.

Required evidence:

- verification plan
- validation figures/tables
- baseline comparison
- sensitivity outputs

Route-specific E-paper failures:

- production-route: service level is claimed but not tabulated, or production quantities are given without inventory/support interpretation;
- monitoring-route: diagnostic methods are listed but not linked to subquestions, or prediction never reaches a monitoring/policy scheme.

## Dimension 7: Reproducibility

Pass indicators:

- Raw data, cleaned data, scripts, outputs, figures, tables, and PDF build path are listed.
- One clear run sequence can regenerate core results.
- Random seeds or repeated-run summaries are recorded.
- Dependency or environment assumptions are documented.

Fail indicators:

- Code cannot be connected to paper results.
- Manual edits change key values without record.
- Data units or columns are ambiguous.
- Generated artifacts are missing from expected paths.

Required evidence:

- artifact ledger
- code entry point
- source data inventory
- generated outputs

## Dimension 8: LaTeX and PDF Quality

Pass indicators:

- PDF compiles.
- Chinese fonts, equations, references, and cross-references render correctly.
- Tables and figures fit final pages.
- Research copy removes unnecessary team identity, stale dates, and default template fields.
- Research copy removes promotional watermark, public-account header/footer residue, and generic placeholder title text.

Fail indicators:

- PDF cannot compile.
- Missing figures or broken references.
- Tables overflow or equations are unreadable.
- Stale contest year, team, school, or member metadata remains.
- Watermarks, public-account residue, `paper title`, `论文题目`, `xx`, or `xxxx` remain in the delivered research copy.

Required evidence:

- compile log
- rendered PDF
- page screenshots when needed
- LaTeX source

E-route presentation checks:

- production-route E papers should keep production tables readable and clearly separated by scenario or material group;
- monitoring-route E papers should keep diagnostic figures and effect-comparison figures distinguishable in captions and section references.

## Dimension 9: Responsible Use and Integrity

Pass indicators:

- Use case is research, post-contest review, education, or authorized quality checking.
- Limitations and uncertainty are visible.
- No fabricated data, citations, experiments, or provenance.
- No concealment of prohibited AI involvement.

Fail indicators:

- Active contest cheating or prohibited submission support.
- Fabricated references, experiments, or evidence.
- Instructions to hide AI involvement when disclosure is required.
- Overstated certainty from unverified outputs.

Required evidence:

- user-stated purpose
- review summary
- limitations section
- artifact ledger

## Human-AI Difference Research Notes

This rubric can support research into differences between human and AI-assisted papers by comparing quality signals, not by making binary authorship claims.

Useful observation axes:

- structure completeness versus evidence completeness
- formula polish versus variable closure
- result neatness versus reproducibility
- figure aesthetics versus source traceability
- explanation smoothness versus actual model-code consistency
- limitation specificity versus generic self-critique

High-quality review should ask:

- Is the paper reliable?
- Which claims are supported?
- Which claims need human verification?
- Which artifacts are missing?
- Which risks are typical of generated drafts?

It should not ask only:

- Was this written by a human or AI?

## Output Format

```text
# Paper Quality Review

## Overall Status
Pass / Needs revision / Reject for research use

## Critical Findings

## Important Findings

## Warnings

## Evidence Checked

## Evidence Missing

## Required Repairs

## Human Verification Needed

## Responsible-Use Notes
```
