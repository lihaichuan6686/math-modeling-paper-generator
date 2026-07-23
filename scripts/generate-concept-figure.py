"""Generate a code-native concept/mechanism figure from a small JSON spec.

This helper is for schematic figures only. It must not be used to invent
numeric evidence or validation charts.
"""

from __future__ import annotations

import argparse
import html
import json
import textwrap
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Zone:
    id: str
    title: str


@dataclass
class Node:
    id: str
    label: str
    zone: str
    highlight: bool = False


@dataclass
class Edge:
    source: str
    target: str
    label: str = ""


DEFAULT_SPEC = {
    "title": "CUMCM model route concept figure",
    "subtitle": "schematic only; numeric evidence must come from code outputs",
    "zones": [
        {"id": "data", "title": "Data objects"},
        {"id": "model", "title": "Model chain"},
        {"id": "result", "title": "Result artifacts"},
        {"id": "review", "title": "Validation"},
    ],
    "nodes": [
        {"id": "input", "zone": "data", "label": "Problem data"},
        {"id": "features", "zone": "data", "label": "Derived variables"},
        {"id": "diagnosis", "zone": "model", "label": "Support diagnosis"},
        {"id": "main_model", "zone": "model", "label": "Main model"},
        {"id": "answer", "zone": "result", "label": "Answer table", "highlight": True},
        {"id": "figure", "zone": "result", "label": "Result figure"},
        {"id": "check", "zone": "review", "label": "Sensitivity check", "highlight": True},
    ],
    "edges": [
        {"source": "input", "target": "features", "label": "clean"},
        {"source": "features", "target": "diagnosis", "label": "screen"},
        {"source": "diagnosis", "target": "main_model", "label": "formulate"},
        {"source": "main_model", "target": "answer", "label": "solve"},
        {"source": "main_model", "target": "figure", "label": "visualize"},
        {"source": "answer", "target": "check", "label": "verify"},
        {"source": "figure", "target": "check", "label": "compare"},
    ],
    "palette": {
        "background": "#ffffff",
        "zone": "#f5f7fb",
        "node": "#ffffff",
        "highlight": "#e8f4ff",
        "edge": "#58606f",
        "accent": "#2f6f9f",
        "text": "#1f2430",
    },
}


def read_spec(path: Path | None) -> dict:
    if path is None:
        return DEFAULT_SPEC
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def as_zones(spec: dict) -> list[Zone]:
    return [Zone(id=str(item["id"]), title=str(item["title"])) for item in spec["zones"]]


def as_nodes(spec: dict) -> list[Node]:
    return [
        Node(
            id=str(item["id"]),
            zone=str(item["zone"]),
            label=str(item["label"]),
            highlight=bool(item.get("highlight", False)),
        )
        for item in spec["nodes"]
    ]


def as_edges(spec: dict) -> list[Edge]:
    return [
        Edge(
            source=str(item["source"]),
            target=str(item["target"]),
            label=str(item.get("label", "")),
        )
        for item in spec.get("edges", [])
    ]


def wrap_label(label: str, width: int = 18) -> str:
    return "\n".join(textwrap.wrap(label, width=width, break_long_words=False)) or label


