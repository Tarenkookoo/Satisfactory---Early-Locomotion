# BUILD NOTES: Deck 3, "Coal, Water and Servicing, Explained"

**RESUME POINT: the build is finished (24 of 24 slides). Nothing is left to build.**
**Push status: NOT PUSHED. Every write to GitHub from the cloud session was refused: `git push -u origin claude-presents-build-deck3` returned HTTP 403 ("Claude doesn't have GitHub access to Tarenkookoo/Satisfactory---Early-Locomotion for your organization"), at the end of each chunk and again at the end; the GitHub tool also refused to create the branch ("403 Resource not accessible by integration"). Nothing was pushed to any branch. All work is committed on the local branch `claude-presents-build-deck3` (commits d09fb51, 413f1a5, e92c736 plus the final notes commit), built on `claude-presents-decks` at 9f3e718. To finish: an owner of the GitHub organisation installs the Claude GitHub App on this repository (https://github.com/apps/claude/installations/select_target) or reconnects GitHub at https://claude.ai/connect-github, then someone runs `git push -u origin claude-presents-build-deck3` from the session's checkout. Or regenerate the deck anywhere with `python3 build/build_deck.py` (needs `python-pptx` and `Pillow`, and the images from branch `claude-presents-decks`).**

## What was built

- `Coal_Water_and_Servicing_Explained.pptx`: 24 slides, 16:9 (13.333 x 7.5 in), Arial, charcoal and orange, built with python-pptx exactly to `DECK_BRIEF.md`. About 2 MB. 10 pictures (9 files; P17 is used on slides 1 and 12), 8 hyperlinks.
- `build/lib.py`: shape library (chips, pictures with crop, tables, locomotive and wagon icons, gauges, arrows).
- `build/slides_a.py`, `slides_b.py`, `slides_c.py`: slides 1 to 8, 9 to 16, 17 to 24 (one function per slide).
- `build/build_deck.py` (builds the deck), `build/check.py` (word counts, smallest font, text-overflow estimate, alt text, notes), `build/verify.py` (tag counts, contrast, links, notes, transitions, document properties), `build/render.sh` (LibreOffice then `pdftoppm -r 80`).

## Checks run

- Rendered every slide with LibreOffice and `pdftoppm -r 80` and looked at every slide image, chunk by chunk (1 to 8, 9 to 16, 17 to 24), then at two contact sheets of all 24. Fixed: a diagram colliding with the title (slide 3), invisible coal fills, crosshairs invisible on orange (slide 15), chips wrapping (slide 23), label overlaps (slides 11 and 19).
- `check.py`: no text-overflow warnings, no missing alt text. Smallest font is 14 pt, except credit lines (10 pt) and the credits table (11 pt).
- `verify.py`: tag counts match the brief (Agreed 11, Background 4, Provisional 3, Proposed 2, Undecided 1, no chip 3). Contrast of every text colour against its fill is at least 4.5 to 1 (the seven warnings it prints are text sitting on a separate shape it cannot see; checked by hand). No speaker notes, no transitions, no animations. Title, author ("Claude (Early Locomotion project)") and language en-GB set. Every picture and diagram group has alt text; each slide has a real title placeholder; shape order is title, chip, visual, caption.
- Zip test and XML parse of all 82 package parts pass.
- **Not checked:** real PowerPoint (not available). LibreOffice was the only renderer; spacing in PowerPoint may differ by a few pixels. Hyperlinks were not clicked (they are the exact URLs from `ASSET_MANIFEST.md`). Rotated engine icons on slide 9 are groups with a rotation; they render correctly in LibreOffice.

## Deviations from the brief (all small; decisions for the owner)

1. **Slide 14, step labels shortened.** Nine full labels plus caption and labels came to 54 words, over the 45-word cap. Used: "Approach slowly", "Settle in", "Long steam hiss", "Coal chutes", "Water arm swings", "Find the hatches", "Tanks fill", "Machinery folds away" (Proposed chip kept), "Depart". The caption and the "Rates and times: Proposed or provisional" note are unchanged except that "Transfer" is dropped from the note. Original wording is in the brief if the owner prefers it and accepts 54 words.
2. **Slide 10:** ranges written "2–3 km" (en dash) instead of "2 to 3 km" so the slide stays under 45 words. Same values. An inline Provisional chip sits in the table header as well as the top-right tag.
3. **Slide 23:** the open-question code is inside each chip ("UNDECIDED · OQ08") instead of a "(OQ08)" suffix on the question, to keep the slide at 45 words. Questions only; no answers.
4. **Slide 17:** the Agreed chip is at the right end of the caption bar (the caption is the headline sentence).
5. **Slide 19:** P18 is 3.4 x 1.68 in (cropped) instead of 3.4 x 2.3 so it clears the train strip; its credit line also names the author and licence.
6. **Slide 12:** the P17 inset is 2.18 x 1.23 in (spec 2.4 x 1.4) so it clears the pipe.
7. **Slides 6 and 7:** P06 and P07 are portrait photos cropped to fit; P06 is cropped to its upper part (arm and hanging bag).
8. **Type size:** the 12 pt section label and 12 pt slide number / inline chips in `OUTLINE.md` are not used; `MULTI_DECK_RULES.md` says nothing below 14 pt, so slide numbers and inline chips are 14 pt (chips are a little wider).
9. **Slide 16:** an Undecided chip sits on the "Rates and buffers: undecided (OQ08)" line (the brief names no chip there). Slide 14 uses two stacked time bars (long and short) instead of one bar with two fills.
10. **Slide 24:** the R01 row says "Project render" in the link column; P17 lists slides "1, 12".
11. **Slide 2:** a small decorative sketch (a slide with a tag in its corner) was added beside the legend; it has no text.
12. **Engine and wagon drawings** on slides 9, 15, 17, 19, 20 and 21 are generic orange silhouettes drawn from shapes. They are not the mod's models.

## Word counts

Counted: caption plus diagram labels plus inline chips that carry their own text. Not counted: the title, plain status chips (AGREED and so on), bare numbers (badges), slide numbers and 10 pt credit lines. Slide 2 and slide 24 are exempt. No slide exceeds 45 (the highest are slides 14 and 23 at 45, then slides 4 and 12 at 43). Slides at 26 to 45 words are over the 25-word aim because the brief's own exact captions plus its quoted labels already come to more than 25: 4, 5, 10, 12 to 23. `build/check.py` prints the table.

## Design checks

- Statuses follow the brief. Proposed items keep visible Proposed chips (slide 14 step 8, slide 15 target names, slide 17 facility set, slide 18 water-only stop and the timetable, slide 19 one-vehicle model and both tender types). Playtest numbers (slides 10 and 16) carry Provisional chips and the footer "Not guaranteed distances or tank sizes." No Superseded idea appears. Slide 4 shows no coal-to-water ratio. Slide 11 does not claim Compacted Coal saves water. Slides 12 and 13 give no dimensions. Slide 22 uses only "Under way" and "Planned" and says nothing implying coal, water or servicing work.
- Wording was checked against the "Fuel and water servicing", "Stations", "Auxiliary tenders", "Service points" and "Balance philosophy" sections and OQ08 to OQ11 on `master` (`Design/GAME_DESIGN.md`) and against the dated public brief for slide 22. No difference from the brief was found.
- Renders R03 and R04 do not appear in this deck, so the "Blender model, not yet in the game" line is not needed. R01 appears only on slide 22, labelled "Early test model, not final art."

## Slides to look at first

14 (shortened labels), 15 (target marks), 12 (station plan), 6 and 7 (diagrams beside photos), 19 (tender strip), 22 (status wording).
