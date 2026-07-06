# Phase 1 Prompt: Ideation

Read:

- `runs/current/problem-analysis.md`
- `runs/current/data-inventory.md`
- `knowledge/algorithms/cumcm-routing-rules.md`
- `knowledge/algorithms/cards/README.md`
- relevant files under `knowledge/algorithms/cards/`
- `knowledge/cumcm/paper-generation-playbook.md`
- recent CUMCM first-pass notes under `knowledge/cumcm/`

Create:

- `runs/current/model-candidates.md`

## Goal

Propose at least three candidate model chains. Each candidate must be a route, not a single algorithm name.
When a candidate route uses a method that has a detailed card, read that card and reflect its inputs, equations, validation, figures, and risks in the candidate.

## Candidate Format

For each candidate:

```text
Candidate name:
Problem type:
Model chain:
Mathematical basis:
Required data:
Expected equations:
Expected figures:
Expected tables:
Validation plan:
Page-structure impact:
Interpretability:
Implementation difficulty:
Main risks:
```

## Required Comparison

Compare candidates by:

- fit to each subquestion
- data support
- mathematical credibility
- interpretability
- reproducibility
- figure/table potential
- validation strength
- LaTeX presentation difficulty
- risk of overclaiming

## Selection Rule

Choose the route with the best balance of:

```text
problem fit + data support + interpretability + validation + reproducibility
```

Avoid choosing a complex model only because it appears advanced.

## Required Final Section

End `model-candidates.md` with:

```text
Recommended route:
Why selected:
Rejected alternatives:
Expected section structure:
Expected figure/table set:
Main open risks:
```
