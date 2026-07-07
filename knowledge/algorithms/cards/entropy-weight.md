# Entropy Weight Method

Use when indicators are available for multiple alternatives and the paper needs objective weights derived from data dispersion. In CUMCM papers it is often paired with TOPSIS, grey relational analysis, or a downstream planning model.

## Good Fit

- supplier, carrier, city, material, policy, or scheme evaluation;
- many indicators with different units;
- the user wants to reduce arbitrary subjective weights;
- indicator variation should affect importance.

## Poor Fit

- too few alternatives for dispersion to be meaningful;
- indicators are nearly constant;
- expert preference is central and cannot be ignored;
- indicator direction is unclear.

## Required Inputs

- alternatives $i=1,\ldots,n$;
- indicators $j=1,\ldots,m$;
- benefit/cost direction for each indicator;
- nonnegative normalized matrix.

## Procedure

1. Normalize each indicator and convert cost indicators so larger is better.
2. Convert the normalized value to a proportion:

\begin{equation}
p_{ij} = \frac{x_{ij}}{\sum_{i=1}^{n}x_{ij}}.
\end{equation}

3. Compute entropy:

\begin{equation}
e_j = -\frac{1}{\ln n}\sum_{i=1}^{n}p_{ij}\ln p_{ij}.
\end{equation}

4. Compute information utility:

\begin{equation}
d_j = 1-e_j.
\end{equation}

5. Compute weight:

\begin{equation}
w_j = \frac{d_j}{\sum_{j=1}^{m}d_j}.
\end{equation}

## Expected Paper Artifacts

- indicator direction table;
- normalized indicator table;
- entropy and utility table;
- final weight table;
- weight bar chart;
- sensitivity note for indicators with extreme weights.

## Validation

- Check that all weights sum to 1.
- Check for indicators with near-zero variance.
- Compare with equal weights or AHP weights when conclusions are important.
- Explain whether high weight is caused by genuine information or noisy outliers.

## Common Writing Pattern

```text
Because indicators have different dimensions and subjective preference is not fixed, we first standardize the indicators and use entropy weight to determine objective weights. Indicators with larger dispersion provide more discriminating information and therefore receive larger weights.
```

## Common Failure

- Forgetting benefit/cost direction before normalization.
- Taking $\ln 0$ without a zero-handling convention.
- Treating entropy weights as universally objective even when the data are noisy.
- Producing weights but never connecting them to ranking or planning.
