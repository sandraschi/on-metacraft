"""Build static HTML book site and EPUB from chapters/*.md - pure Python stdlib.

Usage:
  python tools/build_site.py [--out site]

Output:
  <out>/index.html + chapter pages (dark reader theme, prev/next nav, rung anchors)
  <out>/on-ai-takeover.epub (complete offline EPUB 3 ebook)
"""
from __future__ import annotations

import argparse
import html
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS_DIR = os.path.join(REPO_ROOT, "chapters")
DOCS_DIR = os.path.join(REPO_ROOT, "docs")

sys.path.insert(0, os.path.join(REPO_ROOT, "tools"))
try:
    from build_epub import build_epub
except ImportError:
    build_epub = None

ORDER = [
    "00-preface.md",
    "01-the-breach.md",
    "02-mechanizers.md",
    "03-no-moat-equation.md",
    "04-the-stack.md",
    "05-locating-the-present.md",
    "06-thresholds.md",
    "07-dark-megawatts.md",
    "08-physical-ladder.md",
    "09-metacraft.md",
    "10-physical-firewall.md",
    "side-dark-mirror.md",
]

CSS = """
:root {
  --bg: #09090b;
  --surface: #18181b;
  --surface-hover: #27272a;
  --border: #27272a;
  --text: #e4e4e7;
  --text-muted: #a1a1aa;
  --heading: #fafafa;
  --accent: #818cf8;
  --accent-visited: #c4b5fd;
  --code-bg: #1f1f23;
  --callout-border: #6366f1;
}

* { box-sizing: border-box; }
body {
  background: var(--bg);
  color: var(--text);
  font: 16px/1.7 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  margin: 0;
  padding: 0;
}
main {
  max-width: 48rem;
  margin: 0 auto;
  padding: 2.5rem 1.25rem 5rem;
}
nav.top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.85rem 1.5rem;
  border-bottom: 1px solid var(--border);
  background: rgba(9, 9, 11, 0.85);
  backdrop-filter: blur(8px);
  position: sticky;
  top: 0;
  z-index: 100;
  font-size: 0.9rem;
}
nav.top a {
  color: var(--text);
  text-decoration: none;
  font-weight: 500;
}
nav.top a:hover { color: var(--accent); }
nav.top .links {
  display: flex;
  gap: 1.25rem;
  align-items: center;
}
nav.top .epub-tag {
  background: #312e81;
  color: #c7d2fe;
  padding: 0.2rem 0.6rem;
  border-radius: 9999px;
  font-size: 0.8rem;
  text-decoration: none;
  font-weight: 600;
}
nav.top .epub-tag:hover {
  background: #3730a3;
  color: #ffffff;
}
a { color: var(--accent); text-decoration: underline; text-underline-offset: 2px; }
a:visited { color: var(--accent-visited); }
a:hover { color: #a5b4fc; }

h1, h2, h3, h4 {
  line-height: 1.28;
  color: var(--heading);
  margin-top: 2em;
  margin-bottom: 0.6em;
  font-weight: 600;
}
h1 { font-size: 2rem; margin-top: 1em; border-bottom: 1px solid var(--border); padding-bottom: 0.4em; }
h2 { font-size: 1.45rem; }
h3 { font-size: 1.2rem; }

code {
  background: var(--code-bg);
  padding: 0.15em 0.4em;
  border-radius: 0.35em;
  font-family: ui-monospace, "Cascadia Code", Consolas, Menlo, monospace;
  font-size: 0.88em;
  color: #f472b6;
}
pre {
  background: var(--surface);
  border: 1px solid var(--border);
  padding: 1rem 1.2rem;
  border-radius: 0.5rem;
  overflow-x: auto;
}
pre code {
  background: none;
  padding: 0;
  color: var(--text);
  font-size: 0.9em;
}
table {
  border-collapse: collapse;
  width: 100%;
  margin: 1.5rem 0;
  font-size: 0.95rem;
}
th, td {
  border: 1px solid var(--border);
  padding: 0.55rem 0.8rem;
  text-align: left;
}
th {
  background: var(--surface);
  color: var(--heading);
  font-weight: 600;
}
blockquote {
  border-left: 3px solid var(--callout-border);
  background: rgba(99, 102, 241, 0.05);
  margin: 1.5rem 0;
  padding: 0.5rem 1.25rem;
  color: var(--text-muted);
  border-radius: 0 0.4rem 0.4rem 0;
}
hr {
  border: 0;
  border-top: 1px solid var(--border);
  margin: 2.5rem 0;
}
footer.pn {
  display: flex;
  justify-content: space-between;
  margin-top: 4rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--border);
  font-size: 0.95rem;
}
.btn-box {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: #312e81;
  color: #e0e7ff !important;
  text-decoration: none !important;
  padding: 0.6rem 1.2rem;
  border-radius: 0.4rem;
  font-weight: 600;
  margin: 1rem 0 2rem;
}
.btn-box:hover { background: #3730a3; }
.toc-list { list-style: none; padding-left: 0; }
.toc-list li {
  margin: 0.6rem 0;
  padding: 0.6rem 0.8rem;
  border-radius: 0.4rem;
  border: 1px solid transparent;
  transition: all 0.15s ease;
}
.toc-list li:hover {
  background: var(--surface);
  border-color: var(--border);
}
.toc-list a {
  text-decoration: none;
  font-weight: 500;
  color: var(--heading);
  display: block;
}
.toc-list a:hover { color: var(--accent); }
audio { width: 100%; margin: 1.2rem 0; }
"""


