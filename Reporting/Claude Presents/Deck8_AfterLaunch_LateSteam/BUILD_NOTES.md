# BUILD NOTES: Deck 8, "After Launch, Part 2: Late Steam, Advanced Driving and Prestige, Explained"

**RESUME POINT: the build is finished (25 of 25 slides). Nothing is left to build.** Pushed to `claude-presents-build-deck8` only.

## What was built

- `After_Launch_Late_Steam_Driving_and_Prestige_Explained.pptx`: 25 slides, 16:9 (13.333 x 7.5 in), Arial, charcoal and orange, built with python-pptx to `DECK_BRIEF.md` and the style tokens in `OUTLINE.md`. About 0.27 MB. One picture (P12, title slide) and one hyperlink (credits).
- `build/lib.py`: shape library (chips, groups with alt text, pictures with crop, tables, locomotive, coach, semaphore, lever, padlock, price tag, trophy, globe and other icons).
- `build/slides_a.py`, `slides_b.py`, `slides_c.py`: slides 1 to 9, 10 to 17, 18 to 25 (one function per slide).
- `build/build_deck.py` builds the deck. `build/check.py` prints word counts, smallest font, a text-fit estimate and missing alt text. `build/verify.py` checks tag chips, contrast, links, notes, transitions, document properties and package integrity. `build/render.sh` renders with LibreOffice then `pdftoppm -r 80`.
- Every diagram is native shapes grouped per slide with alt text. Images: bundle copy of P12 only. No new downloads, no other file touched.

## Checks run

- Built in the three chunks the brief names (1 to 9, 10 to 17, 18 to 25). After each chunk I rendered with LibreOffice and `pdftoppm -r 80` and looked at every slide image, then fixed what I found: slide 5 label sitting on the tracks and a hard-edged veil; slide 7 reach label on the ring edge and posts overlapping; slide 8 cross hiding the label (text now sits above the cross); slide 15 hill drawn as a box (contour now separate); slides 16 and 17 locomotive and swatch spacing; slide 23 stray dashes and cramped text; slide 25 harsh table borders; chip text fitting. A final contact sheet of all 25 confirmed the story reads in order.
- `check.py`: no text-overflow warnings, no missing alt text. Smallest font is 14 pt on every slide. The only smaller text is the slide 1 credit line (10 pt) and the credits table (11 pt).
- `verify.py`: tag counts match the brief exactly. Agreed 16 (slides 3, 4, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21), Proposed 4 (6, 7, 18, 22), Provisional 1 (23), Undecided 1 (24), no chip 3 (1, 2, 25). No speaker notes, no transitions, no animations. Title, author ("Claude (Early Locomotion project)") and language en-GB are set; every run is tagged en-GB. No empty placeholders. Zip test and XML parse of all 87 package parts pass. A separate script confirmed the child order of every `a:ln`, `spPr`, `tcPr` and `rPr` is schema-valid (the usual cause of a PowerPoint "repair" prompt).
- `verify.py` prints 10 "low contrast" lines (slides 12, 19, 20). These are dark text on orange or amber badges and tags that sit on a separate shape the script cannot see. Checked by hand: dark `#101418` on orange or amber is well above 4.5 to 1.
- Reading order is title, status chip, visual (diagram group or picture), caption. On slide 1 it is title, picture, credit, caption.

## Not checked

- Real PowerPoint (not available here). LibreOffice was the only renderer; spacing may differ by a few pixels in PowerPoint.
- The hyperlink on slide 25 was not clicked. It is the exact `ASSET_MANIFEST.md` URL.
- The only rotated shapes are the teardrop flame icon on slide 12 (two teardrops turned 45 degrees). They render correctly in LibreOffice; not seen in PowerPoint. Every semaphore in this deck is drawn in its STOP position (flat arm), so there is no rotated signal arm.

## Deviations from the brief (all small; decisions for the owner)

