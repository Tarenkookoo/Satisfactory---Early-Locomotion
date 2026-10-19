# BUILD NOTES: Deck 6, "Your Railway Guide: Lessons and the Build Menu, Explained"

**RESUME POINT: the build is finished (23 of 23 slides). Nothing is left to build.**
Branch `claude-presents-build-deck6` (built from `claude-presents-decks2`). Date: 19 October 2026.

## What was built

- `Railway_Guide_Lessons_and_Build_Menu_Explained.pptx`: 23 slides, 16:9 (13.333 x 7.5 in), Arial, charcoal and orange, built with python-pptx to `DECK_BRIEF.md`. About 94 KB. **No pictures and no media files**: every drawing is a native shape. No speaker notes, transitions or animations.
- `build/lib.py`: shape library (chips, bubbles, the placeholder avatar, miniature table, semaphore, icons).
- `build/slides_a.py`, `slides_b.py`, `slides_c.py`: slides 1 to 8, 9 to 16, 17 to 23 (one function per slide).
- `build/build_deck.py` builds the deck. `build/verify.py` runs the checks. `build/render.sh` renders with LibreOffice then `pdftoppm -r 80`.

## Checks run

- Built and rendered in the three chunks the brief names (1 to 8, 9 to 16, 17 to 23). Looked at every slide image after each chunk, fixed what I saw, then looked at two contact sheets of all 23 and at slides 17 and 22 again at full size.
- Fixed during the build: slide 7 note wrapping and shelf running past the margin; slide 8 station label crowding the train; slide 9 caption bubble wrapping and its tail missing the ring; slide 11 cards too short; slide 15 semaphore arm leaving its panel; slide 17 tab label touching the tab edge; slide 10 title-bar contrast.
- `verify.py` (all pass): word counts per slide; smallest font is 14 pt everywhere (no credit lines or credit table are needed, so there is no 10 or 11 pt text); no text-overflow estimates; no shape outside the slide; every diagram group has alt text; every run is en-GB; text-on-fill contrast is at least 4.5 to 1 (it looks at the shape's own fill, then the nearest filled shape underneath); no notes slides, transitions, animations or media; document title, author ("Claude (Early Locomotion project)") and language set; all 43 XML parts parse; no duplicate shape ids; `a:ln` child order is valid.
- Tag counts match the brief: Agreed 9 (3, 4, 5, 6, 7, 8, 9, 10, 12), Proposed 7 (11, 14, 15, 16, 17, 18, 20), Undecided 3 (13, 19, 22), Provisional 1 (21), no chip 3 (1, 2, 23). Slide chips are top right on every slide except 1, 2 and 23.
- Text dump read against the brief: every caption is word for word. Searched the deck for third-party sound or product names, the "used to be good" idea, prices and guide dialogue: none. The only guide speech is the bubble "...". "Dialogue not written yet." is a briefed label.
- Zip test and XML parse pass.
- **Not checked:** real PowerPoint (not available). LibreOffice was the only renderer; spacing may differ slightly in PowerPoint. The slide 5 strike-through (font attribute) and rotated gear teeth render correctly in LibreOffice but have not been seen in PowerPoint.

## Word counts (caption plus labels; plain status chips, titles, bare numbers and slide numbers not counted)

Slides 2 and 23 are exempt. No slide is above 45. Slides over the 25-word aim, because the brief's own exact text plus its quoted labels already come to more than 25: 3 (36), 7 (27), 11 (38), 14 (27), 17 (26), 20 (26), 21 (27), 22 (40). All others are 25 or fewer. `build/verify.py` prints the table.

## Deviations, additions and interpretations (all small)

1. **Shortened labels: none.** Every briefed label is used word for word at 14 pt or more.
2. **Slide 23 and the addendum.** The addendum says a deck with no images shows "that sentence alone". The brief says the slide shows that sentence and a second line. I followed the brief: caption bar "This deck uses no photographs." plus "All drawings are native shapes made for this deck." There is no table because there is nothing to credit.
3. **Slide 22.** The brief says each card has an outline Undecided chip reading the question. I drew each card with a small outline "UNDECIDED" chip at the top and the briefed question as the card text (so the status is written, not only drawn). Questions only; no answers.
4. **Extra short labels added for a newcomer (no facts):** slide 7 "Open" and "Locked" over the tile groups; slide 8 "Train", "Station", "Semaphore", "Signal box"; slide 9 button words "Pause", "Replay", "Previous", "Next"; slide 10 title-bar words "Railway library"; slide 13 origin label "The surprise"; slide 17 "The game's own tab" under Transport (this is the brief's "(vanilla)" note in plain words). All easy to delete if the owner prefers the briefed labels only.
5. **Placeholder label on slides 11 and 20 as well as 1 and 3.** The brief says "wherever it appears (slides 1 and 3)". The small avatar in step 4 of slide 11 and the avatar on slide 20 also carry "Placeholder avatar. Her look is undecided (OQ15)." No avatar is used on slides 4 to 10.
6. **The avatar** is a featureless round head, a headset and orange shoulders (no face, no hair, no body detail). On slide 4 the two speakers are abstract rings, not characters.
7. **Slide 4:** the Background chip sits on its own row above the left bubble (not literally beside it) so nothing overlaps.
8. **Slide 5:** each card shows its label with a strike-through and a red cross badge; small generic icons (chat, magnifier, calculator, semaphore, gear, engine) sit on the left. The icons are generic, not the mod's models.
9. **Slide 7:** the brief gives no lesson names (OQ17), so the tiles carry only a play icon or a padlock. Open and locked are shown by the words "Open" and "Locked" and the padlock shape as well as colour.
10. **Slide 14:** the dotted question arrow is double-headed, so it implies no direction of history (no "became" story). Only the briefed hint label is used.
11. **Slide 16:** the five row icons are plain geometric shapes (circle, square, triangle, diamond, hexagon) chosen so they do not suggest any subject.
12. **Slide 17:** three unlabelled grey tab stubs sit beside the Transport tab to show a strip of tabs. They name no other vanilla tab.
13. **Slide 21:** all four steps say "planned" in words and have dashed outlines. No technical detail.
14. **Type size:** `OUTLINE.md` lists 12 pt for the slide number and inline chips; `MULTI_DECK_RULES.md` says nothing below 14 pt, so slide numbers and inline chips are 14 pt (as in Deck 3). The caption bar is 6.3 to 7.1 in tall (as in Deck 3), not the 0.6 in of `OUTLINE.md`, so two-line captions never touch the edge.
15. **Status chip position** matches Deck 3: top right at (11.03, 0.58), 1.7 x 0.4 in.

## Design checks

- Read "Railway Assistant & Animated Tutorial System" (Confirmed / Agreed, Proposed, OQ15 to OQ18), "Build menu UX" (OQ19), and the Proposed reaction notes under "Liveries and cameo content" and "VIP / Prestige locomotive framework" on `master`. No difference from the brief was found.
- Agreed slides carry only Agreed content (character and scope, what she is not, library, table, lesson style, library look, original jingle). The first-unlock takeover, older-FICSIT hint, extra lessons, list layout, build menu tab and groups, and reactions are all Proposed with a Proposed chip. Slides 9, 10, 11, 14, 16 and 17 carry their own inline Undecided chips. No design status was changed; no Open Question is answered; no Superseded idea appears.
- The guide is "she" and "her" throughout. No dialogue is written for her. No third-party sound or product is named. The "used to be good, later corrupted" idea is not stated (slide 14 says it is not a story).
- No numbers, names, prices, dates or other facts beyond the brief.

## Slides to look at first in PowerPoint

9 (lesson window: ring, bubble tail, control bar and chip), 17 (tab strip: tab labels and widths), 8 (miniature table: label pills), 3 and 11 (avatar and its label), 10 (older-style screen), 5 (strike-through and the corner cross badges).