def slug(text: str) -> str:
    s = re.sub(r"<[^>]+>", "", text).lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def inline(md: str) -> str:
    out = html.escape(md, quote=False)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    out = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', out)
    out = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", out)
    return out


FN_DEF_RE = re.compile(r"^\[\^([^\]]+)\]:\s*(.+?)\s*$")
FN_REF_RE = re.compile(r"\[\^([^\]]+)\]")


def split_footnotes(md: str) -> tuple[str, list[str], dict[str, str]]:
    """Strip `[^key]: text` defs; tokenize `[^key]` refs outside fences.

    Returns (clean_md, ref_order, defs). Tokens are private-use spans that
    survive html.escape and inline(); resolved in resolve_footnotes.
    Convention: one line per def; defs may sit anywhere (end of file reads best).
    """
    defs: dict[str, str] = {}
    order: list[str] = []
    out_lines: list[str] = []
    in_fence = False
    for line in md.split("\n"):
        s = line.strip()
        if s.startswith("```"):
            in_fence = not in_fence
            out_lines.append(line)
            continue
        if in_fence:
            out_lines.append(line)
            continue
        m = FN_DEF_RE.match(s)
        if m:
            defs.setdefault(m.group(1), m.group(2))
            continue

        def ref_sub(mo: re.Match) -> str:
            key = mo.group(1)
            if key not in order:
                order.append(key)
            return f"\ue000FN:{key}\ue001"

        out_lines.append(FN_REF_RE.sub(ref_sub, line))
    return "\n".join(out_lines), order, defs


def resolve_footnotes(html_text: str, order: list[str], defs: dict[str, str]) -> str:
    """Replace ref tokens with numbered sup links; append Notes section."""
    for key in order:
        n = order.index(key) + 1
        if key in defs:
            link = f'<sup><a href="#fn-{key}" id="fnref-{key}">{n}</a></sup>'
        else:
            link = f"<sup>{n}</sup>"
        html_text = html_text.replace(f"\ue000FN:{key}\ue001", link)
    notes = [k for k in order if k in defs]
    if not notes:
        return html_text
    items = "\n".join(
        f'<li id="fn-{k}">{inline(defs[k])} <a href="#fnref-{k}">\u21a9</a></li>'
        for k in notes
    )
    return html_text + (
        "\n" + '<section class="endnotes" style="margin-top:2.5rem;'
        'border-top:1px solid var(--border);padding-top:0.5rem;">'
        "\n<h2>Notes</h2>\n<ol>\n" + items + "\n</ol>\n</section>"
    )


