# Verification Plan

Run: example-forecast-to-decision

## Main Checks

1. verify that forecast errors are reported with explicit metrics;
2. verify that the decision artifact uses forecast-derived parameters rather than fixed placeholders;
3. verify that at least one uncertainty scenario changes or tests the recommendation;
4. verify that abstract numbers match the final result artifacts.

## Required Artifacts

- forecast table or forecast plot
- backtest/residual artifact
- executable decision table
- scenario comparison table

## Review Warnings

- fail if the paper reports a forecast but no downstream decision artifact
- fail if the recommendation is written as certain despite visible error
- warn if validation covers forecast fit but not decision sensitivity
