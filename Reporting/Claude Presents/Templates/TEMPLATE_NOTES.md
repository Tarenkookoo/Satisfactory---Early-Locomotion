# Template notes: build record for the Early Locomotion house style kit (v001)

Built on 22 October 2026 on branch `claude-presents-templates` (created from `claude-presents-complete`). Read with `TEMPLATE_GUIDE.md`. Every file is new and inside `Reporting/Claude Presents/Templates/`; no existing deck, brief or file on any branch was edited.

## 1. What was built

| Deliverable | File | Size | Notes |
|---|---|---|---|
| A | `EL_Claude_Template_v001.pptx` | 32 KB | Theme, master, 13 custom layouts, **no slides**. |
| B | `EL_Claude_Template_v001.potx` | 32 KB | Identical to A in every part except `[Content_Types].xml`, where the main part type is rewritten to `...presentationml.template.main+xml` (verified member by member). |
| C | `EL_Claude_Template_Patterns_v001.pptx` | 63 KB | 19 slides: 13 (one per layout; the workhorse example is the four-step flow) plus 6 extra workhorse slides: loop with callout, test value on a gauge, open question, plain fact, chips-and-pills reference, diagram-parts gallery. |
| D | `kit/el_kit.py`, `kit/build_template.py`, `kit/check_template.py` | | Plus three supporting files: `kit/layouts.py` (builds theme, master, layouts), `kit/patterns.py` (builds C), `kit/render.sh`. |
| E | `TEMPLATE_GUIDE.md` | | Tokens, layouts, slide rules, chips and pills, polish, Python build, checks, gotchas. |
| F | `TEMPLATE_NOTES.md` | | This file. |

The template: charcoal master background `#1E2126`; theme colours Dark 1 `#1E2126`, Light 1 `#F2F2F2`, Dark 2 `#2B2F36`, Light 2 `#A9B0B8`, Accent 1 to 6 orange, green, blue, purple, amber, red, hyperlink `#8FC7FF`, followed `#C9B2F5`; Arial as theme heading and body font; text styles with a 14 pt floor (title 36 pt bold, body 20/18/16/14); the slide master maps Background 1 to Dark 1 so shapes and text default to light-on-charcoal. The 13 layouts: Cover; Chapter divider; Title + visual + caption; Picture + caption + credit line; Two-panel compare; Table; Card grid (4); Card grid (8); Horizontal timeline; Key-facts tiles; Status legend; Credits / sources table; Closing / what next. All 11 python-pptx default layouts were removed. Placeholders: title, status chip, caption bar, picture, table, body/notes/cards/stops/tiles, credit line, slide number (idx map in `kit/layouts.py`). Layouts carry no transitions, animations or notes.

The five status chips are drawn exactly as in the explainer decks (1.7 x 0.4 in at (11.03, 0.58), 14 pt bold upper case; Undecided outline only). The four report workflow pills (Complete, In progress, Blocked, Planned) are open outline pills with a marker shape and are labelled in the guide as report workflow states, not design statuses.

The shape library `kit/el_kit.py` merges the Deck 3, Deck 5 and Deck 7 libraries (read from their build branches with `git show`; none of those branches was checked out): primitives, chips and inline chips, caption bar, cover-fit pictures with credit line, tables, grouped diagrams with alt text, text measuring, theme and master XML, timeline, cards, tiles, plus the template-aware slide API (`add_slide`, `set_status`, `put`, `fill_picture`, `fill_table`, `finish`, `clone_shape`, `clear_timing`). The locomotive and station silhouettes of the Deck 5 library were deliberately **not** carried over (project-specific); only a plain box wagon and a rail strip remain, as neutral examples.

## 2. Checks run

Tools: LibreOffice 24.2.7.2, pdftoppm 24.02.0, Python 3.13, python-pptx 1.0.2, Pillow 12.3, lxml 6.1.

