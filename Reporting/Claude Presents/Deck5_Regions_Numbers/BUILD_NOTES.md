# BUILD NOTES: Deck 5, "Regions, Running Numbers and Fleet Identity, Explained"

**STATUS: the build is finished (26 of 26 slides). Nothing is left to build.** Built on `claude-presents-decks2`, pushed to `claude-presents-build-deck5` only. To rebuild: `python3 build/build_deck.py` (needs `python-pptx` and `Pillow`; the picture comes from `../images/`).

## What was built

- `Regions_Numbers_and_Fleet_Identity_Explained.pptx`: 26 slides, 16:9 (13.333 x 7.5 in), Arial, charcoal and orange, built with python-pptx exactly to `DECK_BRIEF.md`. About 190 KB. One picture (R01, used on slides 1 and 24), no photographs, no hyperlinks (the brief's credits table has no link for a mod render).
- Every diagram is native shapes in a group with alt text. Locomotive, wagon and station drawings are **generic example silhouettes** drawn from shapes (British-type tank and tender, tall American-type, slim-chimney continental type). They are not the mod's models and not real engines; slide 26 says so.
- `build/lib.py` (shape library, modelled on the accepted Deck 3 library), `build/slides_a.py` (slides 1 to 9), `slides_b.py` (10 to 18), `slides_c.py` (19 to 26), `build_deck.py`, `render.sh`, and three audit scripts: `check.py` (word counts, smallest font, overflow estimate, alt text, notes, text/text and line/text collisions), `verify.py` (tag counts, contrast, alt text, reading order, language, picture aspect, notes/transitions), `xmlcheck.py` (zip integrity, XML parse, child order inside line and shape properties, unique shape ids).

## Design facts checked

Read `Design/GAME_DESIGN.md` on `master` (sections "Locomotive identity and running numbers", "Regional variants", OQ06, OQ27 to OQ30) and the dated public brief. The brief and the design file agree; no difference to record. No status was changed: slides 3 to 9 and 12 to 22 Agreed, 10, 11 and 25 Undecided (questions only), 23 Proposed, 24 Provisional. Identical regional statistics (Superseded) never appear: slide 8 says "about equally useful" and "No values chosen".

## Checks run

- Rendered with LibreOffice and `pdftoppm -r 80`; looked at every slide image chunk by chunk (1 to 9, 10 to 18, 19 to 26), fixed the problems found, then looked at two contact sheets of all 26 and re-opened slides 7, 9, 11, 13, 14, 20 and 21 at full size.
- Fixed during the build: a power symbol running into the title (slide 8), a station water tank poking out of its screen and panel (slides 4, 5), a train icon touching its question text (slide 11), a "Cab side" label touching the cab roof (slide 20), a one-word orphan line in captions (balanced caption width in `lib.py`), a low-contrast "31" on dark orange (slide 16), the American engine touching its panel edge (slide 9), map matches not agreeing with the list (slide 21).
- `check.py`: no overflow warnings, no missing alt text, no text/text or line/text collisions. Smallest font is 14 pt everywhere except the 10 pt credit lines and the 11 pt credits table. The detector was tested on a synthetic overlap before being trusted.
- `verify.py`: tag counts match the brief exactly (Agreed 18, Undecided 3, Proposed 1, Provisional 1, no chip 3). Every text colour is at least 4.5 to 1 against its fill. No speaker notes, transitions or animations. All runs are en-GB. Title, author ("Claude (Early Locomotion project)") and language set. Every picture and group has alt text. Shape order is title, status chip, visual, caption, slide number. The picture is not stretched.
- `xmlcheck.py`: 89 package parts, zip test and XML parse pass; no child-order problems.
- Searched all slide text for: Superseded, expansion, pack, price, currency signs, named engines (Dock Tank, Jinty, Big Boy, Merchant Navy and so on), American spellings. None present.
- **Not checked: real PowerPoint.** LibreOffice was the only renderer; spacing may differ by a few pixels in PowerPoint. The polish script (transitions and builds) was not applied, per the rules for this task.

## Word counts

Convention (same as Deck 3): caption, diagram labels and inline chips that carry words. Not counted: title, the top-right status chip, slide number, 10 pt credit lines, bare numerals. Open-question codes such as "(OQ06)" **are** counted where they sit in a label.

| Slide | Words | | Slide | Words | | Slide | Words |
|---|---|---|---|---|---|---|---|
| 1 | 14 | | 10 | 12 | | 19 | 26 |
| 2 | exempt | | 11 | 33 | | 20 | 27 |
| 3 | 25 | | 12 | 32 | | 21 | 24 |
| 4 | 21 | | 13 | 28 | | 22 | 27 |
| 5 | 20 | | 14 | 38 (45 if the numerals are counted) | | 23 | 19 |
| 6 | 29 | | 15 | 30 | | 24 | 30 |
| 7 | 27 | | 16 | 23 | | 25 | 41 (see deviation 1) |
| 8 | 32 | | 17 | 28 | | 26 | exempt |
| 9 | 29 | | 18 | 31 | | | |

Slides over 25 words are over because the brief's own exact caption plus its quoted labels already come to more than 25. None is over 45 by the convention above; slide 14 reaches 45 and slide 25 reaches 58 only if every numeral and every card-chip word is counted (see below).

## Deviations from the brief (all small; decisions for the owner)

1. **Slide 25, open-question codes moved.** The brief's eight labels carry "(OQ06)" and so on. With the codes inline the slide is 51 words plus the chips, over the 45 cap. Same fix as Deck 3: each card chip reads "UNDECIDED · OQ06" (the code is in the chip, not after the question). The question wording is verbatim. Five of the eight briefed labels are topics rather than questions ("Where IDs are stored", "Number pools and data", "Overflow number format", "Renumber cost and screens", "Search and filter screens"); kept verbatim, with no "?" added. If every word in the chips is counted, the slide is 58 words.
2. **Slide 8, the scales.** The brief says "two balance scales: a heavy engine with heavy wagons and a lighter engine with light wagons, both balanced". It does not say what balances them. I drew weight against power: the heavy train balances a large steam cylinder labelled "More power"; the lighter train balances a small one labelled "Less power". This follows the design's regional-performance section ("heavier/more powerful... lower absolute power and lighter stock", as illustrative principles). Pan labels "Heavy engine, heavy wagons" and "Lighter engine, light wagons" use the brief's own words. Please confirm this reading.
3. **Slides 20 and 21, "Agreed direction".** The brief calls these "Agreed direction" but the chip set has no such chip. The top-right chip is AGREED and a small muted "Agreed direction" note sits under it (two extra words per slide).
4. **Slide 6, which engine shape goes in which cell.** The brief lists three silhouette types (tank engine, tender engine with long boiler, tall American-style engine) without saying which cell gets which. British column: tank, then two tender engines; North American column: tall engine with headlamp and pilot at all three sizes; Continental European column: tank, then two slim-chimney engines with smoke-deflector plates. The mapping is illustrative ("Examples only" is on the slide). The teal, rose and sand colours are arbitrary example colours, not liveries.
5. **Slide 14, loops.** Added a dashed return arrow under each loop and a "You edit" label with a pencil icon (brief gives no label). 45 words if numerals are counted, 38 by the convention.
6. **Slide 16, "after" digits.** The brief gives only "47 298". The first part after switching is shown as "31", an invented example, inside the "Example only" label.
7. **Slide 15, no invented numbers.** Plates show digit blocks, not numbers. Historical Operator plates differ in length, block count and colour band; the three colours stand for "old railway companies" generally and name none.
8. **Slide 3, default selection.** The selector shows "British" selected because it is first in the list. It is not a default claim; "Examples only" and the Undecided chip (OQ06) stay on the slide.
9. **Slide 24, step wording.** The brief writes "Test engine on the game's rails: under way". Shown as the step title plus an "Under way" pill (orange for under way, grey "Planned" for the rest). Only the two permitted states are used.
10. **Slide 26, extras.** The table has four columns (Slot, Slides, What it shows, Credit) and a 14 pt line saying the engine, wagon and station drawings are generic silhouettes, not the mod's models. The brief did not ask for that line.
11. **Slide 1, picture width.** The title needs 6.9 in at 54 pt bold to wrap to three lines, so R01 is 4.93 x 6.4 in (a little under 45 percent). It is cropped, not stretched, around the engine's front. Credit under it: "Early Locomotion project render. Early test model, not final art."
12. **Type size.** The 12 pt inline chips, section label and slide number in `OUTLINE.md` are not used: `MULTI_DECK_RULES.md` says nothing below 14 pt, so inline chips and slide numbers are 14 pt.
13. **Slide 2.** A small decorative sketch of a slide with a tag in its corner sits beside the legend, as on Decks 2 and 3.
14. **Added labels** the brief does not list (short, plain): slide 3 "World style"; slide 4 "Player 1", "Player 2", "One shared world style"; slide 5 "Station", "Engine", "Wagon", "Before", "After"; slide 8 "More power", "Less power"; slide 9 "British style", "North American style", "World style", "Lead engine", "Lone wagon" (the style bands carry the style by colour, shape and words); slide 12 "Fleet ID" on the two pillars; slide 13 step labels and badges; slide 16 "Switch style", "Changes", "Stays"; slide 17 "Yes", "No"; slide 18 "Dismantled", "Number pool", "Pool full", "Overflow"; slide 19 "Renumber unlock", "Unlock", "Edit number"; slide 21 "Class", "Number", "Matches only"; slide 22 "Not reused"; slide 24 step titles.

## Shortened labels

None. Every briefed label is on its slide word for word, except where deviation 1 moves a code into a chip.

## For the owner

- **Real-world identifiers.** Slide 21 uses "9F" and "92214" because the brief requires them (the design file calls them illustrations of a class search and a specific-engine search). They are real-world identifiers: a class designation and a stock number. They carry the "Example only" label. If you would rather avoid any real stock number, swap "92214" for an invented one.
- **Slide 16 "47 298"** is the design file's own illustration number, also labelled "Example only".
- **Slides to open first in real PowerPoint:** 8 (scale reading), 6 (silhouette grid), 9 (consist rows), 14 (two loops), 12 (hidden identity), 20 (number marks and leaders), 21 (fleet search), 25 (codes in chips).
- No price, no pack, no expansion locomotive and no named engine appears anywhere in the deck.
