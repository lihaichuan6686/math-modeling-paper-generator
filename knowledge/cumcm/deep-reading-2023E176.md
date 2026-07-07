# Deep Reading: 2023 E176

Source: `D:\2-各比赛Word模板及LaTeX模板\国赛历年论文【公众号：竞赛资料网】整理\2023年高教社全国大学生数学建模竞赛优秀论文【公众号：竞赛资料网】\E176.pdf`

Problem type: monitoring design, hydrology data analysis, and trend prediction.

Paper title observed from rendered PDF: study on the optimal monitoring scheme of Xiaolangdi Reservoir based on wavelet transform and knapsack model.

Pages: 50-page PDF with a long appendix and support-material inventory.

- Pages 1-2: abstract, problem restatement, assumptions, and overall route.
- Pages 3-8: problem 1, including seasonal indices, sinusoidal fitting, and double-log regression.
- Pages 9-14: problem 2, including descriptive statistics, monthly distribution, monthly indices, change-point tests, and wavelet analysis.
- Pages 14-18: problem 3, including R/S analysis, Holt exponential smoothing, future trend prediction, and 0-1 monitoring design.
- Pages 19-21: problem 4, including micro-element calculation, water-sediment effect assessment, and GM(1,1) ten-year riverbed prediction.
- Pages 21-22: model evaluation, extension, and references.
- Pages 23-50: appendix and support materials, including Python and MATLAB code plus data-processing flow.

Note: this paper is mostly scan-like, so the note is based mainly on rendered-page visual inspection.

## Why This Paper Matters

This is a very useful route example for data-heavy CUMCM papers because it does not force one master model onto all four subproblems. Instead, it builds a layered workflow:

```text
data cleaning and aggregation
-> seasonal description
-> relation fitting
-> periodicity and abruptness diagnosis
-> future trend prediction
-> information-aware monitoring optimization
-> policy-effect evaluation
-> long-horizon consequence forecast
```

The key lesson is structural. The paper wins by matching each question to an appropriate method family, while still keeping the whole paper coherent through one shared data pipeline and one shared hydrology narrative.

## Abstract Pattern

The abstract is dense and method-forward. It explicitly lists:

- missing-value and data-cleaning work;
- seasonal index construction;
- regression relations between sediment, water level, and flow;
- M-K and Fisher methods for abruptness;
- wavelet transform for periodicity;
- R/S analysis and Holt forecasting for future trend;
- 0-1 knapsack style monitoring design;
- micro-element method and GM(1,1) for riverbed-elevation consequences.

Reusable rule:

```text
For multi-question data-analysis papers, the abstract should name one core method per subproblem and end with concrete judgment statements, not just a toolbox list.
```

## Section Structure

Observed main structure:

1. Abstract
2. Problem restatement
3. Assumptions
4. Symbol definitions and route diagram
5. Model establishment and solution
   - problem 1: relation analysis and annual totals
   - problem 2: seasonality, periodicity, and abruptness
   - problem 3: two-year prediction and optimal monitoring scheme
   - problem 4: effect of water-sediment regulation and ten-year riverbed trend
6. Model evaluation and extension
7. References
8. Appendix and support materials

Generator lesson:

- This paper is an excellent example of how a 20-30 page contest paper can become long naturally.
- Each subproblem has its own mini-route, figures, tables, and closing conclusions.
- The final paper length comes from disciplined section allocation, not filler.

## Model Chain

### Stage 1: Data Cleaning and Time-Scale Conversion

The paper first standardizes raw monitoring records, fills or removes invalid points, and converts the data into daily and monthly series.

Observed appendix evidence:

- Python data-processing classes;
- workbook conversion and aggregation code;
- day-level and month-level averaging logic;
- support-material tree that maps files to each question.

Generator rule:

```text
For monitoring problems, define the data-cleaning and aggregation pipeline before any modeling claim.
```

### Stage 2: Seasonal Description and Relation Fitting

Problem 1 uses:

- monthly distribution tables;
- monthly index plots;
- seasonal index summaries;
- sinusoidal fitting to time;
- double-log regression between sediment and water level;
- double-log regression between sediment and flow.

The paper explicitly avoids building a two-variable regression with both water level and flow because it first shows that those two variables are highly linearly correlated.

Generator rule:

```text
Before fitting a multivariable relation, check whether candidate explanatory variables are too strongly correlated to be used together.
```

### Stage 3: Periodicity and Abruptness Diagnosis

Problem 2 uses a staged diagnosis:

- descriptive statistics first;
- monthly distribution and monthly indices second;
- time-series plots and triangle or sinusoidal periodic fitting;
- M-K test for abruptness;
- Fisher optimal split for change-point support;
- wavelet contour and variance plots for main and secondary periods.

Observed conclusions:

- water and sediment both have a strong annual-scale periodicity;
- 2018 is treated as an important abrupt-change period;
- wavelet analysis is used as a stronger visual and scale-based confirmation of the periodic structure.

Generator rule:

```text
For time-series diagnosis, use a layered chain of descriptive evidence, formal test evidence, and scale-space evidence instead of a single test.
```

### Stage 4: Trend Prediction and Monitoring Optimization

Problem 3 is especially valuable for the generator because it connects prediction to decision.

The route is:

