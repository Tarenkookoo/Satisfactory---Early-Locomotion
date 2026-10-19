"""Chunk 3: slides 19 to 26."""
from lib import *


def right_chip(sh, kind, text, right, y, **kw):
    w = text_w(text, 14, True) + 0.34
    return ichip(sh, kind, right - w, y, text, w=w, **kw)


# ---------------------------------------------------------------- slide 19
def s19(prs):
    s = new_slide(prs, "Renumber by hand", "Agreed")
    sh = s.shapes
    g = group(sh, "Unlock card and number editor",
              "A shop-style unlock card for renumbering, with an Unlock button and no price, and a number editor "
              "mock. The scheme part of the number is greyed with a padlock, your digits are editable, and a red "
              "message says Already used. The number is an example only.")
    gs = g.shapes
    # unlock card
    rect(gs, 0.6, 1.5, 4.6, 3.7, PANEL, ORANGE, 2.5, radius=0.12, name="unlock card")
    rect(gs, 0.66, 1.56, 4.48, 0.66, PANEL_ALT, None, radius=0.08, name="unlock header")
    label(gs, 0.9, 1.56, 4.0, 0.66, "Renumber unlock", 20, TEXT, True, align="l", name="unlock title")
    oval(gs, 1.9, 2.45, 2.0, 1.7, BG, ORANGE, 2.5, name="unlock icon disc")
    plate_blank(gs, 2.2, 3.15, 1.4, 0.6)
    pencil(gs, 3.0, 2.55, 0.55, AMBER)
    rect(gs, 1.2, 4.4, 3.4, 0.62, ORANGE, None, radius=0.31, name="unlock button", text="Unlock", size=20,
         color=DARK, bold=True)
    arrow(gs, 5.3, 3.35, 5.9, 3.35, ORANGE, 3.0, name="then arrow")
    # number editor
    rect(gs, 6.0, 1.5, 6.73, 3.7, PANEL, LINE, 1.5, radius=0.12, name="editor panel")
    rect(gs, 6.06, 1.56, 6.61, 0.66, PANEL_ALT, None, radius=0.08, name="editor header")
    label(gs, 6.3, 1.56, 3.0, 0.66, "Edit number", 20, TEXT, True, align="l", name="editor title")
    label(gs, 10.1, 1.56, 2.4, 0.66, "Example only", 14, MUTED, align="r", name="example label")
    rect(gs, 6.4, 2.6, 2.1, 1.2, DARKMETAL, MUTED, 2.0, radius=0.1, dash=MSO_LINE.DASH, name="scheme part (locked)",
         text="47", size=40, color=MUTED, bold=True)
    padlock(gs, 8.0, 2.38, 0.38, AMBER)
    rect(gs, 8.65, 2.6, 3.7, 1.2, COAL, ORANGE, 3.0, radius=0.1, name="your digits (editable)", text="298", size=40,
         color=TEXT, bold=True)
    rect(gs, 11.25, 2.82, 0.05, 0.76, ORANGE, None, name="text cursor")
    rect(gs, 6.4, 4.05, 5.95, 0.7, "#4A1E21", RED, 2.0, radius=0.08, name="error strip")
    cross(gs, 6.85, 4.4, 0.26, RED, 4.5)
    label(gs, 7.25, 4.05, 4.9, 0.7, "Already used", 18, TEXT, True, align="l", name="error text")
    ichip(sh, "Undecided", 0.6, 5.5, "Cost and screens: undecided (OQ30)")
    finish(s, "A cheap unlock lets you edit your numbers. Locked parts stay locked.", 19)
    return s


