#!/usr/bin/env python3
"""Grounding audit: check that every content line in a note cites the course's own sources.

Usage:
  check_sources.py notes/L05-enzyme-kinetics.md
  check_sources.py notes/L05-*.md --slides 42 --skip-slides 1,2,42 --duration 1:14:30
  check_sources.py quizzes/Q-L05.md

What it checks (see references/source-lock.md):
  * Every content line has a source tag: [S12] [S3-S8] [12:34] [12:34-15:10] [L04 §2] [R: ...]
    [H: ...] [Board] [My notes] [VERIFY ...] or an internal pointer like (§2) / (see L03 §2).
    A tag on the first line of a block (consecutive non-blank lines) covers the whole block, e.g.
    "**How it works:** [S7][09:30]" followed by a numbered list. A tag in a section heading covers
    that section's tables and display-math lines.
  * No [Added] tags (outside content is not allowed in notes).
  * Outside examples/analogies only inside side notes: a blockquote starting
    "> 💡 **Side note (not from your lecture)" that names what it illustrates ("Illustrates: ... [S6]").
  * --slides N: which slides are never cited (pass --skip-slides for title/logistics slides).
  * --duration: which transcript segments (--bucket minutes, default 5) are never cited.

Exempt: the header block before the first "## " heading, headings, questions (lines ending in "?"),
multiple-choice options, HTML tags/comments, code blocks (Mermaid), and these sections:
Explain it back, Not covered in this lecture, Gaps and [VERIFY], Next steps, Score yourself.

Exit code 1 if any untagged content line or [Added] tag is found, else 0.
"""
import argparse
import re
import sys

TS = r"\d{1,2}:\d{2}(?::\d{2})?"
TAG_RE = re.compile(
    r"\[S\d+(?:\s*[–-]\s*S?\d+)?\]"                       # slides
    rf"|\[{TS}(?:\s*[–-]\s*{TS})?\]"                       # timestamps
    r"|\[L\d+[^\]]*\]"                                     # earlier lecture note
    r"|\[(?:R|H):[^\]]+\]"                                 # provided reading / handout
    r"|\[Board[^\]]*\]|\[My notes[^\]]*\]|\[VERIFY[^\]]*\]"
    r"|\((?:see\s+)?(?:L\d+\s*)?§\s*\d+[^)]*\)"            # internal pointer (§2) / (see L03 §2)
)
SLIDE_RE = re.compile(r"\[S(\d+)(?:\s*[–-]\s*S?(\d+))?\]")
TIME_RE = re.compile(rf"\[({TS})(?:\s*[–-]\s*({TS}))?\]")
ADDED_RE = re.compile(r"\[Added[^\]]*\]", re.IGNORECASE)
SIDE_START = "> 💡 **Side note (not from your lecture)"
EXEMPT_SECTIONS = ("explain it back", "not covered in this lecture", "gaps and", "next steps",
                   "score yourself", "after grading", "after you grade")
HTML_ONLY = re.compile(r"^(?:</?details>|<summary>.*?</summary>|<details><summary>.*?</summary>|</?\w+[^>]*>)+$")


def secs(ts):
    parts = [int(p) for p in ts.split(":")]
    while len(parts) < 3:
        parts.insert(0, 0)
    h, m, s = parts
    return h * 3600 + m * 60 + s


def is_exempt_line(s):
    if not s or s.startswith("#") or s == "---":
        return True
    if HTML_ONLY.match(s) or (s.startswith("<!--") and s.endswith("-->")):
        return True
    if re.match(r"^\|?\s*:?-{2,}", s):                     # table separator
        return True
    core = re.sub(r"<[^>]+>", "", s).strip()               # drop inline html (e.g. trailing <details>)
    core = re.sub(r"\*+", "", core).strip()
    if not core:
        return True
    if core.endswith("?") or re.search(r"\?\s*\(\d+\s*pts?\)$", core):
        return True                                        # a question
    if re.match(r"^-\s*[A-E]\.\s", s):                     # MCQ option
        return True
    if re.match(r"^(Confidence|Answer)\s*:?\s*_*$", core, re.I):
        return True
    if re.fullmatch(r"(Check yourself|Examples|Definitions|Answer|Answers)\b.*", core, re.I) and not re.search(r"[.;]", core):
        return True                                        # bare label line
    if re.match(r"^\*{1,2}(Professor review|Next steps|Revision task|Memorize vs understand|Professor's-eye)", s):
        return True                                        # instructions to the student, not content
    return False


