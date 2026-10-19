# BUILD NOTES: Deck 4, "The Monorail Transition, Explained"

**RESUME POINT: the build is finished (22 of 22 slides). Nothing is left to build.** All work is committed and pushed to `claude-presents-build-deck4` (created from `claude-presents-decks2` at 9e06b15).

## What was built

- `The_Monorail_Transition_Explained.pptx`: 22 slides, 16:9 (13.333 x 7.5 in), Arial, charcoal and orange, built with python-pptx exactly to `DECK_BRIEF.md`. About 197 KB. Two pictures only: R02 (slide 1) and R01 (slide 20). No photographs, so no hyperlinks.
- Every diagram is native shapes (rectangles, ovals, freeforms, connectors), grouped, with alt text on every group, picture and the credits table.
- `build/lib.py`: shape library (chips, picture crop, table, track, engine, carriage, cursor, tick, cross and so on).
- `build/slides_a.py`, `slides_b.py`, `slides_c.py`: slides 1 to 8, 9 to 15, 16 to 22 (one function per slide).
- `build/build_deck.py` (builds the deck; optional argument = last slide to build), `build/check.py` (word counts, smallest font, overflow estimate, alt text, notes, transitions), `build/verify.py` (titles, chips and captions against the brief, tag counts, contrast, alt text, notes, transitions, document properties, image set, XML parse), `build/render.sh` (LibreOffice then `pdftoppm -r 80`).
- To rebuild: `python3 build/build_deck.py` (needs `python-pptx` and `Pillow`, and the bundle images in `Reporting/Claude Presents/images/`).

## Checks run

- Built and checked in the three chunks the brief names (slides 1 to 8, 9 to 15, 16 to 22). Each chunk was rendered with LibreOffice and `pdftoppm -r 80`, and I looked at every slide of the chunk. After the last chunk I looked at four contact sheets of all 22 slides, plus individual slides after each fix. Fixed along the way: "BACKGROUND" chip wrapping (chips widened to 1.7 in), a vehicle drawn on the steam cross-section on slide 3 (removed: the brief shows track only), a label colliding with supports on slide 7, an overlapping crane leg and crates on slide 14, a signal-box roof touching the rails on slide 10, text overflow estimate on slide 17, and empty or cramped areas on slides 8, 13, 17, 18 and 19.
- `check.py`: no overflow warnings, no missing alt text, smallest body font 14 pt. The only smaller text is the 10 pt credit lines (slides 1 and 20) and the 11 pt credits table (slide 22).
- `verify.py`: all 22 titles, tags and captions match the brief word for word. Tag counts match the brief (Agreed 6: slides 3, 4, 5, 6, 7, 19; Proposed 6: 8, 10, 11, 12, 13, 14; Undecided 5: 9, 15, 16, 17, 21; Provisional 2: 18, 20; no chip 3: 1, 2, 22). Lowest text contrast 4.93 to 1 (blue on the dark panel). No speaker notes, no transitions, no animations. Title "The Monorail Transition, Explained", author "Claude (Early Locomotion project)", language en-GB on every run. Reading order: title, chip, visuals, caption bar, slide number (slide 1: title, picture and credit, rule, caption). Zip test and XML parse of all 82 package parts pass. A scan of the slide XML found no out-of-order line properties and no duplicate shape IDs.
- Design facts checked against `Design/GAME_DESIGN.md` on `master` ("Mk1 to monorail conversion", "Track design", "Balance philosophy", "Progression", OQ01, OQ03, OQ12, OQ13) and, for slide 20, against `Reporting/PUBLIC_PRESENTATION_BRIEF_2026-10-18.md`. No difference from the brief was found that changes any status. Slide 20 uses only "Under way" and "Planned" and no test detail.
- **Not checked:** real PowerPoint (not available). LibreOffice was the only renderer; spacing, the hatch patterns on slide 11 and the transparent fills on slides 6, 8 and 16 may look a little different in PowerPoint. Text-fit was checked by render and by a font-metric estimate, not in PowerPoint.

## Deviations from the brief (all small; decisions for the owner)