# ---------------------------------------------------------------- slide 20
def s20(prs):
    s = new_slide(prs, "Numbers in the right place", "Agreed", chip_note="Agreed direction")
    sh = s.shapes
    g = group(sh, "Number positions on two engines",
              "A tender engine and a tank engine, each with small number marks in different places. The tender "
              "engine has marks on the front of the boiler, the cab side and the tender. The tank engine has marks "
              "on the tank side and the bunker.")
    gs = g.shapes

    def mark(x, y, w, h):
        plate_blank(gs, x, y, w, h)

    def leader(x1, y1, x2, y2):
        line(gs, x1, y1, x2, y2, ORANGE, 1.75, name="leader")
        oval(gs, x2 - 0.06, y2 - 0.06, 0.12, 0.12, ORANGE, None, name="leader dot")

    # tender engine (top row, left)
    u, x0, gy = 0.38, 0.9, 3.55
    rails_strip(gs, x0 - 0.3, gy, 7.7, sleepers=False)
    engine(gs, x0, gy, u, "tender", 2, STEEL)
    X = lambda a: x0 + a * u
    Y = lambda h: gy - h * u
    mark(X(0.7), Y(2.9), 0.95, 0.3)                         # tender
    mark(X(4.7), Y(2.45), 0.6, 0.24)                        # cab side
    rect(gs, X(17.55), Y(3.5), 0.1, 0.5, ORANGE, None, name="front mark")  # front of the boiler
    label(gs, X(0.7) - 0.05, 1.4, 1.1, 0.34, "Tender", 14, TEXT, True, name="mark label")
    leader(X(0.7) + 0.45, 1.76, X(0.7) + 0.45, Y(2.9) + 0.02)
    label(gs, X(4.7) - 0.25, 1.4, 1.1, 0.34, "Cab side", 14, TEXT, True, name="mark label")
    leader(X(4.7) + 0.3, 1.76, X(4.7) + 0.3, Y(2.45) + 0.02)
    label(gs, X(17.9) + 0.45, Y(3.5) - 0.02, 1.9, 0.54, "Front of the boiler", 14, TEXT, True, align="l",
          name="mark label")
    leader(X(17.9) + 0.4, Y(3.5) + 0.25, X(17.65), Y(3.5) + 0.25)
    # tank engine (bottom row, right)
    x2, gy2 = 6.4, 5.95
    rails_strip(gs, x2 - 0.3, gy2, 6.0, sleepers=False)
    engine(gs, x2, gy2, u, "tank", 2, STEEL)
    X2 = lambda a: x2 + a * u
    Y2 = lambda h: gy2 - h * u
    mark(X2(0.25), Y2(2.9), 0.55, 0.26)                     # bunker
    mark(X2(5.9), Y2(2.9), 1.1, 0.3)                        # tank side
    label(gs, X2(0.25) - 0.25, 3.82, 1.1, 0.34, "Bunker", 14, TEXT, True, name="mark label")
    leader(X2(0.25) + 0.28, 4.18, X2(0.25) + 0.28, Y2(2.9) + 0.02)
    label(gs, X2(5.9), 3.82, 1.4, 0.34, "Tank side", 14, TEXT, True, name="mark label")
    leader(X2(5.9) + 0.55, 4.18, X2(5.9) + 0.55, Y2(2.9) + 0.02)
    finish(s, "Each engine shows its number where real ones did. There is no single decal spot.", 20)
    return s


