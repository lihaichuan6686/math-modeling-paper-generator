# Monitoring-Route-E Calibration Example

Purpose: show how to fill a pressure-test calibration log after a monitoring-route E draft looks complete but still fails to close diagnostics into policy.

This is an illustrative calibration record, not a claim that this exact run has been executed.

## Header

- run name: `example-monitoring-route-e-pressure-test`
- date: `fill during real run`
- problem source: `fresh monitoring / policy-style E problem`
- route family: `monitoring-route E`
- nearest run-file example used: `docs/run-file-examples/monitoring-route-e-demo/`
- nearest deep-reading or comparison anchor used: `knowledge/cumcm/deep-reading-2023E176.md`

## Route Decision Audit

- modeled object: monitored system with diagnostic indicators and intervention consequences
- decision object: monitoring rule or policy scheme
- chosen family: monitoring-route E
- nearest rejected family: forecast-to-decision
- did the route fit? `partly`
- note: the diagnosis layer matched the family, but the first draft treated the detected pattern as the final answer instead of building a policy artifact.

## Evidence Audit

| Check | Status | Evidence | Notes |
| --- | --- | --- | --- |
| each major subquestion has a visible artifact | Warn | diagnostic plots exist, policy artifact missing | Q1 is over-evidenced; Q2 is under-evidenced |
| family-specific evidence burden is met | Fail | no monitoring/policy table | monitoring-route E requires a rule or policy artifact |
| validation is real rather than ceremonial | Warn | one long-horizon plot but no intervention comparison | consequence evidence exists but is not tied to policy |
| first strong figure has the right role for this family | Pass | process/diagnostic figure appears early | object and signal are legible |
| abstract numbers and main results match the artifact ledger | Unknown | ledger incomplete | cannot verify abstract until policy artifact is added |

## Writing Audit

- did the abstract close each major subquestion: no; it closes diagnosis but not policy
- did the conclusion stay within the claim boundary: partly; it avoids universal claims but still says the monitoring strategy is effective without a policy table
- which section felt too thin: policy design
- which bridge paragraph was missing or weak: diagnosis-to-policy paragraph
- did any section feel artifact-stacked: yes; diagnostic results
- did paragraph density match the family: no; diagnosis prose was heavy, policy prose was short

## Major Failures

- bucket: `decision_object_missing`
  evidence: no monitoring rule, sampling plan, or policy table appears in the body
  impact: the paper answers what was detected, but not what should be done

- bucket: `bridge_paragraph_missing`
  evidence: the diagnostic section ends at a pattern statement and jumps directly to conclusion language
  impact: the reader cannot see how the detected pattern becomes a rule

- bucket: `claim_overreach`
  evidence: conclusion says the strategy is effective without intervention or horizon comparison tied to a policy
  impact: recommendation outruns the evidence

## What Actually Worked

- strongest section: diagnostic analysis
- strongest artifact: diagnostic process figure
- strongest family-specific control that helped: claim-boundary matrix flagged that the final sentence must state a policy, not only a detected pattern

## Required Repo Write-Back

- file to update: `docs/run-file-examples/monitoring-route-e-demo/writing-style-plan.md`
  why: add a stronger reminder that diagnostic artifacts must each name a policy implication

- file to update: `docs/review-checklist.md`
  why: add a monitoring-route review cue if repeated real runs miss policy artifacts

## Next Decision

- keep current route family guidance unchanged / refine it / split it further: refine if the next run repeats the same missing policy artifact
- run another pressure test on the same family or move to a different family: same family once a policy-table repair is added
- recommended next target problem type: E-style monitoring problem with explicit intervention or sampling decision
