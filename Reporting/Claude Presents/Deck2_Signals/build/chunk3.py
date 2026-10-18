"""Slides 19 to 27 of Deck 2 (the mod's signalling: automatic control, screen, limits, hand driving, status)."""
from lib import *

RED_T, GREEN_T, AMBER_T = C["red_text"], C["green"], C["amber"]
NOTE = "Blender model, not yet in the game."


# ------------------------------------------------------------------------------------------ 19
def _num_card(gs, x, y, w, h, n, text, size=20):
    rect(gs, x, y, w, h, fill=C["panel"], line=C["line"], line_w=1, radius=0.08)
    ellipse(gs, x + 0.5, y + h / 2, 0.55, fill=C["orange"])
    textbox(gs, x + 0.225, y + h / 2 - 0.25, 0.55, 0.5, str(n), 20, C["ink"], bold=True, align="c",
            margins=(0, 0, 0, 0), name="Step number")
    textbox(gs, x + 1.0, y, w - 1.15, h, text, size, C["text"], bold=True, name="Step text")


def s19(d):
    c = d.slide(19, "No wiring for you", "A")
    sh = c.shapes
    g = group(sh, "Signals join a box automatically",
              "Left: a track with one new signal and a dotted line to a signal box. Right: three numbered steps. "
              "Place a signal on connected track; a box with room takes control; rods and wires draw themselves.")
    gs = g.shapes
    ty = 4.3
    rails(gs, 0.8, ty, 5.7)
    box_building(gs, 1.0, 1.75, 2.0, 1.9, windows=True, door=False, name="Signal box")
    semaphore(gs, 5.2, ty + 0.34, "stop", 1.3, name="New signal")
    poly(gs, [(3.1, 2.95), (5.2, 2.95), (5.2, 3.15)], line_c=C["orange"], line_w=2.5, close=False,
         dash=MSO_LINE.ROUND_DOT, tail=True, name="Dotted line: box takes control")
    steps = ["Place a signal on connected track", "A box with room takes control",
             "Rods and wires draw themselves"]
    for i, t in enumerate(steps):
        _num_card(gs, 7.0, 1.6 + i * 1.45, 5.73, 1.25, i + 1, t)
    c.finish("Boxes take control of connected signals automatically. You never place wires.")


# ------------------------------------------------------------------------------------------ 20
def s20(d):
    c = d.slide(20, "Rods and wires you can see", "A")
    sh = c.shapes
    for i, (img, lab, alt) in enumerate([
            ("R03_semaphore_stop.jpg", "STOP: arm flat", "The mod's semaphore stop signal model with its arm flat (stop)."),
            ("R04_semaphore_clear.jpg", "CLEAR: arm raised", "The same signal model with its arm raised (clear).")]):
        x = 0.6 + i * 3.8
        picture(sh, img, x, 2.0, 3.5, 2.6, alt)
        pill = rect(sh, x + 0.1, 4.6 - 0.5, 2.5 if i == 0 else 2.9, 0.4, fill=C["panel"], line=C["line"], line_w=1,
                    radius=0.08, name=f"Label: {lab}")
        set_text(pill, lab, 16, RED_T if i == 0 else GREEN_T, bold=True, align="c", margins=(0.05, 0, 0.05, 0))
        credit(sh, x, 4.66, 3.5, NOTE)
    g = group(sh, "Linkage drawn between a box and its signals",
              "A schematic signal box with three orange dashed lines running to three signals. The lines show "
              "which box controls which signal.")
    gs = g.shapes
    ty = 4.1
    rails(gs, 8.3, ty, 4.45)
    box_building(gs, 8.2, 1.55, 1.3, 1.45, windows=True, door=False, name="Signal box")
    for x, st, ry in ((10.1, "stop", 2.7), (11.1, "clear", 2.5), (12.0, "clear", 2.3)):
        semaphore(gs, x, ty + 0.34, st, 0.9)
        vx = x - 0.35
        poly(gs, [(9.5, ry), (vx, ry), (vx, ty + 0.3)], line_c=C["orange"], line_w=2.25, close=False,
             dash=MSO_LINE.DASH, name="Rod")
    textbox(sh, 8.3, 4.95, 4.43, 0.85, "Visual layer only. Parts may twitch when a signal changes.", 16, C["text"],
            anchor="t")
    chip(sh, "U", x=8.3, y=5.82, w=4.43, h=0.42, text="Rod or wire look: undecided (OQ04)",
         name="Chip: Undecided (rod or wire look)")
    c.finish("Rods and wires are drawn for you. They show which box controls which signal.")


