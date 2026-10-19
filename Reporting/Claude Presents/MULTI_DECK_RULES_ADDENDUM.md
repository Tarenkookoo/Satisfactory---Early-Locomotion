# MULTI-DECK RULES ADDENDUM — Decks 4 to 9 (19 October 2026)

Read `MULTI_DECK_RULES.md` first, then this file, then your `DECK_BRIEF.md`. This addendum changes or adds to the rules for Decks 4 to 9 only. Decks 1 to 3 are finished and on their own branches: do not touch them.

## 1. Authorisation and branches

- The owner (CEO) instructed these six decks in chat on 19 October 2026. The "CEO holiday pause" and "first-session rule" in `CLAUDE.md` do not apply to this task. The rest of `CLAUDE.md` does.
- Check out **`claude-presents-decks2`**. It holds every brief and everything on `claude-presents-decks`. Create your build branch from it. Your brief names the branch and the folder.
- Push only to your own build branch. Never push to `master`, `claude-presents`, `claude-presents-decks`, `claude-presents-decks2` or any other deck's branch. Never force-push. Do not open a pull request. Add files only inside your deck's folder.

| Deck | Build branch | Folder |
|---|---|---|
| 4 | `claude-presents-build-deck4` | `Deck4_Monorail/` |
| 5 | `claude-presents-build-deck5` | `Deck5_Regions_Numbers/` |
| 6 | `claude-presents-build-deck6` | `Deck6_Assistant/` |
| 7 | `claude-presents-build-deck7` | `Deck7_AfterLaunch_Packs/` |
| 8 | `claude-presents-build-deck8` | `Deck8_AfterLaunch_LateSteam/` |
| 9 | `claude-presents-build-deck9` | `Deck9_Balance/` |

## 2. Lessons from the owner's review of Decks 1 to 3 in real PowerPoint

These defects were found. Avoid every one.

1. **Leader lines and arrows must never cross label text.** Start a leader at the edge of its label box and point away from the label. If the target sits under or inside the label box, move or resize the label (two short lines in a narrow box is fine).
2. **Inline chips must not overlap bars, lines or text.** Give a chip its own row, or put it where nothing else is.
3. **Tag every statement at its own status.** The slide chip (top right) describes the slide's main idea. Any statement the brief tags Proposed, Provisional or Undecided carries its own inline chip, even on an Agreed slide. Never leave such a statement untagged.
4. **Use the briefed labels word for word.** If one cannot fit at 14 pt, shorten it and list every shortened label in `BUILD_NOTES.md`.
5. **Check every slide at full size** after the last render: text touching an edge, chips colliding, a caption wrapping so close to its panel edge that it looks cramped.
6. **Diagram labels never go below 14 pt.** Credit lines are 10 pt, the credits table 11 pt.

## 3. Content rules that apply to every deck here

- The briefs give exact captions in quotation marks. Use them word for word. Text quoted in the visual column is a diagram label and also goes on the slide.
- **No numbers, names, prices, dates or facts beyond the brief.** In particular: no pack price, no locomotive stock numbers, no named famous engines, no dates for the "Golden Era". Where the brief says "example only", label it "Example only".
- **Superseded ideas never appear.** Undecided topics appear only as questions.
- "Where this stands" slides use only the states "Under way" and "Planned". No technical test detail, and nothing implying a system already works.
- Alt text on every picture and diagram group. No speaker notes, transitions or animations. Language en-GB. Title and author set as in `MULTI_DECK_RULES.md`.
- Slide 2 of every deck is the legend (same as Decks 2 and 3: five real chips, each with its meaning: Agreed "Decided.", Proposed "Suggested, not confirmed.", Provisional "A test number that may change.", Undecided "Still an open question.", Background "A real-world fact."; caption "Every idea carries a tag in the top-right corner."). Status chips go top right on every slide except slides 1, 2 and the last.
- The last slide is "Image credits" (table, 11 pt) listing every image used in that deck with author, licence and a hyperlinked "Commons" link (credit text in `ASSET_MANIFEST.md`), plus "CC BY-SA photos are shown unmodified except for resizing." Mod renders read "Early Locomotion project (test model, not final art)." If your deck uses no photographs, the table lists only the renders used and the caption reads "This deck uses no photographs." If it uses no images at all, the slide shows that sentence alone.
- Images: bundle copies under `Reporting/Claude Presents/images/` only. No new downloads.
- Word limit: 25 words or fewer per slide (caption plus labels), except slide 2 and the credits slide. Never above 45.

## 4. Final message

Plain language: complete or not (slide count), branch and commit, file size, what you checked, what you could not check (you cannot open real PowerPoint), shortened labels and any deviation, and which slides the owner should open first. Then the handoff block as in `MULTI_DECK_RULES.md` section 5.
