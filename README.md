# School: A Claude Study System

A Claude Code skill that turns **lecture slides, recordings, transcripts and readings** into detailed, exam-ready notes, then builds **quizzes, full practice exams with answer keys, Anki flashcards, study guides and spaced study plans**.

It is built on research from cognitive psychology and university learning centers. The full sources are in [`learning-science.md`](.claude/skills/study-notes/references/learning-science.md).

| Principle | Research | What the skill does |
|---|---|---|
| Retrieval practice | Roediger & Karpicke 2006; Karpicke & Blunt 2011; Adesope et al. 2017 | Every note has hidden-answer cue questions; quizzes after every lecture; practice exams with explanations |
| Spacing | Cepeda et al. 2008; Dunlosky et al. 2013 | Expanding-interval study plans; Anki export |
| Interleaving | Rohrer & Taylor 2007 | Cumulative, mixed-topic quizzes and exams |
| Cornell method | Walter Pauk, Cornell University | Record → question → recite → reflect → review, with a summary |
| Complete + revised notes | Kiewra (students capture about ⅓ of key points) | Merges slides + transcript + readings; flags gaps |
| Generative, not verbatim | Mueller & Oppenheimer 2014 and replications | "Explain it back" prompts; own-words synthesis |
| Worked and faded examples | Sweller (cognitive load theory) | Step-by-step examples, then partial, then independent |
| Matrix notes, dual coding | Kiewra (SOAR); Paivio; Mayer | Comparison tables, Mermaid diagrams |
| Metacognition | Bjork; Nelson & Dunlosky; Oakley; Lovett (CMU exam wrappers) | Confidence ratings, error log, exam wrappers |
| Good test items | Bloom's revised taxonomy; Haladyna et al. 2002 | Blueprinted exams, misconception-based distractors |
| Good flashcards | Wozniak, *20 Rules of Formulating Knowledge* | Atomic, why- and contrast-cards, cloze |

## What's in here

```
.claude/skills/study-notes/
├── SKILL.md                     # the skill: modes, pipeline, quality checklist
├── references/                  # loaded on demand
│   ├── learning-science.md      # the research, with sources
│   ├── source-processing.md     # slides, recordings, transcripts, readings, past exams
│   ├── note-formats.md          # Cornell-hybrid notes, matrices, diagrams, math, flashcard rules
│   ├── practice-exams.md        # blueprints, Bloom's, MCQ rules, keys, rubrics, grading
│   ├── study-planning.md        # spacing, session design, mastery tracker, exam wrappers
│   └── subject-playbooks.md     # STEM, bio/med, CS, humanities, social science, law, languages
├── templates/                   # lecture-note, quiz, practice-exam, exam-key, flashcards,
│                                # study-guide, course-hub, exam-wrapper
├── examples/example-lecture-note.md   # the quality bar
└── scripts/
    ├── extract_slides.py        # PPTX/PDF to Markdown (+ speaker notes, tables, page images)
    ├── transcribe.py            # audio/video to timestamped transcript (whisper); cleans .vtt/.srt
    ├── flashcards_to_anki.py    # deck.md to Anki-importable TSV (Basic + Cloze)
    ├── study_schedule.py        # spaced, interleaved day-by-day plan to an exam
    └── requirements.txt
claude-project/                  # instructions for using this in a claude.ai Project instead
courses/                         # your courses live here (one folder per course)
CLAUDE.md                        # workspace instructions for Claude Code (edit your preferences)
```

## Setup (Claude Code)

1. Clone this repo and open it with Claude Code (`claude` in the repo folder). The skill is picked up automatically from `.claude/skills/`.
   - To use it in **every** project, copy the folder to `~/.claude/skills/study-notes/`.
2. Optional helpers:
   ```bash
   pip install -r .claude/skills/study-notes/scripts/requirements.txt
   # plus ffmpeg for video files (macOS: brew install ffmpeg · Ubuntu: sudo apt install ffmpeg)
   ```
3. Edit the **Personal settings** section in `CLAUDE.md`.

## Using it

Type `/study-notes` or just ask in plain language:

| You say | Claude does |
|---|---|
| "Set up BIO201, here's the syllabus" | Creates `courses/BIO201/` and a hub with exam dates, formats and objectives |
| "Make notes for lecture 5" + slides/recording/transcript | Master note + 10–15 question quiz + flashcards + hub update |
| "Quiz me on L01–L05" | Interactive quiz, one question at a time, with confidence ratings |
| "Make practice midterm 1" | Blueprinted exam + separate answer key with explanations and rubrics |
| "Make flashcards for L05" | Atomic cards in `deck.md`, exported to `deck.tsv` for Anki |
| "Make a study guide for the final" | Cross-lecture synthesis, priorities, matrices, formula sheet, self-test |
| "My exam is Oct 20, make a plan" | Spaced, interleaved day-by-day schedule |
| "Grade this" + your answers | Partial credit, error types, confident-error alerts, targeted re-quiz |
| "I don't get competitive inhibition" | Socratic or Feynman tutoring with worked → faded examples |
| "I got my midterm back" | Exam wrapper and adjustments to your plan |

### Lecture recordings
Claude can't hear audio directly, so either:
- run `python3 .claude/skills/study-notes/scripts/transcribe.py lecture.mp4` (local Whisper), or
- download the auto-transcript from Zoom, Panopto, Teams, Echo360 or YouTube (`.vtt`/`.srt`) and give Claude that file.

### Suggested weekly routine
Skim the slides before class → notes the same day → closed-book quiz the next day → daily Anki → a weekly cumulative quiz → practice exams 6 and 2 days before each exam.

## Academic integrity
This system is for learning. It won't do graded work for submission. Check your course's AI policy.
