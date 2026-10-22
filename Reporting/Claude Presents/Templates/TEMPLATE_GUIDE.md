# Template guide: the Early Locomotion house style kit (v001)

Everything here is generic. It holds no project text, no real vehicle names, no prices and no third-party pictures. Paths are relative to `Reporting/Claude Presents/Templates/`.

| File | What it is |
|---|---|
| `EL_Claude_Template_v001.pptx` | The template: theme, master and 13 layouts. It has no slides. |
| `EL_Claude_Template_v001.potx` | The same file saved as a PowerPoint template (File, New, Personal). |
| `EL_Claude_Template_Patterns_v001.pptx` | 19 example slides, one per layout plus reference slides. Copy from it. |
| `kit/el_kit.py` | The shape and template library. |
| `kit/layouts.py` | Builds the theme, master and layouts. |
| `kit/patterns.py` | Builds the patterns deck. |
| `kit/build_template.py` | Rebuilds the three files above. |
| `kit/check_template.py` | The checker. |
| `kit/render.sh` | LibreOffice to PNG, for a quick look. |

---

## 1. Colour and type tokens

**Canvas** 13.333 x 7.5 in (16:9). **Font** Arial for everything (theme heading and body font). **Language** en-GB. **Native shapes only.**

| Token | Hex | Theme slot | Use |
|---|---|---|---|
| Background | `#1E2126` | Dark 1 (Background 1) | Master background |
| Text | `#F2F2F2` | Light 1 (Text 1) | Titles, body |
| Panel | `#2B2F36` | Dark 2 | Caption bar, cards, panels |
| Muted | `#A9B0B8` | Light 2 | Secondary text, credit lines |
| Orange | `#F28C28` | Accent 1 | Rules, nodes, arrows, bullets |
| Green | `#3FB950` | Accent 2 | Agreed chip |
| Blue | `#4DA3FF` | Accent 3 | Provisional chip |
| Purple | `#B084F5` | Accent 4 | Proposed chip |
| Amber | `#F2C14E` | Accent 5 | Caution, In progress marker |
| Red | `#E5484D` | Accent 6 | Stop, Blocked marker |
| Link | `#8FC7FF` | Hyperlink | Links (followed: `#C9B2F5`) |

Not in the theme, drawn as plain RGB by the kit: panel alt `#343A43`, line `#4A515B`, steel `#9AA0A6`, sleeper `#6B5B4B`, dark text on bright fills `#101418`.

**Type scale.** Nothing below 14 pt, with two legal exceptions.

| Item | Size |
|---|---|
| Title | 36 pt bold (cover 54, closing 44, chapter 48) |
| Caption (inside the bar) | 20 pt |
| Diagram labels | 14 to 18 pt |
| Status chip (top right), inline chip, slide number | 14 pt, chips bold upper case |
| Credit line under a picture | 10 pt (exception) |
| Credits table | 11 pt (exception) |

**Fixed geometry** (inches): title (0.6, 0.4) 10.2 x 0.8; status chip (11.03, 0.58) 1.7 x 0.4; content area y 1.45 to 6.15; caption bar (0.6, 6.3) 12.13 x 0.8 with an orange rule on its left; slide number (11.73, 7.14) 1.0 x 0.3. Margins 0.6 left and right. Panel corners 0.08 in; stroke 1.5 pt; connectors 2.25 pt.

---

## 2. Layouts: what each is for

Pick the layout by the idea, not by the look. Layout names are exactly as below (`k.add_slide(prs, "<name>", ...)`).

