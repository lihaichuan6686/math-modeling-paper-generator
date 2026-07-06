# Deep Reading: 2021 C066

Source: `国赛历年论文.../2021年高教社全国大学生数学建模竞赛优秀论文.../C066.pdf`

Problem type: supply-chain evaluation and planning.

Paper title observed from rendered PDF: production enterprise raw-material ordering and transport evaluation/planning model.

Pages: 60 total.

- Pages 1-32: main paper and appendix summary/symbol table.
- Pages 33-60: code appendix.

Note: text extraction is dominated by watermark text, so this note is based primarily on rendered-page visual inspection.

## Why This Paper Matters

This paper is a strong supply-chain example because it does not stop at supplier ranking. It builds a full chain:

```text
data preprocessing
-> supplier evaluation
-> supplier selection
-> ordering plan
-> transshipment plan
-> inventory/capacity analysis
-> scenario or stability analysis
-> appendix code and data inventory
```

This directly supports the generator rule:

```text
evaluation is not the final answer when the problem asks for a plan.
```

## Abstract Pattern

The abstract is long and result-driven. It names:

- preprocessing of supplier/order data;
- TOPSIS-based supplier evaluation;
- the selected supplier set;
- ordering and transportation planning;
- genetic algorithm / greedy / iterative or planning methods;
- concrete supplier IDs and capacity/productivity conclusions.

Reusable rule:

```text
For supply-chain papers, the abstract should include both selected suppliers and planning results. A supplier ranking alone is insufficient.
```

## Section Structure

Observed main structure:

1. Abstract
2. Problem restatement and analysis
3. Symbol explanation
4. Data preprocessing
5. Model establishment and solution
   - supplier evaluation and TOPSIS
   - supplier screening/selection
   - order-plan model
   - transshipment/carrier allocation model
   - inventory and production-capacity analysis
6. Model evaluation or strengths/weaknesses
7. Appendix file list, supplementary tables, and code

Generator lesson:

- For data-rich planning problems, data preprocessing deserves its own section before modeling.
- The symbol table may be repeated or expanded near appendix when the planning model has many time-indexed variables.
- The paper uses many tables; this is appropriate because the final answer is a plan.

## Model Chain

### Stage 1: Data Preprocessing

The paper begins by cleaning and summarizing supplier order/supply data. It identifies abnormal records and constructs supplier-level statistics.

Observed artifacts:

- supplier statistical analysis table;
- discussion of order volume and supply volume deviation;
- deleted or preprocessed supplier data table in appendix.

Generator rule:

```text
For supply-chain problems, construct supplier-level features before scoring or optimization.
```

### Stage 2: Supplier Indicator System

The paper builds a multi-indicator evaluation model with dimensions such as:

- supply frequency;
- average supply quantity;
- maximum supply quantity;
- supply stability;
- continuity or continuous supply days;
- reasonableness or reliability indicators.

Observed artifact:

- hierarchy diagram for the supplier multi-indicator evaluation model.

Generator rule:

```text
The indicator hierarchy should be shown as a figure before TOPSIS formulas.
```

### Stage 3: TOPSIS and Supplier Screening

The paper applies entropy weighting / indicator weighting and TOPSIS-like closeness evaluation. It produces supplier weights and screening results.

Observed artifacts:

- TOPSIS algorithm steps table;
- indicator weight table;
- selected supplier list table;
- convergence or optimization curve for supplier selection.

Generator rule:

```text
Evaluation output must feed the planning model through selected suppliers or supplier parameters.
```

Risk:

- if TOPSIS ranking is not connected to the later order plan, the paper becomes two disconnected mini-papers.

### Stage 4: Ordering Plan and Transport Plan

The paper creates a 24-week ordering scheme and transport scheme. It tracks inventory and material category proportions.

Observed artifacts:

- 24-week inventory change curve;
- raw-material category share bar chart;
- transport scheme loss/productivity ratio chart;
- planning tables for selected periods;
- formula linking loss rate, product conversion, and production capacity.

Generator rule:

```text
For planning problems, result figures should show time evolution, not only a final total.
```

### Stage 5: Rationality and Stability Analysis

The paper discusses whether a week-by-week plan is reasonable based on inventory stability, production capacity, supplier composition, and material type shares.

Observed artifacts:

- selected-week material supplier share pie charts;
- inventory change charts;
- capacity or productivity comparison metrics.

Generator rule:

```text
Supply-chain validation should include inventory stability and capacity feasibility, not only cost minimization.
```

## Figure Inventory

Observed figure types:

- supplier evaluation hierarchy diagram;
- convergence or objective-change curve;
- supply/order time-series plots;
- inventory change curve over 24 weeks;
- material share bar chart;
- transport-loss or productivity ratio curve;
- material supplier share pie charts;
- code appendix screenshots/printed code pages.

Minimum generator requirement for similar problems:

- one indicator hierarchy figure;
- one supplier-score or selection table;
- one order-plan table;
- one transport/allocation table;
- one time-series/inventory curve;
- one robustness or stability figure/table.

## Table Inventory

Observed table types:

- symbol table;
- supplier statistics table;
- indicator weight table;
- TOPSIS evaluation result table;
- selected supplier table;
- order and transport plan tables;
- appendix file list;
- supplementary supplier/preprocessed-data table.

Generator rule:

```text
The artifact ledger must distinguish evaluation tables from executable plan tables.
```

## Appendix Pattern

The appendix begins with a file list, including:

- ordering scheme data spreadsheet;
- transshipment scheme data spreadsheet;
- deleted/preprocessed data spreadsheet;
- several Python code files grouped by subquestion;
- problem-related PDF or supporting files.

Reusable appendix contract:

- list data spreadsheets and code files separately;
- group code by subproblem;
- include supplementary tables that are too large for the main text;
- ensure final plan tables can be traced to code/data files.

## Quality Signals

Strong signals:

- ranking result is converted into supplier selection and then planning;
- time-indexed inventory and order figures validate operational feasibility;
- multiple visual forms support the story: hierarchy, curves, bars, pies, tables;
- appendix contains code and data file inventory.

Risk signals:

- too many supplier IDs in prose can become unreadable unless tables carry the result;
- TOPSIS weights and later optimization objectives must be connected explicitly;
- genetic/greedy/iterative methods need parameter settings and reproducibility records;
- pie charts are explanatory and should not replace quantitative tables.

## Updates Needed Elsewhere

- Strengthen supply-chain routing rules: require selected supplier list plus executable order/transport plan.
- Strengthen artifact ledger: distinguish evaluation result, decision result, and validation result.
- Ensure model-chain patterns require inventory/capacity validation for supply-chain planning.
