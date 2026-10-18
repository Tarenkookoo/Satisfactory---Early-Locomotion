# STAGE 2 BRIEF — build the "Early Locomotion, Explained" .pptx

This brief is self-contained. You are a cloud Claude Code session. You can see only what is in the GitHub repo, so everything you need is in the files named below. Stage 1 (reading, research, outline) is finished. **Your job is to build the deck exactly as outlined, check it, and push it to a new branch.** Do not redesign the deck, and do not research the design again.

## 1. Where things are

- Repo: `Tarenkookoo/Satisfactory---Early-Locomotion`.
- Check out the branch **`claude-presents`** (the coordinator creates and pushes it before you start). If it does not exist, or `Reporting/Claude Presents/images/` is missing from it, stop and report that. Do not substitute other pictures.
- Push your work to a **new branch `claude-presents-build`** created from `claude-presents`. **Never push to `master`.** Never force-push. Do not open a pull request unless the coordinator asks.
- Deliverable: `Reporting/Claude Presents/Early_Locomotion_Explained.pptx`.
- You may also add, inside `Reporting/Claude Presents/` only: the build scripts (for example `build_deck.py` and a `build/` folder of helpers), the rendered preview PNGs of a few key slides if small (optional), and `STAGE2_BUILD_NOTES.md`. Touch nothing else in the repo. Do not edit any existing file.

## 2. Files to read, in this order

1. `Reporting/Claude Presents/STATE.md` — Stage 1 status, decisions, conflicts and open items.
2. `Reporting/Claude Presents/OUTLINE.md` — the style tokens, the narrative arc and the 42-slide table. **This is your build spec.** Quoted captions are exact.
3. `Reporting/Claude Presents/RESEARCH_NOTES.md` — read the last two parts in full: "FULL SIGNALLING DIAGRAM SPEC" (slides 28 to 31, the must-have diagram) and "OTHER DIAGRAM SPECS" (SPEC-A to SPEC-I). The earlier parts give source URLs and the verified/unverified markers.
4. `Reporting/Claude Presents/ASSET_MANIFEST.md` — every image, its bundle path under `Reporting/Claude Presents/images/`, alt text, credit line, licence and the slide it belongs to. Embed the **bundle copies only**.
5. Only if you doubt a fact or a status tag: `Design/GAME_DESIGN.md` (the authority). If OUTLINE.md and GAME_DESIGN.md ever disagree, follow GAME_DESIGN.md and record the difference in `STAGE2_BUILD_NOTES.md`.
6. Optional style reference: `Reporting/ACCEPTED_PRESENTATION_TEMPLATES.md` (Arial, restrained, native diagrams). The deck's own tokens are in OUTLINE.md and win.

## 3. Rules from the repo that still apply (read this before you start)

`CLAUDE.md` at the repo root contains a "CEO holiday pause" and a "first-session rule". **They do not apply to this task.** The owner lifted the pause for this presentation only (explicit instruction, 18 October 2026) and this task is not a first session. The rest of `CLAUDE.md` still applies:

- British English. Plain, short sentences.
- Never invent facts, numbers or APIs. Use only what OUTLINE.md and RESEARCH_NOTES.md say.
- Do not change any design status. Every **Proposed** item keeps its visible Proposed chip. Playtest numbers stay marked **Provisional**. **Superseded** ideas never appear. **Undecided** topics stay undecided: never choose.
- Do not edit `.uasset`, `.blend` or other binary project assets. The only binary you create is the `.pptx`.
- No commits to `master`. No history rewriting.
- End your final message with the completion report in the format `CLAUDE.md` gives: header `MANAGER HANDOFF - Claude Code - EL Architecture & Research - DD/MM/YY - HH:MM`, one fenced code block, using the fields from `Development/SPECIALIST_DELEGATION.md#required-handoff`. State plainly what you verified and what you did not.

## 4. What you are building

A **read-alone** deck: no presenter, **no speaker notes**, short captions, mostly diagrams and pictures. Reader: someone who knows nothing about Satisfactory, the mod, or steam railways. 42 slides, 16:9 (13.333 × 7.5 in), Arial, dark charcoal with orange accents.

