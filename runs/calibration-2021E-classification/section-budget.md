# Section Budget Template

Use this file as the starting shape for `runs/current/section-budget.md`.

Before filling it in, read:

- `knowledge/cumcm/20-30-page-paper-blueprint.md`
- `knowledge/latex/human-style-soft-rules.md`
- `knowledge/latex/national-family-section-budget-playbook.md`
- `docs/v1.2-draft-contract.md`
- `docs/family-section-budget-examples.md`

## Target

- target paper tier: `v1.2`
- target total body length: `16-24 pages before appendix`
- target appendix length: `3-8 pages`
- route family: `classification-recognition`
- paper family: `high-dimensional data classification and identification`
- target major subquestion count: `3-4`
- strongest section by design: `usually Model establishment`
- early object-identification figure planned: `Yes`

## Section Budget

| Section | Target pages | Why this section deserves the space | Main planned artifacts | Thinness risk | Minimum closure check |
| --- | ---: | --- | --- | --- | --- |
| Abstract | 1 dense page | one method-result closure per subquestion | key result sentences | method-only summary | every major subquestion named and closed |
| Problem restatement | 0.5-1 | restate the task in modelable form | question map table if needed | generic paraphrase | task scope and outputs are explicit |
| Method overview | 0.5-1 | give route map before technical detail | workflow/route figure | late route reveal | route figure or route table exists |
| Problem analysis | 2-4 | justify route and decompose tasks | dependency figure, route comparison table | restatement padding | each subquestion gets a modeling interpretation |
| Assumptions | 0.5-1 | narrow variable scope and uncertainty | assumption list/table | decorative assumptions | assumptions are later used |
| Symbols | 0.5-1 | keep formulas readable | notation table | missing notation | major symbols are defined once |
| Data processing | 1.5-3 | show data cleaning, indicators, exploratory evidence | preprocessing table, exploratory figure | skipped evidence bridge | cleaned inputs support later models |
| Model establishment | 6-10 | main mathematical substance and constraints live here | equations, algorithm flow, decision structure | prestige method name only | every major subquestion has a full model chain |
| Solution process | 1.5-3 | explain computation and executable steps | solver table, algorithm step figure | code-only jump | model-to-output path is explicit |
| Results | 2-4 | show direct answers and decision artifacts | result tables and evidence figures | artifact dumping | each artifact is interpreted |
| Validation and sensitivity | 2-4 | show robustness and feasibility | sensitivity table, audit figure/table | token validation | every major result has a check layer |
| Strengths and limitations | 0.5-1 | show judgment and boundary awareness | comparison notes | empty self-praise | limits are concrete |
| Conclusion | 0.5-1 | close every subquestion and final recommendation | numeric close-out statements | vague ending | each task receives a final answer |
| References | 0.5-1 | support real method and domain claims | reference list | fabricated placeholders | placeholders visibly marked if unresolved |
| Appendix | 3-8 | support reproducibility only | code inventory, long tables | body rescued by appendix | body remains complete without appendix |

## Per-Subquestion Closure

For each subquestion, record where these will appear:

| Subquestion | Analysis | Support layer | Main model | Result artifact | Validation artifact | Planned close-out sentence focus |
| --- | --- | --- | --- | --- | --- | --- |
| Q1 | MIR category task | preprocessing and feature/band selection | category-separation model | spectral overview and separation evidence | category-level split/check if labels are available | category differences must be tied to spectral features |
| Q2 | MIR OP task with 15 targets | labeled/target split and preprocessing | origin classifier | OP prediction table and classifier comparison | per-origin confusion/recall | final OP predictions need origin-level reliability |
| Q3 | NIR+MIR OP task with 10 targets | band-specific preprocessing | NIR/MIR/fused origin models | band-fusion comparison and OP prediction table | band agreement/conflict audit | fusion must improve or explain disagreements |
| Q4 | NIR Class+OP task with 7 targets | partial-label split | category model plus origin model | Class/OP answer table | class-origin consistency check | class and OP claims need separate confidence boundaries |

## Evidence Distribution

- early object or workflow figure: route pipeline plus raw feature/spectrum overview.
- subquestions that have both table and figure coverage: preprocessing, classifier comparison, final validation.
- subquestions currently at risk of having table-only evidence: feature representation if no scatter/component/importance figure is generated.
- subquestions currently at risk of having no visible validation: final identification if confusion evidence is omitted.

## Family Rhythm Check

- which section should be the technical center for this family: preprocessing, feature representation, and classifier comparison.
- which section should stay intentionally short: generic problem restatement and broad background.
- where should the paper earn most of its pages: data processing, model establishment, results, and validation.
- which section most easily becomes filler and must be cut back: method-name explanations copied from textbooks.

## Final Check

- does the abstract target a full dense page: yes, but it must include model-result closure, not padding.
- does every major subquestion have a full loop: planned through the per-subquestion closure table above.
- is the first strong figure placed before late results: yes, route and raw-feature figures should appear before classifier results.
- what artifacts will prevent filler growth: preprocessing comparison, feature representation, classifier table, confusion matrix, sensitivity check.
- which family-specific abstract closure pattern should be used: data -> preprocessing -> representation -> classifier comparison -> final class-level reliability.
