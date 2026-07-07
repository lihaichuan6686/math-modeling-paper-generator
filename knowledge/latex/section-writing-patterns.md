# Section Writing Patterns

Purpose: give Claude Code reusable paragraph and artifact patterns for turning model plans into CUMCM-style LaTeX sections. Use this after `cumcm-section-contract.md` and before editing `paper/sections/`.

This file is practical rather than theoretical. It answers: what should the next paragraph, table, figure, or equation be?

## Global Pattern

Every substantial section should follow this rhythm:

```text
claim -> evidence artifact -> interpretation -> limitation or transition
```

Weak pattern:

```text
We use method X. The result is shown below.
```

Strong pattern:

```text
The supplier score is used to convert heterogeneous indicators into a single planning signal. Table~\ref{tab:supplier-score} shows that Supplier A has the highest comprehensive score, mainly because its reliability compensates for its slightly higher unit price. This ranking is then used as the candidate-selection input for the ordering model in Section~\ref{sec:model}.
```

## Evidence Density Targets

For a 20-30 page paper, aim for:

| Section | Minimum evidence |
|---|---|
| Problem analysis | 1 route diagram or task-dependency table |
| Data processing | 2-4 data/feature tables or exploratory figures |
| Model establishment | equations for each subquestion, plus 1 explanatory figure when useful |
| Solution process | algorithm steps, parameter table, or solver setting table |
| Results | at least 1 result table or figure per subquestion |
| Validation | at least 1 robustness, residual, baseline, or feasibility artifact |
| Appendix | code inventory and run notes |

If a section is too short, add missing evidence before adding prose.

## Problem Restatement Pattern

Use this structure:

```text
background in one compact paragraph
task decomposition
input-output-constraint table
transition to modeling route
```

Useful table:

```latex
\begin{table}[H]
\centering
\caption{Task decomposition and modeling outputs}
\label{tab:task-decomposition}
\begin{tabular}{llll}
\toprule
Task & Input & Output & Main constraint \\
\midrule
1 & ... & ... & ... \\
2 & ... & ... & ... \\
\bottomrule
\end{tabular}
\end{table}
```

Do not copy the contest statement. Rewrite it as modelable tasks.

## Problem Analysis Pattern

Use this paragraph order:

1. Identify problem signals.
2. Map each signal to an archetype from `knowledge/cumcm/problem-type-paper-archetypes.md`.
3. Explain why the selected route is better than rejected routes.
4. List expected evidence artifacts.

Useful wording:

```text
The problem is not only an evaluation task, because the final output must be an executable plan. Therefore the route is evaluation -> planning -> scenario audit rather than ranking alone.
```

Recommended artifact:

- route flowchart;
- subquestion dependency table;
- route comparison table.

## Assumptions Pattern

Use a table instead of loose bullets when assumptions affect equations:

```latex
\begin{table}[H]
\centering
\caption{Model assumptions and possible impacts}
\label{tab:assumptions}
\begin{tabular}{p{0.08\textwidth}p{0.34\textwidth}p{0.25\textwidth}p{0.23\textwidth}}
\toprule
No. & Assumption & Reason & Possible impact \\
\midrule
A1 & ... & ... & ... \\
\bottomrule
\end{tabular}
\end{table}
```

Each assumption should be referenced later by an equation, constraint, or limitation.

## Symbols Pattern

Use symbol rows only for variables that appear later:

```latex
\begin{table}[H]
\centering
\caption{Main symbols}
\label{tab:symbols}
\begin{tabular}{lll}
\toprule
Symbol & Meaning & Unit/domain \\
\midrule
$q_{i,t}$ & order quantity from supplier $i$ in week $t$ & unit \\
\bottomrule
\end{tabular}
\end{table}
```

Review check: every symbol in the equation block must appear in the symbol table or be defined immediately nearby.

## Data Processing Pattern

Use this order:

```text
source and fields -> cleaning rules -> normalization/feature construction -> exploratory artifact -> modeling parameter table
```

Useful transition:

```text
After cleaning, the data are converted into the parameters required by the model. Table~\ref{tab:model-params} records this mapping, which prevents the later optimization variables from being disconnected from the original data.
```

Good artifacts:

