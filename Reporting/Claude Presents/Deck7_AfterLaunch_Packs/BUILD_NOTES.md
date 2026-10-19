# BUILD NOTES: Deck 7, "After Launch, Part 1: Packs, Locomotives and History, Explained"

**Status: COMPLETE. 24 of 24 slides built in three chunks (1 to 8, 9 to 16, 17 to 24), each audited and rendered before the next.** Nothing is left to resume.

Output: `After_Launch_Packs_Locomotives_and_History_Explained.pptx` (about 0.6 MB, one embedded image: P19). Branch `claude-presents-build-deck7`, built from `claude-presents-decks2`. Nothing outside this folder was touched.

## What was built

Every slide follows the brief's table: title, caption, tag, visual and labels as written. Every diagram is native shapes (rectangles, rounded rectangles, ovals, freeform polygons, connectors, one block arrow, one table). The only picture is P19 on slide 1 (cropped, rounded, credit under it).

| Slide | Tag chip | | Slide | Tag chip |
|---|---|---|---|---|
| 1 Title | none | | 13 Two sides of a card | Agreed |
| 2 Legend | none | | 14 Honest history | Agreed |
| 3 Core comes first | Agreed | | 15 The golden age | Proposed |
| 4 One shared engine | Agreed | | 16 Unlocks keep pace | Agreed |
| 5 Packs by region | Proposed | | 17 Where do the unlocks live? | Proposed |
| 6 Growing by updates | Proposed | | 18 Regional buildings | Proposed |
| 7 Packs work together | Agreed | | 19 Changing region with pack engines | Agreed |
| 8 Beyond Small, Medium, Large | Agreed | | 20 Friends and packs | Agreed |
| 9 Jobs, not a ladder | Agreed | | 21 Money and delivery | Undecided |
| 10 What "express" means here | Agreed | | 22 Where this stands | Provisional |
| 11 A cap on the roster | Agreed | | 23 Still undecided | Undecided |
| 12 Regions need not match | Agreed | | 24 Image credits | none |

Tag counts match the brief: Agreed 13, Proposed 5, Undecided 2, Provisional 1, no chip 3 (checked by script).

Inline chips (own row or own space, never over a bar, line or text): slide 5 (two Undecided), 6, 8, 11 (Proposed and Undecided), 15, 16, 17, 18, 19, 20 (Undecided), 22 (Provisional).

## Checks run

- `build/audit.py` on the final file: **no problems found.** It checks, for every slide: word count (caption plus labels, excluding title, status chip, slide number and credit line; a token counts as a word if it has a letter or digit, so the OQ codes count); smallest font size; alt text on every picture, group and table; no notes slide; no transition or timing XML; `lang="en-GB"` and Arial on every run; estimated text overflow in each box; text-on-text collisions; any connector line crossing label text; shapes off the slide; low text contrast against the shape's own fill; reading order (title first, caption before slide number).
- Rendered with LibreOffice and `pdftoppm -r 80` after each chunk. I looked at every slide of each chunk at full size, fixed what I found (see "Fixes made during review"), then looked at all 24 on a contact sheet and re-opened slides 4, 8, 11, 12, 13, 16, 18, 20 and 22 after their fixes.
- Package checks on the final file: no `notesSlides`; no `<p:transition>` or `<p:timing>`; document title "After Launch, Part 1: Packs, Locomotives and History, Explained", author "Claude (Early Locomotion project)", language en-GB; theme fonts and hyperlink colour set (Arial; hyperlinks orange so they are readable on the dark table); the "Commons" link on slide 24 is a real hyperlink to the P19 Commons page.
- Content scan of all slide text: no pound sign or other price, no pack name, no locomotive count as a number, no named engine, no date, no "will", no "under way", no Superseded idea. The words "Price" and "Price and delivery" appear only as the briefed Undecided labels (slides 5, 21, 23).
- Smallest text: 14 pt everywhere except the one credit line on slide 1 (10 pt) and the credits table on slide 24 (11 pt). Caption 20 pt. Slide number 14 pt.

