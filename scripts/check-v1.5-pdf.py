# -*- coding: utf-8 -*-
"""Visible PDF quality checks for the v1.5 CUMCM paper workflow."""

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


PROMPT_LEAK_TERMS = [
    "问题信号识别",
    "路线选择理由",
    "模型链概述",
    "支撑层",
    "验证层",
    "任务类型识别",
    "Claude",
    "prompt",
    "Prompt",
]

DEFAULT_PLOT_TERMS = [
    "Y Concentration",
    "Distribution",
    "Correlation Heatmap",
    "Fitted Curves",
    "Optimal Timing",
    "Feature Importance",
    "ROC Curve",
    "Confusion Matrix",
    "Scatter Plot",
    "Residual Plot",
]

CONCEPT_TERMS = [
    "概念图",
    "机理图",
    "流程图",
    "框架图",
    "示意图",
    "模型流程",
    "变量关系",
    "技术路线",
    "风险窗口",
]

ABSTRACT_TERMS = ["摘要", "针对问题一", "针对问题二", "针对问题三"]
APPENDIX_TERMS = ["附录", "关键代码", "脚本索引", "源代码", "lstlisting", "Python"]
REFERENCE_TERMS = ["参考文献", "References"]
PLACEHOLDER_TERMS = ["Unknown", "fill", "TBD", "待定", "未知", "Not started"]
ARTIFACT_PATTERNS = [
    "paper/figures/",
    "paper\\figures\\",
    "paper/tables/",
    "paper\\tables\\",
    ".png",
    ".jpg",
    ".pdf",
    ".tex",
    ".csv",
    ".xlsx",
]
TEX_PLACEHOLDER_PATTERNS = [
    "<替换",
    "<总述段",
    "<说明",
    "<关键",
    "<对象关键词",
    "<symbol>",
    "<meaning>",
    "<unit>",
    "<script.py>",
    "Put core reproducible code here",
]


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", "", text or "")


def load_pdf_text(pdf_path: Path) -> list[str]:
    try:
        from pypdf import PdfReader
    except Exception as exc:  # pragma: no cover - environment check
        raise RuntimeError(
            "Missing dependency pypdf. Run scripts/setup.ps1 or install requirements-lite.txt."
        ) from exc

    reader = PdfReader(str(pdf_path))
    pages: list[str] = []
    for page in reader.pages:
        try:
            pages.append(page.extract_text() or "")
        except Exception:
            pages.append("")
    return pages


def add(findings: list[Finding], level: str, gate: str, evidence: str, repair: str) -> None:
    findings.append(Finding(level=level, gate=gate, evidence=evidence, repair=repair))


def first_title_line(page_text: str) -> str:
    for raw in page_text.splitlines():
        line = raw.strip()
        if len(line) >= 6 and line not in {"摘要", "关键词"}:
            return line[:80]
    return ""


