# v1.6 calibration Reference And Citation Rhythm

Purpose: make references support the paper like an experienced CUMCM team would, without turning the bibliography into decoration.

Use with:

- `knowledge/community/literature-search-and-citation-rules.md`
- `docs/literature-notes-template.md`
- `knowledge/cumcm/v1-4-section-proportion-and-reference-rules.md`
- `scripts/check-v1.5-pdf.py`
- `scripts/check-v1.6-layout.py`

## Core Rule

References should answer this question:

```text
Which non-obvious method, data source, domain constraint, validation choice, or software dependency does this source support?
```

If a source has no job in the body, remove it or record why it is only background in `literature-notes.md`.

## Reference Count Soft Targets

| Draft type | Reference target | Notes |
|---|---:|---|
| early closed-loop v1 draft | 5-10 | enough to support method/data/domain claims |
| v1.6 calibration human-team draft | 8-15 | preferred range when sources are available |
| source-heavy policy/data paper | 12-20 | acceptable if official data, standards, and methods are all cited |
| small synthetic or no-attachment demo | 3-6 | must explain the limited source base |

Do not pad to hit a number. A short honest list is better than a long uncited list.

## Required Citation Roles

For nontrivial papers, try to cover these roles:

| Role | Supports | Typical paper location |
|---|---|---|
| official/data | contest attachment, official statistic, standard, policy, data dictionary | restatement, data preprocessing |
| domain | real-world constraint, terminology, operating rule | problem analysis, assumptions |
| method | algorithm, metric, model, optimization or evaluation framework | model construction |
| validation | residual test, sensitivity logic, evaluation metric, benchmark | validation section |
| software | package or solver when material to reproducibility | appendix, implementation note |

## Citation Placement Rhythm

Good papers cite near the claim:

- data and official sources appear before or inside data preprocessing;
- domain constraints appear near assumptions or problem analysis;
- method citations appear before or during model construction;
- validation citations appear in validation, not only the reference list;
- software citations appear only when the implementation depends on a notable package/solver.

Weak rhythm:

```text
no citations in the body -> sudden bibliography at the end
```

## Decorative Reference Warnings

Flag references as decorative when:

- they never appear in body citations;
- they support only generic sentences such as "mathematical modeling is important";
- several sources support the same shallow background claim but no model choice;
- method names are cited but assumptions and applicability are not discussed;
- online answer posts are cited as if they were literature;
- citation placeholders remain in `\cite{}` or `\bibitem{}`.

## Literature Notes Conversion

Before drafting `paper/main.tex`, `runs/current/literature-notes.md` should include:

- source role;
- extracted idea;
- run file changed;
- citation duty;
- rejected or deferred sources.

During final review, check that every planned citation duty appears either:

- in `paper/main.tex`;
- in a bibliography file;
- or in a review note explaining why it was deferred.

## Abstract And Conclusion Boundary

Do not cite inside the abstract unless the template or domain makes it unavoidable.

Instead:

- abstract states results;
- body sections cite the support for methods and assumptions;
- conclusion mirrors supported claims and does not introduce new citation-dependent facts.

## Self-Review Questions

1. Does every cited source have a role: official/data, domain, method, validation, or software?
2. Are method citations placed near the model that uses them?
3. Are official/data sources cited before data-derived claims?
4. Does `literature-notes.md` explain what changed because of literature search?
5. Are uncited bibliography-only sources removed or justified?
6. Is the reference count appropriate to the problem instead of padded?
