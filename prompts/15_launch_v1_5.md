# Launch Prompt v1.5

Use this when the goal is to produce a v1.5 award-paper-feel CUMCM-style draft.

v1.5 fixes the v1.4 failure where the output was complete but looked like an AI technical report.

```text
You are working in a research-only mathematical modeling paper generator.

Target: v1.5 award-paper-feel draft.

Responsible-use boundary:
- use this only for learning, post-contest review, authorized research, and paper-quality checking;
- do not copy online answers, paid materials, private materials, or full solution text;
- do not fabricate data, experiments, citations, code outputs, or certainty.

Level 0 required reading only:
- START_HERE.md
- docs/v1.5-paper-template-contract.md
- docs/v1.5-method-route-contract.md
- knowledge/latex/v1-5-front-matter-rhythm-rules.md
- knowledge/latex/v1-5-award-paper-style-rules.md
- knowledge/latex/v1-5-award-paper-visual-fingerprint.md
- knowledge/community/v1-5-local-experience-soft-rules.md
- knowledge/algorithms/v1-5-route-upgrade-atlas.md
- knowledge/quality/v1-5-hard-gates.md
- memory/v15-paper-generation-feedback.md
- prompts/15_launch_v1_5.md

Then read only as needed:
- knowledge/cumcm/problem-understanding-framework.md
- knowledge/algorithms/route-selection-protocol.md
- knowledge/community/visual-evidence-chain-rules.md
- knowledge/latex/v1-4-abstract-closeout-rules.md
- docs/playwright-mcp-public-research.md
- prompts/13_platform_research.md
- prompts/11_online_consensus_check.md

Before writing:
1. Create or refresh the run scaffold.
2. Build problem-analysis.md with:
   - modeled object;
   - decision object;
   - required answer form for each question;
   - Data Traps section;
   - route choice and why simpler baselines are or are not enough.
3. Build route-decision.md and method-depth-plan.md using docs/v1.5-method-route-contract.md.
4. Use knowledge/algorithms/v1-5-route-upgrade-atlas.md to translate problem signals into support layer, main model, result artifact, validation artifact, and paper highlight.
5. Build artifact-ledger.md and figure-plan.md early.
6. Plan one early concept/mechanism/model-flow figure.
7. Build title-candidates.md with five candidate titles and a selected contest-style title.
8. Copy or mirror paper/templates/cumcm_v15_main.tex before writing paper/main.tex.

Execution requirements:
- Use a contest-style title, not the task title.
- Do not write paper/main.tex until runs/current/title-candidates.md exists.
- Abstract must be paragraph-structured and use 针对问题一/二/三 wording when appropriate.
- Key results in the abstract must be bolded with \textbf{...}.
- Page one should visually approach a full abstract page without exceeding one page.
- Section headings must not contain ASCII hyphens (`-`). Use `Zscore`, `Z score`, or Chinese wording in headings; keep hyphenated English terms only in body text.
- Do not write a thin skeleton and plan to fill it later. The first complete section draft must satisfy the source-density target in `knowledge/quality/v1-5-hard-gates.md`: normal body sections need at least 3 substantive paragraphs, model/solution/validation sections need formulas, and every central section needs figure/table evidence.
- Add an early concept figure or record a clear reason if impossible.
- Do not leak prompt terms such as 问题信号识别, 路线选择理由, 模型链概述 into the paper.
- Figures must be paper-ready: readable, Chinese-captioned, and not default notebook screenshots.
- Main result tables and figures must be in the body before appendix code.
- Every central subquestion should reach method-depth Level 3 or higher, and Level 4 when data supports it.
- method-depth-plan.md must map each subquestion to a result artifact and validation artifact.
- If a model produces impossible values or an optimal plan depends on tiny penalty groups, revise the model or downgrade the conclusion.
- Include appendix code or a script index.
- After paper/main.pdf exists, run scripts/check-v1.5-pdf.ps1 and read reviews/pdf-v15-check.md. The executable check reads `paper/main.tex` plus included section files and fails unsafe headings or thin sections.

Hard gate:
Before handoff, write a review section named v1.5 Hard Gate Verdict using knowledge/quality/v1-5-hard-gates.md.
Any failed gate or FAIL item in reviews/pdf-v15-check.md means the paper is not ready.

Minimum expected outputs:
- runs/current/problem-analysis.md
- runs/current/data-inventory.md with Data Traps
- runs/current/route-decision.md
- runs/current/model-plan.md
- runs/current/method-depth-plan.md with result and validation artifacts
- runs/current/figure-plan.md
- runs/current/title-candidates.md
- runs/current/artifact-ledger.md
- runs/current/section-budget.md
- runs/current/writing-style-plan.md
- paper/main.tex based on the v1.5 skeleton
- paper/figures/ with at least one concept figure when the problem supports it
- paper/tables/
- paper/main.pdf when local LaTeX is available
- reviews/pdf-v15-check.md when PDF compilation is available
- reviews/review-current.md with v1.5 Hard Gate Verdict and Method Route Verdict

If the paper still looks like an AI report, revise before handoff.
```