1. **Slide 21, open-question codes moved into the chips.** The brief's labels end in "(OQ12)" and so on. With the codes in the text the slide came to 50 words (limit 45). Each card's Undecided chip now reads "UNDECIDED · OQ12" (or OQ03, OQ13, OQ01) and the question text is word for word without the code. The slide is 42 words (caption plus questions; chips not counted). Same approach as Deck 3. Slides 9, 16 and 17 keep "OQ12" as the footer the brief asks for; slide 18 keeps "(OQ01)" in its footer.
2. **Slide 20, labels and states.** "Test engine on the game's rails: under way" and the four "...: planned" items are written as the step label plus a state pill ("Under way", "Planned"). Same words, colon dropped. The first step also has an orange outline. The Provisional chip and "Plans can change." sit in a strip to the right of the R01 thumbnail (the brief gives no position). The thumbnail's credit line reads "Early test model, not final art." (the brief's wording); the full credit is on slide 22.
3. **Slide 4, shorter wheel labels.** "Steam wheel" and "Clamp wheel" (the brief names the pictures "a steam wheel on a rail" and "a clamp wheel on a beam" but gives no quoted label). Keeps the slide at 22 words.
4. **Slide 14, buffer position.** The brief says "a steam train at a left buffer". The buffer is drawn at the right-hand end of the steam track, the end that faces the interchange. The Agreed chip sits in a strip under the diagram, as the brief asks ("Steam trains cannot cross over").
5. **Slide 22, no CC BY-SA note and no source links.** The addendum says that a deck with no photographs lists only the renders and uses the caption "This deck uses no photographs." The note about CC BY-SA photos and the "Commons" links therefore do not apply. The table credit texts are the two the brief gives.
6. **Type sizes.** `OUTLINE.md` has 12 pt slide numbers and 12 pt inline chips; the rules say nothing below 14 pt, so slide numbers and inline chips are 14 pt (chips are a little wider). Top-right chips are 1.7 x 0.4 in (outline says 1.5 x 0.4) so that "PROVISIONAL" and "BACKGROUND" fit at 14 pt bold.
7. **Caption bar.** At y 6.3 in, 0.8 in high (outline: 6.4 in, 0.6 in) so a two-line 20 pt caption fits (slide 17 wraps). Line spacing on captions is 0.95.
8. **Slide 1, no slide number and no chip** (title slide). R02 is cropped to a portrait shape, centred on the left of the track, with the credit "Early Locomotion project (visual development, not final art)." under it.
9. **Slide 2 sketch.** A small decorative sketch of a slide with a tag in its corner (no text) sits beside the legend, as in Decks 2 and 3.
10. **Illustrations are generic.** The steam engine and wagon on slides 14 and 19 are generic orange silhouettes drawn from shapes, and the tractor on slide 19 is a simple drawing. None of them is the mod's model, and the deck does not claim otherwise.

### Labels added beyond the brief (direct labels so no meaning rests on colour alone)

Slide 5: legend "Steam", "Electric". Slide 7: "Steam track", "Monorail beam". Slide 8: "Hologram preview". Slide 10: "Steam station", "Electric station", "Coal stage", "Water tower", "Platform", "Signal box" (the brief names these objects but gives no quoted labels). Slide 11: "Station name", "Timetable", "Coal stage", "Water tower". Slide 12: "Semaphore", "Electronic signal". Slide 13: "Electric main line", "Steam branches". Slide 14: "Steam network", "Electric network", "Interchange". Slide 18: an extra Undecided chip on the footer (the footer says "provisional and undecided"). No fact, number or status was added. **Shortened labels: none** (every quoted label fits at 14 pt or more).

### Word counts

Counted: caption plus diagram labels plus inline text. Not counted: title, status chips (top-right and inline, including the code in slide 21 chips), number badges, slide number, 10 pt credit lines. Slides 2 and 22 are exempt.

| Slide | 1 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Words | 16 | 23 | 22 | 27 | 27 | 24 | 24 | 17 | 31 | 26 | 19 | 17 | 24 | 14 | 22 | 25 | 36 | 35 | 31 | 42 |

Over the 25-word aim: slides 5, 6, 10, 11, 18, 19, 20 and 21. All but slide 10 are over because the brief's own caption plus its quoted labels already exceed 25. Slide 10 is 27 on the brief's words and 31 with the two station labels I added. No slide is over 45. `build/check.py` prints the table.

## Things for the owner

- **Slide 14's inline Agreed chip.** The brief tags "Steam trains cannot cross over" as Agreed. In `GAME_DESIGN.md` the sentence "Steam cannot move directly between the two track systems" sits inside the paragraph headed "Proposed long term network". The Agreed incompatibility rule is stated in the paragraph before it. I followed the brief. Worth a glance that the owner is happy with the Agreed chip there.
- **Slide 6 says "like upgrading a belt".** The brief's caption is used word for word. The design file says "conveyors or miners".
- **Slide 20 and R01.** R01 is the yellow test model. It is labelled "Early test model, not final art." and not presented as any final locomotive.
- **`polish.py`** (transitions and fade-ins) was not run. Shape names `TITLE`, `CHIP`, `NUM`, `CREDIT` and `CAPTION` follow the names it treats as static, so it should work on this deck unchanged.

## Slides to look at first

3 (steam and monorail cross-sections), 4 (wheels and the crossed arrow), 6 (three-panel upgrade), 8 (hologram and warning dialog), 10 (station replacement, label spacing), 13 (network, interchange labels), 14 (crane and crates, strip under the diagram), 21 (chip text "UNDECIDED · OQ12").
