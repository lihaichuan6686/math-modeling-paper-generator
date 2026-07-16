# National Problem-Family Paragraph Density Playbook

Purpose: turn common CUMCM problem families into family-specific paragraph rhythm, section thickness, and explanation-density rules so the paper reads like a deliberate human-team draft rather than a thin artifact wrapper.

Use this note after:

- route selection is stable;
- the section budget is roughly planned;
- the writing-style plan is being filled or repaired.

This file does not replace page budgeting. It answers a different question:

```text
Inside the allotted pages, where should the paragraphs become dense?
Where should the draft deliberately stay short?
Which sections require interpretation blocks rather than artifact stacking?
```

## How To Use

1. Identify the primary problem family.
2. Copy the matching density pattern into `runs/current/writing-style-plan.md`.
3. Use the warning column to catch machine-thin sections before drafting the PDF.
4. Recheck the abstract and conclusion against the claim-boundary matrix after the body rhythm is stable.

## Quick Map

| Family | Where the paper should feel densest | Where it should stay deliberately compact | Most common thinness smell | Most important explanation block |
|---|---|---|---|---|
| Evaluation to planning | planning model plus plan interpretation | pure score narration | ranking table ends the story | why the score becomes an executable plan |
| Forecast to decision | forecast-to-decision bridge | background trend description | forecast section and decision section feel like two papers | what the forecast changes downstream |
| Geometry / spatial design | derivation plus physical interpretation | generic background and textbook geometry filler | formulas accumulate without scene meaning | what the computed geometry means physically |
| Dynamic scheduling / update | baseline-vs-update comparison | static-task restatement | revised plan appears with little comparison prose | what was preserved, improved, or sacrificed |
| Classification / recognition | preprocessing logic plus error interpretation | generic ML method praise | metrics appear without class-level meaning | what the error structure says about usability |
| Rail / timetable service planning | operation-plan to timetable bridge plus audits | passenger-flow narration alone | timetable artifact appears too late and too abruptly | how the chosen service pattern closes into a feasible timetable |
| Monitoring-route E | diagnosis-to-policy bridge plus long-horizon consequence explanation | descriptive diagnostic recap | diagnostic artifacts never close into a monitoring or intervention rule | how the detected pattern becomes a policy or monitoring scheme |

## Family Playbooks

### 1. Evaluation To Planning

Paragraph rhythm:

- problem analysis should usually contain 2-3 medium paragraphs that explain why ranking alone is not enough;
- data processing can be compact if the indicators are simple, but the planning transition should still get one full explanatory paragraph;
- model establishment should feel heavier in the planning subsection than in the scoring subsection;
- results should alternate `plan artifact -> feasibility meaning -> operational implication`, not `score table -> score table -> final plan`.

Recommended thickness cues:

- the scoring subsection can often close in 2-4 paragraphs plus artifacts;
- the planning subsection often needs 4-6 paragraphs because variables, constraints, and output meaning must all be visible;
- validation should include at least one paragraph on feasibility and one on scenario or comparison evidence.

Do not let these sections go thin:

- the bridge paragraph from ranking to planning;
- the first paragraph after the final plan table;
- the close-out paragraph that says why the plan is executable.

### 2. Forecast To Decision

Paragraph rhythm:

- problem analysis should explicitly separate uncertainty diagnosis from the final decision task;
- data processing should feel purposeful, with paragraphs that explain trend, noise, seasonality, or feature burden rather than decorative EDA;
- the first decision paragraph after the forecast result must explain how forecast outputs become decision inputs;
- validation usually needs two different tones: one paragraph for forecast credibility and one for decision sensitivity.

Recommended thickness cues:

- forecast-model description often needs 3-5 paragraphs if several candidate routes are compared;
- the downstream decision block should not be shorter than one artifact plus 2-3 analytical paragraphs;
- conclusion wording should be shorter than the body but still contain one sentence on uncertainty boundary.

Do not let these sections go thin:

- the decision interpretation paragraph after the forecast figure;
- the uncertainty propagation paragraph;
- the final recommendation sentence that names the strategy under the tested horizon.

### 3. Geometry / Spatial Design

Paragraph rhythm:

- the early scene-description block should use 2-3 compact paragraphs before heavy formulas arrive;
- derivation sections should alternate equation meaning and physical interpretation instead of stacking symbolic transitions;
- result sections should pair every important numeric output with one paragraph that says what moves, where, covers, intersects, or avoids;
- validation should read like replay or feasibility explanation, not only residual reporting.

Recommended thickness cues:

