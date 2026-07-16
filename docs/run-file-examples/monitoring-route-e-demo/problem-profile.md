# Problem Profile

Run: example-monitoring-route-e

## Problem Image

This is a diagnosis-to-policy problem. The paper may begin with signal reading, abruptness detection, periodicity analysis, or risk diagnosis, but it cannot stop there. The detected pattern must close into a monitoring rule, sampling plan, or intervention policy.

## Task Family And Route Signals

- primary family: monitoring-route E
- support family: intervention comparison
- route signals: monitoring indicators, abnormality or periodicity, future or long-horizon effect, explicit policy or sampling recommendation required

## Modeled Object

The modeled object is a monitored system with diagnostic indicators, temporal behavior, and intervention consequences.

## Decision Object

The final decision object is a monitoring rule, policy scheme, or intervention strategy under the studied horizon, not only a diagnostic conclusion.

## Question Map

- Q1: diagnose the monitored pattern and identify the important behavioral signal
- Q2: convert the diagnosis into a monitoring or policy scheme
- Q3: compare intervention effects or long-horizon consequences and state the recommendation

## Evidence Burden

- stacked diagnostic plots alone are insufficient
- the paper needs a monitoring or policy artifact
- intervention, trigger, or long-horizon consequence evidence is required
- the final recommendation must be tied back to detected behavior

## Visual Burden

- one early process figure showing `diagnosis -> policy -> consequence`
- one diagnostic artifact
- one monitoring/policy artifact
- one intervention-effect or long-horizon artifact

## Thinness Risks

- Q1 may become too dominant if the diagnosis block is not controlled
- Q2 may collapse into one short rule list if the bridge from diagnosis is weak
- Q3 may become generic if long-horizon effects are not quantified

## Fake-Completion Risks

- stopping at descriptive diagnostics
- recommending a policy without a traceable trigger
- claiming broad management value from one local diagnostic pattern
