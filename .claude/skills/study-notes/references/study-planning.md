# Study Planning, Mastery Tracking and Exam Strategy

## 1. The weekly rhythm (during the semester)

This is the Cornell "review" step combined with spaced retrieval.

| When | What | Time |
|---|---|---|
| Before lecture | Skim the slides and attempt the warm-up questions (pretesting) | 10 min |
| Same day | Generate the master note from slides and transcript, and fix gaps | 20–30 min |
| +1 day | Take the post-lecture quiz **closed-book**, then do the "Explain it back" prompts | 20 min |
| Daily | Anki flashcard reviews (all courses) | 15–30 min |
| Weekly | Cumulative interleaved quiz over *all* lectures so far; re-study only the misses | 30–45 min |
| After problem sets / labs | Error log, plus redo any wrong problem 3 days later without looking | 15 min |

## 2. Spacing: how far apart?

From Cepeda et al. (2008), the best gap between reviews is roughly 10–20% of the time until the test (larger for close tests, smaller for distant ones). For practical use:

| Days until exam | Review gaps for each topic |
|---|---|
| 28+ | +1d, +7d, +14d, then weekly |
| 14–27 | +1d, +4d, +9d, then every 4–5 days |
| 7–13 | +1d, +3d, +6d |
| 3–6 | +1d, +2d (and interleave everything) |
| < 3 | Triage: highest-priority topics, practice questions only |

Each review is a **retrieval session** (quiz, flashcards, blank-page recall, practice problems), never a re-read.

## 3. Building an exam study plan (`plan` mode)

Inputs: the exam date and time, the topics in scope, hours available per day (ask), mastery from the tracker, and other deadlines.

Algorithm:
1. **Rank topics**: priority = exam weight (lecture time + exam signals + syllabus objectives) × (1 − mastery). Mastery levels: `new` 0, `weak` 0.25, `shaky` 0.5, `solid` 0.8, `mastered` 1.
2. **Schedule each topic 3 or more times** at expanding intervals (§2), with its first session as early as possible.
3. **Interleave**: each session covers 2–4 different topics, mixing weak and solid ones.
4. **Session structure** (50 min, then a 10 min break; Oakley's focused and diffuse modes):
   - 5 min: blank-page recall of the topic (write everything you remember)
   - 25 min: practice questions or problems (mixed)
   - 10 min: check answers, then re-study *only* the misses from the notes
   - 10 min: flashcards or error-log re-tests
5. **Practice exams**: a full timed one 5–7 days out, and another 2–3 days out. Review each with `grade` mode and adjust the plan.
6. **Final 24 hours**: light review of the formula sheet and error log, one short mixed quiz, a normal bedtime. Sleep consolidates memory, and an all-nighter costs more than it gains.
7. Output a day-by-day table and put it in `_course.md` or `guides/study-plan.md`:

```markdown
| Date | Session (min) | Topics (interleaved) | Activities | Done |
|---|---|---|---|---|
| Mon 10/06 | 50 | L01, L04, L07 | Blank recall L04 → Q-cumulative #1–15 → Anki | [ ] |
```

`scripts/study_schedule.py` can generate the skeleton automatically.

## 4. Mastery tracker (in `_course.md`)

```markdown
| Topic | Lecture | Status | Last tested | Score | Confidence calibration | Next review |
|---|---|---|---|---|---|---|
| Michaelis–Menten | L05 | shaky | 10/03 | 3/5 | overconfident | 10/06 |
```

Status rules:
- `new`: not yet tested.
- `weak`: < 50% on the last test.
- `shaky`: 50–79%, or correct but with confidence ≤ 2.
- `solid`: ≥ 80% on a test at least 2 days after studying (delayed judgment).
- `mastered`: `solid` on two spaced tests, including one in a novel or interleaved context.

Only **delayed** test performance counts. "I just read it and it makes sense" is not evidence (the fluency illusion).

## 5. Exam wrapper (after every real exam and every full practice exam)

From Marsha Lovett's work at Carnegie Mellon. Use `templates/exam-wrapper.md`. It has three parts:
1. **Preparation**: how many hours, which activities (rereading? practice problems? flashcards?), and when (spread out or crammed?).
2. **Error analysis**: count the points lost per error type (knowledge gap, misconception, application, misread, time).
3. **Plan**: 2–3 specific changes for the next exam. Put them in `_course.md` and **show them at the start of the next exam's study plan**.

## 6. Exam-day strategy (put in the study guide)

- **Brain dump**: in the first 2 minutes, write the formulas, mnemonics and key frameworks on scratch paper, if that's allowed.
- **Triage**: skim the whole exam, then do the easy, high-point questions first. Budget time as points ÷ total × minutes.
- **MCQ**: answer the stem in your head *before* reading the options, eliminate options, and change an answer only for a concrete reason.
- **Written answers**: lead with the direct answer, then support it. Use the course's terminology. Show all work for partial credit.
- **Stuck**: mark it and move on, then come back. Diffuse-mode thinking often cracks it.
- **Last 5 minutes**: check units, signs, and that every question is answered.

## 7. Anxiety and wellbeing (brief, practical)

- Retrieval practice under realistic conditions is itself anxiety-reducing, because the exam feels familiar.
- Expressive writing (10 minutes writing about worries just before the exam) has been shown to reduce test anxiety.
- Sleep, some exercise and regular meals during exam weeks are part of the plan, not optional extras.
- If the student seems overwhelmed, help them triage to the highest-yield topics and point them to their school's academic support or counselling services.
