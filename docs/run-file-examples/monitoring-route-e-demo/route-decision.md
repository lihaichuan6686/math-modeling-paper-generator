# Route Decision

Run: example-monitoring-route-e

## Selected Route Family

Monitoring-route E.

## Question Map

- Q1 builds the diagnosis layer
- Q2 converts diagnosis into a monitoring or policy rule
- Q3 compares consequences and forms the final recommendation

## Route Chain By Subquestion

### Q1

signal reading -> pattern diagnosis -> key indicator or trigger candidate

### Q2

diagnostic signal -> monitoring/policy rule -> scheme artifact

### Q3

intervention or long-horizon comparison -> consequence summary -> recommendation

## Why This Route Fits The Decision Object

The decision object is a monitoring or policy scheme, not only an explanation of the past signal. Therefore the route must close diagnostics into an explicit rule and then show what following that rule changes.

## Why Rejected Routes Are Weaker

- diagnostic-only route: fails to answer the policy task
- policy-without-diagnostics route: hides why the trigger is credible
- purely descriptive long-horizon route: does not produce a usable scheme

## Required Evidence Chain

- diagnostic artifact
- monitoring/policy artifact
- trigger or rule parameter explanation
- intervention or long-horizon comparison artifact
- recommendation summary

## Required Visuals

- route figure showing diagnosis feeding policy
- diagnostic figure
- policy or monitoring table
- consequence comparison artifact

## Expected Failure Modes

- diagnostics do not produce a traceable trigger
- policy language outruns the actual comparison evidence
- long-horizon effect is asserted without visible artifact support
