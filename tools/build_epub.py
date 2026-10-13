"""Build standalone valid EPUB 3 from chapters/*.md - pure Python stdlib.

No third-party dependencies required. Produces a compliant EPUB archive
with valid mimetype, container.xml, content.opf, nav.xhtml, and toc.ncx.

Usage:
  python tools/build_epub.py [--out site/on-metacraft.epub]
"""
from __future__ import annotations

import argparse
import html
import os
import re
import uuid
import zipfile
from datetime import datetime, timezone

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS_DIR = os.path.join(REPO_ROOT, "chapters")

BOOK_TITLE = "On MetaCraft"
BOOK_SUBTITLE = "The Reimplementation Cost Collapse"
BOOK_AUTHOR = "Sandra Schipal"
BOOK_IDENTIFIER = "urn:uuid:8b34f682-142e-4b61-9c17-1f4803738b55"
BOOK_LANGUAGE = "en"

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

EPUB_CSS = """@charset "utf-8";
body {
    font-family: Georgia, Cambria, "Times New Roman", Times, serif;
    line-height: 1.6;
    margin: 5%;
    text-align: justify;
    color: inherit;
}
h1, h2, h3, h4 {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    line-height: 1.25;
    text-align: left;
    color: inherit;
    margin-top: 1.5em;
    margin-bottom: 0.5em;
}
h1 { font-size: 1.8em; border-bottom: 1px solid #e5e7eb; padding-bottom: 0.3em; }
h2 { font-size: 1.4em; }
h3 { font-size: 1.15em; }
p { margin: 0 0 1em 0; text-indent: 0; }
blockquote {
    margin: 1em 0 1em 1.5em;
    padding-left: 1em;
    border-left: 3px solid #6366f1;
    color: inherit;
    font-style: italic;
}
code {
    font-family: "Courier New", Courier, monospace;
    font-size: 0.9em;
    background-color: transparent;
    padding: 0.1em 0.3em;
}
pre {
    background-color: transparent;
    padding: 0.8em;
    overflow-x: auto;
    font-size: 0.85em;
    border-radius: 4px;
}
pre code { background: none; padding: 0; }
table {
    border-collapse: collapse;
    width: 100%;
    margin: 1.2em 0;
    font-size: 0.9em;
}
th, td {
    border: 1px solid #d1d5db;
    padding: 0.4em 0.6em;
    text-align: left;
}
th { font-weight: bold; }
hr { border: none; border-top: 1px solid #e5e7eb; margin: 2em 0; }
.title-page { text-align: center; margin-top: 20%; }
.title-page h1 { font-size: 2.2em; border: none; text-align: center; }
.title-page .subtitle { font-size: 1.2em; color: inherit; margin-top: 0.5em; }
.title-page .author { font-size: 1.1em; margin-top: 2em; }
.title-page .draft { font-size: 0.9em; color: inherit; margin-top: 1em; }
.title-page .epigraph { font-style: italic; color: inherit; margin-top: 3em; }
section.endnotes { margin-top: 2em; }
section.endnotes h2 { font-size: 1.1em; }
section.endnotes li { font-size: 0.9em; }
nav#toc ol { list-style: none; padding-left: 0; }
nav#toc ol ol { padding-left: 1.2em; }
nav#toc li { margin: 0.25em 0; }
nav#toc .toc-group { font-weight: bold; margin-top: 0.8em; }
"""


def slug(text: str) -> str:
    s = re.sub(r"<[^>]+>", "", text).lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def inline_xhtml(md: str) -> str:
    out = html.escape(md, quote=True)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    out = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', out)
    out = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", out)
    return out


FN_DEF_RE = re.compile(r"^\[\^([^\]]+)\]:\s*(.+?)\s*$")
FN_REF_RE = re.compile(r"\[\^([^\]]+)\]")


def split_footnotes(md: str) -> tuple[str, list[str], dict[str, str]]:
    """Strip `[^key]: text` defs; tokenize `[^key]` refs outside fences."""
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
    """Replace ref tokens with numbered sup links; append Notes section (XHTML)."""
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
        f'<li id="fn-{k}">{inline_xhtml(defs[k])} <a href="#fnref-{k}">\u21a9</a></li>'
        for k in notes
    )
    return html_text + (
        "\n" + '<section class="endnotes"><hr /><h2>Notes</h2>\n<ol>\n'
        + items + "\n</ol>\n</section>"
    )


