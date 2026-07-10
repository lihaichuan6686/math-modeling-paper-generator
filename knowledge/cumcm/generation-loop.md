# CUMCM Generation Loop

Purpose: connect route selection, model building, section writing, visual evidence, and iteration decisions into one executable chain.

This is the bridge between knowledge and action.

## Main Loop

Use this order when generating a paper draft:

```text
problem statement
-> route index
-> problem archetype
-> route example matrix
-> model chain pattern
-> section map
-> figure/table plan
-> artifact ledger
-> LaTeX draft
-> PDF check
-> review
-> iteration decision
```

## What Each Step Must Produce

| Step | Required output | Why it matters |
|---|---|---|
| Route index | route family and evidence pattern | prevents premature method choice |
| Problem archetype | paper shape and required artifacts | keeps the paper structurally complete |
| Model chain pattern | method sequence with validation | prevents method lists without closure |
| Section map | write order and section outputs | keeps writing aligned with evidence |
| Figure/table plan | stable artifact list | prevents late-stage layout surprises |
| Artifact ledger | traceability for claims and outputs | connects paper text to source evidence |
| LaTeX draft | sectioned paper source | turns the plan into a paper |
| PDF check | rendered layout evidence | catches overflow, residue, and missing artifacts |
| Review | quality and risk assessment | makes weaknesses explicit |
| Iteration decision | revise route, tighten gate, or expand atlas | turns one run into a reusable improvement |

## Route To Section Rule

Do not write LaTeX from route notes alone. Route notes decide the backbone; the section map decides the order of exposition.

```text
route family -> archetype -> route example matrix -> section order -> artifact plan -> writing
```

## Artifact Closure Rule

Every important claim in the paper should map to one of:

- data file;
- equation;
- code output;
- generated table;
- generated figure;
- validation artifact;
- review note.

If a claim cannot point to one of these, it is not ready for the body.

## Iteration Rule

After a run, choose only one primary next action:

1. keep the route rule unchanged;
2. tighten a review gate;
3. expand the atlas with a new route anchor;
4. improve the section map or LaTeX contract;
5. add a comparison note for a recurring paper family.

Avoid changing everything at once. Each iteration should make one part of the loop more reliable.

## Best Use

Read this note together with:

- `route-index.md`
- `problem-type-paper-archetypes.md`
- `route-example-matrix.md`
- `model-chain-patterns.md`
- `latex/section-map.md`
- `../docs/v1-runbook.md`
- `../knowledge/learning-status.md`
