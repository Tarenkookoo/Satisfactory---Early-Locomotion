"""Chunk 3: slides 17 to 24."""
import math

from lib import *
from lib import _ends
from slides_a import badge
from slides_b import drop_points


# --- small icons shared by several slides ------------------------------------------
def icon_drop(sh, cx, cy, h, fill=WATER):
    """Water drop about h tall centred at (cx, cy)."""
    r = h / 3.3
    pts = drop_points(cx, cy - h / 2, r)
    poly(sh, pts, fill, None, name="icon drop")


def icon_heap(sh, cx, cy, w, fill=COAL, line_color="#B5BBC2"):
    """Coal heap about w wide centred at (cx, cy)."""
    h = w * 0.55
    poly(sh, [(cx - w / 2, cy + h / 2), (cx - w * 0.28, cy - h * 0.1), (cx - w * 0.05, cy - h / 2),
              (cx + w * 0.2, cy - h * 0.2), (cx + w * 0.5, cy + h / 2)], fill, line_color, 2.0, name="icon heap")


def icon_tower(sh, cx, cy, w):
    rect(sh, cx - w / 2, cy - w * 0.5, w, w * 0.6, WATER, TEXT, 1.5, radius=0.06, name="icon tank")
    for dx in (-0.4, -0.15, 0.15, 0.4):
        rect(sh, cx + dx * w - 0.025, cy + w * 0.1, 0.05, w * 0.55, STEEL, None, name="icon leg")


def icon_stage(sh, cx, cy, w):
    icon_heap(sh, cx, cy - w * 0.2, w * 0.8)
    rect(sh, cx - w / 2, cy, w, 0.08, STEEL, None, name="icon platform")
    for dx in (-0.4, 0.4):
        rect(sh, cx + dx * w - 0.025, cy + 0.08, 0.05, w * 0.45, STEEL, None, name="icon post")


# ---------------------------------------------------------------- slide 17 (SPEC-I)
def s17(prs):
    s = new_slide(prs, "Service points", "Proposed")
    sh = s.shapes
    g = group(sh, "Facilities and route",
              "Four proposed facilities: Water Tower, Coaling Stage, Steam Service Point and Full Station. Below, a "
              "route from a mine to a factory with a water stop, then a water and coal stop, and a train at the "
              "water stop.")
    gs = g.shapes
    tiles = ["Water Tower", "Coaling Stage", "Steam Service Point", "Full Station"]
    for i, nm in enumerate(tiles):
        x = 0.6 + i * 3.11
        rect(gs, x, 1.5, 2.8, 2.4, PANEL, LINE, 1.5, radius=0.1, name="tile")
        cx, cy = x + 1.4, 2.4
        if i == 0:
            icon_tower(gs, cx, cy - 0.1, 0.85)
        elif i == 1:
            icon_stage(gs, cx, cy - 0.05, 1.0)
        elif i == 2:
            icon_drop(gs, cx - 0.4, cy, 0.8)
            icon_heap(gs, cx + 0.45, cy + 0.15, 0.85)
        else:
            rect(gs, x + 0.3, cy + 0.2, 2.2, 0.18, PANEL_ALT, STEEL, 1.5, name="icon platform")
            icon_drop(gs, x + 0.75, cy - 0.1, 0.6)
            icon_heap(gs, x + 1.45, cy + 0.05, 0.6)
            rect(gs, x + 1.9, cy - 0.15, 0.45, 0.35, PANEL_ALT, STEEL, 1.5, name="icon box")
        label(gs, x + 0.1, 3.0, 2.6, 0.4, nm, 18, TEXT, True, name="tile name")
        chip(gs, "Proposed", x + 0.7, 3.45, 1.4, 0.32, 14, name="ICHIP")
    # route
    ry = 5.0
    stops = [(1.6, "Mine", STEEL), (4.8, "Water stop", WATER), (8.2, "Water and coal stop", ORANGE),
             (11.5, "Factory", STEEL)]
    for (x0, _, _), (x1, _, _) in zip(stops[:-1], stops[1:]):
        arrow(gs, x0 + 0.22, ry, x1 - 0.24, ry, ORANGE, 3.5, name="route")
    for x, nm, col in stops:
        oval(gs, x - 0.2, ry - 0.2, 0.4, 0.4, col, DARK, 2.0, name="stop")
        label(gs, x - 1.3, ry + 0.3, 2.6, 0.4, nm, 18, TEXT, True, name="stop label")
    loco_icon(gs, 4.8 - 0.85, ry - 0.3 - 4.4 * 1.7 / 12, 1.7, "tender")
    finish(s, "Separate coal and water stops make long routes possible. Not every stop needs a full station.", 17,
           inline_chip="Agreed")
    return s