def md_to_xhtml(md: str) -> tuple[str, str]:
    """Converts markdown to strictly valid XHTML for EPUB."""
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
            text = inline_xhtml(m.group(2))
            if level == 1 and title == "Untitled":
                title = re.sub(r"<[^>]+>", "", text)
            parts.append(f'<h{level} id="{slug(text)}">{text}</h{level}>')
            i += 1
            continue
        if re.match(r"^---+$", s):
            parts.append("<hr />")
            i += 1
            continue
        if s.startswith(">"):
            quote = []
            while i < n and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip()[1:].strip())
                i += 1
            parts.append("<blockquote><p>" + " ".join(inline_xhtml(q) for q in quote) + "</p></blockquote>")
            continue
        if s.startswith("|") and i + 1 < n and re.match(r"^\|[\s:|-]+\|$", lines[i + 1].strip()):
            header = [c.strip() for c in s.strip("|").split("|")]
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            t = ["<table><thead><tr>" + "".join(f"<th>{inline_xhtml(c)}</th>" for c in header) + "</tr></thead><tbody>"]
            t += ["<tr>" + "".join(f"<td>{inline_xhtml(c)}</td>" for c in r) + "</tr>" for r in rows]
            parts.append("".join(t) + "</tbody></table>")
            continue
        if re.match(r"^[-*]\s+", s):
            items = []
            while i < n and re.match(r"^[-*]\s+", lines[i].strip()):
                items.append("<li>" + inline_xhtml(re.sub(r"^[-*]\s+", "", lines[i].strip())) + "</li>")
                i += 1
            parts.append("<ul>" + "".join(items) + "</ul>")
            continue
        if re.match(r"^\d+\.\s+", s):
            items = []
            while i < n and re.match(r"^\d+\.\s+", lines[i].strip()):
                items.append("<li>" + inline_xhtml(re.sub(r"^\d+\.\s+", "", lines[i].strip())) + "</li>")
                i += 1
            parts.append("<ol>" + "".join(items) + "</ol>")
            continue
        buf = []
        while i < n and lines[i].strip() and not re.match(r"^(#{1,3}\s|```|\||[-*]\s|\d+\.\s|>|---+$)", lines[i].strip()):
            buf.append(lines[i].strip())
            i += 1
        parts.append("<p>" + inline_xhtml(" ".join(buf)) + "</p>")
    return title, resolve_footnotes("\n".join(parts), fn_order, fn_defs)


def build_epub(output_path: str, title: str = BOOK_TITLE, author: str = BOOK_AUTHOR) -> None:
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

    available = [f for f in ORDER if os.path.isfile(os.path.join(CHAPTERS_DIR, f))]
    extra = sorted(f for f in os.listdir(CHAPTERS_DIR) if f.endswith(".md") and f not in ORDER)
    files = available + extra

    chapters: list[dict[str, str]] = []
    for idx, fn in enumerate(files, 1):
        md = open(os.path.join(CHAPTERS_DIR, fn), encoding="utf-8").read()
        ch_title, body_xhtml = md_to_xhtml(md)
        filename = f"chapter_{idx:02d}.xhtml"
        chapters.append({
            "id": f"ch_{idx:02d}",
            "filename": filename,
            "title": ch_title,
            "body": body_xhtml,
            "source": fn,
        })

    rev_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    title_body = (
        '<section class="title-page">\n<h1>On MetaCraft</h1>\n'
        f'<p class="subtitle">{html.escape(BOOK_SUBTITLE)}</p>\n'
        f'<p class="author">{html.escape(author)}</p>\n'
        f'<p class="draft">Construction draft — {rev_date}</p>\n'
        '<p class="epigraph">Beauty is truth, truth beauty, — that is all<br />\n'
        'Ye know on earth, and all ye need to know.<br />— John Keats, 1820</p>\n'
        "</section>"
    )
    chapters.insert(0, {
        "id": "titlepage",
        "filename": "titlepage.xhtml",
        "title": "Title Page",
        "body": title_body,
        "source": "",
        "notoc": True,
    })

    def _group(fn: str) -> str:
        if fn in ("00-preface.md", "cold-open-variants.md"):
            return "Front Matter"
        if fn.startswith("side-"):
            return "Sides"
        return "Chapters"

    pub_date = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # Generate container.xml
    container_xml = """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>"""

    # Generate nav.xhtml (EPUB 3 TOC, grouped: front matter / chapters / sides)
    GROUP_ORDER = ["Front Matter", "Chapters", "Sides"]
    grouped: dict[str, list[dict[str, str]]] = {g: [] for g in GROUP_ORDER}
    for ch in chapters:
        if ch.get("notoc"):
            continue
        grouped.setdefault(_group(ch.get("source", "")), []).append(ch)
    nav_groups = []
    for g in GROUP_ORDER:
        items = grouped.get(g, [])
        if not items:
            continue
        lis = "\n".join(
            f'        <li><a href="{c["filename"]}">{html.escape(c["title"])}</a></li>'
            for c in items
        )
        nav_groups.append(
            f'      <li><span class="toc-group">{g}</span>\n      <ol>\n{lis}\n      </ol>\n      </li>'
        )
    nav_xhtml = f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="{BOOK_LANGUAGE}">
