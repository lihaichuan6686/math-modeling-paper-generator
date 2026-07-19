# Local Experience Extraction Status

Purpose: record the current extraction state for local modeling-experience materials, especially old `.doc` and `.ppt` files.

Use this with `docs/local-experience-extraction-queue.md`.

## Status Meaning

| Status | Meaning |
|---|---|
| `absorbed` | durable rules were converted into repository guidance |
| `sampled` | readable sample was inspected, but conversion is not complete |
| `partial` | only fragments were readable; use with caution |
| `blocked` | current tools cannot read the file reliably |
| `unread` | not yet attempted |

## 2026-07-13 Probe: First Queue Batch

Method:

- temporary ASCII copies were created under `tmp/local_experience_probe`;
- binary text runs were scanned without preserving source text;
- the repeatable script for this style of probe is `scripts/probe-binary-office-text.py`;
- temporary copies must be deleted after the probe;
- extraction was judged by readability, not by whether a file merely existed.

| Source file | Queue priority | Probe result | Readability | Useful signal found | Next action |
|---|---:|---|---|---|---|
| `全国大学生数学建模竞赛论文格式规范 (2).doc` | 1 | sampled | partial | URL/font fragments only; no stable section-rule extraction yet | revisit with Word/LibreOffice/manual sampling |
| `研读数学建模优秀论文心得体会.doc` | 1 | sampled | blocked/partial | only file metadata/font fragments surfaced | revisit with Word/LibreOffice/manual sampling |
| `历年全国数学建模试题及解法归纳.doc` | 2 | sampled | partial | method fragments such as SARS case, curve fitting, Dijkstra, LINGO/MATLAB optimization hints | revisit for route-family extraction with better converter |
| `大学生数学建模竞赛活动的一些问题.ppt` | 1 | sampled | blocked/partial | mostly PowerPoint metadata and transition names | revisit with PowerPoint/LibreOffice/manual slide extraction |

## Current Finding

The first old-format batch is not cleanly readable through simple binary text scanning.

Do not treat these four files as fully absorbed. They should stay in the queue until a stable converter or manual sampling path is available.

## 2026-07-13 Scripted Probe Result

The repeatable probe script was added and tested:

```powershell
python .\scripts\probe-binary-office-text.py .\tmp\local_experience_probe .\tmp\local_experience_probe\probe.csv
```

Observed output:

| Temporary alias | Readable runs | Script readability | Interpretation |
|---|---:|---|---|
| `contest_activity_issues.ppt` | 20 | weak-partial | Some text-like runs exist, but most visible output is PowerPoint metadata or transition text |
| `excellent_paper_reflection.doc` | 6 | blocked | Not enough useful text surfaced |
| `format_spec.doc` | 9 | blocked | Not enough useful text surfaced |
| `historical_solutions.doc` | 81 | partial | Enough fragments surfaced to revisit route/method signals, but not enough for full absorption |

This confirms that the current lightweight binary probe is useful for triage, not full extraction.

## Extraction Tool Gap

Current missing capabilities in the lightweight shell path:

- robust old `.doc` text extraction;
- robust old `.ppt` slide text extraction;
- direct Office COM extraction without opening visible applications;
- LibreOffice/Pandoc-style conversion.

The repository should not depend on these tools for normal v1.4 use, but future maintenance work can use them when available.

## Operational Rule

When extraction is partial:

1. record the file as `partial` or `blocked`;
2. convert only signals that are clearly readable and generally useful;
3. avoid inventing section rules from file names alone;
4. keep the source in the queue for later revisit.

## Next Best Batch

Before continuing the blocked old-format files, try sources that are more likely to be readable:

1. remaining PDFs through bundled `pypdf`/`pdfplumber`;
2. `.docx`/`.pptx` files through bundled document libraries;
3. old `.doc`/`.ppt` only when a stable converter is available.

This keeps static learning moving without pretending poor extraction is real absorption.

## 2026-07-13 PDF Batch: Contest Purpose And Preparation

Method:

- sampled readable PDFs with bundled Python and `pypdf`;
- used extracted text only to identify durable signals;
- converted only general paper/workflow rules into repository guidance;
- did not promote garbled output into stable rules.

| Source file | Probe result | Readability | Useful signal found | Converted to | Next action |
|---|---|---|---|---|---|
| `全国大学生数学建模竞赛作用浅析.pdf` | sampled | clean | judging surface: assumptions, creativity, correctness, computation, result analysis, clear writing | `contest-workflow-and-team-execution.md`, `section-duty-soft-rules.md` | absorbed for v1.4 soft rules |
| `数学中国美赛培训之经验%28整理版%29.pdf` | sampled | clean | first-phase reading should identify objective, decision variables, data needs, cross-question links, and practical route | `contest-workflow-and-team-execution.md`, `run-start-checklist.md` | absorbed for v1.4 workflow |
| `数学中国—美赛经验总结.pdf` | sampled | clean excerpt | preparation should answer what/where/how/why; independent solving and prepared tools matter | `contest-workflow-and-team-execution.md`, `run-start-checklist.md` | revisit later for time-allocation details |
| `美国数学建模论文格式.pdf` | sampled | partial | generic academic paper surface, not CUMCM authority | `section-duty-soft-rules.md` | no further priority |
| `数学建模个人经验谈.pdf` | sampled | garbled/partial | likely team/training discussion, but extraction is too garbled for stable content | absorption log only | revisit with better converter/OCR |

Additional operational rule:

- PDF sources can be absorbed when text extraction is clean enough to identify reusable signals.
- Garbled sources stay partial even if the title sounds useful.

## 2026-07-18 v1.5 PDF Re-Read: Practical Paper Surface And Team Execution

Method:

- re-sampled readable PDFs from `9.数学建模经验分享（36篇）`;
- extracted only general writing, judging, route, appendix, team, and environment signals;
- did not promote garbled sources into rules.

| Source file | Probe result | Readability | Useful signal found | Converted to | Next action |
|---|---|---|---|---|---|
| `如何写好一篇优秀的建模论文（经验谈）.pdf` | sampled | clean | paper is the only judged artifact; assumptions, creativity, result reasonableness, and clear expression are scoring surfaces; body must show main results | `knowledge/community/v1-5-local-experience-soft-rules.md` | absorbed for v1.5 soft rules |
| `成为一个数学建模“高手”的八大奥秘.pdf` | sampled | clean | simple-first modeling, broad knowledge, communication, programming quality | `knowledge/community/v1-5-local-experience-soft-rules.md` | absorbed for v1.5 soft rules |
| `数学中国—美赛经验总结.pdf` | sampled | clean excerpt | software, shared files, code preparation, role split, writing environment | `knowledge/community/v1-5-local-experience-soft-rules.md` | revisit later for detailed time allocation |
| `数学中国美赛培训之经验%28整理版%29.pdf` | sampled | clean | first-day reading, objective/decision variables, cross-question links, practical routes, unified writing | `knowledge/community/v1-5-local-experience-soft-rules.md` | absorbed for v1.5 soft rules |

Current conversion:

- `knowledge/community/v1-5-local-experience-soft-rules.md` records the durable v1.5 rules.
- Old `.doc` and `.ppt` files remain not fully absorbed until a better converter or manual sampling path is used.
