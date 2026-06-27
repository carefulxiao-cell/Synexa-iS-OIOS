#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Synexa Baseline Render Core V0.1

File:
    Synexa_Baseline_Render_Core_V0.1.py

Recommended Path:
    11-templates/renderers/Synexa_Baseline_Render_Core_V0.1.py

Level:
    Global baseline-class Markdown to HTML renderer.

Current First Application:
    DIC Baseline:
        input  = 04-domain-baselines/dic/Synexa_DIC_Baseline_V0.1.md
        output = 04-domain-baselines/dic/Synexa_DIC_Baseline_V0.1.html

Purpose:
    Render Synexa baseline-class Markdown master sources into readable HTML files.

Applies To:
    - Master SSOT reading versions
    - DIC Baseline
    - PCS files
    - SOP files
    - Skill files
    - Tool / Agent Registry files
    - Project workbench files
    - Experience Asset index files

Core Rules:
    1. Markdown is the factual master source.
    2. HTML is only a reading / checking output.
    3. This script must not rewrite factual content.
    4. Any content change must go back to the Markdown source.
    5. This V0.1 script is intentionally single-file for fast adoption.
    6. Future versions may split into:
       - Render Standard.md
       - Render Core.py
       - Config.yaml
       - Project / document wrapper.py

Maintainer:
    iS-Core / iS-Matrix
    Manus may execute and improve file engineering under iS-Core review.

Version:
    V0.1
"""

from __future__ import annotations

import argparse
import datetime as _dt
import html
import os
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple


DEFAULT_TITLE = "超智科技·数智协同基线 V0.1"
DEFAULT_SUBTITLE = "Synexa Digital-Intelligence Collaboration Baseline｜DIC Baseline"
DEFAULT_DOC_TYPE = "Domain / Operational Baseline"
DEFAULT_INPUT = "Synexa_DIC_Baseline_V0.1.md"
DEFAULT_OUTPUT = "Synexa_DIC_Baseline_V0.1.html"


# ---------------------------------------------------------------------
# Basic utilities
# ---------------------------------------------------------------------

def read_text(path: Path) -> str:
    """Read UTF-8 text from a Markdown source file."""
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    """Write UTF-8 text to an output file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def slugify(text: str, used: Optional[set] = None) -> str:
    """
    Create stable heading anchor IDs.

    Chinese characters are preserved.
    Unsafe punctuation is removed.
    Duplicate anchors receive numeric suffixes.
    """
    used = used if used is not None else set()

    raw = text.strip()
    raw = re.sub(r"[#`*_>\[\]{}]", "", raw)
    raw = raw.replace("｜", "-").replace("|", "-")
    raw = raw.replace("：", "-").replace(":", "-")
    raw = raw.replace(" ", "-")
    raw = re.sub(r"-+", "-", raw)
    raw = raw.strip("-")

    if not raw:
        raw = "section"

    raw = re.sub(r"[^\w\u4e00-\u9fff\-\.]", "", raw)

    candidate = raw
    index = 2
    while candidate in used:
        candidate = f"{raw}-{index}"
        index += 1

    used.add(candidate)
    return candidate


def is_table_separator(line: str) -> bool:
    """Detect a Markdown table separator line."""
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return False

    cells = [cell.strip() for cell in stripped.strip("|").split("|")]
    if not cells:
        return False

    return all(re.fullmatch(r":?-{3,}:?", cell or "") is not None for cell in cells)


def split_table_row(line: str) -> List[str]:
    """Split a Markdown table row into cells."""
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def render_inline(text: str) -> str:
    """
    Minimal inline Markdown rendering with escaping.

    Supported:
    - inline code
    - bold
    - italic
    - simple markdown links
    """
    escaped = html.escape(text)

    # Links: [text](url)
    escaped = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: f'<a href="{html.escape(m.group(2), quote=True)}">{m.group(1)}</a>',
        escaped,
    )

    # Inline code
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)

    # Bold
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)

    # Italic, conservative
    escaped = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", escaped)

    return escaped


# ---------------------------------------------------------------------
# Markdown renderer
# ---------------------------------------------------------------------