# ------------------------------------------------------------------------------------------ 21
def s21(d):
    c = d.slide(21, "The box screen", "P")
    sh = c.shapes
    g = group(sh, "Mock-up of a signal box screen",
              "A mock-up panel headed Signal box: Station A. Six signals, S1 to S6, each with a STOP or CLEAR "
              "label. A bar shows signals used, 6 of 8, and a line shows reach, 1,200 metres. Example numbers only.")
    gs = g.shapes
    px, py, pw, ph = 3.87, 1.5, 5.6, 4.4
    rect(gs, px, py, pw, ph, fill="#14171B", line=C["line"], line_w=2, radius=0.15, name="Screen panel")
    textbox(gs, px + 0.4, py + 0.15, pw - 0.8, 0.55, "Signal box: Station A", 22, C["orange"], bold=True)
    line(gs, px + 0.4, py + 0.75, px + pw - 0.4, py + 0.75, C["line"], 1.5)
    states = ["STOP", "CLEAR", "CLEAR", "STOP", "CLEAR", "CLEAR"]
    for i, st in enumerate(states):
        y = py + 0.9 + i * 0.42
        textbox(gs, px + 0.5, y, 0.8, 0.36, f"S{i + 1}", 18, C["text"], bold=True)
        pill = rect(gs, px + 1.4, y + 0.02, 1.3, 0.32, fill=C["red"] if st == "STOP" else C["green"], radius=0.16,
                    name=f"State pill {st}")
        set_text(pill, st, 14, C["ink"], bold=True, align="c", margins=(0.02, 0, 0.02, 0))
    by = py + 3.55
    textbox(gs, px + 0.5, by - 0.02, 2.6, 0.4, "Signals used 6 of 8", 18, C["text"], bold=True)
    rect(gs, px + 3.2, by + 0.06, 2.0, 0.24, fill=C["panel_alt"], radius=0.05)
    rect(gs, px + 3.2, by + 0.06, 2.0 * 6 / 8, 0.24, fill=C["orange"], radius=0.05, name="Used bar")
    textbox(gs, px + 0.5, by + 0.4, 5.0, 0.4, "Reach 1,200 m", 18, C["text"], bold=True)
    textbox(sh, px, py + ph + 0.08, pw, 0.35, "Example numbers only", 14, C["muted"], bold=True, align="c")
    c.finish("The box screen could list its signals, their state, capacity and reach.")


# ------------------------------------------------------------------------------------------ 22
def s22(d):
    c = d.slide(22, "Speed has three limits", "A")
    sh = c.shapes
    g = group(sh, "Three speed limits",
              "Three horizontal bars of different lengths for the track, signal and engine limits. A vertical "
              "line at the end of the shortest bar, with an arrow, shows that you go only that fast.")
    gs = g.shapes
    x0 = 3.5
    bars = [("Track limit", 7.0, C["elec"]), ("Signal limit", 4.2, C["amber"]), ("Engine limit", 5.6, C["orange"])]
    for i, (lab, w, col) in enumerate(bars):
        y = 2.2 + i * 0.95
        textbox(gs, 0.6, y, 2.8, 0.55, lab, 20, C["text"], bold=True, align="r")
        rect(gs, x0, y + 0.02, w, 0.5, fill=col, radius=0.06, name=f"Bar: {lab}")
    xl = x0 + 4.2
    line(gs, xl, 1.75, xl, 5.0, C["text"], 3, dash=MSO_LINE.DASH, name="Shortest limit")
    arrow(gs, x0, 5.05, xl, 5.05, C["orange"], 4, name="Arrow: you go this fast")
    textbox(gs, x0, 5.12, xl - x0, 0.45, "You go this fast", 20, C["orange"], bold=True, align="c")
    chip(gs, "P", x=xl + 0.25, y=1.62, w=3.1, h=0.4, text="Lowest of three: Proposed",
         name="Chip: Proposed (rule)")
    textbox(sh, 0.6, 5.8, 8.0, 0.4, "Hills and loading can slow trains further.", 16, C["muted"], bold=True)
    textbox(sh, 10.0, 5.8, 2.73, 0.4, "Not to scale", 14, C["muted"], bold=True, align="r")
    c.finish("Speed is the lowest of three limits: track, signals and engine.")


