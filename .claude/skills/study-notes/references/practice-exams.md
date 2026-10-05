# Writing Quizzes and Practice Exams

A practice test helps most when it makes the student **retrieve and apply**, looks like the real exam, and comes with **feedback that explains**. Practice testing beats restudying across formats (g ≈ 0.51; Adesope et al., 2017), with larger gains when the final test is more than a day away. Format-matching and feedback add modest gains on top. Feedback is essential for multiple choice, because without it students can remember the wrong option they chose (Butler & Roediger, 2008).

## 0. Source-lock for questions

- Every question tests a concept **from the sources** (slides, transcript, provided materials), and every answer and explanation cites its source tag.
- Application questions may use **new numbers or scenarios** to apply a principle *from the lecture*. That's practice, not new content. The principle and the solution method must come from the sources.
- **Nothing depends on side-note content.** Don't test outside examples or analogies.
- Distractors: prefer errors and confusions the lecture mentions (professor warnings, student questions). Otherwise use plausible wrong options, but never "teach" new facts through them.
- Run `scripts/check_sources.py` on quiz and key files: answers inside `<details>` and key explanations must carry tags.

## 1. Build a blueprint first (for full exams)

Before writing any question, fill this in (in the KEY file header):

```markdown
| Topic (lecture) | Lecture time / emphasis | Exam signals | Student mastery | # Qs | Points |
|---|---|---|---|---|---|
| Enzyme kinetics (L05) | 1 full lecture, 3 signals | "derive MM" | shaky | 4 | 18 |
| ... | | | | | |
```

- **Scope**: only the topics the exam covers (from the syllabus or professor).
- **Weighting**: proportional to lecture time, plus extra weight for exam signals and for learning objectives stated in the syllabus.
- **Format**: match the real exam (from `_course.md` → *Exam intelligence*). The default, if unknown, is a 50-minute midterm with 15 MCQ, 5 short answer and 2 multi-part problems or essays.
- **Bloom's mix** (adjust to past exams):

| Level | Share | Stem starters |
|---|---|---|
| Remember | ~15–20% | Define, identify, list, state |
| Understand | ~25–30% | Explain why, summarize, classify, give an example of, interpret this graph |
| Apply | ~25–30% | Calculate, predict, use X to solve, what would happen if |
| Analyze | ~15–20% | Compare, distinguish, what's the flaw, which factor explains, organize |
| Evaluate / Create | ~5–10% | Justify, critique, design an experiment, propose, which is the best approach and why |

## 2. Question types and when to use them

| Type | Best for | Notes |
|---|---|---|
| **Free recall / brain dump** | Start of any quiz. "Write everything you remember about X" | The most effortful format. It shows exactly what you can't yet generate, and it trains organizing ideas the way essays and long answers require |
| **Short answer** | Definitions with explanation, why/how questions | Answerable in 1–4 sentences, with a model answer and key points for grading |
| **Multiple choice** | Wide coverage, discrimination between close concepts | Follow the MCQ rules below. Well-built MCQs with competitive distractors are a strong practice format (g ≈ 0.70 in Adesope et al., 2017), and always need feedback |
| **Multi-part problem** | Quantitative and procedural skills | Scaffold (a), (b), (c) from easier to harder. Make later parts independent of earlier numeric answers where possible, or give "if you couldn't get (a), use X" |
| **Data / graph / case interpretation** | Application and analysis | Give a novel scenario, table or figure (described or drawn in Mermaid/ASCII) |
| **Compare / contrast** | Confusable concepts | Often the professor's favourite essay question |
| **Example / non-example classification** | Concept boundaries | "Is this a case of X? Why or why not?" Use near misses that lack one critical feature |
| **Error-finding** | Misconceptions | "A student claims … Identify and correct the error" |
| **Explain-to-a-novice** | Deep understanding | Graded on accuracy, completeness and absence of jargon |
| **Essay** | Humanities and social sciences, synthesis | Give a rubric: thesis, evidence, analysis, counterargument, organization |
| **True/False with justification** | Quick checks | Always require "and why". Plain T/F is weak |
| **Ordering / sequence** | Processes, timelines | |
| **Fill-in / cloze** | Terminology | Use sparingly on exams. Better suited to flashcards |

## 3. Multiple-choice rules (after Haladyna, Downing & Rodriguez)

**Stem**
- Put the whole problem in the stem. A student should be able to answer it *without seeing the options*.
- Phrase it positively. If a NOT or EXCEPT is truly necessary, write it in **bold caps**.
- Test one idea. Include no unnecessary information, unless the item deliberately tests picking out what's relevant.
- Prefer scenario-based stems ("A patient presents with…", "A firm raises its price and…") over "Which of the following is true about X?"

