# Prompt 06: Quality Review

Use this prompt after a draft paper, generated artifacts, and review files exist. The goal is to audit the paper as a research artifact, not to praise it.

## Required Inputs

Read these first:

1. `docs/review-checklist.md`
2. `knowledge/quality/quality-rubric-v2.md`
3. `knowledge/quality/v1-2-review-addendum.md`
4. `knowledge/quality/v1-3-self-review-gate.md`
5. `knowledge/quality/v1-4-human-feel-review-gate.md`
6. `knowledge/community/math-modeling-soft-rules.md`
7. `knowledge/community/common-mistakes-and-taboo-phrases.md`
8. `knowledge/community/paper-polish-and-feel.md`
9. `knowledge/community/award-paper-section-rhythm.md`
10. `knowledge/community/public-community-source-playbook.md`
11. `knowledge/cumcm/recent-award-paper-visual-rhythm.md`
12. `knowledge/cumcm/v1-4-section-proportion-and-reference-rules.md`
13. `knowledge/community/literature-search-and-citation-rules.md`
14. `knowledge/cumcm/problem-type-paper-archetypes.md`
15. `knowledge/latex/section-writing-patterns.md`
16. `knowledge/latex/human-style-soft-rules.md`
16. `knowledge/latex/v1-4-paper-composition-rules.md`
17. `knowledge/latex/v1-4-abstract-closeout-rules.md`
18. `knowledge/latex/local-awarded-paper-structure-rules.md`
19. `knowledge/latex/local-figure-table-conventions.md`
20. `knowledge/latex/final-polish-and-appendix-rules.md`
21. `knowledge/algorithms/method-depth-ladder.md`
22. `knowledge/cumcm/official-style-vs-modern-draft-risk.md`
23. `docs/online-consensus-weak-strong-examples.md`
24. `runs/current/online-consensus-notes.md` if it exists or the active run consensus note
25. `runs/current/artifact-ledger.md` or the active run ledger
26. `paper/main.tex`
27. all included files under `paper/sections/`
28. available generated tables and figures under `paper/tables/` and `paper/figures/`
29. latest compile result or rendered PDF pages when available

If the run is not `current`, replace `runs/current` with the active run directory.

## Review Posture

Act as a paper-quality reviewer. Prioritize:

- unsupported claims;
- skipped subquestions;
- formula-variable gaps;
- model-result inconsistency;
- unreproducible figures or tables;
- weak validation;
- abstract and section thinness;
- shallow method chains;
- machine-like paragraph rhythm;
- LaTeX/PDF rendering issues;
- responsible-use and provenance risks;
- methodology drift between route selection and final claims.

Do not spend review space on compliments unless they help explain what is already safe.

## Evidence Rules

For every finding, include:

```text
location -> status -> evidence -> risk -> required repair
```

Allowed statuses:

- `Pass`: evidence is present and consistent.
- `Warn`: issue exists but can be repaired or disclosed.
- `Fail`: issue undermines correctness, reproducibility, compliance, or trust.
- `Unknown`: evidence is missing or was not inspected.

Treat missing evidence as `Unknown`, not as `Pass`.

## Review Steps

### Step 1: Problem Coverage

Check:

- all subquestions are listed;
- subquestion numbering stays stable from abstract to conclusion;
- each subquestion has a model;
- each subquestion has a result;
- each subquestion has validation or a stated reason validation is unavailable;
- conclusion answers the original tasks.

Fail if any subquestion disappears between problem analysis and conclusion.

### Step 2: Structure and Page Logic

Check:

- paper follows a recognizable CUMCM structure;
- sections have distinct roles;
- page length comes from equations, figures, tables, validation, and appendix evidence;
- effective body length is not inflated by blank pages, code screenshots, or promotional residue;
- abstract numbers are supported later.

Warn if the paper is long because of filler background.
Warn if the paper is short because required evidence sections are missing.

For v1.2, also warn if:

- the abstract is far below one dense page without a genuine reason;
- the model section is too short for the claimed route;
- validation exists only as a token paragraph;
- section proportions do not resemble a serious team paper;
- multi-question papers do not grow through visible subquestion loops.

