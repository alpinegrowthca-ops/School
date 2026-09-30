# <COURSE> Flashcards

<!--
Source of truth for the deck. Convert for Anki with:
  python3 .claude/skills/study-notes/scripts/flashcards_to_anki.py courses/<COURSE>/flashcards/deck.md
Then in Anki: File → Import → deck.tsv

Format:
  Q: question        (Basic card)
  A: answer
  Tags: L01 topic    (optional)

  C: text with {{c1::cloze}} deletions   (Cloze card)
  X: optional extra info shown on back
  Tags: L01 topic

Separate cards with a blank line. "## Heading" = sub-deck.
Rules: one fact per card · why-cards too · no lists · contrast confusable pairs.
-->

## L01 – <Topic>

Q: <precise question with one correct answer>
A: <short answer>
Tags: L01 <topic>

Q: Why does <X> happen?
A: <mechanism in 1–2 sentences>
Tags: L01 <topic> why

C: <Term> is defined as {{c1::<definition>}}.
Tags: L01 <topic> definition

Q: <X> vs <Y>: which one <distinguishing property>?
A: <X>, because …; <Y> instead …
Tags: L01 <topic> contrast