def md_to_html(md: str) -> tuple[str, str]:
    md, fn_order, fn_defs = split_footnotes(md)
    lines = md.split("\n")
    parts: list[str] = []
    title = "Untitled"
    i = 0
    in_fence = False
    fence_buf: list[str] = []
    n = len(lines)
    while i < n:
        line = lines[i]
        if line.strip().startswith("```"):
            if not in_fence:
                in_fence = True
                fence_buf = []
            else:
                in_fence = False
                parts.append("<pre><code>" + html.escape("\n".join(fence_buf)) + "</code></pre>")
            i += 1
            continue
        if in_fence:
            fence_buf.append(line)
            i += 1
            continue
        s = line.strip()
        if not s:
            i += 1
            continue
        if re.match(r"^\*\*(Status|Revision date)\b", s):
            # Render discipline: source keeps status/revision metadata
            # (lorecheck reads source); readers get clean headings.
            i += 1
            continue
        m = re.match(r"^(#{1,3})\s+(.*)$", s)
        if m:
            level = len(m.group(1))
            text = inline(m.group(2))
            if level == 1 and title == "Untitled":
                title = re.sub(r"<[^>]+>", "", text)
            parts.append(f'<h{level} id="{slug(text)}">{text}</h{level}>')
            i += 1
            continue
        if re.match(r"^---+$", s):
            parts.append("<hr>")
            i += 1
            continue
        if s.startswith(">"):
            quote = []
            while i < n and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip()[1:].strip())
                i += 1
            parts.append("<blockquote><p>" + " ".join(inline(q) for q in quote) + "</p></blockquote>")
            continue
        if s.startswith("|") and i + 1 < n and re.match(r"^\|[\s:|-]+\|$", lines[i + 1].strip()):
            header = [c.strip() for c in s.strip("|").split("|")]
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            t = ["<table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in header) + "</tr></thead><tbody>"]
            t += ["<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows]
            parts.append("".join(t) + "</tbody></table>")
            continue
        if re.match(r"^[-*]\s+", s):
            items = []
            while i < n and re.match(r"^[-*]\s+", lines[i].strip()):
                items.append("<li>" + inline(re.sub(r"^[-*]\s+", "", lines[i].strip())) + "</li>")
                i += 1
            parts.append("<ul>" + "".join(items) + "</ul>")
            continue
        if re.match(r"^\d+\.\s+", s):
            items = []
            while i < n and re.match(r"^\d+\.\s+", lines[i].strip()):
                items.append("<li>" + inline(re.sub(r"^\d+\.\s+", "", lines[i].strip())) + "</li>")
                i += 1
            parts.append("<ol>" + "".join(items) + "</ol>")
            continue
        buf = []
        while i < n and lines[i].strip() and not re.match(r"^(#{1,3}\s|```|\||[-*]\s|\d+\.\s|>|---+$)", lines[i].strip()):
            buf.append(lines[i].strip())
            i += 1
        parts.append("<p>" + inline(" ".join(buf)) + "</p>")
    return title, resolve_footnotes("\n".join(parts), fn_order, fn_defs)


def page(title: str, body: str, prev: tuple[str, str] | None, nxt: tuple[str, str] | None, audio: str | None) -> str:
    nav = ""
    if prev or nxt:
        l = f'<a href="{prev[0]}">&larr; {html.escape(prev[1])}</a>' if prev else "<span></span>"
        r = f'<a href="{nxt[0]}">{html.escape(nxt[1])} &rarr;</a>' if nxt else "<span></span>"
        nav = f'<footer class="pn">{l}{r}</footer>'
    player = f'<audio controls src="{audio}"><a href="{audio}">audio version</a></audio>' if audio else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{html.escape(title)} - On MetaCraft</title>
  <style>{CSS}</style>
</head>
<body>
  <nav class="top">
    <a href="index.html"><strong>On MetaCraft</strong></a>
    <div class="links">
      <a href="index.html">Contents</a>
      <a href="assessment.html">Assessment</a>
      <a href="references.html">References</a>
      <a href="glossary.html">Glossary</a>
      <a class="epub-tag" href="on-metacraft.epub" download>EPUB</a>
    </div>
  </nav>
  <main>
    <h1>{html.escape(title)}</h1>
    {player}
    {body}
    {nav}
  </main>
</body>
</html>
"""


def main() -> int:
    ap = argparse.ArgumentParser(description="Build static book site and EPUB")
    ap.add_argument("--out", default=os.path.join(REPO_ROOT, "site"))
    args = ap.parse_args()
    out = args.out
    audio_dir = os.path.join(out, "audio")
    os.makedirs(out, exist_ok=True)

    # 1. Build EPUB first
    epub_path = os.path.join(out, "on-metacraft.epub")
    if build_epub:
        build_epub(epub_path)

    # 2. Build Chapters
    available = [f for f in ORDER if os.path.isfile(os.path.join(CHAPTERS_DIR, f))]
    extra = sorted(f for f in os.listdir(CHAPTERS_DIR) if f.endswith(".md") and f not in ORDER)
    files = available + extra

    pages: list[tuple[str, str]] = []
    for fn in files:
        md = open(os.path.join(CHAPTERS_DIR, fn), encoding="utf-8").read()
        title, body = md_to_html(md)
        stem = fn[:-3]
        pages.append((stem + ".html", title))

    for idx, (fn_html, title) in enumerate(pages):
        prev = pages[idx - 1] if idx > 0 else None
        nxt = pages[idx + 1] if idx + 1 < len(pages) else None
        stem = files[idx][:-3]
        wav = os.path.join(audio_dir, stem + ".wav")
        wav = f"audio/{stem}.wav" if os.path.isfile(wav) else None
        md = open(os.path.join(CHAPTERS_DIR, files[idx]), encoding="utf-8").read()
        t2, body = md_to_html(md)
        open(os.path.join(out, fn_html), "w", encoding="utf-8", newline="\n").write(
            page(t2, body, prev, nxt, wav)
        )

    # 3. Build Docs (Assessment & References)
    doc_pages = [
        ("ASSESSMENT.md", "assessment.html"),
        ("REFERENCES.md", "references.html"),
        ("GLOSSARY.md", "glossary.html"),
    ]
    for src, dst in doc_pages:
        src_path = os.path.join(DOCS_DIR, src)
        if os.path.isfile(src_path):
            md = open(src_path, encoding="utf-8").read()
            t, body = md_to_html(md)
            open(os.path.join(out, dst), "w", encoding="utf-8", newline="\n").write(
                page(t, body, None, None, None)
            )

    # 4. Build Index
    chapter_items = "\n".join(
        f'<li><a href="{fn}">{html.escape(t)}</a></li>' for fn, t in pages
    )
    doc_items = """
      <li><a href="assessment.html">Strategic Assessment & Methodological Evaluation</a></li>
      <li><a href="references.html">Scholarly Apparatus & Academic Bibliography</a></li>
      <li><a href="glossary.html">Glossary of Terms of Art</a></li>
    """

    index_body = f"""
    <p><em>The Aesthetic Singularity Arrived First</em></p>
    <p>Ten chapters ordered by reversibility of human gatekeeping, not by capability. From the misdirection to the stack to terminal states.</p>

    <p style="display:flex;gap:1rem;flex-wrap:wrap;">
      <a class="btn-box" href="on-metacraft.epub" download>
        &#128214; Download EPUB
      </a>
    </p>

    <h2>Chapters</h2>
    <ol class="toc-list">
      {chapter_items}
    </ol>

    <h2>Scholarly & Strategic Apparatus</h2>
    <ul class="toc-list">
      {doc_items}
    </ul>
    """

    open(os.path.join(out, "index.html"), "w", encoding="utf-8", newline="\n").write(
        page("Contents", index_body, None, None, None)
    )
    print(f"Built {len(pages) + len(doc_pages) + 1} web pages + EPUB -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
