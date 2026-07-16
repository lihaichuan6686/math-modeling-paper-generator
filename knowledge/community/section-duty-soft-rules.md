# Section Duty Soft Rules

Purpose: convert local contest-experience notes into concrete section duties for v1.4 paper generation.

Primary local signal: `9.数学建模经验分享（36篇）/大学生数学建模介绍及其入门.docx`, supported by the paper-writing experience PDFs and excellent-paper reading notes.

## Core Principle

A mathematical modeling paper is usually around 30 pages because every section carries work.

It should not become long through copied background, repeated formulas, appendix code, or decorative screenshots.

The expected full-paper structure is:

```text
title
abstract
keywords
problem restatement
problem analysis
model assumptions
symbol description
model establishment and solution
model evaluation / strengths and weaknesses
model promotion or extension
references
appendix
supporting files
```

## Section Duties

### Title

The title should fit the actual route.

It can be adapted from the problem title, but it should not be so generic that it hides the modeled object or decision object.

### Abstract

The abstract is a screening surface.

It should contain:

- a short opening background or task orientation;
- the mathematical type or route family;
- the modeling idea;
- the solving or algorithm idea;
- the model feature, validation, sensitivity analysis, or robustness signal;
- the main numeric results, rankings, predictions, decisions, or conclusions for every subquestion;
- a final practical conclusion when the problem asks for one.

Do not accept an abstract that only says the paper "establishes models" and "obtains good results".

### Keywords

Use 3-5 keywords.

They should include:

- the route family;
- the key model or method;
- the main application object;
- one distinctive improvement or validation idea if space allows.

### Problem Restatement

Restatement includes background and task clarification.

It should:

- simplify and reorganize the original problem;
- clarify inputs, outputs, constraints, and subquestions;
- avoid copying the problem statement verbatim;
- avoid free-writing a new story that changes the task.

### Problem Analysis

Problem analysis is the first place where the paper should look intelligent.

It should:

- describe the overall route;
- include a thought-flow or framework figure when useful;
- analyze each subquestion separately;
- explain what data, model object, and output form each subquestion requires;
- connect subquestions so the later paper feels like one team route, not several detached answers.

### Model Assumptions

Assumptions should be necessary, task-fit, and used later.

Good assumptions:

- simplify a real difficulty;
- state a boundary of the model;
- make later formulas or computation valid;
- include key assumptions that the model cannot work without.

Weak assumptions:

- repeat obvious facts;
- excuse missing work;
- never appear again in the paper;
- change the problem in a way that avoids the hard part.

### Symbol Description

Symbol tables should include mainly variables and constants used in formulas.

Each symbol should later appear in a model section.

Do not let the symbol table become a decorative list.

### Model Establishment

Model establishment is the technical center.

It should include:

- the basic mathematical model, formula, or scheme;
- the simplified model when simplification is needed;
- the simplification idea and basis;
- clear route-fit reasoning;
- professional terminology;
- key derivation steps;
- enough detail for a reviewer to follow the logic.

The model should be practical and effective.

Prefer methods that solve the problem clearly over methods that only sound advanced.

### Model Solution

Model solution should explain:

- the computation or algorithm principle;
- the software or programming route when relevant;
- why that software or solver is suitable;
- what outputs are produced;
- which intermediate results are omitted because they do not help the reader.

The paper must visibly compute reasonable numerical or decision results.

### Result Analysis And Validation

Final results are the first-order priority.

For each required answer:

- list the result or conclusion clearly;
- use compact tables or figures for comparison;
- interpret the table or figure immediately;
- test reasonableness through comparison, sensitivity, residuals, constraints, or domain logic when possible;
- explain and repair unreasonable or high-error results instead of hiding them.

The result section should also show the full contest answer surface: assumptions used, model solution, computation path, result analysis, and improvement or robustness thinking. If any of these pieces is missing, the paper may look unfinished even when the numerical answer exists.

### Model Evaluation

Evaluation should discuss the actual model, not praise modeling in general.

Include:

- concrete advantages;
- concrete limitations;
- possible correction or improvement;
- where the model can and cannot be reused.

Keep weaknesses specific and non-fatal.

### Model Promotion

Promotion or extension should show where the model could apply beyond the original problem.

It should not introduce impressive mathematical terms that were not used.

### References

References should be relevant and higher-quality when possible.

They can include:

- method sources;
- official data or standards;
- domain literature;
- data websites used by the paper.

Every important reference should support a claim that appears in the body.

Do not let paper-format references from non-CUMCM contexts override CUMCM requirements. Use them only for generic academic surface habits such as title, abstract, keywords, body, references, and appendix discipline.

### Appendix And Supporting Files

Appendix may contain:

- extra tables and figures;
- code excerpts;
- data processing notes;
- support-file inventory.

It should not contain the only copy of the main answer.

The body must still answer the problem if the appendix is removed.

## v1.4 Generation Rules

- Before writing, prepare a `section-budget.md` that gives each section a duty and approximate length.
- Before accepting the draft, check whether each section performed its duty.
- A 20-30 page draft should be evidence-dense, not filler-dense.
- A 30-45 page stronger draft needs repeated model/result/validation artifacts across the middle body.
- Main-body bullets should be limited; use paragraphs for reasoning and tables for lists.
- Result tables and figures should appear near their interpretation, not in a distant appendix.
