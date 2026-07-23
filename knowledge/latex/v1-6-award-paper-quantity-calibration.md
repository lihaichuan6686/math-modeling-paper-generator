# v1.6 Award-Paper Quantity Calibration

Purpose: calibrate page-count and quantity-feel targets against local CUMCM award-paper PDFs without pretending scanned PDFs provide exact text, figure, table, or reference counts.

Use with:

- `knowledge/cumcm/recent-award-paper-visual-rhythm.md`
- `knowledge/latex/v1-6-section-rhythm-soft-metrics.md`
- `knowledge/latex/v1-6-layout-rhythm-rules.md`
- `knowledge/latex/v1-6-reference-and-citation-rhythm.md`
- `knowledge/community/v1-6-excellent-paper-reader-lens.md`

## Source And Reliability

Local source folder: the national-contest excellent-paper archive under the parent workspace.

Stable page-count extraction with `pypdf`:

| Sample group | Count | Minimum | Median | Mean | Maximum | Reliability |
|---|---:|---:|---:|---:|---:|---|
| 2021 excellent-paper PDFs | 17 | 21 | 39 | 42.9 | 60 | high for page count |
| 2022 excellent-paper PDFs | 11 | 22 | 32 | 34.3 | 57 | high for page count |
| 2023 excellent-paper PDFs | 5 | 27 | 41 | 39.8 | 50 | high for page count |
| all machine-counted PDFs in folder | 79 | 1 | mixed | mixed | 79 | mixed because many 2024 files are solution notes, not excellent papers |

Local team LaTeX reference:

| File | Page count | Use |
|---|---:|---|
| `LATEX/model1.pdf` | 38 | local first-prize-style full paper reference |
| `LATEX/document.pdf` | 13 | template/test reference, not full paper length target |
| `LATEX/example.pdf` | 13 | template/example reference, not full paper length target |

## Key Calibration Rule

Do not mix these categories:

```text
excellent paper PDF != solution note != template demo != short tutorial
```

Short 2024 solution-note/tutorial PDFs in the same local tree may be only 1-4 pages. They are useful for route hints, not for paper-length calibration.

## Page Target Interpretation

For generated CUMCM-style papers:

| Draft state | Expected page feel | Review meaning |
|---|---|---|
| 20-25 pages | minimum closed-loop draft | acceptable for early testing only; likely thin for award-feel |
| 26-32 pages | v1.6 target band | usable handoff band when every page is dense and body-visible |
| 33-45 pages | stronger award-paper feel | preferred when data, subquestions, validation, and appendix code support it |
| 46-60 pages | heavy evidence / long appendix | acceptable only with substantial body evidence and mapped appendix |
| over 60 pages | likely too long for v1.x unless special | needs explicit justification |

The target is not to inflate every paper to 40 pages. The target is to avoid calling a 20-page, thin, low-artifact draft "award-like".

## Quantity Soft Indicators

Use these as planning signals, not hard scoring:

- Abstract: should visually occupy most of page 1; if extracted text is available, `900-1150` Chinese characters is a useful v1.6 planning range.
- Early body: by pages 4-6, a model object, symbol table, route figure, data table, parameter table, or formal model block should be visible when the problem supports it.
- First 12 pages: should contain recurring formulas, tables, figures, or algorithm blocks with interpretation.
- Middle body: avoid more than 2-3 consecutive pages without formula, table, figure, algorithm structure, result artifact, or validation discussion.
- Appendix: can be long, but only after the body has carried main formulas, results, interpretation, and validation.
- References: prefer 8-15 useful sources when source access supports it; never pad a bibliography to imitate a count.

## Scanned-PDF Limitation Rule

Many local excellent PDFs are image-like or extraction-hostile:

- `pypdf` can read page counts reliably;
- text extraction often returns zero text pages;
- figure/table/reference exact counts are not reliable without OCR or visual inspection;
- a checker must not claim exact figure/table/reference norms from these PDFs unless rendered-page or OCR evidence exists.

Record weak evidence as weak evidence.

## Planning Use

Before drafting `paper/main.tex`, the generator should classify the desired output:

```text
early-test draft / v1.6 handoff draft / stronger award-feel draft / heavy-evidence draft
```

Then choose:

- target page band;
- abstract fullness target;
- first-12-page artifact schedule;
- body result and validation schedule;
- appendix/code budget;
- reference count target based on actual source availability.

## Review Questions

1. Is the page target justified by the problem's data, subquestions, figures, validation, and appendix code?
2. Is the draft short because it is efficient, or short because sections are thin?
3. Does the first page look like a compressed solution rather than a short executive summary?
4. Do pages 4-12 already show model objects and evidence?
5. Does the appendix support a body that already answered the problem?
6. Are references and figures being counted only when the evidence source is reliable?

## Conversion Note

This note strengthens quantity feel, not topic content. It should guide layout and self-review, while method quality still comes from route and evidence rules.
