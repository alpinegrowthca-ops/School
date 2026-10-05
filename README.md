# School: A Claude Study System

A Claude Code skill that turns **lecture slides, recordings, transcripts and readings** into detailed, exam-ready notes **built only from your own course material** (every line cites a slide or timestamp; outside examples and analogies appear only as labelled side notes), then builds **quizzes, full practice exams with answer keys, Anki flashcards, study guides and spaced study plans**.

It is built on research from cognitive psychology and university learning centers. The full sources are in [`learning-science.md`](.claude/skills/study-notes/references/learning-science.md).

| Principle | Research | What the skill does |
|---|---|---|
| Source-locked notes | Your rule | No made-up concepts or explanations; every line cites `[S#]` or `[mm:ss]`; outside examples and analogies only in 💡 side notes; gaps listed under "Not covered in this lecture"; enforced by `check_sources.py` |
| Professor-level standard | Bransford et al. 2000 (*How People Learn*); Chi, Feltovich & Glaser 1981 | Notes built on core principles, with epistemic labels, "How do we know?" evidence, derivations, recognition cues, an examiner's view, and a 10-point Professor Review before saving |
| Teaching concepts | Ausubel; Rawson et al. 2014; Tennyson & Cocchiarella; Guzzetti et al. 1993; Fyfe et al. 2014; Fiorella & Mayer 2013 | Concept Ladder per core concept: why → intuition → definition → how → varied examples → non-example → misconception refuted → check; Deep/Standard/Concise depth |
| Retrieval practice | Roediger & Karpicke 2006; Karpicke & Blunt 2011; Adesope et al. 2017 | Every note has hidden-answer cue questions; next-day quizzes (rereading wins at 5 min but loses at 1 week); practice exams with explanations |
| Spacing | Cepeda et al. 2008; Dunlosky et al. 2013 | Expanding-interval study plans; Anki export |
| Interleaving | Rohrer & Taylor 2007; The Learning Scientists | Cumulative, mixed-topic quizzes and exams (without switching too often) |
| Six strategies combined | The Learning Scientists | Session loop: retrieve → repair with elaboration, examples and visuals → retrieve again |
| Cornell method | Pauk; Cornell LSC, UNE, Laurier guides | Record → Questions/Reduce → Recite (aloud) → Reflect → Review (10 min weekly), plus a summary |
| Complete notes + review | Kiewra; U. Michigan CRLT (DeZure et al. 2001) | Merges slides + transcript + readings (students capture about ⅓ on their own); reviewing complete notes works even when someone else wrote them |
| Revise, don't recopy | Luo, Kiewra & Samuelson 2016 | "What your notes missed" + revision task; pause-and-revise for recordings |
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
│   ├── source-lock.md           # source rules (override everything), side notes, grounding audit
│   ├── learning-science.md      # the research, with sources
│   ├── expert-standard.md       # professor-level standard + Professor Review rubric
│   ├── teaching-concepts.md     # depth levels, Concept Ladder, guided lessons
│   ├── source-processing.md     # slides, recordings, transcripts, readings, past exams
│   ├── note-formats.md          # Cornell-hybrid notes, matrices, diagrams, math, flashcard rules
│   ├── practice-exams.md        # blueprints, Bloom's, MCQ rules, keys, rubrics, grading
│   ├── study-planning.md        # spacing, session design, mastery tracker, exam wrappers
│   └── subject-playbooks.md     # STEM, bio/med, CS, humanities, social science, law, languages
├── templates/                   # lecture-note, quiz, practice-exam, exam-key, flashcards,
│                                # study-guide, course-hub, exam-wrapper
├── examples/example-lecture-note.md   # the quality bar
└── scripts/
    ├── check_sources.py         # grounding audit: untagged lines, [Added], side notes, slide/transcript coverage
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
Skim the slides before class → take your own notes in class → master note + revise your notes and recite the same day → closed-book quiz the next day → daily Anki → a 10-minute weekly Cornell review plus a cumulative quiz → practice exams 6 and 2 days before each exam.

## Academic integrity
This system is for learning. It won't do graded work for submission. Check your course's AI policy.