# ------------------------------------------------------------------------------------------ 23
def s23(d):
    c = d.slide(23, "Later signals", "A")
    sh = c.shapes
    g = group(sh, "Signals over time",
              "A timeline of three stages. Start: semaphore blocks (agreed). Later: improved semaphores or "
              "interlocking (proposed), for example 90 km/h and 800 m blocks (provisional). Mature: electronic "
              "signals like vanilla (proposed). Below, complex junctions stay slower than electric rail on purpose.")
    gs = g.shapes
    ly = 2.55
    arrow(gs, 0.9, ly, 12.4, ly, C["steel"], 3, name="Timeline")
    nodes = [(2.4, "A", "Start: semaphore blocks"), (6.67, "P", "Later: improved semaphores or interlocking"),
             (10.93, "P", "Mature: electronic signals like vanilla")]
    for cx, tag, text in nodes:
        chip(gs, tag, x=cx - 0.78, y=1.6, w=1.56, h=0.34)
        ellipse(gs, cx, ly, 0.5, fill=C["orange"], line=C["bg"], line_w=3)
        rect(gs, cx - 1.8, 3.0, 3.6, 1.15, fill=C["panel"], line=C["line"], line_w=1, radius=0.08)
        textbox(gs, cx - 1.65, 3.0, 3.3, 1.15, text, 18, C["text"], bold=True, align="c")
    textbox(gs, 6.67 - 1.8, 4.3, 3.6, 0.4, "Example: 90 km/h, 800 m blocks", 16, C["text"], bold=True, align="c")
    chip(gs, "V", x=6.67 - 0.78, y=4.75, w=1.56, h=0.34)
    # junction icon
    jy = 5.75
    line(gs, 0.9, jy, 2.6, jy, C["steel"], 4)
    line(gs, 1.3, jy, 2.4, jy - 0.4, C["steel"], 4)
    line(gs, 2.4, jy - 0.4, 2.9, jy - 0.4, C["steel"], 4)
    textbox(gs, 3.2, jy - 0.35, 9.2, 0.7, "Complex junctions: slower than electric (deliberate)", 20, C["text"],
            bold=True)
    c.finish("Better signals come later. Busy junctions stay slower than mature electric rail.")


# ------------------------------------------------------------------------------------------ 24
def s24(d):
    c = d.slide(24, "Driving by hand", "A")
    sh = c.shapes
    g = group(sh, "Manual railway operations diagram",
              "A mock-up of a simple track diagram panel: circles joined by lines, with the active route in "
              "bright orange and alternatives in grey. Three mode buttons across the top: AUTO, YARD and MAINLINE.")
    gs = g.shapes
    px, py, pw, ph = 4.27, 1.5, 4.8, 3.8
    rect(gs, px, py, pw, ph, fill="#14171B", line=C["line"], line_w=2, radius=0.18, name="Diagram panel")
    for i, lab in enumerate(["AUTO", "YARD", "MAINLINE"]):
        x = px + 0.2 + i * 1.5
        on = lab == "YARD"
        pill = rect(gs, x, py + 0.17, 1.4, 0.4, fill=C["orange"] if on else C["panel_alt"],
                    line=C["orange"] if on else C["line"], line_w=1.5, radius=0.2, name=f"Mode pill {lab}")
        set_text(pill, lab, 14, C["ink"] if on else C["text"], bold=True, align="c", margins=(0.02, 0, 0.02, 0))
    nodes = {"A": (4.8, 4.75), "B": (5.75, 4.75), "C": (6.7, 4.75), "D": (7.65, 3.95), "E": (8.65, 3.95),
             "F": (7.65, 4.75), "G": (8.65, 4.75), "H": (6.5, 3.2), "I": (7.5, 2.75)}
    grey = [("B", "H"), ("H", "I"), ("C", "F"), ("F", "G")]
    route = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "E")]
    for a, b in grey:
        line(gs, *nodes[a], *nodes[b], "#6C7480", 3)
    for a, b in route:
        line(gs, *nodes[a], *nodes[b], C["orange"], 5)
    on_route = {"A", "B", "C", "D", "E"}
    for k, (x, y) in nodes.items():
        ellipse(gs, x, y, 0.36, fill=C["orange"] if k in on_route else "#2B2F36",
                line=C["text"] if k in on_route else "#6C7480", line_w=2)
    textbox(sh, 9.3, 1.55, 3.43, 0.8, "YARD: you set points one by one", 18, C["text"], bold=True, anchor="t")
    t = "MAINLINE: pick a destination and let the game set points"
    textbox(sh, 1.25, 5.5, 8.2, 0.45, t, 18, C["text"], bold=True, align="r", name="Mainline text")
    chip(sh, "P", x=9.6, y=5.52, w=1.65, h=0.4)
    c.finish("Drivers can set nearby points from a simple track diagram. Signal boxes keep control.")


