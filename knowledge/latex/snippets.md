# LaTeX Snippets for CUMCM Papers

Purpose: provide copy-ready LaTeX patterns for common CUMCM paper elements. These snippets should be adapted to the actual problem, data, and model. Do not paste them as decorative filler.

## Route Figure

Use in problem analysis or method overview.

```latex
\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.88\textwidth]{fig_route_overview}
  \caption{Overall modeling route. The workflow maps problem decomposition to data processing, model construction, solution, and validation.}
  \label{fig:route-overview}
\end{figure}
```

Text reference:

```latex
Figure~\ref{fig:route-overview} summarizes the modeling route used in this paper.
```

## Single Evidence Figure

Use for prediction curves, optimization convergence, residual plots, and data exploration.

```latex
\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.82\textwidth]{fig_prediction_curve}
  \caption{Prediction results of Model II on the test interval. The fitted curve follows the main trend, while the residual peaks indicate intervals where the model underestimates abrupt changes.}
  \label{fig:prediction-curve}
\end{figure}
```

Checklist:

- Generated from code.
- Listed in artifact ledger.
- Caption states what the reader should learn.

## Subfigure Comparison

Use for before/after, baseline/model, or scenario comparisons.

```latex
\begin{figure}[!htbp]
  \centering
  \begin{subfigure}{0.48\textwidth}
    \centering
    \includegraphics[width=\textwidth]{fig_baseline}
    \caption{Baseline scheme}
    \label{fig:baseline-scheme}
  \end{subfigure}
  \hfill
  \begin{subfigure}{0.48\textwidth}
    \centering
    \includegraphics[width=\textwidth]{fig_optimized}
    \caption{Optimized scheme}
    \label{fig:optimized-scheme}
  \end{subfigure}
  \caption{Comparison between the baseline and optimized schemes.}
  \label{fig:scheme-comparison}
\end{figure}
```

## Three-Line Parameter Table

```latex
\begin{table}[!htbp]
  \centering
  \caption{Main parameter settings of Model I}
  \label{tab:model1-parameters}
  \begin{tabular}{lll}
    \toprule
    Symbol & Meaning & Value \\
    \midrule
    $N$ & Number of samples & 1000 \\
    $\epsilon$ & Convergence tolerance & 0.01 \\
    $T_{\max}$ & Maximum iterations & 500 \\
    \bottomrule
  \end{tabular}
\end{table}
```

## Result Table

Use stable units and avoid excessive decimals.

```latex
\begin{table}[!htbp]
  \centering
  \caption{Comparison of candidate schemes}
  \label{tab:scheme-comparison}
  \begin{tabular}{lrrr}
    \toprule
    Scheme & Cost (yuan) & Error (\%) & Feasible \\
    \midrule
    Baseline & 12500 & 8.42 & Yes \\
    Model I & 11320 & 5.16 & Yes \\
    Model II & 10980 & 4.73 & Yes \\
    \bottomrule
  \end{tabular}
\end{table}
```

## Long Table

Use for appendix or long result lists.

```latex
\begin{longtable}{llrr}
  \caption{Detailed decision variables of the optimized scheme}
  \label{tab:decision-details}\\
  \toprule
  Index & Object & Quantity & Time \\
  \midrule
  \endfirsthead
  \toprule
  Index & Object & Quantity & Time \\
  \midrule
  \endhead
  1 & A & 12.5 & 08:00 \\
  2 & B & 10.0 & 09:00 \\
  \bottomrule
\end{longtable}
```

## Optimization Objective and Constraints

```latex
\begin{equation}
  \min Z = \sum_{i \in I}\sum_{j \in J} c_{ij}x_{ij}
  \label{eq:objective}
\end{equation}

\begin{align}
  \sum_{j \in J} x_{ij} &\leq s_i, && i \in I, \label{eq:supply-constraint}\\
  \sum_{i \in I} x_{ij} &\geq d_j, && j \in J, \label{eq:demand-constraint}\\
  x_{ij} &\geq 0, && i \in I,\ j \in J. \label{eq:nonnegative-constraint}
\end{align}
```

Text reference:

```latex
Equation~\eqref{eq:objective} minimizes the total cost. Constraints~\eqref{eq:supply-constraint}--\eqref{eq:nonnegative-constraint} describe supply capacity, demand satisfaction, and non-negativity.
```

## Prediction Error Metrics

```latex
\begin{align}
  \mathrm{MAE} &= \frac{1}{n}\sum_{t=1}^{n}\left|y_t-\hat{y}_t\right|, \label{eq:mae}\\
  \mathrm{RMSE} &= \sqrt{\frac{1}{n}\sum_{t=1}^{n}\left(y_t-\hat{y}_t\right)^2}. \label{eq:rmse}
\end{align}
```

## Classification Metrics Table

```latex
\begin{table}[!htbp]
  \centering
  \caption{Classification performance under different feature sets}
  \label{tab:classification-metrics}
  \begin{tabular}{lrrrr}
    \toprule
    Feature set & Accuracy & Precision & Recall & F1-score \\
    \midrule
    Raw features & 0.912 & 0.905 & 0.898 & 0.901 \\
    PCA features & 0.936 & 0.931 & 0.927 & 0.929 \\
    Selected features & 0.948 & 0.942 & 0.940 & 0.941 \\
    \bottomrule
  \end{tabular}
\end{table}
```

## Algorithm Steps

Use when the solution process is important but code is too long for the body.

```latex
\subsubsection{Solution algorithm}

The solution process is summarized as follows:

\begin{enumerate}
  \item Initialize the decision variables and parameter set.
  \item Compute the objective function value under the current solution.
  \item Update the solution according to the selected search or solver rule.
  \item Check feasibility against all constraints.
  \item Stop when the tolerance threshold or maximum iteration number is reached.
\end{enumerate}
```

## Sensitivity Analysis Table

```latex
\begin{table}[!htbp]
  \centering
  \caption{Sensitivity of the objective value to key parameters}
  \label{tab:sensitivity}
  \begin{tabular}{lrrr}
    \toprule
    Parameter change & Objective value & Relative change & Feasible \\
    \midrule
    $-10\%$ & 102.4 & -3.1\% & Yes \\
    Baseline & 105.7 & 0.0\% & Yes \\
    $+10\%$ & 109.8 & 3.9\% & Yes \\
    \bottomrule
  \end{tabular}
\end{table}
```

## Appendix Code Inventory

```latex
\section{Code and Reproducibility Notes}

The runnable source files are stored under the repository's \texttt{src/} directory. Table~\ref{tab:code-inventory} lists the main files used to reproduce the results.

\begin{table}[!htbp]
  \centering
  \caption{Code file inventory}
  \label{tab:code-inventory}
  \begin{tabular}{lll}
    \toprule
    File & Purpose & Output \\
    \midrule
    \texttt{src/data/clean.py} & Data cleaning & cleaned data files \\
    \texttt{src/models/model1.py} & Model I computation & result tables \\
    \texttt{src/figures/plot_results.py} & Figure generation & paper figures \\
    \bottomrule
  \end{tabular}
\end{table}
```

## Appendix Run Command

```latex
\subsection{Run command}

The main results can be reproduced by running:

\begin{verbatim}
python src/run_all.py
\end{verbatim}

Random seeds, data paths, and output paths are recorded in \texttt{runs/current/artifact-ledger.md}.
```

## Placeholder Policy

When a snippet is inserted before final data exist:

- keep placeholder labels obvious
- do not invent numerical values
- mark the artifact as `Pending` in the artifact ledger
- replace placeholders before writing the abstract
