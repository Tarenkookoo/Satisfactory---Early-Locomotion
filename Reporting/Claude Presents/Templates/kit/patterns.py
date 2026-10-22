"""patterns: builds EL_Claude_Template_Patterns_v001.pptx, one filled example slide per layout.

All text is neutral dummy text ("Example title", "Replace this caption"). Diagrams are native shapes grouped
with alt text. There are no photographs: the picture layout shows a labelled grey "Picture goes here" box.
Nothing here states anything about the mod; status chips are used only to show how they look and where they go.

Each example is a function `slide_xxx(prs)` that a new deck can copy and adapt.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import el_kit as k  # noqa: E402
from pptx.enum.dml import MSO_LINE  # noqa: E402

CAPTION = "Replace this caption"


def _finish(s):
    return k.finish(s)


# ------------------------------------------------------------------ cover, legend, chapter
def slide_cover(prs):
    s = k.add_slide(prs, "Cover", "Example title")
    k.put(s, "Subtitle", "Replace this subtitle")
    k.put(s, "Cover note", "Version 1 · Replace this line")
    return _finish(s)


def slide_legend(prs):
    s = k.add_slide(prs, "Status legend", "How to read the tags",
                    caption="Every idea carries a tag in the top-right corner.")
    return _finish(s)


def slide_chapter(prs):
    s = k.add_slide(prs, "Chapter divider", "Example chapter title")
    k.put(s, "Chapter label", "Part 1")
    k.put(s, "Summary", "Replace this one-line summary")
    return _finish(s)


# ------------------------------------------------------------------ workhorse variants (native diagrams)
def slide_flow(prs):
    """Agreed. Row of steps, a muted label under each, and one inline chip for a statement with its own status."""
    s = k.add_slide(prs, "Title + visual + caption", "Example title", "Agreed", CAPTION)
    g = k.group(s.shapes, "Diagram: four steps", "Four boxes in a row joined by arrows: step one to step four")
    k.flow_row(g.shapes, 0.9, 2.5, 11.5, 1.3, ["Step one", "Step two", "Step three", "Step four"], gap=0.7)
    bw = (11.5 - 0.7 * 3) / 4
    for i in range(4):
        x = 0.9 + i * (bw + 0.7)
        k.label(g.shapes, x, 3.95, bw, 0.4, "Replace this label", 14, k.MUTED, align="c", anchor="t",
                name="step label")
    k.ichip(g.shapes, "Proposed", 0.9 + 2 * (bw + 0.7) + (bw - 1.4) / 2, 4.6, "PROPOSED", w=1.4)
    return _finish(s)


def slide_cycle(prs):
    """Proposed. Three parts in a loop with a callout whose leader starts at the label edge."""
    s = k.add_slide(prs, "Title + visual + caption", "Example title", "Proposed", CAPTION)
    g = k.group(s.shapes, "Diagram: loop of three parts",
                "Three boxes arranged in a triangle with arrows running round in a loop, and a note pointing at one box")
    gs = g.shapes
    top, bl, br = (4.0, 1.7), (1.9, 4.5), (6.1, 4.5)
    for (x, y), t in ((top, "Part A"), (br, "Part B"), (bl, "Part C")):
        k.box(gs, x, y, 1.7, 0.8, t, 18, fill=k.PANEL, line=k.ORANGE, lw=2.0, bold=True, name="part")
    k.arrow(gs, 5.5, 2.5, 6.75, 4.42, k.ORANGE, name="loop arrow")
    k.arrow(gs, 6.05, 4.9, 3.65, 4.9, k.ORANGE, name="loop arrow")
    k.arrow(gs, 2.75, 4.42, 4.0, 2.5, k.ORANGE, name="loop arrow")
    k.callout(gs, 9.0, 2.6, 3.4, 0.8, "Replace this note", (7.85, 4.55), side="b", size=18)
    return _finish(s)


def slide_value(prs):
    """Provisional. A test number: tile, gauge, and an inline Provisional chip."""
    s = k.add_slide(prs, "Title + visual + caption", "Example title", "Provisional", CAPTION)
    g = k.group(s.shapes, "Diagram: test value on a gauge",
                "A tile showing a placeholder number, and a horizontal gauge with a marker partway along")
    gs = g.shapes
    k.tile(gs, 0.9, 1.8, 3.2, 2.9, "00", "Example value", accent=k.WATER)
    k.ichip(gs, "Provisional", 1.5, 4.95, "PROVISIONAL", w=2.0)
    k.rect(gs, 5.0, 3.0, 7.4, 0.5, k.PANEL_ALT, k.LINE, 1.5, radius=0.1, name="gauge track")
    k.rect(gs, 5.0, 3.0, 4.4, 0.5, k.WATER, None, radius=0.1, name="gauge fill")
    k.rect(gs, 9.33, 2.75, 0.1, 1.0, k.TEXT, None, name="gauge marker")
    k.label(gs, 5.0, 3.7, 1.5, 0.4, "Low", 14, k.MUTED, align="l", name="gauge low")
    k.label(gs, 10.9, 3.7, 1.5, 0.4, "High", 14, k.MUTED, align="r", name="gauge high")
    k.label(gs, 8.2, 2.25, 2.5, 0.4, "Test value", 14, k.TEXT, bold=True, name="gauge marker label")
    return _finish(s)


def slide_question(prs):
    """Undecided. An open topic is drawn as a question with dashed options, never as a choice."""
    s = k.add_slide(prs, "Title + visual + caption", "Example title", "Undecided", CAPTION)
    g = k.group(s.shapes, "Diagram: open question with two options",
                "A question mark in a circle beside a question box and two dashed option boxes, none chosen")
    gs = g.shapes
    k.oval(gs, 1.2, 3.1, 1.6, 1.6, None, k.MUTED, 2.5, name="question circle", text="?", size=48, color=k.MUTED,
           bold=True)
    k.box(gs, 3.4, 2.45, 8.9, 0.9, "Example question?", 20, fill=k.PANEL, line=k.MUTED, lw=2.0, bold=True,
          dash=MSO_LINE.DASH, name="question")
    k.box(gs, 3.4, 3.95, 4.2, 1.0, "Option A", 18, fill=None, line=k.MUTED, lw=2.0, dash=MSO_LINE.DASH,
          name="option")
    k.box(gs, 8.1, 3.95, 4.2, 1.0, "Option B", 18, fill=None, line=k.MUTED, lw=2.0, dash=MSO_LINE.DASH,
          name="option")
    return _finish(s)


def slide_fact(prs):
    """Background. A real-world fact with a generic side-on drawing and a labelled leader."""
    s = k.add_slide(prs, "Title + visual + caption", "Example title", "Background", CAPTION)
    g = k.group(s.shapes, "Diagram: plain wagon on a rail",
                "A plain grey box wagon on a length of rail, with a label pointing at it")
    gs = g.shapes
    gy = 4.95
    k.rails_strip(gs, 0.9, gy, 7.9)
    for x in (1.2, 3.3, 5.4):
        k.generic_wagon(gs, x, gy, u=0.4, length=4.4)
    k.callout(gs, 7.9, 1.9, 3.8, 0.8, "Example label", (6.4, 3.4), side="b", size=18)
    return _finish(s)


def slide_chips_pills(prs):
    """Reference: the five design chips and the four report workflow pills, drawn in different styles."""
    s = k.add_slide(prs, "Title + visual + caption", "Chips and pills", None, CAPTION)
    g = k.group(s.shapes, "Reference: status chips and workflow pills",
                "Left: five filled design status chips. Right: four outlined report workflow pills with marker shapes")
    gs = g.shapes
    k.label(gs, 0.9, 1.5, 5.3, 0.45, "Design status chips", 18, k.TEXT, bold=True, align="l", name="heading")
    for i, kind in enumerate(k.CHIPS):
        k.chip(gs, kind, 0.9, 2.1 + i * 0.62, name="Chip: " + kind)
    k.label(gs, 0.9, 5.25, 2.6, 0.4, "Example statement", 18, k.TEXT, align="l", name="example statement")
    k.ichip(gs, "Proposed", 3.35, 5.28, "PROPOSED", w=1.4)
    k.label(gs, 7.0, 1.5, 5.7, 0.45, "Report workflow pills", 18, k.TEXT, bold=True, align="l", name="heading")
    for i, st in enumerate(k.PILLS):
        k.pill(gs, st, 7.0, 2.1 + i * 0.62, w=2.3)
    k.label(gs, 7.0, 4.75, 5.0, 0.4, "Not design statuses", 14, k.MUTED, align="l", name="pill note")
    return _finish(s)


def slide_parts(prs):
    """Reference: the diagram parts the kit draws (arrows, outlines, callouts, track motif)."""
    s = k.add_slide(prs, "Title + visual + caption", "Diagram parts", None, CAPTION)
    cw, ch, gap = (12.13 - 0.4) / 3, 2.2, 0.2

    def cell(i, name, alt, draw, text):
        c, r = i % 3, i // 3
        x, y = 0.6 + c * (cw + gap), 1.5 + r * (ch + gap)
        g = k.group(s.shapes, name, alt)
        k.rect(g.shapes, x, y, cw, ch, k.PANEL, None, radius=0.08, name="cell panel")
        draw(g.shapes, x, y)
        k.label(g.shapes, x + 0.2, y + 1.7, cw - 0.4, 0.4, text, 14, k.MUTED, align="c", name="cell label")

    def d_arrow(gs, x, y):
        k.box(gs, x + 0.4, y + 0.5, 1.0, 0.7, "", 14, name="node")
        k.box(gs, x + cw - 1.4, y + 0.5, 1.0, 0.7, "", 14, name="node")
        k.arrow(gs, x + 1.5, y + 0.85, x + cw - 1.5, y + 0.85, k.ORANGE, name="arrow")

    def d_elbow(gs, x, y):
        k.box(gs, x + 0.4, y + 0.3, 1.0, 0.6, "", 14, name="node")
        k.box(gs, x + cw - 1.4, y + 1.0, 1.0, 0.6, "", 14, name="node")
        k.path(gs, [(x + 0.9, y + 0.95), (x + 0.9, y + 1.3), (x + cw - 1.5, y + 1.3)], k.ORANGE, name="elbow arrow")

    def d_curve(gs, x, y):
        k.box(gs, x + 0.4, y + 0.9, 1.0, 0.6, "", 14, name="node")
        k.box(gs, x + cw - 1.4, y + 0.9, 1.0, 0.6, "", 14, name="node")
        k.curve(gs, (x + 1.0, y + 0.85), (x + cw / 2, y + 0.0), (x + cw - 1.0, y + 0.85), k.ORANGE,
                name="curved arrow")

    def d_dash(gs, x, y):
        k.box(gs, x + 0.8, y + 0.4, cw - 1.6, 1.1, "", 14, fill=None, line=k.MUTED, lw=2.0, dash=MSO_LINE.DASH,
              name="dashed outline")

    def d_callout(gs, x, y):
        k.box(gs, x + cw - 1.5, y + 0.9, 1.1, 0.6, "", 14, name="node")
        k.callout(gs, x + 0.4, y + 0.3, 1.5, 0.5, "Label", (x + cw - 1.0, y + 0.88), side="r", size=14)

    def d_track(gs, x, y):
        k.track_motif(gs, x + 0.4, y + 0.45, cw - 0.8, 0.8, vertical=False)

    cell(0, "Part: arrow", "Two plain boxes joined by an orange arrow", d_arrow, "Arrow")
    cell(1, "Part: elbow arrow", "Two boxes joined by an orange elbow arrow", d_elbow, "Elbow arrow")
    cell(2, "Part: curved arrow", "Two boxes joined by a curved orange arrow", d_curve, "Curved arrow")
    cell(3, "Part: dashed outline", "A box with a dashed outline", d_dash, "Dashed outline")
    cell(4, "Part: callout", "A label with a leader line pointing at a box", d_callout, "Callout and leader")
    cell(5, "Part: track motif", "Two rails and sleepers seen from above", d_track, "Track motif")
    return _finish(s)


# ------------------------------------------------------------------ picture, compare, table
def slide_picture(prs):
    s = k.add_slide(prs, "Picture + caption + credit line", "Example title", "Background", CAPTION)
    k.remove_shape(k.ph(s, "Picture"))       # the Patterns deck has no photographs: grey box instead
    box = k.picture_box(s.shapes, 0.6, 1.45, 8.0, 4.5)
    k.put(s, "Credit line", "Credit line: author, licence, source (10 pt)")
    k.move_before(box, k.ph(s, "Credit line"))   # picture, then its credit line, then the notes
    k.put(s, "Notes", ["Short point to notice", "Another short point"])
    return _finish(s)


def slide_compare(prs):
    s = k.add_slide(prs, "Two-panel compare", "Example title", "Agreed", CAPTION)
    k.put(s, "Left heading", "Option A")
    k.put(s, "Left body", ["Short point", "Another short point"])
    k.put(s, "Right heading", "Option B")
    k.put(s, "Right body", ["Short point", "Another short point"])
    return _finish(s)


def slide_table(prs):
    s = k.add_slide(prs, "Table", "Example title", "Provisional", CAPTION)
    data = [["Item", "Value A", "Value B", "Value C"],
            ["Row one", "00", "00", "00"],
            ["Row two", "00", "00", "00"],
            ["Row three", "00", "00", "00"]]
    k.fill_table(s, data, [3.4, 2.9, 2.9, 2.9], alt="Example table: four columns, three rows of placeholder values",
                 size=18, aligns=["l", "c", "c", "c"], row_h=0.8)
    return _finish(s)


# ------------------------------------------------------------------ cards, timeline, tiles
def slide_cards4(prs):
    s = k.add_slide(prs, "Card grid (4)", "Example title", "Undecided", CAPTION)
    for n in range(1, 5):
        k.put(s, "Card %d" % n, [{"text": "Question %d?" % n}, {"text": "Replace this detail", "lvl": 1}])
    return _finish(s)


def slide_cards8(prs):
    s = k.add_slide(prs, "Card grid (8)", "Example title", "Agreed", CAPTION)
    for n in range(1, 9):
        k.put(s, "Card %d" % n, [{"text": "Card %d" % n}, {"text": "Detail", "lvl": 1}])
    return _finish(s)


def slide_timeline(prs):
    s = k.add_slide(prs, "Horizontal timeline", "Example title", "Proposed", CAPTION)
    for n in range(1, 6):
        k.put(s, "Stop %d" % n, [{"text": "Stop %d" % n}, {"text": "Short detail", "lvl": 1}])
    return _finish(s)


def slide_tiles(prs):
    s = k.add_slide(prs, "Key-facts tiles", "Example title", "Provisional", CAPTION)
    for n in range(1, 5):
        k.put(s, "Tile %d" % n, [{"text": "00"}, {"text": "Short label", "lvl": 1}])
    return _finish(s)


# ------------------------------------------------------------------ credits, closing
def slide_credits(prs):
    s = k.add_slide(prs, "Credits / sources table", "Image credits", None, "This deck uses no photographs.")
    link = {"link": "https://example.org/", "color": k.HLINK}
    names = ["one", "two", "three", "four", "five"]
    data = [["Item", "Author", "Licence", "Source"]] + [
        ["Example item " + n, "Example author", "Example licence", [[("example.org", link)]]] for n in names]
    k.fill_table(s, data, [3.4, 3.0, 3.0, 2.7], alt="Credits table: item, author, licence and source link",
                 size=11, row_h=0.55)
    k.put(s, "Note", "Replace this licence note.")
    return _finish(s)


def slide_closing(prs):
    s = k.add_slide(prs, "Closing / what next", "Example closing title")
    k.put(s, "Next steps", ["First next step", "Second next step", "Third next step"])
    k.put(s, "Closing note", "Replace this contact line")
    return _finish(s)


ORDER = [slide_cover, slide_legend, slide_chapter, slide_flow, slide_cycle, slide_value, slide_question,
         slide_fact, slide_chips_pills, slide_parts, slide_picture, slide_compare, slide_table, slide_cards4,
         slide_cards8, slide_timeline, slide_tiles, slide_credits, slide_closing]


def build_patterns(out_path, template=None):
    prs = k.new_deck("Early Locomotion house style: template patterns (v001)",
                     "One filled example slide per layout, with neutral dummy text and native-shape diagrams",
                     "template; patterns; examples; Early Locomotion; Claude Presents", template=template)
    for fn in ORDER:
        fn(prs)
    prs.save(out_path)
    return out_path