# ---------------------------------------------------------------- slide 21
def s21(prs):
    s = new_slide(prs, "Find any engine", "Agreed", chip_note="Agreed direction")
    sh = s.shapes
    g = group(sh, "Fleet search mock-up",
              "A mock map of a rail network with engine dots. Dots that match the search are bright orange and "
              "the rest are dimmed. Beside it are two search boxes, one with the class 9F and one with the "
              "number 92214, and a list that shows only the matches. All examples only.")
    gs = g.shapes
    rect(gs, 0.6, 1.5, 7.6, 4.05, COAL, LINE, 1.5, radius=0.1, name="map panel")
    nets = [[(0.9, 3.0), (3.0, 3.0), (4.2, 2.1), (7.9, 2.1)],
            [(3.0, 3.0), (4.4, 4.2), (7.9, 4.2)],
            [(0.9, 4.9), (2.4, 4.9), (4.4, 4.2)],
            [(5.8, 2.1), (6.7, 3.2), (7.9, 3.2)]]
    for pts in nets:
        poly(gs, pts, None, "#5B636E", 3.0, closed=False, name="track")
    for (x, y) in [(3.0, 3.0), (4.2, 2.1), (4.4, 4.2), (6.7, 3.2), (5.8, 2.1)]:
        rect(gs, x - 0.1, y - 0.1, 0.2, 0.2, STEEL, None, name="station")
    dots = [(1.5, 3.0, 0), (2.3, 3.0, 1), (3.7, 2.55, 0), (5.2, 2.1, 1), (6.9, 2.1, 0), (3.7, 3.6, 0), (5.2, 4.2, 1),
            (7.0, 4.2, 0), (1.6, 4.9, 0), (6.3, 2.75, 0), (7.4, 3.2, 0), (2.1, 4.9, 0)]
    for (x, y, m) in dots:
        if m:
            oval(gs, x - 0.18, y - 0.18, 0.36, 0.36, ORANGE, TEXT, 2.0, name="match dot")
        else:
            oval(gs, x - 0.11, y - 0.11, 0.22, 0.22, "#444B55", None, name="dim dot")
    label(gs, 0.8, 5.1, 2.0, 0.3, "Example only", 14, MUTED, align="l", name="example label")
    # search boxes
    for k, (q, kind) in enumerate([("9F", "Class"), ("92214", "Number")]):
        y = 1.5 + k * 0.82
        rect(gs, 8.5, y, 4.23, 0.7, PANEL_ALT, ORANGE if k == 0 else STEEL, 2.5 if k == 0 else 1.5, radius=0.1,
             name="search box")
        magnifier(gs, 8.7, y + 0.15, 0.4, TEXT, 2.5)
        label(gs, 9.3, y, 1.9, 0.7, q, 24, TEXT, True, align="l", name="search text")
        label(gs, 11.2, y, 1.4, 0.7, kind, 14, MUTED, align="r", name="search kind")
    label(gs, 8.5, 3.3, 4.23, 0.4, "Matches only", 18, TEXT, True, align="l", name="list heading")
    for k in range(3):
        y = 3.75 + k * 0.58
        rect(gs, 8.5, y, 4.23, 0.5, PANEL, LINE, 1.0, radius=0.06, name="list row")
        oval(gs, 8.68, y + 0.14, 0.22, 0.22, ORANGE, None, name="match marker")
        skel(gs, 9.15, y + 0.19, 1.9 - k * 0.2, 0.12, LINE)
        skel(gs, 11.4, y + 0.19, 0.9, 0.12, LINE)
    right_chip(sh, "Undecided", "Screens: undecided (OQ30)", 12.73, 5.62)
    finish(s, "Type a number or a class. Matches stand out on the map.", 21)
    return s


# ---------------------------------------------------------------- slide 22
def s22(prs):
    s = new_slide(prs, "Researched, not copied", "Agreed")
    sh = s.shapes
    g = group(sh, "Each region researched on its own",
              "Three region cards, each with a magnifying glass and the words Own rules. Crossed arrows from the "
              "British card to the other two cards show that British rules are not reused elsewhere.")
    gs = g.shapes
    xs = [0.6, 4.78, 8.96]
    PW = 3.77
    for x, t in zip(xs, ["British", "North American", "Continental European"]):
        rect(gs, x, 2.95, PW, 2.75, PANEL, LINE, 1.5, radius=0.1, name="region card")
        label(gs, x, 3.05, PW, 0.5, t, 20, TEXT, True, name="region name")
        magnifier(gs, x + PW / 2 - 0.5, 3.65, 1.0, ORANGE, 5)
        label(gs, x, 4.95, PW, 0.5, "Own rules", 20, TEXT, True, name="own rules")
    c0 = xs[0] + PW / 2
    # arrow to North American (inner), arrow to Continental European (outer)
    path(gs, [(c0 + 0.8, 2.92), (c0 + 0.8, 2.4), (xs[1] + PW / 2, 2.4), (xs[1] + PW / 2, 2.9)], ORANGE, 3.0, True,
         name="blocked arrow")
    path(gs, [(c0 - 0.8, 2.92), (c0 - 0.8, 1.8), (xs[2] + PW / 2, 1.8), (xs[2] + PW / 2, 2.9)], ORANGE, 3.0, True,
         name="blocked arrow")
    for cx, cy in (((c0 + 0.8 + xs[1] + PW / 2) / 2, 2.4), ((c0 - 0.8 + xs[2] + PW / 2) / 2, 1.8)):
        oval(gs, cx - 0.3, cy - 0.3, 0.6, 0.6, BG, RED, 3.0, name="cross disc")
        cross(gs, cx, cy, 0.3, RED, 5)
    label(gs, 7.7, 1.33, 2.2, 0.34, "Not reused", 14, TEXT, True, align="l", name="blocked label")
    finish(s, "Each region's numbering is researched on its own. British rules are not reused elsewhere.", 22)
    return s


