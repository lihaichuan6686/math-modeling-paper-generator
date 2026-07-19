# v1.5 Local Experience Soft Rules

Purpose: convert readable local modeling-experience PDFs into reusable contest-writing and execution rules for v1.5 and later versions.

This note supplements awarded-paper visual rules. It focuses on the practical experience layer: what contest mentors and experienced participants repeatedly warn about.

## Sources Sampled

Local source folder:

```text
9.数学建模经验分享（36篇）
```

Readable PDF samples:

| Source | Readability | Main usable signal |
|---|---|---|
| `如何写好一篇优秀的建模论文（经验谈）.pdf` | clean enough | judging principles, paper structure, result presentation, appendix boundary |
| `成为一个数学建模“高手”的八大奥秘.pdf` | clean enough | simple useful methods, broad knowledge, communication, programming quality |
| `数学中国—美赛经验总结.pdf` | clean enough | preparation, role split, dedicated writing machine, code/tool readiness |
| `数学中国美赛培训之经验%28整理版%29.pdf` | clean enough | first-day problem reading, literature role, model practicality, unified writing |

Some other PDFs in the same folder are garbled or format-specific. Do not promote them into rules without corroboration.

## Core Soft Rules

### 1. The Paper Is The Only Scored Artifact

Experience signal:

- contest output is judged through the submitted paper;
- assumptions, model creativity, result reasonableness, and expression clarity are repeatedly named as scoring surfaces.

Generator rule:

```text
If a result, validation, assumption, or modeling choice matters, it must appear clearly in the paper body or mapped appendix. Hidden code output does not count.
```

Review question:

- Could a reviewer understand the answer without opening any script?

### 2. Every Asked Question Must Be Answered Explicitly

Experience signal:

- the paper should list numerical results, conclusions, and answer forms for all required questions;
- result tables should be concentrated, clear, and easy to compare.

Generator rule:

```text
For every numbered subquestion, include a body-level answer artifact and a closing paragraph that states the answer directly.
```

Failure smell:

- a subquestion ends with "therefore the model is effective";
- the final answer is implied by a figure but not stated;
- important numerical results appear only in appendix code.

### 3. Simple Useful Models Beat Decorative Complexity

Experience signal:

- practical problem solving is more important than piling up advanced models;
- simple methods are preferred when they solve the problem clearly;
- advanced methods require justification, implementation, and interpretation.

Generator rule:

```text
Do not add an advanced method for prestige. Use it only when it solves a stated difficulty that the baseline cannot handle.
```

Review question:

- What exact failure of the simple baseline required this stronger method?

### 4. Assumptions Must Be Necessary And Tied To The Task

Experience signal:

- reasonable assumptions are a core judging surface;
- key assumptions should come from the problem conditions and answer requirements.

Generator rule:

```text
Each important assumption should explain what difficulty it removes and why the remaining problem still matches the contest task.
```

Failure smell:

- assumptions are generic, ceremonial, or disconnected from later formulas;
- an assumption changes the original problem but the paper never admits the boundary.

### 5. Results Need Presentation, Inspection, And Repair

Experience signal:

- results should be checked for correctness, reasonableness, and error;
- when results look wrong, the model or algorithm should be revised rather than defended by prose;
- tables and charts are preferred when they make comparison easier.

Generator rule:

```text
Every central result needs one sanity check and one human-readable interpretation before it is used downstream.
```

Review question:

- If this number appeared in an awarded paper, would it look plausible to a human reader?

### 6. Appendix Supports Trust But Does Not Carry The Main Answer

Experience signal:

- detailed results, detailed tables, diagrams, and code can go to the appendix;
- main result data should still appear in the body, even if repeated.

Generator rule:

```text
Put reproducibility detail in the appendix, but keep the main answer, main tables, and main interpretation in the body.
```

Failure smell:

- the appendix is the first place where the answer becomes concrete;
- the body says "see appendix" instead of stating the result.

### 7. Team Writing Should Have One Voice

Experience signal:

- experienced advice warns against splitting the paper into disconnected voices;
- one main writing voice with team review is safer than three unrelated section styles.

Generator rule:

```text
The final paper should read as one team voice: consistent terms, repeated question map, consistent figure/table caption style, and unified conclusion language.
```

Review question:

- Do adjacent sections sound like different authors with different plans?

### 8. Preparation And Environment Are Part Of Quality

Experience signal:

- teams are advised to prepare software, code libraries, shared files, and a dedicated writing machine;
- poor computing setup wastes contest time and damages paper quality.

Generator rule:

```text
The agent should prepare a lightweight environment once, reuse scripts, and keep all artifacts in stable directories.
```

This supports `scripts/setup.ps1`, `requirements-lite.txt`, and the v1.5 run scaffold.

## Direct v1.5 Implications

For v1.5 generation:

1. write down the explicit answer form for each subquestion before implementation;
2. keep a body-level result artifact for every major question;
3. justify any advanced method by a concrete baseline weakness;
4. attach at least one sanity check to each central numerical conclusion;
5. keep appendix code mapped to subquestions;
6. revise wrong-looking results instead of hiding them behind language;
7. use one consistent writing voice across all sections;
8. treat environment setup as part of the workflow, not as an afterthought.

## Direct v1.5 Review Additions

Add these checks to late review:

| Check | Pass condition |
|---|---|
| Scored-paper surface | all key claims appear in paper, not only scripts |
| Explicit answer map | every numbered question has a visible answer artifact |
| Practicality | method complexity is justified by problem difficulty |
| Assumption duty | assumptions are task-specific and later used |
| Result sanity | central results have reasonableness checks |
| Appendix boundary | appendix supports, body answers |
| One voice | terminology and close-out style are consistent |
| Environment readiness | setup and scripts are reusable |

## Extraction Limits

This note is based on readable PDF samples only.

Old `.doc` and `.ppt` files in the same folder still require better conversion or manual sampling before they can be counted as fully absorbed.
