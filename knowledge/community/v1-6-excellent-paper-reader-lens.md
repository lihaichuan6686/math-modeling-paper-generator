# v1.6 calibration Excellent-Paper Reader Lens

Purpose: convert local excellent-paper reading reflections into a reusable reviewer lens for v1.6 and v1.6 calibration generation.

Primary local signal:

```text
9.鏁板寤烘ā缁忛獙鍒嗕韩锛?6绡囷級/澶у姣曚笟璁烘枃蹇冨緱-鐮旇鏁板寤烘ā浼樼璁烘枃蹇冨緱浣撲細.txt
```

The source reflects on a 2005 CUMCM national first-prize C problem paper. The durable lesson is not a topic-specific rain-forecasting method. It is how a reader judges whether each section performs its visible duty.

Use with:

- `knowledge/community/section-duty-soft-rules.md`
- `knowledge/community/v1-5-local-experience-soft-rules.md`
- `knowledge/latex/v1-6-award-feel-soft-rules.md`
- `knowledge/latex/v1-6-section-rhythm-soft-metrics.md`
- `knowledge/quality/v1-6-layout-hard-gates.md`

## Core Reader Lens

An excellent paper is read section by section, but judged as one route.

Each section should make the next section feel necessary:

```text
restatement -> analysis -> assumptions -> symbols -> model -> solution -> result -> error/validation -> evaluation -> promotion -> appendix
```

If a section can be deleted without changing the reader's understanding of the route, it is probably ceremonial.

## Section Acceptance Signals

| Section | Reader wants to see | Failure smell |
|---|---|---|
| abstract | method route plus the most important conclusions | only says "we build models" |
| problem restatement | actual significance and the exact questions to answer | copied background or vague story |
| problem analysis | data needs, route shape, subquestion dependencies, early visual thinking | short transition paragraph with no route |
| assumptions | necessary simplifications that make the model solvable and are reused later | generic assumptions that never return |
| symbols | variables that appear later in formulas | a long glossary that wastes page space |
| model construction | formulas, derivation logic, and why this model fits the task | algorithm names without mathematical duty |
| model solution | implementable computation, software role, intermediate outputs, final answer form | code is hidden and the body has no result |
| result analysis | direct answer, comparison, interpretation, and plausibility check | tables appear without explanation |
| error/validation | the most arguable weakness is confronted | validation is skipped or praises itself |
| model evaluation | concrete advantages and non-fatal limitations | generic "the model is simple and effective" |
| promotion | realistic reuse boundary or extension | new impressive terms appear after the work is over |
| appendix | code and support detail mapped to body claims | appendix carries the first real answer |

## Human-Team Writing Transfer

The local reflection repeatedly compares strengths and weaknesses of the sample paper. Convert that habit into generation:

1. When writing each major section, name the section's duty before drafting it.
2. After drafting, ask what the section still does not prove.
3. Add one reader-facing repair: a figure, formula, table, interpretation, limitation, or cross-reference.
4. Do not hide the repair in the appendix if the body needs it.

This makes the paper sound more like a team that has read strong papers and debated the draft, not an agent filling headings.

## Result And Error Analysis Rule

Good papers do not only produce numbers. They explain why a reader should trust or doubt them.

For every central result:

- state the answer directly;
- show the comparison object or baseline;
- interpret the practical meaning;
- identify the main uncertainty, error source, or controversial assumption;
- explain why the conclusion remains usable.

If the result section is short, first add interpretation and error analysis before adding new algorithms.

## Assumption Reuse Rule

Every important assumption should leave a fingerprint later in the paper.

Acceptable fingerprints include:

- a formula simplification;
- a data preprocessing choice;
- a distance, weight, threshold, or constraint definition;
- a validation or sensitivity discussion;
- a limitation paragraph.

If no fingerprint exists, remove or rewrite the assumption.

## Figure And Table Reader Rule

The reflected excellent paper was praised when a graph made raw spatial data intuitive and when tables/figures made method comparison easy.

Generation rule:

```text
Use figures and tables to expose the modeled object, comparison relation, or result distribution before asking the reader to trust a conclusion.
```

Weak uses:

- decorative flowcharts with no later reference;
- tables that list raw output without comparison;
- figures with captions that only repeat the title;
- charts that do not answer a subquestion.

## Review Questions

Before handoff, answer these in the review file:

1. Which section first makes the paper look like a serious modeling route?
2. Which assumption is most important, and where is it reused?
3. Which table or figure makes the main result easiest to believe?
4. Which error source or controversial choice did the paper confront directly?
5. Which section still feels ceremonial and should be merged, shortened, or given evidence?
6. Does the appendix support reproducibility without becoming the main answer?

## Conversion Note

This note intentionally avoids topic-specific rain-forecasting formulas. The reusable value is the reader's section-by-section acceptance logic.