# ---------------------------------------------------------------- slide 18
def s18(prs):
    s = new_slide(prs, "Service stops in the timetable", "Proposed")
    sh = s.shapes
    g = group(sh, "Timetable card",
              "A timetable with three lines: mine, load; water tower, water only and leave when full; "
              "factory, unload. A side note says automatic servicing at any stop was mentioned but not chosen.")
    gs = g.shapes
    rect(gs, 0.6, 1.55, 7.3, 4.2, PANEL, LINE, 1.5, radius=0.1, name="timetable card")
    label(gs, 0.9, 1.7, 3.0, 0.5, "Timetable", 20, MUTED, True, align="l", name="card title")
    chip(gs, "Proposed", 6.3, 1.78, 1.4, 0.34, 14, name="ICHIP")
    rows = [("Mine: load", False), ("Water Tower: water only, leave when full", True), ("Factory: unload", False)]
    for i, (txt, hot) in enumerate(rows):
        y = 2.45 + i * 1.05
        rect(gs, 0.9, y, 6.7, 0.85, PANEL_ALT, ORANGE if hot else None, 2.25, radius=0.08, name="timetable row")
        badge(gs, 1.3, y + 0.425, i + 1, 0.5)
        label(gs, 1.7, y, 5.8, 0.85, txt, 20, TEXT, hot, align="l", name="timetable text")
    rect(gs, 8.4, 2.35, 4.33, 2.4, PANEL, LINE, 1.5, radius=0.1, name="side note card")
    label(gs, 8.65, 2.5, 3.85, 1.2, "Servicing at any stop, automatically: mentioned, not chosen", 18, TEXT,
          align="l", anchor="t", name="side note")
    chip(gs, "Undecided", 8.65, 3.95, 1.7, 0.4, 14, name="ICHIP")
    finish(s, "A timetable can include a water-only stop. The train leaves when full.", 18)
    return s


# ---------------------------------------------------------------- slide 19
def downside_icons(gs, x, y):
    # crate with a red strike
    rect(gs, x, y + 0.05, 0.6, 0.5, PANEL_ALT, STEEL, 2.0, name="crate")
    line(gs, x, y + 0.55, x + 0.6, y + 0.05, RED, 3.5, name="strike")
    # weight
    poly(gs, [(x + 2.35, y + 0.55), (x + 2.45, y + 0.2), (x + 2.85, y + 0.2), (x + 2.95, y + 0.55)], STEEL, None,
         name="weight")
    oval(gs, x + 2.52, y + 0.04, 0.26, 0.26, None, STEEL, 3.0, name="weight ring")


def s19(prs):
    s = new_slide(prs, "Tenders", "Agreed")
    sh = s.shapes
    add_picture_fit(sh, "P18_lms_tender.jpg", 0.6, 4.12, 3.4, 1.68,
                    "A detached LMS tender at Norton Fitzwarren. Comparison only: not any particular engine's tender.",
                    focus=(0.5, 0.5))
    credit(sh, 0.6, 5.84, 3.4, "A real tender, for illustration. Geof Sheppard, CC BY-SA 4.0.", h=0.34)
    g = group(sh, "Train strip",
              "A train strip. An engine and its normal tender are joined as one vehicle. Next comes a hatched "
              "auxiliary tender, which is a separate wagon, then three cargo wagons. The auxiliary tender "
              "carries no freight and adds weight.")
    gs = g.shapes
    u = 0.38
    ty = 2.3
    rail_y = ty + 4.4 * u
    rect(gs, 0.6, rail_y, 12.13, 0.07, STEEL, None, name="rail")
    loco_icon(gs, 0.7, ty, 12 * u, "tender")
    ax = 0.7 + 12 * u + 0.3
    wagon_icon(gs, ax, ty, u, hatched=True, length=5.0)
    wx = ax + 5.0 * u + 0.15
    for k in range(3):
        wagon_icon(gs, wx + k * (3.8 * u + 0.1), ty, u, length=3.8)
    # bracket and label
    bx0, bx1 = 0.7, 0.7 + 12 * u
    poly(gs, [(bx0, 2.2), (bx0, 2.05), (bx1, 2.05), (bx1, 2.2)], None, STEEL, 2.25, closed=False, name="bracket")
    label(gs, 1.9, 1.5, 1.8, 0.45, "One vehicle", 18, TEXT, True, name="bracket label")
    chip(gs, "Proposed", 3.75, 1.56, 1.4, 0.32, 14, name="ICHIP")
    # under the hatched wagon
    cx = ax + 2.5 * u
    label(gs, cx - 1.7, rail_y + 0.18, 3.4, 0.7, "Auxiliary tender: a separate wagon", 16, TEXT, True,
          name="aux label")
    chip(gs, "Proposed", cx - 1.7, rail_y + 0.98, 1.55, 0.32, 14, "Water only", name="ICHIP TEXT")
    chip(gs, "Proposed", cx - 0.05, rail_y + 0.98, 1.75, 0.32, 14, "Coal and water", name="ICHIP TEXT")
    # downsides
    downside_icons(gs, 9.0, 4.3)
    label(gs, 8.45, 5.0, 1.7, 0.7, "Carries no freight", 16, TEXT, True, name="downside label")
    label(gs, 10.8, 5.0, 1.7, 0.7, "Adds weight", 16, TEXT, True, name="downside label")
    finish(s, "A normal tender belongs to the engine. An auxiliary tender is an extra wagon: more range, less "
              "pulling power.", 19)
    return s


