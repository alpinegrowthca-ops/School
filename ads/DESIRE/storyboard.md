# DESIRE: “The Mystery Blend” storyboard (9:16, ~2:00)

Made with the `storyboard-ai-ad` skill and `references/desire-product-brief.md`, grounded in `sources/Research_Dossier.pdf`. The spoken script, with a source for every claim, is in [`script-draft.md`](script-draft.md).

## Assumptions (stated once)

- **No finished script was supplied.** I drafted one using only claims the dossier verifies, and the skill normally storyboards a finished script. Swap in your script and re-run to keep the same locks.
- **No reference ad video was supplied**, and the `$watch` video-analysis skill isn't installed here. The blueprint below is calibrated to the skill's bundled reference (`calibration-ad-grammar.md`: vertical, educational 3D-cartoon, villain-led direct-response ad) and adapted to DESIRE.
- **Tin artwork is a placeholder** (matte black, white DESIRE logo, flavor-colored rim). Use a real product photo as an image reference so the label is accurate. Label text gets fixed in editing.
- **Market: US DTC.** A Canadian cut must add “High caffeine content” and “Do not eat on the same day as any other source of caffeine” to the end card (§9.1). EU/UK cuts need different claims (§9.2).
- **Captions, numbers (80 mg, 300 mg, 200 mg, 8.4 oz), source supers and the DSHEA disclaimer are an editing layer**, not part of any image prompt.
- Platform-neutral prompts. They work in Higgsfield. Use the character images as reference or character sheets, with fixed seeds where supported.

## Reference-ad blueprint

- **Format:** 9:16 vertical, polished 3D cartoon. Cool charcoal and mint-teal palette for the brand, murky olive-green for the villain.
- **Hook:** the first three words are “Nicotine free” over a tin-lid snap. The tin then slides into a denim pocket worn with a tin-shaped ring, a silent nod to the nicotine-pouch user that makes no cessation claim. Then the problem introduces itself in first person, straight to camera.
- **Pacing:** 30 clips in about 1:57. Beats run 2–4 s in the hook and villain sections and up to 6.5 s on proof lines. The visual changes with every new number, character or claim.
- **Framing and motion:** medium close-ups for characters and macro shots for product. One simple camera move per clip (push-in, tilt, orbit, rack focus). The villain holds direct eye contact.
- **Recurring devices:** the problem is personified as an unlabeled tub (the undisclosed blend), a failed alternative as an oversized generic can, and ingredients as helper characters. Literal metaphors: a dose gauge line, a balance scale, the worn tin ring.
- **Roles:** the villain is the *Mystery Blend* (never caffeine). The protagonist is a silent adult foreman across three parts of the day. The product is a clean, non-speaking hero voiced by an off-screen brand narrator.
- **On-screen text:** bold word-synced captions in edit, number supers on every dose, small source supers (Jagim 2019, EFSA, U.S. Army/Walter Reed), and an 18+ line plus disclaimer on the end card.
- **Phases:** hook → villain → failed alternative → dose truth → turn → DESIRE dose → ingredients → format lineage → flavor day-parts → honest expectation → CTA.

## Character, Voice, Sound, and Style Consistency Lock

Paste each descriptor **word for word**. Never shorten it to a name or “the same ___”.

### Style

“Polished vertical 3D cartoon animation with soft rounded proportions, expressive faces, clean simplified shapes, crisp cool-toned cinematic lighting, murky olive-green antagonist accents, bright mint-teal and clean white solution energy, shallow depth of field, 9:16 composition.”

### The Foreman (protagonist, silent throughout)

- **Identity + job-site wardrobe:** “An adult man in his early thirties with light-olive skin, a short dark-brown fade haircut, a neatly trimmed short dark beard, warm hazel eyes, a friendly square face, and a broad athletic build, wearing a charcoal-grey henley under a fluorescent-orange high-visibility safety vest, dark-blue work jeans with a faded round tin ring worn into the right back pocket, and tan leather work boots.”
- **Identity + gym wardrobe:** “An adult man in his early thirties with light-olive skin, a short dark-brown fade haircut, a neatly trimmed short dark beard, warm hazel eyes, a friendly square face, and a broad athletic build, wearing a plain black fitted training T-shirt, grey athletic shorts, and white trainers.”
- **Video identity anchor:** “the early-thirties man with light-olive skin, a short dark fade, a trimmed dark beard, and hazel eyes”
- Fixed: face, beard, skin, build. Scene variables: wardrobe (site or gym), expression, location, time of day. He never lip-syncs.

### The Mystery Blend (antagonist, the undisclosed blend)

- **Descriptor:** “A squat, oversized cartoon supplement-tub creature with a glossy murky olive-green plastic body, a peeling off-white label scribbled with grey question marks and no numbers, a black screw-top lid tilted on its head like a cap, stubby charcoal-grey arms and legs, narrow yellow eyes, thick slanted black eyebrows, and a sly lopsided grin with uneven teeth.”
- **Video anchor:** “the squat murky olive-green tub creature with the question-mark label, tilted black lid, narrow yellow eyes, and lopsided grin”
- Expressions can go from smug to sulking. The tub shape, color, label style and lid never change. The label may peel only in clips 13 and 27.

### The Big-Can Cousin (failed alternative, silent)

- **Descriptor:** “A tall cartoon energy-drink-can creature with a dented brushed-silver body, a jagged neon-yellow lightning stripe with no logo or text, a pull tab bent up like a crooked cap, skinny grey arms and legs, wide bloodshot white eyes, and a jittery overexcited grin.”
- **Video anchor:** “the dented silver can creature with the neon-yellow lightning stripe and bloodshot eyes”
- No brand marks, ever.

### DESIRE tins (placeholder until a product photo is supplied)

- **Cool Mint (hero):** “A slim round matte-black metal tin about the width of a palm and two centimeters tall, with a flush pressed lid, the word DESIRE in clean white uppercase sans-serif lettering centered on the lid, a small white NICOTINE FREE line beneath the logo, and a thin mint-teal flavor ring around the lid edge.”
- **Watermelon Ice:** “A slim round matte-black metal tin about the width of a palm and two centimeters tall, with a flush pressed lid, the word DESIRE in clean white uppercase sans-serif lettering centered on the lid, a small white NICOTINE FREE line beneath the logo, and a thin watermelon-pink flavor ring around the lid edge.”
- **Mixed Berry:** “A slim round matte-black metal tin about the width of a palm and two centimeters tall, with a flush pressed lid, the word DESIRE in clean white uppercase sans-serif lettering centered on the lid, a small white NICOTINE FREE line beneath the logo, and a thin deep berry-purple flavor ring around the lid edge.”
- **Video anchors:** “the matte-black DESIRE tin with the white logo and mint-teal rim” / “the matte-black DESIRE tin with the white logo and watermelon-pink rim” / “the matte-black DESIRE tin with the white logo and berry-purple rim”

### DESIRE pouch

- **Descriptor:** “A small white rectangular oral pouch with softly rounded corners, a slightly padded smooth fleece-like surface, and no visible grounds or leaks.”
- **Video anchor:** “the small white rounded-corner pouch”

### Ingredient helpers (silent)

- **Caffeine:** “A small bright-white cartoon crystal character with a rounded hexagonal body, a soft inner glow, tiny stubby arms and legs, big round black eyes, and an eager open grin.” Anchor: “the glowing white hexagonal crystal character”
- **L-theanine:** “A small mint-teal cartoon tea-leaf character with a plump rounded leaf body, a pale central vein, tiny stubby arms and legs, calm half-lidded eyes, and a relaxed gentle smile.” Anchor: “the calm mint-teal tea-leaf character”
- Per the dossier (§8.3), L-tyrosine gets no character, benefit or mechanism visual. It appears only on the printed panel.

### Voices

- **Mystery Blend (on-camera when visible, off-screen during cutaways):** “Mid-low, smooth, slightly nasal adult male-presenting character voice with a neutral American accent, quick slick-salesman pace, sly pauses before punchlines, and a smug, evasive, winking delivery.”
- **DESIRE narrator (always off-screen):** “Calm, clear adult female-presenting voice in a low-mid register with a neutral North American accent, measured medium pace, crisp diction, dry understated confidence, and a straight-talking, no-hype delivery.”
- The Foreman, the Big-Can Cousin and both helpers never speak.

### Speaker map

