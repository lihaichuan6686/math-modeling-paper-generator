# v1.6 Layout Hard Gates

Purpose: block visually weak, overlong, or layout-broken papers after the v1.5 hard gates pass.

Run after PDF compilation:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\check-v1.6-layout.ps1 -Pdf .\paper\main.pdf -Tex .\paper\main.tex -Log .\paper\main.log -Review .\reviews\review-current.md
```

## Gate 1: Page Rhythm Gate

Fail if:

- the PDF is under 20 pages;
- the PDF is over 35 pages without explicit review justification;
- references and appendix inflate length while the body remains thin.

Warn if:

- the PDF is under 24 pages or over 32 pages;
- page-density evidence shows repeated sparse pages.

## Gate 2: Abstract Fill Gate

Fail if:

- page one has fewer than 900 extracted characters;
- the abstract spills beyond page one;
- the abstract lacks problem-by-problem closures or bold key results.

Target: 900-1150 extracted characters on page one.

## Gate 3: Blank Space Gate

Fail if:

- the symbols/assumptions zone leaves a mostly blank page;
- two adjacent body pages have very low text density;
- a page has a small isolated artifact and no interpretation.

## Gate 4: Table Width Gate

Fail if:

- LaTeX log contains severe overfull table boxes;
- source contains wide text tables using bare `tabular{lll}`, `tabular{llll}`, or similar;
- appendix script/path tables are not protected by `tabularx`, `adjustbox`, or fixed-width `p{}` columns;
- rendered PDF visibly clips table content.

## Gate 5: Figure Readability And Style Gate

Fail if:

- figure text renders as boxes or unreadable glyphs;
- default English plot titles or labels remain;
- the early concept figure is only a generic flowchart with no model-object logic;
- a figure is too small to inspect in the PDF.

Because raster figure text may not appear in PDF text extraction, the review must include a rendered-page or screenshot inspection note. If no rendered-page inspection is recorded, treat figure readability as unproven.

## Gate 6: Nature-Style Concept Figure Gate

Pass when the early concept figure has:

- grouped modules or zones;
- visible information flow;
- readable labels after insertion into PDF;
- restrained color palette;
- a caption and interpretation paragraph that explain why it supports the modeling route.

## Gate 7: Final Source Cleanup Gate

Fail if final LaTeX source still contains:

- visible `TODO`, `Unknown`, `TBD`, `待定`, `未知`, or `fill` placeholders;
- planning/workflow terms such as `Paper spine`, `First-12-page signal`, `Abstract claim shape`, `Validation close`, or `First-look failure`;
- v1.6 concept-figure fallback text from `cumcm_v16_main.tex`;
- placeholder bibliography items such as `\bibitem{...} TODO`.

These are final-handoff blockers even when the PDF compiles.

## Gate 8: Resource Link Gate

Fail if final LaTeX source contains:

- `\input{...}` or `\include{...}` paths that do not resolve to existing `.tex` files;
- `\includegraphics{...}` paths that do not resolve to existing figure files;
- figure references that point outside the paper artifact structure without a review explanation.

For graphics without an explicit extension, the checker may try common extensions such as `.pdf`, `.png`, `.jpg`, `.jpeg`, and `.eps`. A missing body-critical figure blocks handoff.

## Gate 9: Artifact Ledger Consistency Gate

Fail if:

- `runs/current/artifact-ledger.md` is missing;
- the ledger is missing required sections for figures, tables, key results, code runs, or visual evidence chain;
- the ledger still contains template placeholders such as `Unknown`, `TODO`, `TBD`, `待定`, or `未知`;
- the ledger still records body-critical items as merely `planned` during final handoff;
- figures referenced by `\includegraphics{...}` in the final TeX are not listed in the ledger.

The ledger should make each paper-visible figure/table/result traceable to data, code, generation method, caption, paper section, and review status.

## Gate 10: Title Abstract Consistency Gate

Fail if:

- final `\title{...}` is missing;
- final title contains generic or placeholder wording such as `数学建模论文`, `问题求解`, `论文生成`, `TODO`, `Unknown`, or `待定`;
- final title does not match `Selected title:` in `runs/current/title-candidates.md`;
- final abstract lacks `针对问题一`, `针对问题二`, or `针对问题三` paragraphs;
- final abstract has fewer than three bold key-result expressions;
- keywords are missing or fewer than three object/method/result keyword groups.

Warn if the final title lacks contest-style modeling terms such as `基于`, `面向`, `模型`, `优化`, `评价`, `预测`, `判定`, `策略`, or `研究`.

## Required Review Language

The final review must include a `v1.6 Layout Gate Verdict` table:

| Gate | Pass/Fail | Evidence | Repair |
|---|---|---|---|

The table must include all v1.6 gates:

1. Page Rhythm Gate
2. Abstract Fill Gate
3. Blank Space Gate
4. Table Width Gate
5. Figure Readability And Style Gate
6. Nature-Style Concept Figure Gate
7. Final Source Cleanup Gate
8. Resource Link Gate
9. Artifact Ledger Consistency Gate
10. Title Abstract Consistency Gate

Every row must be marked `Pass` or `Fail`; Unknown verdicts are not allowed in final handoff. The review should cite `reviews/layout-v16-check.md` and mention `artifact-ledger.md` when discussing traceability.

Any failed v1.6 layout gate blocks handoff.