# ---------------------------------------------------------------- slide 20
def s20(prs):
    s = new_slide(prs, "Who gains from a tender?", "Agreed")
    sh = s.shapes
    g = group(sh, "Three class cards",
              "Three cards for Small, Medium and Large. Each shows a locomotive with a hatched auxiliary tender "
              "behind it, and a one-line verdict.")
    gs = g.shapes
    cards = [("Small", "tank", "Extra weight worsens its main weakness"),
             ("Medium", "tender", "Attractive on longer work"),
             ("Large", "tender", "For especially long journeys")]
    u = 0.2
    for i, (nm, kind, verdict) in enumerate(cards):
        x = 0.6 + i * 4.165
        rect(gs, x, 1.55, 3.8, 3.55, PANEL, LINE, 1.5, radius=0.1, name="class card")
        rect(gs, x, 1.55, 3.8, 0.6, PANEL_ALT, None, radius=0.1, name="card header")
        label(gs, x + 0.2, 1.55, 3.4, 0.6, nm, 22, ORANGE, True, align="l", name="class name")
        ly = 2.65
        W = 12 if kind == "tender" else 10
        loco_icon(gs, x + 0.2, ly, W * u, kind)
        wagon_icon(gs, x + 0.2 + W * u + 0.08, ly, u, hatched=True, length=5.0)
        rect(gs, x + 0.1, ly + 4.4 * u, 3.6, 0.06, STEEL, None, name="rail")
        label(gs, x + 0.2, 3.85, 3.4, 1.15, verdict, 20, TEXT, align="l", anchor="t", name="verdict")
    label(gs, 0.6, 5.4, 12.13, 0.45, "Which types at launch: undecided (OQ10).", 18, MUTED, align="c",
          name="footer")
    finish(s, "Small can take one, but the weight hurts. Medium gains most. Large uses one for very long trips.", 20)
    return s