def check_pdf(pdf_path: Path, min_pages: int, min_page1_chars: int) -> tuple[list[Finding], dict[str, object]]:
    pages = load_pdf_text(pdf_path)
    normalized_pages = [normalize_text(page) for page in pages]
    all_text = "\n".join(pages)
    all_norm = normalize_text(all_text)
    char_counts = [len(text) for text in normalized_pages]
    findings: list[Finding] = []

    page_count = len(pages)
    if page_count < 20:
        add(
            findings,
            "FAIL",
            "PDF Density Gate",
            f"Only {page_count} pages were detected.",
            "Extend analysis, results, validation, discussion, and appendix code before handoff.",
        )
    elif page_count < min_pages:
        add(
            findings,
            "WARN",
            "PDF Density Gate",
            f"{page_count} pages detected; v1.5 target is at least {min_pages}.",
            "Check whether each problem has enough model explanation, figures, tables, and validation.",
        )

    if pages:
        title = first_title_line(pages[0])
        title_markers = ["基于", "考虑", "融合", "面向", "模型", "优化", "评价", "预测", "判定", "策略"]
        if not any(marker in title for marker in title_markers):
            add(
                findings,
                "WARN",
                "Title Gate",
                f"First title-like line is: {title or '<empty>'}",
                "Use a contest-style title with method object and modeling action, not a direct task label.",
            )

    page1_chars = char_counts[0] if char_counts else 0
    if page1_chars < min_page1_chars:
        add(
            findings,
            "FAIL",
            "Abstract Gate",
            f"Page 1 extracted character count is {page1_chars}; threshold is {min_page1_chars}.",
            "Rewrite the abstract as a full-page paragraph structure with problem-by-problem results.",
        )

    missing_abstract_terms = [term for term in ABSTRACT_TERMS if term not in all_norm]
    if missing_abstract_terms:
        add(
            findings,
            "FAIL",
            "Abstract Gate",
            "Missing abstract markers: " + ", ".join(missing_abstract_terms),
            "Use 摘要 plus 针对问题一/二/三 wording and concrete numerical conclusions.",
        )

    for term in PROMPT_LEAK_TERMS:
        if term in all_text:
            add(
                findings,
                "FAIL",
                "Prompt-Language Leak Gate",
                f"Leaked internal workflow term: {term}",
                "Rewrite the paper in normal contest-paper language and keep planning terms out of LaTeX.",
            )

    for term in DEFAULT_PLOT_TERMS:
        if term in all_text:
            add(
                findings,
                "WARN",
                "Figure Readability Gate",
                f"Default or English plot text detected: {term}",
                "Regenerate figures with Chinese titles/captions, larger fonts, and paper-ready labels.",
            )

    early_text = normalize_text("\n".join(pages[: min(6, page_count)]))
    if not any(term in early_text for term in CONCEPT_TERMS):
        add(
            findings,
            "FAIL",
            "Concept Figure Gate",
            "No early concept/mechanism/model-flow figure marker was found in the first six pages.",
            "Add an early conceptual figure after problem analysis or before model construction.",
        )

    if not any(term in all_norm for term in APPENDIX_TERMS):
        add(
            findings,
            "FAIL",
            "Appendix Code Gate",
            "No appendix-code or script-index marker was found.",
            "Add appendix code, a script index, or key algorithm listings tied to generated artifacts.",
        )

    if not any(term in all_norm for term in REFERENCE_TERMS):
        add(
            findings,
            "FAIL",
            "Reference Gate",
            "No reference section marker was found.",
            "Add a normal 8-15 item reference section where possible.",
        )

    low_pages = [(idx + 1, count) for idx, count in enumerate(char_counts) if idx > 0 and count < 180]
    if low_pages:
        sample = ", ".join(f"p{idx}:{count}" for idx, count in low_pages[:8])
        add(
            findings,
            "WARN",
            "PDF Density Gate",
            f"Very low text-density pages detected: {sample}",
            "Inspect these pages visually for blank space, oversized figures, or thin discussion.",
        )

    metadata = {
        "pdf": str(pdf_path),
        "pages": page_count,
        "page1_chars": page1_chars,
        "min_pages": min_pages,
        "min_page1_chars": min_page1_chars,
        "char_counts": char_counts,
    }
    return findings, metadata