**Options**
- **Exactly one clearly best answer.** Have it checked by working the problem independently.
- **3–4 options.** Three plausible options beat five with two silly ones.
- **Distractors come from real misconceptions**: the common mistakes the professor mentioned, student questions in the transcript, classic errors (sign errors, unit errors, confusing correlation with causation, reversing a relationship, a right answer to a different question).
- All options are similar in length, grammar and level of detail. The correct answer must not be the longest or most precise.
- Put options in a logical order (numeric ascending, alphabetical). Vary the correct letter position evenly. Aim for a roughly equal A/B/C/D distribution across the exam.
- Avoid "all of the above", "none of the above", "both A and C", absolutes like "always/never" as giveaways, and grammatical cues.
- No trick questions. Difficulty should come from the concept, not the wording.

**The key must explain each option:** why the correct one is right and why *each* distractor is wrong ("B is tempting if you confuse Km with Vmax…").

## 4. Difficulty calibration

- Mix about 30% accessible, 50% medium and 20% hard (the ones that separate A from B students).
- Hard does not mean obscure. Hard means multi-step, novel context, or combining two concepts.
- **Transfer**: at least 30% of questions should use a scenario, dataset or example that is *not* in the notes. Recognizing the lecture's own example is not understanding.
- **Interleave**: don't group questions by lecture. Mix them, so the student has to identify which concept applies.

## 5. Exam file format

**`<exam>-practice-N.md`** (questions only):

```markdown
# <COURSE> <Exam name>: Practice Exam N
**Time:** 50 min · **Total:** 100 pts · **Allowed:** calculator, 1 formula sheet · **Scope:** L01–L09

**Instructions:** Treat this like the real exam: timed, closed notes, no peeking at the KEY. Before checking answers, mark each question with your confidence (1 = guessing … 5 = certain).

## Part A: Multiple choice (2 pts each)
**1.** <stem>
- A. …
- B. …
- C. …
- D. …

Confidence: __

## Part B: Short answer
**16.** (4 pts) …

## Part C: Problems
**21.** (12 pts) …
(a) … (b) … (c) …
```

**`<exam>-practice-N-KEY.md`** (answers):

```markdown
# KEY: <Exam name> Practice Exam N
## Blueprint
<table from §1>

## Answers
**1. C**: <why C is correct>. *A* is wrong because … *B* is a common confusion of … *D* … · Topic: L05 enzymes · Bloom: Apply · Source: [S14][31:05]

**16.** Model answer: … · **Grading (4 pts):** +1 names X, +2 explains mechanism Y, +1 gives example. · Topic … · Source …

**21.** Full worked solution with reasoning for each step; partial-credit rubric per part.

## After you grade
- Score by topic → update the mastery tracker.
- Any confidence ≥4 that was wrong → put it in the error log with the misconception.
- Send the misses to `grade` mode for a targeted re-quiz in 1–2 days.
```

## 6. Quizzes (lighter weight)

- **Post-lecture quiz (10–15 Qs)**: start with 1 free-recall prompt, then about 5 short answer (with at least 2 why/how), about 3 application, and 2–3 MCQ. Put answers in `<details>` blocks inline with an explanation and a source tag.
- **Pre-lecture warm-up (3–5 Qs)**: based on the upcoming slides. The student guesses before class (pretesting effect), and the answers are revealed in the note.
- **Cumulative quiz (15–25 Qs)**: interleaved across all lectures to date, weighted toward topics due for review and those marked shaky or weak.
- **Targeted re-quiz**: only the missed concepts, *reworded and in new contexts*. Never repeat the exact same question, or the student learns the answer rather than the concept.

## 7. Interactive quizzing in chat ("quiz me")

1. Ask one question. Don't show options for questions that can be answered free-recall.
2. Wait for the answer. Ask "Confidence 1–5?" if they didn't give it.
3. Give feedback: correct or incorrect, the explanation, and the source. If it was a confident error, say so explicitly and give a contrastive explanation.
4. If it was wrong, ask a follow-up on the same concept from a different angle before moving on.
5. After 10 questions (or when the student stops): score, weak concepts, and an update to the tracker. Suggest when to re-quiz.

## 8. Grading written answers

- Grade against key points, not wording. Award partial credit.
- Feedback format: **Score**, **What you got right**, **What's missing or wrong**, **Model answer**, **One thing to fix next time**.
- Classify errors (knowledge gap / misconception / application / misread / time) in `review/error-log.md`:

```markdown
| Date | Source | Q | Topic | Error type | Confidence | What I thought | Correct idea | Re-test on |
|---|---|---|---|---|---|---|---|---|
```
