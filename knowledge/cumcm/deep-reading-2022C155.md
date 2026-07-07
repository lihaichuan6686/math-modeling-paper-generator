# Deep Reading: 2022 C155 Decision and Planning with Chemical Data

Source:

```text
D:\2-各比赛Word模板及LaTeX模板\国赛历年论文【公众号：竞赛资料网】整理\2022年高教社全国大学生数学建模竞赛优秀论文【公众号：竞赛资料网】】\2022高教社杯全国大学生数学建模竞赛C题论文展示（C155）.pdf
```

Rendered pages reviewed:

```text
knowledge/_generated/c155_review/c155-01.png ... c155-09.png
```

This note is based on rendered-page visual inspection. The PDF is watermarked, so the main value here is structure, method chain, and generator rules.

## Basic Profile

- Year/problem: 2022 C155
- Topic: chemical composition analysis, decision/planning, robustness
- Problem type: data-driven planning, statistical testing, evaluation-to-decision chain
- Main methods:
  - descriptive statistics
  - ANOVA / chi-square style significance testing
  - Pearson and Yates tests
  - feature comparison / indicator construction
  - planning-oriented model linking data to decisions
- Main evidence form:
  - data description table
  - symbol table
  - statistical test tables
  - result tables for composition / decision outputs
  - appendix or supporting calculations

## Why This Paper Matters

This paper is a good example of a planning route that is not purely optimization. It starts with data analysis and then uses the analysis to justify decisions.

Reusable route:

```text
raw data
-> descriptive analysis
-> statistical significance tests
-> indicator/feature interpretation
-> decision or plan construction
-> robustness or sensitivity discussion
```

For a generator, this is important because many contest problems ask for "what should we do" after a data analysis stage, not only "what does the data say."

## Section Structure

Observed structure:

1. Abstract
2. Problem restatement
3. Model assumptions
4. Symbol explanation
5. Problem analysis
6. Model establishment and solution
   - data preprocessing / descriptive statistics
   - statistical testing
   - indicator or feature comparison
   - decision/planning analysis
7. Conclusion or discussion

Generator lesson:

- Data-heavy planning papers need a visible preprocessing or data-description stage.
- Statistical tests should come before decision claims.
- A planning paper can be built from analysis blocks if each block clearly feeds the next one.

## Abstract Pattern

The abstract is highly result-driven:

- it states the material/data context;
- it names the analysis methods;
- it reports the statistical conclusion or best choice;
- it connects the analysis result to a practical decision or recommendation.

Generator rule:

```text
For data-driven planning papers, the abstract should include:
data context -> analysis method -> significant conclusion -> decision implication
```

Avoid:

- ending the abstract at "we analyzed the data";
- reporting statistics without the decision consequence;
- omitting the key test result that justifies the plan.

## Model Chain

### Stage 1: Data Description and Preprocessing

The paper begins by defining the relevant sample groups and preparing the data for analysis.

Observed artifacts:

- sample or factor tables;
- summary statistics;
- clear symbol definitions for the measured quantities.

Generator rule:

```text
For planning problems with scientific data, build a data summary before any hypothesis test or plan.
```

### Stage 2: Statistical Significance Testing

The paper uses statistical tests such as Pearson and Yates checks, plus related comparisons, to determine whether groups or variables are associated.

Observed artifacts:

- contingency-style result tables;
- chi-square or p-value reporting;
- pairwise test outputs;
- class/group comparison tables.

Generator rule:

```text
If a decision is based on whether categories or factors differ, show the test table and the threshold used.
```

This is a useful pattern for the generator: the paper does not just say "significant" but shows the test and the p-value.

### Stage 3: Feature or Indicator Interpretation

The paper compares measurable indicators and interprets which variables matter.

Observed artifacts:

- coefficient or summary tables;
- tables of composition or factor contributions;
- direct comparison between categories or groups.

Generator rule:

```text
If a planning decision depends on multiple factors, identify the most informative indicators before stating the plan.
```

### Stage 4: Decision / Planning Output

The final step is to turn the analysis into an actionable decision or recommendation.

Generator rule:

```text
Evaluation output must feed the plan; do not leave the paper at the statistic-only stage.
```

This is the main lesson shared with supply-chain papers: analysis is not the end state.

## Figure Inventory

Observed figure types from the first-pass pages:

- process or problem context schematic
- data relation or category diagram
- analysis-support or result interpretation plot

Minimum generator requirement for similar problems:

- one data/feature overview figure;
- one analysis-result figure or diagram;
- one figure that helps connect analysis to the final decision.

## Table Inventory

Observed table types:

- data description table
- symbol table
- significance test table
- category or factor comparison table
- final result or decision table

Generator rule:

```text
For scientific planning problems, tables should show the chain from raw data to decision, not only the final answer.
```

## Validation and Review Signals

Strong signals:

- significance tests are explicit and interpretable;
- data analysis is not isolated from the decision;
- the result table has a practical meaning;
- the paper keeps a clean chain from data to recommendation.

Risk signals:

- p-values are reported without context or threshold;
- the paper has test tables but no decision implication;
- too much narrative without data linkage;
- statistical language is used where the actual claim is just a heuristic comparison.

## Generator Rules Added

1. For data-driven planning problems, always put data preprocessing and descriptive statistics before the model.
2. Use significance tests when decisions rely on group differences or factor effects.
3. Convert test outcomes into a decision or plan, not just a statistical conclusion.
4. Keep raw data, statistical tests, and final recommendations in one traceable chain.
5. Make the abstract reflect the final decision implication, not just the analysis method.