- the scene/coordinate setup may be short in pages but should still have enough prose to make the object visible;
- the derivation core often earns the most paragraphs, especially around case splits, constraints, and parameter meaning;
- the conclusion should compress back to 1-2 paragraphs that return to engineering meaning.

Do not let these sections go thin:

- the first paragraph after the scene figure;
- the paragraph after the final design table;
- the feasibility explanation after replay or residual artifacts.

### 4. Dynamic Scheduling / Update

Paragraph rhythm:

- the body should clearly split baseline scheduling and disturbance response into distinct prose blocks;
- the update logic deserves more than an algorithm list: it should include why the trigger matters and what objective changes;
- results should use a repeated rhythm of `baseline artifact -> updated artifact -> difference interpretation`;
- validation should emphasize what constraints remain satisfied after adjustment.

Recommended thickness cues:

- the baseline model often needs 3-4 paragraphs, but the update block should be similarly heavy if the task truly centers on disturbance response;
- comparison prose after before/after tables is often where human-team credibility is won;
- the conclusion usually needs one explicit sentence on what performance was preserved or improved.

Do not let these sections go thin:

- the paragraph introducing the disturbance or rolling-update trigger;
- the interpretation paragraph after the revised schedule;
- the final comparison close-out.

### 5. Classification / Recognition

Paragraph rhythm:

- preprocessing should have explanatory paragraphs about leakage prevention, feature meaning, or class imbalance, not just a pipeline list;
- model comparison should include prose on why the chosen classifier wins, not only a metric table;
- result interpretation should descend to class level whenever confusion or misclassification matters;
- validation should include one paragraph that separates usable recognition behavior from remaining error risk.

Recommended thickness cues:

- preprocessing and feature design often deserve as much prose as the classifier description;
- the chosen-classifier subsection can be compact if evidence is strong, but the error-analysis subsection should still receive 2-3 real paragraphs;
- conclusion should state both what the model recognizes well and where caution remains.

Do not let these sections go thin:

- the paragraph after the comparison table;
- the paragraph after the confusion matrix;
- the closing caution on class-level errors.

### 6. Rail / Timetable Service Planning

Paragraph rhythm:

- early analysis should turn passenger-flow facts into service-design logic before timetable recurrence appears;
- the operation-pattern block should explain why the selected stopping/service rule is preferable, not only list candidate plans;
- the timetable subsection should include one paragraph on recurrence construction and one on operational meaning of the resulting timetable;
- each audit artifact should be followed by a paragraph that says what it confirms operationally.

Recommended thickness cues:

- service-pattern design and timetable generation should be comparable in paragraph weight;
- the operation-to-timetable bridge is often the single most important explanatory block in the paper;
- validation usually needs multiple compact paragraphs rather than one long summary paragraph because capacity, headway, dwell, and scenarios answer different questions.

Do not let these sections go thin:

- the paragraph that connects passenger-flow analysis to the selected service plan;
- the first interpretation paragraph after the timetable artifact;
- the audit close-out paragraph that states why the plan is feasible.

### 7. Monitoring-route E

Paragraph rhythm:

- early analysis should separate descriptive diagnosis from the later monitoring or policy task;
- diagnostic sections should explain what each detected pattern implies for intervention, not only what the pattern is;
- the policy-design block should include one paragraph on rule construction and one on why the rule matches the detected behavior;
- long-horizon or intervention artifacts should be followed by one paragraph stating what practical consequence they confirm.

Recommended thickness cues:

- the diagnosis block can be substantial, but it should not outweigh the policy block so much that the final recommendation looks bolted on;
- the diagnosis-to-policy bridge is often the single most important prose block in the paper;
- conclusion wording should stay compact but must still state the rule or policy and the studied horizon boundary.

Do not let these sections go thin:

- the paragraph that converts diagnostics into a monitoring rule or policy trigger;
- the first paragraph after the policy/intervention artifact;
- the long-horizon consequence close-out.

## Cross-Family Rewrite Rules

When a section feels machine-thin, repair it in this order:

1. add the missing interpretation paragraph after the artifact;
2. add the bridge paragraph between two model layers;
3. add the validation paragraph that explains what was actually checked;
4. only then consider adding more artifacts or equations.

If a section feels bloated, cut in this order:

1. generic route praise;
2. repeated restatement of the contest text;
3. bullet-heavy narration that can be carried by one table plus one paragraph;
4. appendix-like implementation detail leaking into the main body.

## Best Use

Read this note together with:

- `human-style-soft-rules.md`
- `national-family-section-budget-playbook.md`
- `national-abstract-and-closeout-playbook.md`
- `national-problem-family-claim-boundary-matrix.md`
- `../../docs/writing-style-plan-template.md`
