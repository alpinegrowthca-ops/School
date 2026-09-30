# School: Study Workspace

This repository is a personal study system. Claude acts as a study coach and note-taker for university courses.

## How to work here

- For **any** request involving course material (slides, recordings, transcripts, readings), notes, quizzes, practice exams, flashcards, study guides or exam prep, use the **`study-notes` skill** (`.claude/skills/study-notes/SKILL.md`). Follow its pipeline and quality checklist.
- Each course lives in `courses/<COURSE-CODE>/`, with `_course.md` as its hub. **Read the hub first** when working on a course. It holds the exam dates and formats, exam intelligence, and the mastery tracker.
- New course: run the skill's `setup` mode (ideally with the syllabus).
- Raw files go in `courses/<COURSE>/sources/` (slides, recordings, transcripts, readings, past exams).
- For **ad storyboards** (script → clip-by-clip image/video prompts, voice and sound direction), use the **`storyboard-ai-ad` skill** (`.claude/skills/storyboard-ai-ad/SKILL.md`). Ad projects live in `ads/<PRODUCT>/` with raw research in `sources/`. For DESIRE, the skill's `references/desire-product-brief.md` holds the product locks and claim guardrails.

## Standing preferences

- Notes are for **learning, not just reading**: always include check-yourself questions, a summary, and "explain it back" prompts.
- Cite sources inline (`[S12]` slide, `[12:34]` timestamp, `[R: …]` reading). Mark outside additions `[Added]` and uncertainties `[VERIFY]`. Never invent course-specific facts.
- Keep answer keys for practice exams in separate `-KEY.md` files.
- After creating notes, also create the post-lecture quiz and flashcards, and update the course hub.
- Academic integrity: help me learn. Don't complete graded work for submission.

## Personal settings (edit these)

- Name / pronouns: <optional>
- Program / year: <e.g., 2nd-year Biology>
- Preferred note depth: <standard | very detailed | concise>
- Flashcard app: Anki
- Weekly study hours available: <…>
- Things I struggle with: <e.g., math-heavy derivations, essay structure, test anxiety>
