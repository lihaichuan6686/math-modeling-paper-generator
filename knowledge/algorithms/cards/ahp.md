# Analytic Hierarchy Process

Use when expert preference, policy priority, or qualitative hierarchy matters. AHP is most useful when the paper must justify subjective weights and then test whether conclusions are stable.

## Good Fit

- evaluation indicator systems with clear hierarchy;
- expert or policy preference is meaningful;
- qualitative criteria such as safety, reliability, or convenience matter;
- the paper needs explainable subjective weights.

## Poor Fit

- no defensible expert basis exists;
- too many indicators make pairwise comparison unreliable;
- data dispersion should dominate weighting;
- consistency ratio fails and is not repaired.

## Required Inputs

- goal layer;
- criterion and subcriterion layers;
- pairwise comparison matrices;
- consistency threshold, usually $CR<0.1$.

## Procedure

1. Build a hierarchy:

```text
goal -> criteria -> subcriteria -> alternatives
```

2. Fill pairwise comparison matrix $A=(a_{ij})$, where $a_{ij}$ represents the importance of criterion $i$ over criterion $j$.
3. Estimate the weight vector $w$ from the principal eigenvector:

\begin{equation}
Aw=\lambda_{\max}w.
\end{equation}

4. Compute consistency index:

\begin{equation}
CI = \frac{\lambda_{\max}-n}{n-1}.
\end{equation}

5. Compute consistency ratio:

\begin{equation}
CR = \frac{CI}{RI}.
\end{equation}

6. Accept the matrix if $CR<0.1$; otherwise revise comparisons.

## Expected Paper Artifacts

- hierarchy diagram or hierarchy table;
- pairwise comparison matrix;
- weight table;
- consistency-ratio table;
- combined weight table when multiple layers exist;
- weight sensitivity plot if the final ranking matters.

## Validation

- Report $CI$ and $CR$.
- Check whether final conclusions change under moderate weight perturbation.
- Compare with entropy weights when objective indicator data are available.
- Explain expert source or preference rationale.

## Common Writing Pattern

```text
Because the relative importance of criteria cannot be determined purely from data, we use AHP to encode expert preference. The consistency ratio is checked before the weights are used in the comprehensive evaluation model.
```

## Common Failure

- Claiming AHP is objective.
- Omitting the consistency test.
- Using too many indicators in one matrix.
- Hiding the pairwise comparison matrix.
- Feeding subjective weights into a model without sensitivity analysis.
