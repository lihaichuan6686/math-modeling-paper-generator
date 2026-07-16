# Human-Team Paper Composition

Purpose: help the generator write papers that feel like coordinated team drafts instead of stitched machine sections.

## Composition Principle

A strong paper is not just "all required sections are present".

It should feel like:

```text
the team understood the object
-> chose a route on purpose
-> built models in layers
-> used visuals to make the route concrete
-> interpreted results immediately
-> admitted limits without collapsing confidence
```

## Section Rhythm

For each major subquestion, the section rhythm should usually be:

```text
why this subquestion matters
-> why this route fits
-> variable / model setup
-> equation or algorithm details
-> artifact
-> interpretation
-> validation or comparison
-> close-out sentence
```

If a subquestion ends right after equations or right after one table, it usually still reads machine-made.

## Early Figure Rule

Place an early figure or table that identifies the modeled object before the most technical section becomes dense.

Examples:

- network map
- process diagram
- route or flow diagram
- feature or variable relationship map
- staged workflow diagram

This keeps the paper object-first rather than algorithm-first.

## Paragraph Rule

Prefer analytical paragraphs over stacked bullets when:

- explaining why a route fits;
- interpreting table differences;
- describing tradeoffs or limitations;
- closing a major subquestion.

Bullets are acceptable for:

- assumptions;
- symbols;
- short result summaries;
- explicit contribution or limitation lists.

## Close-Out Rule

Every major subquestion should end with a paragraph that states:

1. the finding;
2. the evidence that supports it;
3. why the next subquestion is needed.

This is one of the clearest differences between a team-like paper and a staged generator draft.

## Abstract Composition Rule

The abstract should compress full closures, not partial steps.

For each subquestion:

```text
method used -> artifact/result -> decision implication
```

Do not let the abstract list method names without closing them into results.

## Visual Distribution Rule

Do not cluster all visuals at the end.

Good distribution usually means:

- one early object-identification figure;
- one exploration or mechanism figure in data/model setup;
- one result artifact per major subquestion when feasible;
- one validation or robustness artifact.

## Long-Paper Rule

A long paper should earn length through repeated loops, not through one giant method block.

When the problem has several numbered tasks, length should usually come from:

```text
Q1 full loop
Q2 full loop
Q3 full loop
...
```

not from:

```text
one oversized global model section
-> very short result section
-> token validation
```

## Human-Team Warning Signs

Warn when:

- section intros all sound the same;
- most paragraphs begin by naming a model;
- tables are inserted without immediate interpretation;
- conclusions repeat abstract wording too closely;
- validation is separated so far from the relevant method that it loses force;
- the paper sounds like a pipeline log rather than a reasoned argument.