| Clips | Speaker | Mode |
|---|---|---|
| 01–02 | DESIRE narrator | Narrator voiceover |
| 03–07 | Mystery Blend | On-camera dialogue |
| 08 | Mystery Blend | Off-screen character voice (Foreman silent) |
| 09–10 | Mystery Blend | On-camera dialogue (Foreman / Big-Can Cousin silent) |
| 11 | Mystery Blend | Off-screen character voice (Big-Can Cousin silent) |
| 12–30 | DESIRE narrator | Narrator voiceover |

### Global sound lock

- **Music bed:** minimal modern electronic, low-to-medium intensity: dry soft kick, muted bass pulse, sparse plucks. In the villain section, a detuned murky synth drone over the same tempo. It drops out under the EFSA line (clip 12), then at the turn (clip 13) resolves into a clean, bright mint-toned pluck arpeggio. The flavor run adds a light hi-hat. The end card thins to one chord.
- **Motifs:** DESIRE tin = crisp metal lid click (the signature sting) plus a soft cool-air shimmer. Mystery Blend = hollow plastic creak and powder rattle. Big-Can Cousin = carbonation hiss and jittery electric buzz. Caffeine helper = bright spark tick. L-theanine helper = soft airy chime.
- **Ambience:** match each set (job-site wind and machinery, gym clanks and HVAC, lab or store hum), always low.
- **Transitions:** short air whooshes. Use the tin-lid click on key reveals.
- **Mix priority:** voice > signature click > music > ambience. Duck music about 10 dB under speech, and keep effects off spoken numbers.

## Storyboard

### Clip 01

**Script section / voiceover text**
“Nicotine free.”

**Text-to-image prompt**
A slim round matte-black metal tin about the width of a palm and two centimeters tall, with a flush pressed lid, the word DESIRE in clean white uppercase sans-serif lettering centered on the lid, a small white NICOTINE FREE line beneath the logo, and a thin mint-teal flavor ring around the lid edge. The tin sits closed in the center of a dark charcoal surface in a tight overhead macro close-up, lit by a cool mint-teal rim light against a soft black background. Polished vertical 3D cartoon animation with soft rounded proportions, expressive faces, clean simplified shapes, crisp cool-toned cinematic lighting, murky olive-green antagonist accents, bright mint-teal and clean white solution energy, shallow depth of field, 9:16 composition.

**Image-to-video prompt**
The lid of the matte-black DESIRE tin with the white logo and mint-teal rim snaps open with a crisp pop, revealing a neat ring of small white pouches, and a faint cool mint mist drifts up from inside. No character is visible and no one lip-syncs; the locked DESIRE narrator says off-screen: “Nicotine free.” Preserve the tin's round shape, matte-black finish, logo placement, and mint-teal rim. Quick snap push-in, fast confident tempo.

**Sound / voiceover direction**
Narrator voiceover; no visible speaker. Calm, clear adult female-presenting voice in a low-mid register with a neutral North American accent, measured medium pace, crisp diction, dry understated confidence, and a straight-talking, no-hype delivery. Music: the minimal electronic bed starts on this downbeat with a dry soft kick and muted bass pulse. Ambience: near-silent studio air. SFX: the signature crisp metal tin-lid click on the open, then a soft cool-air shimmer as the mist rises. Mix: speech clearly dominant; duck music about 10 dB under the line; keep effects short and never on top of a spoken number.

**Estimated length**
1.5 seconds

### Clip 02

**Script section / voiceover text**
“Fifteen pouches. The same tin you already know.”

**Text-to-image prompt**
An adult man in his early thirties with light-olive skin, a short dark-brown fade haircut, a neatly trimmed short dark beard, warm hazel eyes, a friendly square face, and a broad athletic build, wearing a charcoal-grey henley under a fluorescent-orange high-visibility safety vest, dark-blue work jeans with a faded round tin ring worn into the right back pocket, and tan leather work boots. A slim round matte-black metal tin about the width of a palm and two centimeters tall, with a flush pressed lid, the word DESIRE in clean white uppercase sans-serif lettering centered on the lid, a small white NICOTINE FREE line beneath the logo, and a thin mint-teal flavor ring around the lid edge. Tight close-up from behind at hip height: his right hand holds the tin just above the faded round ring on his back jeans pocket, on a sunlit construction site with blurred scaffolding. Polished vertical 3D cartoon animation with soft rounded proportions, expressive faces, clean simplified shapes, crisp cool-toned cinematic lighting, murky olive-green antagonist accents, bright mint-teal and clean white solution energy, shallow depth of field, 9:16 composition.

**Image-to-video prompt**
The hand of the early-thirties man with light-olive skin, a short dark fade, a trimmed dark beard, and hazel eyes slides the matte-black DESIRE tin with the white logo and mint-teal rim into his back jeans pocket, where it settles exactly inside the faded round ring worn into the denim. His face stays out of frame, he stays silent and does not lip-sync, and the locked DESIRE narrator says off-screen: “Fifteen pouches. The same tin you already know.” Preserve his skin tone, vest, jeans, and the tin design. Slow tilt down following the tin into the pocket, easy relaxed tempo.

**Sound / voiceover direction**
Narrator voiceover; the man reacts silently and has no speaking role. Calm, clear adult female-presenting voice in a low-mid register with a neutral North American accent, measured medium pace, crisp diction, dry understated confidence, and a straight-talking, no-hype delivery. Music: bed continues, low intensity. Ambience: distant construction machinery and light wind. SFX: soft denim rustle and a small satisfying tin-seat thump as it fits the pocket ring. Mix: speech clearly dominant; duck music about 10 dB under the line; keep effects short and never on top of a spoken number.

**Estimated length**
3.5 seconds

### Clip 03

**Script section / voiceover text**
“Hi. I'm the Mystery Blend.”

**Text-to-image prompt**
A squat, oversized cartoon supplement-tub creature with a glossy murky olive-green plastic body, a peeling off-white label scribbled with grey question marks and no numbers, a black screw-top lid tilted on its head like a cap, stubby charcoal-grey arms and legs, narrow yellow eyes, thick slanted black eyebrows, and a sly lopsided grin with uneven teeth. The creature pops up from a crowded supplement-store shelf between plain unlabeled tubs, leaning toward camera in a medium close-up with a smug grin, under dim greenish store lighting. Polished vertical 3D cartoon animation with soft rounded proportions, expressive faces, clean simplified shapes, crisp cool-toned cinematic lighting, murky olive-green antagonist accents, bright mint-teal and clean white solution energy, shallow depth of field, 9:16 composition.

**Image-to-video prompt**
The squat murky olive-green tub creature with the question-mark label, tilted black lid, narrow yellow eyes, and lopsided grin rises from between the tubs, tips its lid like a hat, looks straight into the camera with a raised eyebrow, and lip-syncs in precise natural synchronization with clear mouth shapes, speaking: “Hi. I'm the Mystery Blend.” Preserve its tub shape, murky olive-green color, question-mark label, and 3D cartoon style. Slow push-in, sly playful tempo.

**Sound / voiceover direction**
On-camera Mystery Blend dialogue; the creature lip-syncs the line. Mid-low, smooth, slightly nasal adult male-presenting character voice with a neutral American accent, quick slick-salesman pace, sly pauses before punchlines, and a smug, evasive, winking delivery. Music: bed shifts into the villain variation, a detuned murky synth drone over the same kick. Ambience: muted store hum. SFX: hollow plastic creak as it rises, a small lid squeak on the hat-tip. Mix: speech clearly dominant; duck music about 10 dB under the line; keep effects short and never on top of a spoken number.

**Estimated length**
2.5 seconds

### Clip 04

**Script section / voiceover text**
“I live in your tubs, your scoops, and your giant cans,”

**Text-to-image prompt**
A squat, oversized cartoon supplement-tub creature with a glossy murky olive-green plastic body, a peeling off-white label scribbled with grey question marks and no numbers, a black screw-top lid tilted on its head like a cap, stubby charcoal-grey arms and legs, narrow yellow eyes, thick slanted black eyebrows, and a sly lopsided grin with uneven teeth. The creature lounges on a dim kitchen counter beside a heaping plastic scoop of murky grey powder and a tall plain silver can with no logo, one arm draped over the scoop, eyes on camera. Medium shot, moody low kitchen light. Polished vertical 3D cartoon animation with soft rounded proportions, expressive faces, clean simplified shapes, crisp cool-toned cinematic lighting, murky olive-green antagonist accents, bright mint-teal and clean white solution energy, shallow depth of field, 9:16 composition.

**Image-to-video prompt**
The squat murky olive-green tub creature with the question-mark label, tilted black lid, narrow yellow eyes, and lopsided grin taps the scoop so a small puff of grey powder rises, then pats the plain silver can, keeping direct eye contact and lip-syncing in precise natural synchronization with a smug, easy grin while speaking: “I live in your tubs, your scoops, and your giant cans,” Preserve its face, tub body, colors, and 3D cartoon style. Slow lateral slide, lazy confident tempo.

