#!/usr/bin/env python3
"""Generate a spaced, interleaved study schedule (Markdown table) leading up to an exam.

Usage:
  study_schedule.py --exam 2026-10-20 --topics topics.txt
  study_schedule.py --exam 2026-10-20 --topic "L01 Cells:shaky:2" --topic "L02 Membranes:weak:3" \
                    --start 2026-10-01 --minutes 90 --skip sat

topics.txt: one topic per line, "Name[:mastery[:weight]]"
  mastery: new | weak | shaky | solid | mastered   (default new)
  weight:  relative exam importance, 1-5           (default 2)

Rules (see references/study-planning.md):
  * Each topic gets several retrieval sessions at expanding intervals; weaker/heavier topics get more.
  * Sessions interleave 2-4 topics.
  * Full timed practice exams ~6 days and ~2 days before the exam; the final day is light review.
"""
import argparse
import datetime as dt
import sys

MASTERY = {"new": 0.0, "weak": 0.25, "shaky": 0.5, "solid": 0.8, "mastered": 1.0}
DAYS = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]


def parse_topic(line):
    parts = [p.strip() for p in line.split(":")]
    name = parts[0]
    mastery = parts[1].lower() if len(parts) > 1 and parts[1] else "new"
    if mastery not in MASTERY:
        sys.exit(f"Unknown mastery '{mastery}' for topic '{name}'. Use one of: {', '.join(MASTERY)}")
    weight = int(parts[2]) if len(parts) > 2 and parts[2] else 2
    return {"name": name, "mastery": mastery, "weight": max(1, min(5, weight))}


def review_offsets(days_available, n_reviews, expand=1.4):
    """Expanding offsets (days from a topic's first session) that span the available window.

    Gaps grow with each review (spacing effect) and the last review lands near the end of the
    window, so every topic is retrieved again shortly before the exam.
    """
    if n_reviews <= 0 or days_available <= 0:
        return []
    if n_reviews == 1 or days_available == 1:
        return [0]
    span = days_available - 1
    offsets = []
    for k in range(n_reviews):
        pos = round(span * (k / (n_reviews - 1)) ** expand)
        if offsets and pos <= offsets[-1]:
            pos = offsets[-1] + 1
        if pos > span:
            break
        offsets.append(pos)
    return offsets


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--exam", required=True, help="exam date YYYY-MM-DD")
    ap.add_argument("--start", default=dt.date.today().isoformat(), help="first study day (default today)")
    ap.add_argument("--topics", help="file with one topic per line")
    ap.add_argument("--topic", action="append", default=[], help="topic spec, repeatable")
    ap.add_argument("--minutes", type=int, default=60, help="study minutes available per day (default 60)")
    ap.add_argument("--skip", action="append", default=[], help="weekday to skip (mon..sun), repeatable")
    ap.add_argument("--max-per-session", type=int, default=4, help="max topics per day (default 4)")
    args = ap.parse_args()

    exam = dt.date.fromisoformat(args.exam)
    start = dt.date.fromisoformat(args.start)
    specs = list(args.topic)
    if args.topics:
        with open(args.topics, encoding="utf-8") as f:
            specs += [ln.strip() for ln in f if ln.strip() and not ln.startswith("#")]
    if not specs:
        sys.exit("No topics given. Use --topics FILE or --topic 'Name:mastery:weight'.")
    topics = [parse_topic(s) for s in specs]

    skip = {d.lower()[:3] for d in args.skip}
    study_days = [start + dt.timedelta(days=i) for i in range((exam - start).days)
                  if DAYS[(start + dt.timedelta(days=i)).weekday()] not in skip]
    if len(study_days) < 2:
        sys.exit("Fewer than 2 study days before the exam. Triage: do mixed practice questions on "
                 "the highest-weight, weakest topics today, then rest.")

    last = study_days[-1]
    practice_days = set()
    for back in (6, 2):
        target = exam - dt.timedelta(days=back)
        cands = [d for d in study_days if d <= target and d != last]
        if cands and len(study_days) > back:
            practice_days.add(cands[-1])
    learn_days = [d for d in study_days if d not in practice_days and d != last]
    if not learn_days:
        learn_days = [d for d in study_days if d != last] or study_days

    # Priority and number of retrieval sessions per topic.
    for t in topics:
        t["priority"] = t["weight"] * (1.1 - MASTERY[t["mastery"]])
        t["sessions"] = max(2, min(6, round(2 + 3 * (1 - MASTERY[t["mastery"]]) + (t["weight"] - 2) * 0.5)))
    topics.sort(key=lambda t: -t["priority"])

    schedule = {d: [] for d in learn_days}
    n_days = len(learn_days)
    for i, t in enumerate(topics):
        # Stagger first sessions (two new topics per day) so high-priority topics start earliest.
        first = min(i // 2, max(0, n_days // 3))
        for off in review_offsets(n_days - first, t["sessions"]):
            idx = first + off
            # If the day is full (or already has this topic), use the nearest day with room.
            def has_room(k):
                day = schedule[learn_days[k]]
                return len(day) < args.max_per_session and t["name"] not in day
            if not has_room(idx):
                near = sorted((k for k in range(n_days) if has_room(k)), key=lambda k: (abs(k - idx), -k))
                if not near:
                    continue
                idx = near[0]
            schedule[learn_days[idx]].append(t["name"])

    print(f"# Study plan: exam on {exam:%a %Y-%m-%d}\n")
    print(f"{len(study_days)} study days · {args.minutes} min/day · topics ranked by weight × (1 − mastery)\n")
    print("| Topic | Mastery | Weight | Sessions |\n|---|---|---|---|")
    for t in topics:
        print(f"| {t['name']} | {t['mastery']} | {t['weight']} | {t['sessions']} |")
    print("\n| Date | Min | Topics (interleaved) | Activities | Done |\n|---|---|---|---|---|")
    for d in study_days:
        if d in practice_days:
            row = ("Full timed practice exam", "Take exam → grade (grade mode) → error log → re-study misses")
        elif d == last:
            row = ("Light review", "Formula sheet + error log + 10-question mixed quiz. Normal bedtime.")
        else:
            names = schedule.get(d, [])
            if not names:
                row = ("Flashcards only", "Anki reviews; re-test any error-log items due")
            else:
                row = (", ".join(names),
                       "Blank-page recall (5) → mixed practice Qs (25) → repair misses: why, example, diagram (10) → Anki (10)")
        print(f"| {d:%a %m/%d} | {args.minutes} | {row[0]} | {row[1]} | [ ] |")
    print(f"| **{exam:%a %m/%d}** | | **EXAM** | Brain dump formulas first; triage by points | |")


if __name__ == "__main__":
    main()