<head>
  <title>Table of Contents</title>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
  <nav epub:type="toc" id="toc">
    <h1>Contents</h1>
    <ol>
{chr(10).join(nav_groups)}
    </ol>
  </nav>
</body>
</html>"""

    # Generate toc.ncx (EPUB 2 backward compatibility; title page excluded)
    ncx_navpoints = "\n".join(
        f"""    <navPoint id="navpoint-{idx}" playOrder="{idx}">
      <navLabel><text>{html.escape(ch["title"])}</text></navLabel>
      <content src="{ch["filename"]}"/>
    </navPoint>"""
        for idx, ch in enumerate([c for c in chapters if not c.get("notoc")], 1)
    )
    toc_ncx = f"""<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head>
    <meta name="dtb:uid" content="{BOOK_IDENTIFIER}"/>
    <meta name="dtb:depth" content="1"/>
    <meta name="dtb:totalPageCount" content="0"/>
    <meta name="dtb:maxPageNumber" content="0"/>
  </head>
  <docTitle><text>{html.escape(title)}</text></docTitle>
  <navMap>
{ncx_navpoints}
  </navMap>
</ncx>"""

    # Generate content.opf
    manifest_items = [
        '    <item id="style" href="style.css" media-type="text/css"/>',
        '    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
        '    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
    ]
    for ch in chapters:
        manifest_items.append(
            f'    <item id="{ch["id"]}" href="{ch["filename"]}" media-type="application/xhtml+xml"/>'
        )

    spine_items = [f'    <itemref idref="{ch["id"]}"/>' for ch in chapters]

    content_opf = f"""<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="pub-id" xml:lang="{BOOK_LANGUAGE}">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="pub-id">{BOOK_IDENTIFIER}</dc:identifier>
    <dc:title>{html.escape(title)}</dc:title>
    <dc:creator>{html.escape(author)}</dc:creator>
    <dc:language>{BOOK_LANGUAGE}</dc:language>
    <dc:date>{pub_date}</dc:date>
    <meta property="dcterms:modified">{pub_date}</meta>
  </metadata>
  <manifest>
{chr(10).join(manifest_items)}
  </manifest>
  <spine toc="ncx">
{chr(10).join(spine_items)}
  </spine>
</package>"""

    # Assemble ZIP file
    with zipfile.ZipFile(output_path, "w") as zf:
        # 1. mimetype must be stored uncompressed, as the very first file
        zf.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)

        # 2. META-INF/container.xml
        zf.writestr("META-INF/container.xml", container_xml, compress_type=zipfile.ZIP_DEFLATED)

        # 3. OEBPS contents
        zf.writestr("OEBPS/content.opf", content_opf, compress_type=zipfile.ZIP_DEFLATED)
        zf.writestr("OEBPS/nav.xhtml", nav_xhtml, compress_type=zipfile.ZIP_DEFLATED)
        zf.writestr("OEBPS/toc.ncx", toc_ncx, compress_type=zipfile.ZIP_DEFLATED)
        zf.writestr("OEBPS/style.css", EPUB_CSS, compress_type=zipfile.ZIP_DEFLATED)

        # 4. Each chapter XHTML
        for ch in chapters:
            doc = f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="{BOOK_LANGUAGE}">
<head>
  <title>{html.escape(ch["title"])}</title>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
  {ch["body"]}
</body>
</html>"""
            zf.writestr(f'OEBPS/{ch["filename"]}', doc, compress_type=zipfile.ZIP_DEFLATED)

    size_kb = os.path.getsize(output_path) / 1024
    print(f"Generated EPUB 3: {output_path} ({size_kb:.1f} KB, {len(chapters)} chapters)")


def main() -> int:
    ap = argparse.ArgumentParser(description="Build EPUB 3 from chapters")
    ap.add_argument("--out", default=os.path.join(REPO_ROOT, "site", "on-metacraft.epub"))
    args = ap.parse_args()
    build_epub(args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