def audit(path):
    lines = open(path, encoding="utf-8").read().splitlines()
    problems, added, lead_covered = [], [], 0
    side_notes, side_bad = 0, []
    in_side, side_text, side_line = False, "", 0
    slides, times = set(), []
    in_code = in_comment = False
    seen_h2 = False
    section, section_tagged = "", False
    block_tagged = False
    table_first_row = True

    for n, raw in enumerate(lines, start=1):
        s = raw.strip()
        for a, b in SLIDE_RE.findall(raw):
            lo, hi = int(a), int(b or a)
            slides.update(range(min(lo, hi), max(lo, hi) + 1))
        for a, b in TIME_RE.findall(raw):
            times.append((secs(a), secs(b) if b else secs(a)))
        if ADDED_RE.search(raw):
            added.append((n, s))

        if in_side and not s.startswith(">"):
            if "Illustrates:" not in side_text:
                side_bad.append((side_line, "side note has no 'Illustrates:' anchor"))
            in_side = False
        if s.startswith(SIDE_START):
            in_side, side_text, side_line = True, s, n
            side_notes += 1
            continue
        if in_side:
            side_text += " " + s
            continue
        if "💡" in s and s.startswith(">"):
            side_bad.append((n, "side note not labelled exactly '> 💡 **Side note (not from your lecture)'"))
            continue

        if s.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if in_comment:
            in_comment = "-->" not in s
            continue
        if s.startswith("<!--") and "-->" not in s:
            in_comment = True
            continue
        if s.startswith("## ") or s.startswith("### "):
            if s.startswith("## "):
                seen_h2 = True
                section = s[3:].lower()
            section_tagged = bool(TAG_RE.search(s)) or (s.startswith("### ") and section_tagged)
            if s.startswith("### "):
                section_tagged = bool(TAG_RE.search(s))
            block_tagged = False
            continue
        if not s:
            block_tagged = False
            table_first_row = True
            continue
        if re.match(r"^\*\*Next steps", s):
            section = "next steps"
        if not seen_h2 or any(k in section for k in EXEMPT_SECTIONS):
            continue

        tagged = bool(TAG_RE.search(s))
        starts_block = n == 1 or not lines[n - 2].strip()
        if starts_block or lines[n - 2].strip().startswith("<"):
            # Only a lead-in line (bold label, or text ending in ":") covers the lines below it.
            # An ordinary bullet or sentence covers only itself.
            bare = TAG_RE.sub("", s).strip()
            lead_in = bool(re.match(r"^(>\s*)?\*\*[^*]+\*\*", s)) or bare.endswith(":")
            block_tagged = tagged and lead_in and not s.startswith("|")

        is_table_row = s.startswith("|")
        if is_table_row:
            if table_first_row:            # header row
                table_first_row = False
                continue
        else:
            table_first_row = True

        if is_exempt_line(s) or tagged:
            continue
        if block_tagged or (section_tagged and (is_table_row or s.startswith("$$"))):
            lead_covered += 1
            continue
        if is_table_row and n >= 2:
            # table covered by a tagged line just above it (allow one blank line between)
            prev = [lines[k].strip() for k in range(max(0, n - 4), n - 1) if lines[k].strip()]
            above = next((p for p in reversed(prev) if not p.startswith("|")), "")
            if TAG_RE.search(above):
                lead_covered += 1
                continue
        problems.append((n, s))
    if in_side and "Illustrates:" not in side_text:
        side_bad.append((side_line, "side note has no 'Illustrates:' anchor"))
    return problems, added, slides, times, lead_covered, side_notes, side_bad


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+")
    ap.add_argument("--slides", type=int, help="number of slides in the deck (reports uncited slides)")
    ap.add_argument("--skip-slides", default="", help="comma-separated slides that need no citation (title, logistics)")
    ap.add_argument("--duration", help="recording length h:mm:ss or mm:ss (reports uncited segments)")
    ap.add_argument("--bucket", type=int, default=5, help="segment size in minutes for --duration (default 5)")
    args = ap.parse_args()

    all_slides, all_times, failed = set(), [], False
    for path in args.files:
        problems, added, slides, times, lead, side_n, side_bad = audit(path)
        all_slides |= slides
        all_times += times
        print(f"== {path}")
        if problems:
            failed = True
            print(f"  {len(problems)} content line(s) with no source tag:")
            for n, s in problems:
                print(f"    line {n}: {s[:110]}")
        if added:
            failed = True
            print(f"  {len(added)} [Added] tag(s): outside content is not allowed in notes:")
            for n, s in added:
                print(f"    line {n}: {s[:110]}")
        if side_bad:
            failed = True
            print(f"  {len(side_bad)} side-note problem(s):")
            for n, msg in side_bad:
                print(f"    line {n}: {msg}")
        if not problems and not added and not side_bad:
            print("  OK: every content line is source-tagged.")
        if side_n:
            print(f"  {side_n} side note(s) with outside examples/analogies. Check each is only an illustration "
                  "(no new concepts or testable facts) and that no quiz, flashcard or key relies on it.")
        if lead:
            print(f"  note: {lead} line(s) are covered only by a tag on their block's lead-in line or heading. "
                  "Spot-check them.")

    if args.slides:
        skip = {int(x) for x in args.skip_slides.split(",") if x.strip().isdigit()}
        missing = [i for i in range(1, args.slides + 1) if i not in all_slides and i not in skip]
        print(f"== Slide coverage: {args.slides - len(missing)}/{args.slides} cited or skipped")
        if missing:
            print(f"  never cited: {', '.join('S' + str(i) for i in missing)}")
    if args.duration:
        total = secs(args.duration)
        size = args.bucket * 60
        uncovered = []
        for start in range(0, total, size):
            end = min(start + size, total)
            if not any(a <= end and b >= start for a, b in all_times):
                uncovered.append(f"{start // 60:02d}:00–{end // 60:02d}:{end % 60:02d}")
        n_buckets = -(-total // size)
        print(f"== Transcript coverage: {n_buckets - len(uncovered)}/{n_buckets} segments of {args.bucket} min cited")
        if uncovered:
            print(f"  never cited: {', '.join(uncovered)} (check these segments for missed content)")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