| Layout | Placeholders (name, idx) | Use it for |
|---|---|---|
| **Cover** | Title 0, Subtitle 1, Cover note 18 | Slide 1. Track motif on the right. No chip, no number. |
| **Chapter divider** | Title 0, Chapter label 19, Summary 17 | Opens a part of a long deck. |
| **Title + visual + caption** | Title 0, Status chip 13, Caption 14 | The workhorse. You draw one diagram (a group of native shapes) in the open area. |
| **Picture + caption + credit line** | Title, Status chip, Picture 16, Credit line 15, Notes 17, Caption | One picture with its credit line directly under it and two or three short points beside it. |
| **Two-panel compare** | Title, Status chip, Left heading 21, Left body 22, Right heading 23, Right body 24, Caption | Two options, before and after, or two views of one thing. |
| **Table** | Title, Status chip, Table 20, Caption | A small table (aim for 4 columns by 5 rows at most). |
| **Card grid (4)** | Title, Status chip, Card 1 to 4 (idx 21 to 24), Caption | Four items, 2 x 2. Good for open questions. |
| **Card grid (8)** | Title, Status chip, Card 1 to 8 (idx 21 to 28), Caption | Eight short items, 4 x 2. Heading and one short line each. |
| **Horizontal timeline** | Title, Status chip, Stop 1 to 5 (idx 21 to 25), Caption | Five stops in order. Labels alternate above and below. |
| **Key-facts tiles** | Title, Status chip, Tile 1 to 4 (idx 21 to 24), Caption | Four big values with a short label each. |
| **Status legend** | Title, Caption | "How to read the tags". The five chips and their meanings are drawn on the layout, so every legend slide is identical. |
| **Credits / sources table** | Title, Table 20, Note 17, Caption | Last content slide: every picture, author, licence, link. Table text is 11 pt. |
| **Closing / what next** | Title 0, Next steps 17, Closing note 18 | Final slide: up to three numbered next steps. |

How the text goes in:

- **Cards and tiles** take two lines in one placeholder: the heading on the first paragraph, the detail as a second paragraph at level 2 (`{"text": "...", "lvl": 1}` in Python, or Enter then Tab in PowerPoint). Tiles: the big value first, the label second.
- **Panels, rules, track motifs** are drawn on the layout behind the placeholders. Edit them in Slide Master view, not on slides.
- Layouts carry **no transitions, no animations, no speaker notes**, and no autofit: text never shrinks silently, so keep it short.

---

## 3. Slide rules

1. **One idea per slide.** The title says it; the caption says it again in one or two lines.
2. **Words.** Aim for 25 words or fewer in total (caption plus diagram labels plus inline chips that carry words). Never above 45. Not counted: title, status chip, slide number, credit lines. Exempt: Status legend, Credits, Cover, Chapter divider, Closing.
3. **Never rely on colour alone.** Every status chip carries its word. Every pill has a marker shape and its word. In a diagram, name a state in words as well as colouring it.
4. **Alt text** on every picture, every diagram group and every table (`k.set_alt`, or Format, Alt Text). One plain sentence that says what the picture or diagram shows. Group a diagram so it needs only one.
5. **Credits.** A photograph gets a 10 pt credit line directly under it (`Credit line` placeholder) and a row in the credits table. Credit text is the author's, never "found online". Pictures are cropped to fit, never stretched (`k.fill_picture`).
6. **14 pt floor.** Diagram labels 14 pt or more. Only credit lines (10 pt) and credits tables (11 pt) go lower.
7. **One status chip** top right on every content slide, naming the status of the slide's main idea. Not on the cover, legend, chapter, credits or closing slides. A statement with a *different* status gets its own inline chip beside it (`k.ichip`). Never leave such a statement untagged.
8. **Reading order** is title, chip, visual, caption, slide number. `k.finish(slide)` puts shapes in that order.
9. **No speaker notes, no transitions or animations in the file you edit.** Add them last with `polish.py` (section 5).
10. British English, plain short sentences, no invented facts.

### Status chips and report workflow pills (two different things)

| Design status chips (filled, upper case) | Meaning |
|---|---|
| **AGREED** green `#3FB950` | Decided. |
| **PROPOSED** purple `#B084F5` | Suggested, not confirmed. |
| **PROVISIONAL** blue `#4DA3FF` | A test number that may change. |
| **UNDECIDED** outline `#A9B0B8`, no fill | Still an open question. |
| **BACKGROUND** grey `#4A515B` | A real-world fact. |

The kit never assigns a status to anything. Use chips only where your deck has a source of truth for its statuses.

**Report workflow pills** (`k.pill`): **Complete**, **In progress**, **Blocked**, **Planned**. These are *report workflow states*, not design statuses. They are drawn as open outline pills with a marker (tick, dots, bar, dashed ring) so they cannot be mistaken for filled chips. Do not put a pill where a chip belongs, and do not mix the two on one slide unless the slide is explicitly about both.

In PowerPoint, the chip placeholder takes the word; to colour it, copy a chip from the Patterns deck ("Chips and pills" slide) or use Shape Fill and Shape Outline with the hex values above. In Python, `k.set_status(slide, "Agreed")` does all of it.

---

## 4. Build a new deck from the kit (Python)

