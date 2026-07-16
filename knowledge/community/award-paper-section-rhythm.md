# Award Paper Section Rhythm

Purpose: convert local experience notes and CUMCM format guidance into section-by-section rhythm rules for v1.4.

This file is about visible paper feel. It should guide drafting before the paper is written and review after the paper is assembled.

## Judging Surface

CUMCM-style papers are judged through the submitted answer sheet, not through hidden effort.

The strongest visible signals are:

- reasonable assumptions;
- creative but task-fit modeling;
- correct and interpretable results;
- clear written expression;
- clean overall structure;
- a dense abstract that lets reviewers screen the paper quickly.

Treat these as paper-design constraints, not afterthoughts.

## Page And Format Rhythm

For CUMCM-style work:

- the title and abstract are a front-facing screening surface;
- the abstract should be concise but detailed, and should not exceed one page;
- the main body usually starts after the title/abstract page;
- page numbers, anonymity, reference citation format, and appendix separation must be deliberate;
- avoid relying on color printing for essential meaning.

For a 20-30 page draft, the paper should feel long because each section carries evidence, not because restatement and appendix material are inflated.

## Section Duties

### Abstract

The abstract must quickly prove that the team solved the problem.

It should contain:

- the decomposition of the problem;
- the core model or method for each major subquestion;
- the most important numerical or decision result;
- validation, sensitivity, or comparison when it changes trust;
- final recommendation when the problem asks for one.

Weak abstracts mention methods without conclusions or conclusions without enough method.

### Problem Restatement

Restatement should be short and useful.

It should clarify:

- what is given;
- what must be output;
- which constraints matter;
- which uncertainties or data limitations will shape modeling.

It should not paraphrase the original problem at length.

### Problem Analysis

Problem analysis is where the paper begins to look intelligent.

It should explain:

- why the task is decomposed in this way;
- what each subquestion is really asking;
- what data or variables drive the route;
- why the chosen route family fits the required answer;
- how results will later be checked.

Do not list model names before explaining the task logic.

### Assumptions

Assumptions should simplify the problem without breaking its practical meaning.

A strong assumption:

- has a real-world or data-based reason;
- is used later in formulas, algorithms, or interpretation;
- helps convert the problem into a solvable form;
- is not so broad that it hides the hard part of the problem.

Too many assumptions make the paper look defensive; unused assumptions make it look ceremonial.

### Symbols

Symbol tables exist to reduce reading friction.

Include symbols that are actually used in formulas or algorithms. Avoid turning the symbol section into a glossary of ordinary words.

### Model Establishment And Solution

For each subquestion, write in this rhythm:

```text
task interpretation
-> modeling object
-> formula or algorithm
-> computation or solving process
-> result table/figure
-> interpretation
-> validation or comparison
```

The reader should never need to guess how a result was produced or why a formula appears.

### Error, Sensitivity, And Robustness

This section should answer likely reviewer doubts.

Useful content includes:

- why a key parameter choice is stable enough;
- which data limitation may change the result;
- what happens under a reasonable perturbation;
- why the selected route is still acceptable despite known weakness.

Generic claims like "the model is accurate and robust" are not enough.

### Model Evaluation And Promotion

Evaluation should state concrete advantages and limitations.

Promotion or extension is useful only when the model has a realistic application path. Avoid saying the model can be applied everywhere.

### References

References should support methods, data sources, domain facts, and official standards.

Use references in the text where the claim appears. Do not pad the reference list with unused or irrelevant items.

### Appendix

Appendix is for code, long tables, supplementary figures, and reproducibility details.

Main answers and main evidence should remain in the body. A reviewer should not need to search the appendix to understand the solution.

## Human-Team Rhythm

A serious team paper often shows:

- one clear main route rather than several disconnected method fragments;
- baseline-to-improvement logic;
- visible result interpretation after every important artifact;
- a small number of honest limitations;
- enough implementation detail to show the calculations were actually done;
- smooth transitions between subquestions.

This rhythm matters as much as individual algorithm names.
