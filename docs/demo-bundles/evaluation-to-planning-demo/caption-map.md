# Evaluation-to-Planning Caption Map

Purpose: show how figure/table captions and nearby interpretation paragraphs should read in an evaluation-to-planning v1.2 paper.

## Caption Rule

For this route family, every important figure or table should answer three things:

1. what object or result is shown;
2. why it belongs to the current subquestion;
3. what the reader should notice before moving on.

## Figure Caption Map

| Artifact role | Weak caption pattern | Strong caption pattern | What the nearby prose should explain |
|---|---|---|---|
| route figure | supplier workflow | Overall route from supplier evaluation to executable planning and scenario verification. | why ranking alone is insufficient and why planning must follow screening |
| candidate-bridge figure | screening process | Bridge from normalized supplier indicators to retained candidate set for the planning model. | how the evaluation layer reduces the planning space |
| score comparison figure | score result | Comprehensive score comparison of candidate suppliers after indicator normalization. The leading group combines lower effective burden with higher reliability. | which suppliers remain credible and what burden dimensions drive the ranking |
| plan result figure | plan output | Executable allocation result for the retained supplier set across the planning horizon. The figure shows how the selected suppliers share the final burden under feasibility constraints. | how the plan converts ranking into an operational decision |
| sensitivity figure | sensitivity result | Scenario sensitivity of the final recommendation under disturbed demand, loss, or capacity settings. The stable region indicates where the baseline recommendation remains acceptable. | what perturbation range the recommendation survives and where it weakens |

## Table Caption Map

| Artifact role | Weak caption pattern | Strong caption pattern | What the nearby prose should explain |
|---|---|---|---|
| indicator table | supplier data | Raw and normalized supplier indicators used in the evaluation layer. | which fields required normalization and why |
| ranking table | ranking result | Comprehensive supplier ranking and retained candidate set after multi-indicator evaluation. | which candidates survive and why the ranking is only an intermediate result |
| candidate table | selected suppliers | Retained supplier set passed from the evaluation model to the planning layer. | how screening narrows the later decision space |
| plan table | final plan | Executable supplier allocation plan over the planning horizon. | what operational question this table answers |
| feasibility audit table | feasibility check | Feasibility audit of the baseline plan under demand, capacity, and effective-loss constraints. | which constraints are tight and whether the plan is truly executable |
| scenario table | scenario comparison | Comparison of baseline and disturbed scenarios for the final recommendation. | whether the recommendation remains credible beyond the baseline case |

## Interpretation Paragraph Pattern

Use this rhythm after an important figure or table:

```text
identify the artifact's role
-> state the main pattern
-> connect the pattern to the subquestion
-> state why the next layer is needed
```

Example rhythm:

```text
Table X does not finish the paper; it identifies the suppliers that remain credible after screening.
The leading candidates combine stronger reliability with lower effective burden, so they are retained for the planning layer.
This means the evaluation result is serving as a space-reduction device rather than a final recommendation.
The next step is therefore to test whether these candidates can support an executable plan under the stated constraints.
```

## Common Failure Checks

Fail the draft if:

- a caption could fit almost any paper;
- the prose only says that a table or figure exists;
- the ranking artifact is interpreted as the final answer;
- the scenario caption does not state what is being stressed.
