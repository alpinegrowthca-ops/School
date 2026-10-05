# Source-Lock Policy (overrides everything else)

**The student's rule:** notes must be built only from the course's own lecture material. Claude must not make up concepts, explanations or facts. The **one exception** is outside **examples and analogies**, which help understanding. They're allowed, but only as clearly labelled **side notes** (§4), kept visually separate from the course content. This policy overrides any instruction elsewhere in the skill that seems to call for added content. When this file and another file disagree, this file wins.

---

## 1. What counts as a source

| Tag | Source | Allowed in notes |
|---|---|---|
| `[S12]`, `[S12–15]` | Lecture slides (including speaker notes) | ✅ Primary |
| `[12:34]`, `[12:34–15:10]`, `[1:02:10]` | Lecture recording or transcript, with timestamp | ✅ Primary |
| `[L04 §2]` | An earlier note in this course (itself source-locked) | ✅ For links and prerequisites |
| `[R: <short ref> p.X]` | A reading or textbook section **the student provided** | ✅ Only if the student gave it to you |
| `[H: <name>]` | A handout, problem set, lab manual or syllabus **the student provided** | ✅ Only if the student gave it to you |
| `[Board]` | A photo of the whiteboard or the professor's annotations | ✅ |
| `[My notes]` | The student's own class notes | ✅ Their content, checked against the slides and transcript |
| `> 💡 **Side note (not from your lecture)**` | Claude's outside **example or analogy** illustrating a concept that *is* in the sources | ⚠️ Only in a side-note callout (§4) |
| *(none)* | Claude's general knowledge as *content*: concepts, facts, explanations, history | ❌ **Never in a note** |

If `CLAUDE.md` restricts sources further (for example, "slides and transcripts only"), follow that.

## 2. What Claude may do with the sources

Claude is the *editor and teacher of the lecture's own content*, not an extra author.

**Allowed (it adds no new content):**
- **Reorganize**: reorder, group by principle, build a roadmap, put content under headings.
- **Rephrase for clarity**: rewrite a rambling spoken explanation into clean sentences that **keep the meaning exactly**, with no new claims, examples or qualifiers. Keep the professor's key wording for definitions (quote the slide when the exact wording matters).
- **Re-present**: turn source content into tables, comparison matrices and Mermaid diagrams, where every cell or node comes from the sources.
- **Connect**: point out links between two things that are *both* in the sources (`see L03 §2`). If the professor didn't state the link, write "(link not stated in lecture)".
- **Fix transcription errors** using the slides (for example, a misheard technical term). If the slides can't resolve it, use `[VERIFY]`.
- **Compute**: carry out the arithmetic in a worked example *that the lecture gives*, and recompute it to check.
- **Ask questions**: Check-yourself questions, quizzes and exam questions about source content. Practice questions may use new numbers or scenarios to *apply* a principle from the lecture, but the principle and the answer must come from the sources, and the answer key cites them.

**Not allowed in the main note** (outside examples and analogies go in side notes, §4):
- New examples, analogies, non-examples or "real-world" applications that the lecture didn't give, *anywhere except a side note*.
- Background, history, researcher names, dates or experiments the lecture didn't mention.
- Explanations, mechanisms or derivation steps the lecture skipped. Don't fill the gap; record it (§3).
- Misconceptions or "common mistakes" the professor or a student didn't raise.
- Corrections from outside knowledge. If something in a source looks wrong, flag it `[VERIFY]` and say *what* looks inconsistent (with another slide, the transcript, or a provided reading), but don't insert a replacement fact.
- Learning objectives or "big questions" that aren't on the slides or syllabus or stated by the professor.
- The `[Added]` tag. It's retired from notes.

## 3. When the lecture doesn't give something: the "Not covered in this lecture" section

The teaching structure (Concept Ladder, professor-level hallmarks) lists *slots* a great note fills. **Fill a slot only from the sources.** When a slot is empty for a core concept, leave it out of the main text and list it at the end of the note:

```markdown
## Not covered in this lecture
*Your slides and transcript don't provide these. Where a side note fills the gap, it says so, but side notes are Claude's illustrations, not course content. Ask about the rest in office hours or check your assigned reading.*
- **Km**: the lecture gave no analogy (see the side note in §1). The derivation skips the step from steady state to [ES].
- **Uncompetitive inhibition**: the lecture gave no example (see the side note in §3).
```

This keeps notes honest: the student sees exactly what the course gave them and what's missing.

## 4. Side notes: outside examples and analogies

The student wants outside **examples and analogies** to aid understanding, kept separate from the course content. Write them as side notes:

```markdown
> 💡 **Side note (not from your lecture): analogy.** Think of an enzyme population like cashiers in a store … *Where the analogy breaks:* … *Illustrates:* Km and Vmax (§1, [S5–S6]).
```

**Rules**
1. **Only examples and analogies.** A side note may *illustrate* a concept from the sources: a real-world example, an analogy (always with **where it breaks**), or a worked numeric illustration of a formula the lecture gave. It may **not** introduce a new concept, definition, fact the exam could test, mechanism, history or "misconception".
2. **Anchor it.** Every side note names the course concept it illustrates and points to that concept's source tag ("*Illustrates:* … [S6]").
3. **Placement.** Put it *after* the source content it illustrates, never in the middle of the lecture's explanation. Never inside a definition, Check-yourself answer, table or worked example from the lecture.
4. **Format.** Always a blockquote starting exactly `> 💡 **Side note (not from your lecture)`, so it's visually distinct and the checker can recognize it.
5. **Accuracy.** Use only examples you are *certain* are true. A real-world example must be well established. If there's any doubt, use a clearly hypothetical one ("Imagine…") or leave it out. Never invent statistics, names or studies.
6. **Dose.** Deep depth: up to 2 side notes per core concept, prioritizing concepts where the lecture gave no example or analogy (listed in "Not covered in this lecture"). Standard: only for the hardest concepts. Concise: none, unless the student asks.
7. **Never in the retrieval layer.** Quizzes, practice exams, flashcards, study-guide fact sheets and answer keys must not depend on side-note content. Exam prep stays course-grounded.

**Larger outside material** (extra concepts, a fuller outside explanation, background reading) only goes in, on explicit request, a **separate file** `notes/Lxx-<slug>-SUPPLEMENT.md` headed `> ⚠️ Not from your course materials. General explanation by Claude; verify it against your course before relying on it.` In chat (`tutor` mode), teach from the sources first. When you go beyond them, say so explicitly: **"Beyond your lecture:"** …

## 5. Source-locking the other outputs

| Output | Rule |
|---|---|
| Quizzes and practice exams | Every question tests source content. Every answer and explanation cites its source. Distractors should come from errors or confusions the lecture mentions where possible; otherwise they are just plausible wrong options, not new teaching. |
| Flashcards | Front and back come from the note. Put the source tag in `Tags:` (for example `L05 S6`). |
| Study guides | Synthesize only from the notes. When re-teaching a weak topic, use a *different source angle* (the transcript explanation vs the slide, a second lecture example), not new outside content. |
| Grading | Judge answers against the sources and the key. Where the student's answer is correct but goes beyond the course, say so, and don't mark it wrong. |

## 6. Enforcement: the grounding audit

Before saving any note, quiz or guide:
1. Run `python3 .claude/skills/study-notes/scripts/check_sources.py <file> --slides <N> --duration <h:mm:ss>`.
   - Every content line must carry a source tag, sit under a tagged lead-in line (a `**Label:** … [S7]` line or a heading followed by a list or table), or be inside a properly labelled side note.
   - It reports untagged lines, any `[Added]` tag, side notes missing their `Illustrates:` anchor, and (with `--slides` and `--duration`) slides and transcript segments that are never cited.
2. Fix every flagged line: add the correct tag, or delete the content if no source supports it.
3. Spot-check: for each core concept, open the cited slide or timestamp and confirm it actually says what the note claims. A tag on an unsupported claim is worse than no tag.
4. Side-note check: each side note is only an example or analogy (no new concepts or testable facts), has an `Illustrates:` anchor, and nothing in the quiz, flashcards or keys depends on it.
5. The Professor Review's **Source fidelity** criterion must score **5/5**. This is a hard gate.