def parse_markdown(md_text: str) -> Tuple[str, List[Dict[str, str]], Dict[str, int]]:
    """
    Convert a controlled subset of Markdown into HTML.

    Supported:
    - headings
    - paragraphs
    - unordered and ordered lists
    - fenced code blocks
    - blockquotes
    - Markdown tables
    - horizontal rules

    Returns:
        body_html
        toc
        stats
    """
    lines = md_text.splitlines()
    used_ids = set()
    toc: List[Dict[str, str]] = []
    out: List[str] = []

    stats = {
        "headings": 0,
        "tables": 0,
        "code_blocks": 0,
        "paragraphs": 0,
        "lists": 0,
        "blockquotes": 0,
    }

    in_code = False
    code_lang = ""
    code_buffer: List[str] = []

    in_ul = False
    in_ol = False
    paragraph: List[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            text = " ".join(part.strip() for part in paragraph if part.strip())
            if text:
                out.append(f"<p>{render_inline(text)}</p>")
                stats["paragraphs"] += 1
            paragraph = []

    def close_lists() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    def flush_code() -> None:
        nonlocal code_buffer, code_lang
        code = "\n".join(code_buffer)
        lang_class = f" language-{html.escape(code_lang)}" if code_lang else ""
        out.append(
            f'<pre><code class="{lang_class}">{html.escape(code)}</code></pre>'
        )
        stats["code_blocks"] += 1
        code_buffer = []
        code_lang = ""

    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Fenced code block start / end
        fence_match = re.match(r"^```([A-Za-z0-9_\-]*)", stripped)
        if fence_match:
            if in_code:
                flush_code()
                in_code = False
            else:
                flush_paragraph()
                close_lists()
                in_code = True
                code_lang = fence_match.group(1) or ""
                code_buffer = []
            i += 1
            continue

        if in_code:
            code_buffer.append(line)
            i += 1
            continue

        # Blank line
        if stripped == "":
            flush_paragraph()
            close_lists()
            i += 1
            continue

        # Horizontal rule
        if re.fullmatch(r"[-*_]{3,}", stripped):
            flush_paragraph()
            close_lists()
            out.append("<hr>")
            i += 1
            continue

        # Markdown table
        if stripped.startswith("|") and stripped.endswith("|"):
            if i + 1 < len(lines) and is_table_separator(lines[i + 1]):
                flush_paragraph()
                close_lists()

                headers = split_table_row(lines[i])
                i += 2

                rows: List[List[str]] = []
                while i < len(lines):
                    row_line = lines[i].strip()
                    if row_line.startswith("|") and row_line.endswith("|"):
                        rows.append(split_table_row(row_line))
                        i += 1
                    else:
                        break

                out.append('<div class="table-wrap"><table>')
                out.append("<thead><tr>")
                for header in headers:
                    out.append(f"<th>{render_inline(header)}</th>")
                out.append("</tr></thead>")

                out.append("<tbody>")
                for row in rows:
                    out.append("<tr>")
                    for cell in row:
                        out.append(f"<td>{render_inline(cell)}</td>")
                    out.append("</tr>")
                out.append("</tbody>")
                out.append("</table></div>")

                stats["tables"] += 1
                continue

        # Heading
        heading_match = re.match(r"^(#{1,6})\s+(.*)$", line)
        if heading_match:
            flush_paragraph()
            close_lists()

            level = len(heading_match.group(1))
            title = heading_match.group(2).strip()
            anchor = slugify(title, used_ids)

            toc.append(
                {
                    "level": str(level),
                    "title": title,
                    "anchor": anchor,
                }
            )

            out.append(
                f'<h{level} id="{anchor}">'
                f'<a class="anchor" href="#{anchor}">#</a> '
                f"{render_inline(title)}</h{level}>"
            )

            stats["headings"] += 1
            i += 1
            continue

        # Blockquote
        if stripped.startswith(">"):
            flush_paragraph()
            close_lists()
            quote = stripped.lstrip(">").strip()
            out.append(f"<blockquote>{render_inline(quote)}</blockquote>")
            stats["blockquotes"] += 1
            i += 1
            continue

        # Unordered list
        ul_match = re.match(r"^[-*+]\s+(.*)$", stripped)
        if ul_match:
            flush_paragraph()
            if in_ol:
                out.append("</ol>")
                in_ol = False
            if not in_ul:
                out.append("<ul>")
                in_ul = True
                stats["lists"] += 1
            out.append(f"<li>{render_inline(ul_match.group(1))}</li>")
            i += 1
            continue

        # Ordered list
        ol_match = re.match(r"^\d+\.\s+(.*)$", stripped)
        if ol_match:
            flush_paragraph()
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if not in_ol:
                out.append("<ol>")
                in_ol = True
                stats["lists"] += 1
            out.append(f"<li>{render_inline(ol_match.group(1))}</li>")
            i += 1
            continue

        # Normal paragraph
        paragraph.append(line)
        i += 1

    if in_code:
        flush_code()

    flush_paragraph()
    close_lists()

    return "\n".join(out), toc, stats


# ---------------------------------------------------------------------
# HTML template
# ---------------------------------------------------------------------

def build_toc(toc: List[Dict[str, str]], max_level: int = 3) -> str:
    """Build a table of contents."""
    if not toc:
        return ""

    items: List[str] = []
    for item in toc:
        level = int(item["level"])
        if level > max_level:
            continue

        cls = f"toc-l{level}"
        title = html.escape(item["title"])
        anchor = html.escape(item["anchor"])
        items.append(f'<a class="{cls}" href="#{anchor}">{title}</a>')

    return "\n".join(items)


def default_css() -> str:
    """Global Synexa baseline reading style."""
    return """
:root {
  --bg: #f7f7f4;
  --paper: #ffffff;
  --ink: #1d1d1f;
  --muted: #6b6b6f;
  --line: #e7e3dc;
  --accent: #8a5a44;
  --accent-deep: #5a392b;
  --accent-soft: #f1e8df;
  --code-bg: #1f2430;
  --code-ink: #f3f4f6;
  --table-head: #f5efe8;
  --shadow: 0 10px 30px rgba(0,0,0,0.055);
}

* {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font-family:
    -apple-system,
    BlinkMacSystemFont,
    "Segoe UI",
    "PingFang SC",
    "Hiragino Sans GB",
    "Microsoft YaHei",
    Arial,
    sans-serif;
  line-height: 1.75;
  font-size: 16px;
}

.layout {
  display: grid;
  grid-template-columns: 310px minmax(0, 1fr);
  min-height: 100vh;
}

.sidebar {
  position: sticky;
  top: 0;
  height: 100vh;
  overflow: auto;
  padding: 28px 22px;
  background: #fbfaf7;
  border-right: 1px solid var(--line);
}

.sidebar .brand {
  font-size: 13px;
  color: var(--accent);
  letter-spacing: .08em;
  text-transform: uppercase;
  margin-bottom: 10px;
  font-weight: 700;
}

.sidebar h1 {
  font-size: 20px;
  line-height: 1.35;
  margin: 0 0 8px 0;
}

.sidebar .subtitle {
  font-size: 13px;
  color: var(--muted);
  margin-bottom: 22px;
}

.toc {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.toc a {
  color: #3b3b3f;
  text-decoration: none;
  border-radius: 8px;
  padding: 5px 8px;
  font-size: 13px;
  line-height: 1.35;
}

.toc a:hover {
  background: var(--accent-soft);
  color: var(--accent);
}

.toc-l1 {
  font-weight: 700;
  margin-top: 10px;
}

.toc-l2 {
  padding-left: 18px !important;
}

.toc-l3 {
  padding-left: 32px !important;
  color: var(--muted) !important;
}

.main {
  padding: 48px 56px 80px;
}

.paper {
  max-width: 1120px;
  margin: 0 auto;
  background: var(--paper);
  box-shadow: var(--shadow);
  border: 1px solid var(--line);
  border-radius: 20px;
  padding: 56px 68px;
}

.cover {
  border-bottom: 1px solid var(--line);
  margin-bottom: 36px;
  padding-bottom: 28px;
}

.cover .kicker {
  color: var(--accent);
  font-weight: 800;
  letter-spacing: .08em;
  text-transform: uppercase;
  font-size: 13px;
}

.cover h1 {
  margin: 8px 0 6px;
  font-size: 34px;
  line-height: 1.2;
}

.cover .subtitle {
  color: var(--muted);
  font-size: 17px;
}

.cover .meta {
  margin-top: 18px;
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.badge {
  display: inline-block;
  padding: 4px 10px;
  border-radius: 999px;
  background: var(--accent-soft);
  color: var(--accent-deep);
  font-size: 12px;
  font-weight: 700;
}

.notice {
  margin-top: 18px;
  padding: 14px 16px;
  background: #fff8ea;
  border: 1px solid #ead9aa;
  border-radius: 12px;
  color: #5c4822;
}

.stats {
  margin-top: 14px;
  color: var(--muted);
  font-size: 13px;
}

h1, h2, h3, h4, h5, h6 {
  line-height: 1.35;
  margin-top: 1.7em;
  margin-bottom: .65em;
  color: #151515;
}

h1 {
  font-size: 30px;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--line);
}

h2 {
  font-size: 24px;
}

h3 {
  font-size: 20px;
}

h4 {
  font-size: 17px;
}

p {
  margin: .75em 0;
}

a {
  color: var(--accent-deep);
}

a.anchor {
  text-decoration: none;
  color: #c9b7aa;
  font-weight: 400;
  margin-right: 2px;
}

a.anchor:hover {
  color: var(--accent);
}

blockquote {
  margin: 20px 0;
  padding: 14px 18px;
  border-left: 4px solid var(--accent);
  background: var(--accent-soft);
  color: #3d332d;
  border-radius: 0 10px 10px 0;
}

code {
  font-family:
    "SFMono-Regular",
    Consolas,
    "Liberation Mono",
    Menlo,
    monospace;
  background: #f0eee9;
  color: #3b2c24;
  padding: 2px 5px;
  border-radius: 5px;
  font-size: .92em;
}

pre {
  background: var(--code-bg);
  color: var(--code-ink);
  padding: 18px 20px;
  border-radius: 14px;
  overflow: auto;
  line-height: 1.55;
  margin: 20px 0;
}

pre code {
  background: transparent;
  color: inherit;
  padding: 0;
}

.table-wrap {
  width: 100%;
  overflow-x: auto;
  margin: 20px 0 26px;
  border: 1px solid var(--line);
  border-radius: 14px;
}

table {
  border-collapse: collapse;
  width: 100%;
  min-width: 720px;
  background: #fff;
}

th, td {
  padding: 10px 12px;
  border-bottom: 1px solid var(--line);
  border-right: 1px solid var(--line);
  text-align: left;
  vertical-align: top;
}

th:last-child, td:last-child {
  border-right: 0;
}

tr:last-child td {
  border-bottom: 0;
}

thead th {
  background: var(--table-head);
  color: #2d241f;
  font-weight: 700;
}

ul, ol {
  padding-left: 1.45em;
}

li {
  margin: .25em 0;
}

hr {
  border: 0;
  border-top: 1px solid var(--line);
  margin: 34px 0;
}

.footer {
  margin-top: 52px;
  padding-top: 24px;
  border-top: 1px solid var(--line);
  color: var(--muted);
  font-size: 13px;
}

@media print {
  .sidebar {
    display: none;
  }

  .layout {
    display: block;
  }

  .main {
    padding: 0;
  }

  .paper {
    box-shadow: none;
    border: 0;
    max-width: none;
    padding: 24px;
  }
}

@media (max-width: 980px) {
  .layout {
    grid-template-columns: 1fr;
  }

  .sidebar {
    position: relative;
    height: auto;
    border-right: 0;
    border-bottom: 1px solid var(--line);
  }

  .main {
    padding: 24px 16px 48px;
  }

  .paper {
    padding: 32px 22px;
    border-radius: 14px;
  }

  .cover h1 {
    font-size: 26px;
  }
}
"""


def build_html(
    body_html: str,
    toc: List[Dict[str, str]],
    stats: Dict[str, int],
    title: str,
    subtitle: str,
    doc_type: str,
    version: str,
    status: str,
    source_file: str,
    output_file: str,
) -> str:
    """Build final HTML document."""
    rendered_at = _dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    toc_html = build_toc(toc)

    stats_text = (
        f"Headings: {stats.get('headings', 0)} · "
        f"Tables: {stats.get('tables', 0)} · "
        f"Code Blocks: {stats.get('code_blocks', 0)} · "
        f"Paragraphs: {stats.get('paragraphs', 0)}"
    )

    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <style>
{default_css()}
  </style>
</head>
<body>
  <div class="layout">
    <aside class="sidebar">
      <div class="brand">Synexa Baseline Renderer</div>
      <h1>{html.escape(title)}</h1>
      <div class="subtitle">{html.escape(subtitle)}</div>
      <nav class="toc">
        {toc_html}
      </nav>
    </aside>

    <main class="main">
      <article class="paper">
        <section class="cover">
          <div class="kicker">{html.escape(doc_type)}</div>
          <h1>{html.escape(title)}</h1>
          <div class="subtitle">{html.escape(subtitle)}</div>
          <div class="meta">
            <span class="badge">{html.escape(version)}</span>
            <span class="badge">{html.escape(status)}</span>
            <span class="badge">Markdown → HTML</span>
            <span class="badge">Source: {html.escape(os.path.basename(source_file))}</span>
          </div>
          <div class="notice">
            本 HTML 为阅读版 / 检查版，不是事实主源。事实性修改必须回到 Markdown 主源：
            <strong>{html.escape(os.path.basename(source_file))}</strong>
          </div>
          <div class="stats">{html.escape(stats_text)}</div>
        </section>

        {body_html}

        <footer class="footer">
          <p>Rendered at: {html.escape(rendered_at)}</p>
          <p>Source file: {html.escape(source_file)}</p>
          <p>Output file: {html.escape(output_file)}</p>
          <p>Renderer: Synexa_Baseline_Render_Core_V0.1.py</p>
          <p>Rule: Markdown is the factual master source. HTML is a reading output.</p>
        </footer>
      </article>
    </main>
  </div>
</body>
</html>
"""


# ---------------------------------------------------------------------
# Rendering entry
# ---------------------------------------------------------------------

def render(
    input_path: Path,
    output_path: Path,
    title: str,
    subtitle: str,
    doc_type: str,
    version: str,
    status: str,
) -> None:
    """Render Markdown to HTML."""
    md_text = read_text(input_path)
    body_html, toc, stats = parse_markdown(md_text)

    final_html = build_html(
        body_html=body_html,
        toc=toc,
        stats=stats,
        title=title,
        subtitle=subtitle,
        doc_type=doc_type,
        version=version,
        status=status,
        source_file=str(input_path),
        output_file=str(output_path),
    )

    write_text(output_path, final_html)


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(
        description="Render Synexa baseline-class Markdown master source to HTML."
    )

    parser.add_argument(
        "--input",
        "-i",
        default=DEFAULT_INPUT,
        help=f"Markdown input file. Default: {DEFAULT_INPUT}",
    )

    parser.add_argument(
        "--output",
        "-o",
        default=DEFAULT_OUTPUT,
        help=f"HTML output file. Default: {DEFAULT_OUTPUT}",
    )

    parser.add_argument(
        "--title",
        default=DEFAULT_TITLE,
        help=f"Document title. Default: {DEFAULT_TITLE}",
    )

    parser.add_argument(
        "--subtitle",
        default=DEFAULT_SUBTITLE,
        help=f"Document subtitle. Default: {DEFAULT_SUBTITLE}",
    )

    parser.add_argument(
        "--doc-type",
        default=DEFAULT_DOC_TYPE,
        help=f"Document type. Default: {DEFAULT_DOC_TYPE}",
    )

    parser.add_argument(
        "--version",
        default="V0.1",
        help="Document version. Default: V0.1",
    )

    parser.add_argument(
        "--status",
        default="Working Draft",
        help="Document status. Default: Working Draft",
    )

    return parser.parse_args()


def main() -> None:
    """CLI entry point."""
    args = parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    render(
        input_path=input_path,
        output_path=output_path,
        title=args.title,
        subtitle=args.subtitle,
        doc_type=args.doc_type,
        version=args.version,
        status=args.status,
    )

    print("Synexa baseline render completed.")
    print(f"Input : {input_path}")
    print(f"Output: {output_path}")
    print("Renderer level: Global baseline-class renderer V0.1")
    print("Reminder: HTML is a reading output. Markdown remains the factual master source.")


if __name__ == "__main__":
    main()