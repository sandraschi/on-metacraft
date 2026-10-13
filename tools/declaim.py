"""Declaim reader for on-ai-takeover - markdown to speech via speech-mcp providers.

Usage:
  python tools/declaim.py chapters/05-locating-the-present.md --provider auto --voice Kore
  python tools/declaim.py /tmp/cold-open.md --provider windows --print
  python tools/declaim.py cold.md --provider gemini --voice Kore --out out.wav --no-play

Providers:
  auto    -> gemini if GOOGLE_API_KEY present and google.genai importable, else windows
  gemini  -> Gemini 3.1 Flash TTS (needs GOOGLE_API_KEY, google-genai SDK)
  windows -> SAPI5 via pyttsx3, offline, no key

Key lookup (presence only, never printed):
  env GOOGLE_API_KEY, then on-ai-takeover/.env, then ../speech-mcp/.env
"""
from __future__ import annotations

import argparse
import io
import os
import re
import sys
import tempfile
import wave

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAX_CHUNK = 1400


def load_dotenv(path: str) -> None:
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                k = k.strip()
                if k and k not in os.environ:
                    os.environ[k] = v.strip().strip('"').strip("'")
    except FileNotFoundError:
        pass


for _p in (
    os.path.join(REPO_ROOT, ".env"),
    os.path.join(os.path.dirname(REPO_ROOT), "speech-mcp", ".env"),
):
    load_dotenv(_p)


def clean_for_speech(md: str) -> str:
    md = re.sub(r"```.*?```", " ", md, flags=re.S)
    md = re.sub(r"^(#{1,6}\s+)", "", md, flags=re.M)
    md = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", md)
    md = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", md)
    md = re.sub(r"(https?://\S+)", " ", md)
    md = re.sub(r"[`*_~|>]", " ", md)
    md = re.sub(r"^---+$", " ", md, flags=re.M)
    md = re.sub(r"[ \t]+", " ", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip()


def chunk_text(text: str, limit: int = MAX_CHUNK) -> list[str]:
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    chunks: list[str] = []
    buf = ""
    for p in paras:
        if len(buf) + len(p) + 2 <= limit:
            buf = f"{buf}\n\n{p}" if buf else p
            continue
        if buf:
            chunks.append(buf)
            buf = ""
        if len(p) <= limit:
            buf = p
            continue
        # split long para at sentences
        sents = re.split(r"(?<=[.!?])\s+", p)
        cur = ""
        for s in sents:
            if len(cur) + len(s) + 1 <= limit:
                cur = f"{cur} {s}".strip()
            else:
                if cur:
                    chunks.append(cur)
                cur = s
        if cur:
            buf = cur
    if buf:
        chunks.append(buf)
    return chunks


def have_gemini() -> bool:
    if not os.getenv("GOOGLE_API_KEY"):
        return False
    try:
        import google.genai  # noqa: F401
        return True
    except Exception:
        return False


def synth_gemini(chunks: list[str], voice: str) -> bytes:
    sys.path.insert(0, os.path.join(os.path.dirname(REPO_ROOT), "speech-mcp", "src"))
    from speech_mcp.providers.gemini import GeminiProvider

    prov = GeminiProvider()
    wavs = [prov.synthesize_wav(c, voice_name=voice) for c in chunks]
    # concat PCM frames (all 24k mono 16-bit from provider)
    frames = b""
    for w in wavs:
        with wave.open(io.BytesIO(w), "rb") as wf:
            frames += wf.readframes(wf.getnframes())
    buf = io.BytesIO()
    with wave.open(buf, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)
        wf.writeframes(frames)
    return buf.getvalue()


def speak_windows(chunks: list[str], voice: str) -> None:
    import pyttsx3

    engine = pyttsx3.init()
    if voice and voice != "default":
        try:
            voices = engine.getProperty("voices") or []
            for v in voices:
                vid = getattr(v, "id", "") or ""
                vname = getattr(v, "name", "") or ""
                if voice == vid or voice.lower() in vname.lower():
                    engine.setProperty("voice", vid)
                    break
        except Exception:
            pass
    for c in chunks:
        engine.say(c)
    engine.runAndWait()


def play_wav(path: str) -> None:
    if sys.platform == "win32":
        import winsound
        winsound.PlaySound(path, winsound.SND_FILENAME)
    else:
        print(f"saved (no auto-play on {sys.platform}): {path}")


def main() -> int:
    ap = argparse.ArgumentParser(description="Declaim markdown via speech-mcp providers")
    ap.add_argument("file", help="markdown file to declaim")
    ap.add_argument("--provider", default="auto", choices=["auto", "gemini", "windows"])
    ap.add_argument("--voice", default="Kore", help="gemini voice (Kore default) or windows voice name")
    ap.add_argument("--out", default="", help="save combined wav here (gemini only)")
    ap.add_argument("--no-play", action="store_true", help="synthesize/save but do not play")
    ap.add_argument("--print", dest="show", action="store_true", help="dry run: show chunks only")
    args = ap.parse_args()

    with open(args.file, encoding="utf-8") as f:
        raw = f.read()
    text = clean_for_speech(raw)
    chunks = chunk_text(text)
    provider = args.provider
    if provider == "auto":
        provider = "gemini" if have_gemini() else "windows"

    print(f"file: {args.file} | chars: {len(text)} | chunks: {len(chunks)} | provider: {provider} | voice: {args.voice}")
    print(f"gemini_key: {'present' if os.getenv('GOOGLE_API_KEY') else 'missing'} (value never printed)")
    if args.show:
        for i, c in enumerate(chunks, 1):
            print(f"\n--- chunk {i}/{len(chunks)} ({len(c)} chars) ---\n{c[:600]}{'...' if len(c) > 600 else ''}")
        return 0

    if provider == "gemini":
        wav = synth_gemini(chunks, args.voice)
        out = args.out or os.path.join(tempfile.gettempdir(), "declaim.wav")
        parent = os.path.dirname(os.path.abspath(out))
        if parent:
            os.makedirs(parent, exist_ok=True)
        with open(out, "wb") as f:
            f.write(wav)
        print(f"saved: {out} ({len(wav)} bytes)")
        if not args.no_play:
            play_wav(out)
    else:
        if args.out:
            print("note: --out ignored for windows provider (live SAPI only)", file=sys.stderr)
        speak_windows(chunks, args.voice)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
