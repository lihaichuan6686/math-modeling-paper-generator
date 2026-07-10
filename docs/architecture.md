# Architecture

Purpose: show how the repository is organized as one closed-loop paper-generation system.

## Core Loop

```text
problem statement
-> intake
-> route selection
-> model plan
-> code and figures
-> LaTeX draft
-> PDF build
-> review
-> revision
```

## Main Layers

| Layer | Role | Main entry |
|---|---|---|
| `knowledge/` | absorb contest knowledge and structure rules | `knowledge/README.md` |
| `prompts/` | stage the agent through the run | `prompts/README.md` |
| `docs/` | define workflow, state, review, and roadmap | `docs/README.md` |
| `inventory/` | keep the source-coverage ledger | `inventory/README.md` |
| `paper/` | hold the LaTeX draft and generated artifacts | `paper/main.tex` |
| `runs/` | keep per-run planning and evidence files | `runs/current/` |
| `reviews/` | store review findings and final status | `reviews/review-current.md` |
| `scripts/` | create runs, compile PDFs, and run checks | `scripts/new-run.ps1` |
| `src/` | generate tables, figures, and model outputs | `src/` |

## Evidence Flow

1. Route signals are read from the problem and stored in the run notes.
2. A route is selected from the CUMCM knowledge base and algorithm cards.
3. The model plan defines assumptions, variables, outputs, and validation.
4. Code generates tables and figures with stable paths.
5. LaTeX writes the paper around the generated evidence.
6. The PDF is compiled and visually checked.
7. The review files record Pass/Warn/Fail/Unknown findings.

## Maintenance Rule

- Keep the top-level entry pages short.
- Put details in the layer that owns them.
- Use state files to record what has actually changed.
- Update the architecture page when the layer boundaries change.
