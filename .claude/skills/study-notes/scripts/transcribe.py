#!/usr/bin/env python3
"""Turn a lecture recording or caption file into a clean, timestamped Markdown transcript.

Usage:
  transcribe.py lecture.vtt                     # clean platform captions (.vtt/.srt) -> stdout
  transcribe.py lecture.txt                     # plain transcript passes through (paragraphs kept)
  transcribe.py lecture.mp4 --model small -o L05_transcript.md
  transcribe.py lecture.m4a --language en

Audio/video transcription uses faster-whisper (preferred) or openai-whisper:
  pip install faster-whisper      # plus ffmpeg from your OS package manager for video/most audio
Models: tiny, base, small (default), medium, large-v3. Bigger = slower but better with jargon/accents.
"""
import argparse
import html
import os
import re
import sys

CAPTION_EXTS = {".vtt", ".srt"}
TEXT_EXTS = {".txt", ".md"}
MEDIA_EXTS = {".mp3", ".m4a", ".wav", ".aac", ".ogg", ".flac", ".opus", ".webm",
              ".mp4", ".mov", ".mkv", ".avi", ".m4v"}

TS_RE = re.compile(r"(?:(\d+):)?(\d{1,2}):(\d{2})[.,](\d{1,3})")


def fmt_ts(seconds):
    seconds = int(seconds)
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def parse_ts(text):
    m = TS_RE.search(text)
    if not m:
        return None
    h, mnt, s, _ = m.groups()
    return int(h or 0) * 3600 + int(mnt) * 60 + int(s)


def parse_captions(path):
    """Return a list of (start_seconds, text) from a .vtt or .srt file."""
    with open(path, encoding="utf-8-sig", errors="replace") as f:
        raw = f.read()
    blocks = re.split(r"\n\s*\n", raw.replace("\r\n", "\n"))
    segments = []
    for block in blocks:
        lines = [ln.strip() for ln in block.strip().split("\n") if ln.strip()]
        if not lines or lines[0].startswith(("WEBVTT", "NOTE", "STYLE", "REGION")):
            continue
        ts_idx = next((i for i, ln in enumerate(lines) if "-->" in ln), None)
        if ts_idx is None:
            continue
        start = parse_ts(lines[ts_idx].split("-->")[0])
        text = " ".join(lines[ts_idx + 1:])
        text = re.sub(r"<[^>]+>", "", text)          # strip vtt tags like <c>, <00:00:01.000>
        text = html.unescape(text).strip()
        if start is not None and text:
            segments.append((start, text))
    return _dedupe_rolling(segments)


def _dedupe_rolling(segments):
    """Auto-captions (YouTube etc.) repeat the previous line; drop repeated prefixes."""
    cleaned = []
    prev = ""
    for start, full in segments:
        if full == prev:
            continue
        new = full
        if prev and full.startswith(prev):
            new = full[len(prev):].strip()
        elif prev:
            # overlap: previous cue's tail equals this cue's head
            words_prev, words_cur = prev.split(), full.split()
            for k in range(min(len(words_prev), len(words_cur)), 0, -1):
                if words_prev[-k:] == words_cur[:k]:
                    new = " ".join(words_cur[k:])
                    break
        prev = full
        if new:
            cleaned.append((start, new))
    return cleaned


def to_paragraphs(segments, window):
    """Merge segments into paragraphs of ~window seconds, breaking at sentence ends when possible."""
    paras, cur, cur_start = [], [], None
    for start, text in segments:
        if cur_start is None:
            cur_start = start
        cur.append(text)
        joined = " ".join(cur)
        long_enough = start - cur_start >= window
        if (long_enough and re.search(r"[.?!]\"?$", text)) or start - cur_start >= window * 2:
            paras.append((cur_start, joined))
            cur, cur_start = [], None
    if cur:
        paras.append((cur_start, " ".join(cur)))
    return paras


def transcribe_media(path, model_name, language):
    try:
        from faster_whisper import WhisperModel
        print(f"Transcribing with faster-whisper ({model_name})...", file=sys.stderr)
        try:
            model = WhisperModel(model_name, device="auto", compute_type="auto")
        except Exception as e:  # usually the first-run model download failing
            sys.exit(f"Could not load whisper model '{model_name}': {e}\n"
                     "The first run downloads the model from huggingface.co. Check your internet "
                     "connection, or use the platform's .vtt/.srt transcript instead.")
        segs, info = model.transcribe(path, language=language, vad_filter=True)
        out = []
        for s in segs:
            out.append((s.start, s.text.strip()))
            print(f"\r  {fmt_ts(s.end)} transcribed", end="", file=sys.stderr)
        print(file=sys.stderr)
        return out
    except ImportError:
        pass
    try:
        import whisper
        print(f"Transcribing with openai-whisper ({model_name})...", file=sys.stderr)
        model = whisper.load_model(model_name)
        result = model.transcribe(path, language=language, verbose=False)
        return [(s["start"], s["text"].strip()) for s in result["segments"]]
    except ImportError:
        sys.exit(
            "No speech-to-text engine found. Options:\n"
            "  1) pip install faster-whisper   (and install ffmpeg), then re-run\n"
            "  2) Download the auto-transcript from Zoom/Panopto/Teams/Echo360/YouTube (.vtt/.srt/.txt)\n"
            "     and run this script on that file instead."
        )


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("-o", "--out", help="write Markdown here instead of stdout")
    ap.add_argument("--model", default="small", help="whisper model size (default: small)")
    ap.add_argument("--language", default=None, help="language code, e.g. en (default: auto-detect)")
    ap.add_argument("--window", type=int, default=45, help="target seconds per paragraph (default 45)")
    args = ap.parse_args()

    if not os.path.exists(args.file):
        sys.exit(f"File not found: {args.file}")
    ext = os.path.splitext(args.file)[1].lower()
    name = os.path.basename(args.file)

    if ext in CAPTION_EXTS:
        paras = to_paragraphs(parse_captions(args.file), args.window)
    elif ext in MEDIA_EXTS:
        paras = to_paragraphs(transcribe_media(args.file, args.model, args.language), args.window)
    elif ext in TEXT_EXTS:
        with open(args.file, encoding="utf-8", errors="replace") as f:
            text = f.read()
        md = f"# Transcript: {name}\n\n{text.strip()}\n"
        paras = None
    else:
        sys.exit(f"Unsupported file type '{ext}'.")

    if paras is not None:
        lines = [f"# Transcript: {name}", "",
                 "> Auto-generated transcript: technical terms may be misheard. Check against slides.", ""]
        lines += [f"**[{fmt_ts(start)}]** {text}\n" for start, text in paras]
        md = "\n".join(lines)

    if args.out:
        os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"Wrote {args.out}", file=sys.stderr)
    else:
        print(md)


if __name__ == "__main__":
    main()
