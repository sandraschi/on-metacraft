# Install - on-metacraft

Book repo, not a service. No daemon.

```powershell
py -3 tools/lorecheck.py
just declaim chapters/01-the-breach.md
just build
just serve
```

Requires: Python 3.11+, `just`. Optional: GOOGLE_API_KEY for Gemini TTS.
