#!/usr/bin/env python3
"""Convert a flashcards deck.md into an Anki-importable TSV (Basic + Cloze in one file).

Usage:
  flashcards_to_anki.py courses/BIO201/flashcards/deck.md            # writes deck.tsv next to it
  flashcards_to_anki.py deck.md -o bio201.tsv --deck "BIO201"

deck.md format (cards separated by blank lines; "## Heading" sets the sub-deck):
  Q: question            ->  Basic card
  A: answer
  Tags: L05 enzymes      (optional)

  C: The {{c1::active site}} binds substrate.   ->  Cloze card
  X: optional extra shown on the back
  Tags: L05

Import in Anki (2.1.55+): File -> Import -> choose the .tsv. Note type, deck and tags are read
from the file header, so no field mapping is needed.
"""
import argparse
import html
import os
import re
import sys

FIELD_RE = re.compile(r"^(Q|A|C|X|Tags):\s?(.*)$", re.IGNORECASE)


def slug_tag(text):
    return re.sub(r"[^\w:-]+", "_", text.strip()).strip("_")


def md_inline_to_html(text):
    """Minimal Markdown -> HTML so bold/italics/code survive in Anki."""
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<i>\1</i>", text)
    return text


def parse(path, root_deck):
    cards, errors = [], []
    subdeck = None
    card, last_field = {}, None

    def flush(lineno):
        nonlocal card, last_field
        if not card:
            return
        if "C" in card:
            cards.append(("Cloze", subdeck, card["C"], card.get("X", ""), card.get("TAGS", "")))
            if "{{c" not in card["C"]:
                errors.append(f"line {lineno}: cloze card has no {{{{c1::...}}}} deletion")
        elif "Q" in card and "A" in card:
            cards.append(("Basic", subdeck, card["Q"], card["A"], card.get("TAGS", "")))
        else:
            errors.append(f"line {lineno}: incomplete card (needs Q+A or C): {card}")
        card, last_field = {}, None

    in_comment = False
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
    for n, line in enumerate(lines, start=1):
        stripped = line.strip()
        if in_comment:
            in_comment = "-->" not in stripped
            continue
        if stripped.startswith("<!--"):
            in_comment = "-->" not in stripped
            continue
        if stripped.startswith("# "):
            continue
        if stripped.startswith("## "):
            flush(n)
            subdeck = stripped[3:].strip()
            continue
        if not stripped:
            flush(n)
            continue
        m = FIELD_RE.match(stripped)
        if m:
            key = m.group(1).upper()
            if key in ("Q", "C") and card:
                flush(n)
            card[key] = m.group(2).strip()
            last_field = key
        elif last_field and last_field != "TAGS":
            card[last_field] += "\n" + stripped  # continuation line
        else:
            errors.append(f"line {n}: text outside a card ignored: {stripped[:60]}")
    flush(len(lines))

    rows = []
    for notetype, sub, front, back, tags in cards:
        deck = f"{root_deck}::{sub}" if sub else root_deck
        tag_list = [slug_tag(t) for t in tags.split()] if tags else []
        if sub and not tags:
            tag_list.append(slug_tag(sub.split()[0]))
        fields = [md_inline_to_html(x).replace("\n", "<br>") for x in (front, back)]
        rows.append([notetype, deck, *fields, " ".join(tag_list)])
    return rows, errors


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("deck_md")
    ap.add_argument("-o", "--out", help="output .tsv (default: same folder, deck.tsv)")
    ap.add_argument("--deck", help="root Anki deck name (default: course folder name, e.g. BIO201)")
    args = ap.parse_args()

    if not os.path.exists(args.deck_md):
        sys.exit(f"File not found: {args.deck_md}")
    src = os.path.abspath(args.deck_md)
    root_deck = args.deck or os.path.basename(os.path.dirname(os.path.dirname(src))) or "Study"
    out = args.out or os.path.join(os.path.dirname(src), os.path.splitext(os.path.basename(src))[0] + ".tsv")

    rows, errors = parse(src, root_deck)
    header = [
        "#separator:tab",
        "#html:true",
        "#notetype column:1",
        "#deck column:2",
        "#tags column:5",
    ]
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(header) + "\n")
        for r in rows:
            f.write("\t".join(c.replace("\t", " ") for c in r) + "\n")

    basic = sum(1 for r in rows if r[0] == "Basic")
    print(f"Wrote {out}: {len(rows)} cards ({basic} Basic, {len(rows) - basic} Cloze), deck '{root_deck}'",
          file=sys.stderr)
    for e in errors:
        print(f"  warning: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
