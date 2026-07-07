# Deep Reading: 2022 E029

Source: `D:\2-各比赛Word模板及LaTeX模板\国赛历年论文【公众号：竞赛资料网】整理\2022年高教社全国大学生数学建模竞赛优秀论文【公众号：竞赛资料网】】\2022高教社杯全国大学生数学建模竞赛E题论文展示（E029）.pdf`

Problem type: production planning based on time-series prediction.

Paper title observed from rendered PDF: dynamic production optimization model based on time-series prediction.

Pages: 22 total.

- Pages 1-2: abstract, problem restatement, and problem analysis.
- Pages 3-8: data screening, order statistics, material grouping, and periodic-pattern reading.
- Pages 9-12: ARIMA forecasting route, model comparison, residual checking, and forecast-weight construction.
- Pages 13-16: safety-stock and service-level analysis for selected materials and production plans.
- Pages 17-18: dynamic production model summary, model evaluation, and references.
- Pages 19-22: appendix and MATLAB program code.

Note: this paper is largely scan-like, so the note is based mainly on rendered-page visual inspection.

## Why This Paper Matters

This paper is a very strong production-route E sample because it shows a clean, industrially plausible chain:

```text
historical order-volume data
-> material screening and grouping
-> periodic-pattern analysis
-> ARIMA demand forecasting
-> forecast-weight construction
-> safety-stock and service-level reasoning
-> dynamic production planning
-> code appendix
```

The important lesson is that prediction is not the headline by itself. The paper uses prediction as a bridge into an executable production decision.

## Research Question and Significance

Core question:

- how to use historical order data to predict future demand for key materials;
- how to convert those predictions into dynamic production decisions under inventory and service-level constraints.

Why it matters:

- this is a classic E-type contest route where forecasting must support operations;
- the paper is a good reference for generator design because it produces business-style outputs rather than stopping at model fit;
- it is a compact but complete example of turning uncertain demand into feasible scheduling logic.

## Methodology

### Data and Problem Setup

Observed setup:

- the paper works from historical order volumes for many material codes;
- it screens down to a smaller set of high-frequency or high-importance materials;
- the selected materials are then studied for periodic behavior and demand variation.

Observed evidence:

- order-volume summary tables;
- material screening table;
- monthly or periodic scatter/bar figures;
- service-level and inventory comparison tables.

Generator rule:

```text
For production-route E papers, identify the key materials before forecasting all items equally.
```

### Stage 1: Material Screening and Grouping

The paper does not forecast every item symmetrically. It first narrows attention to representative materials and groups their demand behavior.

Observed artifacts:

- top-material or candidate-material lists;
- group-specific order figures;
- discussion of high-frequency and stable-demand materials.

Why this matters:

- it reduces dimensionality;
- it makes the later production model easier to explain;
- it gives a clear reason for why only some materials are used to drive the dynamic plan.

Generator rule:

```text
If the raw SKU or material space is large, add a screening step before deep forecasting and optimization.
```

### Stage 2: Periodic Analysis

The paper checks periodicity before forecasting. The selected materials show repeating order patterns that justify time-series modeling.

Observed signals:

- grouped periodic plots;
- narrative around repeated cycles;
- transition from pattern reading to formal forecasting.

Generator rule:

```text
For production-route E papers, show that demand has usable temporal structure before committing to a forecasting model.
```

### Stage 3: ARIMA Forecasting

This is the clearest technical core in the middle of the paper.

Observed route:

- use recent actual data as the base sequence;
- construct ARIMA candidates;
- compare several candidate models;
- inspect residual behavior;
- choose the best-fitting ARIMA route for each target material.

Observed evidence:

- ARIMA candidate table with fit quality;
- residual diagnostics table;
- forecast curves or predicted-value table;
- explicit mention of white-noise style residual checking.

The paper also builds a forecast-weight mechanism:

- convert predicted volumes into normalized weights;
- use those weights later in planning and service-level reasoning.

Generator rule:

```text
Forecasting sections should include model comparison and residual checking, not just one chosen model.
```

### Stage 4: Safety Stock and Service Level

