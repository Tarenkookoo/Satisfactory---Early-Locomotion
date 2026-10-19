# BUILD NOTES — Deck 9, "How the Mod Is Balanced, Explained"

**Status: complete. 18 of 18 slides built.** Nothing to resume.

- Output: `How_the_Mod_Is_Balanced_Explained.pptx` (about 127 KB, 16:9, 13.333 x 7.5 in, Arial, en-GB).
- Branch: `claude-presents-build-deck9`, built from `claude-presents-decks2`. Only files inside `Reporting/Claude Presents/Deck9_Balance/` were added.
- Image used: R02 only (slide 1). No photographs. No new downloads.
- Built with python-pptx 1.0.2 and Pillow. Every diagram is native shapes (rectangles, rounded rectangles, ovals, freeforms, connectors, a gear, a teardrop). The only picture is R02. The only real table is the credits table on slide 18.

## How to rebuild

```
cd "Reporting/Claude Presents/Deck9_Balance/build"
python3 build_deck.py            # writes ../How_the_Mod_Is_Balanced_Explained.pptx
python3 build_deck.py 9 out.pptx # first nine slides only
python3 audit.py ../How_the_Mod_Is_Balanced_Explained.pptx
./render.sh ../How_the_Mod_Is_Balanced_Explained.pptx /some/dir   # LibreOffice -> PDF -> PNG at 80 dpi
```

| File | Purpose |
|---|---|
| `build/lib.py` | Shape library: style tokens, text measuring (Liberation Sans = Arial metrics), chips, caption bar, locomotive/wagon/track/electric-train drawings, group and alt-text helpers, theme set-up. |
| `build/slides_a.py` | Slides 1 to 9 (chunk 1). |
| `build/slides_b.py` | Slides 10 to 18 (chunk 2). |
| `build/build_deck.py` | Builds the deck. |
| `build/audit.py` | Word counts, smallest font, alt text, notes/transitions, status chips, contrast, text fit, text overlaps, lines crossing text. |
| `build/render.sh` | Render to PNG for inspection. |

## Checks run

- Rendered the whole deck (LibreOffice, then `pdftoppm -r 80`) after each chunk and looked at every slide image. Re-rendered and re-looked at every slide that was changed. Looked at a contact sheet of all 18 at the end.
- `audit.py` on the final file reports **no problems**: every run has an explicit size and Arial; no text below 14 pt (credit line 10 pt, credits table 11 pt); contrast of text against its own fill at least 4.5:1; every text box fits its box (estimated with real font metrics); no text overlaps text; no connector crosses label text; every group, picture and table has alt text; no notes slides; no transitions or animations; no empty placeholders; the status chip on each slide matches the brief.
- Tag counts match the brief: Agreed 7 (slides 3, 4, 5, 7, 8, 12, 13), Proposed 3 (6, 9, 15), Undecided 2 (10, 17), Provisional 3 (11, 14, 16), no chip 3 (1, 2, 18).
- Text search of the whole package (slide text and alt text): "100 m", "half", "km/h", "Superseded", "16 to 24" and any code class name are absent. "150 m" appears once, on slide 6. No locomotive speeds anywhere. No wagon counts per class (20 and 32 are per wagon type, as the brief says).
- Document properties: title "How the Mod Is Balanced, Explained", author "Claude (Early Locomotion project)", language en-GB. Every text run is tagged en-GB.
- Reading order: title, status chip, visual groups, caption, slide number.
- Title is a real title placeholder on every slide. Shapes are named "Status chip", "Slide number" and "Credit line …" so `tools/polish.py` treats them as static. I ran `polish.py` on a throw-away copy: it works (78 animated shapes). The polished copy is not committed.

## Word counts

"Counted" = caption plus diagram labels plus inline-chip labels, not counting the title, the status chip, the slide number, credit lines, or bare status words (such as the UNDECIDED chips on slide 17). "All text" = every word on the slide.

| Slide | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Counted | 14 | 26 | 22 | 28 | 21 | 17 | 35 | 17 | 44 | 27 | 37 | 29 | 24 | 41 | 36 | 32 | 40 | 5 |
| All text | 28 | 37 | 27 | 34 | 27 | 23 | 42 | 23 | 50 | 32 | 44 | 35 | 29 | 47 | 41 | 37 | 52 | 30 |

Slides 2 and 18 are exempt. On the "counted" measure no slide is above 45 (the maximum is slide 9 at 44). Slides 4, 7, 9, 10, 11, 12, 14, 15, 16 and 17 are above the 25-word target because the brief's exact captions and labels already exceed it; I cut nothing from the brief. **If the owner counts every word on the slide, slides 9 (50), 14 (47) and 17 (52) are above 45.** Slide 17's total is mostly eight UNDECIDED chip words. Reducing these would mean cutting briefed text.

## Deviations from the brief and rules (please read)

