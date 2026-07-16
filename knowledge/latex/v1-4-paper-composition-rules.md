# v1.4 Paper Composition Rules

Purpose: convert community soft rules and award-paper feel into writing controls.

## Abstract Controller

Read `v1-4-abstract-closeout-rules.md` before final abstract writing.

Before accepting the abstract, check:

- Does it answer every major subquestion?
- Does each subquestion include method plus result?
- Are the main numeric or decision results visible?
- Is validation or robustness mentioned when important?
- Is it dense enough for the problem's scale?
- Does it plausibly fill most of page one for a multi-question paper?
- Do abstract, body, conclusion, and artifact ledger agree on every final answer?

Forbidden abstract shape:

```text
We analyze the problem, establish models, and obtain good results.
```

Preferred abstract shape:

```text
For problem 1, we use ... and obtain ...
For problem 2, we construct ... and find ...
For problem 3, we compare ... and recommend ...
```

## Section Density Controller

Use length to carry evidence, not filler.

Expected feel:

- title: fits the modeled object or decision object;
- problem restatement: compact;
- problem analysis: route-aware;
- assumptions: few but used later;
- symbols: readable and necessary;
- data processing: enough to support trust;
- model establishment: technical center;
- results: table/figure plus interpretation;
- validation: real comparison or sensitivity;
- conclusion: direct answers.

Before accepting the section plan, verify that every standard contest-paper section has a duty:

```text
abstract -> compressed solution and results
keywords -> method/object signal
restatement -> task and output clarification
analysis -> decomposition and route logic
assumptions -> solvability boundaries used later
symbols -> formula readability
model/solution -> technical reasoning and computation
results/validation -> answer visibility and trust
evaluation/promotion -> concrete strengths, limits, reuse
references -> method/data/domain support
appendix -> reproduction support
```

## Early Artifact Controller

Before accepting the page plan, check the first 12 pages:

- page 1 should be title, dense abstract, and keywords;
- page 2 should begin problem restatement and/or problem analysis;
- pages 3-4 should introduce assumptions, symbols, route overview, or model setup;
- pages 4-6 should visibly contain at least one symbol table, route/model diagram, data table, parameter table, formal model block, or equation group when the problem supports it;
- pages 8-12 should already alternate prose with formulas, figures, tables, or model artifacts.

If the first 12 pages are mostly continuous prose, the paper lacks recent award-paper visual rhythm.

## Middle-Body Evidence Controller

In model-heavy problems, the middle body should not have long artifact droughts.

Check:

- are formulas, algorithm blocks, tables, figures, or result artifacts recurring through the model core?
- are result figures and tables introduced before the conclusion and appendix?
- does each artifact have nearby interpretation?
- does code appear only after the main model/result logic is visible?

Warn if more than 2-3 consecutive core pages are mostly prose when the problem supports mathematical or computational artifacts.

## Model Narrative Controller

Each major subquestion should follow:

```text
why this subquestion matters
-> what object is modeled
-> what method is used
-> what output is produced
-> what the output means
-> how it is checked
```

## Figure/Table Controller

Every major subquestion should have at least one visible artifact unless it is purely conceptual.

For each artifact:

- introduce it before or at citation;
- explain what it shows;
- state what decision or conclusion it supports.

Captions must not be generic.

## Reference Controller

Before final writing, ask:

- Which method claims need references?
- Which data or domain facts need sources?
- Are official documents or data sources cited?
- Are references padded with irrelevant material?

References are usually not a page-count engine. They should be real, cited in the body, and placed before appendix material.

## Appendix Controller

Appendix can be substantial, especially when code excerpts are included.

Before accepting appendix pages, check:

- does the body already contain the main formulas, result tables, result figures, and interpretation?
- does appendix code map to specific subquestions or method roles?
- is there a support-file inventory when many code files or output files are involved?
- would the paper still answer the problem if the appendix were removed?

Fail the draft if code listings or appendix screenshots replace the body explanation.

## Human Feel Controller

Avoid:

- long runs of one-sentence paragraphs;
- excessive bullets in main model sections;
- repeated scaffold phrases;
- method-name stacking;
- unsupported praise of the model.

Include:

- route-fit sentences;
- rejected-route comparison when useful;
- specific limitations;
- immediately interpreted figures/tables;
- final answer repetition.

## Thirty-Page Controller

For a CUMCM-style 20-30 page draft, length should come from:

- one dense abstract page;
- concise but complete setup sections;
- model sections that combine formulas, route explanations, tables, figures, and interpretation;
- visible validation or comparison for each major result;
- references and appendix after the body has closed the problem.

Do not create page count through:

- copied problem background;
- oversized symbol lists;
- repeated screenshots;
- code listings before body results;
- unsupported general praise in evaluation or conclusion.