**Sound / voiceover direction**
On-camera Mystery Blend dialogue; the creature lip-syncs the line. Mid-low, smooth, slightly nasal adult male-presenting character voice with a neutral American accent, quick slick-salesman pace, sly pauses before punchlines, and a smug, evasive, winking delivery. Music: villain drone continues. Ambience: quiet kitchen room tone. SFX: soft powder puff on the scoop tap, a hollow metallic tap on the can. Mix: speech clearly dominant; duck music about 10 dB under the line; keep effects short and never on top of a spoken number.

**Estimated length**
4.5 seconds

### Clip 05

**Script section / voiceover text**
“and I never tell you how much.”

**Text-to-image prompt**
A squat, oversized cartoon supplement-tub creature with a glossy murky olive-green plastic body, a peeling off-white label scribbled with grey question marks and no numbers, a black screw-top lid tilted on its head like a cap, stubby charcoal-grey arms and legs, narrow yellow eyes, thick slanted black eyebrows, and a sly lopsided grin with uneven teeth. Close-up of the creature leaning into camera with narrowed eyes, one stubby hand cupped beside its mouth as if sharing a secret, dark background with a single green rim light. Polished vertical 3D cartoon animation with soft rounded proportions, expressive faces, clean simplified shapes, crisp cool-toned cinematic lighting, murky olive-green antagonist accents, bright mint-teal and clean white solution energy, shallow depth of field, 9:16 composition.

**Image-to-video prompt**
The squat murky olive-green tub creature with the question-mark label, tilted black lid, narrow yellow eyes, and lopsided grin leans even closer, lip-syncs in a conspiratorial half-whisper with precise mouth shapes, speaking: “and I never tell you how much.” then gives one slow wink to camera. Preserve its face, label, lid, and colors. Slow push-in to an extreme close-up, teasing tempo.

**Sound / voiceover direction**
On-camera Mystery Blend dialogue; the creature lip-syncs the line. Mid-low, smooth, slightly nasal adult male-presenting character voice with a neutral American accent, quick slick-salesman pace, sly pauses before punchlines, and a smug, evasive, winking delivery. Music: drone drops almost out for the whisper. Ambience: none. SFX: a tiny cartoon wink tick on the final beat. Mix: speech clearly dominant; duck music about 10 dB under the line; keep effects short and never on top of a spoken number.

**Estimated length**
3 seconds

### Clip 06

**Script section / voiceover text**
“The average popular pre-workout packs 18 ingredients.”

**Text-to-image prompt**
A squat, oversized cartoon supplement-tub creature with a glossy murky olive-green plastic body, a peeling off-white label scribbled with grey question marks and no numbers, a black screw-top lid tilted on its head like a cap, stubby charcoal-grey arms and legs, narrow yellow eyes, thick slanted black eyebrows, and a sly lopsided grin with uneven teeth. The creature stands on a dark lab bench with its lid popped off, a jumbled fountain of about eighteen small multicolored capsules, pellets, and powder chunks bursting up out of its open top. Medium shot, green-tinted light. Polished vertical 3D cartoon animation with soft rounded proportions, expressive faces, clean simplified shapes, crisp cool-toned cinematic lighting, murky olive-green antagonist accents, bright mint-teal and clean white solution energy, shallow depth of field, 9:16 composition.

**Image-to-video prompt**
The fountain of ingredient pellets bursts higher and tumbles around the squat murky olive-green tub creature with the question-mark label, tilted black lid, narrow yellow eyes, and lopsided grin as it spreads its stubby arms proudly, looks at camera, and lip-syncs in precise natural synchronization, speaking: “The average popular pre-workout packs 18 ingredients.” Preserve its tub body, colors, and label. Slight tilt up with the fountain, showy tempo.

**Sound / voiceover direction**
On-camera Mystery Blend dialogue; the creature lip-syncs the line. Mid-low, smooth, slightly nasal adult male-presenting character voice with a neutral American accent, quick slick-salesman pace, sly pauses before punchlines, and a smug, evasive, winking delivery. Music: villain drone with an off-kilter pluck. Ambience: faint lab hum. SFX: a rattling cascade of pellets, kept low under the voice. Mix: speech clearly dominant; duck music about 10 dB under the line; keep effects short and never on top of a spoken number.

**Estimated length**
3.5 seconds

### Clip 07

**Script section / voiceover text**
“About eight of them hide inside a blend like me, with no amounts on the label.”

**Text-to-image prompt**
A squat, oversized cartoon supplement-tub creature with a glossy murky olive-green plastic body, a peeling off-white label scribbled with grey question marks and no numbers, a black screw-top lid tilted on its head like a cap, stubby charcoal-grey arms and legs, narrow yellow eyes, thick slanted black eyebrows, and a sly lopsided grin with uneven teeth. Close medium shot: the creature pats its own question-mark label while several small colored pellets sink into a swirl of grey fog visible through its semi-translucent olive plastic side. Polished vertical 3D cartoon animation with soft rounded proportions, expressive faces, clean simplified shapes, crisp cool-toned cinematic lighting, murky olive-green antagonist accents, bright mint-teal and clean white solution energy, shallow depth of field, 9:16 composition.

**Image-to-video prompt**
The squat murky olive-green tub creature with the question-mark label, tilted black lid, narrow yellow eyes, and lopsided grin smugly pats its label as the colored pellets inside sink and disappear into the grey fog, holding eye contact and lip-syncing in precise natural synchronization, speaking: “About eight of them hide inside a blend like me, with no amounts on the label.” Preserve its face, colors, label, and lid. Slow push-in toward the fogged side, sly tempo.

**Sound / voiceover direction**
On-camera Mystery Blend dialogue; the creature lip-syncs the line. Mid-low, smooth, slightly nasal adult male-presenting character voice with a neutral American accent, quick slick-salesman pace, sly pauses before punchlines, and a smug, evasive, winking delivery. Music: villain drone. Ambience: faint lab hum. SFX: low murky swirl as the pellets vanish, one hollow pat on the label. Mix: speech clearly dominant; duck music about 10 dB under the line; keep effects short and never on top of a spoken number.

**Estimated length**
6.5 seconds

### Clip 08

**Script section / voiceover text**
“So you take a scoop, spend the next three hours itching and buzzing,”

**Text-to-image prompt**
An adult man in his early thirties with light-olive skin, a short dark-brown fade haircut, a neatly trimmed short dark beard, warm hazel eyes, a friendly square face, and a broad athletic build, wearing a plain black fitted training T-shirt, grey athletic shorts, and white trainers. He stands between weight racks in a gym, scratching his forearm with a tense grimace, eyes wide and shoulders hunched, an empty shaker bottle in his other hand. Medium shot, harsh overhead gym light with a faint olive-green tint. Polished vertical 3D cartoon animation with soft rounded proportions, expressive faces, clean simplified shapes, crisp cool-toned cinematic lighting, murky olive-green antagonist accents, bright mint-teal and clean white solution energy, shallow depth of field, 9:16 composition.

**Image-to-video prompt**
The early-thirties man with light-olive skin, a short dark fade, a trimmed dark beard, and hazel eyes scratches his forearms, twitches restlessly, and glances nervously up at a wall clock; he stays silent and does not lip-sync while the locked Mystery Blend voice says off-screen: “So you take a scoop, spend the next three hours itching and buzzing,” Preserve his face, beard, build, and gym clothing. Slight handheld jitter, uneasy tempo.

**Sound / voiceover direction**
Off-screen Mystery Blend character voice; the man reacts silently. Mid-low, smooth, slightly nasal adult male-presenting character voice with a neutral American accent, quick slick-salesman pace, sly pauses before punchlines, and a smug, evasive, winking delivery. Music: villain drone with a nervous ticking pulse. Ambience: low gym clanks and HVAC hum. SFX: a fast clock tick and a faint electric buzz, both under the voice. Mix: speech clearly dominant; duck music about 10 dB under the line; keep effects short and never on top of a spoken number.

**Estimated length**
5.5 seconds

### Clip 09

**Script section / voiceover text**
“and never find out what you actually took.”