1. **Slide 14 ranges use an en dash** ("2–3 km", "4–5 km", "6–7 km") instead of "2 to 3 km". With "to" the slide would have 49 counted words; with the dash it has 41. Meaning is the same. "about 7 km" and "about 10 km" are unchanged. Easy to revert in `slides_b.py`, function `s14`.
2. **Credit wording on slide 1 and slide 18.** The brief says "Early Locomotion project (visual development, not final art)." The addendum says mod renders read "(test model, not final art)". I followed the brief, because `ASSET_MANIFEST.md` describes R02 as visual development, not a test model.
3. **Slide 18 omits "CC BY-SA photos are shown unmodified except for resizing."** The addendum says a deck with no photographs shows only the renders table and the caption "This deck uses no photographs." I added one column to the table, "What it shows", from the manifest's alt text.
4. **Caption bar is 0.9 in high at y 6.2** (tokens: 0.6 in at y 6.4), on every slide, so two-line captions (slide 7) have breathing room. Content area therefore ends at y 6.1.
5. **Status chips are 1.6 x 0.4 in** (tokens: 1.5 x 0.4) so "PROVISIONAL" and "BACKGROUND" at 14 pt bold fit without crowding. Inline chips are 14 pt (tokens: 12 pt) because the rules allow nothing below 14 pt except credits and the credits table. The slide number is 14 pt for the same reason. I added no section label.
6. **Inline chips carry their full briefed label** (for example "Exact recipes: undecided (OQ02)"), outlined for Undecided and filled for Provisional. Slide 17 cards carry a plain UNDECIDED chip plus the question text.
7. **Slide 1 picture** is 5.13 in wide (about 38% of the slide, inside the right 45%), 6.2 in tall, cropped from the 16:9 render, with the credit under it. "Full height" is therefore 6.2 in, not 7.5 in, so the credit fits below.

## Interpretation choices (the brief is silent; each is shape only, no numbers)

- **Slide 10, "Later idea":** only "Medium tallest" is specified. Small and Large are drawn the same lower height. That is a neutral "not the fastest" level, not a claim that they are equal. "Earlier idea" rises Small, Medium, Large. Both ladders carry "Speed" and "Not to scale". The highest bar in each is orange.
- **Slide 13:** the width of each stop block stands for time stopped; green up-arrows from each stop to a "Reliability" bar show what a stop buys. The "To be tested" chip sits under the short stop (the top-up case). The brief does not say more than this.
- **Slide 4:** "pricier" is shown with a short coin stack (steam train) against a tall one (electric train). No prices or counts are implied.
- **Slide 8:** small engine with eleven wagons, large engine with one wagon, medium-sized engine with four wagons. Wagon counts here are illustration only and are not tied to any class.
- **Slide 9:** engine drawings are generic. Small has no tender; Medium and Large have a normal tender (this matches the design file). Wheel counts are not meaningful.
- **Slide 6:** "OQ02" is plain muted footer text, not a chip. The ruler follows the curve beside the track.
- **Slides 12, 15:** the small icons (coin, crate, clock, pause, gear and so on) are decoration drawn from shapes.
- **Slide 16:** the four markers carry no numbers, so no order or schedule is implied beyond the brief's row order.
- **Slide 17:** each card shows the briefed label word for word. Only one of the eight is literally a question; the others stay as briefed ("Questions only" means no answers are given).

## Design-file check

I read `Design/GAME_DESIGN.md` on `master` (Balance philosophy, Track design, Locomotives, Fuel and water servicing, Development and asset direction, OQ02, OQ05, OQ07 to OQ11). It agrees with the brief on every status and number used. The 16 to 24 range, the 50 m and 100 m values, the half-length limit and the old speed numbers are not shown. The "Where this stands" claims were checked against `PUBLIC_PRESENTATION_BRIEF_2026-10-18.md`; slide 16 says only "under way" for the test engine and "planned" for the rest.

## What I could not check

- I cannot open real PowerPoint. All visual checks are LibreOffice renders (Liberation Sans has Arial's metrics, so wrapping should match, but small differences are possible). Please open the deck in PowerPoint and look especially at: slide 6 (ruler and curved track, built from freeforms and rotated sleepers), slide 5 (curved track), slide 7 (two-line caption), slides 9, 10 and 11 (the cards, ladders and wagon grids), slide 14 (the table is drawn from shapes, so it is a diagram group, not a PowerPoint table), and slide 18 (a real PowerPoint table).
- The text-fit and contrast checks in `audit.py` are my own estimates, not PowerPoint's. Contrast is checked against the shape's own fill; text sitting on a panel without its own fill is assumed to be on the slide background (the two are close in luminance).
- Alt text and reading order were set and read back with python-pptx. I did not test with a screen reader.

## Open items for the owner

- Decide whether the three deviations that touch the rules (en-dash ranges on slide 14; no CC BY-SA sentence on slide 18; "visual development" wording for R02) should be reverted.
- Slides 9, 14 and 17 are above 45 words if every word on the slide is counted (see the table). Say if you want any briefed text cut.
