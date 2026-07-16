# Data Inventory

Run: calibration-2021E-classification
Created: 2026-07-13 11:09:49

| ID | File | Description | Fields | Units | Risks |
|---|---|---|---|---|---|
| D01 | `CUMCM2021-E.pdf` | problem statement | category/origin identification tasks, target `No` lists | text/rendered PDF | text extraction has mojibake; use `problem-brief.md` |
| D02 | Attachment 1 | mid-infrared category-recognition data | `No` plus 3348 spectral columns | wave number 652-3999 `cm^-1`, absorbance | no explicit `Class` column in extracted sheet; category structure must be inferred from problem/paper route or hidden grouping |
| D03 | Attachment 2 | mid-infrared origin-recognition data | `No`, `OP`, 3448 spectral columns | wave number 551-3998 `cm^-1`, absorbance | 15 missing `OP` targets |
| D04 | Attachment 3 | near-infrared and mid-infrared origin-recognition data | each sheet has `No`, `OP`, spectral columns | NIR 4004-10000 `cm^-1`, MIR 552-3999 `cm^-1`, absorbance | 10 missing `OP` targets in both bands; fusion must avoid leakage |
| D05 | Attachment 4 | near-infrared category and origin recognition | `No`, `Class`, `OP`, 5996 spectral columns | wave number 4004-10000 `cm^-1`, absorbance | many missing `Class` or `OP`; final asked IDs are a small subset |
| D06 | `source-extraction.md/json` | raw text and workbook extraction | PDF text, sheet previews | mixed | PDF text is not reliable for direct quoting |
| D07 | `data-schema-summary.md/json` | normalized schema extraction | rows, columns, label-missing lists, wave-number ranges | structured | generated summary should be refreshed if source files change |

## Cleaning Plan

- Use `No` as sample identifier inside each attachment; do not assume `No` is comparable across attachments unless the problem logic requires it.
- Treat missing `OP` and `Class` cells as prediction targets, not ordinary missing values to impute.
- Separate labeled rows from target rows before preprocessing and validation.
- Record missing values, constant columns, extreme absorbance values, and duplicate spectral curves.
- Use spectral preprocessing appropriate for absorbance curves, then compare whether feature selection or dimensionality reduction improves class/origin separability.

## Data Risks

- label leakage if target rows are included in supervised fitting;
- inconsistent sample identifiers across attachments;
- high-dimensional feature matrix with far more variables than samples;
- preprocessing choices changing the validation outcome;
- class imbalance making accuracy misleading;
- fusion in Q3 may overweight one spectral band unless band-level evidence is reported.
