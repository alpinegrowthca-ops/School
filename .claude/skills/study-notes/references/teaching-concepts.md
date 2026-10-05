# Teaching Concepts: How to Explain So the Student Actually Understands

Lecture notes that only *record* the lecture leave the student to do the teaching themselves. This file defines how every core concept in a note is *taught*: built up from what the student already knows, explained before it is formalized, tested against examples and non-examples, and protected against the misconceptions students usually form.

Use it for `notes` mode (every core concept), `tutor` mode (guided lessons), and `guide` mode (re-teaching weak topics).

> **Source-lock applies to every rung.** `source-lock.md` overrides this file. In a note, fill each rung **only from the student's slides and transcripts** (or provided course materials), with source tags. When the lecture doesn't supply a rung, don't invent it. List it under **Not covered in this lecture**. The one exception: outside **analogies** (rung 3) and **examples** (rungs 6–7) may be added as clearly labelled `> 💡 **Side note (not from your lecture)` callouts. Teaching quality comes from *how well the lecture's own content is organized and explained*, not from adding material.

---

## 1. Depth levels

Read the student's preferred depth from `CLAUDE.md` (Personal settings) or the course hub's **Learner profile**. A request can override it ("quick notes", "teach me from scratch").

| Depth | When | What every *core* concept gets | Typical length (50–75 min lecture) |
|---|---|---|---|
| **Deep** *(default)* | "Teach me", new or hard material, weak topics, first pass on a lecture | The full Concept Ladder (§2), filled from the sources (derivation or mechanism, examples, non-example, misconceptions and boundaries *as the lecture gives them*), plus up to 2 side notes per core concept | As long as the sources support (often 4,000–9,000 words), written section by section |
| **Standard** | Familiar material, review notes | Ladder rungs 1, 3, 4, 5, 6, 8 and 11 (§2), from the sources; side notes only for the hardest concepts | 2,000–4,500 words |
| **Concise** | Revision sheets, a second pass, when explicitly requested | Definition, one example, the key relationship and the cue questions | 800–2,000 words |

**Core vs supporting.** A *core* concept is one the lecture spends real time on, the exam is likely to test, or later ideas depend on. Supporting facts (dates, minor terms) get a precise one-line definition and a source tag, not the full ladder. Mark the lecture's core concepts in the Roadmap (§3).

Never cut substance to hit a length. If a lecture is dense, the note is long. Write it to the file section by section (see SKILL.md, Step 3) rather than compressing.

---

## 2. The Concept Ladder

Teach each core concept in this order. Each rung has a research reason. Fill each rung from the sources. If the sources don't supply it, record it in "Not covered in this lecture" (or, for analogies and examples, optionally add a side note). Never skip a rung the sources *do* supply just to save space.