**Text-to-image prompt**
An adult man in his early thirties with light-olive skin, a short dark-brown fade haircut, a neatly trimmed short dark beard, warm hazel eyes, a friendly square face, and a broad athletic build, wearing a plain black fitted training T-shirt, grey athletic shorts, and white trainers. A squat, oversized cartoon supplement-tub creature with a glossy murky olive-green plastic body, a peeling off-white label scribbled with grey question marks and no numbers, a black screw-top lid tilted on its head like a cap, stubby charcoal-grey arms and legs, narrow yellow eyes, thick slanted black eyebrows, and a sly lopsided grin with uneven teeth. In a gym locker area, he holds the tub creature up at eye level with both hands, squinting in confusion at its question-mark label, while the creature grins toward camera. Medium close-up. Polished vertical 3D cartoon animation with soft rounded proportions, expressive faces, clean simplified shapes, crisp cool-toned cinematic lighting, murky olive-green antagonist accents, bright mint-teal and clean white solution energy, shallow depth of field, 9:16 composition.

**Image-to-video prompt**
The early-thirties man with light-olive skin, a short dark fade, a trimmed dark beard, and hazel eyes slowly turns the creature in his hands, frowning in silent confusion without lip-syncing, while the squat murky olive-green tub creature with the question-mark label, tilted black lid, narrow yellow eyes, and lopsided grin looks at camera, shrugs, and lip-syncs in precise natural synchronization, speaking: “and never find out what you actually took.” Preserve both characters' faces, colors, and clothing. Static camera with a slight push-in, deadpan tempo.

**Sound / voiceover direction**
On-camera Mystery Blend dialogue; the creature lip-syncs and the man stays silent. Mid-low, smooth, slightly nasal adult male-presenting character voice with a neutral American accent, quick slick-salesman pace, sly pauses before punchlines, and a smug, evasive, winking delivery. Music: villain drone resolves on a sour note. Ambience: locker-room echo. SFX: hollow plastic creak as he turns the tub. Mix: speech clearly dominant; duck music about 10 dB under the line; keep effects short and never on top of a spoken number.

**Estimated length**
3.5 seconds

### Clip 10

**Script section / voiceover text**
“Or you grab one of my big-can cousins.”

**Text-to-image prompt**
A squat, oversized cartoon supplement-tub creature with a glossy murky olive-green plastic body, a peeling off-white label scribbled with grey question marks and no numbers, a black screw-top lid tilted on its head like a cap, stubby charcoal-grey arms and legs, narrow yellow eyes, thick slanted black eyebrows, and a sly lopsided grin with uneven teeth. A tall cartoon energy-drink-can creature with a dented brushed-silver body, a jagged neon-yellow lightning stripe with no logo or text, a pull tab bent up like a crooked cap, skinny grey arms and legs, wide bloodshot white eyes, and a jittery overexcited grin. The tub creature stands on a gas-station counter gesturing up at the much taller can creature beside it, which vibrates with a jittery grin, under harsh fluorescent convenience-store light. Polished vertical 3D cartoon animation with soft rounded proportions, expressive faces, clean simplified shapes, crisp cool-toned cinematic lighting, murky olive-green antagonist accents, bright mint-teal and clean white solution energy, shallow depth of field, 9:16 composition.

**Image-to-video prompt**
The squat murky olive-green tub creature with the question-mark label, tilted black lid, narrow yellow eyes, and lopsided grin sweeps a stubby arm up toward the dented silver can creature with the neon-yellow lightning stripe and bloodshot eyes, looks at camera, and lip-syncs in precise natural synchronization, speaking: “Or you grab one of my big-can cousins.” The can creature stays silent with its grin clenched, bouncing on its toes. Preserve both characters' shapes, colors, and faces. Slow tilt up to the can, sly tempo.

**Sound / voiceover direction**
On-camera Mystery Blend dialogue; the can creature stays silent. Mid-low, smooth, slightly nasal adult male-presenting character voice with a neutral American accent, quick slick-salesman pace, sly pauses before punchlines, and a smug, evasive, winking delivery. Music: villain drone plus a jittery hi-hat. Ambience: fridge hum and store beeps. SFX: fizzy carbonation hiss from the can. Mix: speech clearly dominant; duck music about 10 dB under the line; keep effects short and never on top of a spoken number.

**Estimated length**
3.5 seconds

### Clip 11

**Script section / voiceover text**
“Some carry 300 milligrams in a single can.”

**Text-to-image prompt**
A tall cartoon energy-drink-can creature with a dented brushed-silver body, a jagged neon-yellow lightning stripe with no logo or text, a pull tab bent up like a crooked cap, skinny grey arms and legs, wide bloodshot white eyes, and a jittery overexcited grin. Low-angle close-up of the can creature shaking with overexcited energy, beads of condensation flying off its dented body, crackles of neon-yellow sparks around it, dark convenience-store backdrop. Polished vertical 3D cartoon animation with soft rounded proportions, expressive faces, clean simplified shapes, crisp cool-toned cinematic lighting, murky olive-green antagonist accents, bright mint-teal and clean white solution energy, shallow depth of field, 9:16 composition.

**Image-to-video prompt**
The dented silver can creature with the neon-yellow lightning stripe and bloodshot eyes vibrates harder, eyes bulging, sparks crackling around it; it keeps its grin clenched, stays silent and does not lip-sync while the locked Mystery Blend voice says off-screen: “Some carry 300 milligrams in a single can.” Preserve its dented silver body, yellow stripe, and face. Slow push-in, frantic tempo.

**Sound / voiceover direction**
Off-screen Mystery Blend character voice; the visible can creature is silent. Mid-low, smooth, slightly nasal adult male-presenting character voice with a neutral American accent, quick slick-salesman pace, sly pauses before punchlines, and a smug, evasive, winking delivery. Music: villain drone, the jittery hi-hat tightens. Ambience: fridge hum. SFX: electric buzz and carbonation crackle, kept under the voice. Mix: speech clearly dominant; duck music about 10 dB under the line; keep effects short and never on top of a spoken number.

**Estimated length**
4 seconds

### Clip 12

**Script section / voiceover text**
“Europe's food-safety authority considers up to 200 milligrams a safe single dose for healthy adults.”

**Text-to-image prompt**
A tall cartoon energy-drink-can creature with a dented brushed-silver body, a jagged neon-yellow lightning stripe with no logo or text, a pull tab bent up like a crooked cap, skinny grey arms and legs, wide bloodshot white eyes, and a jittery overexcited grin. The can creature stands beside a tall clean white wall gauge with a single glowing mint-teal marker line at mid-height, its head rising well above the line, in a bright minimalist white room. Polished vertical 3D cartoon animation with soft rounded proportions, expressive faces, clean simplified shapes, crisp cool-toned cinematic lighting, murky olive-green antagonist accents, bright mint-teal and clean white solution energy, shallow depth of field, 9:16 composition.

**Image-to-video prompt**
The glowing mint-teal marker line on the gauge brightens and pulses as the dented silver can creature with the neon-yellow lightning stripe and bloodshot eyes looks up at it, gulps, and shrinks back sheepishly. The can creature stays silent and does not lip-sync while the locked DESIRE narrator says off-screen: “Europe's food-safety authority considers up to 200 milligrams a safe single dose for healthy adults.” Preserve the can creature's look and the clean white set. Slow tilt up the gauge, sober tempo.

**Sound / voiceover direction**
Narrator voiceover; the can creature reacts silently. Calm, clear adult female-presenting voice in a low-mid register with a neutral North American accent, measured medium pace, crisp diction, dry understated confidence, and a straight-talking, no-hype delivery. Music: the villain drone cuts out; a clean sustained pad enters. Ambience: quiet white-room tone. SFX: a soft clear tone as the marker line glows. Mix: speech clearly dominant; duck music about 10 dB under the line; keep effects short and never on top of a spoken number.

**Estimated length**
6.5 seconds

### Clip 13

**Script section / voiceover text**
“The problem was never caffeine. It was not knowing.”

**Text-to-image prompt**
A squat, oversized cartoon supplement-tub creature with a glossy murky olive-green plastic body, a peeling off-white label scribbled with grey question marks and no numbers, a black screw-top lid tilted on its head like a cap, stubby charcoal-grey arms and legs, narrow yellow eyes, thick slanted black eyebrows, and a sly lopsided grin with uneven teeth. A slim round matte-black metal tin about the width of a palm and two centimeters tall, with a flush pressed lid, the word DESIRE in clean white uppercase sans-serif lettering centered on the lid, a small white NICOTINE FREE line beneath the logo, and a thin mint-teal flavor ring around the lid edge. The tin stands upright like a small monolith in the foreground, glowing with clean mint-teal light, while the tub creature recoils behind it, shielding its narrow yellow eyes, in a dark space. Polished vertical 3D cartoon animation with soft rounded proportions, expressive faces, clean simplified shapes, crisp cool-toned cinematic lighting, murky olive-green antagonist accents, bright mint-teal and clean white solution energy, shallow depth of field, 9:16 composition.

