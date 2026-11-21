# Working rules for AI agents in this repo

- **LF line endings only**, UTF-8 without BOM, in every text file (`.bat`/`.cmd` may be CRLF).
- **Single trunk.** Work on the default branch. No leftover agent branches, WIP branches or stashes;
  if a branch is unavoidable, merge or delete it in the same session.
- **No em dash** (U+2014) in any file. Use a hyphen or restructure the sentence.
- Name your paths when committing (`git add <path>`); never `git add -A` or `git commit -a`.

## Documentation preservation and hooks

On 2026-11-20 a README "standardization" sweep across the fleet deleted project descriptions,
status sections and user warnings in nine repos. Full rules:
`mcp-central-docs/standards/CONTENT_PRESERVATION_STANDARD.md`.

- Applying any standard or template restructures; it never deletes. Move content (within the file
  or to `docs/` with a link), do not drop it. Never remove what the project is, what it is based on,
  its status (what works, what does not, what is not built) or warnings to users.
- Remove content only when Sandra explicitly asks for that removal, in this repo.
- Never add claims you have not verified (release downloads, versions, test counts, features).
- Only standards with `status: active` may be applied across repos. A change across several repos is
  done on one repo first and approved by Sandra; its commits name the tool and carry a `Sweep-Id:` line.
- `.githooks/commit-msg` blocks a commit that deletes a Markdown file, removes 20% of its lines
  (15 or more) or removes 3 or more headings. A removal Sandra asked for passes with
  `Docs-Removal-Approved: <who and why>` in the message. Enable once per clone:
  `git config core.hooksPath .githooks`. Never use `--no-verify`; if a hook blocks you, stop and ask.
