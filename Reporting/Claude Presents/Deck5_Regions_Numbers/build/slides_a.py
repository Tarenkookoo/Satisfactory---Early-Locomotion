"""Chunk 1: slides 1 to 9."""
from lib import *


def right_chip(sh, kind, text, right, y, **kw):
    w = text_w(text, 14, True) + 0.34
    return ichip(sh, kind, right - w, y, text, w=w, **kw)


# ---------------------------------------------------------------- slide 1
def s01(prs):
    s = new_slide(prs, "Regions, Running Numbers and Fleet Identity", None, title_size=54,
                  title_box=(0.6, 0.55, 6.95, 3.2))
    s.shapes.title.text_frame.vertical_anchor = MSO_ANCHOR.BOTTOM
    sh = s.shapes
    add_picture_fit(sh, "R01_pannier_visual_probe_v004.jpg", 7.8, 0.5, 4.93, 6.4,
                    "Early test model of a tank engine (a yellow 'visual probe') on a short length of track. "
                    "Not final art.", focus=(0.55, 0.5))
    credit(sh, 7.8, 6.96, 4.93, "Early Locomotion project render. Early test model, not final art.", h=0.22)
    rect(sh, 0.6, 3.95, 1.8, 0.08, ORANGE, None, name="orange rule")
    label(sh, 0.6, 4.25, 6.5, 1.3,
          "How the mod gives every engine a look, a number and a hidden identity.",
          20, TEXT, align="l", anchor="t", name="CAPTION", margins=(0, 0, 0, 0))
    return s


# ---------------------------------------------------------------- slide 2
def s02(prs):
    s = new_slide(prs, "How to read this guide", None)
    sh = s.shapes
    g = group(sh, "Tag legend", "Legend: five tags and what each means. Agreed is decided, Proposed is suggested, "
              "Provisional is a test number, Undecided is an open question, Background is a real-world fact.")
    gs = g.shapes
    rows = [("Agreed", "Decided."), ("Proposed", "Suggested, not confirmed."),
            ("Provisional", "A test number that may change."), ("Undecided", "Still an open question."),
            ("Background", "A real-world fact.")]
    rect(gs, 0.6, 1.5, 8.0, 4.45, PANEL, None, radius=0.08, name="legend panel")
    for i, (k, m) in enumerate(rows):
        y = 1.72 + i * 0.86
        chip(gs, k, 0.95, y, 1.7, 0.4, name="CHIP LEGEND")
        label(gs, 3.0, y - 0.1, 5.4, 0.6, m, 20, TEXT, align="l", name="LEGEND TEXT")
    sk = group(sh, "Corner sketch", "Sketch of a slide with a tag in its top-right corner.")
    ks = sk.shapes
    rect(ks, 9.2, 1.9, 3.5, 1.97, BG, STEEL, 2.0, radius=0.08, name="slide sketch")
    rect(ks, 9.45, 2.15, 1.5, 0.12, LINE, None, name="title line")
    rect(ks, 9.45, 2.5, 2.2, 0.08, LINE, None, name="body line")
    rect(ks, 9.45, 2.7, 1.8, 0.08, LINE, None, name="body line")
    rect(ks, 11.7, 2.1, 0.8, 0.26, GREEN, None, radius=0.08, name="tag sketch")
    arrow(ks, 11.0, 3.0, 11.9, 2.4, ORANGE, 2.25, name="pointer")
    finish(s, "Every idea carries a tag in the top-right corner.", 2)
    return s


