# TOPSIS

Use TOPSIS when alternatives should be ranked by closeness to an ideal solution and distance from a negative ideal solution. It is common in CUMCM evaluation tasks and often follows entropy weight or AHP.

## Good Fit

- alternatives must be ranked;
- indicators are numeric and comparable after normalization;
- both positive and negative ideal references are meaningful;
- the ranking may feed a planning model.

## Poor Fit

- indicators are mostly qualitative and cannot be scored reliably;
- indicator direction is ambiguous;
- alternatives are not comparable;
- final task requires an executable plan but the paper stops at ranking.

## Required Inputs

- normalized decision matrix $X=(x_{ij})$;
- weight vector $w_j$;
- benefit/cost direction already handled;
- alternatives and indicator names.

## Procedure

1. Standardize indicators and unify direction.
2. Apply weights:

\begin{equation}
v_{ij}=w_jx_{ij}.
\end{equation}

3. Define positive and negative ideal points:

\begin{equation}
v_j^+ = \max_i v_{ij},\quad v_j^- = \min_i v_{ij}.
\end{equation}

4. Compute distances:

\begin{equation}
D_i^+ = \sqrt{\sum_j(v_{ij}-v_j^+)^2},\quad D_i^- = \sqrt{\sum_j(v_{ij}-v_j^-)^2}.
\end{equation}

5. Compute closeness:

\begin{equation}
C_i = \frac{D_i^-}{D_i^+ + D_i^-}.
\end{equation}

6. Rank alternatives by descending $C_i$.

## Expected Paper Artifacts

- indicator direction table;
- normalized weighted matrix or compact summary;
- positive/negative ideal table;
- distance and closeness table;
- ranking table;
- ranking bar chart;
- sensitivity comparison under alternate weights.

## Validation

- Check all indicators have the intended direction.
- Compare TOPSIS ranking with one baseline ranking method.
- Test rank stability under weight perturbation.
- If ranking feeds planning, verify selected alternatives satisfy later constraints.

## Common Writing Pattern

```text
After obtaining indicator weights, TOPSIS is used to evaluate each alternative by its distance from the positive and negative ideal solutions. The closeness coefficient gives a comprehensive score and ranking.
```

## Common Failure

- Using raw indicators without standardization.
- Mixing benefit and cost indicators incorrectly.
- Reporting ranking without distances or closeness coefficients.
- Treating TOPSIS as a final plan when the problem asks for quantities, routes, schedules, or allocations.