**Image-to-video prompt**
Clean mint-white light from the matte-black DESIRE tin with the white logo and mint-teal rim sweeps over the squat murky olive-green tub creature with the question-mark label, tilted black lid, narrow yellow eyes, and lopsided grin, whose question-mark label peels away and flutters off as it cowers and shrinks. The tub creature stays silent and does not lip-sync while the locked DESIRE narrator says off-screen: “The problem was never caffeine. It was not knowing.” Preserve both designs and the 3D cartoon style. Slow push-in toward the tin, decisive tempo.

**Sound / voiceover direction**
Narrator voiceover; the Mystery Blend reacts silently. Calm, clear adult female-presenting voice in a low-mid register with a neutral North American accent, measured medium pace, crisp diction, dry understated confidence, and a straight-talking, no-hype delivery. Music: the bed resolves from minor to major into a clean, bright mint-toned pluck arpeggio. Ambience: none. SFX: signature tin-lid click on the light sweep, a papery flutter as the label peels. Mix: speech clearly dominant; duck music about 10 dB under the line; keep effects short and never on top of a spoken number.

**Estimated length**
4.5 seconds

### Clip 14

**Script section / voiceover text**
“One DESIRE pouch: 80 milligrams of caffeine.”

**Text-to-image prompt**
A small white rectangular oral pouch with softly rounded corners, a slightly padded smooth fleece-like surface, and no visible grounds or leaks. A small bright-white cartoon crystal character with a rounded hexagonal body, a soft inner glow, tiny stubby arms and legs, big round black eyes, and an eager open grin. The pouch rests on a clean white surface in macro close-up, and the crystal character stands on top of it with arms raised, glowing softly, against a soft mint-teal gradient background. Polished vertical 3D cartoon animation with soft rounded proportions, expressive faces, clean simplified shapes, crisp cool-toned cinematic lighting, murky olive-green antagonist accents, bright mint-teal and clean white solution energy, shallow depth of field, 9:16 composition.

**Image-to-video prompt**
The glowing white hexagonal crystal character hops once on top of the small white rounded-corner pouch, plants its feet, and flexes proudly toward camera with a bright grin. The crystal character stays silent and does not lip-sync while the locked DESIRE narrator says off-screen: “One DESIRE pouch: 80 milligrams of caffeine.” Preserve the pouch shape and the character's glow and face. Slow orbit, upbeat tempo.

**Sound / voiceover direction**
Narrator voiceover; the crystal character reacts silently. Calm, clear adult female-presenting voice in a low-mid register with a neutral North American accent, measured medium pace, crisp diction, dry understated confidence, and a straight-talking, no-hype delivery. Music: bright pluck arpeggio. Ambience: clean studio air. SFX: a bright spark tick when it lands. Mix: speech clearly dominant; duck music about 10 dB under the line; keep effects short and never on top of a spoken number.

**Estimated length**
3 seconds

### Clip 15

**Script section / voiceover text**
“About the same as a standard 8.4-ounce energy drink,”

**Text-to-image prompt**
A small white rectangular oral pouch with softly rounded corners, a slightly padded smooth fleece-like surface, and no visible grounds or leaks. The pouch sits on the left pan of a sleek white balance scale, and a small plain unbranded silver can with no logo or text sits on the right pan, both pans perfectly level, on a clean studio set with mint-teal backlight. Polished vertical 3D cartoon animation with soft rounded proportions, expressive faces, clean simplified shapes, crisp cool-toned cinematic lighting, murky olive-green antagonist accents, bright mint-teal and clean white solution energy, shallow depth of field, 9:16 composition.

**Image-to-video prompt**
The balance-scale pans sway gently and settle perfectly level, with the small white rounded-corner pouch on one side and the plain silver can on the other. No character appears and no one lip-syncs; the locked DESIRE narrator says off-screen: “About the same as a standard 8.4-ounce energy drink,” Preserve the pouch and the unbranded can. Slow push-in, measured tempo.

**Sound / voiceover direction**
Narrator voiceover; no visible speaker. Calm, clear adult female-presenting voice in a low-mid register with a neutral North American accent, measured medium pace, crisp diction, dry understated confidence, and a straight-talking, no-hype delivery. Music: pluck arpeggio, light. Ambience: studio air. SFX: a soft metallic settle as the scale levels. Mix: speech clearly dominant; duck music about 10 dB under the line; keep effects short and never on top of a spoken number.

**Estimated length**
4 seconds

### Clip 16

**Script section / voiceover text**
“without the can or the sugar.”

**Text-to-image prompt**
A small white rectangular oral pouch with softly rounded corners, a slightly padded smooth fleece-like surface, and no visible grounds or leaks. The pouch sits alone on the left pan of a sleek white balance scale; on the right pan a small plain unbranded silver can with no logo stands beside a small pile of white sugar cubes, on a clean studio set with mint-teal backlight. Polished vertical 3D cartoon animation with soft rounded proportions, expressive faces, clean simplified shapes, crisp cool-toned cinematic lighting, murky olive-green antagonist accents, bright mint-teal and clean white solution energy, shallow depth of field, 9:16 composition.

**Image-to-video prompt**
The plain silver can and the sugar cubes dissolve into drifting mint-teal sparkles and vanish from the right pan, leaving the small white rounded-corner pouch alone on the scale. No character appears and no one lip-syncs; the locked DESIRE narrator says off-screen: “without the can or the sugar.” Preserve the pouch design. Static camera, crisp tempo.

**Sound / voiceover direction**
Narrator voiceover; no visible speaker. Calm, clear adult female-presenting voice in a low-mid register with a neutral North American accent, measured medium pace, crisp diction, dry understated confidence, and a straight-talking, no-hype delivery. Music: pluck arpeggio. Ambience: studio air. SFX: a light sparkle dissolve. Mix: speech clearly dominant; duck music about 10 dB under the line; keep effects short and never on top of a spoken number.

**Estimated length**
2.5 seconds

### Clip 17

**Script section / voiceover text**
“Plus 80 milligrams of L-theanine,”

**Text-to-image prompt**
A small bright-white cartoon crystal character with a rounded hexagonal body, a soft inner glow, tiny stubby arms and legs, big round black eyes, and an eager open grin. A small mint-teal cartoon tea-leaf character with a plump rounded leaf body, a pale central vein, tiny stubby arms and legs, calm half-lidded eyes, and a relaxed gentle smile. The two characters stand side by side on a clean white surface, the crystal character on the left and the tea-leaf character stepping in from the right, against a soft mint-teal gradient background. Polished vertical 3D cartoon animation with soft rounded proportions, expressive faces, clean simplified shapes, crisp cool-toned cinematic lighting, murky olive-green antagonist accents, bright mint-teal and clean white solution energy, shallow depth of field, 9:16 composition.

**Image-to-video prompt**
The calm mint-teal tea-leaf character steps in beside the glowing white hexagonal crystal character, takes its tiny hand, and both turn to face the camera with friendly smiles. Both characters stay silent and do not lip-sync while the locked DESIRE narrator says off-screen: “Plus 80 milligrams of L-theanine,” Preserve both characters' shapes, colors, and faces. Slow push-in, warm tempo.

**Sound / voiceover direction**
Narrator voiceover; both helper characters react silently. Calm, clear adult female-presenting voice in a low-mid register with a neutral North American accent, measured medium pace, crisp diction, dry understated confidence, and a straight-talking, no-hype delivery. Music: pluck arpeggio adds a soft pad. Ambience: clean studio air. SFX: a soft airy chime as the tea leaf arrives. Mix: speech clearly dominant; duck music about 10 dB under the line; keep effects short and never on top of a spoken number.

**Estimated length**
2.5 seconds

### Clip 18

**Script section / voiceover text**
“the most per milligram of caffeine of any pouch brand that publishes its doses.”

**Text-to-image prompt**
A slim round matte-black metal tin about the width of a palm and two centimeters tall, with a flush pressed lid, the word DESIRE in clean white uppercase sans-serif lettering centered on the lid, a small white NICOTINE FREE line beneath the logo, and a thin mint-teal flavor ring around the lid edge. The tin stands in a row on a clean white shelf beside three plain unbranded matte-grey tins with blank lids; a tall glowing mint-teal bar rises behind the DESIRE tin, a shorter grey bar rises behind one grey tin, and a floating grey question mark hovers above each of the other two. Polished vertical 3D cartoon animation with soft rounded proportions, expressive faces, clean simplified shapes, crisp cool-toned cinematic lighting, murky olive-green antagonist accents, bright mint-teal and clean white solution energy, shallow depth of field, 9:16 composition.

