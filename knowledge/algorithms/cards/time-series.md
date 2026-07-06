# Time-Series Forecasting Card

Purpose: support prediction and trend analysis for ordered observations such as demand, price, traffic, production, weather, and monitoring signals.

## Use When

- Data are ordered by time and future values are needed.
- Seasonality, trend, cycles, or shocks may matter.
- Forecasts feed planning, inventory, pricing, or warning decisions.
- The paper can compare at least two forecasting baselines.

## Avoid When

- Observations are not equally spaced and no correction is planned.
- The series is too short for the proposed model.
- Future values are driven by known exogenous decisions that are ignored.
- The forecast is used as a deterministic fact without uncertainty.

## Required Inputs

- Time index and response series.
- Missing-value and outlier treatment.
- Train/test split that respects time order.
- Candidate models: naive, moving average, exponential smoothing, ARIMA/SARIMA, regression with lag features.
- Error metrics such as MAE, RMSE, MAPE, or sMAPE.

## Mathematical Objects

Exponential smoothing:

```text
S_t = alpha y_t + (1 - alpha) S_{t-1}
```

ARIMA form:

```text
phi(B)(1 - B)^d y_t = theta(B) epsilon_t
```

Lag-regression form:

```text
y_t = f(y_{t-1}, ..., y_{t-p}, x_t)
```

## Outputs

- Forecast values and confidence or prediction intervals.
- Error metric table.
- Residual diagnostics.
- Scenario forecast table when future assumptions vary.
- Downstream planning input table.

## Figure and Table Expectations

- Time-series plot with train/test split.
- Forecast-vs-actual plot.
- Residual or autocorrelation plot.
- Model comparison table.
- Planning impact chart if forecasts feed optimization.

## Validation

- Preserve time order in validation.
- Compare against naive or seasonal naive baseline.
- Check residual autocorrelation.
- Test sensitivity to forecast horizon.
- Report uncertainty, not only point estimates.

## CUMCM Writing Pattern

1. Describe temporal structure and forecasting target.
2. Clean and split data by time.
3. Compare simple and stronger models.
4. Use error metrics and residual checks.
5. Pass forecasts into the next decision model with uncertainty notes.

## Common Risks

- Random train/test split leaks future information.
- MAPE is used when actual values are near zero.
- A complicated model is used on a tiny series.
- Forecast intervals are omitted.
- The forecast is not connected to later decisions.

## Review Checks

- Is time order respected?
- Is there a baseline?
- Are errors measured on future-held-out data?
- Are trend/seasonality claims supported?
- Is uncertainty propagated into decisions?
