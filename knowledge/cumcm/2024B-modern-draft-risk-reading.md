# 2024 B Modern-Draft Risk Reading: Complete-Looking Papers Are Not Complete Papers

Purpose: inspect several locally collected 2024 CUMCM B-topic "finished paper" drafts as a risk corpus for the generator. The goal is not to imitate these documents directly, but to distinguish page-count completeness from evidence-backed paper completeness.

## Corpus

Problem family: 2024 CUMCM B, electronic-product quality control and production-cost management.

Local samples:

- `邵老师-2024数模国赛B题成品论文（已更新1-3问）.pdf` - 21 pages
- `2024数模国赛B题成品论文.pdf` (set 4) - 24 pages
- `2024数模国赛B题成品论文 .pdf` (set 5) - 22 pages

The page counts were checked with the bundled PDF reader. The first four pages and the final pages were rendered and visually inspected. These are reference/course-material drafts, not a verified official award corpus; their value here is diagnostic.

## Core Finding

All three documents are long enough to look like complete papers, and all follow a recognizable contest structure:

```text
abstract
-> problem restatement and analysis
-> assumptions and notation
-> data preprocessing
-> model construction and solution
-> results / sensitivity / evaluation
-> conclusions and appendix
```

However, the visual and textual evidence shows that structural presence is not equivalent to completion. A generator that optimizes only for page count can easily produce a document that has headings, formulas, and an appendix shell while lacking a concrete title, populated data, executable code, or traceable results.

## What the Samples Teach About Structure

### Stable macro-structure

The B problem naturally supports a four-question progression:

1. sampling and defect-rate estimation;
2. inspection and defective-product handling decisions;
3. multi-stage production decision optimization;
4. updating the decisions with observed sampling data.

The most useful reusable contract is therefore not merely "write five chapters." Each question should expose a complete local chain:

```text
question interpretation
-> variables and assumptions
-> model choice
-> parameter / data source
-> solver or calculation
-> numerical result
-> decision interpretation
-> validation or limitation
```

The samples also confirm that the abstract should be organized by question, not by a generic description of the topic. A strong abstract states the decision target, the model family, the main numerical output, and the practical meaning of the output for each question.

### Page count is mostly a structural consequence

Twenty-plus pages can be reached quickly by allocating one or two pages to every standard section, adding a notation table, and placing code in the appendix. That is useful for planning a readable document, but it is not evidence of quality. The generator should estimate page budget from required evidence blocks rather than add prose until a target page count is reached.

Recommended page-budget units:

- front matter and abstract: 1-2 pages;
- problem restatement / analysis: 2-3 pages;
- assumptions, notation, and data: 2-3 pages;
- one self-contained block per question: 2-4 pages each;
- cross-question validation and sensitivity: 2-3 pages;
- conclusions, references, and real appendix: 2-5 pages.

The exact total can vary, but every allocated block must be backed by a concrete artifact: a formula, table, chart, algorithm trace, numerical result, or limitation statement.

## Diagnostic Findings

### 1. Placeholder leakage

The first sample visibly contains generic text such as `xxxx` in the title/abstract or appendix label, blank assumption items, and an empty notation table. This is a hard failure, not a stylistic imperfection. Placeholder detection must run over both source text and rendered pages.

Required checks:

- reject `xxxx`, `TODO`, `TBD`, `待补`, `示例`, and template-only labels;
- reject generic titles that do not mention the problem's actual object or decision;
- reject empty numbered lists and tables with headers but no rows;
- reject an abstract that still contains `问题一，` without a model or result after it.

### 2. Watermark and distribution residue

All inspected drafts contain large promotional watermarks and repeated banner text. This is especially damaging when the output is meant to be evaluated as a research artifact: it competes with equations and figures, makes pages look unfinished, and may carry third-party distribution information into a new document.

The generator pipeline should:

- keep source provenance in an internal manifest rather than in the paper body;
- run a rendered-page scan for repeated banners, promotional phrases, and large translucent text;
- maintain a clean output mode with no source watermark;
- preserve citations and acknowledgements only when they are explicitly justified.

### 3. Empty appendix shells

The final pages of the inspected samples show appendix headings and code-container tables whose code area is empty or effectively blank. An appendix heading therefore cannot count as evidence that code was delivered.

An appendix is complete only when it contains at least one of:

- a runnable source file with a stable entry point;
- a meaningful pseudocode listing tied to the equations;
- an input/output example that can be reproduced;
- a figure-generation script or data-processing script with a stated dependency list.

The review report should record the appendix artifact hash, language, execution command, and generated output files when code is available.

### 4. Formula presence without model closure