1. **`check_template.py` passes on A, B and C** (B: package-level checks only, because python-pptx refuses a `.potx`). Zero errors, zero warnings on A and C. C has 19 slides; every slide is at or under 25 words (largest 24); smallest fonts: 14 pt everywhere, 10 pt on the picture credit line, 11 pt in the credits table.
2. **The checker was tested by breaking it.** Eleven planted defects, each in a copy of a good deck: font below 14 pt, group without alt text, empty placeholder, caption out of reading order, a `p:transition`, speaker notes, `en-US` language, `a:ln` children in the wrong order, text overflowing its box, a stretched picture, 55 words on a slide. All eleven were reported by the intended check (confirmed after finishing each slide so reading order could not mask the others). A transition passes only with `--polished`.
3. **Schema validation.** With `--xsd` the checker validated A, C and the polished C against the ISO/IEC 29500-4:2016 Transitional schemas (`pml.xsd`, `dml-main.xsd` and imports): zero schema errors on presentation, master, 13 layouts, 19 slides and theme. A planted `<a:bogus/>` and an unknown attribute were reported, so the validator is live. The schema files are a third-party copy downloaded to a scratch folder from a public GitHub repository (`davila7/claude-code-templates`, folder `.../pptx/ooxml/schemas/ISO-IEC29500-4_2016/`). They are **not** committed.
4. **LibreOffice renders, every slide looked at.** The 13-slide layout preview (every placeholder filled), all 19 slides of C at 80 dpi, the 5-slide guide example, and a picture test. Defects found and fixed this way:
   - The chip placeholder's dashed outline in the layout showed through filled chips (and would have been inherited by pictures): outlines removed from the chip, picture and table placeholders.
   - **A stray "STATUS" appeared on slides without a chip and garbled the Undecided chip.** Isolated by experiment: LibreOffice draws a layout text placeholder's prompt onto slides when that placeholder has its own shape geometry. Fixed by taking the geometry out of the layout and writing the rounded chip shape on the slide in `set_status`.
   - Chapter divider: the label placeholder preceded the title in reading order; swapped.
   - Pattern slides: wagons too small and the callout leader pointing at nothing (rebuilt larger and re-aimed), three slides sitting high (centred), credits note floating far from a two-row table (five rows).
5. **Pictures.** `fill_picture` tested in LibreOffice with synthetic grid images (not photographs): a 16:9 and a 9:16 image both cropped to fit the 8.0 x 4.5 in placeholder, not stretched, credit line directly beneath. The checker verifies visible aspect ratio against the box.
6. **`tools/polish.py`** run on C: 19 slides, 13 animated shapes; the output passes `check_template.py --polished` and schema validation. Only non-placeholder shapes animate (diagram groups, picture box); title, chip, caption, notes and number stay put, as the tool's rules say.
7. **Copy helpers.** `clone_shape` verified to strip a planted `a16:creationId` and `p:custDataLst` and to give unique ids; `clear_timing` verified by the checker.
8. **The guide's Python examples were run verbatim** (only the output path and image path substituted) and their output passed the checker.
9. **Zip integrity, content types, relationship targets, `r:id` resolution, unique shape ids and XML child order** for every part of A, B and C (part of the checker). `pyflakes` is clean on the kit.
10. LibreOffice opens A and B (`--convert-to odp` succeeded for both).

## 3. What could not be checked

I cannot open real PowerPoint. Everything above is LibreOffice, python-pptx, lxml and the XSDs. **Not verified:**

- That A, B and C open in PowerPoint **without a repair prompt**. XSD validity and child-order checks make it likely but are not proof.
- That the `.potx` opens in PowerPoint as a new untitled presentation (checked: content type, zip, LibreOffice opens it).
- How PowerPoint draws the layouts and the New Slide gallery thumbnails; that the layouts behave when you switch a slide from one layout to another.
- Arial in PowerPoint against Liberation Sans in LibreOffice. The metrics match, so line breaks should too, but no line was compared.
- The status-chip editing experience in PowerPoint: the chip placeholder takes the word but not the colour (colouring is done by `set_status` or by copying a chip). A slide made by hand in PowerPoint gets a plain text chip until formatted.
- Slide numbers on slides made in PowerPoint (they need Insert, Slide Number, Apply to All; the kit adds them in Python).
- A real photograph in the picture placeholder in PowerPoint (only synthetic images, in LibreOffice).
- Playback of `polish.py` animations and transitions; PowerPoint's Accessibility Checker; screen-reader reading order; Keynote, Google Slides, PowerPoint for Mac, phone viewers.
- Hyperlink colour (set in the theme; LibreOffice drew the link light blue).

## 4. Deviations and decisions