def draw(spec: dict, output: Path) -> None:
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

    zones = as_zones(spec)
    nodes = as_nodes(spec)
    edges = as_edges(spec)
    palette = DEFAULT_SPEC["palette"] | spec.get("palette", {})

    zone_index = {zone.id: idx for idx, zone in enumerate(zones)}
    zone_nodes: dict[str, list[Node]] = {zone.id: [] for zone in zones}
    for node in nodes:
        if node.zone not in zone_nodes:
            raise ValueError(f"Node {node.id} references unknown zone {node.zone}")
        zone_nodes[node.zone].append(node)

    fig_width = max(12.0, 3.1 * len(zones))
    fig_height = 7.0
    fig, ax = plt.subplots(figsize=(fig_width, fig_height), dpi=220)
    fig.patch.set_facecolor(palette["background"])
    ax.set_facecolor(palette["background"])
    ax.set_xlim(0, len(zones))
    ax.set_ylim(0, 1)
    ax.axis("off")

    title = str(spec.get("title", "Concept figure"))
    subtitle = str(spec.get("subtitle", ""))
    ax.text(0.02, 0.965, title, fontsize=18, weight="bold", color=palette["text"], transform=ax.transAxes)
    if subtitle:
        ax.text(0.02, 0.925, subtitle, fontsize=9, color=palette["edge"], transform=ax.transAxes)

    node_positions: dict[str, tuple[float, float]] = {}
    for zone in zones:
        idx = zone_index[zone.id]
        x0 = idx + 0.08
        width = 0.84
        zone_box = FancyBboxPatch(
            (x0, 0.11),
            width,
            0.72,
            boxstyle="round,pad=0.014,rounding_size=0.02",
            linewidth=1.1,
            edgecolor="#d8dde8",
            facecolor=palette["zone"],
            linestyle="--",
        )
        ax.add_patch(zone_box)
        ax.text(idx + 0.5, 0.79, zone.title, ha="center", va="center", fontsize=11, weight="bold", color=palette["text"])

        items = zone_nodes[zone.id]
        count = max(1, len(items))
        for item_index, node in enumerate(items):
            y = 0.66 - item_index * min(0.18, 0.48 / count)
            x = idx + 0.5
            node_positions[node.id] = (x, y)
            facecolor = palette["highlight"] if node.highlight else palette["node"]
            edgecolor = palette["accent"] if node.highlight else "#c9d0dc"
            node_box = FancyBboxPatch(
                (x - 0.31, y - 0.052),
                0.62,
                0.104,
                boxstyle="round,pad=0.018,rounding_size=0.025",
                linewidth=1.2,
                edgecolor=edgecolor,
                facecolor=facecolor,
            )
            ax.add_patch(node_box)
            ax.text(x, y, wrap_label(node.label), ha="center", va="center", fontsize=8.6, color=palette["text"])

    for edge in edges:
        if edge.source not in node_positions or edge.target not in node_positions:
            raise ValueError(f"Edge {edge.source}->{edge.target} references unknown node")
        start = node_positions[edge.source]
        end = node_positions[edge.target]
        patch = FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=12,
            linewidth=1.2,
            color=palette["edge"],
            connectionstyle="arc3,rad=0.05",
            shrinkA=22,
            shrinkB=22,
        )
        ax.add_patch(patch)
        if edge.label:
            lx = (start[0] + end[0]) / 2
            ly = (start[1] + end[1]) / 2 + 0.035
            ax.text(lx, ly, edge.label, ha="center", va="center", fontsize=7.5, color=palette["accent"])

    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, bbox_inches="tight", pad_inches=0.08)
    plt.close(fig)


