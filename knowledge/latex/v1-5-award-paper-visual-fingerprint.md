# v1.5 Award-Paper Visual Fingerprint

Purpose: convert visual sampling of recent local CUMCM awarded-paper PDFs into reusable layout, rhythm, and artifact-placement rules.

This note focuses on what makes a generated PDF look like a serious team paper before the reader audits every method detail.

## Sample Scope

Local source folder:

```text
国赛历年论文【公众号：竞赛资料网】整理
```

Visual sample:

| Sample | Source PDF | Pages rendered |
|---|---|---|
| 1 | 2023 `A0127.pdf` | front 1-6, tail 45-50 |
| 2 | 2023 `B311.pdf` | front 1-6, tail 26-31 |
| 3 | 2023 `C050.pdf` | front 1-6, tail 36-41 |
| 4 | 2023 `D039.pdf` | front 1-6, tail 22-27 |
| 5 | 2023 `E176.pdf` | front 1-6, tail 45-50 |

Text extraction was unreliable for many PDFs because of watermark, scan, and image layers. The rules below therefore come from page rendering and visual inspection rather than from raw extracted text.

## Visual Fingerprint

### 1. Page One Is A Compressed Solution

Observed pattern:

- page one is not a title page with a short abstract;
- the title is specific and contest-like;
- the abstract occupies most of the page;
- keywords close the first page;
- there is little empty vertical space.

Generator rule:

```text
The first page should look like a compressed solution memo: title -> dense abstract -> keywords.
```

Failure smell:

- page one looks like a generic report cover;
- the abstract is one block but visually short;
- the abstract names methods without giving answer-level results.

### 2. Page Two Starts Solving Immediately

Observed pattern:

- page two usually enters problem restatement or problem analysis;
- the restatement is compact and turns the task into modelable objects;
- long textbook background is rare.

Generator rule:

```text
After the abstract page, move quickly into restatement and analysis. Do not spend page two on generic background.
```

Failure smell:

- the paper delays modeling for broad background prose;
- page two still reads like a contest introduction rather than a modeling paper.

### 3. Pages Three To Six Must Show Modeling Objects

Observed pattern across the five samples:

- symbol tables, assumption blocks, mechanism diagrams, model-flow diagrams, equations, data tables, and early charts appear before page six;
- even when a paper is prose-heavy, it introduces formal objects early;
- model establishment does not wait until the middle of the paper.

Generator rule:

```text
By pages 3-6, the paper should visibly contain at least two modeling objects: symbol table, route diagram, assumption table, formula group, data table, result chart, or mechanism schematic.
```

Failure smell:

- first six pages are mostly prose;
- the first figure is decorative;
- formulas begin without a symbol table or scene/model explanation.

### 4. Early Figures Serve Orientation, Not Decoration

Observed pattern:

- early figures are often mechanism, process, scene, geometry, or model-flow figures;
- they help the reader understand the object before dense formulas or result tables;
- the figure is near the paragraph that explains it.

Generator rule:

```text
The early concept figure should orient the reader to the modeled object, mechanism, feature pipeline, route relation, or decision chain.
```

Failure smell:

- an AI-generated decorative picture appears in the background section;
- a chart appears before the reader knows what question it supports;
- the caption says only what the picture is, not what role it plays.

### 5. The Middle Body Alternates Artifacts And Interpretation

Observed pattern:

- strong pages are rarely all prose;
- formulas, tables, plots, algorithm blocks, and explanatory paragraphs alternate;
- result artifacts appear inside the body instead of being delayed to conclusion or appendix.

Generator rule:

```text
In model and result sections, use the rhythm artifact -> interpretation -> next artifact -> validation.
```

Failure smell:

- two or three consecutive model pages contain only short paragraphs;
- results are reported as bullets without nearby tables or figures;
- figures are inserted in a batch without interpretation.

### 6. Tail Pages Commonly Carry Code Or Support Files

Observed pattern:

- the final pages of all five sampled PDFs contain code, script fragments, support-file lists, or appendix-like technical material;
- long appendix blocks are normal in stronger papers, especially 30-50 page samples;
- code appears after the body has already explained the answer logic.

Generator rule:

```text
Appendix code or a script index is part of the expected paper shape, but it must support body results rather than replace them.
```

Failure smell:

- no code or script inventory appears;
- code appears before the main result is interpreted;
- the only concrete result is buried inside a code listing.

## v1.5 Generation Rules

Before drafting `paper/main.tex`, require the run plan to answer:

| Page zone | Required visual duty |
|---|---|
| Page 1 | title, dense paragraph abstract, keywords |
| Page 2 | restatement/analysis begins; no generic background wall |
| Pages 3-6 | at least two visible modeling objects |
| Pages 7-12 | recurring formulas, figures, tables, or algorithm/result artifacts |
| Middle body | artifact and interpretation alternate |
| Tail | references plus appendix code or script index |

## v1.5 Review Questions

Add these questions to the human visual review:

1. Does page one look like a full solution abstract rather than a short report summary?
2. Does page two start solving the problem instead of introducing the contest?
3. By page six, can the reader see formal modeling objects rather than only prose?
4. Are early figures explanatory and tied to nearby text?
5. Does the middle body keep alternating artifacts and interpretation?
6. Does the appendix make the work reproducible without carrying the main answer?

## Use In Later Versions

For v1.5, use this note as a review and prompt-support rule.

For v1.6/v2.0, this can become an executable visual-density checker if rendered-page image analysis is added.
