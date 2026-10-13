set windows-shell := ["powershell.exe", "-NoProfile", "-Command"]

default:
  @just --list

# Declaim a markdown file via speech-mcp providers (Gemini if key present, else Windows SAPI).
# Usage: just declaim chapters/05-locating-the-present.md
#        just declaim file.md Kore gemini
declaim FILE VOICE="Kore" PROVIDER="auto":
  @py -3 tools/declaim.py {{FILE}} --provider {{PROVIDER}} --voice {{VOICE}}

# Dry run: show speech chunks without audio.
declaim-print FILE:
  @py -3 tools/declaim.py {{FILE}} --print

# Audio version of a chapter (Gemini TTS, needs GOOGLE_API_KEY). Embedded by build_site.
audio FILE:
  @py -3 tools/declaim.py {{FILE}} --provider auto --voice Kore --out site/audio/{{file_stem(FILE)}}.wav --no-play

# Build static HTML reader site and EPUB ebook.
build:
  @py -3 tools/build_site.py

# Build EPUB ebook directly.
epub:
  @py -3 tools/build_epub.py

# Build + serve the book locally (http://localhost:11026/).
serve PORT="11026":
  @py -3 tools/build_site.py
  @py -3 -m http.server {{PORT}} --bind 127.0.0.1 --directory site

# Lore-check: chapters I-X coverage, dates, forbidden terms.
lore:
  @py -3 tools/lorecheck.py

lore-strict:
  @py -3 tools/lorecheck.py --strict

# ---- bookkit (shared toolkit, ../bookkit) ----
bk := "py -3 ../bookkit/bk.py"

# Style check: AI-writer tells, rhythm, readability. Add --llm for an editor's critique.
critic *ARGS:
  @{{bk}} critic {{ARGS}}

# Claims ledger of [construction] flags (docs/claims.json). --stale N for unchecked ones.
claims *ARGS:
  @{{bk}} claims {{ARGS}}

# Flag count per commit -> docs/burndown.csv
burndown:
  @{{bk}} burndown

# Machine translation into chapters_<lang>/ (dry run first!). Example: just translate --lang fr --dry-run
translate *ARGS:
  @{{bk}} translate {{ARGS}}

# Reading-level editions. Example: just dumbdown --level kids --dry-run
dumbdown *ARGS:
  @{{bk}} dumbdown {{ARGS}}

# Cross-model review. Example: just review --target chapters/04-the-ladder.md --topic ladder --dry-run
review *ARGS:
  @{{bk}} review {{ARGS}}

# Dated GitHub evidence snapshot (needs [evidence] in book.toml)
evidence *ARGS:
  @{{bk}} evidence {{ARGS}}

# Print PDF, covers, EPUB validation, KDP packages (no upload)
pdf *ARGS:
  @{{bk}} pdf {{ARGS}}
cover *ARGS:
  @{{bk}} cover {{ARGS}}
validate:
  @{{bk}} validate
publish *ARGS:
  @{{bk}} publish {{ARGS}}

# Everything at once: evidence, claims, lore, editions, build, validate
keepcurrent *ARGS:
  @{{bk}} keepcurrent {{ARGS}}

# Series dashboard across all books + port collision check
series:
  @{{bk}} series
