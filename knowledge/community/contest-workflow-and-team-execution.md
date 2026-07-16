# Contest Workflow And Team Execution Rules

Purpose: convert local modeling-experience materials into reusable execution rules for v1.4 paper generation.

These rules are not about one problem type. They describe how a strong modeling team appears to work, and how Claude Code should imitate that structure in run files and final papers.

## Absorbed Local Signals

This note consolidates durable signals from:

- `9.数学建模经验分享（36篇）/大学生数学建模介绍及其入门.docx`
- `9.数学建模经验分享（36篇）/数学建模经验交流.pptx`
- `9.数学建模经验分享（36篇）/数学中国美赛培训之经验%28整理版%29.pdf`
- `9.数学建模经验分享（36篇）/全国大学生数学建模竞赛作用浅析.pdf`
- `9.数学建模经验分享（36篇）/数学中国—美赛经验总结.pdf`

The repeated pattern is clear: good papers come from disciplined workflow, not from isolated algorithm display.

## Team-Like Execution

Claude Code should simulate a three-role team even when working alone:

- modeling role: problem abstraction, assumptions, route selection, equations, validation logic;
- programming role: data cleaning, numerical solution, plots, tables, reproducibility artifacts;
- writing role: abstract, section rhythm, result interpretation, references, final polish.

Every run should show evidence that these three roles were coordinated. A paper that only contains prose, only contains code output, or only contains formulas does not feel like a complete modeling-team product.

## Pre-Run Preparation Rules

Before writing the final paper, the run should check:

- all problem files and attachments are identified;
- the expected output form for each subquestion is known;
- the route family is selected by problem demand, not by the author's favorite algorithm;
- required software and scripts are available;
- figure/table outputs have planned filenames and body locations;
- LaTeX or Word template constraints are understood;
- online consensus reflection has either been completed or responsibly skipped.

This should appear in `problem-profile.md`, `route-decision.md`, `figure-plan.md`, and `section-budget.md`.

Preparation also includes file and tool discipline:

- use one active run folder and one paper folder;
- keep generated figures under `paper/figures/`;
- keep generated tables under `paper/tables/`;
- record every body-critical artifact in `artifact-ledger.md`;
- keep code, table filenames, figure filenames, captions, and LaTeX references synchronized;
- avoid manual copy-paste results when a reproducible script can generate the table or figure.

A paper can lose human-team credibility when its code outputs, figure names, table captions, and final text disagree.

## First-Phase Problem Reading

The early phase should not rush into modeling.

It should first answer:

- What is the central target?
- What are the decision variables, state variables, or evaluation objects?
- Which subquestions are linked and which are independent?
- What data or assumptions control the final answer?
- Which outputs must be numeric, ranked, classified, scheduled, visualized, or explained?
- Which parts are likely traps, subjective choices, or hidden constraints?

For optimization-like tasks, identify objective, decision variables, constraints, and evaluation criteria early. For non-optimization tasks, identify the equivalent answer structure: ranking criteria, prediction target, classification label, mechanism explanation, or policy decision.

When a problem contains several questions, read all questions together before committing to a route. Later questions often reveal the real decision object, required data granularity, or validation burden. A route that solves question 1 elegantly but cannot answer question 3 should be downgraded before implementation begins.

The first-phase note should explicitly record:

- objective or central target;
- decision variables or equivalent answer object;
- constraints and assumptions that cannot be ignored;
- data needed and data actually available;
- cross-question dependencies;
- expected final artifact for each question.

## Literature And Public Information Search

Search should not be treated as "find an answer."

Useful search extracts:

- problem background and domain terms;
- typical variable definitions;
- common data sources;
- simplified versions of the same problem;
- standard validation methods;
- traps reported by other teams or instructors;
- plausible result ranges.

The run should record what was adopted, what was rejected, and why. Popularity is not proof. A public number is a sanity signal, not a target to copy.

Before a contest-style run, answer four preparation questions, abbreviated as what/where/how/why:

- `what`: what is being selected, optimized, predicted, evaluated, or explained?
- `where`: where will data, references, and domain constraints come from?
- `how`: how will the team compute, visualize, validate, and write the answer?
- `why`: why does the chosen route fit the problem better than simpler or more popular alternatives?

These questions should appear in `problem-profile.md`, `data-inventory.md`, `route-decision.md`, and `model-plan.md` rather than only in private reasoning.

## Model Selection Rules

The strongest local experience signal is practical model fit.

Use these rules:

- do not list models just to look rich;
- do not use an advanced method if a simpler method gives clearer evidence;
- do not force a prepared template onto a problem;
- build one central route and let submodels support it;
- explain why a model is useful for this question, not merely what the model is;
- innovation is acceptable when it improves simplification, solution, validation, result presentation, or promotion.

The paper should feel like it solves a real problem. It should not feel like a catalogue of algorithms.

Practicality is a judging signal. If a route cannot produce interpretable outputs, reproducible computation, visible result tables, or a clear validation story within the paper, it should lose to a simpler route that can.

## Writing Execution Rules

The writing role should start before all computation is finished, but final abstract writing should happen late.

Minimum writing rhythm:

1. early outline after route selection;
2. section budget before final drafting;
3. model sections written around actual formulas and result artifacts;
4. abstract rewritten after final result tables are stable;
5. final pass checks wording, tables, figures, references, and appendix boundary.

The abstract deserves repeated revision. It should state the route, model idea, algorithm idea, model feature or validation, and final results for every major subquestion.

## Result Presentation Rules

Results must be easy to inspect.

Use:

- concentrated final answer tables;
- figures when comparison, trend, sensitivity, geography, network, or route structure matters;
- captions that state what the reader should notice;
- nearby paragraphs that interpret the artifact;
- body-visible answers before appendix code.

Do not leave the judge to infer the final answer from raw output, scattered code, or appendix tables.

## Time-Rhythm Simulation For Claude Code

Claude Code should not literally follow a contest clock, but its run files should preserve the same rhythm:

1. read and profile the problem;
2. choose the route after comparing alternatives;
3. build the minimum working model;
4. generate evidence artifacts early;
5. expand validation and sensitivity;
6. draft the paper around artifacts;
7. rewrite abstract and conclusion at the end;
8. run self-review and revise.

This rhythm matters because it produces a paper that looks worked through, not assembled from disconnected paragraphs.

For a short 72-hour-style CUMCM simulation, preserve this order:

1. first reading: all questions, attachments, and possible routes;
2. early route decision: no implementation until the final answer form is visible;
3. first artifact: a working table or figure before the paper body becomes long;
4. mid-run writing: problem analysis, assumptions, symbols, and partial model sections grow around real artifacts;
5. final writing: abstract, conclusion, references, appendix boundary, and formatting after result artifacts stabilize.

This is a paper-generation rhythm, not a literal clock.

## Review Questions

A v1.4 review should ask:

- Does the paper show modeling, programming, and writing roles?
- Did the route come from the problem's demanded output?
- Are the main results centralized and visible?
- Are advanced methods justified by evidence?
- Did search and public consensus improve the run files rather than become decoration?
- Was the abstract rewritten after results were known?
- Would a reader understand the answer without opening code appendix?

If the answer is no, repair the run files before polishing prose.
