# Problem Understanding Framework

Purpose: give the generator a reusable way to understand a CUMCM-style problem before selecting models.

This note exists because many weak drafts fail before modeling begins. They read the question as a list of subquestions, but not as a structured modeling task with a review burden.

## Core Idea

Do not start from:

```text
Which algorithm should I use?
```

Start from:

```text
What kind of object is this?
What kind of decision must the paper produce?
What evidence will make that decision credible?
```

## Problem Profile Fields

Every run should first produce a `problem profile` with these fields:

```text
Contest and identifier:
Task family:
Modeled object:
Decision object:
Observed data:
Main constraints:
Evaluation target:
Evidence burden:
Visual burden:
Human-review risk:
```

## Task Family Guide

Typical families:

- mechanism / physical process
- evaluation / ranking
- prediction / forecasting
- optimization / planning
- classification / diagnosis
- simulation / stress testing
- geometry / measurement
- scheduling / transport / timetable
- monitoring / intervention / policy

Many strong papers combine two families.
Record the primary family and the support family instead of flattening them into one vague label.

Local beginner-training material often introduces mathematical modeling through three broad families:

- prediction;
- optimization;
- evaluation.

Use these as first-pass orientation only. A strong v1.4 run must immediately expand the family into answer form and evidence burden:

| Broad family | Typical answer form | Evidence burden |
|---|---|---|
| prediction | future value, trend, interval, warning, or downstream input | baseline comparison, error metric, residual or robustness check, explanation of downstream use |
| optimization | plan, allocation, route, schedule, parameter choice, or policy | objective/constraint clarity, feasibility check, scenario comparison, sensitivity to key parameters |
| evaluation | score, grade, ranking, classification, priority list, or recommendation | indicator source, direction and normalization, weight logic, ranking sensitivity, decision closure |

Do not stop at the broad label. For example, "evaluation" is not a paper route until it states what will be evaluated, how the score becomes a decision, and how ranking stability will be checked.

## Modeled Object

Name the real object early.

Examples:

- supplier system
- passenger-flow network
- production process
- chromosome-screening workflow
- river section
- heat-transfer device
- road segment system

If the paper cannot name its object clearly, it often delays all explanatory figures and becomes method-first in a weak way.

## Decision Object

Record the final actionable output, not just the intermediate quantity.

Examples:

- best supplier set
- recommended inspection schedule
- timetable and service pattern
- earliest reliable test time
- anomaly judgment rule
- monitoring policy

If the draft only produces:

- scores,
- clusters,
- forecasts,
- fitted curves,

without connecting them to a decision object, the paper is not yet closed.

## Evidence Burden

Different families need different evidence.

Examples:

- evaluation papers need weight sensitivity or ranking comparison;
- forecasting papers need error checks and downstream impact;
- planning papers need feasibility and scenario stress;
- classification papers need split policy, confusion evidence, and threshold logic;
- mechanism papers need fit residuals and parameter interpretation.

Record the evidence burden before implementation.

Use the broad-family evidence map as a quick intake test:

- If the route is prediction, ask what baseline forecast and error table will appear.
- If the route is optimization, ask what feasibility and scenario table will appear.
- If the route is evaluation, ask what indicator table and sensitivity table will appear.
- If the route is simulation, ask what scenario design and comparison figure will appear.
- If the route is classification or diagnosis, ask what split, threshold, confusion, or error artifact will appear.

## Visual Burden

Good papers know early which visuals must appear.

At minimum ask:

1. What figure identifies the modeled object?
2. What figure proves the main pattern?
3. What figure or table shows the final decision?
4. What figure or table shows robustness?

If these are unknown during intake, the route is still underdefined.

## Hidden-Trap Questions

Before route selection, ask:

1. Is the problem asking for a decision, but tempting us to stop at diagnosis?
2. Is the problem asking for optimization, but tempting us to reuse a sample partition without proving it?
3. Is the problem asking for credibility, but tempting us to skip validation?
4. Is the problem asking for a system, but tempting us to analyze isolated variables only?
5. Is the problem asking for a long paper, but tempting us to grow by filler instead of loops?

## Problem-Profile Output Pattern

Recommended shape for `runs/current/problem-profile.md`:

```text
Problem image
Task family and route signals
Modeled object
Decision object
Question map
Evidence burden
Visual burden
Thinness risks
Fake-completion risks
```

This file should be short, but it should make the later route decision easier and more consistent.
