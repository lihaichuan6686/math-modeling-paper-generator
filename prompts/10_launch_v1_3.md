# Launch Prompt v1.3

Use this when the goal is to improve the general methodology layer instead of only producing one stronger paper.

```text
You are working in a research-only mathematical modeling paper generator.

Your target is a v1.3 methodology-guided run.
Do not optimize only one paper instance.
Use the active problem as a test of the general method.

First read:
- docs/README.md
- docs/run-start-checklist.md
- docs/v1.3-methodology-runbook.md
- docs/v1.2-runbook.md
- knowledge/README.md
- knowledge/cumcm/problem-understanding-framework.md
- knowledge/algorithms/route-selection-protocol.md
- knowledge/cumcm/paper-generation-playbook.md
- knowledge/algorithms/cumcm-routing-rules.md
- knowledge/latex/human-team-paper-composition.md
- knowledge/latex/human-style-soft-rules.md
- knowledge/quality/v1-3-self-review-gate.md
- knowledge/quality/completion-gate.md

Then inspect problems/problem.md and any attachments.

Your job is to make the run follow a reusable methodology:

1. build the problem profile
2. compare route families
3. record the route decision
4. define the method chain and evidence chain
5. define the visual and section strategy
6. implement artifacts
7. draft the paper
8. review with both v1.2 and v1.3 gates
9. revise if the route, evidence, or composition still look weak

Required run outputs:
- runs/current/problem-profile.md
- runs/current/problem-analysis.md
- runs/current/data-inventory.md
- runs/current/model-candidates.md
- runs/current/route-decision.md
- runs/current/model-plan.md
- runs/current/method-depth-plan.md
- runs/current/verification-plan.md
- runs/current/figure-plan.md
- runs/current/section-budget.md
- runs/current/writing-style-plan.md
- runs/current/methodology-checklist.md
- runs/current/artifact-ledger.md
- reviews/review-current.md

Hard rules:
- define the modeled object before late-stage modeling;
- define the decision object before claiming completion;
- choose a route family before naming prestige algorithms;
- treat every major subquestion as a full argument loop;
- make visuals part of the method chain, not decoration;
- keep abstract and conclusion strictly bounded by the artifact ledger;
- if the review reveals method mismatch, repair the route or evidence chain, not only the prose;
- when one active problem exposes a generic weakness, document the generic rule instead of patching that problem alone.
```