This is one of the most valuable production-route moves.

The paper turns predicted demand into:

- safety-stock calculations;
- service-level estimates;
- material-level support or shortage summaries.

Observed artifacts:

- tables listing expected inventory, support quantity, and service level;
- production-plan tables with current inventory, production quantity, and safety-stock gap;
- statements showing which materials meet 100% service and which are weaker.

Generator rule:

```text
For production E papers, prediction results should be translated into inventory risk and service-level language before final scheduling.
```

### Stage 5: Dynamic Production Optimization

The later model layer is a compact dynamic production-planning model.

Observed structure:

- next-period production depends on previous inventory and predicted demand;
- explicit constraints appear for inventory nonnegativity, production bounds, and shortage control;
- the objective or evaluation logic balances feasible output with lower shortage risk.

Observed equations and appendix code suggest:

- rolling-period production updates;
- shortage or loss counting;
- inventory carry-over;
- scenario-like repeated calculation across weeks.

Generator rule:

```text
A production-route E paper should express the production update equation, the inventory carry-over relation, and the shortage or service metric explicitly.
```

## Key Findings

Main observed findings:

1. A screened subset of materials can represent the meaningful production-driving demand behavior.
2. ARIMA can capture short-term order structure well enough to support operational planning.
3. The production plan is judged not only by quantity but also by support level and service rate.
4. The paper obtains high service levels for most key materials after combining prediction and dynamic planning.

## Interpretation and Implications

Interpretation:

- the paper treats forecasting as an operational input, not a final research result;
- grouping and screening are what make the forecast-to-plan chain manageable;
- service-level reporting makes the result legible to a business or factory decision-maker.

Practical implication for the generator:

```text
When the problem asks for production decisions, always continue from "forecast quantity" to "inventory consequence" to "production action."
```

## Figure Inventory

Observed figure types:

- grouped order-volume plots;
- periodic-pattern plots for selected materials;
- ARIMA fit or forecast comparison figures;
- residual or forecast-performance visual evidence.

Minimum generator requirement for similar problems:

- one material-screening or importance figure;
- one periodicity figure set;
- one forecasting comparison figure;
- one production-result or service-level figure/table block.

## Table Inventory

Observed table types:

- material screening table;
- periodic grouping summary;
- ARIMA candidate comparison table;
- residual-check table;
- production-plan table;
- safety-stock and service-level tables.

Generator rule:

```text
Production-route E papers should use tables to show decision feasibility, not just model coefficients.
```

## Appendix Pattern

The appendix is modest but meaningful.

Observed evidence:

- MATLAB code pages;
- forecasting and production-update logic;
- looping structure over materials and time windows;
- shortage and inventory calculations.

This gives a good appendix template:

- keep the forecasting code traceable;
- show the production-update logic, not only preprocessing;
- include enough code to prove the paper's dynamic plan is executable.

## Quality Signals

Strong signals:

- clear material screening before detailed modeling;
- periodic analysis justifies the choice of forecasting route;
- ARIMA model comparison and residual checking are both present;
- prediction outputs are converted into service-level and safety-stock decisions;
- appendix code aligns with the dynamic production narrative.

Risk signals:

- the paper is compact, so some business assumptions may be under-explained;
- a stronger generated version should make the service-level threshold choice more explicit;
- sensitivity analysis on production bounds or inventory parameters appears limited from the observed pages.

## Reusable Generator Rules

1. Screen key materials before forecasting.
2. Use periodic-pattern evidence to justify time-series forecasting.
3. Compare multiple ARIMA candidates and check residuals.
4. Convert forecasts into normalized planning weights when needed.
5. Report safety stock, service level, and support quantity, not only predicted demand.
6. Express rolling inventory and production update equations explicitly.
7. Include code evidence for both forecasting and production logic.

## Revisions Needed Elsewhere

- Add `2022 E029` as the production-route anchor in the E-paper archetype.
- Update the E-route comparison note to treat `E029` as a full deep-read reference, not only a quick contrast sample.
- Add a production-route E checklist item: forecast -> safety stock -> service level -> rolling production plan.
