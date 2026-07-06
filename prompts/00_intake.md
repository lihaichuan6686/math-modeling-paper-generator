# Phase 0 Prompt: Intake

Read:

- `problems/problem.md`
- all attachments under `problems/`
- `knowledge/cumcm/paper-generation-playbook.md`
- `knowledge/algorithms/cumcm-routing-rules.md`
- relevant files under `knowledge/algorithms/cards/`

Create:

- `runs/current/problem-analysis.md`
- `runs/current/data-inventory.md`
- `runs/current/artifact-ledger.md` from `docs/artifact-ledger-template.md`

Do not start writing the paper in this phase.

## Required Analysis

Extract and record:

1. contest/year/problem identifier, if known
2. problem background in concise language
3. all subquestions
4. known inputs
5. required outputs
6. constraints
7. evaluation indicators
8. data files and fields
9. possible hidden traps
10. missing or uncertain information

## Routing Signals

Identify terms that suggest model routes:

- geometry or engineering mechanics
- statistics plus chemical/material optimization
- supply chain evaluation and planning
- online scheduling or industrial optimization
- machine learning classification
- time-series prediction plus decision
- evaluation and ranking
- simulation

Record candidate route signals, but do not choose the final model yet.

## Evidence Rules

- Mark unknown information as `Unknown`.
- Mark inferred information as `Inference`.
- Do not invent missing data.
- Do not fabricate references, experiments, or official facts.
- If the request appears to support active contest cheating, stop and redirect to compliant research/review use.

## Output Structure

`problem-analysis.md` should include:

```text
Problem summary
Subquestions
Inputs
Outputs
Constraints
Evaluation metrics
Routing signals
Risks and missing information
Questions for human confirmation
```

`data-inventory.md` should include:

```text
Data files
Field descriptions
Units
Missing values
Potential cleaning steps
Data risks
```
