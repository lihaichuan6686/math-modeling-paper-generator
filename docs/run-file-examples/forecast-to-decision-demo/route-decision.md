# Route Decision

Run: example-forecast-to-decision

## Selected Route Family

Forecast to decision.

## Question Map

- Q1 diagnoses the historical pattern and builds the forecast layer
- Q2 turns the forecast output into a downstream decision
- Q3 measures how forecast uncertainty changes the recommendation

## Route Chain By Subquestion

### Q1

exploratory diagnosis -> candidate forecast routes -> comparison -> chosen forecast

### Q2

forecast output -> decision parameters -> constrained decision model -> executable recommendation

### Q3

error band or scenario set -> recomputed decisions -> comparison summary

## Why This Route Fits The Decision Object

The final object is a future-facing recommendation. Therefore the forecast is only a middle layer. The route must continue into the decision model and then into an uncertainty layer that keeps the recommendation honest.

## Why Rejected Routes Are Weaker

- descriptive trend route: does not produce a real decision
- deterministic forecast route: hides uncertainty and overstates confidence
- decision-first route: makes the future input burden opaque

## Required Evidence Chain

- trend diagnosis artifact
- forecast artifact
- forecast error artifact
- downstream decision artifact
- scenario comparison artifact

## Required Visuals

- route figure showing forecast feeding the decision model
- trend or decomposition figure
- forecast table/plot
- decision table
- uncertainty comparison figure or table

## Expected Failure Modes

- overfitting the forecast layer
- giving a decision that is too sensitive to small forecast shifts
- collapsing uncertainty into one vague sentence