## Deviations from the brief and rules (please read)

1. **Slide 23 is 46 words by a strict count (limit 45).** The brief's eight chip labels plus its caption add up to 46 tokens, because each label carries an OQ code in brackets and slide 23's "Buildings when a pack is missing (OQ23)" is seven tokens. Without the eight OQ codes it is 38. I kept every label word for word. If you want it at 45 or under, shorten that one label in PowerPoint. The status chip, the title and the "?" glyphs are not counted.
2. **Slides over 25 words (the limit is 25, hard ceiling 45).** Counts of caption plus labels: slide 5 (34), 8 (28), 13 (30), 14 (31), 15 (33), 17 (30), 18 (27), 19 (40), 20 (30), 22 (36), 23 (46). Most of this is the brief's own captions and labels. Words I added on top of the brief are listed in item 4; dropping those would bring slides 17 and 20 closer to 25.
3. **Title slide title wraps to four lines, not three.** At 54 pt bold in the left 55%, "After Launch:" / "Packs," / "Locomotives and" / "History". "Packs, Locomotives" does not fit one line at 54 pt in that width. I kept 54 pt rather than shrink the title. The P19 box is 5.3 in wide by 6.35 in tall (about 40% of the slide width, from x = 7.4 in), a little less than the brief's 45%, so that the semaphore and the engine front both stay in the crop.
4. **Words and labels I added that are not in the brief's visual column** (each needed to read the diagram without a presenter):
   - Slide 9: "Same category" (bracket above the two cards).
   - Slide 10: "Fast freight" and "Passenger coach" under the two vehicles. "Ticket sales" is the brief's own icon name, used as its label.
   - Slide 12: "Region A" and "Region B" above the shelves (same generic labels as slide 5).
   - Slide 16: "Early" and "Later" at the ends of the track, "Core" and "Pack" as track names (the brief names the tracks).
   - Slide 17: a key, "Core" (solid box) and "Pack" (dashed box), and the heading "Pack" on the separate column.
   - Slide 19: row labels "Core engine", "Pack engine, no match", "Pack engine, with match"; notes "Changes look" and "Unchanged"; the arrow reads "Switch region". The brief's "May change when a match exists" is used exactly.
   - Slide 20: "Has a pack", "No pack", "One world".
   - Slide 7: each pack block reads "Pack".
5. **Inline chips carry the state word.** To keep "never rely on colour alone", a chip whose briefed label does not contain its status word has the word added in front: slide 11 "PROPOSED · Lots of variety: an aspiration", slide 17 "UNDECIDED · Needs a technical check (OQ20)", slide 20 "UNDECIDED · Not checked (OQ27)", slide 22 "PROVISIONAL · Plans can change." Chips that already say "undecided" are unchanged. Inline chips are 14 pt bold (the style token says 12 pt; the multi-deck rule says nothing below 14 pt), and are sized to their text rather than fixed at 1.1 by 0.3 in.
6. **No label was shortened to fit.** All briefed labels are on the slides word for word. (The slide 23 chips wrap to two or three lines inside their cards.)
7. **Slide 23 chips do not say "undecided" in words.** Adding the word to eight chips would push the slide far over 45 words. The state is written in the slide chip (UNDECIDED), the title ("Still undecided") and the caption ("These questions are open"), and every chip is drawn in the Undecided outline style.
8. **Slide 17 caption bar is the taller two-line size** although the text fits on one line in LibreOffice (it is within 0.7 in of the edge, so a different renderer could wrap it). Its text is centred in the bar so it looks normal either way.
9. **Section label** (small caps text above the title in the style tokens) is not used: it would add words and the type rule forbids 12 pt.
10. **Credits slide extras.** Besides the required note "CC BY-SA photos are shown unmodified except for resizing." I added "The photograph on slide 1 is cropped to fit." because P19 is shown cropped. The brief's note is about BY-SA photos; this deck's only photo is CC BY 2.0.

## Things the owner and lead should know

