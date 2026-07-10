# 2024 D Modern-Draft Risk Reading: Physics-Probability Papers Need Evidence Closure

Purpose: extend the modern-draft risk corpus to a physics / probability / optimization problem and extract rules for judging whether a generated D-type paper is structurally complete.

## Corpus

Problem: 2024 CUMCM D, anti-submarine depth-charge hit probability and deployment optimization.

Local materials inspected:

- set-1 complete-paper-labeled PDF: 31 rendered PDF pages;
- set-1 idea PDF: 20 rendered PDF pages;
- set-1 code: three notebooks for questions 1, 2, and 3;
- set-2 question-1 PDF: 3 rendered PDF pages;
- set-2 idea PDF: 1 rendered PDF page.

Rendered pages were visually inspected for the complete-paper PDF, the final reference page, and the short question-1 PDF. The PDFs include promotional watermarks and should not be treated as formatting exemplars.

## Main Finding

The D-type route exposes a different risk pattern from 2024 B/C:

```text
physical geometry -> probability model -> optimization variable -> numerical result -> deployment recommendation
```

A paper can look mathematically dense while still failing as a complete contest paper if it stops at formulas, omits numerical closure, or cannot link diagrams, code, and result tables.

The generator must therefore check both the argument route and the evidence route:

```text
coordinate frame
-> random variables and distributions
-> hit-event decomposition
-> integral / simulation / optimization method
-> parameter table
-> result figure or table
-> sensitivity / error analysis
-> final operational recommendation
```

## Structural Lessons

The complete-paper sample follows a recognizable three-question progression:

1. no depth-location error: derive the relationship between horizontal location error, detonation depth, and hit probability;
2. all directions have location error: introduce a vertical error distribution and optimize detonation depth;
3. multiple depth charges: optimize detonation depth and planar spacing for an array attack.

For this problem family, the paper needs visual evidence early. The inspected sample uses schematic figures for target coordinates and multi-charge deployment. That is the right kind of figure, even though the watermark and generic title make the PDF unsuitable as a clean format model.

Reusable section chain:

```text
problem restatement with parameter values
-> coordinate and geometry diagram
-> assumptions and variable table
-> single-charge hit event decomposition
-> probability expression
-> numerical optimization or simulation
-> multi-charge array extension
-> sensitivity / error analysis
-> deployment advice
```

## Risk Findings

### 1. Identity and watermark residue

The complete-paper sample starts with the generic title `paper title` rather than a real topic title. It also has a large promotional watermark. The short question-1 sample has red promotional headers/footers and explanatory annotations.

Hard checks:

- reject generic titles such as `paper title`, `论文题目`, `xx`, or `xxxx`;
- reject promotional headers, watermarks, and public-account residue;
- separate useful route extraction from formatting imitation.

### 2. Effective page count differs from PDF page count

The complete-paper PDF has 31 pages, but the final rendered page is blank except for the watermark. The page before it is the reference list. For a generator that targets 20-30 pages, this matters: the review should count effective body pages, not raw PDF pages.

Hard checks:

- `pdf_total_pages`: raw rendered PDF page count;
- `effective_body_pages`: pages containing argument, figures, tables, equations, or appendix evidence;
- `blank_or_watermark_pages`: blank pages and promotional residue;
- reject length claims based only on PDF page count.

### 3. Formula density is not result closure

The short question-1 PDF contains dense probability integrals and geometric hit-event decomposition. That is valuable for model construction, but it is not a full paper. It lacks the full contest-paper structure, complete multi-question coverage, and a final numerical result chain.

For the generator, formulas must be followed by:

- explicit parameter values and units;
- numerical method or simulation method;
- optimum depth / spacing / hit probability values;
- table or figure carrying those values;
- short interpretation in the language of the problem.

### 4. Code evidence exists, but provenance still needs checks

The complete-paper folder includes three notebooks for questions 1, 2, and 3. The notebooks use `numpy`, `scipy`, `scipy.stats`, `scipy.optimize`, and `matplotlib`; they contain normal-distribution calculations, optimization calls, and plotting. This is stronger than an empty appendix.

However, the review must still check:

- fixed random seeds for simulation-based results;
- notebook output files or tables named in the paper;
- consistent parameter values between paper, code, and problem statement;
- one code artifact per solved question;
- result values in code matching reported values in tables/figures.

### 5. Reference relevance can be weak

The complete-paper sample ends with a reference list, but visually inspected references are mostly about mathematical-modeling education and teaching. For this D problem, better references should support probability modeling, target search, error distributions, underwater weapon modeling, numerical optimization, or simulation.

Reference gate:

- at least some citations should be method/domain relevant;
- teaching or contest-introduction references cannot be the main evidence base;
- references should not be used as filler to make the paper look formal.

## Generator Gates

Add or strengthen these checks for physics-probability D routes:

- `identity_gate`: title and metadata are problem-specific, not template text.
- `watermark_gate`: rendered pages contain no promotional residue.
- `effective_length_gate`: body page count is computed after excluding blank and residue-only pages.
- `geometry_gate`: coordinate frame, target dimensions, orientation, and units are explicit.
- `distribution_gate`: every random variable has a named distribution and parameter source.
- `event_decomposition_gate`: hit conditions are decomposed into cases before optimization.
- `numerical_closure_gate`: formulas lead to numeric optimum values and hit probabilities.
- `figure_gate`: include at least one coordinate/geometry figure and one result/evidence figure.
- `code_link_gate`: notebooks/scripts map to questions and produce named outputs.
- `reference_relevance_gate`: references match the method/domain, not only modeling education.

## Page Blueprint For D-Type Probability / Physics Papers

Target body:

- Abstract: 0.8-1 page, one paragraph per question plus keywords.
- Restatement and parameter extraction: 1.5-2 pages, including a parameter table.
- Assumptions and notation: 1.5-2 pages.
- Geometry and probability foundations: 3-4 pages, with schematic figures.
- Question 1 model/results: 3-4 pages.
- Question 2 model/results: 3-4 pages.
- Question 3 deployment optimization: 4-5 pages.
- Sensitivity, error, and robustness: 2-3 pages.
- Strengths, limitations, and conclusion: 1.5-2 pages.
- References and appendix inventory: 1-2 pages, with code stored as linked artifacts when possible.

## Review Questions

When reviewing a generated D paper, ask:

1. Does the paper establish a physical coordinate system before deriving equations?
2. Are all dimensions, uncertainties, and distribution parameters traceable to the problem?
3. Does every formula have a role in a result table, figure, or optimization?
4. Are the optimum strategy variables clearly named and numerically reported?
5. Do result figures show geometry, probability surface, sensitivity, or strategy layout?
6. Can a reviewer run code and reproduce the reported values?
7. Are references method/domain relevant rather than decorative?
8. Is the rendered PDF free of placeholder title text, watermarks, blank pages, and public-account residue?

## Status

This note is a risk-reading extension. It should feed the v1 generator's quality gates and D-type route planning, not be treated as an endorsement of the inspected source drafts.
