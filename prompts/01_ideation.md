# Phase 1 Prompt: Ideation

Read:

- `runs/current/problem-analysis.md`
- `runs/current/data-inventory.md`
- `knowledge/algorithms/cumcm-routing-rules.md`
- `knowledge/algorithms/cards/README.md`
- `knowledge/algorithms/model-chain-patterns.md`
- relevant files under `knowledge/algorithms/cards/`
- `knowledge/cumcm/paper-generation-playbook.md`
- `knowledge/cumcm/official-style-vs-modern-draft-risk.md`
- recent CUMCM first-pass notes under `knowledge/cumcm/`

Create:

- `runs/current/model-candidates.md`

## Goal

Propose at least three candidate model chains. Each candidate must be a route, not a single algorithm name.
When a candidate route uses a method that has a detailed card, read that card and reflect its inputs, equations, validation, figures, and risks in the candidate.

If the problem looks like an E-type forecast-driven paper, at least one candidate must be framed as `production-route E` and at least one candidate must be framed as `monitoring-route E` unless the task evidence clearly rules one family out.

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

For E-type problems, explicitly decide:

```text
Selected E-route family:
- production-route E
or
- monitoring-route E
Reason:
```

Do not leave the route at a generic `forecast to decision` label.

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

## Mandatory Candidate Checks

Before recommending a route, explicitly record:

```text
Question map:
Object-first figure:
Decision closure:
Effective body-length risk:
Fake-completion risks to avoid:
```

Rules:

- `Question map` means the subquestion numbering and role assignment that must stay stable from abstract to conclusion.
- `Object-first figure` means the earliest explanatory figure that identifies the modeled object, such as network, geometry, process, or system.
- `Decision closure` means the concrete decision artifact the route will produce, not only an intermediate forecast or diagnosis.
- `Effective body-length risk` means where the route may become too short because evidence is missing, or look long only because of appendix/code inflation.
- `Fake-completion risks to avoid` should borrow from the recent 2024 risk notes: placeholders, residue, unstable numbering, unsupported claims, or method stacking.