Needs `python-pptx`, `Pillow` and `lxml`. The kit measures text with Liberation Sans (Arial's metrics), so install it on Linux if it is missing (`/usr/share/fonts/truetype/liberation/`).

```python
import sys
sys.path.insert(0, "Reporting/Claude Presents/Templates/kit")
import el_kit as k

prs = k.new_deck("My deck title", subject="One line", keywords="a; b")   # opens the template, sets en-GB + author

# 1. Cover
s = k.add_slide(prs, "Cover", "Deck title")
k.put(s, "Subtitle", "Replace this subtitle")
k.put(s, "Cover note", "Version 1 · Author")
k.finish(s)

# 2. Workhorse: a status chip, a native-shape diagram in a group with alt text, an inline chip, a caption
s = k.add_slide(prs, "Title + visual + caption", "One idea per slide", "Agreed", "One sentence that says it.")
g = k.group(s.shapes, "Diagram: three steps", "Three boxes in a row joined by arrows")
k.flow_row(g.shapes, 0.9, 2.5, 11.5, 1.3, ["Step one", "Step two", "Step three"], gap=0.7)
k.ichip(g.shapes, "Proposed", 5.95, 4.2, "PROPOSED", w=1.4)   # centred under step two
k.finish(s)

# 3. Cards: heading on the first paragraph, detail at level 2
s = k.add_slide(prs, "Card grid (4)", "Four open questions", "Undecided", "Each one is still open.")
for n in range(1, 5):
    k.put(s, "Card %d" % n, [{"text": "Question %d?" % n}, {"text": "Short detail", "lvl": 1}])
k.finish(s)

# 4. Table (placeholder insert, every cell formatted)
s = k.add_slide(prs, "Table", "A small table", "Provisional", "Test numbers only.")
k.fill_table(s, [["Item", "Value"], ["Row one", "00"], ["Row two", "00"]], [6, 3],
             alt="Table of two rows of placeholder values", size=18, aligns=["l", "c"], row_h=0.8)
k.finish(s)

prs.save("my_deck.pptx")
```

With a picture (cropped to fit, credit line included):

```python
s = k.add_slide(prs, "Picture + caption + credit line", "A picture", "Background", "What the picture shows.")
k.fill_picture(s, "path/to/image.png", "Alt text: what the picture shows",
               credit_text="Author, licence, source")
k.put(s, "Notes", ["First short point", "Second short point"])
k.finish(s)
```

What `k.finish(slide)` does: removes any placeholder you did not fill (so nothing is empty), adds the live slide-number placeholder, and puts shapes in reading order. Always call it last on each slide, after you have drawn your diagram.

Useful kit calls (all take a shapes collection `sh`, so they work on a slide or inside a group): `rect`, `box`, `oval`, `label`, `poly`, `line`, `arrow`, `path` (elbow), `curve`, `group`, `chip`, `ichip`, `pill`, `callout`, `flow_row`, `card`, `tile`, `timeline`, `track_motif`, `rails_strip`, `generic_wagon`, `picture_box`, `add_picture_fit`, `add_table`, `credit`, `caption_bar`. Measuring: `text_w`, `wrap_lines`, `balanced_width`, `word_count`. Each has a docstring.

Draw a diagram like this: make one group with `k.group(...)`, draw into `g.shapes`, start every leader line at the edge of its label and point it away from the label, give any inline chip its own space, keep every label at 14 pt or more.

---

## 5. Fade transitions and fade-in builds (`tools/polish.py`)

Do this **last**, on a deck that already passes the checker. `polish.py` is the existing tool in `Reporting/Claude Presents/tools/`; the kit does not copy or change it.

```
python3 "Reporting/Claude Presents/tools/polish.py" my_deck.pptx my_deck_polished.pptx
python3 Templates/kit/check_template.py my_deck_polished.pptx --polished
```

- Every slide gets a 0.7 s Fade transition.
- On each slide, the top-level **non-placeholder** shapes (diagram groups, pictures, free shapes) fade in automatically, in z-order, with no clicks.
- Placeholders (title, status chip, caption, notes, slide number) and shapes named `Chip...`, `Status chip...`, `Slide number`, `Credit...`, `Series line`, `Section label` or `num` stay put. So in kit decks the title, chip and caption are on screen from the start.
- A slide made only of placeholders (cards, tiles, timeline, compare, table) gets the transition but no builds. That is expected.
- Plays in Slide Show mode only. Editing view and most phone viewers show the finished slide.
- `polish.py` rewrites the transition and timing on every run, so you can re-run it. Keep the unpolished file as the source; polish a copy.
- The `--polished` flag tells the checker to expect transitions on slides. Layouts and master must still be clean.

---

## 6. Check it

```
python3 Templates/kit/check_template.py my_deck.pptx              # errors fail, warnings do not
python3 Templates/kit/check_template.py my_deck.pptx --words      # word table for every slide
python3 Templates/kit/check_template.py my_deck.pptx --xsd DIR    # also validate against the OOXML schemas
bash Templates/kit/render.sh my_deck.pptx /tmp/render 80          # LibreOffice to PNG, then look at every slide
```

The checker reports, per file: zip integrity, XML that parses, relationships and content types, no notes, no transitions or animations (unless `--polished`), theme fonts Arial and a light link colour, master background `#1E2126`, no stale default layouts, prompt text in every layout placeholder, smallest font (10 pt credit lines and 11 pt credits tables allowed, everything else 14 pt), alt text on pictures, groups and tables, language en-GB, reading order, no empty placeholders, text overflow estimate, stretched pictures, word budget, XML child order and unique shape ids. With `--xsd DIR` it also validates presentation, master, layouts, slides and theme against `pml.xsd` and `dml-main.xsd` (ISO/IEC 29500-4 Transitional) found in `DIR`; the schema files are not shipped with the kit.

The checker is not PowerPoint. A pass means the file is well formed and follows the house rules. Always open the deck in real PowerPoint and look at every slide before it goes out.

---

## 7. python-pptx gotchas

1. **Set left, top, width and height together on a placeholder.** Setting only one writes an `xfrm` with zero for the rest and the shape vanishes. Read the inherited values first, then write all four (the kit's `fill_picture` and `set_status` do).
2. **New slides do not get a slide-number placeholder.** python-pptx skips date, footer and number placeholders. `k.finish()` adds a live one. In PowerPoint use Insert, Slide Number, Apply to All.
3. **Strip `p:custDataLst` and `a16:creationId` when copying shapes** between slides, or PowerPoint can reuse ids it should not. `k.clone_shape(shape, slide)` does this and gives the copy fresh ids. Pictures need their own relationship: copy those with `add_picture`.
4. **Cloned slides can carry a copied `p:timing`** (and a transition). Call `k.clear_timing(slide)` on the copy.
5. **Empty placeholders show nothing in a slide show but fail the checker.** Fill them or let `finish()` remove them.
6. **python-pptx cannot open a `.potx`.** Script against the `.pptx`. Only PowerPoint opens the `.potx`.
7. **Do not move a group by editing its child offsets.** Set `group.left` and `group.top`. Child coordinates in groups the kit builds equal slide coordinates.
8. **Table borders must come before the cell fill in `a:tcPr`.** Use `k.set_cell`; it orders them correctly and removes the table style id so nothing is inherited.
9. **XML child order matters to PowerPoint, not to LibreOffice** (for example `a:ln` children, `a:tcPr` children). A deck can look right in LibreOffice and still need repair in PowerPoint. The checker tests the common containers.
10. **LibreOffice draws a layout placeholder's prompt text onto slides if that layout placeholder has its own shape geometry.** So text placeholders in layouts carry no `prstGeom`; the kit writes the chip's rounded shape on the slide instead. Keep to that when you edit layouts.
11. **Hyperlink colour comes from the theme** (`#8FC7FF`), whatever colour the run says.
12. **Autofit is off** in every layout. Overflowing text overflows visibly. Shorten it.

---

## 8. Editing the template

Layouts are built in code (`kit/layouts.py`) so they are reproducible; edit there and run `python3 kit/build_template.py`. You can also edit the layouts by hand in PowerPoint (View, Slide Master) but then the code and the file drift apart: either copy the change back into `layouts.py` or treat the `.pptx` as the new source. Keep the placeholder names and idx numbers stable: the kit finds placeholders by name, and slides keep their text when you switch layouts only if idx numbers match.

To add a layout: write a `build_xxx(b)` function in `layouts.py` (decor first with the `el_kit` drawing calls on `L.sh`, then placeholders with `L.title()`, `L.chip()`, `L.body(...)`, `L.caption()`, `L.number()`), add it to `build_all`, add its name to `LAYOUT_NAMES`, add an example to `patterns.py`, rebuild and run the checker.