# ------------------------------------------------------------------------------------------ 25
def s25(d):
    c = d.slide(25, "Where this stands", "V")
    sh = c.shapes
    for i, (img, alt) in enumerate([
            ("R03_semaphore_stop.jpg", "The mod's semaphore stop signal model with its arm flat (stop)."),
            ("R04_semaphore_clear.jpg", "The same signal model with its arm raised (clear).")]):
        x = 0.6 + i * 2.85
        picture(sh, img, x, 2.3, 2.6, 1.95, alt)
        credit(sh, x, 4.3, 2.6, NOTE, h=0.35)
    g = group(sh, "Where the signalling work stands",
              "Four stages in a row. The semaphore model is built in Blender and is under way. In the game, "
              "signal boxes, and rods and wires are all planned.")
    gs = g.shapes
    labels = ["Semaphore model: built in Blender", "In the game: planned", "Signal boxes: planned",
              "Rods and wires: planned"]
    xs = [6.45 + i * 1.61 for i in range(4)]
    line(gs, xs[0] + 0.72, 2.4, xs[3] + 0.72, 2.4, C["steel"], 3)
    for i, (x, lab) in enumerate(zip(xs, labels)):
        done = i == 0
        ellipse(gs, x + 0.725, 2.4, 0.34, fill=C["orange"] if done else C["bg"], line=C["orange"] if done else C["steel"],
                line_w=3)
        card = rect(gs, x, 2.85, 1.45, 2.05, fill=C["panel"], line=C["orange"] if done else C["steel"], line_w=2,
                    dash=None if done else MSO_LINE.DASH, radius=0.08, name=f"Stage: {lab}")
        set_text(card, lab, 16, C["text"], bold=True, align="c", anchor="t", margins=(0.08, 0.12, 0.08, 0.05))
        if done:
            p = rect(gs, x + 0.12, 4.35, 1.21, 0.38, fill=C["orange"], radius=0.19, name="State: Under way")
            set_text(p, "Under way", 14, C["ink"], bold=True, align="c", margins=(0.02, 0, 0.02, 0))
    chip(sh, "V", x=6.45, y=5.2, w=3.0, h=0.42, text="Plans can change.", name="Chip: Provisional (plans)")
    c.finish("The semaphore model exists in Blender only. It is not in the game yet.")