def check_run_files(run_path: Path, findings: list[Finding]) -> None:
    if not run_path.exists():
        add(
            findings,
            "WARN",
            "Title Gate",
            f"Run directory was not found: {run_path}",
            "Run the check from a scaffolded run or pass --run to the active run directory.",
        )
        return

    title_file = run_path / "title-candidates.md"
    if not title_file.exists():
        add(
            findings,
            "FAIL",
            "Title Gate",
            f"Missing run file: {title_file}",
            "Create title-candidates.md with five candidate titles and a selected contest-style title.",
        )
        return

    text = title_file.read_text(encoding="utf-8", errors="replace")
    if text.count("| T") < 5 or "Selected title:" not in text:
        add(
            findings,
            "FAIL",
            "Title Gate",
            f"Incomplete title candidate file: {title_file}",
            "Record five candidate titles, rejection notes, and the selected title before writing LaTeX.",
        )

    title_lower = text.lower()
    title_placeholder_hits = [term for term in PLACEHOLDER_TERMS if term.lower() in title_lower]
    if title_placeholder_hits:
        add(
            findings,
            "WARN",
            "Title Gate",
            "title-candidates.md still contains placeholder terms: " + ", ".join(title_placeholder_hits),
            "Replace placeholders with real modeled object, decision object, five candidate titles, and the selected title.",
        )

    selected_match = re.search(r"^Selected title:[ \t]*(.*)$", text, re.MULTILINE)
    selected_title = selected_match.group(1).strip() if selected_match else ""
    if not selected_title or selected_title.lower() in {"unknown", "tbd", "fill", "待定", "未知"}:
        add(
            findings,
            "FAIL",
            "Title Gate",
            "Selected title is empty or still a placeholder in title-candidates.md.",
            "Choose one final contest-style title before writing paper/main.tex.",
        )

    candidate_rows = [
        line for line in text.splitlines()
        if re.match(r"^\|\s*T\d+\s*\|", line)
    ]
    filled_candidate_rows = [
        row for row in candidate_rows
        if not any(term.lower() in row.lower() for term in PLACEHOLDER_TERMS)
    ]
    if len(filled_candidate_rows) < 5:
        add(
            findings,
            "FAIL",
            "Title Gate",
            f"Only {len(filled_candidate_rows)} filled title candidate rows were detected.",
            "Write five real candidate titles and rejection/keep reasons before selecting the final title.",
        )

    method_file = run_path / "method-depth-plan.md"
    if not method_file.exists():
        add(
            findings,
            "FAIL",
            "Method Route Depth Gate",
            f"Missing run file: {method_file}",
            "Create method-depth-plan.md using docs/v1.5-method-route-contract.md.",
        )
        return

    method_text = method_file.read_text(encoding="utf-8", errors="replace")
    required_headers = [
        "Subquestion",
        "Family",
        "Support layer",
        "Main model",
        "Result artifact",
        "Validation artifact",
        "Paper section",
        "Depth",
    ]
    missing_headers = [header for header in required_headers if header not in method_text]
    if missing_headers:
        add(
            findings,
            "FAIL",
            "Method Route Depth Gate",
            "method-depth-plan.md is missing columns: " + ", ".join(missing_headers),
            "Use the v1.5 method route table with family, artifacts, validation, section, and depth.",
        )

    lower_text = method_text.lower()
    has_artifact = any(pattern.lower() in lower_text for pattern in ARTIFACT_PATTERNS)
    if not has_artifact:
        add(
            findings,
            "FAIL",
            "Method Route Depth Gate",
            "method-depth-plan.md does not name any concrete figure/table/data artifact path.",
            "Name concrete artifacts such as paper/figures/q2_backtest.png or paper/tables/q3_audit.tex.",
        )

    placeholder_hits = [term for term in PLACEHOLDER_TERMS if term.lower() in lower_text]
    if placeholder_hits:
        add(
            findings,
            "WARN",
            "Method Route Depth Gate",
            "method-depth-plan.md still contains placeholder terms: " + ", ".join(placeholder_hits),
            "Replace placeholders with route family, model role, result artifact, validation artifact, and depth.",
        )

    if "Method Route Verdict" not in method_text:
        add(
            findings,
            "WARN",
            "Method Route Depth Gate",
            "method-depth-plan.md has no Method Route Verdict draft section.",
            "Add the verdict draft so the final review can copy real evidence instead of improvising.",
        )


def extract_latex_environment(text: str, env_name: str) -> str:
    pattern = rf"\\begin\{{{re.escape(env_name)}\}}(.*?)\\end\{{{re.escape(env_name)}\}}"
    match = re.search(pattern, text, re.DOTALL)
    return match.group(1) if match else ""


def check_tex_source(tex_path: Path, findings: list[Finding]) -> None:
    if not tex_path.exists():
        add(
            findings,
            "WARN",
            "LaTeX Source Gate",
            f"LaTeX source was not found: {tex_path}",
            "Pass --tex or -Tex with the final paper/main.tex path when source checking is available.",
        )
        return

    text = tex_path.read_text(encoding="utf-8", errors="replace")
    abstract = extract_latex_environment(text, "abstract")

    if not abstract:
        add(
            findings,
            "FAIL",
            "Abstract Gate",
            f"No abstract environment was found in {tex_path}.",
            "Use a normal LaTeX abstract environment with paragraph-structured problem closures.",
        )
    else:
        bold_count = abstract.count(r"\textbf")
        if bold_count < 3:
            add(
                findings,
                "FAIL",
                "Abstract Gate",
                f"Only {bold_count} bold result expressions were found in the LaTeX abstract.",
                "Bold the key numerical or decision results for at least three major outputs when supported.",
            )

        missing_markers = [term for term in ABSTRACT_TERMS[1:] if term not in abstract]
        if missing_markers:
            add(
                findings,
                "FAIL",
                "Abstract Gate",
                "LaTeX abstract is missing markers: " + ", ".join(missing_markers),
                "Use problem-by-problem abstract paragraphs such as 针对问题一/二/三.",
            )

    for term in PROMPT_LEAK_TERMS:
        if term in text:
            add(
                findings,
                "FAIL",
                "Prompt-Language Leak Gate",
                f"LaTeX source contains internal workflow term: {term}",
                "Remove prompt-planning vocabulary from paper/main.tex and rewrite in contest-paper language.",
            )

    placeholder_hits = [pattern for pattern in TEX_PLACEHOLDER_PATTERNS if pattern in text]
    if placeholder_hits:
        add(
            findings,
            "FAIL",
            "Template Placeholder Gate",
            "LaTeX source still contains template placeholders: " + ", ".join(placeholder_hits[:8]),
            "Replace skeleton placeholders before compiling or handing off the paper.",
        )


