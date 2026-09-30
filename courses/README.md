# Courses

One folder per course, for example `courses/BIO201/`. The easiest way to create one is to ask Claude:

> "Set up a new course BIO201" (attach or point to the syllabus if you have it)

Layout created by the `study-notes` skill:

```
courses/<COURSE>/
├── _course.md      # hub: exam dates and formats, lecture list, mastery tracker, study plan
├── sources/        # put raw files here
│   ├── slides/
│   ├── recordings/
│   ├── transcripts/
│   ├── readings/
│   └── past-exams/
├── notes/          # L01-<topic>.md ...
├── quizzes/        # Q-L01.md, cumulative quizzes
├── exams/          # practice exams + separate -KEY.md files
├── flashcards/     # deck.md (edit this) and deck.tsv (import into Anki)
├── guides/         # study guides, formula sheets, study plans
└── review/         # graded attempts, error-log.md, exam wrappers
```

Tip: large recordings and copyrighted slide decks can stay out of git. See the `.gitignore` at the repo root.
