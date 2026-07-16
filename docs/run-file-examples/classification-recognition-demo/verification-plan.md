# Verification Plan

Run: example-classification-recognition

## Main Checks

1. verify that preprocessing steps and split policy are explicit enough to judge leakage risk;
2. verify that classifier choice uses more than one global metric;
3. verify that class-level errors are interpreted, not only displayed;
4. verify that abstract and conclusion stay within the tested dataset scope.

## Required Artifacts

- preprocessing or feature artifact
- classifier comparison artifact
- confusion or error artifact
- recognition summary artifact

## Review Warnings

- fail if the paper reports only one headline score
- fail if the chosen classifier is not justified against alternatives
- warn if the conclusion sounds deployable beyond the tested sample scope