- **P19 shows a locomotive number and a headboard inside the photograph itself** (the number plate on the smokebox door and a green headboard are visible on the engine front). The slides never name the engine, class or number: the on-slide credit reads "A real locomotive, for illustration. Photo: Ben Salter, CC BY 2.0.", the alt text describes it as a real British steam locomotive, and the credits table gives only author, licence and the Commons link. I did not edit the photograph (it must stay unmodified). If "no named engine" should cover what is readable in the photo, P19 needs swapping for another image or a different crop.
- **Illustrative counts.** Slide 11 draws six filled shelf slots, a bookend and three dotted slots. Slide 12 draws six slots in Region A and four in Region B. Slide 16 draws five stages and four pack engines. Slide 5 and 7 have three packs. These are drawing choices only, not roster counts. None of the design's roster numbers appears anywhere.
- **Dashed outline means "later".** Dashed orange outlines are used the same way throughout (later packs, pack engines, pack unlock tags). Solid means Core. This is a drawing convention, not a status chip.
- **Engines and stations** are simple native-shape silhouettes drawn for this deck (not the mod's models, not any real class).
- **Slide 6** shows a crossed-out price tag with the words "No charge per locomotive." The tag has no number or currency symbol on it.
- **Slide 22** uses only the states in the brief ("first" and "an idea"). "Under way" does not appear anywhere in the deck.
- **Slide 19** is the one to look at first for layout: three rows, one big "Switch region" arrow, the Agreed fallback shown as an engine that does not change, and the open matching rules as an Undecided chip.

## Fixes made during review

- Chunk 1: title duplicated on slide 1 (text was appended, not replaced); status chip "BACKGROUND" wrapped (chip text no longer wraps); engine chimney and chassis were invisible against the dark background (given a steel outline); slide 6 price-tag icon and note box crowded the staircase; slide 7 top pack sat too close to the title.
- Chunk 2: slide 13 last left row touched the card frame; slide 16 largest engines ran off the right margin and overlapped each other (resized, spacing widened); slides 11 and 12 sat high with empty space below.
- Chunk 3: slide 18 canopies clashed with the roof; slide 20 equator line crossed the "One world" label (label moved below the globe), the pack icon read as a plus sign (now a box with a lid) and an arrowhead pointed at the "?" circle; slide 21 right card ran past the margin; slide 22 sat high.

## What I could not check

- **Real PowerPoint.** I cannot open it here. All rendering was LibreOffice (Liberation Sans stands in for Arial and has the same metrics). Text fit in PowerPoint should match but may differ by a line in tight boxes: the audit's own text-fit estimate found no overflow. Please look at slides 13, 19, 22 and 23 in PowerPoint for wrapped text, and at slide 1 for the four-line title.
- Shape rendering of dashed outlines, the rounded picture crop and the table borders in PowerPoint (they use standard OOXML but were only seen in LibreOffice).
- Screen-reader reading order in PowerPoint's own Selection Pane. Shape order in the file is title, chip, visuals, caption, slide number.

## Files

- `After_Launch_Packs_Locomotives_and_History_Explained.pptx`: the deck.
- `BUILD_NOTES.md`: this file.
- `build/el_lib.py`: shape library (engine, person, rails, coach and wagon icons, chips, caption bar, picture crop, table borders, text measuring).
- `build/slides_1_8.py`, `build/slides_9_16.py`, `build/slides_17_24.py`: one function per slide, one file per chunk.
- `build/build_deck7.py`: builds the deck. Run `python3 build_deck7.py` for all 24 slides, or `python3 build_deck7.py 8 out.pptx` for a partial build.
- `build/audit.py`: the audit described above. `python3 audit.py deck.pptx [first last]`.
- `build/render.sh`: `render.sh deck.pptx outdir [dpi]` renders to PNG through LibreOffice and `pdftoppm`.

Requirements: Python 3, `python-pptx` 1.0.2, `Pillow`, LibreOffice (`soffice`) and `pdftoppm` for rendering, and the Liberation Sans fonts for text measuring.
