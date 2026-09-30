# Using this system in a claude.ai Project (web / desktop / mobile app)

If you study in **Claude Code**, you don't need this folder: the skill in `.claude/skills/study-notes/` loads automatically. This folder is for when you'd rather use a **Project** on claude.ai.

## Option A: Project instructions + knowledge files (works on every plan with Projects)

1. On claude.ai, go to **Projects → Create project** (for example "BIO201 Study" or one project for all of school).
2. Open **Set project instructions** and paste everything below the line in `PROJECT_INSTRUCTIONS.md`.
3. Under **Project knowledge**, upload these files from `.claude/skills/study-notes/`:
   - `references/learning-science.md`
   - `references/note-formats.md`
   - `references/practice-exams.md`
   - `references/study-planning.md`
   - `references/subject-playbooks.md`
   - `references/source-processing.md`
   - `templates/lecture-note.md`
   - `examples/example-lecture-note.md`
   - (optional) the other templates you want Claude to follow exactly
4. Per course, also upload: the **syllabus**, **past exams** or sample questions, and the lecture slides and transcripts as the term goes on.
5. Start chatting: "Here are the L05 slides and the transcript. Make my notes." · "Quiz me on L01–L05." · "Make practice midterm 1."

Tip: create one Project per course so the knowledge stays focused and Claude doesn't mix up courses.

## Option B: Upload the skill itself (claude.ai with Skills enabled)

If your plan has **Settings → Capabilities → Skills**, you can upload this as a custom skill:

1. Zip the `study-notes` folder, with `SKILL.md` at the top level of the folder:
   ```bash
   cd .claude/skills && zip -r study-notes.zip study-notes
   ```
2. Settings → Capabilities → Skills → **Upload skill** → choose `study-notes.zip`.
3. It then activates automatically whenever you share course material or ask for notes, quizzes or exams. Claude can run the helper scripts in its code-execution sandbox (for example to convert flashcards to an Anki file).
