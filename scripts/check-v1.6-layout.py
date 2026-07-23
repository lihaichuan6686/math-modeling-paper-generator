# -*- coding: utf-8 -*-
"""Layout and visual-readiness checks for the v1.6 CUMCM paper workflow."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Finding:
    level: str
    gate: str
    evidence: str
    repair: str


WIDE_TABULAR_RE = re.compile(r"\\begin\{tabular\}\{([^{}]*[lcr]{3,}[^{}]*)\}")
SAFE_TABLE_MARKERS = ["tabularx", "adjustbox", r"p{", r"m{", r"b{"]
OVERFULL_RE = re.compile(r"Overfull \\hbox \((?P<amount>[0-9.]+)pt too wide\)")
LONG_TEXT_TABLE_HINTS = [
    "script",
    "src/",
    "runs/",
    ".py",
    ".csv",
    ".xlsx",
    "路径",
    "脚本",
    "索引",
    "生成内容",
    "正文位置",
]
DEFAULT_FIGURE_TEXT_TERMS = [
    "ROC Curve",
    "Feature Importance",
    "Confusion Matrix",
    "Correlation Heatmap",
    "Residual Plot",
    "Scatter Plot",
    "Distribution",
    "Fitted Curve",
]
FINAL_SOURCE_PLACEHOLDERS = [
    "TODO",
    "Unknown",
    "TBD",
    "待定",
    "未知",
    "fill",
]
FINAL_SOURCE_LEAK_TERMS = [
    "Paper spine",
    "First-12-page signal",
    "Abstract claim shape",
    "Validation close",
    "First-look failure",
    "award-feel-checklist",
    "figure-style-spec.md",
    "route-decision.md",
]
TEMPLATE_FALLBACK_TERMS = [
    "生成 Nature-style 早期概念图后替换此占位",
    "图中应包含问题对象、数据流、模型层、结果层和验证层",
]
INPUT_COMMAND_RE = re.compile(r"\\(?:input|include)\{([^{}]+)\}")
GRAPHICS_COMMAND_RE = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^{}]+)\}")
GRAPHICS_EXTENSIONS = ["", ".pdf", ".png", ".jpg", ".jpeg", ".eps"]
LEDGER_PLACEHOLDER_TERMS = ["Unknown", "planned", "TODO", "TBD", "待定", "未知"]
V16_REQUIRED_REVIEW_GATES = [
    "Page Rhythm Gate",
    "Abstract Fill Gate",
    "Blank Space Gate",
    "Table Width Gate",
    "Figure Readability And Style Gate",
    "Nature-Style Concept Figure Gate",
    "Final Source Cleanup Gate",
    "Resource Link Gate",
    "Artifact Ledger Consistency Gate",
    "Title Abstract Consistency Gate",
]
TITLE_COMMAND_RE = re.compile(r"\\title\{([^{}]+)\}", re.DOTALL)
ABSTRACT_ENV_RE = re.compile(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", re.DOTALL)
KEYWORDS_RE = re.compile(r"\\keywords\{([^{}]+)\}", re.DOTALL)
TITLE_BAD_TERMS = ["数学建模论文", "问题求解", "论文生成", "TODO", "Unknown", "待定", "某问题"]
TITLE_GOOD_TERMS = ["基于", "面向", "考虑", "融合", "模型", "优化", "评价", "预测", "判定", "策略", "研究"]
ABSTRACT_MARKERS = ["针对问题一", "针对问题二", "针对问题三"]


def add(findings: list[Finding], level: str, gate: str, evidence: str, repair: str) -> None:
    findings.append(Finding(level, gate, evidence, repair))


def normalize(text: str) -> str:
    return re.sub(r"\s+", "", text or "")


def load_pdf_pages(pdf_path: Path) -> list[str]:
    try:
        from pypdf import PdfReader
    except Exception as exc:  # pragma: no cover
        raise RuntimeError("Missing pypdf. Run scripts/setup.ps1 first.") from exc

    reader = PdfReader(str(pdf_path))
    pages: list[str] = []
    for page in reader.pages:
        try:
            pages.append(page.extract_text() or "")
        except Exception:
            pages.append("")
    return pages


def check_pdf(pdf_path: Path, findings: list[Finding]) -> dict[str, object]:
    pages = load_pdf_pages(pdf_path)
    all_text = "\n".join(pages)
    counts = [len(normalize(page)) for page in pages]
    page_count = len(pages)
    page1_chars = counts[0] if counts else 0

    if page_count < 20:
        add(findings, "FAIL", "Page Rhythm Gate", f"Only {page_count} pages detected.", "Extend real body analysis and evidence before handoff.")
    elif page_count < 24:
        add(findings, "WARN", "Page Rhythm Gate", f"{page_count} pages detected; v1.6 target is 26-32.", "Check whether sections are thin or missing visual evidence.")
    elif page_count > 35:
        add(findings, "FAIL", "Page Rhythm Gate", f"{page_count} pages detected; v1.6 hard upper bound is 35 without justification.", "Compress layout, move raw material out of body, and remove appendix inflation.")
    elif page_count > 32:
        add(findings, "WARN", "Page Rhythm Gate", f"{page_count} pages detected; v1.6 target is 26-32.", "Check for sparse pages, overlong appendix, or bloated model exposition.")

    if page1_chars < 900:
        add(findings, "FAIL", "Abstract Fill Gate", f"Page 1 has {page1_chars} extracted chars; target is 900-1150.", "Expand the abstract with problem-by-problem concrete results while keeping it on page one.")
    elif page1_chars > 1200:
        add(findings, "WARN", "Abstract Fill Gate", f"Page 1 has {page1_chars} extracted chars; target is 900-1150.", "Check whether the abstract is too dense or spills visually.")

    low_pages = [(idx + 1, count) for idx, count in enumerate(counts) if idx > 0 and count < 180]
    if len(low_pages) >= 3:
        sample = ", ".join(f"p{idx}:{count}" for idx, count in low_pages[:8])
        add(findings, "WARN", "Blank Space Gate", f"Multiple low-density pages detected: {sample}", "Inspect for mostly blank symbol pages, oversized figures, or isolated tables.")
    adjacent = [(a, b) for (a, ca), (b, cb) in zip(low_pages, low_pages[1:]) if b == a + 1]
    if adjacent:
        sample = ", ".join(f"p{a}-p{b}" for a, b in adjacent[:4])
        add(findings, "FAIL", "Blank Space Gate", f"Adjacent low-density pages detected: {sample}", "Compact sparse sections or add interpretation tied to figures/tables.")

    default_hits = [term for term in DEFAULT_FIGURE_TEXT_TERMS if term in all_text]
    if default_hits:
        add(
            findings,
            "WARN",
            "Figure Readability And Style Gate",
            "Default English figure text detected: " + ", ".join(default_hits[:6]),
            "Regenerate figures with readable Chinese labels or justify domain-standard English terms in the review.",
        )

    add(
        findings,
        "WARN",
        "Raster Figure Manual Review Gate",
        "Raster figure glyph quality cannot be proven from PDF text extraction alone.",
        "Render representative pages and inspect figure text for boxed glyphs, tiny labels, clipping, and default notebook styling.",
    )

    return {
        "pdf": str(pdf_path),
        "pages": page_count,
        "page1_chars": page1_chars,
        "char_counts": counts,
    }


def read_tex_tree(tex_path: Path) -> list[tuple[Path, str]]:
    visited: set[Path] = set()
    sources: list[tuple[Path, str]] = []

    def load(path: Path) -> None:
        resolved = path.resolve()
        if resolved in visited or not resolved.exists():
            return
        visited.add(resolved)
        text = resolved.read_text(encoding="utf-8", errors="replace")
        sources.append((resolved, text))
        for match in INPUT_COMMAND_RE.finditer(text):
            raw = match.group(1).strip()
            child = (resolved.parent / raw).with_suffix(".tex")
            if not child.exists():
                child = resolved.parent / raw
            load(child)

    load(tex_path)
    return sources


def resolve_input_path(base: Path, raw: str) -> Path | None:
    candidate = base / raw
    candidates = [candidate]
    if candidate.suffix != ".tex":
        candidates.insert(0, candidate.with_suffix(".tex"))
    for path in candidates:
        if path.exists():
            return path
    return None


def resolve_graphics_path(base: Path, raw: str) -> Path | None:
    candidate = base / raw
    candidates: list[Path] = []
    if candidate.suffix:
        candidates.append(candidate)
    else:
        candidates.extend(candidate.with_suffix(ext) if ext else candidate for ext in GRAPHICS_EXTENSIONS)
    for path in candidates:
        if path.exists():
            return path
    return None


def collect_graphics_refs(sources: list[tuple[Path, str]]) -> list[str]:
    refs: list[str] = []
    for _, text in sources:
        for match in GRAPHICS_COMMAND_RE.finditer(text):
            raw = match.group(1).strip()
            if raw and not raw.startswith(("http://", "https://")):
                refs.append(raw)
    return refs


def check_resource_links(sources: list[tuple[Path, str]], findings: list[Finding]) -> None:
    missing_inputs: list[str] = []
    missing_graphics: list[str] = []

    for path, text in sources:
        base = path.parent
        for match in INPUT_COMMAND_RE.finditer(text):
            raw = match.group(1).strip()
            if resolve_input_path(base, raw) is None:
                missing_inputs.append(f"{path.name}: {raw}")

        for match in GRAPHICS_COMMAND_RE.finditer(text):
            raw = match.group(1).strip()
            if raw.startswith(("http://", "https://")):
                continue
            if resolve_graphics_path(base, raw) is None:
                missing_graphics.append(f"{path.name}: {raw}")

    if missing_inputs:
        add(
            findings,
            "FAIL",
            "Resource Link Gate",
            "Missing LaTeX input/include files: " + "; ".join(missing_inputs[:8]),
            "Fix broken \\input or \\include paths before compiling and handing off the paper.",
        )

    if missing_graphics:
        add(
            findings,
            "FAIL",
            "Resource Link Gate",
            "Missing includegraphics files: " + "; ".join(missing_graphics[:8]),
            "Generate the referenced figures under paper/figures or update the LaTeX paths before handoff.",
        )


def ledger_mentions(ledger_text: str, ref: str) -> bool:
    normalized = ref.replace("\\", "/")
    basename = Path(normalized).name
    stem = Path(normalized).stem
    return normalized in ledger_text.replace("\\", "/") or basename in ledger_text or stem in ledger_text


def check_artifact_ledger(run_path: Path, graphics_refs: list[str], findings: list[Finding]) -> None:
    ledger_path = run_path / "artifact-ledger.md"
    if not ledger_path.exists():
        add(
            findings,
            "FAIL",
            "Artifact Ledger Consistency Gate",
            f"Missing artifact ledger: {ledger_path}",
            "Create runs/current/artifact-ledger.md and map body-critical figures, tables, code runs, and key results.",
        )
        return

    text = ledger_path.read_text(encoding="utf-8", errors="replace")
    required_sections = ["## Figures", "## Tables", "## Key Results", "## Code Runs", "## Visual Evidence Chain"]
    missing_sections = [section for section in required_sections if section not in text]
    if missing_sections:
        add(
            findings,
            "FAIL",
            "Artifact Ledger Consistency Gate",
            "artifact-ledger.md is missing sections: " + ", ".join(missing_sections),
            "Use docs/artifact-ledger-template.md so results, code, figures, tables, and validation remain traceable.",
        )

    placeholder_hits = [term for term in LEDGER_PLACEHOLDER_TERMS if term in text]
    if placeholder_hits:
        add(
            findings,
            "FAIL",
            "Artifact Ledger Consistency Gate",
            "artifact-ledger.md still contains placeholder/status terms: " + ", ".join(sorted(set(placeholder_hits))),
            "Replace template placeholders and planned/Unknown statuses with generated/inserted/rendered/accepted evidence before handoff.",
        )

    missing_from_ledger = [ref for ref in graphics_refs if not ledger_mentions(text, ref)]
    if missing_from_ledger:
        add(
            findings,
            "FAIL",
            "Artifact Ledger Consistency Gate",
            "Figures referenced in TeX are absent from artifact-ledger.md: " + "; ".join(missing_from_ledger[:8]),
            "Add each body-critical figure to the ledger with subquestion, role, source, generated-by, caption, and status.",
        )


def selected_title_from_run(run_path: Path) -> str:
    title_file = run_path / "title-candidates.md"
    if not title_file.exists():
        return ""
    text = title_file.read_text(encoding="utf-8", errors="replace")
    match = re.search(r"^Selected title:[ \t]*(.+?)\s*$", text, re.MULTILINE)
    return match.group(1).strip() if match else ""


def check_title_abstract_consistency(all_text: str, run_path: Path, findings: list[Finding]) -> None:
    title_match = TITLE_COMMAND_RE.search(all_text)
    final_title = re.sub(r"\s+", "", title_match.group(1)) if title_match else ""
    selected_title = re.sub(r"\s+", "", selected_title_from_run(run_path))

    if not final_title:
        add(
            findings,
            "FAIL",
            "Title Abstract Consistency Gate",
            "No final \\title{...} was found in the TeX source.",
            "Set the final contest-style title from runs/current/title-candidates.md.",
        )
    else:
        bad_hits = [term for term in TITLE_BAD_TERMS if term in final_title]
        if bad_hits:
            add(
                findings,
                "FAIL",
                "Title Abstract Consistency Gate",
                "Final title contains generic or placeholder wording: " + ", ".join(bad_hits),
                "Use a CUMCM-style title that names the object, modeling action, decision target, and method signal.",
            )
        if not any(term in final_title for term in TITLE_GOOD_TERMS):
            add(
                findings,
                "WARN",
                "Title Abstract Consistency Gate",
                f"Final title lacks common contest-style modeling terms: {final_title}",
                "Check whether the title sounds like a team paper title rather than a direct task label.",
            )

    if selected_title and final_title and selected_title != final_title:
        add(
            findings,
            "FAIL",
            "Title Abstract Consistency Gate",
            "Final \\title does not match Selected title in title-candidates.md.",
            "Copy the selected title into paper/main.tex exactly, or update title-candidates.md with the final decision.",
        )
    elif not selected_title:
        add(
            findings,
            "FAIL",
            "Title Abstract Consistency Gate",
            f"Selected title was not found under {run_path / 'title-candidates.md'}.",
            "Fill runs/current/title-candidates.md before final handoff.",
        )

    abstract_match = ABSTRACT_ENV_RE.search(all_text)
    abstract = abstract_match.group(1) if abstract_match else ""
    if not abstract:
        add(
            findings,
            "FAIL",
            "Title Abstract Consistency Gate",
            "No abstract environment was found in the final TeX source.",
            "Use the v1.6 structured abstract block before handoff.",
        )
        return

    missing_markers = [marker for marker in ABSTRACT_MARKERS if marker not in abstract]
    if missing_markers:
        add(
            findings,
            "FAIL",
            "Title Abstract Consistency Gate",
            "Abstract is missing per-question markers: " + ", ".join(missing_markers),
            "Use 针对问题一/二/三 paragraphs with method, result, and validation hints.",
        )

    bold_count = abstract.count(r"\textbf")
    if bold_count < 3:
        add(
            findings,
            "FAIL",
            "Title Abstract Consistency Gate",
            f"Abstract has only {bold_count} bold key-result expressions.",
            "Bold key numerical, decision, rule, or validation conclusions for at least three major results.",
        )

    keywords_match = KEYWORDS_RE.search(abstract)
    keywords = keywords_match.group(1).strip() if keywords_match else ""
    if not keywords or keywords.count(r"\quad") < 2:
        add(
            findings,
            "FAIL",
            "Title Abstract Consistency Gate",
            "Keywords are missing or fewer than three keyword groups.",
            "Use object, method, and result keywords separated by \\quad.",
        )


def check_tex(tex_path: Path, findings: list[Finding], run_path: Path | None = None) -> list[tuple[Path, str]]:
    if not tex_path.exists():
        add(findings, "WARN", "Table Width Gate", f"TeX source not found: {tex_path}", "Pass --tex with paper/main.tex to enable source layout checks.")
        return []

    sources = read_tex_tree(tex_path)
    all_text = "\n".join(text for _, text in sources)
    check_resource_links(sources, findings)
    if run_path is not None:
        check_title_abstract_consistency(all_text, run_path, findings)

    placeholder_hits = []
    for term in FINAL_SOURCE_PLACEHOLDERS:
        if term in all_text:
            placeholder_hits.append(term)
    if placeholder_hits:
        add(
            findings,
            "FAIL",
            "Final Source Cleanup Gate",
            "TeX source still contains placeholder terms: " + ", ".join(sorted(set(placeholder_hits))),
            "Replace every template TODO/Unknown/TBD placeholder before compiling the final handoff PDF.",
        )

    leak_hits = [term for term in FINAL_SOURCE_LEAK_TERMS if term in all_text]
    if leak_hits:
        add(
            findings,
            "FAIL",
            "Final Source Cleanup Gate",
            "TeX source still contains planning/workflow terms: " + ", ".join(leak_hits[:8]),
            "Convert planning vocabulary into normal contest-paper prose before handoff.",
        )

    fallback_hits = [term for term in TEMPLATE_FALLBACK_TERMS if term in all_text]
    if fallback_hits:
        add(
            findings,
            "FAIL",
            "Concept Figure Placeholder Gate",
            "The v1.6 concept-figure fallback placeholder is still present.",
            "Generate and insert a real early concept/mechanism figure, or replace the fallback with a problem-specific compilable diagram.",
        )

    ref_placeholders = re.findall(r"\\bibitem\{[^{}]+\}\s*TODO", all_text)
    if ref_placeholders:
        add(
            findings,
            "FAIL",
            "Reference Cleanup Gate",
            "Reference section still contains TODO bibliography items.",
            "Replace placeholder references with real method, data, software, or domain references before handoff.",
        )

    for path, text in sources:
        for match in WIDE_TABULAR_RE.finditer(text):
            env_end = text.find(r"\end{tabular}", match.end())
            if env_end == -1:
                env_end = min(len(text), match.end() + 800)
            else:
                env_end += len(r"\end{tabular}")
            context = text[match.start():env_end]
            if not any(marker in context for marker in SAFE_TABLE_MARKERS):
                spec = match.group(1)
                alignment_cols = len(re.findall(r"[lcr]", spec))
                has_long_text_hint = any(hint in context for hint in LONG_TEXT_TABLE_HINTS)
                if spec in {"lll", "llll"} or has_long_text_hint:
                    add(
                        findings,
                        "FAIL",
                        "Table Width Gate",
                        f"{path.name} uses a bare text-like tabular column spec {{{spec}}}.",
                        "Use tabularx/adjustbox or p{} columns for text, path, script-index, and appendix tables.",
                    )
                elif alignment_cols >= 6:
                    add(
                        findings,
                        "WARN",
                        "Table Width Gate",
                        f"{path.name} uses a bare {alignment_cols}-column numeric tabular spec {{{spec}}}.",
                        "Keep it only if the final log has no severe overfull boxes and the rendered PDF table is not clipped.",
                    )

    if "figure-style-spec.md" not in all_text and "Nature" not in all_text and "机制图" not in all_text and "流程示意图" not in all_text:
        add(
            findings,
            "WARN",
            "Nature-Style Concept Figure Gate",
            "TeX source has no obvious Nature-style/spec-driven concept figure marker.",
            "Create runs/current/figure-style-spec.md and include an early mechanism/model-route figure.",
        )
    return sources


def check_log(log_path: Path, findings: list[Finding]) -> None:
    if not log_path.exists():
        add(findings, "WARN", "Table Width Gate", f"LaTeX log not found: {log_path}", "Pass --log with paper/main.log to inspect overfull boxes.")
        return

    text = log_path.read_text(encoding="utf-8", errors="replace")
    amounts = [float(match.group("amount")) for match in OVERFULL_RE.finditer(text)]
    severe = [value for value in amounts if value > 50]
    moderate = [value for value in amounts if value > 10]
    if severe:
        add(findings, "FAIL", "Table Width Gate", f"Severe Overfull hbox detected: max {max(severe):.1f}pt.", "Fix wide tables, long paths, or unbreakable text before handoff.")
    if len(moderate) > 8:
        add(findings, "FAIL", "Table Width Gate", f"{len(moderate)} overfull hbox warnings above 10pt detected.", "Compact tables and line-breaking before handoff.")


def check_review(review_path: Path, findings: list[Finding]) -> None:
    if not review_path.exists():
        add(findings, "WARN", "Required Review Gate", f"Review file not found: {review_path}", "Create reviews/review-current.md with v1.6 Layout Gate Verdict.")
        return
    text = review_path.read_text(encoding="utf-8", errors="replace")
    if "v1.6 Layout Gate Verdict" not in text:
        add(findings, "FAIL", "Required Review Gate", "Review lacks v1.6 Layout Gate Verdict.", "Add the v1.6 verdict table and cite reviews/layout-v16-check.md.")
    missing_gates = [gate for gate in V16_REQUIRED_REVIEW_GATES if gate not in text]
    if missing_gates:
        add(
            findings,
            "FAIL",
            "Required Review Gate",
            "Review verdict table is missing v1.6 gates: " + ", ".join(missing_gates),
            "Update reviews/review-current.md from the latest new-run scaffold and fill every v1.6 gate row.",
        )
    verdict_lines = [
        line for line in text.splitlines()
        if line.startswith("|") and any(gate in line for gate in V16_REQUIRED_REVIEW_GATES)
    ]
    unknown_lines = [line for line in verdict_lines if "Unknown" in line]
    if unknown_lines:
        add(
            findings,
            "FAIL",
            "Required Review Gate",
            f"{len(unknown_lines)} v1.6 verdict rows still contain Unknown.",
            "Replace every Unknown with Pass or Fail plus concrete evidence before handoff.",
        )
    if "reviews/layout-v16-check.md" not in text:
        add(
            findings,
            "FAIL",
            "Required Review Gate",
            "Review does not reference reviews/layout-v16-check.md.",
            "Cite the executable v1.6 layout report in the final review.",
        )
    if "artifact-ledger.md" not in text:
        add(
            findings,
            "WARN",
            "Required Review Gate",
            "Review does not mention artifact-ledger.md.",
            "Reference the artifact ledger when discussing figure/table/result traceability.",
        )
    review_lower = text.lower()
    visual_markers = ["rendered", "screenshot", "page image", "渲染", "截图", "抽页"]
    if not any(marker in review_lower for marker in visual_markers):
        add(
            findings,
            "WARN",
            "Raster Figure Manual Review Gate",
            "Review does not mention rendered-page or screenshot inspection.",
            "Add a short note naming inspected PDF pages and whether figure labels showed boxed glyphs, tiny text, or clipping.",
        )


def write_report(out_path: Path, findings: list[Finding], metadata: dict[str, object]) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# v1.6 Layout Quality Check",
        "",
        f"- PDF: `{metadata.get('pdf', '')}`",
        f"- Pages: {metadata.get('pages', 'unknown')}",
        f"- Page 1 extracted chars: {metadata.get('page1_chars', 'unknown')}",
        "",
        "## Findings",
        "",
    ]
    if findings:
        lines.append("| Level | Gate | Evidence | Repair |")
        lines.append("| --- | --- | --- | --- |")
        for item in findings:
            lines.append(f"| {item.level} | {item.gate} | {item.evidence} | {item.repair} |")
    else:
        lines.append("No v1.6 layout gate failures or warnings were detected.")

    counts = metadata.get("char_counts")
    if counts:
        lines.extend(["", "## Page Text Density", ""])
        lines.append(", ".join(f"p{idx + 1}:{count}" for idx, count in enumerate(counts)))

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check v1.6 layout and visual readiness gates.")
    parser.add_argument("--pdf", default="paper/main.pdf")
    parser.add_argument("--tex", default="paper/main.tex")
    parser.add_argument("--log", default="paper/main.log")
    parser.add_argument("--review", default="reviews/review-current.md")
    parser.add_argument("--run", default="runs/current")
    parser.add_argument("--out", default="reviews/layout-v16-check.md")
    parser.add_argument("--no-fail", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    findings: list[Finding] = []
    metadata: dict[str, object] = {}

    pdf_path = Path(args.pdf)
    if pdf_path.exists():
        try:
            metadata = check_pdf(pdf_path, findings)
        except RuntimeError as exc:
            metadata = {"pdf": str(pdf_path), "pages": "unknown", "page1_chars": "unknown"}
            add(
                findings,
                "FAIL",
                "Dependency Gate",
                str(exc),
                "Run scripts/setup.ps1, then rerun scripts/check-v1.6-layout.ps1.",
            )
    else:
        add(findings, "FAIL", "Page Rhythm Gate", f"PDF not found: {pdf_path}", "Compile paper/main.pdf before layout handoff.")

    sources = check_tex(Path(args.tex), findings, Path(args.run) if args.run else None)
    if args.run:
        check_artifact_ledger(Path(args.run), collect_graphics_refs(sources), findings)
    check_log(Path(args.log), findings)
    check_review(Path(args.review), findings)
    write_report(Path(args.out), findings, metadata)

    fails = sum(1 for item in findings if item.level == "FAIL")
    warns = sum(1 for item in findings if item.level == "WARN")
    print(f"v1.6 layout check wrote {args.out}")
    print(f"Findings: {fails} fail, {warns} warn")
    return 0 if args.no_fail or fails == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