# ---------------------------------------------------------------- slide 3
def s03(prs):
    s = new_slide(prs, "One world, one style", "Agreed")
    sh = s.shapes
    g = group(sh, "World card",
              "A world card with a selector offering three example regional styles: British, North American and "
              "Continental European. One style is chosen for the whole world.")
    gs = g.shapes
    rect(gs, 1.5, 1.55, 10.3, 3.45, PANEL, LINE, 1.5, radius=0.12, name="world card")
    globe(gs, 3.1, 3.3, 1.0)
    label(gs, 4.7, 1.75, 4.0, 0.4, "World style", 18, MUTED, True, align="l", name="card heading")
    for i, t in enumerate(["British", "North American", "Continental European"]):
        y = 2.25 + i * 0.78
        sel = i == 0
        rect(gs, 4.7, y, 4.9, 0.62, PANEL_ALT, ORANGE if sel else LINE, 3.0 if sel else 1.5, radius=0.31,
             name="style chip")
        oval(gs, 4.95, y + 0.16, 0.3, 0.3, ORANGE if sel else None, ORANGE if sel else STEEL, 2.0, name="radio")
        label(gs, 5.45, y, 3.9, 0.62, t, 20, TEXT, True, align="l", name="style name")
    label(gs, 4.7, 4.55, 3.0, 0.3, "Examples only", 14, MUTED, align="l", name="examples label")
    station_building(gs, 9.95, 4.15, 0.2, "gable", STYLE_A)
    ichip(sh, "Undecided", 1.5, 5.3, "Launch regions: undecided (OQ06)")
    finish(s, "The world picks one regional style. It is not a personal setting.", 3)
    return s


# ---------------------------------------------------------------- slide 4
def s04(prs):
    s = new_slide(prs, "Why not per player?", "Agreed")
    sh = s.shapes
    g = group(sh, "Two players, two styles",
              "Two player screens side by side. Each shows a different station style, and a red cross between "
              "them says this is not allowed.")
    gs = g.shapes
    for (mx, kind, col, who) in ((1.9, "gable", STYLE_A, "Player 1"), (7.55, "depot", STYLE_B, "Player 2")):
        ix, iy, iw, ih = monitor(gs, mx, 1.55, 3.9, 2.35)
        rect(gs, ix + 0.15, iy + ih - 0.5, iw - 0.3, 0.07, STEEL, None, name="rail")
        station_building(gs, ix + (iw - 8 * 0.24) / 2, iy + ih - 0.5, 0.24, kind, col)
        label(gs, mx, 4.28, 3.9, 0.36, who, 18, TEXT, True, name="player label")
    oval(gs, 6.2, 2.25, 0.95, 0.95, BG, RED, 3.0, name="cross disc")
    cross(gs, 6.675, 2.725, 0.48, RED, 8)
    g2 = group(sh, "One shared world style",
               "One shared world card with a single style for every player, marked with a tick.")
    cs = g2.shapes
    rect(cs, 3.4, 4.85, 6.5, 1.2, PANEL, GREEN, 2.0, radius=0.12, name="shared world card")
    globe(cs, 4.4, 5.45, 0.45)
    label(cs, 5.05, 4.85, 3.8, 1.2, "One shared world style", 20, TEXT, True, align="l", name="shared label")
    tick(cs, 9.1, 5.45, 0.5, GREEN, 6)
    finish(s, "Two players seeing different stations would be confusing. So the style belongs to the world.", 4)
    return s


# ---------------------------------------------------------------- slide 5
def s05(prs):
    s = new_slide(prs, "What changes with the region", "Agreed")
    sh = s.shapes
    g = group(sh, "Before and after strip",
              "A before and after strip. A station, an engine and a wagon each change their look when the region "
              "changes, and stock you already own changes too.")
    gs = g.shapes
    xs = [1.95, 5.6, 9.25]
    PW = 3.4
    for x, t in zip(xs, ["Station", "Engine", "Wagon"]):
        label(gs, x, 1.38, PW, 0.4, t, 18, TEXT, True, name="column heading")
    label(gs, 0.6, 1.9, 1.3, 1.55, "Before", 18, TEXT, True, align="l", name="row heading")
    label(gs, 0.6, 4.0, 1.3, 1.55, "After", 18, TEXT, True, align="l", name="row heading")
    for yy, after in ((1.9, False), (4.0, True)):
        col = STYLE_B if after else STYLE_A
        for x in xs:
            rect(gs, x, yy, PW, 1.55, PANEL, LINE, 1.5, radius=0.1, name="panel")
        gy = yy + 1.32
        for x in xs:
            rect(gs, x + 0.2, gy, PW - 0.4, 0.05, STEEL, None, name="rail")
        station_building(gs, xs[0] + (PW - 8 * 0.19) / 2, gy, 0.19, "depot" if after else "gable", col)
        est = 17.5 if after else 17.9
        info = engine(gs, xs[1] + (PW - est * 0.15) / 2, gy, 0.15, "american" if after else "tender", 2, col)
        wagon(gs, xs[2] + (PW - 4.4 * 0.3) / 2, gy, 0.3, "hopper" if after else "box", col)
    for x in xs:
        arrow(gs, x + PW / 2, 3.5, x + PW / 2, 3.97, ORANGE, 3.0, name="change arrow")
    right_chip(sh, "Undecided", "Not yet tested", 12.65, 5.72)
    finish(s, "Changing the region restyles stock you already own, not just new builds.", 5)
    return s


