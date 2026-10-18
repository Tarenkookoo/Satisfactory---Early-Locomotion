# STAGE 2 BUILD NOTES — "Early Locomotion, Explained"

**RESUME POINT:** Chunks 1–3 (slides 1–31) are built, checked and committed. Resume at **chunk 4, slide 32**.

**PUSH BLOCKED:** every `git push` to `claude-presents-build-opus` has been refused by GitHub (HTTP 403: the Claude GitHub App has no access to this repository for the organisation). The commits exist only in the session's local clone until access is fixed (connect or reconnect GitHub at https://claude.ai/connect-github and install the Claude GitHub App on the repository), then `git push -u origin claude-presents-build-opus`.

Branch: `claude-presents-build-opus` (created from `claude-presents`; branch name set by the coordinator's override).

## How to rebuild

```
cd "Reporting/Claude Presents"
python3 build_deck.py                      # writes Early_Locomotion_Explained.pptx
RENDER_DIR=/some/tmp python3 build_deck.py --render 1 10   # also renders slides 1-10 to PNG (LibreOffice + pdftoppm)
python3 build/check_deck.py Early_Locomotion_Explained.pptx   # word counts, smallest font, alt text, fit, chips
```

Needs Python 3, `python-pptx` 1.0.2, Pillow, LibreOffice and poppler (`pdftoppm`) for renders, and the Liberation Sans fonts (same metrics as Arial) for the text-fit estimate. Renders are not committed.

Files: `build_deck.py` (driver), `build/lib.py` (shape library and slide base), `build/slides_a.py` … `slides_d.py` (one function per slide, four chunks), `build/check_deck.py` (checks). Image credits and alt text are read straight from `ASSET_MANIFEST.md`, so they cannot drift from it.

## Word-count method

"Words" = caption plus every label on the slide (digits inside numbered badges are not counted), including chips that carry extra words (for example "UNDECIDED (OQ01)"). Not counted: title, the corner status chip, inline chips that hold only a status word (AGREED, PROPOSED, PROVISIONAL, UNDECIDED; they are tags like the corner chip), section label, slide number and photo credit lines. The checker also prints the count including the title.

## Choices and small deviations (with reasons)

### Whole deck
- **Section label, slide number and inline chips use 14 pt**, not the 12 pt in the OUTLINE tokens. The brief allows nothing below 14 pt except credits (10 pt) and the credit tables (11 pt).
- **Corner status chip is 1.7 × 0.4 in** (outline 1.5 × 0.4) so upper-case PROVISIONAL and BACKGROUND fit at 14 pt bold. Right edge stays at 12.73 in.
- **Caption bar grows for two-line captions:** 0.6 in high at y 6.4 for one line; 0.88 in high at y 6.12 for two lines. The caption stays 20 pt and is never shortened.
- **No red text on the dark background** (4.1:1, below 4.5:1). STOP labels use a darker red pill (`#B3262B`, white text 5.8:1). Every state is also written in words.
- Theme fonts set to Arial; theme hyperlink colour set to a light blue (6.5:1 on the panel colour) so the credit links on slides 41–42 stay readable.
- Shapes without text that sit outside a group are marked decorative. Every picture and diagram group has alt text. All runs are tagged `en-GB`.

### Chunk 1 (slides 1–10)
- **Slide 1:** title 54 pt as specified; the caption sits under the title rule at 24 pt (title-slide layout, so no caption bar). Credit line under R01: "Early Locomotion project render. Early test model. Not final art." (the outline's wording with the project attribution in front).
- **Slide 5:** with every label in the outline the slide would have about 69 words (cap 45). Following the brief ("shorten the labels, not the caption"), the bracketed unlock lists for each tier became small engine pictograms instead of words: small tank engine, medium engine with tender, large engine with tender, electric train. Tier names stay. The Tier 6 label reads "Monorail: the game's electric trains". Footer: "Tiers and prerequisites:" with PROVISIONAL and UNDECIDED (OQ01) chips. 45 words.
- **Slide 6:** the cross-section is drawn end-on, so it shows one sleeper under the two rails (the spec says three sleepers; an end-on section only shows the nearest one). The photo beside it shows the repeated sleepers.
- **Slide 7:** P03 sits lower right (y 3.35 in) so the "Exhaust" label clears it. Badges 1–4 stay as specified.
- **Slide 8 (SPEC-A):** headings "Before" and "After" added above the two panels; tanks are 2.3 in tall (spec 2.6) to leave a strip for the chimney, steam puffs and the steam label. The "Empty first" tag sits inside the nearly empty water tank. The "(Agreed)" note uses an inline AGREED chip. 44 words.
- **Slide 9:** "Side tanks: water. Bunker: coal." is split into two callouts, so each points at its own part of the engine. Leader-line targets were read off the photos on a grid.
- **Slide 10 (SPEC-B):** the swing arrow is drawn as an arc over the crane arm, ending above the hatch.

### Chunk 2 (slides 11–20)
- **Slide 11 (SPEC-C):** coal heaps get a light outline so dark coal shows on the dark background. Section headings "Coal stage" and "Coaling tower" label the two stacked diagrams.
- **Slide 12:** the three block bands are neutral (no red/green state colours); block states are taught on slide 28. Signals carry STOP and CLEAR pills.
- **Slide 13:** cards are 2.9 × 1.75 in (outline 1.3 in tall) so three-line meanings fit at 18 pt. Exempt slide, 66 words.
- **Slide 14:** the row names (Track, Power, Stops, Signals, Station) are unquoted in the outline and are not printed; each cell carries a small icon instead. 43 words.
- **Slide 15:** "Short range" fans out to its three answers with three arrows.
- **Slide 16 (SPEC-G):** rows are 0.86 in apart (spec 1.0 in) so the last row clears the caption bar.
- **Slide 17:** R02, R05 and P02 sit in one row. At the specified sizes R05 cannot go under R02 and still leave room for the speed-rule band. To stay at 45 words, "A real railway, for comparison" became "Real railway, for comparison" and the footer became "Longest track piece:" plus an UNDECIDED (OQ02) chip (slide 40 uses the same wording).
- **Slide 18 (SPEC-F):** each bar's label sits above the bar (a 3.0 in bar and a label cannot share one 3.8 in card row); bars are 3.3 in. The Medium speed bar is hatched with a "FASTEST? UNDECIDED" chip. To stay within 45 words, the footer reads "Shape only. Not measured." (SPEC-G's wording) instead of "Bars show shape only. They are not measured values."
- **Slide 19:** the note reads "A related Fowler tank engine (a Jinty). The design's reference, the Dock Tank, has no survivor." It drops "to photograph" to stay within 45 words, and still says the photo is a related Jinty and that the Dock Tank has no surviving example.
- **Slide 20:** "Reference: Merchant Navy class" is a 16 pt label under the credit line so it can be read. The "Fastest class" row puts its PROPOSED and UNDECIDED (OQ05) chips on a second line so the words do not break.

### Chunk 3 (slides 21–31)
- **All native signals** draw the arm on the left of the post, as in the R03/R04 renders. This keeps arms clear of the trains.
- **Slide 21:** same layout as slides 19–20; the "Slower to speed up" row carries a PROPOSED chip.
- **Slide 22:** wagons are 4.6 × 1.6 in (outline 3.4 × 1.4) so the 32 squares stay readable.
- **Slide 23:** to stay within 45 words, the gauges are labelled with icons (coal heap, water drop) instead of words, the chip by the "Range left" card reads AGREED DIRECTION, "km" moved into the column headers ("Water (km)", "Coal (km)"), and ranges are written "2–3", "about 7" and so on. All values are exactly those in the outline. The table is a native PowerPoint table with alt text.
- **Slide 24:** the train faces left (engine, normal tender, gap, hatched auxiliary tender, three wagons, matching the outline's left-to-right order). Labels sit under the train. P18 sits bottom right at the specified 3.4 × 2.27 in; there is no room for it bottom left. "A real tender, for illustration" is a 14 pt label above it.
- **Slide 25 (SPEC-D):** P17 sits top right, so the water pipe enters the tower from above; a pipe from (12.3, 1.7) would have run under the photo. "Coal bunker" and "Water hatch" label the two circles on the docked engine.
- **Slide 26 (SPEC-E):** to stay within 45 words, five step labels are shorter: "Settle into dock", "Long steam hiss", "Water arm swings", "Finds the hatches" and "Folds away". The caption already says the machinery finds the hatches and folds away. Steps snake: row 2 runs right to left, with 6 under 5. The time strip has a clock icon, "Empty tanks" (long bar), "Small top-up" (short bar), and "Rates and times:" with PROPOSED and PROVISIONAL chips.
- **Slide 27 (SPEC-I):** the AGREED chip for the headline sentence sits inside the caption bar, at its right-hand end.
- **Slide 28 (SIG-28):** band A reads "Block A: occupied" (the spec says green) because the waiting train stands in it; a free band under a train would contradict "one train per block". The legend reads "Arm flat: stop / Arm raised: go" instead of "red arm = stop; raised arm = go", because the arm is red in both states (RESEARCH_NOTES object rule).
- **Slide 29 (SIG-29):** the separate fail-safe strip is left out because the caption already carries the exact sentence beginning "On real railways…". Repeating it would push the slide past 45 words. The labels "STOP: arm flat" and "CLEAR: arm raised" sit on the renders with arrows to the arms. Each render credit carries the addendum line "Blender model, not yet in the game." The corner chip ARM STYLE: UNDECIDED sits under the status chip.
- **Slide 30 (SIG-30):** the lever groups are labelled "Stop", "Distant", "Points" and "Lock", with "Example colours only" (spec: "Example colours; not fixed") to stay within 45 words.
- **Slide 31 (SIG-31):** to stay within 45 words: the steps read "Train in block", "Signal at STOP", "Train leaves" and "Lever pulled: arm lifts"; the link label reads "Bell codes"; the territory label reads "Box territory: limited" (the pointer to slide 32 dropped); the amber footer reads "In the mod: no player wiring." with an AGREED chip. Counterweights are drawn but not labelled; the alt text describes them. Blocks run 0.8–4.6–7.6–10.4 in (spec 5.0 / 8.0 / 11.0) so all three state pills stay inside the territory outline; signal names S1–S3 are not printed. Rods run from the box down to the ground and along the track to each post foot, so they cross neither the train nor the arms.

## Checks run so far

| Chunk | Rendered and inspected | Checker result |
|---|---|---|
| 1 (1–10) | All 10 slides at 80 dpi, fixed, re-rendered | 0 problems; max 45 words (slide 5); smallest text 14 pt outside credits |
| 2 (11–20) | All 10 slides at 80 dpi, fixed, re-rendered | 0 problems; max 45 words (slide 19); smallest text 14 pt outside credits |
| 3 (21–31) | All 11 slides at 80 dpi, fixed, re-rendered (28–31 twice) | 0 problems; max 45 words (slides 26, 30); smallest text 14 pt outside credits |
