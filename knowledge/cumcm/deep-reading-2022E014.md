# Deep Reading: 2022 E014

Source: `D:\2-各比赛Word模板及LaTeX模板\国赛历年论文【公众号：竞赛资料网】整理\2022年高教社全国大学生数学建模竞赛优秀论文【公众号：竞赛资料网】】\2022高教社杯全国大学生数学建模竞赛E题论文展示（E014）.pdf`

Problem type: production scheduling based on time-series prediction with service-level control.

Paper title observed from rendered PDF: material production scheduling model based on time-series prediction.

Pages: 24 total.

- Pages 1-2: abstract, problem restatement, and question analysis.
- Pages 3-8: material screening, demand-pattern observation, and time-series trend or periodic fitting.
- Pages 9-12: forecast-versus-actual comparison and prediction method setup.
- Pages 13-16: service-level analysis and first-stage rolling production model.
- Pages 17-20: second-stage capacity-use model, result summary, evaluation, and references.
- Pages 21-24: appendix support-material list and MATLAB code.

Note: this paper is scan-like, so the note is based mainly on rendered-page visual inspection.

## Why This Paper Matters

This paper is one of the clearest conservative production-route E samples in the local collection. Its route is:

```text
historical material-demand data
-> key-material screening
-> time-pattern reading
-> time-series prediction
-> support-rate and service-level analysis
-> rolling production rule with parameter tuning
-> alternative capacity-use model
-> appendix support files and code
```

Compared with `2022 E029`, this paper is less "dynamic optimization first" and more "service-level stability first." That makes it especially useful for building a safer, more conservative production-template route for the generator.

## Research Question and Significance

Core question:

- how to predict short-term demand for representative materials;
- how to arrange production under different capacity assumptions;
- how to keep service level high while controlling inventory and shortage risk.

Why it matters:

- many production E-type problems are not only about maximizing output;
- a contest-grade solution often needs to show robust support ability;
- this paper gives a useful example of rule-based parameter tuning built on top of forecasts.

## Methodology

### Data and Problem Setup

Observed setup:

- the paper starts from historical material-demand or order records;
- it screens six representative materials;
- the later modeling focuses on months 101-110 and 110-117 style windows;
- the decision layer is evaluated with support rate and service level.

Observed evidence:

- material-screening table;
- demand scatterplots for representative materials;
- support-material file list in the appendix;
- forecast-vs-actual tables and production-result tables.

Generator rule:

```text
For conservative production-route E papers, narrow the material set early and make service-level evaluation visible from the beginning.
```

### Stage 1: Material Screening

The paper chooses six representative materials instead of treating the full material list uniformly.

Observed signals:

- a reduced set of key material codes;
- qualitative comments about demand frequency and usefulness;
- early transition from screening to demand-structure observation.

Why it matters:

- simplifies later production logic;
- makes rule tuning feasible;
- keeps the final tables readable.

Generator rule:

```text
If the final production rule is material-specific, the paper should first justify why those materials are the focus set.
```

### Stage 2: Time-Pattern Reading and Prediction

The paper studies the historical behavior of the selected materials and then compares predicted values with actual values.

Observed signals:

- scatterplots or fitted plots for selected materials;
- actual-versus-forecast tables;
- forecast error terms and variance-style summaries;
- visual overlays of actual and predicted demand.

The prediction layer appears less about aggressive model comparison and more about obtaining operationally usable forecasts.

Generator rule:

```text
For robust production papers, forecasting can be simpler than in optimization-heavy papers, but it must still be audited against actual values.
```

### Stage 3: Service-Level and Support Analysis

This is the real center of gravity of the paper.

Observed results:

- average production demand and average demand forecasts;
- average production quantity;
- support quantity and service level;
- multiple tables showing some materials at 100% support and others lower.

The paper explicitly reasons about:

- whether a material can be fully supported;
- how much safety margin is needed;
- how different production assumptions affect average service level.

Generator rule:

```text
A service-level-first production paper should evaluate production plans using both support quantity and service rate, not only forecast accuracy.
```

### Stage 4: Rolling Production Model With Tuned Parameters

One of the most distinctive features of this paper is the parameterized rolling rule.