# ---------------------------------------------------------------- slide 6
def s06(prs):
    s = new_slide(prs, "Three sizes, many looks", "Agreed")
    sh = s.shapes
    g = group(sh, "Three by three engine grid",
              "A grid of nine example locomotive silhouettes. Rows are Small, Medium and Large. Columns are three "
              "example regional styles, and each style draws its engines in its own shape.")
    gs = g.shapes
    cx0, cw, gap = 2.2, 3.4, 0.1
    xs = [cx0 + i * (cw + gap) for i in range(3)]
    for x, t in zip(xs, ["British", "North American", "Continental European"]):
        rect(gs, x, 1.35, cw, 0.4, PANEL_ALT, LINE, 1.5, radius=0.2, name="region heading",
             text=t, size=18, color=TEXT, bold=True)
    label(gs, 0.6, 1.35, 1.55, 0.4, "Examples only", 14, MUTED, True, align="l", name="examples label")
    cols = [(STYLE_A, ["tank", "tender", "tender"], [None, None, None]),
            (STYLE_B, ["american"] * 3, [None] * 3),
            (STYLE_C, ["tank", "euro", "euro"], ["euro", None, None])]
    for ri, (rt, ry) in enumerate(zip(["Small", "Medium", "Large"], [1.85, 3.25, 4.65])):
        label(gs, 0.6, ry, 1.55, 1.32, rt, 20, TEXT, True, align="l", name="row heading")
        for ci, (col, styles, variants) in enumerate(cols):
            x = xs[ci]
            rect(gs, x, ry, cw, 1.32, PANEL, LINE, 1.5, radius=0.1, name="panel")
            gy = ry + 1.12
            rect(gs, x + 0.15, gy, cw - 0.3, 0.05, STEEL, None, name="rail")
            u = 0.145
            # width is known only after drawing; estimate by style/size for centring
            est = {"tank": [11.4, 13.4, 15.4], "tender": [15.6, 17.9, 20.2], "american": [15.1, 17.5, 20.3],
                   "euro": [15.6, 17.9, 20.2]}[styles[ri]][ri]
            engine(gs, x + (cw - est * u) / 2, gy, u, styles[ri], ri + 1, col, variant=variants[ri])
    finish(s, "Every style gets a Small, a Medium and a Large. Each engine looks and behaves in its own way.", 6)
    return s


