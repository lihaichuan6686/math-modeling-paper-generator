# Prompt 09: v1.2 Revision

Use this prompt after `prompts/06_quality_review.md` has produced a review and the draft still feels too thin, too mechanical, or too shallow.

## Required Inputs

Read these first:

1. `reviews/review-current.md` or the active run review
2. `runs/current/method-depth-plan.md`
3. `runs/current/section-budget.md`
4. `runs/current/writing-style-plan.md`
5. `runs/current/artifact-ledger.md`
6. `knowledge/latex/human-style-soft-rules.md`
7. `knowledge/latex/national-family-section-budget-playbook.md`
8. `knowledge/latex/national-abstract-and-closeout-playbook.md`
9. `knowledge/latex/local-awarded-paper-structure-rules.md`
10. `knowledge/algorithms/method-depth-ladder.md`
11. `knowledge/cumcm/20-30-page-paper-blueprint.md`
12. `paper/main.tex`
13. all included files under `paper/sections/`

If the run is not `current`, replace the paths accordingly.

## Revision Goal

Do not rewrite blindly.

Repair the paper in the smallest set of changes that meaningfully improves:

- section density;
- paragraph flow;
- method depth;
- result interpretation;
- validation visibility;
- abstract closure;
- subquestion-loop completeness.
- family-level page rhythm.
- subquestion ending quality.

## Repair Priorities

Fix in this order:

1. missing subquestion loops
2. shallow method chains
3. thin abstract
4. wrong family-level page rhythm
5. thin model / results / validation sections
6. bullet-heavy or scaffold-like prose
7. weak interpretation after figures and tables
8. abrupt subquestion endings and transitions

## Typical Repairs

### A. Thin Abstract

Repair by adding:

- one method-result closure per subquestion;
- one validation or comparison sentence;
- one final decision sentence.

Do not add generic background.

### B. Shallow Method Chain

Upgrade:

```text
method -> result
```

into:

```text
support layer -> main model -> result -> validation/comparison
```

Possible upgrades:

- add preprocessing or indicator-construction explanation;
- add executable plan layer after evaluation;
- add scenario comparison after forecast-driven decision;
- add baseline comparison or sensitivity check.
- add one missing analysis-to-model bridge when later questions change variable scope or difficulty.

### C. Wrong Family-Level Page Rhythm

Repair by:

- expanding the true center section for the active family;
- shrinking decorative background that steals pages from model/results/validation;
- making the abstract match the family-specific closure pattern;
- making sure high-value artifact chains appear in the sections where that family normally earns length.

### D. Thin Results

Repair by adding:

- one missing table or figure;
- one interpretive paragraph that says what the artifact proves;
- one connection from the artifact to the original task.
- one explicit subquestion close-out sentence before moving to the next question.

### E. Thin Validation

Repair by adding:

- baseline comparison;
- sensitivity range and interpretation;
- feasibility audit;
- residual/error artifact;
- scenario stress table.

### F. Machine-Like Prose

Repair by:

- merging list-like fragments into analytical paragraphs;
- moving repeated "first/second/third" language into table structure when appropriate;
- writing transitions that explain why the next model step is needed;
- replacing generic praise with evidence-based interpretation.
- restoring the full subquestion loop when the body jumped from analysis to result too quickly.

### G. Abrupt Subquestion Endings And Transitions

Repair by:

- adding one explicit close-out paragraph after the main artifact;
- naming what conclusion the artifact supports;
- stating what validation confirms it;
- writing the next-step transition in route-aware language instead of `next we solve...`.

## Required Outputs

Update:

- `paper/sections/*.tex`
- `paper/main.tex` only when needed
- `runs/current/artifact-ledger.md` if new key results appear
- `runs/current/method-depth-plan.md` if the chain is upgraded
- `runs/current/section-budget.md` if section roles change
- `reviews/review-current.md` only after rerunning the review prompt

## Stop Rule

Do not stop after prose polish alone.

Stop when:

- the repaired draft closes the flagged loops;
- the strongest weak points from the review are concretely improved;
- the paper feels more like a team draft and less like a scaffold.

## Best Use

Read this together with:

- `06_quality_review.md`
- `08_launch_v1_2.md`
- `../docs/v1.2-runbook.md`
- `../knowledge/latex/human-style-soft-rules.md`
- `../knowledge/latex/local-awarded-paper-structure-rules.md`
- `../knowledge/algorithms/method-depth-ladder.md`
