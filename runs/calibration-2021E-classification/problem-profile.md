# Problem Profile

Run: calibration-2021E-classification
Created: 2026-07-13 11:09:49
Problem: CUMCM2021-E.pdf with four E attachments

## Problem Image

2021 CUMCM E, spectral or high-dimensional data classification and origin identification, with one problem statement PDF and four spreadsheet attachments.

This run is a methodology calibration run. Its purpose is to test the reusable classification-recognition route, not to optimize only this one historical problem.

## Task Family And Route Signals

- classification / recognition;
- high-dimensional tabular or spectral features;
- preprocessing and feature extraction are part of the model, not only data cleaning;
- final answer must identify categories or origins with bounded confidence;
- route failure risk is overclaiming from a single global score.

## Modeled Object

Samples represented by high-dimensional measured features after preprocessing, feature selection, or dimensionality reduction.

## Decision Object

Reliable identification rule for category or origin, with class-level evidence and a stated scope of validity.

## Question Map

- Q1: understand raw feature structure, missingness/noise, and preprocessing needs.
- Q2: design candidate preprocessing and feature-reduction routes.
- Q3: compare classifiers under a consistent split and metric policy.
- Q4: report final identification conclusions with class-level error evidence and claim boundaries.

## Evidence Burden

- data inventory and split policy;
- preprocessing comparison;
- dimensionality-reduction or feature-selection evidence;
- classifier comparison table;
- confusion matrix or per-class metrics;
- bounded conclusion that does not generalize beyond the tested sample source.

## Visual Burden

- object-first data shape or spectrum/feature overview;
- preprocessing effect comparison;
- feature-reduction scatter, component contribution, or feature-importance chart;
- classifier comparison table;
- confusion matrix or class-level diagnostic figure.

## Thinness Risks

- treating preprocessing as a one-line implementation detail;
- reporting only accuracy;
- using one classifier with no baseline;
- claiming universal identification ability without sample-scope limits;
- making figures decorative instead of diagnostic.

## Fake-Completion Risks

- a paper can look complete with a pipeline diagram, one accuracy number, and a few plots while still failing validation.
- the route only counts as complete if class-level errors and rejected model alternatives are visible.