def draw_svg(spec: dict, output: Path) -> None:
    zones = as_zones(spec)
    nodes = as_nodes(spec)
    edges = as_edges(spec)
    palette = DEFAULT_SPEC["palette"] | spec.get("palette", {})

    zone_nodes: dict[str, list[Node]] = {zone.id: [] for zone in zones}
    for node in nodes:
        if node.zone not in zone_nodes:
            raise ValueError(f"Node {node.id} references unknown zone {node.zone}")
        zone_nodes[node.zone].append(node)

    width = max(1200, 320 * len(zones))
    height = 680
    margin = 40
    zone_gap = 24
    zone_width = (width - margin * 2 - zone_gap * (len(zones) - 1)) / max(1, len(zones))
    node_positions: dict[str, tuple[float, float]] = {}
    parts: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        f'<rect width="100%" height="100%" fill="{palette["background"]}"/>',
        "<defs>",
        '<marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">',
        f'<path d="M0,0 L0,6 L9,3 z" fill="{palette["edge"]}"/>',
        "</marker>",
        "</defs>",
        f'<text x="36" y="44" font-family="Arial, sans-serif" font-size="24" font-weight="700" fill="{palette["text"]}">{html.escape(str(spec.get("title", "Concept figure")))}</text>',
    ]
    subtitle = str(spec.get("subtitle", ""))
    if subtitle:
        parts.append(
            f'<text x="36" y="72" font-family="Arial, sans-serif" font-size="13" fill="{palette["edge"]}">{html.escape(subtitle)}</text>'
        )

    for zone_index, zone in enumerate(zones):
        x = margin + zone_index * (zone_width + zone_gap)
        parts.append(
            f'<rect x="{x:.1f}" y="110" width="{zone_width:.1f}" height="500" rx="18" '
            f'fill="{palette["zone"]}" stroke="#d8dde8" stroke-width="2" stroke-dasharray="8 6"/>'
        )
        parts.append(
            f'<text x="{x + zone_width / 2:.1f}" y="148" text-anchor="middle" font-family="Arial, sans-serif" '
            f'font-size="17" font-weight="700" fill="{palette["text"]}">{html.escape(zone.title)}</text>'
        )
        items = zone_nodes[zone.id]
        for item_index, node in enumerate(items):
            nx = x + zone_width / 2
            ny = 220 + item_index * min(120, 330 / max(1, len(items)))
            node_positions[node.id] = (nx, ny)
            fill = palette["highlight"] if node.highlight else palette["node"]
            stroke = palette["accent"] if node.highlight else "#c9d0dc"
            parts.append(
                f'<rect x="{nx - 105:.1f}" y="{ny - 34:.1f}" width="210" height="68" rx="16" '
                f'fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
            )
            lines = textwrap.wrap(node.label, width=20, break_long_words=False) or [node.label]
            line_start = ny - (len(lines) - 1) * 8
            for line_index, line in enumerate(lines[:3]):
                parts.append(
                    f'<text x="{nx:.1f}" y="{line_start + line_index * 17:.1f}" text-anchor="middle" '
                    f'font-family="Arial, sans-serif" font-size="13" fill="{palette["text"]}">{html.escape(line)}</text>'
                )

    for edge in edges:
        if edge.source not in node_positions or edge.target not in node_positions:
            raise ValueError(f"Edge {edge.source}->{edge.target} references unknown node")
        sx, sy = node_positions[edge.source]
        tx, ty = node_positions[edge.target]
        parts.append(
            f'<line x1="{sx:.1f}" y1="{sy:.1f}" x2="{tx:.1f}" y2="{ty:.1f}" '
            f'stroke="{palette["edge"]}" stroke-width="2" marker-end="url(#arrow)" opacity="0.9"/>'
        )
        if edge.label:
            parts.append(
                f'<text x="{(sx + tx) / 2:.1f}" y="{(sy + ty) / 2 - 10:.1f}" text-anchor="middle" '
                f'font-family="Arial, sans-serif" font-size="12" fill="{palette["accent"]}">{html.escape(edge.label)}</text>'
            )

    parts.append("</svg>")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(parts), encoding="utf-8")


def write_example(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(DEFAULT_SPEC, handle, ensure_ascii=False, indent=2)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate a schematic concept figure from JSON. Keep runs/current/figure-style-spec.md synchronized."
    )
    parser.add_argument("--spec", type=Path, help="JSON figure specification.")
    parser.add_argument("--out", type=Path, default=Path("paper/figures/concept_route.png"))
    parser.add_argument("--write-example", type=Path, help="Write an example JSON spec and exit.")
    args = parser.parse_args()

    if args.write_example:
        write_example(args.write_example)
        return 0

    spec = read_spec(args.spec)
    if args.out.suffix.lower() == ".svg":
        draw_svg(spec, args.out)
    else:
        draw(spec, args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
