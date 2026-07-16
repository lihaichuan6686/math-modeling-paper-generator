# v1.3 Self-Review Gate

Purpose: review whether the repository is producing reusable methodology behavior rather than one-off paper completion.

Use this gate together with the normal v1.2 review rubric.

## Gate Questions

### 1. Problem Understanding

- Is the modeled object named clearly?
- Is the final decision object explicit?
- Does the run record evidence burden and visual burden?
- Are hidden traps recorded before model choice?

### 2. Route Selection

- Was a route chosen as a chain rather than as a single method name?
- Does `route-decision.md` explain why rejected routes were worse?
- Can the selected route naturally generate a decision artifact and a validation artifact?

### 3. Paper Composition

- Is there an early object-first figure or table?
- Does each major subquestion close a full loop?
- Are the long sections long because of evidence and interpretation rather than padding?
- Does the draft feel coordinated rather than stitched?

### 4. Evidence And Claims

- Do abstract claims match the artifact ledger?
- Do conclusion claims match the visible body evidence?
- Are figures and tables doing argumentative work rather than occupying space?

### 5. Fake-Completion Checks

Warn or fail if any of these appear:

- the paper answers intermediate calculations but not the real decision;
- the route is copied from a sample family without fit explanation;
- section count is complete but the close-out logic is missing;
- visuals exist but do not identify the object or decision;
- abstract and conclusion sound stronger than the body evidence;
- model prestige replaces validation.

## Output Expectation

A v1.3-aware review should be able to state:

```text
what method family was used
why it was selected
what evidence chain it required
where the paper still reads machine-like
what must change in the method, not only in the prose
```

If the review cannot say those things, the run has not yet absorbed the methodology layer.
