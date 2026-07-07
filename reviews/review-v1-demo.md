# Review

Run: v1-demo
Created: 2026-07-07

## Summary

The expanded v1-demo run is a synthetic closed-loop smoke test. It now generates three tables and three figures, inserts them into LaTeX, compiles an 11-page PDF, renders key pages, and records traceability in the run ledger. This is still not a contest-quality solution, but it is a stronger v1.0 demonstration of the paper-generation chain.

## Blocking Issues

None for the expanded v1.0 smoke-test goal.

## Important Issues

- The paper is 11 pages, still below the eventual 20-30 page target.
- The model remains a greedy baseline; no exact optimization solver is used.
- The data are synthetic and must not be presented as real contest evidence.
- The runner currently resets ledger and review files to placeholders, so evidence recording still needs hardening.

## Minor Issues

- MiKTeX emits font and PDF-bookmark warnings, but the PDF compiles and renders.
- The sensitivity experiment perturbs only transport loss, not supplier weights or demand.

## Evidence Checked

- `scripts/run-v1-demo.ps1 -Name v1-demo -Force` generated the run scaffold, tables, figures, and run summary.
- `scripts/compile.ps1` produced `paper/main.pdf` with 11 pages.
- Rendered pages 1-11 to `knowledge/_generated/v1_expanded_pdf-*.png`.
- Visually inspected page 4 for the supplier table, page 8 for the cost figure, and page 9 for the sensitivity table and figure.

## Evidence Not Checked

- Real CUMCM problem fit.
- Full 20-30 page pacing.
- Optimization-model solution quality.
- Automated skill execution in a fresh cloned repository.

## Required Fixes

No required fixes before committing this as the expanded v1.0 demonstration baseline.

## Human Verification Needed

Decide whether the next iteration should prioritize full-length page expansion, runner hardening, or replacing the greedy baseline with an optimization solver example.

## Final Status

Pass for expanded v1.0 closed-loop smoke test. Needs revision for production paper quality.
