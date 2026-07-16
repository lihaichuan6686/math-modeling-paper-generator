# Problem Profile

Run: example-forecast-to-decision

## Problem Image

This is a future-driven decision problem. The paper cannot stop at fitting a trend curve, because the forecast must feed a later planning or policy choice under uncertainty.

## Task Family And Route Signals

- primary family: forecast to decision
- support family: scenario robustness
- route signals: historical time series, uncertainty burden, explicit future recommendation required, forecast and decision must stay connected

## Modeled Object

The modeled object is a time-evolving demand or load system whose historical pattern drives a later allocation, capacity, or policy choice.

## Decision Object

The final decision object is a future-facing plan, threshold, or capacity recommendation conditioned on the predicted trajectory, not only a forecast curve.

## Question Map

- Q1: identify the key trend pattern and build the forecasting route
- Q2: convert the forecast output into an executable decision model
- Q3: test how uncertainty changes the recommendation

## Evidence Burden

- a forecast figure alone is insufficient
- the paper needs a decision artifact tied to the forecast
- backtest or residual evidence is required
- scenario propagation is needed to keep the recommendation credible

## Visual Burden

- one early figure explaining the forecast-to-decision chain
- one trend or decomposition artifact
- one forecast output artifact
- one decision artifact
- one scenario or uncertainty artifact

## Thinness Risks

- Q1 may become too long if exploratory trend narration is not controlled
- Q2 may collapse into one short table if the forecast-to-decision bridge is weak
- Q3 may become symbolic if uncertainty is not quantified

## Fake-Completion Risks

- ending at forecasting
- treating the forecast as certain
- giving a decision table without showing how forecast error changes it
