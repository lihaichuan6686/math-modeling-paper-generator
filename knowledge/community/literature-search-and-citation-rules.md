# Literature Search And Citation Rules

Purpose: convert local contest-experience advice about literature search into reusable v1.4 behavior.

These rules sit between problem understanding, online consensus, model planning, and final paper writing. They are about research discipline, not bibliography padding.

## Core Principle

Search is not answer hunting.

For a modeling paper, useful literature search should produce:

- domain vocabulary;
- variable definitions;
- simplified versions of the same problem;
- partial analogues;
- model families worth comparing;
- validation methods;
- data-source hints;
- citation support for nontrivial assumptions, metrics, and algorithms.

It should not produce copied final answers, copied solution text, or blind adoption of another team's route.

## Local Experience Signal

Local experience materials repeatedly imply:

- read related work deeply enough to understand the method, not just whether it solves the exact problem;
- one useful related paper can be enough to trace a method lineage through its references;
- a clear literature summary near the beginning of a paper makes the later model feel more credible;
- citations must be recorded where claims appear;
- do not create a bibliography that is long but disconnected from the body.

## Search Phases

### Phase 1: Orientation

Before selecting a route, search for:

- official background terms;
- domain constraints;
- standard data sources;
- known evaluation criteria;
- common modeling families for similar problems.

Output should update:

- `problem-profile.md`;
- `problem-analysis.md`;
- `data-inventory.md`;
- `model-candidates.md`.

### Phase 2: Route Support

After candidate routes exist, search for:

- method assumptions;
- solver requirements;
- standard validation or sensitivity checks;
- known limitations;
- comparable simplified examples.

Output should update:

- `route-decision.md`;
- `model-plan.md`;
- `verification-plan.md`;
- `method-depth-plan.md`.

### Phase 3: Writing And Citation

After results are stable, citations should support:

- method choice;
- domain assumptions;
- data sources;
- metrics or evaluation criteria;
- software/package choices only when material.

Output should update:

- `paper/main.tex`;
- bibliography file or reference section;
- `artifact-ledger.md` when a cited source supports a figure/table/data claim;
- review notes if a claim lacks support.

## Literature Note Shape

For nontrivial problems, record a compact literature note inside `route-decision.md`, `model-plan.md`, or a dedicated run note:

| Source | Role | Extracted idea | Used in run file | Citation needed? |
|---|---|---|---|---|
| fill | domain/method/data/validation | fill | fill | yes/no |

Do not paste long quotations. Convert the idea into a route choice, assumption, validation check, or citation requirement.

## Depth-First Search Rule

When one source is clearly relevant:

1. identify its problem simplification;
2. identify its main variables and assumptions;
3. identify its method chain;
4. identify its validation style;
5. inspect its most relevant references or cited method names;
6. decide whether the current paper should adapt, reject, or cite the idea.

This is more useful than skimming many sources only to collect names.

## Citation Discipline

Every cited source should have a job:

- `method`: supports a model, algorithm, metric, or solver choice;
- `data`: supports a dataset, official number, standard, or preprocessing rule;
- `domain`: supports a background fact or real-world constraint;
- `validation`: supports a benchmark, comparison method, or evaluation protocol;
- `software`: supports reproducibility when software choice is material.

Reject these citation patterns:

- source appears only in the bibliography;
- citation is attached to a generic sentence that needs no source;
- source is used to imply a result without actually supporting it;
- web link is included because it looks academic;
- citation placeholder remains unresolved.

## Relationship To Online Consensus

Literature search and online consensus are different:

| Layer | Main use | Not allowed |
|---|---|---|
| Literature search | method, data, assumptions, validation, citations | copying a paper's solution route without adaptation |
| Online consensus | traps, rough ranges, community interpretation, missing artifacts | copying final answers or treating popularity as proof |

Both layers should change concrete run files or be explicitly rejected.

## Paper-Writing Effects

A strong paper should show literature discipline through:

- concise domain/method background in problem analysis or model setup;
- route choice that references problem logic rather than prestige;
- citations near the claims they support;
- method descriptions that explain assumptions and applicability;
- validation choices that are not invented after the fact;
- reference list length that matches real support needs.

## Review Questions

Before final handoff, ask:

1. Did the route decision use literature to understand methods rather than copy answers?
2. Are all nontrivial method, data, domain, and validation claims supported?
3. Are references cited in the body where their claims appear?
4. Does any reference look decorative?
5. Did literature search produce a concrete change in run files?
6. Did the paper avoid fabricating citations or unresolved placeholders?
