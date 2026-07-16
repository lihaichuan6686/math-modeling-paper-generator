# v1.4 Abstract And Closeout Rules

Purpose: make the abstract, subquestion endings, and conclusion feel like a serious contest paper rather than a generated method summary.

This file converts local experience notes and award-paper observations into acceptance rules. It should be read together with `national-abstract-and-closeout-playbook.md`.

## Core Principle

For a multi-question CUMCM-style paper, the abstract is a compressed solution surface.

It should usually occupy most of page one because it must carry:

- the task orientation;
- the route family or modeling idea;
- method and result for every major subquestion;
- validation, comparison, sensitivity, or robustness information when relevant;
- the final decision, ranking, recommendation, or answer.

A short abstract is acceptable only when the problem itself is small or the draft is explicitly marked as incomplete.

## Abstract Acceptance Rules

Before accepting the abstract, verify:

| Item | Requirement |
|---|---|
| Length feel | dense enough to plausibly fill most of page one without exceeding one page |
| Question coverage | every major subquestion appears explicitly or through a stable question map |
| Method-result closure | each subquestion has both a method/route and a result/decision |
| Evidence visibility | key numeric or decision results are visible, not deferred to the body |
| Validation signal | major claims mention comparison, sensitivity, error, feasibility, or sanity check when the route supports it |
| Final answer | the final recommendation, ranking, design, prediction, or policy is stated |
| Claim boundary | wording does not exceed what the body, code, data, and validation prove |

Fail the abstract if it is mainly:

```text
background -> method names -> "good results"
```

Also fail the abstract if it names a method but does not expose the answer form the problem asked for. For example, an evaluation problem needs a ranking, score, classification, or conclusion; a prediction problem needs predicted values or trend conclusions; an optimization problem needs a selected plan, parameter setting, schedule, allocation, or tradeoff result.

## Abstract Sentence Budget

Use this default budget for a three-subquestion paper:

```text
1-2 sentences: task orientation and route overview
2-3 sentences: Q1 method and result
2-3 sentences: Q2 method and result
2-3 sentences: Q3 method and result
1-2 sentences: validation / comparison / robustness
1 sentence: final recommendation or overall conclusion
```

For four or more subquestions, compress the setup and pair related subquestions, but do not drop final answers.

## Per-Subquestion Closeout Rule

Each major subquestion section should end with a paragraph that states:

```text
main result
-> evidence artifact
-> validation or reasonableness check
-> how this result feeds the next subquestion or final conclusion
```

Do not end a subquestion immediately after a table, figure, or code output.

## Conclusion Acceptance Rules

The conclusion should:

- repeat the key answer for each major subquestion;
- distinguish final results from validation evidence;
- state concrete strengths and limitations;
- avoid introducing new models, data, or unsupported claims;
- use the same question map as the abstract and body;
- remain shorter and more direct than the abstract.

Fail the conclusion if it only says:

```text
The model is reasonable, scientific, and effective.
```

## Cross-File Consistency

Before final writing, compare:

- `runs/current/artifact-ledger.md`;
- `runs/current/section-budget.md`;
- `runs/current/writing-style-plan.md`;
- `paper/main.tex` and included section files.

Every abstract and conclusion result should appear in the artifact ledger as a key result or be clearly marked as qualitative.

Every final answer should appear in:

```text
abstract
-> body result section
-> conclusion
-> artifact-ledger key result
```

If one of these four locations is missing, the paper is not ready for v1.4 user testing.

Main numerical or decision results should be body-visible before the appendix. Detailed intermediate tables, code, and full data listings can move to the appendix, but the reader must be able to find the final answer without opening appendix code or raw output files.

## Machine-Like Warning Signs

Watch for:

- every abstract sentence begins with "For question...";
- method names appear without result values or decision outputs;
- conclusion repeats the abstract sentence order exactly;
- closeout paragraphs are all the same length and structure;
- validation is named but no artifact is cited;
- final answer tables exist but are not mentioned in abstract or conclusion.

Good variation still preserves coverage. The paper should feel written, not merely filled.