# ---------------------------------------------------------------- slide 21
def s21(prs):
    s = new_slide(prs, "Four ways to go further", "Agreed")
    sh = s.shapes
    g = group(sh, "Route and four answers",
              "A route that is too long for one engine's range, shown with a red dashed gap. Below, four answers: "
              "add an auxiliary tender, add a water stop, build a service point, or pick a bigger engine.")
    gs = g.shapes
    ry = 2.75
    arrow(gs, 1.6, ry, 5.7, ry, ORANGE, 5.0, name="route in range")
    line(gs, 5.7, ry, 11.9, ry, RED, 5.0, dash=MSO_LINE.DASH, name="route gap")
    line(gs, 5.7, ry - 0.25, 5.7, ry + 0.25, ORANGE, 4.0, name="range end")
    oval(gs, 11.9, ry - 0.22, 0.44, 0.44, STEEL, DARK, 2.0, name="destination")
    loco_icon(gs, 0.8, ry - 0.12 - 4.4 * 1.5 / 12, 1.5, "tender")
    rect(gs, 7.2, ry - 0.62, 1.7, 0.4, RED, None, radius=0.1, name="gap tag", text="Too far", size=18, color=DARK,
         bold=True)
    answers = ["Auxiliary tender", "Water stop", "Service point", "Bigger engine"]
    for i, nm in enumerate(answers):
        x = 0.6 + i * 3.11
        rect(gs, x, 3.55, 2.8, 2.2, ORANGE, None, radius=0.1, name="answer card")
        cx, cy = x + 1.4, 4.4
        if i == 0:
            hatch_rect(gs, cx - 0.8, cy - 0.3, 1.6, 0.6, DARK, ORANGE, DARK, 2.0, name="icon aux tender")
        elif i == 1:
            icon_drop(gs, cx, cy, 0.9, DARK)
        elif i == 2:
            icon_drop(gs, cx - 0.4, cy, 0.8, DARK)
            icon_heap(gs, cx + 0.45, cy + 0.15, 0.85, DARK, DARK)
        else:
            base = cy + 0.3
            loco_icon(gs, cx - 1.15, base - 4.4 * 0.8 / 10, 0.8, "tank", DARK)
            loco_icon(gs, cx - 0.2, base - 4.4 * 1.35 / 12, 1.35, "tender", DARK)
        label(gs, x + 0.1, 5.0, 2.6, 0.5, nm, 20, DARK, True, name="answer label")
    finish(s, "Add a tender. Add a water stop. Build a service point. Or pick a bigger engine.", 21)
    return s


# ---------------------------------------------------------------- slide 22
def s22(prs):
    s = new_slide(prs, "Where this stands", "Provisional")
    sh = s.shapes
    add_picture_fit(sh, "R01_pannier_visual_probe_v004.jpg", 0.6, 1.5, 2.4, 1.35,
                    "Early test model of a tank engine (a yellow 'visual probe') on a short length of track. "
                    "Not final art.")
    credit(sh, 0.6, 2.88, 2.6, "Early test model, not final art.")
    g = group(sh, "Five steps",
              "Five steps in a row. Test engine on the game's rails is under way. Coal and water, station "
              "servicing, service points and tenders are planned.")
    gs = g.shapes
    steps = [("Test engine on the game's rails", "Under way"), ("Coal and water", "Planned"),
             ("Station servicing", "Planned"), ("Service points", "Planned"), ("Tenders", "Planned")]
    cw, gap = 2.29, 0.17
    my = 3.45
    line(gs, 0.6 + cw / 2, my, 0.6 + 4 * (cw + gap) + cw / 2, my, LINE, 3.0, name="step line")
    for i, (nm, st) in enumerate(steps):
        x = 0.6 + i * (cw + gap)
        on = i == 0
        oval(gs, x + cw / 2 - 0.25, my - 0.25, 0.5, 0.5, ORANGE if on else BG, ORANGE if on else MUTED, 2.5,
             name="step marker")
        rect(gs, x, 3.9, cw, 1.6, PANEL, ORANGE if on else LINE, 2.0 if on else 1.0, radius=0.1, name="step card",
             text=[[(nm, {"size": 18, "bold": False})],
                   [(st, {"size": 18, "bold": True, "color": ORANGE if on else MUTED})]],
             anchor="t", margins=(0.15, 0.15, 0.1, 0.1), align="l")
    chip(gs, "Provisional", 10.1, 1.95, 2.6, 0.45, 14, "Plans can change.", name="ICHIP TEXT")
    finish(s, "Coal, water and servicing are planned. They are not built yet.", 22)
    return s


# ---------------------------------------------------------------- slide 23
def s23(prs):
    s = new_slide(prs, "Still undecided", "Undecided")
    sh = s.shapes
    g = group(sh, "Eight open questions",
              "Eight cards, each marked undecided, with an open question and its open-question number. "
              "No answers are given.")
    gs = g.shapes
    qs = [("Which fuels work?", "OQ08"), ("What happens when supplies run out?", "OQ08"),
          ("Station buffers and transfer rates", "OQ08"), ("Station size and reach", "OQ09"),
          ("Two engines at one station", "OQ09"), ("Tender types and rules", "OQ10"),
          ("Which service buildings?", "OQ11"), ("Timetable controls for service stops", "OQ11")]
    cw, ch, gx = 2.9, 1.75, 0.18
    for i, (q, code) in enumerate(qs):
        r, c = divmod(i, 4)
        x = 0.6 + c * (cw + gx)
        y = 1.65 + r * (ch + 0.3)
        rect(gs, x, y, cw, ch, PANEL, LINE, 1.0, radius=0.1, name="question card")
        chip(gs, "Undecided", x + 0.15, y + 0.15, 2.5, 0.34, 14, "UNDECIDED · " + code, name="ICHIP")
        label(gs, x + 0.15, y + 0.6, cw - 0.3, ch - 0.7, q, 18, TEXT, align="l", anchor="t", name="question")
    finish(s, "These questions are open. Nothing here has been chosen yet.", 23)
    return s


