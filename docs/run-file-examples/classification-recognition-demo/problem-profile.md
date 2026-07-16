# Problem Profile

Run: example-classification-recognition

## Problem Image

This is a recognition and judgment problem driven by preprocessing, feature construction, and class-level evaluation. The paper cannot stop at one headline metric, because the real decision value depends on how errors are distributed across classes.

## Task Family And Route Signals

- primary family: classification / recognition
- support family: error interpretation
- route signals: labeled samples, preprocessing burden, feature extraction or selection, classifier comparison, class-level conclusion required

## Modeled Object

The modeled object is a labeled sample system with measurable features, possible class imbalance, and recognition uncertainty.

## Decision Object

The final decision object is a usable classification or diagnostic rule under the reported error tradeoff, not only the best overall score.

## Question Map

- Q1: preprocess the samples and construct the usable feature representation
- Q2: compare candidate classifiers and choose the recognition route
- Q3: interpret class-level errors and state the defensible recognition conclusion

## Evidence Burden

- one accuracy number is insufficient
- the paper needs explicit preprocessing evidence
- classifier comparison evidence is required
- confusion-level or class-level error evidence is required

## Visual Burden

- one early workflow figure for `preprocessing -> features -> classifier -> evaluation`
- one preprocessing or feature artifact
- one classifier comparison artifact
- one confusion or class-level error artifact

## Thinness Risks

- Q1 may shrink into a pipeline list if preprocessing is not interpreted
- Q2 may collapse into one comparison table without route explanation
- Q3 may become a token caveat if error cases are not planned early

## Fake-Completion Risks

- reporting only one headline metric
- choosing a classifier without explaining the class-level tradeoff
- claiming general deployment from one benchmark split
