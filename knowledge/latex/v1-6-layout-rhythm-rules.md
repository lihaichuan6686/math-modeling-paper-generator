# v1.6 Layout Rhythm Rules

Purpose: prevent papers from becoming too long, too sparse, or visually careless after the v1.5 full-length loop.

## Page Rhythm Targets

| Section | Target pages | Notes |
|---|---:|---|
| Title and abstract | 1 | Full page but not overflowing |
| Problem restatement and analysis | 3-4 | Must include the early concept/mechanism figure zone |
| Assumptions and symbols | 1-1.5 | Compact; never allow symbol table to waste a mostly blank page |
| Data preprocessing | 2-3 | Data structure, cleaning, traps, and one evidence artifact |
| Model construction | 5-7 | Equations, route justification, model role |
| Solution and results | 7-9 | Main numerical answer tables and figures |
| Validation and sensitivity | 2-3 | Must interpret instability and not just list metrics |
| Strengths, limitations, conclusion | 2-3 | Human-team closeout, not checklist prose |
| References and appendix | 3-5 | Traceability without raw dumps |

## Abstract Page Target

- Target extracted page-one characters: 900-1150.
- Fail below 900 unless the rendered page is visually full and the review explains extraction weakness.
- Warn above 1200.
- Fail if the abstract spills onto page two.
- Keep problem-by-problem structure and bold key results.

## Symbol Section Compaction

The symbols section should not consume a mostly empty page.

Preferred repairs:

- merge assumptions and symbols when both are short;
- use a compact three-column symbol table when many symbols are short;
- place common units in the meaning column instead of a separate sparse column;
- avoid starting the next major section on a new page unless the template requires it.

## Body Page Density

Flag pages where:

- extracted text is below 180 chars and the page is not an intentional full-page figure;
- a page has one small table or figure and no interpretation paragraph;
- two adjacent body pages are mostly whitespace or plot-only;
- the last page before references is mostly blank.

## Table Safety Rules

Never use bare `tabular{lll}` for wide text, paths, script indexes, or result descriptions.

Preferred table patterns:

```latex
\begin{tabularx}{\textwidth}{p{0.24\textwidth} X p{0.18\textwidth}}
```

```latex
\begin{adjustbox}{max width=\textwidth}
\begin{tabular}{...}
...
\end{tabular}
\end{adjustbox}
```

Long text columns must use `p{...}` or `X`. Long paths should be shortened, wrapped, or moved to appendix prose.

## Overfull Box Policy

- Any severe `Overfull \hbox` above 50pt in the final log is a fail.
- More than 8 overfull warnings above 10pt is a fail.
- Any visible table clipping is a fail even if the log is quiet.

## Figure Placement

Figures should earn their space:

- every figure needs an interpretation paragraph before or after it;
- concept figures belong in the first six pages;
- result figures belong near the subquestion they support;
- appendix figures cannot carry the main answer.
