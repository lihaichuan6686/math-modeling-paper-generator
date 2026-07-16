# Problem Analysis

Run: example-monitoring-route-e

## Problem Summary

The task is not only to detect patterns, but to use those patterns to design a monitoring or intervention scheme. Therefore the paper must separate the diagnosis layer from the policy layer and then show the consequence of following the proposed rule.

## Subquestions

1. Diagnose the monitored behavior and identify the main abnormality, periodicity, or risk pattern.
2. Design a monitoring rule, sampling scheme, or intervention policy from that diagnosis.
3. Evaluate intervention effect or long-horizon consequence and state the final recommendation.

## Inputs

- monitored time-series or process indicators;
- possible diagnostic thresholds or structural features;
- intervention or policy constraints;
- scenario settings for long-horizon comparison.

## Outputs

- diagnostic evidence;
- policy or monitoring artifact;
- intervention-effect or long-horizon comparison;
- final recommendation with scope and caveat.

## Constraints

- diagnostic indicators must be stable and interpretable;
- the policy rule must be linked to observable signals;
- intervention comparisons must use consistent metrics;
- final claims must stay within the studied horizon and scenario range.

## Evaluation Metrics

- diagnostic quality or signal strength indicators;
- monitoring/policy trigger parameters;
- intervention-effect or long-horizon consequence metrics;
- comparison of candidate policies when relevant.

## Routing Signals

- diagnosis is necessary but not sufficient;
- the paper needs a visible rule or policy artifact;
- the recommendation must be justified by consequence evidence, not only by the elegance of diagnostics.

## Selected Route

Primary route:

```text
diagnosis -> forecast or consequence reading -> monitoring/policy design -> intervention comparison -> recommendation
```

Rejected route:

- diagnostics only: too weak because no policy is produced;
- policy-only route: too weak because the trigger burden is hidden;
- narrative recommendation only: too weak because consequence evidence is missing.

## Artifact Intent

- analysis section: task decomposition table and route figure;
- model section: diagnostic logic plus monitoring/policy rule;
- result section: diagnostic artifact, policy artifact, consequence artifact;
- validation section: intervention comparison or long-horizon audit.

## Risks and Missing Information

- one diagnostic pattern may not remain stable under different horizons;
- policy triggers may be sensitive to threshold choice;
- intervention effects may depend on assumptions outside the observed data range.

## Questions for Human Confirmation

- When tradeoffs appear, should the final recommendation prioritize early detection, lower intervention cost, or lower false alarms?
- Is the expected output closer to a monitoring rule, a sampling scheme, or a broader management policy?