- data inventory table;
- missing/outlier summary;
- feature construction table;
- normalized indicator table;
- distribution or trend figure.

## Model Establishment Pattern

For each subquestion, write:

```text
Subquestion target
model idea
variables and parameters
objective/equations/constraints
solver or algorithm
expected outputs
limitations
```

Optimization paragraph pattern:

```text
Let $x$ denote the decision variable and $c$ denote the cost coefficient. The objective in Equation~\eqref{eq:objective} minimizes total cost, while Equations~\eqref{eq:capacity}--\eqref{eq:demand} enforce capacity and demand feasibility.
```

Classification paragraph pattern:

```text
The classifier is trained after preprocessing to avoid feature leakage. Model comparison is based on accuracy, macro-F1, and the confusion matrix rather than accuracy alone.
```

Evaluation paragraph pattern:

```text
The evaluation score is not treated as the final answer. It becomes an input to the later planning model, so the ranking table and the decision table must both appear in the paper.
```

## Solution Process Pattern

Use this order:

```text
data path -> algorithm steps -> parameter settings -> output files -> reproducibility note
```

Useful algorithm block:

```latex
\begin{enumerate}
\item Read cleaned data and model parameters.
\item Compute intermediate indicators or model scores.
\item Solve the decision model under constraints.
\item Write tables to \texttt{paper/tables/} and figures to \texttt{paper/figures/}.
\item Record key results in the artifact ledger.
\end{enumerate}
```

Avoid body text that says only "we use Python to calculate".

## Results Pattern

For each result artifact:

```text
what the artifact answers -> the table/figure -> interpretation -> relation to original task
```

Table interpretation pattern:

```text
Table~\ref{tab:plan} gives the executable plan. The rows correspond to time periods, and the decision columns correspond to model variables. The plan satisfies the capacity constraint because no order exceeds the supplier limit.
```

Figure interpretation pattern:

```text
Figure~\ref{fig:sensitivity} shows that total cost increases under higher loss rates. The monotone trend is consistent with the inventory balance equation because higher loss requires larger order quantities.
```

Review check:

- No result table should appear without at least one interpretive paragraph.
- No figure should be used only as decoration.

## Validation Pattern

Use validation that matches the model type:

| Model type | Validation artifact |
|---|---|
| evaluation | rank stability, weight perturbation, method comparison |
| planning | constraint audit, baseline comparison, scenario stress test |
| forecast | train/test error, residual plot, interval or scenario propagation |
| classification | confusion matrix, macro-F1, split policy, leakage check |
| geometry | residual map, physical feasibility, engineering-performance metric |
| simulation | distribution plot, confidence interval, repeated-run stability |

Validation paragraph pattern:

```text
The validation does not prove global optimality; it checks whether the generated result remains credible under the assumptions used by the model. The tested perturbation range is therefore reported explicitly.
```

## Strengths And Limitations Pattern

Tie every strength to evidence:

```text
The first strength is traceability: Table~\ref{tab:ledger} and the generated output paths connect the conclusion to code-produced artifacts.
```

Tie every limitation to a fix:

```text
The main limitation is that supplier weights are fixed. A future version should compare entropy weights, AHP weights, and equal weights to quantify ranking stability.
```

Avoid generic phrases like "the model is simple and effective" unless the evidence explains why.

## Conclusion Pattern

Use this order:

```text
answer each subquestion
state the most important numbers
state the final recommendation
state the uncertainty or human-verification need
```

Do not introduce new methods or new numbers.

## Appendix Pattern

Start with a file inventory:

```latex
\begin{table}[H]
\centering
\caption{Code and output file inventory}
\label{tab:code-inventory}
\begin{tabular}{lll}
\toprule
File & Role & Output \\
\midrule
\texttt{src/demo\_v1.py} & generate demo results & tables and figures \\
\bottomrule
\end{tabular}
\end{table}
```

Then include run notes:

```text
software environment
commands
random seeds
output paths
known limitations
```

Appendix should support reproducibility, not hide the main method.

## Final Draft Scan

Before compiling:

- Every section has a purpose.
- Every main claim points to an equation, table, figure, or ledger entry.
- Every generated figure/table has a caption and text reference.
- Every conclusion number appears in results or validation.
- The appendix lists code and output files.
- Synthetic data are clearly marked.