```text
R/S analysis
-> Hurst-based trend judgment
-> Holt exponential smoothing for the next 2 years
-> wavelet-based future time-scale change reading
-> dynamic-information proxy
-> 0-1 optimization for monitoring frequency
```

Important observed details:

- the paper uses R/S analysis to judge whether the future tends to continue, reverse, or randomize;
- it uses Holt smoothing to obtain the next two years of water and sediment sequences;
- it then converts the predicted month-to-month change into an information proxy;
- the monitoring plan is formulated as a minimum-sampling 0-1 model under an average-information constraint;
- the final scheme chooses not to monitor May and to monitor the other months.

Generator rule:

```text
A strong contest paper should make prediction outputs feed directly into a downstream optimization or management decision.
```

### Stage 5: Policy-Effect Evaluation and Long-Horizon Consequence

Problem 4 evaluates the effect of water-sediment regulation with a new route:

- micro-element method to compute average riverbed elevation from section points;
- comparison before and after the intervention;
- water-volume and sediment-volume comparisons;
- construction of a new short time series that removes the yearly intervention effect;
- GM(1,1) forecasting of ten-year riverbed-elevation trend.

Observed conclusions:

- yearly regulation keeps the riverbed elevation around 45m and prevents continued rise;
- water- and sediment-volume effects are less stable than the riverbed-elevation effect;
- without continued regulation, the riverbed elevation is predicted to rise to about 64.79m after ten years.

Generator rule:

```text
For policy-effect questions, separate short-term intervention comparison from long-term no-intervention consequence forecasting.
```

## Figure Inventory

Observed figure types:

- route diagram across four subproblems;
- monthly-index line charts;
- seasonal bar charts;
- scatter plots for relation fitting;
- fitted time-series curves;
- wavelet contour plots;
- wavelet variance plots;
- historical-versus-forecast comparison plots;
- cross-section schematic for the micro-element method;
- intervention effect comparison charts;
- long-term GM(1,1) forecast plot;
- appendix support-material tree.

Minimum generator requirement for similar monitoring papers:

- one global route figure;
- one descriptive seasonality figure set;
- one regression evidence figure set;
- one periodicity figure set with wavelet visuals;
- one prediction-versus-history figure set;
- one optimization-result table or chart;
- one physical-meaning schematic for the evaluation model.

## Table Inventory

Observed table types:

- statistical feature table;
- monthly distribution tables;
- monthly index tables;
- regression parameter tables;
- forecast-error table;
- month-by-month monitoring decision table;
- reconstructed time-series table for riverbed elevation;
- GM(1,1) simulation and forecast table;
- support-material mapping table.

Generator rule:

```text
For long data-analysis papers, tables should carry the parameter and decision evidence, while figures carry the trend and structure evidence.
```

## Appendix Pattern

The appendix is one of the strongest parts of the paper.

Observed support-material organization:

- question 1 program and results:
  - double-log regression;
  - annual runoff and annual sediment calculations;
- question 2 program and results:
  - seasonality;
  - periodicity;
  - abruptness;
  - Excel support data;
- question 3 program and results:
  - R/S analysis;
  - wavelet analysis;
  - Excel outputs for monitoring scheme;
- question 4 program and results:
  - Python data processing;
  - intermediate data cleaning;
  - averaging and sorting utilities;
  - final effect-analysis outputs.

This is a valuable appendix pattern for the agent:

- keep a support-material tree;
- map each file group to the question it serves;
- allow mixed-language tooling when justified;
- show the preprocessing code, not just the final solver code.

## Quality Signals

Strong signals:

- each question has a distinct but appropriate method route;
- the paper uses a shared data pipeline, so the multi-method structure still feels coherent;
- periodicity is supported by both simple charts and wavelet evidence;
- prediction is connected to an actionable monitoring design problem;
- policy evaluation uses both explanatory schematics and numerical comparison;
- the appendix shows code and file organization rather than pretending the paper is detached from computation.

Risk signals:

- the method stack is very broad, so a generated paper could become method-dump-like if transitions are not written carefully;
- some fitted functional forms appear practical rather than deeply justified, so a future generator should explain why each form is chosen;
- the final monitoring optimization is elegant but light, so a stronger generated version should add sensitivity analysis on the information threshold or budget.

## Reusable Generator Rules

1. Start with a visible data pipeline for raw monitoring data.
2. Let each subproblem have one main method family, but keep them connected through shared variables and narrative.
3. Use descriptive statistics before formal time-series testing.
4. Check explanatory-variable correlation before building regression models.
5. Diagnose periodicity with both simple plots and wavelet-based scale evidence.
6. Make forecast outputs feed into a downstream decision model.
7. Use a clear information proxy when translating time-series change into monitoring value.
8. For intervention assessment, compare before and after first, then build a long-horizon counterfactual forecast.
9. Use an appendix support-material tree so code, spreadsheets, and plots remain traceable.

## Revisions Needed Elsewhere

- Add a monitoring and hydrology route card to the problem-type library.
- Strengthen the paper blueprint with a rule that each subproblem should include its own model-result-conclusion mini-loop.
- Add a quality-rubric item for "prediction must feed decision" when the problem asks for future planning.
- Add an appendix standard that mixed Python, MATLAB, Excel, and LINGO workflows must still be traceable by question.