# ------------------------------------------------------------------------------------------ 26
def s26(d):
    c = d.slide(26, "Still undecided", "U")
    sh = c.shapes
    cards = [("Block lengths, speed caps", "OQ03"), ("If a signal fails?", "OQ03"),
             ("Which later signals first?", "OQ03"), ("Measuring a box's reach", "OQ04"),
             ("Which box wins an overlap?", "OQ04"), ("Rod or wire look", "OQ04"),
             ("Arm: rises or drops?", None), ("Who sets points near signals?", None)]
    g = group(sh, "Open questions",
              "Eight cards, each marked undecided, each a question that is still open. Nothing has been chosen.")
    gs = g.shapes
    for i, (q, oq) in enumerate(cards):
        x = 0.6 + (i % 4) * 3.077
        y = 1.65 + (i // 4) * 2.15
        rect(gs, x, y, 2.9, 1.95, fill=C["panel"], line=C["line"], line_w=1, radius=0.08)
        chip(gs, "U", x=x + 0.15, y=y + 0.15, w=2.3, h=0.34, text="UNDECIDED" + (f" · {oq}" if oq else ""),
             name="Chip: Undecided (card)")
        textbox(gs, x + 0.15, y + 0.6, 2.6, 1.25, q, 20, C["text"], bold=True, anchor="t", margins=(0, 0.02, 0, 0))
    c.finish("These questions are open. Nothing here has been chosen yet.")


# ------------------------------------------------------------------------------------------ 27
CREDITS = [
    ("P13", "7", "Richard Dunn, CC BY-SA 2.0",
     "https://commons.wikimedia.org/wiki/File:Semaphore_distant_signal_on_the_approach_to_Henley_in_Arden._-_geograph.org.uk_-_11867.jpg"),
    ("P14", "9", "Reading Tom, CC BY 2.0",
     "https://commons.wikimedia.org/wiki/File:Williton_Signal_Box_-_November_2014.jpg"),
    ("P15", "10", "Nigel Brown, CC BY-SA 2.0",
     "https://commons.wikimedia.org/wiki/File:Signalbox_workings,_Didcot_Railway_Centre_-_geograph.org.uk_-_658545.jpg"),
    ("P16", "11", "mattbuck (category), CC BY-SA 3.0",
     "https://commons.wikimedia.org/wiki/File:Williton_railway_station_MMB_10.jpg"),
    ("R03", "1, 20, 25", "Early Locomotion project (test model, not final art)", None),
    ("R04", "20, 25", "Early Locomotion project (test model, not final art)", None),
]


def s27(d):
    c = d.slide(27, "Image credits", None)
    sh = c.shapes
    rows, cols = len(CREDITS) + 1, 4
    gf = sh.add_table(rows, cols, E(0.6), E(1.5), E(12.13), E(0.42 * rows))
    set_alt(gf, "Table of image credits: slot, slide, author and licence, and a source link for each picture.",
            "Image credits table")
    tbl = gf.table
    for i, w in enumerate((1.1, 1.5, 6.6, 2.93)):
        tbl.columns[i].width = E(w)
    heads = ["Slot", "Slide", "Author and licence", "Source link"]

    def fill_cell(cell, text, bold=False, fill=C["panel"], link=None):
        cell.fill.solid()
        cell.fill.fore_color.rgb = rgb(fill)
        cell.margin_left = cell.margin_right = E(0.1)
        cell.margin_top = cell.margin_bottom = E(0.05)
        cell.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = cell.text_frame.paragraphs[0]
        r = p.add_run()
        r.text = text
        r.font.name, r.font.size, r.font.bold = FONT, Pt(11), bold
        r.font.color.rgb = rgb(C["text"])
        if link:
            r.hyperlink.address = link
            r.font.underline = True
        tcPr = cell._tc.get_or_add_tcPr()
        for tag in ("a:lnL", "a:lnR", "a:lnT", "a:lnB"):
            ln = etree.SubElement(tcPr, qn(tag))
            ln.set("w", "12700")
            sf = etree.SubElement(ln, qn("a:solidFill"))
            etree.SubElement(sf, qn("a:srgbClr")).set("val", "4A515B")
        # borders must precede the fill in tcPr
        fill_el = tcPr.find(qn("a:solidFill"))
        if fill_el is not None:
            tcPr.remove(fill_el)
            tcPr.append(fill_el)

    for j, h in enumerate(heads):
        fill_cell(tbl.cell(0, j), h, True, C["line"])
    for i, (slot, slide, who, url) in enumerate(CREDITS, 1):
        f = C["panel"] if i % 2 else C["panel_alt"]
        fill_cell(tbl.cell(i, 0), slot, True, f)
        fill_cell(tbl.cell(i, 1), slide, False, f)
        fill_cell(tbl.cell(i, 2), who, False, f)
        fill_cell(tbl.cell(i, 3), "Commons" if url else "Project render (no link)", False, f, link=url)
    for r_ in tbl.rows:
        r_.height = E(0.42)
    textbox(sh, 0.6, 5.0, 12.13, 0.4, "CC BY-SA photos are shown unmodified except for resizing.", 14, C["text"],
            bold=True)
    c.finish("Photographs come from Wikimedia Commons under Creative Commons licences.")


SLIDES = [s19, s20, s21, s22, s23, s24, s25, s26, s27]