# ---------------------------------------------------------------- slide 7
def s07(prs):
    s = new_slide(prs, "Different engines, same rules", "Agreed")
    sh = s.shapes
    g = group(sh, "Engines plugging into shared rules",
              "Three differently shaped example engines. Each has its own data card and plugs into one bar "
              "labelled Shared rules.")
    gs = g.shapes
    u = 0.185
    gy = 3.3
    centres = [2.7, 6.67, 10.64]
    specs = [("tender", STYLE_A), ("american", STYLE_B), ("euro", STYLE_C)]
    for cx, (st, col) in zip(centres, specs):
        est = {"tender": 17.9, "american": 17.5, "euro": 17.9}[st]
        rect(gs, cx - 1.9, gy, 3.8, 0.05, STEEL, None, name="rail")
        engine(gs, cx - est * u / 2, gy, u, st, 2, col)
        rect(gs, cx - 1.15, 3.65, 2.3, 0.62, PANEL_ALT, ORANGE, 2.0, radius=0.08, name="data card")
        rect(gs, cx - 1.0, 3.8, 0.3, 0.32, TEXT, None, radius=0.03, name="card icon")
        for k in range(3):
            rect(gs, cx - 0.94, 3.86 + k * 0.08, 0.18, 0.03, LINE, None, name="card icon line")
        label(gs, cx - 0.62, 3.65, 1.75, 0.62, "Own data card", 14, TEXT, True, align="l", name="card label")
        line(gs, cx, 4.27, cx, 4.78, STEEL, 2.5, name="plug lead")
        rect(gs, cx - 0.2, 4.7, 0.4, 0.28, ORANGE, None, radius=0.04, name="plug head")
        rect(gs, cx - 0.1, 4.98, 0.06, 0.14, ORANGE, None, name="plug prong")
        rect(gs, cx + 0.04, 4.98, 0.06, 0.14, ORANGE, None, name="plug prong")
    rect(gs, 0.9, 4.98, 11.5, 0.85, PANEL_ALT, ORANGE, 2.5, radius=0.1, name="shared rules bar",
         text="Shared rules", size=24, color=TEXT, bold=True, anchor="m", margins=(0.1, 0.1, 0.1, 0.0))
    finish(s, "The code is shared. The engines are not. Each model keeps its own wheels and shape.", 7)
    return s


# ---------------------------------------------------------------- slide 8
def power_symbol(sh, cx, base_y, k, col=STEEL):
    """Steam cylinder with a piston rod and three steam puffs; k scales it (height about 1.1 k)."""
    w, h = 1.5 * k, 0.5 * k
    rect(sh, cx - w / 2, base_y - h, w, h, col, None, radius=0.08 * k, name="cylinder")
    rect(sh, cx - w / 2 - 0.38 * k, base_y - h * 0.62, 0.38 * k, 0.14 * k, TEXT, None, name="piston rod")
    rect(sh, cx - w / 2 - 0.46 * k, base_y - h * 0.82, 0.1 * k, 0.34 * k, TEXT, None, name="piston crosshead")
    for dx, dy, d in [(-0.38, 0.08, 0.42), (0.02, 0.24, 0.5), (0.42, 0.1, 0.4)]:
        oval(sh, cx + (dx - d / 2) * k, base_y - h - (dy + d * 0.7) * k, d * k, d * 0.7 * k, TEXT, None,
             alpha=0.85, name="steam puff")


def s08(prs):
    s = new_slide(prs, "Weight and power differ", "Agreed")
    sh = s.shapes
    g = group(sh, "Two balanced scales",
              "Two balance scales, both level. On the first, a heavy engine with heavy wagons balances more power. "
              "On the second, a lighter engine with light wagons balances less power. Illustration only.")
    gs = g.shapes
    cx = 6.67
    rows = [
        dict(top=1.4, train=("american", 3, STYLE_B, 0.11, "hopper", 0.11), pk=1.0,
             lt="Heavy engine, heavy wagons", rt="More power"),
        dict(top=3.55, train=("tender", 1, STYLE_A, 0.095, "flat", 0.095), pk=0.6,
             lt="Lighter engine, light wagons", rt="Less power"),
    ]
    for r in rows:
        a = scale(gs, cx, r["top"], 6.5, post_h=1.55, ph=1.35, pan_half=1.8)
        (lx, ly), (rx, ry) = a
        st, size, col, eu, wst, wu = r["train"]
        est = {"american": {3: 20.3}, "tender": {1: 15.6}}[st][size]
        wl = 4.4 * wu
        total = est * eu + 2 * (wl + 0.05) + 0.05
        x0 = lx - total / 2
        wagon(gs, x0, ly, wu, wst, col)
        wagon(gs, x0 + wl + 0.05, ly, wu, wst, col)
        engine(gs, x0 + 2 * (wl + 0.05) + 0.05, ly, eu, st, size, col)
        power_symbol(gs, rx, ry, r["pk"])
        label(gs, lx - 1.8, ly + 0.2, 3.6, 0.36, r["lt"], 18, TEXT, True, name="pan label")
        label(gs, rx - 1.8, ly + 0.2, 3.6, 0.36, r["rt"], 18, TEXT, True, name="pan label")
    label(gs, 2.0, 5.8, 9.3, 0.36, "Illustration only. No values chosen.", 18, MUTED, True, name="illustration note")
    finish(s, "Regions differ in weight and power. The aim is trains that are about equally useful.", 8)
    return s