1. **Extra kit files.** The brief named three kit files; there are six (`layouts.py`, `patterns.py`, `render.sh` added) so the library, the layouts and the examples each stay readable. `build_template.py` still builds A, B and C. The checker also gained an optional `--xsd` mode and a `--polished` flag.
2. **A has no slides.** A real template; the Patterns deck is the filled version. A has no slides to render, so the visual checks used a throwaway preview deck (one slide per layout) and C.
3. **Panels are layout decoration; placeholders carry only text.** Caption bar, cards, tiles, notes panel, legend rows, track motifs and rules are shapes on the layout behind transparent placeholders, so a slide holds only what you type. Consequence: they change in Slide Master view, not on slides.
4. **The Status legend's five chips and meanings are static text on the layout** (wording from `MULTI_DECK_RULES_ADDENDUM.md`: Decided. / Suggested, not confirmed. / A test number that may change. / Still an open question. / A real-world fact.). Every legend slide is identical; changing the words means editing the layout.
5. **Status chip is a text placeholder** (idx 13), recoloured per status by the kit. Its rounded shape is written on the slide, not the layout (LibreOffice prompt-ghost issue above).
6. **Slide number is a real field placeholder** added to each slide by `finish()` (python-pptx never copies it). Cover and Closing have no number; Cover, Chapter, Legend, Credits and Closing have no chip.
7. **`polish.py` treats every placeholder as static**, so the caption bar does not fade in with the diagram, as it did in the nine decks (where the caption was a loose shape). Slides built only from placeholders get the transition and no builds. I did not edit `polish.py` (rule: do not edit existing files); if the owner wants captions to fade in, that is a one-line change to `is_static` there.
8. **Autofit off everywhere** (`noAutofit`) so PowerPoint cannot shrink text below the 14 pt floor silently. The checker estimates overflow instead.
9. **Master background is a literal `srgbClr 1E2126`** (as the brief says), not a theme reference; Dark 1 carries the same value.
10. **Settled values used where OUTLINE.md differs:** chip 1.7 x 0.4 at (11.03, 0.58); caption bar (0.6, 6.3) 12.13 x 0.8 at 20 pt; slide numbers and inline chips 14 pt; credit lines 10 pt; credits tables 11 pt; title box (0.6, 0.4), as in the finished decks.
11. **Word budget** counts caption, diagram labels, inline chips and table cells, not titles, status chips, numbers or credit lines; the Status legend, Credits, Cover, Chapter and Closing are exempt. Same convention as the Deck 5 audit.
12. **Commit trailer** uses an ASCII `@` (`noreply@anthropic.com`), not the full-width `＠` that appeared in the brief, so Git and GitHub parse it as an address. A `Claude-Session` line follows it, as the session's attribution rule requires.
13. **The report workflow pills** are an addition to the five chips and are kept visually apart (outline, marker shape, sentence case). Their colours (green, amber, red, steel) are deliberately not the Proposed, Provisional or Undecided colours.
14. **`docProps/app.xml`** was rewritten minimal ("Early Locomotion kit (python-pptx)"), and the default template's Mac printer-settings part, blank thumbnail and `type="screen4x3"` size tag were removed.

## 5. For the local review in PowerPoint

1. Open A, B (File, New, Personal) and C. Any repair prompt: note which part and send it back; `check_template.py --xsd` should reproduce it if it is a schema issue.
2. New Slide gallery: all 13 layouts present, named as in the guide, none of the Office defaults.
3. Add a slide from each layout; type into every placeholder; confirm 36 pt titles, 20 pt captions, the status chip placeholder, and that nothing shrinks.
4. Insert a real picture into the picture placeholder; check the crop, rounded corners and that the credit line sits under it.
5. Insert Slide Number, Apply to All; confirm 14 pt muted bottom right.
6. Selection Pane on a kit slide: Title should be the bottom item (screen readers read bottom to top), Slide number the top.
7. Run the Accessibility Checker on C; the slides use groups with alt text and a table with alt text.
8. Apply `tools/polish.py` to a copy of C and play it in Slide Show.
9. Decide whether captions should fade in (deviation 7) and whether the Status legend wording belongs on the layout (deviation 4).

## 6. Push status

Commits `8330430` and `79a1e4e` were pushed to `origin/claude-presents-templates` with ordinary pushes; no other branch was touched and nothing was force-pushed. The final commit (this guide and these notes, plus lint tidy) is pushed the same way; its status is stated in the final message. If a push were refused, every commit stays local on `claude-presents-templates`.
