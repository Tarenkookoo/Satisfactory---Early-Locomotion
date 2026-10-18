# BUILD NOTES — Deck 2, "Signals and Signal Boxes, Explained"

**RESUME POINT (18/10/26, 23:25 UTC): the build is COMPLETE (27 of 27 slides, all three chunks checked).
The only open item is the push.** Every commit is on the local branch `claude-presents-build-deck2`, but
GitHub refused all writes from this cloud session (git push: HTTP 403 "Claude doesn't have GitHub access to
Tarenkookoo/Satisfactory---Early-Locomotion for your organization"; the GitHub connector's `create_branch`
also failed: 403 "Resource not accessible by integration"). The branch does not exist on GitHub yet.
Nothing was pushed anywhere else. To finish: connect or reconnect GitHub with write access for this repo
(https://claude.ai/connect-github, and install the Claude GitHub App on the repository if needed), then run
`git push -u origin claude-presents-build-deck2` from the session's checkout, or push the local branch from
any copy of this working tree. The .pptx is also in this folder, so nothing needs rebuilding.

## What was built

- `Signals_and_Signal_Boxes_Explained.pptx`: 27 slides, 16:9 (13.333 x 7.5 in), Arial, charcoal and orange,
  about 1.1 MB. Every diagram is native PowerPoint shapes (grouped, with alt text). Pictures: R03, R04, P13,
  P14, P15, P16 from the bundle in `Reporting/Claude Presents/images/`, cropped, never stretched.
- `build/`: `lib.py` (shape library), `chunk1.py`, `chunk2.py`, `chunk3.py` (one function per slide),
  `build_deck.py` (assembles the deck), `render.sh` (LibreOffice to PDF to PNG at 80 dpi), `check_deck.py`
  (word counts, smallest font, alt text, overflow estimate), `verify_brief.py` (captions, titles and tag
  counts against `DECK_BRIEF.md`; package checks). Rebuild with `python3 build/build_deck.py`.

## Checks run (all passed unless listed under "Deviations")

- Built in three chunks (1-9, 10-18, 19-27). After each chunk: rendered with LibreOffice and `pdftoppm -r 80`,
  looked at every slide image, fixed what showed up (see below), ran `check_deck.py`, committed.
- `verify_brief.py`: 27 slides; all 27 titles and all 27 captions match the brief's table exactly; tag counts
  match the brief (Agreed 8: slides 15, 16, 17, 19, 20, 22, 23, 24; Proposed 1: 21; Provisional 2: 18, 25;
  Undecided 1: 26; Background 12: 3 to 14; no chip 3: 1, 2, 27).
- No notes slides, no transitions, no animations, no leftover placeholders. Language `en-GB` on every run.
  Document title and author set (author "Claude (Early Locomotion project)"). Alt text on every picture,
  every diagram group, every chip and the credits table. Reading order: title, chip, visual, caption.
- Font sizes in the file: 54 (title slide), 36 (titles), 22, 20 (captions), 18, 16, 14 (smallest on any
  slide except credits), 11 (credits table), 10 (credit lines). Nothing else is below 14 pt.
- Pictures: aspect-ratio check passed for all pictures (crop only).
- Contrast: text colours were chosen against the tokens' backgrounds. Plain `#E5484D` red is only 4.1:1 on
  the charcoal, so red text uses a lighter red `#FF7A7E` (about 6:1), and red pills carry dark text.
  Never colour alone: STOP/CLEAR/Free/Occupied are written out wherever a state is shown.

## What I could not check

- I cannot open real PowerPoint. LibreOffice substitutes Liberation Sans for Arial (same metrics), so wrapping
  should match, but line breaks, group rotation of arms and table borders may differ slightly in PowerPoint.
  Please open the file once and page through it. No contrast tool was run; contrast is by calculation.
- Hyperlinks on slide 27 were set but not clicked (no network test).

## Word counts (caption plus labels; excluding title, status chips, slide number, credit lines)

Target 25, hard cap 45 (MULTI_DECK_RULES section 4). Slides at or under 25: 1 (20), 4 (21), 8 (23), 10 (24),
11 (16), 12 (22), 13 (21), 15 (17), 16 (20), 17 (23); slides 2 and 27 are exempt. Over 25 but under the cap:
3 (26), 5 (32), 6 (27), 7 (42), 9 (30), 19 (31), 20 (36), 21 (39), 22 (35), 23 (37), 24 (34), 25 (35);
at or just under the cap: 14 (45), 18 (44), 26 (44). The brief's quoted captions plus its quoted labels already
total more than 25 on most slides, so I kept every caption exact and trimmed labels only where the cap forced
it (slides 14, 18, 26). If you also count titles and credit lines, slides 7, 20 and 25 pass 45 (55, 57, 53).
My checker counts any text shape that is not the title, a plain tag chip, the slide number or a credit line.

## Deviations from the brief (all small; none changes a status or a decision)

Labels trimmed to hold the 45-word cap:
- **Slide 14:** block bands read "Free / Occupied / Free" (no "Block 1/2/3"); the neighbour box label is
  "Bell codes" (brief: "Bell codes: is the line clear?"; slide 13 carries the full question). No STOP/CLEAR
  words on the three signals (arm angle and lamp show the state; the four steps name it). The brief's mod
  footer and territory rectangle are left out, as the brief says.
- **Slide 18:** tiles read "Block: about 400-500 m", "Speed cap: about 60 km/h", "Signals per box: 6-8
  station, 12-16 dedicated", "Reach: about 1-1.5 km" (brief: "Block length ...", "Box reach ..."); ruler
  label "450 m"; footer "Final values: undecided (OQ03)." (brief: "Block lengths and speed caps: undecided
  (OQ03)."). All four tiles keep their own Provisional chip.
- **Slide 26:** question wording shortened: "Block lengths, speed caps" / "If a signal fails?" / "Which later
  signals first?" / "Measuring a box's reach" / "Which box wins an overlap?" / "Rod or wire look" / "Arm:
  rises or drops?" / "Who sets points near signals?". The OQ codes sit inside each card's outline Undecided
  chip ("UNDECIDED · OQ03"). Questions only; no answers. Card size 2.9 x 1.95 in (brief 2.9 x 1.5) for
  18 pt text. If you want the brief's exact question wording, say so and I will accept going over 45 on that slide.

Type-size floor (rules say nothing else below 14 pt, the Outline tokens say 12 pt):
- Status chips, inline chips and slide numbers are 14 pt; the main chip is 1.65 x 0.4 in at x 11.05 (token:
  1.5 in at x 11.2) so "BACKGROUND" stays on one line. Inline chips are 1.55 to 4.5 in wide and 0.32 to
  0.45 in high. The Outline's small section label is not used. No slide number on the title slide.

Sizes and positions:
- **Slide 9:** photo P14 is 4.0 x 4.7 in (brief 4.2 x 5.0) so the credit line fits above the caption bar.
- **Slide 21:** the mock panel is 5.6 x 4.4 in (brief 5.6 x 3.6) so six rows fit at 18 pt. Tag stays
  Proposed as the brief says; the box-screen contents are not labelled Agreed in the design file, and
  **you may upgrade the tag if you decide the screen contents are agreed.**
- **Slide 20:** the state labels ("STOP: arm flat", "CLEAR: arm raised") sit on the render, not under it;
  the 10 pt "Blender model, not yet in the game." line is directly under each picture. Same on slide 25.
- **Slide 27:** the two render rows say "Project render (no link)" in the link column (they are not on
  Commons).

Small additions (not in the brief):
- Slide 1: grey line "Early Locomotion: a mod for Satisfactory" above the title (the reader knows nothing
  about the mod). Slide 7: headings "Stop arm" and "Distant arm". Slide 8: "CLEAR" beside the intact
  panel's signal. Slides 5, 12, 15: STOP/CLEAR/state words beside signals. Slide 22: "Not to scale" (the
  research notes require it wherever a bar shape appears). Slide 25: a thin progress line above the four
  stage cards. Slide 16: station platforms drawn under the box icons.

Other notes:
- The slide 6 raised arm and the slide 7, 8 and 12 raised arms are examples of "clear" only; the deck does
  not choose whether the mod's arm rises or drops (slide 6 chip, slide 26 card).
- Slide 8's counterweight is drawn as the brief describes (a square hanging at the arm's foot). It is a
  schematic, not an engineering drawing.
- Hyperlink colours in the theme were set to a light blue so the "Commons" links read on the dark
  background. The unused default layouts were removed; the one remaining layout is "Title Only".
- Design source checked: `Design/GAME_DESIGN.md` on this branch ("Signalling", "Signal boxes", "Mechanical
  signal-box linkage visuals", "Track design", OQ03 and OQ04) and `Reporting/PUBLIC_PRESENTATION_BRIEF_
  2026-10-18.md` (manual operation) agree with the brief's tags. No difference found.

## Look at these slides first

5, 7, 8, 10 and 14 (the diagrams the brief singles out), then 24 (the hand-driving panel), 18 and 26 (trimmed
labels), 21 (Proposed tag), and 27 (open the "Commons" links).
