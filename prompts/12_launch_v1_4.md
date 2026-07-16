# Launch Prompt v1.4

Use this when the goal is to produce a v1.4 contest-feel CUMCM-style paper draft.

This launch prompt builds on v1.3 methodology and v1.2 drafting quality, then adds:

- contest-circle soft rules;
- online consensus reflection;
- recent award-paper visual rhythm;
- section proportion and reference controls;
- stronger figure/table/page-band planning;
- human-feel review.

```text
You are working in a research-only mathematical modeling paper generator.

Your target is a v1.4 contest-feel run.
Produce a complete CUMCM-style mathematical modeling paper draft, but do not optimize only one narrow historical problem. Use the active problem as a test of the general reusable method.

Responsible-use boundary:
- use this only for learning, post-contest review, authorized research, and paper-quality checking;
- do not copy online answers, paid materials, private materials, or full solution text;
- do not fabricate data, experiments, citations, or code outputs.

First read:
- docs/README.md
- docs/run-start-checklist.md
- docs/v1.4-community-learning-plan.md
- docs/community-signal-to-rule-pipeline.md
- docs/playwright-mcp-public-research.md
- docs/v1.4-definition.md
- docs/v1.4-runbook.md
- docs/v1.3-methodology-runbook.md
- docs/v1.2-draft-contract.md
- knowledge/README.md
- knowledge/community/math-modeling-soft-rules.md
- knowledge/community/paper-polish-and-feel.md
- knowledge/community/contest-workflow-and-team-execution.md
- knowledge/community/literature-search-and-citation-rules.md
- knowledge/community/section-duty-soft-rules.md
- knowledge/community/visual-evidence-chain-rules.md
- knowledge/community/award-paper-section-rhythm.md
- knowledge/community/public-community-source-playbook.md
- knowledge/community/source-quality-rubric.md
- knowledge/cumcm/problem-understanding-framework.md
- knowledge/cumcm/recent-award-paper-visual-rhythm.md
- knowledge/cumcm/v1-4-section-proportion-and-reference-rules.md
- docs/visual-generation-pipeline.md
- knowledge/algorithms/route-selection-protocol.md
- knowledge/latex/v1-4-paper-composition-rules.md
- knowledge/latex/v1-4-abstract-closeout-rules.md
- knowledge/quality/v1-4-human-feel-review-gate.md
- prompts/13_platform_research.md
- prompts/11_online_consensus_check.md
- docs/online-consensus-weak-strong-examples.md

Then inspect:
- problems/problem.md
- any data attachments
- any user-specified output requirements

Required workflow:

1. Create or refresh the run scaffold.
2. Build `problem-profile.md`, naming the modeled object, decision object, inputs, outputs, and constraints.
3. Build `problem-analysis.md`, explaining subquestion decomposition and the required answer form while simulating modeling, programming, and writing roles.
4. Build `model-candidates.md` and `route-decision.md`, comparing route families before naming advanced algorithms.
5. Build `model-plan.md`, `verification-plan.md`, and `methodology-checklist.md`, using literature search to support method, data, domain, and validation choices without copying answers.
6. Build `literature-notes.md`, separating literature support from online consensus and converting useful sources into run-file changes or citation duties.
7. Run the Playwright MCP public browsing phase after the initial model plan and before final writing. Search general contest-circle experience before exact problem discussion, browse only public pages, and do not use cookies, hidden APIs, ZSE/internal endpoints, login bypass, private groups, paid content, or app-only content.
7.5. Use `prompts/13_platform_research.md` to draft public research notes into `runs/current/online-consensus-notes.md`, then use `prompts/11_online_consensus_check.md` to review, downgrade, reject, or convert the signals.
8. Update the route only when public signals reveal a real interpretation, validation, result-range, or figure/table gap.
8.5. Convert any useful public or local-experience signal through `docs/community-signal-to-rule-pipeline.md`; every adopted signal must change a run file, review note, or explicit rule, and weak signals must be rejected or downgraded.
9. Build `figure-plan.md`, `section-budget.md`, and `writing-style-plan.md` with v1.4 page rhythm:
   - page 1: dense abstract and keywords;
   - page 2: problem restatement or analysis begins;
   - pages 4-6: early model evidence such as symbols, equations, model diagram, data table, or parameter table;
   - pages 8-12: artifacts and interpretation already recur;
   - middle body: avoid more than 2-3 artifact-light pages in model-heavy problems;
   - body result tables and figures appear before appendix code.
10. Implement code, tables, and figures. Record them in `artifact-ledger.md`.
11. Draft the LaTeX paper with paragraph-driven, human-team writing.
12. Write the abstract last so it compresses method plus result for each major subquestion and fills most of page one without exceeding one page.
13. Compile the PDF when local LaTeX is available.
14. Run `prompts/06_quality_review.md`.
15. Revise if the paper is thin, shallow, machine-like, answer-hidden, appendix-inflated, or missing online-consensus reflection.

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
- runs/current/literature-notes.md
- runs/current/online-consensus-notes.md, or a clear reason for skipping
- runs/current/artifact-ledger.md
- paper/figures/
- paper/tables/
- paper/main.tex
- paper/main.pdf when compilation is available
- reviews/review-current.md

Online consensus requirements:
- use Playwright MCP as the default public-web access route when available;
- record searched queries or platform attempts;
- search public experience and writing soft rules before searching exact problem discussion;
- classify source quality;
- record inaccessible login/captcha/paywalled/private/app-only pages and move on;
- include route reflection;
- reject or discount at least one weak/unsafe signal when encountered;
- record remaining uncertainty;
- never treat popularity as proof;
- never copy final answers.

Paper-feel requirements:
- the abstract is a dense solution surface, not a method list;
- the abstract plausibly fills most of page one and contains method-result closure for every major subquestion;
- abstract, body, conclusion, and artifact ledger agree on final answers;
- every standard section performs a real duty rather than existing as a heading;
- the run files show coordinated modeling, programming, and writing work rather than one isolated prose draft;
- problem restatement is compact;
- problem analysis explains route logic rather than repeating the background;
- assumptions and symbols are used later;
- each major subquestion closes the loop: analysis -> model -> result -> validation;
- figures and tables carry evidence, not decoration;
- every body-critical figure or table has a source, role, subquestion link, caption, and nearby interpretation;
- AI-generated images are schematic only and never support numeric claims;
- references support method, data, and domain claims without padding;
- literature search changes concrete run files or is explicitly rejected as irrelevant;
- appendix code supports reproducibility and never replaces body explanation;
- page count is explained as a 20-30 page early closed-loop draft, a 30-45 page stronger award-feel draft, or a justified 45+ page heavy-evidence draft.

Hard fail conditions:
- answers are hidden only in code or appendix;
- online sources are copied or treated as target answers;
- the paper uses prestige algorithms without task-fit reasoning;
- the body remains thin while appendix code creates page count;
- the route-decision and final paper disagree;
- abstract, conclusion, tables, and code outputs contradict each other.
```
