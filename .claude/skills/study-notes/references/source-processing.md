# Processing Course Sources

The goal is to capture everything examinable from every source, then merge it into one coherent note. Each source type has its own strengths and blind spots.

| Source | Strength | Blind spot |
|---|---|---|
| Slides | Structure, official terminology, diagrams, what the professor chose to show | Missing the spoken explanation, the reasoning and the emphasis |
| Recording or transcript | Explanations, examples, emphasis, exam hints, answers to student questions | Rambling, no structure, transcription errors in technical terms |
| Readings or textbook | Depth, precise definitions, extra examples, end-of-chapter problems | Often broader than what's examined |
| Student's own notes | What the student noticed and found confusing; board work | Incomplete |
| Past exams and problem sets | *What is actually tested and how* | None. Treat these as the highest-signal source for exam style |

## Slides

### PDF
- Read them directly with the Read tool, in page ranges of 20 or fewer (`pages: "1-20"`, then `"21-40"`, and so on).
- If the extracted text is sparse (a scanned or image-only deck), or the slides are diagram-heavy, render them to images and look at them:
  `python3 .claude/skills/study-notes/scripts/extract_slides.py lecture.pdf --images /tmp/slides_L05`
  This writes `slide-001.png` and so on. View the images for the slides that carry diagrams, graphs, equations or annotations.

### PPTX
- `python3 .claude/skills/study-notes/scripts/extract_slides.py lecture.pptx > /tmp/L05_slides.md`
- This extracts titles, body text, tables and **speaker notes**. Speaker notes often contain the full explanation the professor reads aloud. Treat them as transcript-grade content.
- To see the visuals, convert to PDF first if LibreOffice is available: `soffice --headless --convert-to pdf lecture.pptx`. Then use `--images`.
- Requires `pip install python-pptx` (and `pymupdf` for PDF rendering). The script prints install hints if they're missing.

### Reading slides well
- The slide title is usually the concept. Bullets are cues, not explanations. Expand them using the transcript or reading.
- For every **diagram or graph**, state what's on the axes or components, what relationship it shows, and why it matters. Recreate it (Mermaid, ASCII, or a table) if it's central.
- Equations: transcribe to LaTeX, define every symbol, and state the conditions under which each one applies.
- "Review", "recap" or "summary" slides reveal what the professor considers core. Mark those topics as high priority.
- Slides that appear in several lectures, or questions posed on slides ("Why might…?"), are strong exam signals.

## Recordings (audio or video)

Claude can't listen to audio directly. Transcribe it first.

```bash
python3 .claude/skills/study-notes/scripts/transcribe.py lecture05.mp4 --model small --out courses/BIO201/sources/transcripts/L05.md
```

- The script uses `faster-whisper` (preferred) or `openai-whisper`, and `ffmpeg` handles the video to audio conversion. Install with `pip install faster-whisper` (plus `ffmpeg` from the system package manager). Model size trades speed for accuracy: `base` is fast, `small` is a good default, and `medium` is best for heavy accents and technical vocabulary.
- Output is Markdown with `[mm:ss]` or `[h:mm:ss]` timestamps per paragraph. Use them as source tags in notes.
- If transcription isn't possible here, ask the student for the platform's auto-transcript. Zoom, Panopto, Microsoft Stream/Teams, Echo360, Kaltura and YouTube all export `.vtt`, `.srt` or `.txt`.
- For long recordings, process the transcript in segments that align with slide sections, not in arbitrary chunks.

## Transcripts (.vtt, .srt, .txt, .docx)

```bash
python3 .claude/skills/study-notes/scripts/transcribe.py lecture05.vtt > /tmp/L05_transcript.md
```

This strips cue numbers and duplicate caption lines and merges captions into timestamped paragraphs of about 30–60 seconds.

### Reading transcripts well
- **Fix technical-term errors** using the slides as a dictionary. For example, "my toe con dree a" becomes "mitochondria". If you can't resolve a term, write `[VERIFY: sounded like "…" at 23:10]`.
- **Strip filler**: logistics, jokes, tangents. Keep anecdotes only if they serve as memorable examples. Keep all logistics about exams (dates, allowed materials, topics) and put them in `_course.md`.
- **Hunt for exam signals.** Search the transcript (case-insensitive) for: `exam`, `test`, `midterm`, `final`, `quiz`, `important`, `key`, `remember`, `make sure`, `common mistake`, `trick`, `always`, `never`, `you need to know`, `I'll ask`, `this is why`. Tag each one with its timestamp.
- **Student questions and the professor's answers** reveal common confusions. Turn them into "Common mistakes" entries and quiz items.
- **Worked examples done live** should be captured step by step, including the professor's commentary on *why* each step is taken.
- **Align to slides**: note transitions ("next slide", "moving on to…", topic changes). Where there's no slide deck, derive the structure from the transcript's topic shifts.

## Readings and textbooks

- Read the chapter's headings, objectives and summary first, to get the frame.
- Pull in: precise definitions, extra examples, and anything the lecture referenced but didn't explain. Tag it `[R: <short title> p.X]`.
- Do not import whole chapters into lecture notes. If a reading is assigned separately, make a separate reading note (same template, with page numbers as tags).
- End-of-chapter problems are free practice material. Reference them in the study guide rather than re-typing them.

## Photos: whiteboard, handwritten notes, textbook pages

- Read the image with the Read tool. Transcribe the content, reconstruct any diagrams, and flag illegible parts `[VERIFY: illegible]`.
- Whiteboard content is high-signal: the professor chose to write it out live.

## Past exams, sample questions, problem sets

- These are the **single best guide to what matters**. Analyze them before writing practice exams:
  - Question types and their proportions, point weights, time per question.
  - Bloom's levels (mostly recall or mostly application?).
  - Recurring topics, and phrasing patterns ("Explain why…", "Compare…", "Calculate…").
  - Whether they use scenario or case-based questions, data interpretation, or proofs.
- Record this analysis in `_course.md` under **Exam intelligence**.
- **Don't reproduce copyrighted questions verbatim** in new practice exams. Write new questions of the same style and difficulty.

## Merging multiple sources into one note

1. The slides are the skeleton (sections and order).
2. The transcript adds explanation, examples and emphasis under each slide's section.
3. The readings add precise definitions and depth where the lecture was thin.
4. The student's notes add their own questions, insights and board work.
5. **When sources conflict**, don't silently pick one. Present both, cite them, and add a `[VERIFY]` gap question. The lecture usually wins for "what's on the exam", but flag it.
6. Keep source tags inline, so the student can jump back to slide 14 or 32:10 in the recording.

## Missing sources

- **Slides only**: note that spoken content is missing. Expand the bullets with `[Added]` explanations and suggest getting the recording or transcript.
- **Recording only**: build the structure from topic shifts, and be extra careful with terminology.
- **Just a topic** ("make notes on the Krebs cycle"): write from general knowledge and mark the whole note `Source: general knowledge. Align to your course materials.` Ask for the course materials so the notes can be matched to the professor's framing and notation.
