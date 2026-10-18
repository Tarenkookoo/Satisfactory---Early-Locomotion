# MULTI-DECK RULES — follow-on explainer decks (Deck 2 and Deck 3)

Read this first, then the `DECK_BRIEF.md` in your deck's folder. These are follow-on decks to "Early Locomotion, Explained" (Deck 1). Deck 1 is being built by another cloud session on its own branch (`claude-presents-build-opus`). Do not touch Deck 1's files or branches.

## 1. Who you are and what you do

You are a cloud Claude Code session. You see only what is on GitHub (repo `Tarenkookoo/Satisfactory---Early-Locomotion`). Your job: **build one .pptx exactly as the deck brief specifies, check it, and push it to your own build branch.** Do not redesign the deck. Do not research the design again. Do not add facts.

- Check out the branch **`claude-presents-decks`** (it holds both deck briefs and Deck 1's research and images). If it does not exist, stop and report that.
- Deck 2 (signals) pushes to **`claude-presents-build-deck2`**. Deck 3 (servicing) pushes to **`claude-presents-build-deck3`**. Create your branch from `claude-presents-decks`. **Never push to `master`, `claude-presents`, `claude-presents-decks` or any other branch.** Never force-push. Do not open a pull request.
- Add files only inside your deck's folder (`Reporting/Claude Presents/Deck2_Signals/` or `Deck3_Servicing/`). Do not edit any existing file.

## 2. What to read, in order

1. This file.
2. Your `DECK_BRIEF.md` (slide table: exact captions, visuals, tags, images). **This is your build spec.**
3. `Reporting/Claude Presents/OUTLINE.md`: only the "Style tokens" and "Rules for every slide" sections (colours, type scale, tag chips). They apply to your deck unchanged.
4. `Reporting/Claude Presents/RESEARCH_NOTES.md`: the diagram specs your brief names (SIG-28 to SIG-31, SPEC-A to SPEC-I, "Reusable objects") and the source notes.
5. `Reporting/Claude Presents/ASSET_MANIFEST.md`: image paths (use the **bundle copies** under `Reporting/Claude Presents/images/` only), alt text, credit lines.
6. `Reporting/Claude Presents/STAGE2_CLOUD_BRIEF.md`: sections 4 to 6 (hard limits, tooling, method, easy-to-get-wrong notes) apply to you in full, with the changes in section 4 below.
7. `Design/GAME_DESIGN.md` **on `master`** only if you doubt a status tag. Note: the file on `master` may be slightly older than the owner's working copy. If it differs from your brief, follow the brief and record the difference in your build notes.
8. `Reporting/PUBLIC_PRESENTATION_BRIEF_2026-10-18.md` on `master`: use it only to check current-position claims (the "Where this stands" slide).

## 3. Rules that still apply (from the repo's `CLAUDE.md`)

- The "CEO holiday pause" and "first-session rule" in `CLAUDE.md` do not apply to this task: the owner authorised these decks explicitly on 18 October 2026. The rest of `CLAUDE.md` applies.
- British English. Plain, short sentences. Never invent facts, numbers or APIs. Use only the brief, the research notes and the design file.
- Do not change a design status. Every **Proposed** item keeps a visible Proposed chip. Playtest numbers stay marked **Provisional**. **Superseded** ideas never appear. **Undecided** topics stay undecided: show them as questions, never choose.
- Do not edit `.uasset`, `.blend` or other binary project assets. The only binary you create is the `.pptx`.
- No commits to `master`. No history rewriting. Commit small and often to your own branch.

## 4. Changes to the Deck 1 build rules

- **Slide count** is the number in your brief (not 42). **Slide numbers** shown on slides are your own deck's numbers.
- **Status chips** go top right on every slide except the first, second and last (credits).
- **Word limit:** 25 words or fewer per slide (caption plus labels). Exempt: slide 2 and the credits slide. Never exceed 45 on any other slide.
- **Type size:** caption 20 pt; diagram labels 14 pt or more; credit lines 10 pt; the credits table 11 pt. Nothing else below 14 pt.
- **Credits slide:** the final slide lists every image used in your deck with its author, licence and a hyperlinked source link, taken from the "Credit text" table in `ASSET_MANIFEST.md`. Include the note "CC BY-SA photos are shown unmodified except for resizing." The mod renders carry "Early Locomotion project (test model, not final art)."
- **Renders R03 and R04** (semaphore): wherever they appear, add under each "Blender model, not yet in the game."
- **Deck 1 slide references:** your brief names Deck 1 diagram specs (SIG-28 and so on). Rebuild them natively in your own deck. You cannot copy slides from Deck 1.
- **Notes file:** write `BUILD_NOTES.md` in your deck's folder: what you built, checks run, deviations, anything for the owner. If you are cut off, put the exact resume point (slide number) at the top and push your last commit.
- **Build scripts:** keep them in `<your deck folder>/build/`. You may write your own shape library (the one Deck 1's session is writing is not available to you).
- **Output file:** `<your deck folder>/<name given in your brief>.pptx`. Embed images from the bundle only; keep aspect ratio (crop, never stretch).
- **No speaker notes, no transitions, no animations.** Alt text on every picture and diagram group. Reading order: title, chip, visual, caption. Language en-GB. Set document title and author (author: "Claude (Early Locomotion project)").

## 5. Check, then report

After each chunk of about ten slides: save, render to PNG (LibreOffice then `pdftoppm -r 80`), look at every slide of the chunk, fix overflow, overlaps, tiny text, low contrast, missing chips, stretched pictures. Run a script that prints each slide's word count and smallest font size. Commit and push the chunk.

Final message, in plain language: complete or not (slide count), branch and commit, file size, what you checked, what you could not check (you cannot open real PowerPoint), deviations from the brief, and which slides the owner should look at first. Then the handoff block in the format `CLAUDE.md` gives: header `MANAGER HANDOFF - Claude Code - EL Architecture & Research - DD/MM/YY - HH:MM`, one fenced code block, fields from `Development/SPECIALIST_DELEGATION.md#required-handoff`.

## 6. Photographs

The photographs are third-party Creative Commons works (CC BY and CC BY-SA). The owner approved pushing them to GitHub for these decks on 18 October 2026. Keep the finished decks on their build branches only. Do not copy the images anywhere else and do not publish the decks.
