# Deep Reading: 2021 A028

Source: `国赛历年论文.../2021年高教社全国大学生数学建模竞赛优秀论文.../A028.pdf`

Problem type: geometry and engineering mechanics.

Paper title observed from rendered PDF: `"FAST" active reflector adjustment model`.

Pages: 38 total.

- Pages 1-23: main paper and references.
- Pages 24-38: appendix/code inventory and code excerpts.

Note: the PDF has heavy watermark text and noisy text extraction. This note is based primarily on rendered-page visual inspection.

## Why This Paper Matters

This paper is a strong example of a geometry/engineering CUMCM route. It does not start from a generic optimizer. It first builds the physical and coordinate model of the FAST reflector, then defines geometric deviation metrics, then solves node adjustment, and finally evaluates reflected electromagnetic signal reception.

Reusable route:

```text
engineering object
-> coordinate and geometric abstraction
-> ideal target surface
-> deviation metric
-> actuator/node adjustment model
-> signal reception evaluation
-> model strengths and limitations
-> code appendix
```

## Section Structure

Observed structure:

1. Abstract
2. Problem restatement and analysis
3. Symbol explanation
4. Model assumptions
5. Model establishment and solution
   - Problem 1: ideal paraboloid analysis and solution
   - Problem 2: actuator/node adjustment and fitting
   - Problem 3: reception-ratio calculation and comparison
6. Model evaluation
7. References
8. Appendix/code files

Generator lesson:

- For engineering geometry papers, `symbols` and `assumptions` are not decorative. They are needed before the model because later formulas are dense.
- The main model section can be long, but it should be divided by subquestion and each subquestion should close with results or figures.
- A long appendix can be justified when it lists runnable files and maps them to subquestions.

## Abstract Pattern

The abstract is result-heavy. It names:

- the overall target: active reflector adjustment for FAST;
- the model idea for each problem;
- fitted ideal paraboloid equations;
- coordinate-rotation or coordinate-transform logic;
- actuator/node adjustment result;
- electromagnetic signal reception ratio comparison.

Reusable rule:

```text
For engineering geometry papers, the abstract should include at least one concrete equation or numerical result if verified by the main text.
```

Risk:

- The abstract is strong only if those equations and ratios can be traced to model outputs and tables.

## Model Chain

### Stage 1: Rotate and Define the Geometric Frame

The paper sets a coordinate frame around the reflector and incoming electromagnetic wave direction. It uses direction angles and vectors to relate the feed cabin, spherical center, main cable nodes, and reflector surface.

Expected artifacts:

- coordinate/frame diagram;
- symbol table with centers, radii, angles, focal length, node coordinates;
- equations for direction angles and rotation.

Generator rule:

```text
Do not introduce optimization before the coordinate frame is fixed.
```

### Stage 2: Determine the Ideal Paraboloid

The paper builds candidate ideal paraboloids and evaluates them using radial and axial deviation metrics. It derives equations for ideal paraboloids and compares candidate surfaces by deviation.

Observed artifacts:

- cross-section figure for ideal paraboloid and spherical crown;
- deviation relationship plots;
- equations for maximum radial deviation, axial deviation sum, and RMS-style metrics.

Reusable validation:

- compare candidate surfaces by deviation metrics before choosing one;
- use plots to show how deviation changes with distance from the axis.

### Stage 3: Node and Actuator Adjustment

The paper models main-cable nodes and actuator extension. It uses node-neighbor geometry to estimate adjusted node position and reports repeated adjustment until RMS decreases.

Observed artifacts:

- schematic of node movement / cable-node adjustment;
- hexagonal neighbor-node selection diagram;
- table of multiple adjustment iterations;
- table of final coordinates and actuator extension values;
- output file reference such as `result.xlsx`.

Reusable rule:

```text
For engineering adjustment problems, a result table should list object id, original/final coordinates, and control quantity.
```

Validation:

- report RMS or another deviation metric before and after adjustment;
- show the number of adjustment rounds;
- ensure actuator extension limits are checked.

### Stage 4: Reflection and Reception Evaluation

The paper evaluates reflected electromagnetic signal reception. It treats each small reflector panel, projects reflected signal coverage to a plane, and estimates reception ratio, including a Monte Carlo style calculation for overlap or received area.

Observed artifacts:

- schematic flowchart for Monte Carlo reception-ratio calculation;
- reflected-area table;
- plots relating distance or projection to reflected surface position;
- reported reception-ratio comparison between adjusted and baseline reflector states.

Reusable rule:

```text
Evaluation should use a physically meaningful final metric, not only geometric fitting error.
```

For this problem type, the final metric is not just node deviation. It is reception efficiency or signal reception ratio.

## Figure Inventory

Observed figure types:

- cross-section sketch of ideal paraboloid and spherical surface;
- radial/axial deviation curves;
- geometric rotation/coordinate diagram;
- node movement schematic;
- neighbor-node selection hexagon;
- Monte Carlo reception-ratio flowchart;
- reflected-area/projection diagrams;
- final comparison plots.

Minimum generator requirement for similar problems:

- one coordinate/physical setup diagram;
- one target-surface or geometry relation diagram;
- one deviation or residual plot;
- one control-adjustment diagram/table;
- one final physical-performance evaluation plot/table.

## Table Inventory

Observed table types:

- symbol table;
- adjustment iteration table;
- node coordinate and actuator extension table;
- reflected-area/reception-ratio table;
- code file inventory in appendix.

Generator rule:

```text
Engineering papers should not hide all numerical results in prose. At least one table should expose the final control variables.
```

## Appendix Pattern

Pages 24-38 contain code file inventory and code excerpts. The appendix starts with a list of files, including MATLAB scripts and data files. It then maps code to problems.

Reusable appendix contract:

- list every code/data file;
- group files by subquestion;
- name the main scripts;
- include generated data files such as coordinate/result spreadsheets;
- avoid dumping unrelated code without mapping to paper results.

This pattern should be added to the generator's appendix checklist for engineering and optimization problems.

## Quality Signals

Strong signals:

- dense but purposeful formulas;
- visible coordinate and geometric figures;
- result tables for adjustment quantities;
- model evaluation section with advantages, disadvantages, and improvement directions;
- appendix code inventory.

Risk signals:

- heavy watermark and extracted text noise require visual review;
- abstract results must be checked against result tables and appendix outputs;
- Monte Carlo or sampling-based evaluation must state sampling size, seed, and geometry assumptions in a reproducible run.

## Updates Needed Elsewhere

- Strengthen geometry/engineering routing rules with a required physical-performance metric.
- Add a geometry engineering model-chain pattern.
- Add appendix-code inventory rules to review checklist and artifact ledger.
- Ensure visual-generation pipeline treats coordinate sketches and engineering schematics as explanatory figures unless generated from model coordinates.
