# Problem Analysis

Run: calibration-2021E-classification
Created: 2026-07-13 11:09:49
Problem: CUMCM2021-E.pdf with four E attachments

## Problem Summary

This is the 2021 CUMCM E problem, "中药材的鉴别". It asks for medicinal-material category and origin identification from mid-infrared and near-infrared spectral absorbance data. The task is a high-dimensional spectral classification-recognition problem with missing target labels that must be filled in final answer tables.

## Subquestions

1. Attachment 1: study mid-infrared spectral features of several material categories and identify category differences.
2. Attachment 2: use mid-infrared spectra of one material to identify origins for 15 specified `No` values.
3. Attachment 3: combine near-infrared and mid-infrared spectra to identify origins for 10 specified `No` values.
4. Attachment 4: use near-infrared spectra to identify both category and origin for 7 specified `No` values.

## Inputs

- one local problem statement PDF;
- four local spreadsheet attachments;
- rendered-page inspection for the problem statement;
- `source-extraction.md`, `source-extraction.json`, `data-schema-summary.md`, and `data-schema-summary.json`;
- deep-reading note for the 2021 E excellent-paper pattern;
- classification-recognition run-file example and sample package.

## Outputs

- filled run files for the calibration attempt;
- final answer tables for missing `OP` and `Class` entries if the pressure test proceeds to modeling;
- later draft artifacts, if the pressure test proceeds;
- review note and calibration log identifying route, evidence, or writing failures;
- reusable repo write-back after the first generated attempt.

## Constraints

- do not optimize only for this historical problem;
- do not invent fields or metrics beyond the observed `No`, `Class`, `OP`, wave-number, and absorbance structure;
- use consistent data splits for model comparison;
- avoid final claims that exceed class-level validation evidence.

## Evaluation Metrics

- accuracy only as a secondary headline metric;
- macro-F1, per-class recall, or equivalent class-sensitive metrics;
- confusion matrix or class-level error table;
- stability under preprocessing or representation changes.

## Routing Signals

- categorical identification output;
- high-dimensional features;
- two spectral regimes: mid-infrared around 551-3999 `cm^-1` and near-infrared around 4004-10000 `cm^-1`;
- preprocessing, feature extraction, and band-fusion are essential;
- validation risk is stronger than pure solver risk.

## Risks and Missing Information

- PDF text extraction contains mojibake, so `problem-brief.md` should be used as the clean human-readable task note;
- training/test roles are implicit through missing labels rather than separate test files;
- class imbalance and leakage risks remain to be checked after schema extraction.

## Questions for Human Confirmation

- None for now. The next step is model-route calibration from the extracted source structure.