| # | Rung | What to write | Why (research) |
|---|---|---|---|
| 1 | **Why it exists** | The problem, question or puzzle this concept answers. "Before X, we couldn't explain…" | Motivation and an anchor for new information (Ausubel's meaningful learning) |
| 2 | **What you need first** | 1–3 prerequisite ideas, as recapped by the professor or linked to earlier notes (`[L02 §3]`). Don't write outside refreshers; if a prerequisite isn't covered in any source, list it in "Not covered" | Elaboration and self-explanation only work when prior knowledge exists (Dunlosky et al., 2013). Mayer's *pre-training* principle: teach the components before the process |
| 3 | **Intuition first** | The lecture's own plain-language explanation (often spoken in the transcript), rephrased clearly with no new claims. Use the professor's analogy if they gave one. Otherwise an outside analogy may go in a **side note**, always saying **where it breaks** | Builds a mental model before formal detail. Saying where it breaks prevents analogy-induced misconceptions |
| 4 | **Precise definition** | The course's exact terminology and definition, cited. Every term in the definition is either already defined or defined here | Exams grade the official wording. Define before use |
| 5 | **How it works** | The mechanism, derivation or argument as a numbered causal chain ("because A, B happens; therefore C"). For math: the derivation's key steps and the *idea* behind each one | Explaining the *how* and *why* is what makes knowledge transferable (self-explanation, Chi et al., 1989) |
| 6 | **Examples (2 or more, varied)** | All the examples the lecture gives. For each, one line on **how it shows the concept**. If the lecture gives fewer than 2, add an outside example in a **side note** (Deep depth), varying the surface features (context, domain) while keeping the principle | Multiple varied examples improve conceptual learning and transfer (Rawson, Thomas & Jacoby, 2014). The Learning Scientists: explain *how* each example illustrates the idea. Varying non-critical features prevents a too-narrow concept (Merrill & Tennyson) |
| 7 | **Non-example (near miss)** | A near miss *from the lecture* that looks like an instance but isn't, plus the **single critical feature** that disqualifies it. If the lecture gives none, an outside one may go in a side note | Matched example/non-example pairs teach the concept's boundary (Carnine, 1980; Tennyson & Cocchiarella, 1986) |
| 8 | **Misconception → refutation** | Only misconceptions the lecture raises (professor warnings, student questions, slide errors): state the wrong idea, say plainly that it's wrong, explain *why* it's tempting, then give the correct idea from the source | Refutation texts correct misconceptions better than texts that just state the correct idea (Guzzetti et al., 1993; Tippett, 2010) |
| 9 | **Representations** | The same idea in at least two forms: words + diagram, words + formula + numbers, timeline, table. Diagrams sit next to the text that explains them | Dual coding (Paivio; the Learning Scientists' six strategies). Mayer's spatial contiguity and signaling principles |
| 10 | **Boundaries and connections** | When it applies and when it doesn't (assumptions, edge cases, limits) *as the sources state them*, and how it links to earlier and later concepts in the course | Knowing the conditions of use is what lets students pick the right tool on the exam (discrimination). Relationship understanding is what revised notes improve most (Luo, Kiewra & Samuelson, 2016) |
| 11 | **Check** | 2–4 **Check yourself** questions: at least one *why/how* and one *apply to a new case*, answers hidden | Retrieval practice locks in what was just taught (Roediger & Karpicke, 2006; Dunlosky et al., 2013). These are the Cornell cue-column questions (Cornell LSC) |

### Ladder template (Markdown)

```markdown
### <Concept name> [S7–S11]

**Why it exists:** <the problem it solves>. [S7]

**What you need first:** <prereq 1> [L03 §2] · <prereq 2>, as recapped in lecture [01:30]

**Intuition (the professor's explanation):** <the lecture's plain-language explanation, rephrased clearly>. [05:10–06:20]

> 💡 **Side note (not from your lecture): analogy.** <outside analogy>. *Where it breaks:* <limit>. *Illustrates:* <concept> ([S8]).

**Definition:** **<Term>**: <precise course definition>. [S8]

**How it works:**
1. <step / cause> → <effect> [12:40]
2. Because <…>, <…>.
3. Therefore <…>.

**Examples**
- *<Example 1, professor's>*: <description>. **Shows the concept because** <link to definition>. [S9]
- *<Example 2 from the lecture, if given>*: <…>. **Shows it because** <…>. [14:20]

> 💡 **Side note (not from your lecture): real-world example.** <outside example, only if certain it's true>. *Illustrates:* <concept> ([S9]).

**Non-example (from lecture):** *<near miss>*: looks like <concept> because <surface similarity>, but **isn't**, because <critical feature missing>. [S10]

> **Misconception:** "<common wrong belief>." This is **wrong**. It's tempting because <reason>. Actually, <correct idea + why>. [S10][15:05]

**Boundaries:** applies when <conditions>. Fails or changes when <conditions>. Connects to <concept> [L06 §1]. [S11]

**Check yourself** *(answer aloud before opening)*
1. Why <…>? <details><summary>Answer</summary>

   …
   </details>
2. A new case: <scenario>. Does <concept> apply? <details><summary>Answer</summary>

   …
   </details>
```

---

## 3. Sequencing a whole note

1. **Roadmap first (an advance organizer).** Before section 1, give a 3–6 line map: the big question, the core concepts in order, and how they connect (a small Mermaid flowchart or numbered outline). Students given an organizing overview before new material learn more, especially when the overview links new ideas to familiar ones (Ausubel; meta-analyses of advance organizer research).
2. **Prerequisites block.** Collect the prerequisites for the whole lecture into one "Before you start" box with one-line refreshers, so the student can fix gaps before reading.
3. **Simple → complex, concrete → abstract → concrete.** Start from a concrete case, generalize to the abstract principle, then apply it back to a new concrete case through a Check-yourself question (a question, not new content), or a side-note example. This is *concreteness fading* (Fyfe, McNeil, Son & Goldstone, 2014), which supports transfer better than staying concrete or starting abstract.
4. **One new idea at a time** (Mayer's segmenting principle). Don't introduce two new terms in the same sentence. Every section should end in a stable state the student can check.
5. **Signal the structure** (signaling principle). Use headings that state the idea, not just the topic ("Km measures substrate needed, not speed" beats "Km"), and "Key idea" callouts.
6. **Cut decoration** (coherence principle). Drop anecdotes, tangents and visuals that don't carry meaning. Keep a story only if it *is* the memorable example.
7. **Close the loop.** The Summary answers the Big question from the header, using the core concepts in order.

---

## 4. Writing explanations that teach

- **Define before use.** Scan each paragraph: any term not yet defined gets defined at first use, or linked to where it is.
- **Causal language.** Prefer "because", "so", "which means", "unlike" over lists of facts. Relationships are what exams test and what revision research shows students miss.
- **Answer the questions a confused student would ask.** After each explanation, ask yourself: *what would a student ask here?* ("Why not just…?", "What if…?", "How is this different from…?"). Then answer it inline *if the sources answer it*, turn it into a Check-yourself question, or list it under "Not covered in this lecture".
- **Show the reasoning of experts.** In worked examples, say *why* this method and not another, and what cue in the problem tells you that.
- **Concrete numbers.** Use the lecture's numeric examples right after the formula. If the lecture gave none, a quick numeric illustration may go in a side note ("if Km = 2 mM and [S] = 2 mM, v₀ = ½Vmax").
- **Name the trap at the moment of risk.** Put the misconception refutation right after the idea it distorts, not in a list at the end. Then *also* gather them in "Common mistakes" for review.
- **Honest uncertainty.** If the sources disagree, show both versions with their tags and add a `[VERIFY]` gap question. Never smooth over a contradiction to make the explanation neater, and never resolve it with outside knowledge.
- **Clarity comes from editing, not adding.** The lecture's spoken explanation is often the best "intuition" material: rephrase it cleanly. Re-sequence and re-present (tables, diagrams). If an explanation is still missing, say so in "Not covered in this lecture", and use a side note only for an analogy or example.

---

## 5. Guided lesson (tutor mode: "teach me X")

Use when the student asks to be taught a concept interactively, or after a quiz reveals a weak topic. Teach in **chunks** (one ladder at a time), and keep the student generating throughout:

1. **Probe.** Ask 1–2 quick questions to find what they already know, and their misconceptions. Even wrong guesses prime learning (the pretesting effect).
2. **Teach one chunk.** Rungs 1–5 of the ladder, briefly. Use their answers from the probe: build on what they know, and refute what they got wrong.
3. **Check.** One why-question. Wait for the answer. If it's wrong, re-explain from a different angle (another source explanation, a diagram, a numeric case, or an analogy labelled "outside your lecture"), not by repeating the same words.
4. **Apply.** A new example or problem. For procedures, go worked → faded → independent.
5. **Discriminate.** "Is this an example or a non-example? Why?" or "Which concept applies here?"
6. **Teach-back.** The student explains the concept as if teaching a classmate. Actually explaining to others produces better long-term learning than only preparing to teach (Fiorella & Mayer, 2013). Point out gaps, jargon used without understanding, and missing causal links. They revise once.
7. **Wrap up.** 2–3 retrieval questions, a one-line summary in *their* words, and a note in the tracker. Schedule a re-check in 1–2 days.

---

## 6. Self-check before saving a teaching note

- [ ] Every rung that the sources supply is filled, with source tags. Rungs the sources don't supply are listed under "Not covered in this lecture", never invented.
- [ ] No term is used before it is defined or linked.
- [ ] Every lecture example has a "shows it because" line. Core concepts with fewer than 2 lecture examples get a side-note example (Deep depth).
- [ ] Each misconception the lecture raises is stated explicitly, refuted, and explained.
- [ ] All outside analogies and examples are in labelled side notes, with "Where it breaks" (analogies) and "Illustrates:".
- [ ] There's a Roadmap at the top and a "Before you start" prerequisites box.
- [ ] Concrete → abstract → concrete: each principle is applied back to a new case.
- [ ] A student who missed the lecture could learn the material from this note alone.

## Sources

- Ausubel, D. P. (1960). The use of advance organizers in the learning and retention of meaningful verbal material. *Journal of Educational Psychology*, 51. Updated meta-analysis: https://www.ideals.illinois.edu/items/20405
- Carnine, D. W. (1980). Relationships between stimulus variation and the formation of misconceptions. *Journal of Educational Research*. Also Merrill & Tennyson; Tennyson & Cocchiarella (1986), *Review of Educational Research*: https://theelearningcoach.com/elearning_design/examples-and-nonexamples/
- Chi, M. T. H., Bassok, M., Lewis, M. W., Reimann, P., & Glaser, R. (1989). Self-explanations: How students study and use examples in learning to solve problems. *Cognitive Science*, 13.
- Fiorella, L., & Mayer, R. E. (2013). The relative benefits of learning by teaching and teaching expectancy. *Contemporary Educational Psychology*, 38. https://alexandria.ucsb.edu/lib/ark:/48907/f3ms3qvb
- Fyfe, E. R., McNeil, N. M., Son, J. Y., & Goldstone, R. L. (2014). Concreteness fading in mathematics and science instruction: A systematic review. *Educational Psychology Review*, 26.
- Guzzetti, B. J., Snyder, T. E., Glass, G. V., & Gamas, W. S. (1993). Promoting conceptual change in science: A comparative meta-analysis. *Reading Research Quarterly*, 28. Tippett, C. D. (2010). Refutation text in science education: A review. *International Journal of Science and Mathematics Education*, 8. Overview: https://link.springer.com/article/10.1007/s10648-021-09656-z
- Mayer, R. E. *Multimedia Learning* (pre-training, segmenting, signaling, coherence and spatial-contiguity principles).
- Rawson, K. A., Thomas, R. C., & Jacoby, L. L. (2014). The power of examples: Illustrative examples enhance conceptual learning of declarative concepts. *Educational Psychology Review*, 27, 483–504.