The samples contain standard formulas for hypergeometric sampling, confidence intervals, hypothesis tests, and cost functions. Those formulas are useful, but formula density can create a false impression of rigor. A formula is not a closed model until the paper states:

- what the symbols mean and their units;
- which data or assumptions determine each parameter;
- what decision variable is optimized or tested;
- how the formula connects to the subsequent numerical result;
- whether the chosen approximation is valid for the stated sample size and population.

For the generator, every displayed equation should have a downstream reference or result anchor. Orphan-equation detection should be part of self-review.

### 5. Overconfident claims

The inspected abstracts and conclusions use strong phrases such as "fully solves," "high efficiency," and "wide applicability" while the visible evidence is mostly model description and generic interpretation. Such claims should be conditional on validation.

Preferred contract:

```text
claim
-> metric or comparison
-> experiment / sensitivity / baseline
-> scope and limitation
```

If no baseline or perturbation test exists, the paper should say that the model is a plausible decision framework rather than claim demonstrated superiority.

## Method-Specific Lessons for 2024 B

### Question 1: sampling and defect-rate estimation

The route can legitimately use hypergeometric sampling when sampling is without replacement from a finite batch. A generator must not silently replace it with a binomial approximation merely because the latter is easier to explain. The finite-population correction, confidence level, error tolerance, and acceptance/rejection rule should be explicit.

The sample-size calculation also needs a parameter policy. If the defect rate is unknown, the paper must state whether it uses a conservative prior value, a pilot estimate, or a worst-case value. A bare numerical sample size with no parameter provenance is not reproducible.

### Questions 2 and 3: cost and multi-stage decisions

The four-stage production process is well suited to binary decision variables and exhaustive enumeration for small cases, but the paper must justify the search method. For 2^4 cases, enumeration is transparent and auditable. For more components or stages, an integer program, dynamic program, or decomposition strategy may be needed.

The cost function should distinguish inspection, assembly, disassembly, replacement or exchange loss, and market loss. The generator should create a cost-ledger table before writing the objective function and verify that each ledger item appears once, with units.

### Question 4: updating the policy with observed data

The last question should not be a copy of the earlier optimization with a new paragraph. It should show exactly which estimated defect rates replace which parameters, how the policy changes, and whether the changed policy remains stable under sampling uncertainty. A before/after decision table and a small sensitivity plot are stronger than a generic statement that the model was "further optimized."

## Generator Quality Gates Derived From This Corpus

Before a paper is accepted as a complete draft, the pipeline should pass all of the following:

1. `identity`: title, problem number, authorship metadata, and all problem-specific nouns are concrete.
2. `coverage`: every question has an interpretation, model, result, and conclusion.
3. `closure`: every important parameter has a source, assumption, or computed value.
4. `traceability`: each headline number maps to code, a table, or a reproducible calculation.
5. `visual evidence`: every figure has a caption, data provenance, axis/unit labels, and a nearby interpretation.
6. `table evidence`: every result table has populated rows, units, and a comparison purpose.
7. `code evidence`: code or pseudocode is non-empty, tied to the model, and passes a smoke test.
8. `placeholder`: no template markers, fake values, empty sections, or unresolved references remain.
9. `render`: no watermark, clipping, blank result page, broken equation, or bad page transition remains after PDF rendering.
10. `claim discipline`: conclusions do not exceed what the validation actually supports.

## Implications for the 20-30 Page Blueprint

The blueprint should separate three counters:

- `page_count`: number of rendered pages;
- `evidence_count`: number of completed model/result/validation artifacts;
- `risk_count`: unresolved placeholders, orphan equations, empty figures, missing code, and unsupported claims.

The target condition is not simply `20 <= page_count <= 30`. A usable draft should satisfy:

```text
20 <= page_count <= 30
and evidence_count >= route-specific minimum
and risk_count == 0 for hard failures
```

This prevents the generator from padding a weak paper with repeated background prose or empty appendix pages.

## Review Questions To Add To Future Self-Checks

- Could a reader reproduce the main numerical result from the stated inputs and code?
- Is the paper's title still meaningful if the abstract is read alone?
- Does each question end with a decision, not just a formula?
- Are the figures generated from the current run, or are they decorative placeholders?
- Does the final question update earlier model parameters in a visible before/after chain?
- Would deleting the appendix remove any evidence needed to trust the result?
- Is the paper's length produced by completed content, or by section shells and code boxes?

## Status

This is a risk-reading note for modern complete-looking drafts. It should be used together with official excellent-paper deep reads and same-problem comparisons; it is not a quality endorsement of the source drafts.
