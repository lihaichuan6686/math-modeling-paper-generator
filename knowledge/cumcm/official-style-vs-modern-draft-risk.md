# Official Style vs Modern-Draft Risk: What The Generator Should Learn

Purpose: connect the recent modern-draft risk notes to the already absorbed official excellent-paper readings, so the generator can imitate the right signals and reject the wrong ones.

## Corpus Used

Official-style anchors already in the knowledge base:

- `deep-reading-2022E014.md`
- `deep-reading-2022E029.md`
- `deep-reading-2023E176.md`
- `2021C-comparison-C066-C085-C169-C283.md`
- `2021D-comparison-D017-D026-D034.md`

Recent modern-draft risk notes:

- `2024B-modern-draft-risk-reading.md`
- `2024C-modern-draft-risk-reading.md`
- `2024D-modern-draft-risk-reading.md`
- `2024E-modern-draft-risk-reading.md`

## Core Contrast

Official excellent papers and recent complete-draft materials differ less in topic coverage than in closure quality.

The main contrast is:

```text
official excellent paper
-> stable question map
-> method-to-result closure
-> relevant figures and tables
-> appendix supports the paper
-> page length grows from repeated evidence loops

modern risky draft
-> unstable question map
-> method stacking or placeholder closure
-> page inflation from code, blank pages, or residue
-> appendix used as decoration
-> page length can look complete without proving anything
```

## What Official Papers Consistently Do Well

### 1. They keep a stable question map

From the same-problem comparisons and official E papers, one recurring strength is consistency:

- the abstract's subproblem order matches the body;
- each section closes the same subproblem it opened;
- conclusions refer back to the same numbered tasks;
- result tables have a clear problem role.

This matters because the 2024 E draft sample already showed how easy it is for a paper to drift between abstract numbering and body numbering.

Generator rule:

```text
The question map is a contract. Extract it once from the problem statement and reuse it in abstract, section titles, result tables, captions, and conclusion.
```

### 2. They become long by closing loops, not by accumulating methods

The official same-problem notes for `2021 C` and `2021 D` show that good papers repeat a disciplined pattern:

```text
subproblem
-> model construction
-> algorithm or rule
-> result table/figure
-> interpretation
-> robustness / comparison
```

The official E papers do the same thing in data-analysis form:

```text
data preparation
-> forecast / diagnosis
-> decision model
-> operational recommendation
```

By contrast, the 2024 risk notes show several ways modern drafts break this loop:

- placeholders and empty shells;
- formulas without numeric closure;
- code screenshots without runnable artifact linkage;
- methods listed in advance but weakly tied to outputs.

Generator rule:

```text
Every named method must produce a visible artifact and a sentence-level decision consequence.
```

### 3. Their figures explain the object before proving the result

Official concise papers tend to introduce the modeled object visually:

- supply-chain and scheduling papers show networks, process flow, or scheme tables;
- physics-probability papers need geometry or coordinate schematics;
- monitoring and traffic-control papers need map-like or route-like object views;
- only then do later pages introduce comparison charts, residuals, or sensitivity plots.

This matches the modern-draft lessons from:

- `2024 D`: geometry before optimization;
- `2024 E`: road network before control algorithms.

Generator rule:

```text
The first figure should usually identify the object of modeling, not celebrate the final result.
```

### 4. Their appendices support the paper instead of pretending to be the paper

Official papers do use appendices and code, but the paper body already stands on its own:

- core conclusions appear in the main text;
- appendix materials are traceable by question;
- support materials extend reproducibility rather than replacing argument;
- code is not used only to inflate length.

Recent risky drafts repeatedly violate this:

- empty appendix shells;
- long code screenshots with little linkage;
- overlong PDFs whose extra pages come from code blocks or residue pages.

Generator rule:

```text
Count appendix evidence separately from paper-body argument. The body must still be complete without code screenshots.
```

### 5. Their references are connected to the modeling route

Official papers are usually not citation-heavy for its own sake, but their references support the route they actually use. The risky 2024 D sample shows the opposite pattern: a physically modeled paper ending with mostly teaching-style modeling references.

Generator rule:

```text
Reference lists should contain at least some route-relevant citations: method, domain, or data context. Teaching-only references are not enough.
```

## Hard Gates The Generator Should Keep

These gates are now strongly supported by both the official readings and the 2024 risk readings:

- `question_map_gate`
- `identity_gate`
- `placeholder_gate`
- `watermark_or_residue_gate`
- `effective_body_length_gate`
- `method_output_gate`
- `decision_closure_gate`
- `figure_object_gate`
- `appendix_traceability_gate`
- `code_link_gate`
- `reference_relevance_gate`

## Length Lesson

The official notes teach that a 20-30 page contest paper is not hard to reach if every subproblem gets:

- model construction;
- one or two real figures/tables;
- a result paragraph;
- a robustness or comparison paragraph.

The modern-draft notes teach that page count becomes misleading when it is padded by:

- placeholders;
- blank tail pages;
- promotional residue;
- raw code screenshots;
- unsupported claim paragraphs.

Generator rule:

```text
Target effective body length, not PDF length. A 22-page closed-loop paper is stronger than a 30-page inflated draft.
```

## Immediate Design Consequence For v1

The v1 generator should not aim to mimic recent "complete draft" aesthetics. It should instead:

1. keep the official concise-paper backbone;
2. use the modern-risk notes as a blacklist of fake-completion signals;
3. require one evidence artifact per subproblem;
4. separate body-page budgeting from appendix budgeting;
5. run a review pass that checks numbering, figures, tables, code linkage, and residue before claiming completion.

## Status

This note is a synthesis rule-set for future generator prompts, reviewers, and paper blueprints. It turns the recent learning burst into a usable standard for the next 1.0 and 1.1 iterations.
