# BIO201 L05: Enzyme Kinetics

<!-- EXAMPLE of the expected quality bar. Content is illustrative; source tags reference an imaginary lecture. -->

**Date:** 2026-09-29 · **Professor:** Dr. Rivera · **Unit/Exam:** Midterm 1
**Sources:** Slides `L05-enzymes.pdf` [S#] · Transcript `L05.vtt` [mm:ss] · Reading Lehninger Ch. 6 [R]
**Big question:** How fast does an enzyme-catalyzed reaction go, and how can we measure and change that speed?

**Learning objectives**
- By the end, I can explain what Km and Vmax mean physically.
- By the end, I can predict how different inhibitors change a Michaelis–Menten or Lineweaver–Burk plot.
- By the end, I can calculate reaction velocity from [S], Km and Vmax.

---

## 1. The Michaelis–Menten model [S3–S8]

- Enzymes (E) bind substrate (S) to form an **enzyme–substrate complex (ES)**, which converts to product (P). [S3]
  $$E + S \underset{k_{-1}}{\overset{k_1}{\rightleftharpoons}} ES \xrightarrow{k_{cat}} E + P$$
- At low [S], velocity rises almost linearly with [S]. At high [S], it levels off at **Vmax** because every enzyme is occupied (**saturation**). [S4][06:20]
- **Vmax**: the maximum reaction velocity when the enzyme is fully saturated. *In plain words:* the enzyme's top speed at a given enzyme concentration. *Example:* doubling the amount of enzyme doubles Vmax. [S5]
- **Km (Michaelis constant)**: the substrate concentration at which $v_0 = \tfrac{1}{2}V_{max}$. *In plain words:* how much substrate is needed to get the enzyme half-busy. A **lower Km generally means higher apparent affinity**. *Example:* hexokinase (Km ≈ 0.1 mM for glucose) is half-saturated at far lower glucose than glucokinase (Km ≈ 10 mM). [S6][R: p.203] [Added: values]

$$v_0 = \frac{V_{max}[S]}{K_m + [S]}$$

| Symbol | Meaning | Units |
|---|---|---|
| $v_0$ | initial reaction velocity | µM/s |
| $V_{max}$ | maximum velocity (saturated) | µM/s |
| $[S]$ | substrate concentration | µM or mM |
| $K_m$ | [S] at half Vmax | same as [S] |

*Use when:* initial rates are measured ([P] ≈ 0), [S] ≫ [E], at steady state for ES. *Assumption:* a single substrate and no significant reverse reaction.

> **Key idea:** Km is a *concentration*, not a rate. It tells you where the curve bends, while Vmax tells you where it tops out.

> **Exam signal [11:45]:** "I want you to be able to derive what happens to $v_0$ when [S] equals Km. That's a classic exam question."

**Worked example: velocity at a given [S]** [S8][14:10]
*Given:* Vmax = 120 µM/s, Km = 3 mM, [S] = 1 mM. *Find:* $v_0$.
1. **Identify the approach.** We have Vmax, Km and [S] and need initial velocity, so we use the Michaelis–Menten equation directly.
2. **Set up.** $v_0 = \frac{120 \times 1}{3 + 1}$ (Km and [S] are both in mM, so the units cancel).
3. **Solve.** $v_0 = 120/4 = 30$ µM/s.
4. **Check.** [S] < Km, so $v_0$ should be below ½Vmax (60). 30 < 60 ✓.
**Answer:** 30 µM/s (¼ of Vmax).
**Pattern to remember:** When [S] = Km, $v_0 = ½V_{max}$. When [S] = 3·Km, $v_0 = ¾V_{max}$. When [S] ≫ Km, $v_0 → V_{max}$.

**Check yourself** *(answer aloud before opening)*
1. Why does the velocity curve level off at high [S]?
   <details><summary>Answer</summary>

   Every enzyme active site is occupied (saturation), so adding more substrate can't increase the number of ES complexes. The rate is then limited by $k_{cat}$ and [E]. [S4][06:20]
   </details>
2. Enzyme A has Km = 0.5 mM and enzyme B has Km = 5 mM for the same substrate. At [S] = 0.5 mM, which is closer to its Vmax?
   <details><summary>Answer</summary>

   Enzyme A. At [S] = Km it's at exactly ½Vmax, while B is at 0.5/(5 + 0.5) ≈ 9% of Vmax. [S6]
   </details>
3. What happens to Km if you double the enzyme concentration?
   <details><summary>Answer</summary>

   Nothing. Km is independent of [E]. Only Vmax doubles. (A common trap.) [S5][09:02]
   </details>

---

## 2. Enzyme inhibition [S9–S15]
<!-- … remaining sections follow the same pattern … -->

## Comparison matrix: types of reversible inhibition [S15]
| | Competitive | Uncompetitive | Mixed / noncompetitive |
|---|---|---|---|
| Binds to | Free E (active site) | ES complex only | E and ES (allosteric site) |
| Apparent Km | ↑ | ↓ | ↑, ↓ or = (pure noncompetitive: =) |
| Apparent Vmax | = | ↓ | ↓ |
| Overcome by more [S]? | Yes | No | No |
| Lineweaver–Burk | Lines meet on y-axis | Parallel lines | Lines meet left of y-axis (on x-axis if pure) |
| **Tell-apart cue** | "Same top speed, needs more S" | "Parallel" | "Top speed drops" |

## Connections
- Builds on: L04 §3, activation energy and transition-state stabilization (why enzymes speed up reactions at all).
- Leads to: L06, allosteric regulation (sigmoidal kinetics *don't* follow Michaelis–Menten).
- Big theme: regulation of metabolism. Inhibitors are how cells and drugs control pathway flux.

## Common mistakes and confusions
- **"Low Km = fast enzyme."** No. Km is about the substrate concentration needed. Speed at saturation is Vmax or kcat. (Student question at [27:40].)
- **Mixing up which inhibitor changes which parameter.** Use the matrix and the tell-apart cues.

## Summary
Enzyme-catalyzed reactions speed up with substrate concentration until the enzyme becomes saturated, at which point the velocity plateaus at Vmax. The Michaelis–Menten equation describes this hyperbolic relationship using two parameters: Vmax, which depends on the amount of enzyme and its turnover rate, and Km, the substrate concentration giving half-maximal velocity, which reflects apparent affinity. Because Km is independent of enzyme concentration, it characterizes the enzyme–substrate pair itself. Reversible inhibitors change these parameters in characteristic ways: competitive inhibitors raise the apparent Km, uncompetitive inhibitors lower both, and mixed inhibitors lower Vmax. Reading these signatures from plots lets biochemists identify how a drug or regulator acts.

## Explain it back (no answers on purpose)
1. Explain Km to a friend who has never taken biochemistry, without using the words "affinity" or "Michaelis".
2. Why can a competitive inhibitor be overcome by adding more substrate, but a noncompetitive one can't?
3. Sketch the Lineweaver–Burk plot for a competitive inhibitor from memory, and explain why the lines cross where they do.

## Gaps and [VERIFY]
- [ ] [VERIFY] Slide 12 labels the x-intercept as "−Km" but the transcript [19:30] says "−1/Km". The textbook (p.206) says −1/Km. Confirm with the professor.

## What your notes missed
| Missed or incorrect point | Why it matters | Source |
|---|---|---|
| Km does **not** change with enzyme concentration (your notes say "Km ↑ with more enzyme") | Classic trap, and the professor warned about it | [S5][09:02] |
| Why competitive inhibition can be overcome by high [S] | Relationship question: "compare inhibitor types" is likely on the exam | [S13][24:15] |
| The "[S] = Km gives ½Vmax" derivation | Explicit exam signal | [11:45] |

**Revision task:** add each point to *your own* notes in your own words, and link it to something already there. Revise, don't recopy.

---
**Next steps (Cornell cycle)**
- [ ] **Today, recite:** cover each section, answer "Check yourself" aloud, then do "Explain it back".
- [ ] **09/30, quiz:** `quizzes/Q-L05.md`, closed-book, confidence first.
- [ ] **Weekly, review:** 10 min reciting cue questions across L01–L05. Next full review: 10/06.
- [ ] 11 new flashcards added to the deck.