**Image-to-video prompt**
The mint-teal bar behind the matte-black DESIRE tin with the white logo and mint-teal rim rises smoothly to its full height, the shorter grey bar rises only partway, and the two grey question marks bob gently in place. No character appears and no one lip-syncs; the locked DESIRE narrator says off-screen: “the most per milligram of caffeine of any pouch brand that publishes its doses.” Preserve the tin design and the blank competitor tins. Slow push-in, confident tempo.

**Sound / voiceover direction**
Narrator voiceover; no visible speaker. Calm, clear adult female-presenting voice in a low-mid register with a neutral North American accent, measured medium pace, crisp diction, dry understated confidence, and a straight-talking, no-hype delivery. Music: pluck arpeggio. Ambience: studio air. SFX: a smooth rising tone with the mint bar, a small muted blip for the grey bar. Mix: speech clearly dominant; duck music about 10 dB under the line; keep effects short and never on top of a spoken number.

**Estimated length**
5.5 seconds

### Clip 19

**Script section / voiceover text**
“Caffeine with L-theanine is one of the most studied pairings in supplement research.”

**Text-to-image prompt**
A small bright-white cartoon crystal character with a rounded hexagonal body, a soft inner glow, tiny stubby arms and legs, big round black eyes, and an eager open grin. A small mint-teal cartoon tea-leaf character with a plump rounded leaf body, a pale central vein, tiny stubby arms and legs, calm half-lidded eyes, and a relaxed gentle smile. The two characters sit side by side on top of a tall neat stack of plain white research journals with blank covers on a clean library desk, under a warm desk lamp. Polished vertical 3D cartoon animation with soft rounded proportions, expressive faces, clean simplified shapes, crisp cool-toned cinematic lighting, murky olive-green antagonist accents, bright mint-teal and clean white solution energy, shallow depth of field, 9:16 composition.

**Image-to-video prompt**
The glowing white hexagonal crystal character and the calm mint-teal tea-leaf character each flip open the top journal beside them, glance at the page, then look up at camera and nod. Both characters stay silent and do not lip-sync while the locked DESIRE narrator says off-screen: “Caffeine with L-theanine is one of the most studied pairings in supplement research.” Preserve both characters' shapes, colors, and faces. Slow tilt up the stack, calm studious tempo.

**Sound / voiceover direction**
Narrator voiceover; both helper characters react silently. Calm, clear adult female-presenting voice in a low-mid register with a neutral North American accent, measured medium pace, crisp diction, dry understated confidence, and a straight-talking, no-hype delivery. Music: pluck arpeggio, lighter. Ambience: quiet library room tone. SFX: two soft page flips. Mix: speech clearly dominant; duck music about 10 dB under the line; keep effects short and never on top of a spoken number.

**Estimated length**
5.5 seconds

### Clip 20

**Script section / voiceover text**
“We just print both numbers.”

**Text-to-image prompt**
A slim round matte-black metal tin about the width of a palm and two centimeters tall, with a flush pressed lid, the word DESIRE in clean white uppercase sans-serif lettering centered on the lid, a small white NICOTINE FREE line beneath the logo, and a thin mint-teal flavor ring around the lid edge. A small bright-white cartoon crystal character with a rounded hexagonal body, a soft inner glow, tiny stubby arms and legs, big round black eyes, and an eager open grin. A small mint-teal cartoon tea-leaf character with a plump rounded leaf body, a pale central vein, tiny stubby arms and legs, calm half-lidded eyes, and a relaxed gentle smile. Overhead close-up of the closed tin on a clean white surface, with the crystal character and the tea-leaf character standing on its lid on either side of the DESIRE logo. Polished vertical 3D cartoon animation with soft rounded proportions, expressive faces, clean simplified shapes, crisp cool-toned cinematic lighting, murky olive-green antagonist accents, bright mint-teal and clean white solution energy, shallow depth of field, 9:16 composition.

**Image-to-video prompt**
The glowing white hexagonal crystal character and the calm mint-teal tea-leaf character give a small synchronized wave to camera from the lid of the matte-black DESIRE tin with the white logo and mint-teal rim, then stand still. Both characters stay silent and do not lip-sync while the locked DESIRE narrator says off-screen: “We just print both numbers.” Preserve the tin, logo placement, and both characters. Static overhead camera, tidy tempo.

**Sound / voiceover direction**
Narrator voiceover; both helper characters react silently. Calm, clear adult female-presenting voice in a low-mid register with a neutral North American accent, measured medium pace, crisp diction, dry understated confidence, and a straight-talking, no-hype delivery. Music: pluck arpeggio lands a small resolving phrase. Ambience: studio air. SFX: a soft stamp-like press as they settle. Mix: speech clearly dominant; duck music about 10 dB under the line; keep effects short and never on top of a spoken number.

**Estimated length**
2.5 seconds

### Clip 21

**Script section / voiceover text**
“Add B6 and B12, and every active is listed by amount, right on the tin.”

**Text-to-image prompt**
A slim round matte-black metal tin about the width of a palm and two centimeters tall, with a flush pressed lid, the word DESIRE in clean white uppercase sans-serif lettering centered on the lid, a small white NICOTINE FREE line beneath the logo, and a thin mint-teal flavor ring around the lid edge. The tin is tilted up in a hand-sized close-up to show its underside, a neat white printed facts panel with clean rows of small placeholder lines, on a white surface with a soft mint-teal backlight. Polished vertical 3D cartoon animation with soft rounded proportions, expressive faces, clean simplified shapes, crisp cool-toned cinematic lighting, murky olive-green antagonist accents, bright mint-teal and clean white solution energy, shallow depth of field, 9:16 composition.

**Image-to-video prompt**
The matte-black DESIRE tin with the white logo and mint-teal rim slowly rotates on its edge to turn its printed underside panel toward camera as a soft mint-teal light sweeps across the rows. No character appears and no one lip-syncs; the locked DESIRE narrator says off-screen: “Add B6 and B12, and every active is listed by amount, right on the tin.” Preserve the tin's shape and finish. Slow orbit, clear tempo.

**Sound / voiceover direction**
Narrator voiceover; no visible speaker. Calm, clear adult female-presenting voice in a low-mid register with a neutral North American accent, measured medium pace, crisp diction, dry understated confidence, and a straight-talking, no-hype delivery. Music: pluck arpeggio. Ambience: studio air. SFX: a gentle metallic roll and a light sweep shimmer. Mix: speech clearly dominant; duck music about 10 dB under the line; keep effects short and never on top of a spoken number.

**Estimated length**
6.5 seconds

### Clip 22

**Script section / voiceover text**
“The U.S. Army spent six years working out how to give soldiers caffeine without a cup.”

**Text-to-image prompt**
A vintage olive-drab military field-ration box with no insignia or text sits open on a steel research-lab bench beside a clipboard and an upside-down empty enamel coffee cup, holding a small plain olive-green gum pack, under cool fluorescent lab light. Polished vertical 3D cartoon animation with soft rounded proportions, expressive faces, clean simplified shapes, crisp cool-toned cinematic lighting, murky olive-green antagonist accents, bright mint-teal and clean white solution energy, shallow depth of field, 9:16 composition.

**Image-to-video prompt**
Dust motes drift through the fluorescent light as the camera slowly pushes in toward the small olive-green gum pack in the open ration box. No characters appear and no one lip-syncs; the locked DESIRE narrator says off-screen: “The U.S. Army spent six years working out how to give soldiers caffeine without a cup.” Keep the objects unbranded and the style consistent. Slow push-in, documentary tempo.

**Sound / voiceover direction**
Narrator voiceover; no visible speaker. Calm, clear adult female-presenting voice in a low-mid register with a neutral North American accent, measured medium pace, crisp diction, dry understated confidence, and a straight-talking, no-hype delivery. Music: bed thins to a low pad and soft kick, a restrained curious tone. Ambience: fluorescent-light buzz and quiet lab room tone. SFX: a faint cardboard creak. Mix: speech clearly dominant; duck music about 10 dB under the line; keep effects short and never on top of a spoken number.

**Estimated length**
6.5 seconds

### Clip 23

**Script section / voiceover text**
“No brewing. No can. Just a measured dose.”