def check_review_file(review_path: Path, findings: list[Finding]) -> None:
    if not review_path.exists():
        add(
            findings,
            "FAIL",
            "Review Verdict Gate",
            f"Review file was not found: {review_path}",
            "Create reviews/review-current.md or the active run review before handoff.",
        )
        return

    text = review_path.read_text(encoding="utf-8", errors="replace")
    required_sections = ["v1.5 Hard Gate Verdict", "Method Route Verdict"]
    missing_sections = [section for section in required_sections if section not in text]
    if missing_sections:
        add(
            findings,
            "FAIL",
            "Review Verdict Gate",
            "Review is missing sections: " + ", ".join(missing_sections),
            "Use the v1.5 review scaffold and fill both verdict tables.",
        )

    verdict_rows = [
        line for line in text.splitlines()
        if line.startswith("|") and ("Gate" in line or re.match(r"^\|\s*Q\d+", line))
    ]
    unknown_rows = [row for row in verdict_rows if "Unknown" in row]
    if unknown_rows:
        add(
            findings,
            "FAIL",
            "Review Verdict Gate",
            f"{len(unknown_rows)} verdict rows still contain Unknown.",
            "Replace every Unknown verdict with Pass or Fail and concrete evidence before handoff.",
        )

    pass_fail_rows = [
        line for line in text.splitlines()
        if line.startswith("|") and ("Pass" in line or "Fail" in line)
    ]
    if len(pass_fail_rows) < 3:
        add(
            findings,
            "FAIL",
            "Review Verdict Gate",
            "Review does not contain enough Pass/Fail verdict rows.",
            "Fill v1.5 Hard Gate Verdict and Method Route Verdict with real pass/fail decisions.",
        )

    if "reviews/pdf-v15-check.md" not in text:
        add(
            findings,
            "WARN",
            "Review Verdict Gate",
            "Review does not reference reviews/pdf-v15-check.md.",
            "Reference the executable PDF/source/run-file check evidence in the final review.",
        )


def write_report(out_path: Path, findings: list[Finding], metadata: dict[str, object]) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = [
        "# v1.5 PDF Quality Check",
        "",
        f"- PDF: `{metadata['pdf']}`",
        f"- Pages: {metadata['pages']}",
        f"- Page 1 extracted chars: {metadata['page1_chars']}",
        f"- Min pages target: {metadata['min_pages']}",
        f"- Min page 1 chars: {metadata['min_page1_chars']}",
        "",
        "## Findings",
        "",
    ]

    if findings:
        lines.append("| Level | Gate | Evidence | Repair |")
        lines.append("| --- | --- | --- | --- |")
        for item in findings:
            lines.append(
                f"| {item.level} | {item.gate} | {item.evidence} | {item.repair} |"
            )
    else:
        lines.append("No visible v1.5 PDF gate failures or warnings were detected.")

    counts = metadata.get("char_counts") or []
    if counts:
        lines.extend(["", "## Page Text Density", ""])
        lines.append(", ".join(f"p{idx + 1}:{count}" for idx, count in enumerate(counts)))

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check visible v1.5 PDF quality gates.")
    parser.add_argument("--pdf", default="paper/main.pdf", help="PDF path to inspect.")
    parser.add_argument("--out", default="reviews/pdf-v15-check.md", help="Markdown report path.")
    parser.add_argument("--run", default="", help="Optional run directory for run-file checks.")
    parser.add_argument("--tex", default="", help="Optional LaTeX source path for source-level checks.")
    parser.add_argument("--review", default="", help="Optional review markdown path for verdict checks.")
    parser.add_argument("--min-pages", type=int, default=25, help="Expected minimum page count.")
    parser.add_argument(
        "--min-page1-chars",
        type=int,
        default=900,
        help="Minimum extracted character count for the abstract/title page.",
    )
    parser.add_argument("--no-fail", action="store_true", help="Always exit 0 after writing report.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    pdf_path = Path(args.pdf)
    out_path = Path(args.out)

    if not pdf_path.exists():
        print(f"FAIL: PDF not found: {pdf_path}", file=sys.stderr)
        return 1

    findings, metadata = check_pdf(pdf_path, args.min_pages, args.min_page1_chars)
    if args.run:
        check_run_files(Path(args.run), findings)
    if args.tex:
        check_tex_source(Path(args.tex), findings)
    if args.review:
        check_review_file(Path(args.review), findings)
    write_report(out_path, findings, metadata)

    fails = sum(1 for item in findings if item.level == "FAIL")
    warns = sum(1 for item in findings if item.level == "WARN")
    print(f"v1.5 PDF check wrote {out_path}")
    print(f"Findings: {fails} fail, {warns} warn")

    if fails and not args.no_fail:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
