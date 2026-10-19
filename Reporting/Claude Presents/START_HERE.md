# START HERE — building one explainer deck (Decks 4 to 9)

You were told to "follow START_HERE.md for Deck N". Find your row in the table at the bottom, then do the steps below. The owner authorised this work on 19 October 2026 (see `MULTI_DECK_RULES_ADDENDUM.md`).

## 1. Setup

- Fetch the repository, check out branch **`claude-presents-decks2`**, then create your build branch **`claude-presents-build-deckN`** from it (N is your deck number).
- Everything you need is under `Reporting/Claude Presents/`.

## 2. Read, in this order, before building

1. `MULTI_DECK_RULES.md`
2. `MULTI_DECK_RULES_ADDENDUM.md`
3. `OUTLINE.md` (style tokens)
4. `ASSET_MANIFEST.md` (image credits)
5. `RESEARCH_NOTES.md`
6. Your spec: `DeckN_.../DECK_BRIEF.md` (folder named in the table)
7. `Design/GAME_DESIGN.md` **on `master`**, only the sections your brief names

The brief's slide table is exact: use its titles, captions, tags and visuals as written.

## 3. Build

- Use python-pptx (install python-pptx and Pillow if missing). Draw every diagram with native shapes.
- Use only images from `Reporting/Claude Presents/images/`. Download nothing new.
- Build in the chunks the brief names. Check each chunk (render or audit) before moving on.
- Put the .pptx, `BUILD_NOTES.md` and the `build/` scripts in your deck's folder, with the file name the brief gives.

## 4. Hard rules

- British English. Never invent facts.
- Never change a design status: Proposed stays Proposed, Superseded never appears, Undecided appears only as questions.
- No price, no named famous engines.
- Do not modify any file outside your own deck folder.

## 5. Done means

- The .pptx, `BUILD_NOTES.md` and `build/` scripts are committed and pushed to **your build branch only**. Never push to `master` or any other branch. Never force-push.
- Your final message follows the format in the addendum and lists every deviation from the brief.

## Decks

| N | Deck | Slides | Folder | Build branch | Images | Extra rules |
|---|---|---|---|---|---|---|
| 4 | The Monorail Transition | 22 | `Deck4_Monorail/` | `claude-presents-build-deck4` | R01, R02 | None beyond the brief. |
| 5 | Regions, Running Numbers and Fleet Identity | 26 | `Deck5_Regions_Numbers/` | `claude-presents-build-deck5` | R01 | Every invented number plate is labelled "Example only". Never imply equal locomotive stats across regions. |
| 6 | Your Railway Guide: Lessons and the Build Menu | 23 | `Deck6_Assistant/` | `claude-presents-build-deck6` | none | No images. Draw the guide only as the native placeholder avatar with its placeholder label. Write no dialogue for her. Name no third-party sound or product. |
| 7 | After Launch, Part 1: Packs, Locomotives and History | 24 | `Deck7_AfterLaunch_Packs/` | `claude-presents-build-deck7` | P19 | The whole programme is Proposed and post-launch: say "could" where the brief does. No price, pack name, locomotive count or named historical engine. |
| 8 | After Launch, Part 2: Late Steam, Advanced Driving and Prestige | 25 | `Deck8_AfterLaunch_LateSteam/` | `claude-presents-build-deck8` | P12 | Post-launch. No price, named famous engine, engine count or formula. Explosions and permanent damage are not features. |
| 9 | How the Mod Is Balanced | 18 | `Deck9_Balance/` | `claude-presents-build-deck9` | R02 | Numbers are Playtest Targets and carry a Provisional chip. No locomotive speeds or per-class wagon counts. Never show 50 m, 100 m or "half the vanilla length". |