# ---------------------------------------------------------------- slide 23
def s23(prs):
    s = new_slide(prs, "A note on the build card", "Proposed")
    sh = s.shapes
    g = group(sh, "Mock build card with a numbering note",
              "A mock build card with a picture of an engine, placeholder text lines and a small secondary line "
              "that reads Numbering note, example only. The note is a suggestion.")
    gs = g.shapes
    rect(gs, 3.4, 1.55, 6.5, 4.1, PANEL, LINE, 1.75, radius=0.12, name="build card")
    rect(gs, 3.7, 1.85, 2.0, 1.6, COAL, LINE, 1.5, radius=0.08, name="card picture")
    rect(gs, 3.8, 3.1, 1.8, 0.04, STEEL, None, name="rail")
    engine(gs, 3.95, 3.1, 0.09, "tank", 1, ORANGE)
    skel(gs, 6.0, 1.95, 3.5, 0.26, LINE, "title bar")
    for k in range(4):
        skel(gs, 6.0, 2.5 + k * 0.24, 3.5 - (k % 2) * 0.8, 0.12, "#3A3F47")
    line(gs, 3.7, 3.75, 9.6, 3.75, LINE, 1.5, name="divider")
    rect(gs, 3.7, 3.95, 5.9, 0.85, PANEL_ALT, None, radius=0.06, name="note inset")
    rect(gs, 3.7, 3.95, 0.09, 0.85, PURPLE, None, name="note rule")
    label(gs, 3.95, 3.95, 3.7, 0.85, "Numbering note (example only)", 16, TEXT, False, align="l", name="note text")
    skel(gs, 3.7, 5.05, 2.6, 0.12, "#3A3F47")
    skel(gs, 3.7, 5.3, 1.8, 0.12, "#3A3F47")
    ichip(sh, "Proposed", 7.75, 4.2, "PROPOSED", w=1.6, h=0.34)
    finish(s, "A build card could show a short note on how the class was numbered.", 23)
    return s


# ---------------------------------------------------------------- slide 24
def s24(prs):
    s = new_slide(prs, "Where this stands", "Provisional")
    sh = s.shapes
    add_picture_fit(sh, "R01_pannier_visual_probe_v004.jpg", 0.6, 1.45, 2.4, 1.35,
                    "Early test model of a tank engine (a yellow 'visual probe') on a short length of track. "
                    "Not final art.", focus=(0.5, 0.5))
    credit(sh, 0.6, 2.84, 3.6, "Early test model, not final art.")
    g = group(sh, "Four planned steps",
              "A row of four steps. A test engine on the game's rails is under way. Regional styles, running "
              "numbers and fleet search are planned.")
    gs = g.shapes
    xs = [0.6, 3.69, 6.78, 9.87]
    PW = 2.85
    line(gs, 1.5, 3.6, 12.3, 3.6, LINE, 3.0, name="timeline")
    steps = [("Test engine on the game's rails", "Under way"), ("Regional styles", "Planned"),
             ("Running numbers", "Planned"), ("Fleet search", "Planned")]
    for k, (x, (t, st)) in enumerate(zip(xs, steps)):
        cx = x + PW / 2
        on = st == "Under way"
        oval(gs, cx - 0.2, 3.4, 0.4, 0.4, ORANGE if on else BG, ORANGE if on else STEEL, 3.0, name="step dot")
        rect(gs, x, 4.0, PW, 1.95, PANEL, ORANGE if on else LINE, 2.5 if on else 1.5, radius=0.1, name="step card")
        label(gs, x + 0.15, 4.1, PW - 0.3, 1.1, t, 18, TEXT, True, align="l", anchor="t", name="step title")
        rect(gs, x + 0.15, 5.4, 1.5, 0.4, ORANGE if on else LINE, None, radius=0.2, name="state pill", text=st,
             size=14, color=DARK if on else TEXT, bold=True)
    right_chip(sh, "Provisional", "Plans can change.", 12.73, 1.6)
    finish(s, "Regions and numbering are planned. They are not built yet.", 24)
    return s