# ---------------------------------------------------------------- slide 24
CREDITS = [
    ("P04", "5", "www.mgaylard.co.uk, CC BY 2.0",
     "https://commons.wikimedia.org/wiki/File:73082_Camelot_British_Railways_Standard_Class_5_4-6-0_-_54304789041.jpg"),
    ("P05", "5", "www.mgaylard.co.uk, CC BY 2.0",
     "https://commons.wikimedia.org/wiki/File:British_Railways_Standard_Class_4MT_2-6-4_Tank_Locomotive_No._80151_-_54303345950.jpg"),
    ("P06", "6", "Barry Skeates, CC BY 2.0",
     "https://commons.wikimedia.org/wiki/File:Didcot_Railway_Centre_Water_(4714616590).jpg"),
    ("P07", "6", "David Merrett, CC BY 2.0",
     "https://commons.wikimedia.org/wiki/File:Signal_and_Water_Tower_(3715807921).jpg"),
    ("P08", "7", "Gillett's Crossing, CC BY 2.0",
     "https://commons.wikimedia.org/wiki/File:Coaling_stage,_GWS_Didcot-9940117084.jpg"),
    ("P09", "7", "kitmasterbloke, CC BY 4.0",
     "https://commons.wikimedia.org/wiki/File:Carnforth_Ash_plant,_water_tower_and_Cenotaph_coaling_tower.jpg"),
    ("P17", "1, 12", "Rosser1954, CC BY-SA 4.0",
     "https://commons.wikimedia.org/wiki/File:Coal_stage_and_water_tank,_Didcot_Railway_Centre,_England.jpg"),
    ("P18", "19", "Geof Sheppard, CC BY-SA 4.0",
     "https://commons.wikimedia.org/wiki/File:Norton_Fitzwarren_-_LMS_tender.JPG"),
]


def s24(prs):
    s = new_slide(prs, "Image credits", None)
    sh = s.shapes
    rows = len(CREDITS) + 2
    rh = 0.38
    gf, tbl = add_table(sh, 0.6, 1.45, 12.13, rh * rows, rows, 4, [1.0, 1.3, 7.4, 2.43],
                        "Table of image credits: slot, slide, author and licence, and a link to the source on "
                        "Wikimedia Commons. The final row credits the mod render on slide 22.")
    for r in tbl.rows:
        r.height = I(rh)
    for j, h in enumerate(("Slot", "Slide", "Author and licence", "Source link")):
        set_cell(tbl.cell(0, j), h, 11, TEXT, True, PANEL_ALT, "l")
    for i, (slot, sl, who, url) in enumerate(CREDITS, 1):
        fill = PANEL if i % 2 else BG
        set_cell(tbl.cell(i, 0), slot, 11, ORANGE, True, fill)
        set_cell(tbl.cell(i, 1), sl, 11, TEXT, False, fill)
        set_cell(tbl.cell(i, 2), who, 11, TEXT, False, fill)
        set_cell(tbl.cell(i, 3), [[("Commons", {"link": url, "color": "#8FC7FF"})]], 11, TEXT, False, fill)
    i = len(CREDITS) + 1
    fill = PANEL if i % 2 else BG
    set_cell(tbl.cell(i, 0), "R01", 11, ORANGE, True, fill)
    set_cell(tbl.cell(i, 1), "22", 11, TEXT, False, fill)
    set_cell(tbl.cell(i, 2), "Early Locomotion project (test model, not final art).", 11, TEXT, False, fill)
    set_cell(tbl.cell(i, 3), "Project render", 11, TEXT, False, fill)
    label(sh, 0.6, 1.45 + rh * rows + 0.2, 12.13, 0.4, "CC BY-SA photos are shown unmodified except for resizing.", 14,
          MUTED, align="l", name="credit note")
    finish(s, "Photographs come from Wikimedia Commons under Creative Commons licences.", 24)
    return s


SLIDES = [s17, s18, s19, s20, s21, s22, s23, s24]