1. **Slide 14, punctuation.** The four cause and effect labels are drawn as two boxes joined by an arrow, so the colon is dropped: "Wrong settings" to "Weaker pull", "Too much power" to "Wheels slip", "Low steam pressure" to "Less power", "Weak fire" to "Weaker engine". The words are as briefed.
2. **Inline chips carry the status word.** To avoid relying on colour, the Background chip on slide 19 reads "BACKGROUND  Like the game's golden trophies" and the Provisional chip on slide 23 reads "PROVISIONAL  Plans can change." The Undecided chips already contain "undecided" in the briefed text, so they have no extra prefix. Slide 24 cards each carry a plain "UNDECIDED" chip, with the question and its OQ code as the card text.
3. **Short labels added so each diagram can be read alone** (all taken from the brief's own visual description, none adds a fact): slide 6 "Smaller terminal", "Bigger terminal", "Extra platforms", "Larger service yard"; slide 7 "Small signal box", "Large signal box", "Short reach", "Wide reach"; slide 10 "Preselected"; slide 11 "Crew"; slide 15 "Speed" and "Hill"; slide 17 "The pack you own"; slide 21 "Normal engine" and "Prestige engine". Slide 25 also has one extra note: "The photograph shows a real steam locomotive. It is not a model from the mod."
4. **Word count.** Counted: caption plus diagram labels plus inline chips that carry text. Not counted: title, the top-right status chip, plain UNDECIDED chips, bare numbers, slide numbers, credit lines. Slides 3 (27), 9 (26), 13 (27), 14 (38), 15 (32), 23 (29) and 24 (41) are over the 25-word aim because the brief's exact captions plus its own quoted labels already exceed 25. None is above 45. Slide 2 (26) and slide 25 (33) are exempt. No label was shortened.
5. **Type sizes.** The 12 pt section label, slide number and inline chips in `OUTLINE.md` are not used, because `MULTI_DECK_RULES.md` allows nothing below 14 pt except credit lines and the credits table. Slide numbers and inline chips are 14 pt. No section label is drawn (the brief has no section column).
6. **Status chip** is 1.62 x 0.4 in (right edge still at 12.7 in) instead of 1.5 x 0.4, so "PROVISIONAL" is not cramped.
7. **Caption bar** is 12.13 x 0.76 in at y 6.28 instead of 12.13 x 0.6 at y 6.4, so two-line captions fit (slide 5 wraps to two lines). Content area therefore ends at about y 6.15.
8. **Slide 1 picture and credit.** P12 is cropped (not stretched) to the portrait slot, 4.63 x 6.35 in, focused on the front of the engine. The credit line reads "A real steam locomotive, shown for illustration. Photo: Tony Hisgett, CC BY 2.0." It gives no class, name or number. **Owner note:** the photograph itself, being unmodified, shows the real engine's smokebox number and nameplate. My text never names it. If the owner prefers a crop with neither visible, say so.
9. **Slide 25** lists only P12, with author and licence in separate columns ("Tony Hisgett" and "CC BY 2.0") and "Commons" as the hyperlink. The required note "CC BY-SA photos are shown unmodified except for resizing." is included although P12 is CC BY, not BY-SA. The slide 1 crop is a crop, not any other change.
10. **Locomotive, coach and signal drawings** (slides 12, 16, 18, 19, 21, 22, 7, 8) are generic silhouettes drawn from shapes. They are not the mod's models and name no real engine. Livery colours on slides 16 to 18 are arbitrary examples.
11. **Slide 2** has a small decorative sketch (a slide with a tag in its corner) beside the legend, as on Decks 2 and 3. It has no text.

## Design checks

- Wording checked against `Design/GAME_DESIGN.md` on `master`: "Post-release enthusiast expansion programme", "Late steam and advanced infrastructure", "Advanced manual driving — refined Agreed scope", "Liveries and cameo content", "VIP / Prestige locomotive framework — Agreed", OQ22, OQ24, OQ25. No difference from the brief was found.
- All of it is post-launch. Slide 1 and slide 23 say so. No price (the slide 17 tag is blank), no named famous engine, no engine count, no formula, no date. Examples are marked "Examples only." (slide 16) or kept generic.
- Slide 3, 4, 5, 8: steam never gets electric's abilities (slide 8 crosses out "Electronic-signal powers"). Slides 6 and 7 are Proposed and carry the Proposed chip, slide 6 with its Undecided chip. Slides 9 to 15 (advanced driving): Agreed in scope, with Undecided chips for screens (10), rules (14) and how much better (15). Slide 14 says plainly that explosions and permanent damage are not features. Slide 15 draws Simple as a steady, close second to Advanced, with the size of the gap undecided. Slide 18 is Proposed and unchecked. Slides 19 to 21 Agreed with no real names, numbers or prices. Slide 22 Proposed with no passengers shown. Slide 23 says "an idea" for all four items and nothing is "under way". Slide 24 shows questions only.
- Superseded ideas: none appear.

## Slides to look at first

14 (cause and effect split), 15 (hill and speed lines), 12 (the fourth control, Brake, is shown with "+" because the title says three things), 20 (nameplate card), 9 (levers), 4 (terminal plan), then 5 and 7 (veil and rings), 19 and 21 (engine drawings).
