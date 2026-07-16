# v1.4 Human-Feel Review Gate

Purpose: review whether a generated modeling paper looks like a serious human student team wrote it.

This gate supplements v1.3 methodology review.

## Review Statuses

- `Pass`: ready for user production testing.
- `Needs revision`: structurally usable but feels thin, mechanical, or under-evidenced.
- `Fail`: route, answer, or writing shape is not credible.

## Gate 1: Contest Answer Surface

Check:

- Are all problem-required answers visible?
- Are final answer tables easy to find?
- Does the abstract answer the questions?
- Does the conclusion repeat the key answers?
- Are main result tables and figures in the body before appendix code begins?

Fail if:

- answers are hidden in code or appendix;
- abstract only lists methods;
- final conclusions are vague.
- appendix pages create length while the body remains thin.

## Gate 2: Award-Paper Feel

Check:

- Is the abstract dense and result-oriented?
- Does the abstract stay within the one-page ceiling while still carrying method and result for each major subquestion?
- Does the abstract contain route family, modeling idea, algorithm idea, validation or robustness signal, and main results?
- Is problem restatement compact?
- Is problem analysis route-aware?
- Does problem analysis include subquestion decomposition and output form?
- Are assumptions necessary and reused later?
- Do symbol-table entries appear in later formulas?
- Does the model section have layered reasoning?
- Are figures/tables doing argumentative work?
- Does each section perform its expected duty rather than filling a template slot?
- Does appendix code support the already-closed body instead of replacing body evidence?

Fail if:

- sections are long because of padding;
- figures appear decorative;
- tables are not interpreted.
- assumptions, symbols, error analysis, or model evaluation are ceremonial and unused.
- code listings appear before the reader has seen the main result logic.
- a 20-30 page draft reaches length through background, appendix, or boilerplate instead of model/result/validation substance.

## Gate 2.5: Visual Evidence Chain

Check:

- Does each major subquestion have a body-visible result table or figure when the task supports one?
- Does every body-critical figure/table have a clear source, role, subquestion link, caption, and nearby interpretation?
- Are reproducible figures generated from code or data rather than invented manually?
- Are validation claims backed by a validation/comparison/sensitivity/error artifact?
- Are AI-generated visuals labeled as schematic and kept away from numeric claims?
- Do `figure-plan.md`, `artifact-ledger.md`, and `paper/main.tex` agree?

Fail if:

- figures are decorative or disconnected from nearby prose;
- result figures/tables appear only in the appendix;
- captions say only "result" or "model" without argumentative role;
- schematic images are presented as evidence;
- a generated paper has long model sections with no visual, table, formula, or algorithm artifacts when the problem supports them.

## Gate 3: Community Soft-Rule Compliance

Check:

- Does the paper avoid template forcing?
- Does it avoid advanced-algorithm decoration?
- Does it include baseline or comparison when useful?
- Does it explain practical meaning?

Fail if:

- a prestigious method is used without necessity;
- the draft sounds like it copied a reference route blindly.

## Gate 4: Online Consensus Reflection

Check:

- Does `online-consensus-notes.md` exist, or is skipping justified?
- Were sources classified by quality?
- Did the route change or stay stable for a stated reason?
- Were rough result ranges treated as sanity signals, not copied answers?
- Were public or local-experience signals converted into concrete run-file changes, review comments, or explicit rejections?
- Did the run avoid promoting one narrow post, topic, or answer screenshot into a general rule?

Fail if:

- online material is copied;
- no reflection exists when public discussion would reasonably be available;
- the paper ignores a major discovered misinterpretation.
- the note lists sources but never changes or audits `route-decision.md`, `model-plan.md`, `verification-plan.md`, `figure-plan.md`, `section-budget.md`, or `writing-style-plan.md`.

## Gate 5: Machine-Like Prose

Check:

- Are paragraphs varied but disciplined?
- Are bullets limited in the main body?
- Are results interpreted in human language?
- Are limitations specific?

Flag when:

- every paragraph starts the same way;
- sections read like filled templates;
- conclusion praises the model without evidence.

## Required Review Output

The review note must include:

- overall status;
- top three human-feel problems;
- missing answer-surface items;
- overclaim risks;
- exact files or sections to revise.
