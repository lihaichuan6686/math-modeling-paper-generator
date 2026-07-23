# v1.6 Section Rhythm Soft Metrics

Purpose: convert local award-paper observations into practical section-level targets before drafting. This file is a soft planning layer, not a rigid scoring table.

Use it with:

- `knowledge/latex/v1-6-layout-rhythm-rules.md`
- `knowledge/latex/v1-6-award-feel-soft-rules.md`
- `knowledge/cumcm/recent-award-paper-visual-rhythm.md`
- `knowledge/latex/local-awarded-paper-structure-rules.md`

## Source Signals

Local evidence already distilled in this repository shows a stable award-paper rhythm:

- page 1 is a dense abstract with keywords;
- page 2 enters restatement or analysis quickly;
- pages 4-6 show at least one model artifact such as a symbol table, concept diagram, data table, formula group, or route table;
- pages 8-12 already alternate formulas, figures, tables, and interpretation;
- middle pages grow from repeated subquestion loops, not from one long method dump;
- appendix code is acceptable only after the body has already carried the answer logic.

The key local lesson is:

```text
credible length = subquestion loop density + visible evidence chain + interpretation,
not background padding or appendix inflation.
```

## Section Soft Metrics

| Section | Target pages | Paragraph rhythm | Formula/table/figure expectation | First-look failure |
|---|---:|---|---|---|
| Abstract | 1 | opening task sentence, one method-result paragraph per major question, final value sentence, keywords | 3+ bold result fragments; 3+ keyword groups | half-page abstract, no bold results, only method names |
| Problem restatement | 1-1.5 | rewrite the real decision objects and outputs, not the original wording | one object/variable map when the problem is complex | copied statement or generic social background |
| Problem analysis | 1.5-2.5 | explain subquestion dependency, route changes, data traps, and output form | early concept/mechanism figure or route table by pages 2-4 | analysis says only "we build a model" |
| Assumptions and symbols | 1-1.5 | each assumption supports a simplification; symbols are compact | compact 2- or 3-column symbol table | half-empty page or decorative assumptions |
| Data preprocessing | 2-3 | data source, cleaning, derived variables, traps, and exploratory facts | data inventory table plus at least one diagnostic figure/table | column dump with no modeling consequence |
| Model construction | 5-7 | each subquestion has variables, objective or target, constraints, and route justification | at least one formal block per central subquestion | prestige algorithm names without variable/domain logic |
| Solution process | 3-5 | solver steps, parameter choices, reproducibility, and convergence or iteration logic | algorithm table, convergence curve, parameter table, or decision table | code narrative without mathematical closure |
| Results and interpretation | 4-6 | answer each question with result, comparison, and interpretation | main answer table/figure near each claim | raw output table with no conclusion sentence |
| Validation and sensitivity | 2-3 | test whether the answer survives perturbation, split, residual, capacity, or feasibility checks | at least two validation artifacts when data permits | "model is good" praise paragraph |
| Evaluation, conclusion, references, appendix | 4-6 | limitations are concrete; conclusion mirrors abstract; appendix maps code to questions | 8-15 references if source base supports it; code/script index | appendix is a raw dump or references are decorative |

## Per-Subquestion Loop Target

For every major numbered question, draft the paper around this loop:

```text
task role
-> route choice
-> variables and assumptions
-> model or solver
-> result artifact
-> interpretation
-> validation or limitation
```

Soft target for central subquestions:

- 3-5 substantial paragraphs across analysis/model/result sections;
- 1-2 equations or formal definitions unless the question is purely descriptive;
- at least one table or figure that supports the final answer;
- one credibility sentence explaining why the result is plausible.

If a subquestion cannot meet this target, record why in `section-rhythm-budget.md` before writing the abstract.

## Page Economy Rules

Do not grow the paper by:

- creating a separate mostly blank symbol page;
- placing one small figure alone on a page;
- moving main answer tables into the appendix;
- adding generic background after page 2;
- using code listings to compensate for missing body explanation.

Grow the paper by:

- adding route justification before formulas;
- adding interpretation after each result artifact;
- adding validation or sensitivity checks near the claims;
- adding compact comparison tables;
- adding a concept/mechanism figure that explains the problem object, not the writing workflow.

## Drafting Rule

Before writing `paper/main.tex`, the generator should fill `runs/current/section-rhythm-budget.md` with:

- target pages;
- paragraph target;
- expected formulas;
- expected tables/figures;
- compression risk;
- exact evidence file or section.

During writing, do not create a thin skeleton and promise to fill it later. Write each section to its soft metric on the first pass, then compact or expand after PDF review.

## Review Questions

Ask these before handoff:

1. Can a reader see the answer route in the first 12 pages?
2. Does every major result have a nearby interpretation paragraph?
3. Does each central subquestion have its own model-result-validation loop?
4. Is any page long only because of blank space, oversized tables, or appendix dumping?
5. Would the title, abstract, first figure, and first result table look plausible beside recent award papers?
