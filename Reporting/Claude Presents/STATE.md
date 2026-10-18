# STATE — Early Locomotion explainer deck, Stage 1

**Status: COMPLETE.** Stage 1 (read, research, outline) finished on 18 October 2026. No .pptx was built. Nothing outside `Reporting/Claude Presents/` was written (scratch files went to the session scratchpad, outside the repo). **No git changes were made** (read-only `git ls-files` and `git status` only). No sub-agents or other sessions were started. Nothing was scheduled.

## What is in this folder
| File | Purpose |
|---|---|
| `OUTLINE.md` | Style tokens, narrative arc, 42-slide table (caption, visual spec, status tag, design reference, image slot) |
| `RESEARCH_NOTES.md` | Findings with source URLs and verified/unverified markers; full signalling diagram spec (slides 28 to 31); other diagram specs SPEC-A to SPEC-I |
| `ASSET_MANIFEST.md` | 19 photographs and 5 mod renders: paths, alt text, credit and licence as recorded, slide map, exclusions |
| `STAGE2_CLOUD_BRIEF.md` | Self-contained brief for the cloud build session |
| `images/` | 24 web-sized copies of the images used (about 5 MB), needed because the originals are not on GitHub |

## Decisions carried in (do not re-ask)
- Agreed and Proposed content included; every Proposed item has a visible Proposed chip; Playtest numbers shown as Provisional or left out; Superseded never included; Open Questions stay "undecided"; no design status changed.
- Primer slides (what Satisfactory is, how steam railways work, glossary), one plain "where we are" slide, no probe detail.
- Style: dark charcoal with orange accent, Arial (tokens in OUTLINE.md). British English.
- CEO holiday pause lifted for this presentation task only (user instruction, 18 October 2026). The cloud brief tells Stage 2 so, because `CLAUDE.md` in the repo still states the pause.

## Usage readings (`get_usage`)
- Start: 5-hour 0%, weekly 40%.
- After design reading: 5-hour 3%. After research and image review: 8%, weekly 41%.
- Before writing outputs: 11%, weekly 41%. At finish: **5-hour 18%, weekly 42%**. Extra usage: not enabled, no spend recorded at any reading. The 85% guard never triggered.

## Conflicts and open items for the coordinator and owner
1. **Images are untracked.** Only seven Jinty photos under `Asset References/` are in git; no `Blender/` renders are. The coordinator must **commit and push `Reporting/Claude Presents/` (including `images/`) to `claude-presents`** before Stage 2 starts. Stage 2 uses the bundle copies only.
2. **Publishing third-party photos is the owner's call.** The repo is public. Photos are CC BY or CC BY-SA. Several infrastructure source manifests say "NOT authorised to publish in this task" (listed in `ASSET_MANIFEST.md`, column "Repo note"). Licences allow redistribution with credit; owner approval is still needed. CC BY-SA (share-alike) photos are used unmodified apart from resizing and credited on slides 41 and 42. CC BY was preferred wherever a choice existed.
3. **Small-class reference trap.** The design's Small reference is the LMS Fowler Dock Tank (none preserved). The repo has only Jinty photos. Slide 19 uses a Jinty and says so.
4. **No conflict** between `Design/GAME_DESIGN.md` and `Design/Early Locomotion Design Reference.docx` (220 of 220 paragraphs matched; four trivial formatting lines differ). The Feature Catalogue is derived and consistent, but lines 338 to 372 of its extracted text were not read.
5. **Mod renders are early work.** R01 is a yellow "visual probe" test model, not a final or Small-class design. R02 and R05 are high-detail visual development, not Unreal-tested or production-ready. Captions say "early test model, not final art".
6. **Excluded images:** the four AI-generated Semaphore sheets, the missing `P08_Loose_Chair_CC0.jpg`, very large originals, and the Black 5 previews.
7. **Binary-asset rule.** Images were opened read-only to choose them, and copied (some resized) into `images/`. No original was changed. No `.blend` file was opened.
8. **Wording fixes made on purpose:** slide 29 says "On real railways" for the broken-wire fail-safe (the mod's failure behaviour is undecided, OQ03); slide 39 leaves out technical test detail; slide 19 labels the Jinty as a related engine.

## Unverified or caveated facts
- Satisfactory background facts (release dates, Tier 6 monorail unlock) come from store listings and `satisfactory.wiki.gg`, summary level only.
- Flanged-wheel explanation: general knowledge, not fetched. The block-instrument three states and bell codes come from a search summary of mainline sources. Coaling facts are search-summary level (the Water crane page was read in full).
- Lever colours are an example from one heritage frame (Bluebell), not a universal scheme; the deck labels them "example colours".
- Deck-format research (Mayer, Duarte) is from summaries; no source was found giving an ideal slide count for a read-alone explainer.
- Everything numerical in the deck is a Playtest Target and is marked Provisional.

## What Stage 2 needs
1. The `claude-presents` branch with this folder and `images/` pushed.
2. `STAGE2_CLOUD_BRIEF.md` as its first instruction, then `OUTLINE.md`, `RESEARCH_NOTES.md` and `ASSET_MANIFEST.md`.
3. Owner decision on publishing the third-party photos (item 2 above) before the deck leaves the build branch.