Observed structure:

- production in the next period depends on predicted demand and current inventory;
- a piecewise or banded parameter table adjusts reaction strength;
- different deviation intervals map to different control coefficients;
- the paper explains the logic of being more or less conservative depending on the sign and scale of demand gaps.

This is a very valuable generator lesson because it is not a black-box optimizer. It is a controllable policy rule.

Generator rule:

```text
When the decision model is rule-based rather than solver-based, write the parameter intervals and their operational meaning explicitly.
```

### Stage 5: Alternative Capacity-Use Assumptions

The paper studies at least two capacity settings:

- a model under one capacity assumption;
- a second model under a different capacity-use assumption.

Observed evidence:

- separate equations and tables for `k=1` and `k=2` style capacity cases;
- comparison of resulting support levels;
- summary statements about which scenario gives stronger service performance.

Generator rule:

```text
For production-route E papers, alternate capacity assumptions are a useful way to produce scenario analysis without building a huge global optimizer.
```

## Key Findings

Main observed findings:

1. The selected materials have enough structure to support short-term forecasting and rolling production decisions.
2. Service level is the paper's dominant success metric, not raw output alone.
3. A tuned rolling rule can keep most key materials at high support rates.
4. Different capacity assumptions materially affect support performance, and the paper uses this to compare plans.

## Interpretation and Implications

Interpretation:

- this is a more cautious and policy-like production paper than `E029`;
- the operational logic is readable because the control parameters are explicitly tabulated;
- the paper is especially useful for the generator when we want a "safe" production answer rather than an aggressive optimization narrative.

Practical implication for the generator:

```text
If the production task emphasizes fulfillment reliability, prefer service-level-first rolling rules over purely profit- or quantity-centered narratives.
```

## Figure Inventory

Observed figure types:

- representative-material scatterplots;
- fitted trend or periodicity figures;
- actual-versus-forecast overlay plots;
- production-support visual summaries.

Minimum generator requirement for similar problems:

- one material-screening or representative-material figure block;
- one actual-versus-forecast figure block;
- one service-level result table or visual block;
- one scenario-comparison block when multiple capacity assumptions are used.

## Table Inventory

Observed table types:

- key-material screening table;
- forecast-versus-actual table;
- service-level result table;
- parameter-interval tuning table;
- scenario result tables for different capacity assumptions;
- support-material list in the appendix.

Generator rule:

```text
If the production policy uses tuned coefficients, those coefficients should live in a dedicated interpretation table.
```

## Appendix Pattern

The appendix has two useful parts:

- a left-hand support-material list by question;
- MATLAB code fragments implementing the forecasting and rolling production logic.

This is a strong, lightweight appendix pattern:

- list the spreadsheets used for each subproblem;
- keep the code fragments question-bound;
- make it easy to trace results back to files even without a large software project.

## Quality Signals

Strong signals:

- service level is clearly foregrounded as the operational criterion;
- the paper shows actual-versus-forecast comparison instead of hiding forecast performance;
- the rolling rule is interpretable because the parameters are banded and explained;
- scenario comparison is built into the model structure;
- appendix support files are organized by question.

Risk signals:

- the forecasting layer looks more practical than theoretically rich, so a stronger generated version should explain model choice more explicitly;
- the rule-based tuning is readable, but a future generated paper should add sensitivity evidence for the chosen interval boundaries;
- because the paper is compact, some business assumptions around capacity and inventory reset may need clearer narration in generated output.

## Reusable Generator Rules

1. Screen key materials early.
2. Compare forecast values against actual values explicitly.
3. Turn forecasting into support-rate and service-level evaluation before final production planning.
4. If using a rolling control rule, publish the parameter intervals and what each interval means.
5. Use scenario comparison when multiple capacity assumptions are plausible.
6. Prefer interpretable rule-based policies when the paper wants robust fulfillment logic.
7. Keep appendix file lists organized by subproblem.

## Revisions Needed Elsewhere

- Mark `2022 E014` as the conservative production-route companion to `2022 E029`.
- Update the E-route comparison note so `E014` and `E029` become a full production-route pair.
- Add a production-route E checklist item for coefficient-band interpretation and service-level-first reporting.