### Step 3: Model Credibility

Check:

- assumptions are used later;
- symbols are defined;
- objectives match stated goals;
- constraints match real limits;
- algorithm cards and problem-type archetypes support the chosen route;
- methods have enough data support.

Fail if a decision model has no constraints.
Fail if a classifier lacks data split and confusion-level evaluation.
Fail if a forecast drives decisions but no forecast error is propagated.

For v1.2, also warn if a major subquestion stays at a shallow chain such as:

```text
method -> result
```

without a support layer or a comparison/validation layer.

For E-type papers:

- if the route is production-route E, check that forecasts feed service-level, inventory, or production decisions;
- if the route is monitoring-route E, check that diagnostics and forecasts feed monitoring or policy decisions;
- fail if the paper is reviewed as generic forecast-to-decision while route-specific evidence is missing.

### Step 4: Result Traceability

Check:

- every key number in abstract and conclusion appears in the artifact ledger;
- every table and figure has a source path;
- paper values match generated output files;
- code entry points are named;
- synthetic data are marked.

Fail if the paper relies on code screenshots or appendix-only material where a main-text result artifact should exist.

Fail if important values cannot be traced.

### Step 5: Figure and Table Quality

Check:

- every figure/table is cited in text;
- `figure-plan.md`, `artifact-ledger.md`, and `paper/main.tex` agree on body-critical figures and tables;
- every body-critical figure/table has a subquestion link or whole-paper route role;
- every body-critical figure/table appears in the body before appendix support;
- captions explain modeling purpose;
- captions identify source or model role when needed;
- important figures/tables have nearby interpretation, not only captions;
- the earliest explanatory figures identify the modeled object clearly;
- axes, units, legends, and precision are adequate;
- rendered PDF pages show no clipping or unreadable labels;
- AI-generated schematic figures are not presented as data evidence;
- filenames and captions do not still read like raw one-off local shorthand.

Warn if a figure is visually readable but weak as evidence.

Also warn if important figures or tables are cited but not interpreted in prose.
Warn if most visuals are postponed to late result pages and earlier subquestions stay visually thin.
Fail if a final-answer artifact exists only in appendix or code output while the body lacks the corresponding result table/figure.

### Step 6: Validation and Robustness

Check validation according to model type:

| Model type | Required review evidence |
|---|---|
| evaluation | weight sensitivity or method comparison |
| planning | feasibility audit and scenario stress |
| rail timetable/service planning | full timetable artifact, capacity audit, tracking/dwell audit, baseline comparison, scenario recommendations |
| forecast | holdout/rolling error and uncertainty propagation |
| classification | split policy, confusion matrix, macro metric |
| geometry | residual map and physical feasibility |
| simulation | repeated runs, seed, uncertainty summary |

Fail if the paper reports final results with no validation path.

For v1.2, also warn if validation exists but is too thin to look contest-grade.

For rail-timetable/service-planning drafts, fail if:

- the timetable is only plotted and no machine-readable full output exists;
- large/small route or frequency choices are not compared against candidate alternatives;
- capacity, headway, tracking, or dwell constraints are not audited;
- Q3 recommendations lack a scenario table;
- raw cost and service-level components are hidden behind only normalized scores.

For E-route drafts, fail if:

- production-route E: no executable production table exists, or service-level/support-rate claims are not tabulated;
- production-route E: rolling-rule coefficients or capacity scenarios are used but not explained;
- monitoring-route E: diagnostics are listed without subquestion mapping;
- monitoring-route E: prediction ends the paper and no monitoring/policy scheme is produced;
- monitoring-route E: policy claims lack intervention or comparison evidence when the problem asks for effect assessment.

### Step 7: LaTeX and PDF

Check:

- compile success;
- no missing figures;
- no unresolved references;
- no stale identity fields for research copies;
- no placeholder title text, `xx`, `xxxx`, or generic `paper title` residue;
- no promotional watermark/header/footer residue in delivered research copies;
- tables and figures fit pages;
- references are real and human-readable;
- appendix boundary is explicit when long code excerpts appear;
- support-file inventory appears before long appendix code when the PDF includes code excerpts.

