# 2024 E Modern-Draft Risk Reading: Traffic Control Papers Need Decision Closure

Purpose: extend the modern-draft risk corpus to a traffic-flow control E problem and extract rules for generation, layout, evidence, and self-review.

## Corpus

Problem: 2024 CUMCM E, traffic-flow control for a scenic-town road network.

Local materials inspected:

- set-1 complete-paper-labeled PDF: 28 rendered PDF pages;
- set-1 idea PDF: 19 rendered PDF pages;
- set-2 idea PDF: 4 rendered PDF pages.

The complete-paper PDF's first three pages and final two pages were rendered and visually inspected. The idea PDFs were sampled for problem structure and route design. The PDFs include promotional watermarks and public-account residue, so they are route/risk references rather than format exemplars.

## Main Finding

This E problem belongs to a monitoring-to-control route:

```text
road-network interpretation
-> traffic-flow aggregation
-> period / state classification
-> signal-control optimization
-> parking-demand estimation
-> before-after policy evaluation
-> management recommendation
```

It is not enough to forecast traffic or list traffic-control methods. A complete paper must show how data analysis changes a traffic-management decision.

## Structural Lessons

The inspected complete-paper sample frames four tasks:

1. classify a day into periods and estimate directional traffic flow;
2. optimize traffic-signal timing to improve average traffic speed;
3. identify cruising vehicles and estimate temporary parking-space demand;
4. evaluate the effectiveness of temporary traffic-control measures.

The idea PDF adds a useful first-page pattern: start with a road-network map and named intersections before writing formulas. For traffic-control papers, the object of modeling is the network, not only a CSV table.

Reusable section chain:

```text
road-network map and data dictionary
-> time and direction aggregation
-> period classification / traffic state identification
-> queue, flow, or simulation model
-> signal-timing or policy decision variables
-> parking/cruising behavior identification
-> before-after evaluation indicators
-> final control strategy and limitations
```

## Risk Findings

### 1. Question-number consistency can drift

The inspected abstract describes question 1 as period clustering and flow estimation, question 2 as signal optimization, question 3 as parking demand, and question 4 as policy evaluation. The following restatement page shifts the wording and order, putting signal optimization into question 1.

This is a high-risk failure for generated four-question papers.

Hard checks:

- build a question map from the original problem statement;
- require abstract, section headings, result tables, and conclusion to use the same question map;
- reject papers where the same method appears under inconsistent question numbers;
- require one result artifact per question.

### 2. Method lists can hide weak decision evidence

The sample mentions K-means, traffic-flow models, cellular automata or VISSIM, genetic algorithms, queuing models, Monte Carlo simulation, regression, and time-series analysis. This looks rich, but it can become method stacking.

For generation, each method must have a direct evidence output:

- clustering -> period labels and traffic-state table;
- flow model -> directional flow or speed table;
- signal optimization -> timing plan and before-after speed/delay comparison;
- parking model -> cruising-vehicle detection and parking-space estimate;
- evaluation model -> control-effect indicators and uncertainty/robustness statement.

### 3. Road-network figures are mandatory

The idea PDF starts with a map of the scenic-area road network and named monitoring points/intersections. This is the right first visual. The generated paper should not rely only on abstract plots, because readers need to understand road topology, directions, monitored approaches, and decision locations.

Minimum visual inventory:

- road-network / intersection map;
- time-of-day traffic-flow plot;
- directional flow or heatmap by approach;
- signal-timing comparison chart or table;
- parking-demand / cruising-vehicle evidence figure;
- before-after control-effect comparison.

### 4. Code screenshots are not reproducibility

The complete-paper final pages show a code screenshot reading `Attachment 2.csv`, parsing time fields, grouping by month/day/hour/direction, scaling data, sampling 50,000 records with a fixed random seed, and exporting a sampled CSV.

This is useful evidence for preprocessing, but it is not enough for full reproducibility.

The review should verify:

- whether actual scripts/notebooks exist outside screenshots;
- whether code covers all four questions, not just preprocessing;
- whether output filenames appear in the paper's tables/figures;
- whether random seeds, sample sizes, and encodings are stated;
- whether the optimization and evaluation outputs can be regenerated.

### 5. Effective page count and residue still matter

The complete-paper PDF has 28 pages, which matches the target range, but the final page is mostly a code screenshot plus blank space and a promotional watermark. As in 2024 B/C/D, page count should be audited as effective argument length.

Hard checks:

- exclude blank/residue-only pages from effective length;
- reject watermark and public-account header/footer residue;
- require appendix pages to contain runnable artifact references, not only images.

## Generator Gates

Add or strengthen these checks for traffic-control E routes:

- `question_map_gate`: abstract, headings, conclusions, and result tables use the same problem-question mapping.
- `network_map_gate`: the road network, intersections, monitoring directions, and decision locations are visualized.
- `data_dictionary_gate`: attachments, fields, time span, direction labels, and units are documented.
- `method_output_gate`: every named method has a named table, figure, or policy output.
- `control_decision_gate`: analysis leads to signal timing, parking-space, or management recommendations.
- `before_after_gate`: control effects are compared against baseline indicators such as speed, delay, flow, queue, or travel time.
- `code_coverage_gate`: code covers preprocessing, modeling, optimization, and evaluation, not only data cleaning.
- `artifact_trace_gate`: generated figures/tables name the producing script and input attachment.
- `effective_length_gate`: target page count excludes blank, watermark-only, and screenshot-only filler.
- `residue_gate`: rendered PDF contains no public-account headers, watermarks, or promotional text.

## Page Blueprint For Traffic-Control E Papers

Target body:

- Abstract: 0.8-1 page, one result sentence per question.
- Problem restatement and road-network description: 2 pages, including a map.
- Data dictionary and preprocessing: 2-3 pages.
- Question 1 period classification and flow estimation: 3-4 pages.
- Question 2 signal optimization: 4-5 pages.
- Question 3 cruising / parking demand: 3-4 pages.
- Question 4 before-after control evaluation: 3-4 pages.
- Sensitivity and robustness: 2 pages.
- Strengths, limitations, and recommendations: 1.5-2 pages.
- References and reproducibility inventory: 1-2 pages.

## Review Questions

When reviewing a generated traffic-control E paper, ask:

1. Is the road network visible before the algorithms are introduced?
2. Are data fields, monitoring directions, and time ranges documented?
3. Does the question mapping stay consistent from abstract to conclusion?
4. Does every algorithm produce a visible table, figure, or control decision?
5. Are signal-timing decisions and constraints explicitly reported?
6. Is parking demand tied to identified cruising behavior rather than guessed?
7. Is the control effect evaluated with baseline and post-control indicators?
8. Can the code regenerate the figures/tables and not just preprocess a CSV?
9. Does the rendered PDF avoid watermarks, public-account residue, and blank filler?

## Status

This note is a risk-reading extension for the v1 generator's E-type route. It should feed generation planning and quality gates, not be treated as an endorsement of the inspected source drafts.
