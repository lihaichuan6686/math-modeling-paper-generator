---
name: cumcm-paper-generator
description: Generate and review CUMCM-style mathematical modeling research paper drafts from a problem statement. Use when Claude Code is asked to use this repository to solve a mathematical modeling problem, create code-generated figures/tables, assemble a LaTeX paper, compile a PDF, or produce a self-review report. Research-only; not for active contest rule violations or fabricated evidence.
---

# CUMCM Paper Generator

Use this skill inside the cloned `math-modeling-paper-generator` repository.

## First Actions

1. Read `START_HERE.md`.
2. Read `CLAUDE.md`.
3. Read `prompts/15_launch_v1_5.md`.
4. Read `docs/v1.5-paper-template-contract.md`.
5. Read `docs/v1.5-method-route-contract.md`.
6. Read `knowledge/latex/v1-5-front-matter-rhythm-rules.md`.
7. Read `knowledge/latex/v1-5-award-paper-style-rules.md`.
8. Read `knowledge/latex/v1-5-award-paper-visual-fingerprint.md`.
9. Read `knowledge/community/v1-5-local-experience-soft-rules.md`.
10. Read `knowledge/algorithms/v1-5-route-upgrade-atlas.md`.
11. Read `knowledge/quality/v1-5-hard-gates.md`.
12. Read `problems/problem.md` unless the user specifies another problem file.
13. Create or refresh a run scaffold:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\start-current.ps1 -Name current
```

Use `-Force` only when the user wants to overwrite current run placeholders.

## Required Workflow

Default to v1.5 unless the user explicitly asks for an older version.

For v1.5, do not read the whole repository before acting. Use the Level 0 files above first, then load only task-specific references as needed.

Work through this loop:

```text
problem -> problem profile -> analysis -> candidate model routes -> selected route decision -> selected model plan -> code -> figures/tables -> LaTeX -> PDF -> review -> revision if needed
```

For v1.5, the loop must also enforce:

```text
method route contract -> title candidates -> title pattern -> paragraph abstract -> early concept figure -> paper-ready figures/tables -> sanity gates -> appendix code -> v1.5 PDF check -> v1.5 hard gate verdict
```

For v1.4/v1.5 runs, insert online consensus reflection after the initial model plan and before final paper writing when public-web access is available:

```text
initial model plan -> Playwright MCP public browsing -> online consensus notes -> route reflection -> implementation/writing
```

Use Playwright MCP as the default public-web access route when available. Search broad contest-circle experience before exact problem discussion, then use exact-problem public signals only for interpretation, sanity checking, validation ideas, and figure/table planning.
Do not use cookies, hidden APIs, ZSE/internal endpoints, login bypass, private groups, paid content, or app-only content. Record inaccessible pages and move on.
Convert useful community or local-experience signals through `docs/community-signal-to-rule-pipeline.md`; adopted signals must alter a run file, review note, prompt, or stable rule, while weak signals must be rejected or downgraded.

Do not wait for complete reading before producing the first usable draft. But when the user wants a stronger reusable method, default to the v1.5 hard-gate layer plus the v1.4 soft-rule layer and v1.3 methodology layer rather than the old small-demo standard.

Produce or update:

- `runs/current/problem-profile.md`
- `runs/current/problem-analysis.md`
- `runs/current/data-inventory.md`
- `runs/current/model-candidates.md`
- `runs/current/route-decision.md`
- `runs/current/model-plan.md`
- `runs/current/method-depth-plan.md`
- `runs/current/verification-plan.md`
- `runs/current/figure-plan.md`
- `runs/current/title-candidates.md`
- `runs/current/section-budget.md`
- `runs/current/writing-style-plan.md`
- `runs/current/methodology-checklist.md`
- `runs/current/literature-notes.md`
- `runs/current/online-consensus-notes.md` when public discussion is available or when the user asks for consensus checking
- `runs/current/artifact-ledger.md`
- code under `src/`
- figures under `paper/figures/`
- tables under `paper/tables/`
- LaTeX under `paper/`, based on `paper/templates/cumcm_v15_main.tex` for v1.5 runs
- appendix code or script index
- `reviews/pdf-v15-check.md` after `paper/main.pdf` exists in v1.5 runs
- review under `reviews/review-current.md`, including `v1.5 Hard Gate Verdict` for v1.5 runs

## Knowledge Files

Load these as needed:

- Problem understanding: `knowledge/cumcm/problem-understanding-framework.md`
- Paper structure: `knowledge/cumcm/20-30-page-paper-blueprint.md`
- v1.2 execution standard: `docs/v1.2-runbook.md`
- v1.3 methodology standard: `docs/v1.3-methodology-runbook.md`
- v1.2 drafting contract: `docs/v1.2-draft-contract.md`
- Problem-type paper archetypes: `knowledge/cumcm/problem-type-paper-archetypes.md`
- Generation workflow: `knowledge/cumcm/paper-generation-playbook.md`
- Route selection: `knowledge/algorithms/cumcm-routing-rules.md`
- Route decision protocol: `knowledge/algorithms/route-selection-protocol.md`
- Method depth: `knowledge/algorithms/method-depth-ladder.md`
- Algorithm cards: `knowledge/algorithms/cards/README.md`
- Rail/timetable route: `knowledge/algorithms/cards/rail-timetable-operation.md` when the problem involves trains, timetables, headways, OD flow, or large/small routes
- Visual rules: `docs/visual-generation-pipeline.md`
- Final pass control: `docs/v1.2-final-pass-guide.md`
- Review rules: `knowledge/quality/quality-rubric-v2.md`
- Short repair map: `knowledge/quality/v1-2-quality-matrix.md`
- Methodology review gate: `knowledge/quality/v1-3-self-review-gate.md`
- Human-feel review gate: `knowledge/quality/v1-4-human-feel-review-gate.md`
- v1.4 community learning plan: `docs/v1.4-community-learning-plan.md`
- Community signal-to-rule pipeline: `docs/community-signal-to-rule-pipeline.md`
- Community soft rules: `knowledge/community/math-modeling-soft-rules.md`
- Team execution rules: `knowledge/community/contest-workflow-and-team-execution.md`
- Literature and citation rules: `knowledge/community/literature-search-and-citation-rules.md`
- Section duty soft rules: `knowledge/community/section-duty-soft-rules.md`
- Visual evidence chain rules: `knowledge/community/visual-evidence-chain-rules.md`
- Common mistakes: `knowledge/community/common-mistakes-and-taboo-phrases.md`
- Paper polish and feel: `knowledge/community/paper-polish-and-feel.md`
- Award-paper section rhythm: `knowledge/community/award-paper-section-rhythm.md`
- Recent award-paper visual rhythm: `knowledge/cumcm/recent-award-paper-visual-rhythm.md`
- v1.4 section/reference proportions: `knowledge/cumcm/v1-4-section-proportion-and-reference-rules.md`
- Online consensus protocol: `docs/online-consensus-check-protocol.md`
- Playwright MCP public research: `docs/playwright-mcp-public-research.md`
- Playwright public browsing prompt: `prompts/13_platform_research.md`
- Online consensus weak/strong examples: `docs/online-consensus-weak-strong-examples.md`
- Public community source playbook: `knowledge/community/public-community-source-playbook.md`
- v1.4 launch prompt: `prompts/12_launch_v1_4.md`
- v1.4 user test protocol: `docs/v1.4-user-test-protocol.md`
- v1.4 user feedback template: `docs/v1.4-user-test-feedback-template.md`
- v1.5 paper template contract: `docs/v1.5-paper-template-contract.md`
- v1.5 method route contract: `docs/v1.5-method-route-contract.md`
- v1.5 front matter rhythm: `knowledge/latex/v1-5-front-matter-rhythm-rules.md`
- v1.5 award-paper style: `knowledge/latex/v1-5-award-paper-style-rules.md`
- v1.5 award-paper visual fingerprint: `knowledge/latex/v1-5-award-paper-visual-fingerprint.md`
- v1.5 local experience soft rules: `knowledge/community/v1-5-local-experience-soft-rules.md`
- v1.5 route upgrade atlas: `knowledge/algorithms/v1-5-route-upgrade-atlas.md`
- v1.5 hard gates: `knowledge/quality/v1-5-hard-gates.md`
- v1.5 launch prompt: `prompts/15_launch_v1_5.md`
- v1.5 user feedback template: `docs/v1.5-user-test-feedback-template.md`
- v1.5 feedback triage matrix: `docs/v1.5-feedback-triage-matrix.md`
- LaTeX style: `knowledge/latex/cumcm-section-contract.md`
- Human-team composition: `knowledge/latex/human-team-paper-composition.md`
- v1.4 paper composition: `knowledge/latex/v1-4-paper-composition-rules.md`
- v1.4 abstract and closeout: `knowledge/latex/v1-4-abstract-closeout-rules.md`
- Section writing patterns: `knowledge/latex/section-writing-patterns.md`
- Human-style writing rules: `knowledge/latex/human-style-soft-rules.md`
- Executable review prompt: `prompts/06_quality_review.md`
- v1.2 repair prompt: `prompts/09_revision_v1_2.md`
- Online consensus prompt: `prompts/11_online_consensus_check.md`

## v1.2 / v1.3 Acceptance Gate

A stronger paper run is acceptable only if:

- there is a coherent problem profile and problem analysis;
- at least one model route is selected and justified;
- every major subquestion has a visible result artifact and a visible validation or comparison layer when the route reasonably allows it;
- at least one table and one figure are generated by code;
- explanatory schematics, if needed, are clearly labeled as schematics and traced to a prompt or source;
- LaTeX references the generated table and figure;
- the section budget, writing-style plan, and methodology checklist exist;
- the literature note exists and separates citation support from online consensus;
- the online-consensus note exists when public discussion is relevant, or the run explains why it was skipped;
- the abstract is written last and closes each subquestion with method plus result;
- PDF compilation has been attempted and errors are fixed when possible;
- review records remaining weaknesses, methodology drift, human-feel issues, and human-verification needs.

## Paper Shape

For the eventual 20-30 page target, length must come from missing substance, not filler. Prefer:

- problem restatement;
- route analysis;
- assumptions and symbols;
- data processing;
- model establishment;
- solution process;
- results;
- validation;
- strengths and limitations;
- conclusion;
- references and appendix.

If the draft is too short, add missing figures, tables, validation, and explanation before adding prose padding.

For E-type problems, split early into:

- production-route E: forecast -> inventory / service-level / production decision;
- monitoring-route E: diagnosis -> forecast -> monitoring / policy decision.

Record that choice in the run files and make the evidence chain visible in the paper.

For the review step, use `prompts/06_quality_review.md` rather than writing a free-form summary.
If the review still flags thin sections, shallow method chains, weak abstract closure, route mismatch, or scaffold-like prose, run `prompts/09_revision_v1_2.md` before handing off the draft.

If the problem is a timetable/service-planning problem, the output must also include machine-readable operation-plan, timetable, capacity-audit, tracking/dwell-audit, and scenario-analysis artifacts, or the review must mark the run `Needs revision`.

## Responsible Use

Do not fabricate data, citations, experiments, or certainty. Mark synthetic data clearly. Refuse requests that aim at active contest cheating, hidden prohibited AI participation, or disguised authorship.