If PDF was not compiled or rendered, mark layout evidence as `Unknown`.

### Step 7.5: Human-Team Style Review

Check:

- whether the main body is paragraph-driven rather than bullet-driven;
- whether each major subquestion closes a full argument loop;
- whether prose explains why the method fits before showing equations;
- whether results are interpreted instead of only listed;
- whether the paper earns length through repeated analysis/model/result loops instead of one flat oversized method block.

### Step 7.6: v1.4 Contest-Feel Review

Check:

- whether the draft follows `knowledge/quality/v1-4-human-feel-review-gate.md`;
- whether the abstract feels like a compressed solution rather than a method list;
- whether online consensus was checked or explicitly skipped with a reason;
- whether public discussion was used only for sanity checking, not copied answers;
- whether the online-consensus note has source-quality labels, route reflection, rejected signals, and remaining uncertainty;
- whether the note avoids treating popularity as proof;
- whether useful online signals were converted into concrete run-file changes or explicitly rejected;
- whether exact-problem discussion happened only after the initial route-decision existed;
- whether the paper avoids template forcing and decorative advanced algorithms;
- whether restatement, analysis, assumptions, symbols, solution, error analysis, evaluation, references, and appendix each perform their expected section duty;
- whether the PDF opening follows recent award-paper rhythm: dense page-one abstract, page-two problem restatement/analysis, and no delayed modeling start;
- whether pages 4-6 contain early model evidence such as symbols, tables, diagrams, equations, or formal model setup when the problem supports them;
- whether pages 8-12 avoid long pure-prose drift by alternating artifacts and interpretation;
- whether the middle body avoids more than 2-3 consecutive artifact-light pages in model-heavy problems;
- whether code listings appear after main model/result logic rather than replacing it;
- whether body result tables and figures appear before appendix code or support files;
- whether every major subquestion has a body-visible result artifact when the task supports one;
- whether every important figure/table has source, role, subquestion link, caption, and nearby interpretation;
- whether AI-generated visuals are schematic only and never support numeric claims;
- whether long appendix code is mapped to subquestions and supported by an inventory or clear headings;
- whether references support method, data, and domain claims without uncited padding;
- whether `literature-notes.md` separates literature support from online consensus and converts useful literature signals into run-file changes or citation duties;
- whether section proportions match the declared length tier;
- whether the page count is explained as either a 20-30 page early draft or a 30-45 page stronger award-feel draft;
- whether every major answer is easy to locate in abstract, body, conclusion, and artifact ledger.
- whether the abstract plausibly fills most of page one for a multi-question paper without becoming background padding;
- whether every major subquestion has method-result closure in the abstract;
- whether every abstract and conclusion result appears in artifact-ledger key results or is explicitly qualitative;

Warn if the paper is technically complete but lacks contest-circle feel.
Fail if online material appears copied, if final answers are hidden, or if prestigious methods replace evidence.

Warn if the draft still reads like a staged scaffold rather than a team paper.

### Step 7.7: v1.3 Methodology Review

Check:

- whether `problem-profile.md` names the modeled object and decision object clearly;
- whether `route-decision.md` matches the final paper route;
- whether the paper solves the real decision task rather than only intermediate calculations;
- whether the object-first figure actually appears early enough;
- whether `methodology-checklist.md` matches the final abstract and conclusion boundaries.

Warn if the paper is locally polished but the route logic is still one-off and not reusable.

### Step 8: Responsible Use

Check:

- draft is framed for research, post-contest review, education, or authorized quality checking;
- no fabricated citations, data, or experiments;
- no hidden active-contest submission framing;
- limitations are visible.

Reject for research use if integrity risk is severe.

### Step 9: Machine Gate

Run the minimum artifact gate and cite the result in the review:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\check-run-quality.ps1 -Run current
```

For a named run and paper source, pass both:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\check-run-quality.ps1 -Run rail-demo -Paper rail_demo.tex
```

If the script reports issues, the paper cannot receive `Pass` until the issues are fixed or explicitly justified in the review.

## Output File

Write the review to:

```text
reviews/review-current.md
```

or, for a named run:

```text
reviews/review-<run>.md
```