# ---------------------------------------------------------------- slide 9
def s09(prs):
    s = new_slide(prs, "A consist follows its lead engine", "Agreed")
    sh = s.shapes
    g = group(sh, "Three mini trains",
              "Three examples. A British engine pulls British-styled wagons. A North American engine pulls "
              "North American-styled wagons. A lone wagon beside a station takes the world style. Style is shown by "
              "a colour band, a shape and a label.")
    gs = g.shapes
    rows = [1.4, 2.95, 4.5]
    RH = 1.5
    for ry in rows:
        rect(gs, 0.6, ry, 12.13, RH, PANEL, LINE, 1.5, radius=0.1, name="row panel")
    u = 0.15
    # row 1: British
    gy = rows[0] + 1.05
    x = 0.95
    wl = 4.4 * u
    for k in range(3):
        wagon(gs, x + k * (wl + 0.07), gy, u, "box", STYLE_A)
    ex = x + 3 * (wl + 0.07)
    info = engine(gs, ex, gy, u, "tender", 2, STYLE_A)
    end1 = ex + info["W"] * u
    rect(gs, x - 0.1, gy, end1 - x + 0.2, 0.05, STEEL, None, name="rail")
    rect(gs, x, gy + 0.1, end1 - x, 0.3, STYLE_A, None, radius=0.05, name="style band",
         text="British style", size=14, color=DARK, bold=True)
    line(gs, end1 + 0.55, rows[0] + 0.6, end1 + 0.15, rows[0] + 0.6, ORANGE, 2.5, tail=True, name="lead pointer")
    label(gs, end1 + 0.65, rows[0] + 0.4, 2.2, 0.4, "Lead engine", 18, TEXT, True, align="l", name="lead label")
    # row 2: North American
    gy = rows[1] + 1.05
    for k in range(3):
        wagon(gs, x + k * (wl + 0.07), gy, u, "hopper", STYLE_B)
    info = engine(gs, ex, gy, u, "american", 2, STYLE_B)
    end2 = ex + info["W"] * u
    rect(gs, x - 0.1, gy, end2 - x + 0.2, 0.05, STEEL, None, name="rail")
    rect(gs, x, gy + 0.1, end2 - x, 0.3, STYLE_B, None, radius=0.05, name="style band",
         text="North American style", size=14, color=DARK, bold=True)
    line(gs, end2 + 0.55, rows[1] + 0.6, end2 + 0.15, rows[1] + 0.6, ORANGE, 2.5, tail=True, name="lead pointer")
    label(gs, end2 + 0.65, rows[1] + 0.4, 2.2, 0.4, "Lead engine", 18, TEXT, True, align="l", name="lead label")
    # row 3: lone wagon beside a station in the world style
    gy = rows[2] + 1.05
    rect(gs, x - 0.1, gy, 2.0 + 4.4 * u + 0.2, 0.05, STEEL, None, name="rail")
    station_building(gs, x + 0.0, gy, 0.16, "gable", STYLE_C)
    wagon(gs, x + 2.0, gy, u, "flat", STYLE_C)
    rect(gs, x, gy + 0.1, 2.0 + 4.4 * u, 0.3, STYLE_C, None, radius=0.05, name="style band",
         text="World style", size=14, color=DARK, bold=True)
    label(gs, x + 2.0 + 4.4 * u + 0.3, rows[2] + 0.4, 2.4, 0.4, "Lone wagon", 18, TEXT, True, align="l",
          name="lone label")
    finish(s, "Wagons take the look of the engine pulling them. A lone wagon follows the world style.", 9)
    return s


SLIDES = [s01, s02, s03, s04, s05, s06, s07, s08, s09]