Per slide: title, status chip (top right, except slides 1, 2, 41, 42), the visual, the exact caption from OUTLINE.md in the caption bar, a small credit line under any photograph, and the slide number.

### Hard limits
- **Words:** aim for 25 or fewer words in total on a slide (caption plus labels). Exempt: slides 2, 13, 32, 41, 42. Never exceed 45 on any other slide; if a slide would, shorten the labels, not the caption.
- **Type size:** caption and body text 18 pt or more (caption 20 pt). Diagram labels 14 pt or more. Only credit lines (10 pt) and the credit tables on slides 41 and 42 (11 pt) may be smaller.
- **Native shapes** for every diagram (rectangles, rounded rectangles, ovals, lines, connectors, freeforms). Pictures only where the table names an image slot. Group the parts of each reusable object so they are easy to move.
- **Contrast:** all text at least 4.5:1 against its background. Never use colour alone to show a state: write the state too.
- **Accessibility:** set alt text on every picture and every diagram group (`descr` on the shape's `cNvPr`). Use the "What it shows" text in ASSET_MANIFEST.md for photos and renders, and one plain sentence for diagrams. Put shapes in reading order (title, chip, visual, caption) because shape order is the reading order. Set the language to `en-GB` on all runs. Set the document title and author in the core properties.
- **No speaker notes** (do not create notes slides). **No transitions and no animations.**
- **Pictures:** keep aspect ratio (crop, never stretch). Round the corners by 0.08 in if easy; never add effects. Credit line directly under each photograph, 10 pt, from ASSET_MANIFEST.md. Never describe a photo of a real locomotive as the mod's model. R01 is an "early test model, not final art".
- **File size:** target well under 60 MB (about 10 MB is expected: the bundle images total about 5 MB). Do not re-compress the images further unless the file is over 40 MB.

## 5. Suggested tooling and method

1. Check what is installed (`python3 --version`, `pip list`, `which soffice libreoffice pdftoppm`). Prefer **python-pptx** (`pip install python-pptx`). `pptxgenjs` is an acceptable alternative. Use LibreOffice (`soffice --headless --convert-to pdf`) and `pdftoppm -r 80 -png` to render slides to images so you can inspect them. If rendering tools are missing, install them if you can (for example `apt-get install -y libreoffice-impress poppler-utils fonts-liberation`). LibreOffice will substitute Liberation Sans for Arial: it has the same metrics, so overflow checks stay valid.
2. **Write a small shape library first** (one module): `add_base(slide, section, title, chip, caption, n)`, `add_chip`, `add_picture_fit` (cover or contain, crop not stretch), `add_credit`, `rails(x, y, length)`, `sleepers`, `signal_post(x, y, state)` (stop or clear), `distant_arm`, `train(x, y, n_wagons)`, `block_band(x, y, w, state, label)`, `person_icon`, `lever_row`, `box_building`, `arrow`, `elbow_connector`, `dashed_connector`, `tank_gauge`, `bar_row`. The object sizes and colours are in RESEARCH_NOTES.md ("Reusable objects") and the style tokens in OUTLINE.md. Reuse them so the deck looks consistent.
3. **Build in chunks of about ten slides**, one script function per slide, in this order, and check each chunk before starting the next:
   - Chunk 1: slides 1 to 10 (welcome, primers, water).
   - Chunk 2: slides 11 to 20.
   - Chunk 3: slides 21 to 31 (give the signalling slides 28 to 31 the most care; they are the must-have diagram).
   - Chunk 4: slides 32 to 42.
4. **After each chunk:** save the .pptx, render it to PNGs, look at **every** slide image of that chunk, and fix: text overflow or clipping, overlapping shapes, labels that touch lines, tiny text, low contrast, stretched pictures, missing chips, misaligned columns. Run a script that lists every slide's word count and the smallest font size on it. Commit the chunk to `claude-presents-build` when it passes (small commits; this protects your work if the session is cut off).
5. When a diagram spec is unclear, make the simplest reasonable choice that follows the spec's intent and note it in `STAGE2_BUILD_NOTES.md`. Do not ask the owner; do not add new facts.
6. Final pass: open the whole deck as a contact sheet (all 42 renders), check the story reads in order, check every Proposed item has its chip, check slides 41 and 42 list all 24 images with the right credits and links, and check there are no empty placeholders left on any slide (delete unused layout placeholders).

## 6. Per-slide notes that are easy to get wrong

- **Slide 19:** the photo is a Jinty. The note under it says so and says the design's reference (the Dock Tank) has no surviving example. Do not caption it as the Small locomotive.
- **Slide 29:** the fail-safe text must begin "On real railways". The mod's behaviour when a signal fails is undecided. The corner chip reads "Arm style: undecided".
- **Slide 32:** all four numbers are provisional; each tile carries a Provisional chip.
- **Slide 35 and SPEC-H:** the upgrade hologram, the warning and the mixed network are Proposed; the "steam trains cannot use converted track" rule and the in-place upgrade are Agreed. Keep both chips visible.
- **Slide 39:** plain language only. No technical test detail. Only "Under way" and "Planned" states.
- **Slide 40:** open questions are shown as questions. Do not offer answers.
- **Slides 1 and 3:** R01 is an early test model. Its credit line must say so.
- Tag counts to check against OUTLINE.md: Agreed 23, Proposed 2, Provisional 4, Undecided 1, Background 8, no chip 4.

## 7. Push and report

```
git fetch origin
git checkout claude-presents
git checkout -b claude-presents-build
# ... build, check, commit in chunks ...
git add "Reporting/Claude Presents/Early_Locomotion_Explained.pptx" "Reporting/Claude Presents/STAGE2_BUILD_NOTES.md" "Reporting/Claude Presents/build"
git commit -m "Build Early Locomotion explainer deck (Stage 2)"
git push -u origin claude-presents-build
```

Add only files inside `Reporting/Claude Presents/`. Check `git status` first and leave anything else alone.

Your final message should say, in plain language: whether the deck is complete (42 slides), the branch and commit, the file size, what you checked (render and inspect, word counts, font sizes, alt text, no notes) and what you could not check (for example, you cannot open it in real PowerPoint), any deviation from OUTLINE.md and why, and any slide you think the owner should look at first. Then the handoff block (section 3).

## 8. Owner decisions to pass back (do not decide these yourself)

- **Publishing the photographs.** The repo is public and the photographs are third-party Creative Commons works (CC BY and CC BY-SA). Several source manifests say "NOT authorised to publish in this task". The licences allow redistribution with credit, but the owner must approve before the images (and the deck containing them) go anywhere public. Pushing to `claude-presents-build` is fine; do not publish the deck elsewhere.
- CC BY-SA is share-alike. The images are used unmodified apart from resizing, and slides 41 and 42 carry the credit and licence for each. If the owner prefers, the BY-SA photos can be swapped for CC BY ones later.

## 9. Usage and limits

The owner is on the Pro plan with purchased credits available as headroom, and wants the plan allowance used first and the credits left alone if possible. Work in the chunks above, commit at the end of each chunk, and keep renders small (80 dpi, and look only at the slides you changed). If you hit a usage limit or the session is cut off, make sure the last commit on `claude-presents-build` is pushed and write the exact resume point (chunk and slide number) at the top of `STAGE2_BUILD_NOTES.md`.

## 10. Coordinator addendum (18 October 2026, added after Stage 1)

- GPT-OP has published `Reporting/PUBLIC_PRESENTATION_BRIEF_2026-10-18.md`, a dated, public-safe snapshot of the project's current position. Read it right after `STATE.md`. Use it **only** to check current-position claims (slide 39 and the status wording on slides 1, 3, 17 and 29). If it differs from `OUTLINE.md` on current status, follow the dated brief and record the difference in `STAGE2_BUILD_NOTES.md`. It adds no slides and is not a design authority: `Design/GAME_DESIGN.md` still wins on design status.
- **Caption fix, slide 29:** under each of the renders R03 and R04, add the credit line "Blender model, not yet in the game." (the semaphore model has Blender-side checks only, with no runtime implementation).
- **Photographs:** on 18 October the owner decided to push all 24 bundled images, each with its recorded credit and licence. GPT-OP's brief says third-party photography still needs separate review for its own scope. So keep the deck, with its images, on the build branch only. Do not copy the images elsewhere or publish the deck.
- The holiday-pause lift (section 3) is unchanged: it covers this one deck only.