# ---------------------------------------------------------------- slide 25
def s25(prs):
    s = new_slide(prs, "Still undecided", "Undecided")
    sh = s.shapes
    g = group(sh, "Eight open questions",
              "Eight cards, each with an Undecided tag and an open-question code. They ask which regions launch, "
              "which engine leads, what happens to running trains after a switch, where IDs are stored, how number "
              "pools and overflow numbers work, what renumbering costs and which search screens exist. "
              "Nothing is chosen.")
    gs = g.shapes
    qs = [("Which regions at launch?", "OQ06"), ("Which engine leads?", "OQ06, OQ27"),
          ("Running trains after a switch", "OQ06"), ("Where IDs are stored", "OQ28"),
          ("Number pools and data", "OQ29"), ("Overflow number format", "OQ29"),
          ("Renumber cost and screens", "OQ30"), ("Search and filter screens", "OQ30")]
    CW, GAP = 2.9, 0.1767
    for k, (q, code) in enumerate(qs):
        x = 0.6 + (k % 4) * (CW + GAP)
        y = 1.5 + (k // 4) * 2.2
        rect(gs, x, y, CW, 2.0, PANEL, LINE, 1.5, radius=0.1, name="question card")
        chip(gs, "Undecided", x + 0.1, y + 0.12, CW - 0.2, 0.36, 14, "UNDECIDED · " + code, name="CHIP CARD")
        label(gs, x + 0.15, y + 0.6, CW - 0.3, 1.3, q, 20, TEXT, True, align="l", anchor="t", name="question")
    finish(s, "These questions are open. Nothing here has been chosen yet.", 25)
    return s


# ---------------------------------------------------------------- slide 26
def s26(prs):
    s = new_slide(prs, "Image credits", None)
    sh = s.shapes
    gf, tbl = add_table(sh, 0.6, 1.5, 12.13, 1.6, 2, 4, [1.0, 1.2, 5.6, 4.33],
                        "Credits table: one mod render, R01, used on slides 1 and 24.")
    heads = ["Slot", "Slides", "What it shows", "Credit"]
    for c, h in enumerate(heads):
        set_cell(tbl.cell(0, c), h, 11, TEXT, True, PANEL_ALT)
    row = ["R01", "1, 24",
           "Early test model of a tank engine (a yellow 'visual probe') on a short length of track. Not final art.",
           "Early Locomotion project (test model, not final art)."]
    for c, v in enumerate(row):
        set_cell(tbl.cell(1, c), v, 11, TEXT, False, PANEL)
    tbl.rows[0].height = I(0.45)
    tbl.rows[1].height = I(1.0)
    label(sh, 0.6, 3.4, 12.13, 0.6,
          "Engine, wagon and station drawings in this deck are generic example silhouettes made from shapes. "
          "They are not the mod's models.", 14, MUTED, align="l", anchor="t", name="drawing note")
    finish(s, "This deck uses no photographs.", 26)
    return s


SLIDES = [s19, s20, s21, s22, s23, s24, s25, s26]
