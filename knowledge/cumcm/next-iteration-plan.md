# Next Iteration Plan

Purpose: define the next concrete experiments for the CUMCM paper generator after the atlas and risk layers are in place.

## Current Baseline

Already in place:

- route atlas: `knowledge/cumcm/cumcm-atlas.md`
- official-versus-risk synthesis: `knowledge/cumcm/official-style-vs-modern-draft-risk.md`
- recent risk notes: `2024B`, `2024C`, `2024D`, `2024E`
- official anchors: `2022E014`, `2022E029`, `2023E176`
- same-problem comparisons: `2021C`, `2021D`
- route and review gates: prompts, blueprint, rubric, checklist

## Next Experiments

### Experiment 1: Fresh Real Problem Run

Goal:

- test whether the strengthened prompts and review gates catch fake completion before a draft is considered complete.

Inputs:

- one fresh contest problem statement;
- attachments and data files;
- atlas route selection.

Expected outputs:

- `runs/current/problem-analysis.md`
- `runs/current/data-inventory.md`
- `runs/current/model-candidates.md`
- `runs/current/model-plan.md`
- `runs/current/verification-plan.md`
- `runs/current/figure-plan.md`
- `runs/current/artifact-ledger.md`

Success criteria:

- question map stays stable;
- the object is introduced before the algorithms;
- each method produces a visible artifact;
- review gates can identify any screenshot-only or residue-only evidence.

### Experiment 2: Same-Problem Comparison Expansion

Goal:

- add one more same-problem comparison set to sharpen the difference between route backbone and writing voice.

Preferred targets:

- one supply-chain family;
- one forecasting-to-decision family;
- one geometry/engineering family.

Expected outputs:

- one new `knowledge/cumcm/*.md` comparison note;
- one route update in the atlas if the comparison changes a gate;
- one prompt or rubric refinement if a recurring gap appears.

Success criteria:

- the comparison explains why papers sound different while keeping the same route;
- the note yields at least one reusable gate or figure/table requirement.

### Experiment 3: LaTeX Weak-Spot Drill

Goal:

- catch recurring layout or structure weaknesses before they reach PDF rendering.

Focus areas:

- abstract numbering;
- figure/table caption discipline;
- appendix traceability;
- effective body length versus filler;
- route-specific section roles.

Expected outputs:

- one revised LaTeX guideline or snippet;
- one additional checklist item if a weakness repeats;
- one example section contract if needed.

Success criteria:

- the paper blueprint explains how pages emerge from evidence;
- the review checklist can reject screenshot-heavy or residue-heavy drafts.

## Decision Rule

After each experiment, decide one of three actions:

1. keep the route rule unchanged;
2. tighten a review gate;
3. expand the atlas with a new route anchor.

## Status

This plan is intentionally short and operational. It is meant to be updated after each new run, not to become a static manifesto.