**Text-to-image prompt**
A slim round matte-black metal tin about the width of a palm and two centimeters tall, with a flush pressed lid, the word DESIRE in clean white uppercase sans-serif lettering centered on the lid, a small white NICOTINE FREE line beneath the logo, and a thin mint-teal flavor ring around the lid edge. A small white rectangular oral pouch with softly rounded corners, a slightly padded smooth fleece-like surface, and no visible grounds or leaks. The tin sits open in focus on a clean pale-grey bench, filled with a neat ring of pouches, while an unplugged drip coffee maker and a plain crushed silver can with no logo sit pushed aside, blurred, at the edge of frame in crisp morning light. Polished vertical 3D cartoon animation with soft rounded proportions, expressive faces, clean simplified shapes, crisp cool-toned cinematic lighting, murky olive-green antagonist accents, bright mint-teal and clean white solution energy, shallow depth of field, 9:16 composition.

**Image-to-video prompt**
A hand lifts a single small white rounded-corner pouch out of the matte-black DESIRE tin with the white logo and mint-teal rim and holds it up to camera, while the coffee maker and crushed can stay still and soft in the background. No character's face is visible and no one lip-syncs; the locked DESIRE narrator says off-screen: “No brewing. No can. Just a measured dose.” Preserve the tin and pouch designs. Rack focus onto the pouch, crisp tempo.

**Sound / voiceover direction**
Narrator voiceover; no visible speaker. Calm, clear adult female-presenting voice in a low-mid register with a neutral North American accent, measured medium pace, crisp diction, dry understated confidence, and a straight-talking, no-hype delivery. Music: bright pluck arpeggio returns, with a small lift on “Just a measured dose.” Ambience: quiet morning room tone. SFX: a soft fabric lift of the pouch. Mix: speech clearly dominant; duck music about 10 dB under the line; keep effects short and never on top of a spoken number.

**Estimated length**
3.5 seconds

### Clip 24

**Script section / voiceover text**
“Cool Mint on the early shift.”

**Text-to-image prompt**
An adult man in his early thirties with light-olive skin, a short dark-brown fade haircut, a neatly trimmed short dark beard, warm hazel eyes, a friendly square face, and a broad athletic build, wearing a charcoal-grey henley under a fluorescent-orange high-visibility safety vest, dark-blue work jeans with a faded round tin ring worn into the right back pocket, and tan leather work boots. A slim round matte-black metal tin about the width of a palm and two centimeters tall, with a flush pressed lid, the word DESIRE in clean white uppercase sans-serif lettering centered on the lid, a small white NICOTINE FREE line beneath the logo, and a thin mint-teal flavor ring around the lid edge. A small white rectangular oral pouch with softly rounded corners, a slightly padded smooth fleece-like surface, and no visible grounds or leaks. He stands on a construction site at sunrise holding the open tin in one hand and a single pouch between two fingers of the other, with a relaxed half-smile, cool dawn light behind him. Medium close-up. Polished vertical 3D cartoon animation with soft rounded proportions, expressive faces, clean simplified shapes, crisp cool-toned cinematic lighting, murky olive-green antagonist accents, bright mint-teal and clean white solution energy, shallow depth of field, 9:16 composition.

**Image-to-video prompt**
The early-thirties man with light-olive skin, a short dark fade, a trimmed dark beard, and hazel eyes tucks the small white rounded-corner pouch under his upper lip, snaps the matte-black DESIRE tin with the white logo and mint-teal rim closed, and looks out over the site with a calm, ready expression; he stays silent and does not lip-sync while the locked DESIRE narrator says off-screen: “Cool Mint on the early shift.” Preserve his face, beard, build, vest, and the tin design. Slow push-in, fresh morning tempo.

**Sound / voiceover direction**
Narrator voiceover; the man reacts silently. Calm, clear adult female-presenting voice in a low-mid register with a neutral North American accent, measured medium pace, crisp diction, dry understated confidence, and a straight-talking, no-hype delivery. Music: pluck arpeggio adds a light upbeat hi-hat for the flavor run. Ambience: dawn wind and distant machinery. SFX: signature tin-lid click, a soft cool-mint air shimmer. Mix: speech clearly dominant; duck music about 10 dB under the line; keep effects short and never on top of a spoken number.

**Estimated length**
2.5 seconds

### Clip 25

**Script section / voiceover text**
“Watermelon Ice after lunch.”

**Text-to-image prompt**
An adult man in his early thirties with light-olive skin, a short dark-brown fade haircut, a neatly trimmed short dark beard, warm hazel eyes, a friendly square face, and a broad athletic build, wearing a charcoal-grey henley under a fluorescent-orange high-visibility safety vest, dark-blue work jeans with a faded round tin ring worn into the right back pocket, and tan leather work boots. A slim round matte-black metal tin about the width of a palm and two centimeters tall, with a flush pressed lid, the word DESIRE in clean white uppercase sans-serif lettering centered on the lid, a small white NICOTINE FREE line beneath the logo, and a thin watermelon-pink flavor ring around the lid edge. He sits at a cluttered site-office table covered in rolled blueprints, pulling the tin from his vest pocket with a focused expression, in warm midday light through a small window. Medium shot. Polished vertical 3D cartoon animation with soft rounded proportions, expressive faces, clean simplified shapes, crisp cool-toned cinematic lighting, murky olive-green antagonist accents, bright mint-teal and clean white solution energy, shallow depth of field, 9:16 composition.

**Image-to-video prompt**
The early-thirties man with light-olive skin, a short dark fade, a trimmed dark beard, and hazel eyes thumbs open the matte-black DESIRE tin with the white logo and watermelon-pink rim and turns back to the blueprints with a focused, steady look; he stays silent and does not lip-sync while the locked DESIRE narrator says off-screen: “Watermelon Ice after lunch.” Preserve his face, beard, build, vest, and the tin design. Gentle push-in, steady tempo.

**Sound / voiceover direction**
Narrator voiceover; the man reacts silently. Calm, clear adult female-presenting voice in a low-mid register with a neutral North American accent, measured medium pace, crisp diction, dry understated confidence, and a straight-talking, no-hype delivery. Music: upbeat flavor-run groove continues. Ambience: site-office fan and faint radio chatter. SFX: tin-lid click, a light icy shimmer. Mix: speech clearly dominant; duck music about 10 dB under the line; keep effects short and never on top of a spoken number.

**Estimated length**
2 seconds

### Clip 26

**Script section / voiceover text**
“Mixed Berry before the gym.”

**Text-to-image prompt**
An adult man in his early thirties with light-olive skin, a short dark-brown fade haircut, a neatly trimmed short dark beard, warm hazel eyes, a friendly square face, and a broad athletic build, wearing a plain black fitted training T-shirt, grey athletic shorts, and white trainers. A slim round matte-black metal tin about the width of a palm and two centimeters tall, with a flush pressed lid, the word DESIRE in clean white uppercase sans-serif lettering centered on the lid, a small white NICOTINE FREE line beneath the logo, and a thin deep berry-purple flavor ring around the lid edge. He stands at an open gym locker holding the tin, smiling slightly, a gym bag on his shoulder, in bright clean gym lighting. Polished vertical 3D cartoon animation with soft rounded proportions, expressive faces, clean simplified shapes, crisp cool-toned cinematic lighting, murky olive-green antagonist accents, bright mint-teal and clean white solution energy, shallow depth of field, 9:16 composition.

**Image-to-video prompt**
The early-thirties man with light-olive skin, a short dark fade, a trimmed dark beard, and hazel eyes flips the matte-black DESIRE tin with the white logo and berry-purple rim in his palm, pockets it, and walks toward the weights with an easy, confident stride; he stays silent and does not lip-sync while the locked DESIRE narrator says off-screen: “Mixed Berry before the gym.” Preserve his face, beard, build, gym clothing, and the tin design. Tracking follow shot, energetic tempo.

**Sound / voiceover direction**
Narrator voiceover; the man reacts silently. Calm, clear adult female-presenting voice in a low-mid register with a neutral North American accent, measured medium pace, crisp diction, dry understated confidence, and a straight-talking, no-hype delivery. Music: flavor-run groove peaks. Ambience: gym clanks and HVAC hum. SFX: a light tin flip whoosh, a locker door close. Mix: speech clearly dominant; duck music about 10 dB under the line; keep effects short and never on top of a spoken number.

**Estimated length**
2 seconds

### Clip 27

**Script section / voiceover text**
“It isn't a 300-milligram pre-workout, and it won't pretend to be.”

