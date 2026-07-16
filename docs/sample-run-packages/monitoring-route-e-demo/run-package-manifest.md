# Monitoring-Route-E Run Package Manifest

Purpose: show what a near-real v1.2 run package should contain for a monitoring-route E paper before it is pressure-tested.

This manifest is a packaging checklist, not a review checklist.

## Minimum Package Contents

### Run Workspace

| Path | Role |
|---|---|
| `runs/<name>/problem-profile.md` | monitored system and policy decision object |
| `runs/<name>/problem-analysis.md` | diagnosis, trigger, and policy burden |
| `runs/<name>/route-decision.md` | diagnosis -> policy -> consequence route choice |
| `runs/<name>/model-plan.md` | diagnostic model plus monitoring/policy rule |
| `runs/<name>/verification-plan.md` | intervention or long-horizon evidence plan |
| `runs/<name>/figure-plan.md` | process, diagnostic, policy, and consequence visuals |
| `runs/<name>/section-budget.md` | page rhythm and artifact allocation |
| `runs/<name>/writing-style-plan.md` | policy-aware paragraph rhythm |
| `runs/<name>/artifact-ledger.md` | claim-to-artifact traceability |
| `runs/<name>/calibration-log.md` | pressure-test result when available |

### Generated Outputs

| Path family | Role |
|---|---|
| diagnostic artifact | monitored-pattern evidence |
| policy or monitoring table | decision artifact |
| trigger/rule parameter table | traceability from diagnosis to policy |
| consequence comparison artifact | intervention or long-horizon evidence |
| recommendation summary table | bounded policy close |
| `paper/tables/` | diagnostic, policy, and consequence tables |
| `paper/figures/` | process, diagnostic, and consequence visuals |
| `src/` entry points | reproducible generation path |

### Review Layer

| Path | Role |
|---|---|
| `reviews/review-<name>.md` | quality review with findings and required repairs |
| `reviews/calibration-<name>.md` | pressure-test log and write-back decision |

## Minimum Artifact Story

A run package is not yet worth testing unless it can tell this whole story:

```text
diagnostic pattern
-> trigger or rule construction
-> monitoring/policy artifact
-> intervention or horizon consequence
-> scoped policy recommendation
```

## Ready-For-Test Signals

Treat the package as ready for pressure testing only if:

1. diagnostics feed an explicit rule or policy;
2. the policy has a traceable trigger;
3. consequence evidence exists;
4. the conclusion can end on a policy rather than a detected pattern;
5. the calibration log can distinguish diagnostic evidence from decision evidence.
