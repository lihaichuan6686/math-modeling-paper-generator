# v1.5 Paper Generation Feedback

Purpose: preserve user-side and Claude Code test feedback that should become v1.6 product rules.

## Feedback 1: LaTeX Heading Hyphen Truncation

Observed defect:

- A heading such as `\subsubsection{Z-score基线}` can break `hyperref` bookmark or table-of-contents argument handling in Chinese XeLaTeX documents.
- The compiler may still emit a PDF, but later sections, references, and appendix content can be silently truncated or lost.

Product rule:

- Section-like headings must not contain ASCII hyphens.
- Use `Zscore基线判定法`, `Z score基线判定法`, or a Chinese phrase such as `标准分数基线判定法`.
- Hyphenated English terms may appear in body text, but not in `\section`, `\subsection`, `\subsubsection`, `\paragraph`, or `\subparagraph`.

Implemented response:

- Added `LaTeX Heading Safety Gate` to `knowledge/quality/v1-5-hard-gates.md`.
- Added executable source checking to `scripts/check-v1.5-pdf.py`.
- Added launch-prompt instruction in `prompts/15_launch_v1_5.md`.

## Feedback 2: First Draft Section Density Was Too Low

Observed defect:

- A detailed skeleton can create a false sense of completeness.
- If the first compiled draft is only 10-12 pages, later padding produces filler rather than naturally developed contest-paper prose.

Product rule:

- Do not write a thin skeleton first and plan to fill it later.
- The first complete section draft must already contain explanatory paragraphs, formulas where appropriate, and figure/table evidence.

Minimum targets:

| Section family | Minimum paragraphs | Minimum formulas | Minimum figure/table evidence |
|---|---:|---:|---:|
| Problem restatement / analysis | 3 | 0 | 1 |
| Data preprocessing | 3 | 1 | 1 |
| Model construction | 3 | 2 | 1 |
| Solution / computation | 3 | 1 | 1 |
| Results analysis | 3 | 0 | 2 |
| Validation / sensitivity | 3 | 1 | 1 |

Implemented response:

- Added `Section Density Gate` to `knowledge/quality/v1-5-hard-gates.md`.
- Added executable section-density checks to `scripts/check-v1.5-pdf.py`.
- Added launch-prompt instruction that sections must meet density while being written, not after page-count failure.