**Text-to-image prompt**
An adult man in his early thirties with light-olive skin, a short dark-brown fade haircut, a neatly trimmed short dark beard, warm hazel eyes, a friendly square face, and a broad athletic build, wearing a plain black fitted training T-shirt, grey athletic shorts, and white trainers. A squat, oversized cartoon supplement-tub creature with a glossy murky olive-green plastic body, a peeling off-white label scribbled with grey question marks and no numbers, a black screw-top lid tilted on its head like a cap, stubby charcoal-grey arms and legs, narrow yellow eyes, thick slanted black eyebrows, and a sly lopsided grin with uneven teeth. In a gym, he places the tub creature back onto a high supplement shelf while the creature sulks with drooping eyebrows and its question-mark label half peeled, in bright gym lighting. Medium shot. Polished vertical 3D cartoon animation with soft rounded proportions, expressive faces, clean simplified shapes, crisp cool-toned cinematic lighting, murky olive-green antagonist accents, bright mint-teal and clean white solution energy, shallow depth of field, 9:16 composition.

**Image-to-video prompt**
The early-thirties man with light-olive skin, a short dark fade, a trimmed dark beard, and hazel eyes slides the squat murky olive-green tub creature with the question-mark label, tilted black lid, narrow yellow eyes, and lopsided grin back onto the shelf with an amused, unbothered look, while the creature crosses its stubby arms and pouts; both stay silent and neither lip-syncs while the locked DESIRE narrator says off-screen: “It isn't a 300-milligram pre-workout, and it won't pretend to be.” Preserve both characters' faces, colors, and clothing. Slow pull-back, wry tempo.

**Sound / voiceover direction**
Narrator voiceover; the man and the Mystery Blend react silently. Calm, clear adult female-presenting voice in a low-mid register with a neutral North American accent, measured medium pace, crisp diction, dry understated confidence, and a straight-talking, no-hype delivery. Music: groove drops to the plain pad with one playful sour note for the pout. Ambience: gym room tone. SFX: a hollow plastic thunk on the shelf. Mix: speech clearly dominant; duck music about 10 dB under the line; keep effects short and never on top of a spoken number.

**Estimated length**
5 seconds

### Clip 28

**Script section / voiceover text**
“It's one known dose you chose.”

**Text-to-image prompt**
An adult man in his early thirties with light-olive skin, a short dark-brown fade haircut, a neatly trimmed short dark beard, warm hazel eyes, a friendly square face, and a broad athletic build, wearing a plain black fitted training T-shirt, grey athletic shorts, and white trainers. A slim round matte-black metal tin about the width of a palm and two centimeters tall, with a flush pressed lid, the word DESIRE in clean white uppercase sans-serif lettering centered on the lid, a small white NICOTINE FREE line beneath the logo, and a thin deep berry-purple flavor ring around the lid edge. Close-up of his open palm holding the closed tin at chest height, with his face softly out of focus behind it wearing a confident half-smile, against a clean gym background. Polished vertical 3D cartoon animation with soft rounded proportions, expressive faces, clean simplified shapes, crisp cool-toned cinematic lighting, murky olive-green antagonist accents, bright mint-teal and clean white solution energy, shallow depth of field, 9:16 composition.

**Image-to-video prompt**
The early-thirties man with light-olive skin, a short dark fade, a trimmed dark beard, and hazel eyes closes his fingers around the matte-black DESIRE tin with the white logo and berry-purple rim and gives the camera a small, confident nod; he stays silent and does not lip-sync while the locked DESIRE narrator says off-screen: “It's one known dose you chose.” Preserve his face, beard, and the tin design. Slow rack focus from the tin to his face, assured tempo.

**Sound / voiceover direction**
Narrator voiceover; the man reacts silently. Calm, clear adult female-presenting voice in a low-mid register with a neutral North American accent, measured medium pace, crisp diction, dry understated confidence, and a straight-talking, no-hype delivery. Music: clean pluck arpeggio returns, warm and settled. Ambience: soft gym room tone. SFX: none; let the line land. Mix: speech clearly dominant; duck music about 10 dB under the line; keep effects short and never on top of a spoken number.

**Estimated length**
2.5 seconds

### Clip 29

**Script section / voiceover text**
“DESIRE. Nicotine free. Every dose on the tin.”

**Text-to-image prompt**
A slim round matte-black metal tin about the width of a palm and two centimeters tall, with a flush pressed lid, the word DESIRE in clean white uppercase sans-serif lettering centered on the lid, a small white NICOTINE FREE line beneath the logo, and a thin mint-teal flavor ring around the lid edge. A slim round matte-black metal tin about the width of a palm and two centimeters tall, with a flush pressed lid, the word DESIRE in clean white uppercase sans-serif lettering centered on the lid, a small white NICOTINE FREE line beneath the logo, and a thin watermelon-pink flavor ring around the lid edge. A slim round matte-black metal tin about the width of a palm and two centimeters tall, with a flush pressed lid, the word DESIRE in clean white uppercase sans-serif lettering centered on the lid, a small white NICOTINE FREE line beneath the logo, and a thin deep berry-purple flavor ring around the lid edge. Hero shot of the three tins standing upright in a row on a glossy black surface, mint-teal on the left, watermelon-pink in the center, and berry-purple on the right, each softly backlit in its flavor color with gentle reflections. Polished vertical 3D cartoon animation with soft rounded proportions, expressive faces, clean simplified shapes, crisp cool-toned cinematic lighting, murky olive-green antagonist accents, bright mint-teal and clean white solution energy, shallow depth of field, 9:16 composition.

**Image-to-video prompt**
A slow band of light sweeps left to right across the three matte-black DESIRE tins with the white logo and mint-teal, watermelon-pink, and berry-purple rims, glinting off each logo in turn. No characters appear and no one lip-syncs; the locked DESIRE narrator says off-screen: “DESIRE. Nicotine free. Every dose on the tin.” Preserve all three tin designs and rim colors. Slow push-in, confident settled tempo.

**Sound / voiceover direction**
Narrator voiceover; no visible speaker. Calm, clear adult female-presenting voice in a low-mid register with a neutral North American accent, measured medium pace, crisp diction, dry understated confidence, and a straight-talking, no-hype delivery. Music: full, clean brand phrase at its highest intensity, still under the voice. Ambience: none. SFX: a soft light-sweep shimmer, then a subtle low impact under “DESIRE.” Mix: speech clearly dominant; duck music about 10 dB under the line; keep effects short and never on top of a spoken number.

**Estimated length**
3.5 seconds

### Clip 30

**Script section / voiceover text**
“Tap the link to pick your flavor. For adults 18 and over.”

**Text-to-image prompt**
A slim round matte-black metal tin about the width of a palm and two centimeters tall, with a flush pressed lid, the word DESIRE in clean white uppercase sans-serif lettering centered on the lid, a small white NICOTINE FREE line beneath the logo, and a thin mint-teal flavor ring around the lid edge. A slim round matte-black metal tin about the width of a palm and two centimeters tall, with a flush pressed lid, the word DESIRE in clean white uppercase sans-serif lettering centered on the lid, a small white NICOTINE FREE line beneath the logo, and a thin watermelon-pink flavor ring around the lid edge. A slim round matte-black metal tin about the width of a palm and two centimeters tall, with a flush pressed lid, the word DESIRE in clean white uppercase sans-serif lettering centered on the lid, a small white NICOTINE FREE line beneath the logo, and a thin deep berry-purple flavor ring around the lid edge. A hand holds a smartphone showing a blank bright product page above the three tins arranged in a gentle arc on a clean white surface, in soft mint-teal light. Polished vertical 3D cartoon animation with soft rounded proportions, expressive faces, clean simplified shapes, crisp cool-toned cinematic lighting, murky olive-green antagonist accents, bright mint-teal and clean white solution energy, shallow depth of field, 9:16 composition.

**Image-to-video prompt**
A thumb taps the smartphone screen, which glows a little brighter, while the three matte-black DESIRE tins with the white logo and mint-teal, watermelon-pink, and berry-purple rims stay still below. No character's face is visible and no one lip-syncs; the locked DESIRE narrator says off-screen: “Tap the link to pick your flavor. For adults 18 and over.” Preserve all three tin designs. Slow pull-back to reveal the full arrangement, calm closing tempo.

**Sound / voiceover direction**
Narrator voiceover; no visible speaker. Calm, clear adult female-presenting voice in a low-mid register with a neutral North American accent, measured medium pace, crisp diction, dry understated confidence, and a straight-talking, no-hype delivery. Music: bed thins to one sustained chord and ends on the signature tin-lid click after the last word. Ambience: none. SFX: a soft UI tap. Mix: speech clearly dominant; duck music about 10 dB under the line; keep effects short and never on top of a spoken number.

**Estimated length**
5 seconds

---

**Estimated total runtime: 117 seconds (~1:57) across 30 clips.**
