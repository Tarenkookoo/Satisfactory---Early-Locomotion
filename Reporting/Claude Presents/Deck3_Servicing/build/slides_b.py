"""Chunk 2: slides 9 to 16."""
import math

from lib import *
from lib import _ends
from slides_a import badge, dot


def crosshair(sh, cx, cy, d=0.34, color=TEXT):
    """Target mark: white ring and cross over a dark halo, so it shows on orange, grey or dark."""
    for col, w in ((DARK, 6.0), (color, 2.5)):
        oval(sh, cx - d / 2, cy - d / 2, d, d, None, col, w, name="crosshair ring")
        line(sh, cx - d * 0.8, cy, cx + d * 0.8, cy, col, w * 0.8, name="crosshair")
        line(sh, cx, cy - d * 0.8, cx, cy + d * 0.8, col, w * 0.8, name="crosshair")


def time_bars(sh, x, y_short, y_long, track=6.0, bh=0.4, label_gap=0.12, labels=True):
    """Two qualitative time bars: a short top-up and a long refill from empty."""
    for yy, frac, txt in ((y_short, 0.26, "Small top-up"), (y_long, 0.94, "Empty tanks")):
        rect(sh, x, yy, track, bh, PANEL_ALT, LINE, 1.0, radius=0.06, name="time track")
        rect(sh, x, yy, track * frac, bh, ORANGE, None, radius=0.06, name="time fill")
        if labels:
            label(sh, x, yy - 0.45, track, 0.4, txt, 18, TEXT, True, align="l", name="bar label")


# ---------------------------------------------------------------- slide 9
def s09(prs):
    s = new_slide(prs, "What makes an engine burn more", "Agreed")
    sh = s.shapes
    g = group(sh, "Hill profile and fuel use",
              "A hill with an engine climbing, running flat and rolling downhill. Under each, a bar shows fuel use: "
              "high while climbing, medium when steady, low when coasting.")
    gs = g.shapes
    prof = [(0.7, 3.75), (2.0, 3.75), (5.0, 2.35), (8.2, 2.35), (11.2, 3.75), (12.6, 3.75)]
    poly(gs, prof + [(12.6, 4.2), (0.7, 4.2)], PANEL, None, name="hill ground")
    poly(gs, prof, None, STEEL, 3.0, closed=False, name="hill line")
    W = 1.9
    th = math.atan(1.4 / 3.0)
    # (x on the line, y on the line, rotation in degrees, up-normal)
    spots = [
        (3.5, 3.75 - (3.5 - 2.0) * 1.4 / 3.0, -math.degrees(th), (-math.sin(th), -math.cos(th))),
        (6.6, 2.35, 0.0, (0.0, -1.0)),
        (9.7, 2.35 + (9.7 - 8.2) * 1.4 / 3.0, math.degrees(th), (math.sin(th), -math.cos(th))),
    ]
    H = 4.4 * W / 12.0
    for (lx, ly, rot, nrm) in spots:
        cx, cy = lx + nrm[0] * (H / 2 + 0.03), ly + nrm[1] * (H / 2 + 0.03)
        lg = gs.add_group_shape()
        set_alt(lg, "Small drawing of a steam engine with its tender.", "engine icon")
        loco_icon(lg.shapes, cx - W / 2, cy - H / 2, W, "tender")
        lg.rotation = rot
    # fuel bars
    items = [(3.5, "Climbing: high", 0.9), (6.6, "Steady: medium", 0.55), (9.7, "Coasting: low", 0.22)]
    for cx, txt, frac in items:
        label(gs, cx - 1.5, 4.4, 3.0, 0.42, txt, 18, TEXT, True, name="fuel label")
        rect(gs, cx - 1.3, 4.92, 2.6, 0.3, PANEL_ALT, LINE, 1.0, radius=0.05, name="fuel track")
        rect(gs, cx - 1.3, 4.92, 2.6 * frac, 0.3, ORANGE, None, radius=0.05, name="fuel fill")
    label(gs, 0.7, 5.55, 5.0, 0.35, "Shape only. Not measured.", 14, MUTED, align="l", name="note")
    finish(s, "Heavy loads, acceleration and hills use more. Coasting uses less.", 9)
    return s


# ---------------------------------------------------------------- slide 10
def s10(prs):
    s = new_slide(prs, "Test targets for range", "Provisional")
    sh = s.shapes
    tx, ty = 2.37, 1.85
    gf, tbl = add_table(sh, tx, ty, 8.6, 3.3, 5, 3, [2.6, 3.0, 3.0],
                        "Table of provisional range targets per tank for Small, Medium and Large engines. "
                        "Small: water 2 to 3 kilometres, coal 4 to 5. Medium: water 4 to 5, coal about 7. "
                        "Large: water 6 to 7, coal about 10.")
    heights = [0.65, 0.55, 0.7, 0.7, 0.7]
    for r, hh in zip(tbl.rows, heights):
        r.height = I(hh)
    tbl.cell(0, 0).merge(tbl.cell(0, 2))
    set_cell(tbl.cell(0, 0), "Route-dependent targets", 20, TEXT, True, PANEL_ALT, "l")
    set_cell(tbl.cell(1, 0), "", 18, TEXT, False, PANEL)
    set_cell(tbl.cell(1, 1), "Water", 20, WATER, True, PANEL, "c")
    set_cell(tbl.cell(1, 2), "Coal", 20, TEXT, True, PANEL, "c")
    rows = [("Small", "2–3 km", "4–5 km"), ("Medium", "4–5 km", "about 7 km"),
            ("Large", "6–7 km", "about 10 km")]
    for i, (a, b, c) in enumerate(rows, 2):
        set_cell(tbl.cell(i, 0), a, 20, ORANGE, True, PANEL, "l")
        set_cell(tbl.cell(i, 1), b, 20, TEXT, False, PANEL, "c")
        set_cell(tbl.cell(i, 2), c, 20, TEXT, False, PANEL, "c")
    ichip(sh, "Provisional", tx + 8.6 - 1.75, ty + 0.17, 1.6)
    label(sh, tx, ty + 3.35, 8.6, 0.45, "Not guaranteed distances or tank sizes.", 18, MUTED, align="c",
          name="footer")
    finish(s, "Test targets for range per tank. They depend on the route and may change.", 10)
    return s


# ---------------------------------------------------------------- slide 11
def drop_points(cx, y0, r):
    cy = y0 + 1.9 * r
    pts = [(cx, y0)]
    a0 = math.degrees(math.acos(r / (1.9 * r)))
    n = 30
    for i in range(n + 1):
        a = math.radians(a0 + (360 - 2 * a0) * i / n)
        pts.append((cx + r * math.sin(a), cy - r * math.cos(a)))
    return pts


def s11(prs):
    s = new_slide(prs, "A better fuel", "Agreed")
    sh = s.shapes
    g = group(sh, "Two fuels and a water question",
              "Coal and Compacted Coal side by side, each with a bar for burn time. The Compacted Coal bar is "
              "longer. A water drop with a question mark shows that water saving is not established.")
    gs = g.shapes
    for i, (nm, frac) in enumerate((("Coal", 0.55), ("Compacted Coal", 0.92))):
        x = 0.6 + i * 3.9
        rect(gs, x, 1.55, 3.7, 3.5, PANEL, None, radius=0.1, name="fuel card")
        if i == 0:
            poly(gs, [(x + 1.05, 3.05), (x + 0.9, 2.45), (x + 1.3, 1.95), (x + 1.85, 1.8), (x + 2.45, 2.0),
                      (x + 2.8, 2.5), (x + 2.6, 3.05), (x + 1.9, 3.15)], "#101215", "#B5BBC2", 2.0, name="coal lump")
            for fx0, fy0, fx1, fy1 in ((1.3, 1.95, 1.85, 2.55), (1.85, 2.55, 2.8, 2.5), (1.85, 2.55, 1.9, 3.15)):
                line(gs, x + fx0, fy0, x + fx1, fy1, "#5A616B", 1.5, name="facet")
        else:
            rect(gs, x + 0.85, 1.95, 2.0, 1.1, "#101215", "#B5BBC2", 2.0, radius=0.12, name="compacted block")
            for k in (1, 2):
                line(gs, x + 0.85 + k * 0.667, 2.0, x + 0.85 + k * 0.667, 3.0, "#5A616B", 2.0, name="groove")
        label(gs, x + 0.2, 3.3, 3.3, 0.45, nm, 20, TEXT, True, name="fuel name")
        label(gs, x + 0.25, 3.85, 3.2, 0.3, "Burn time", 14, MUTED, align="l", name="bar caption")
        rect(gs, x + 0.25, 4.2, 3.2, 0.34, PANEL_ALT, LINE, 1.0, radius=0.06, name="burn track")
        rect(gs, x + 0.25, 4.2, 3.2 * frac, 0.34, ORANGE, None, radius=0.06, name="burn fill")
    label(gs, 0.6, 5.2, 7.6, 0.35, "Not to scale", 14, MUTED, align="c", name="scale note")
    # water question
    rect(gs, 8.6, 1.55, 4.13, 3.5, PANEL, LINE, 1.5, radius=0.1, name="water card")
    poly(gs, drop_points(10.665, 1.8, 0.68), WATER, None, name="water drop")
    label(gs, 10.065, 2.55, 1.2, 1.0, "?", 54, DARK, True, name="question mark")
    chip(gs, "Undecided", 8.85, 4.25, 3.63, 0.5, 14, "Water saving: not established", name="ICHIP TEXT")
    finish(s, "Compacted Coal burns more efficiently. Water saving is not assumed.", 11)
    return s


# ---------------------------------------------------------------- slide 12 (SPEC-D)
def s12(prs):
    s = new_slide(prs, "A steam station", "Agreed")
    sh = s.shapes
    g = group(sh, "Steam station plan",
              "Top-down plan of a steam station. A coal conveyor feeds a coal stage and a pipe feeds a water tower. "
              "A locomotive stands on the track beside a platform and a signal box. A dashed line marks a "
              "large footprint with an exact size that is undecided.")
    gs = g.shapes
    # footprint outline first (behind everything)
    rect(gs, 0.75, 1.95, 9.55, 3.95, None, ORANGE, 2.0, radius=0.15, dash=MSO_LINE.DASH, name="footprint")
    label(gs, 4.6, 5.32, 5.6, 0.5, "Large footprint. Exact size undecided.", 14, ORANGE, True, align="r",
          name="footprint label")
    # track
    rect(gs, 0.9, 3.85, 11.6, 0.07, STEEL, None, name="rail")
    rect(gs, 0.9, 4.1, 11.6, 0.07, STEEL, None, name="rail")
    for k in range(30):
        rect(gs, 1.0 + k * 0.39, 3.8, 0.1, 0.42, SLEEPER, None, name="sleeper")
    # platform, box
    rect(gs, 4.5, 4.35, 3.6, 0.5, PANEL_ALT, STEEL, 1.5, name="platform", text="Platform and cargo loading",
         size=14, color=TEXT)
    rect(gs, 2.2, 4.55, 1.5, 1.1, PANEL_ALT, STEEL, 1.5, name="signal box", text="Signal box", size=14, color=TEXT)
    line(gs, 2.2, 4.8, 3.7, 4.55, STEEL, 1.5, name="roof line")
    # coal stage, conveyor, chute
    rect(gs, 5.6, 2.35, 1.8, 0.9, PANEL_ALT, STEEL, 1.5, name="coal stage", text="Coal stage", size=14, color=TEXT)
    line(gs, 1.0, 2.8, 5.6, 2.8, STEEL, 3.0, dash=MSO_LINE.DASH, tail=True, name="conveyor")
    label(gs, 1.0, 2.38, 3.4, 0.35, "Conveyor: coal in", 14, TEXT, True, align="l", name="conveyor label")
    line(gs, 6.5, 3.25, 6.5, 3.82, STEEL, 3.0, name="chute")
    # water tower, crane, pipe
    oval(gs, 8.6, 2.3, 1.0, 1.0, WATER, TEXT, 1.5, name="water tower", text="Water tower", size=14, color=DARK,
         bold=True)
    line(gs, 9.1, 3.3, 7.7, 3.82, WATER, 3.0, name="crane")
    line(gs, 12.5, 3.15, 9.6, 3.15, WATER, 5.0, name="water pipe")
    label(gs, 10.4, 3.2, 2.1, 0.35, "Pipe: water in", 14, TEXT, True, align="r", name="pipe label")
    # locomotive (top-down) with two marks
    rect(gs, 5.9, 3.84, 2.4, 0.35, ORANGE, None, radius=0.1, name="locomotive")
    oval(gs, 6.4, 3.9, 0.22, 0.22, COAL, TEXT, 1.5, name="coal bunker mark")
    oval(gs, 7.6, 3.9, 0.22, 0.22, WATER, TEXT, 1.5, name="water hatch mark")
    # vanilla comparison
    rect(gs, 10.55, 5.05, 2.15, 0.95, PANEL_ALT, STEEL, 1.5, name="vanilla station",
         text="Vanilla station (for comparison)", size=14, color=TEXT)
    # photo inset
    add_picture_fit(sh, "P17_coal_stage_water_tank_didcot.jpg", 10.55, 1.45, 2.18, 1.23,
                    "A coal stage and a water tank at Didcot Railway Centre.")
    credit(sh, 10.55, 2.7, 2.18, "Rosser1954, CC BY-SA 4.0")
    finish(s, "A steam station is big. It has a water tower, coal loading, a signal box and a platform.", 12)
    return s


# ---------------------------------------------------------------- slide 13
def s13(prs):
    s = new_slide(prs, "Big on purpose", "Agreed")
    sh = s.shapes
    g = group(sh, "Two station footprints",
              "A large dashed footprint for a steam station holds four blocks: water, coal, signal box and "
              "platform. Beside it a much smaller solid rectangle shows a vanilla station.")
    gs = g.shapes
    rect(gs, 0.8, 1.6, 8.3, 4.0, None, ORANGE, 2.5, radius=0.15, dash=MSO_LINE.DASH, name="steam footprint")
    label(gs, 1.0, 1.68, 4.0, 0.45, "Steam station", 18, ORANGE, True, align="l", name="footprint title")
    blocks = [("Water", WATER, 1.15, 2.3, DARK), ("Coal", COAL, 5.15, 2.3, TEXT),
              ("Signal box", PANEL_ALT, 1.15, 3.9, TEXT), ("Platform", PANEL_ALT, 5.15, 3.9, TEXT)]
    for nm, fill, bx, by, tc in blocks:
        rect(gs, bx, by, 3.7, 1.35, fill, STEEL if fill != WATER else TEXT, 1.5, radius=0.08, name="block",
             text=nm, size=18, color=tc, bold=True)
    rect(gs, 10.0, 4.2, 2.3, 1.4, PANEL_ALT, STEEL, 2.0, name="vanilla footprint", text="Vanilla station",
         size=16, color=TEXT, bold=True)
    label(gs, 0.8, 5.7, 8.3, 0.4, "Exact sizes: undecided (OQ09)", 18, MUTED, align="c", name="size note")
    finish(s, "Steam technology is cheap in materials but costs land and buildings. That is the price.", 13)
    return s


# ---------------------------------------------------------------- slide 14 (SPEC-E)
def step_icon(sh, n, cx, cy):
    """Simple shape icon for servicing step n, centred at (cx, cy), about 0.7 x 0.5 in."""
    if n == 1:  # approach: slow arrow
        arrow(sh, cx - 0.35, cy, cx + 0.35, cy, ORANGE, 4.0, name="icon approach")
    elif n == 2:  # dock outline with a small engine block
        line(sh, cx - 0.35, cy - 0.22, cx - 0.35, cy + 0.22, STEEL, 3.0, name="icon dock")
        line(sh, cx - 0.35, cy + 0.22, cx + 0.35, cy + 0.22, STEEL, 3.0, name="icon dock")
        line(sh, cx + 0.35, cy + 0.22, cx + 0.35, cy - 0.22, STEEL, 3.0, name="icon dock")
        rect(sh, cx - 0.2, cy - 0.05, 0.4, 0.22, ORANGE, None, radius=0.05, name="icon engine")
    elif n == 3:  # steam hiss: three ellipses
        for k, (dx, dy, w) in enumerate(((-0.22, 0.12, 0.26), (0.0, -0.02, 0.34), (0.22, -0.16, 0.42))):
            oval(sh, cx + dx - w / 2, cy + dy - 0.09, w, 0.18, TEXT, None, alpha=0.85, name="icon steam")
    elif n == 4:  # coal chute
        poly(sh, [(cx - 0.35, cy - 0.25), (cx + 0.1, cy + 0.1), (cx + 0.1, cy + 0.2), (cx - 0.35, cy - 0.15)],
             STEEL, None, name="icon chute")
        poly(sh, [(cx + 0.05, cy + 0.28), (cx + 0.15, cy + 0.12), (cx + 0.3, cy + 0.14), (cx + 0.38, cy + 0.28)],
             COAL, "#B5BBC2", 1.5, name="icon coal")
    elif n == 5:  # crane arc
        curve(sh, (cx - 0.35, cy + 0.2), (cx, cy - 0.45), (cx + 0.35, cy + 0.2), WATER, 3.5, name="icon crane")
    elif n == 6:  # two crosshairs
        crosshair(sh, cx - 0.2, cy, 0.24)
        crosshair(sh, cx + 0.22, cy, 0.24)
    elif n == 7:  # clock
        oval(sh, cx - 0.25, cy - 0.25, 0.5, 0.5, None, TEXT, 2.5, name="icon clock")
        line(sh, cx, cy, cx, cy - 0.16, TEXT, 2.5, name="icon hand")
        line(sh, cx, cy, cx + 0.12, cy + 0.04, TEXT, 2.5, name="icon hand")
    elif n == 8:  # retract arrow
        arrow(sh, cx + 0.35, cy, cx - 0.25, cy, PURPLE, 4.0, name="icon retract")
        line(sh, cx - 0.3, cy - 0.2, cx - 0.3, cy + 0.2, PURPLE, 4.0, name="icon stop")
    elif n == 9:  # engine leaves
        rect(sh, cx - 0.3, cy - 0.1, 0.5, 0.25, ORANGE, None, radius=0.05, name="icon engine")
        arrow(sh, cx + 0.22, cy + 0.02, cx + 0.42, cy + 0.02, ORANGE, 3.0, name="icon depart")


def s14(prs):
    s = new_slide(prs, "Servicing takes time", "Agreed")
    sh = s.shapes
    g = group(sh, "Servicing steps",
              "Nine steps in two rows: approach slowly, settle in, long steam hiss, coal chutes, water arm swings, "
              "find the hatches, tanks fill, machinery folds away, depart. Below, a long bar for empty tanks and a "
              "short bar for a small top-up.")
    gs = g.shapes
    steps = ["Approach slowly", "Settle in", "Long steam hiss", "Coal chutes", "Water arm swings",
             "Find the hatches", "Tanks fill", "Machinery folds away", "Depart"]
    BW, BH, STEP = 2.2, 1.5, 2.48
    pos = []
    for i in range(9):
        if i < 5:
            pos.append((0.6 + i * STEP, 1.45))
        else:
            pos.append((0.6 + (i - 5) * STEP, 3.3))
    for i, (x, y) in enumerate(pos):
        rect(gs, x, y, BW, BH, PANEL, LINE, 1.5, radius=0.1, name="step card")
        step_icon(gs, i + 1, x + 1.25, y + 0.5)
        badge(gs, x + 0.32, y + 0.32, i + 1, 0.4)
        label(gs, x + 0.08, y + 0.85, BW - 0.16, 0.6, steps[i], 14, TEXT, True, name="step label")
    for i in range(9):
        x, y = pos[i]
        if i in (0, 1, 2, 3, 5, 6, 7):
            arrow(gs, x + BW + 0.02, y + BH / 2, x + STEP - 0.02, y + BH / 2, ORANGE, 2.25, name="step arrow")
    # row-to-row connector (step 5 to step 6)
    x5 = pos[4][0] + BW / 2
    x6 = pos[5][0] + BW / 2
    poly(gs, [(x5, 2.95), (x5, 3.12), (x6, 3.12), (x6, 3.28)], None, ORANGE, 2.25, closed=False, name="row link")
    _ends(gs[-1], False, True)
    # inline chip on step 8
    x8, y8 = pos[7]
    chip(gs, "Proposed", x8 + BW - 1.45, y8 - 0.17, 1.4, 0.32, 14, name="ICHIP")
    # time bars
    time_bars(gs, 0.6, 5.15, 5.57, track=9.6, bh=0.3, labels=False)
    label(gs, 10.35, 5.1, 2.4, 0.4, "Small top-up", 14, TEXT, True, align="l", name="bar label")
    label(gs, 10.35, 5.52, 2.4, 0.4, "Empty tanks", 14, TEXT, True, align="l", name="bar label")
    label(gs, 0.6, 5.93, 9.6, 0.32, "Rates and times: Proposed or provisional", 14, MUTED, align="l", name="note")
    finish(s, "The machinery finds each engine's hatches. Servicing takes visible time. Then it folds away.", 14)
    return s


# ---------------------------------------------------------------- slide 15
def s15(prs):
    s = new_slide(prs, "Finding the hatches", "Agreed")
    sh = s.shapes
    g = group(sh, "Two engines and machinery arms",
              "A tender engine and a tank engine, each with its water hatch and coal point in a different place. "
              "A machinery arm reaches to a crosshair on each point.")
    gs = g.shapes
    rail_y = 4.85
    rect(gs, 0.6, rail_y, 12.1, 0.07, STEEL, None, name="rail")
    # tender engine
    u1w = 5.0
    t1 = loco_icon(gs, 1.7, rail_y - 4.4 * u1w / 12.0, u1w, "tender")
    # tank engine
    u2w = 4.3
    t2 = loco_icon(gs, 7.5, rail_y - 4.4 * u2w / 10.0, u2w, "tank")
    beam_y = 2.55
    for tgt, left_post, (bx0, bx1) in ((t1, 1.0, (1.0, 3.8)), (t2, 7.0, (7.0, 10.4))):
        line(gs, left_post, beam_y, left_post, rail_y, STEEL, 6.0, name="gantry post")
        line(gs, bx0, beam_y, bx1, beam_y, STEEL, 6.0, name="gantry beam")
        for key in ("water", "coal"):
            px, py = tgt[key]
            line(gs, px, beam_y, px, py - 0.17, STEEL, 5.0, name="machinery arm")
            crosshair(gs, px, py, 0.34)
    # labels above the beam
    wx, _ = t1["water"]
    cx1, _ = t1["coal"]
    label(gs, wx - 1.55, beam_y - 0.5, 1.55, 0.4, "Water hatch", 14, ORANGE, True, align="r", name="target label")
    label(gs, cx1 + 0.1, beam_y - 0.5, 1.5, 0.4, "Coal point", 14, ORANGE, True, align="l", name="target label")
    wx2, _ = t2["water"]
    cx2, _ = t2["coal"]
    label(gs, cx2 - 0.75, beam_y - 0.5, 1.5, 0.4, "Coal point", 14, ORANGE, True, name="target label")
    label(gs, wx2 - 0.75, beam_y - 0.5, 1.5, 0.4, "Water hatch", 14, ORANGE, True, name="target label")
    label(gs, 1.7, rail_y + 0.08, 5.0, 0.35, "Tender engine", 14, TEXT, True, name="engine label")
    label(gs, 7.5, rail_y + 0.08, 4.3, 0.35, "Tank engine", 14, TEXT, True, name="engine label")
    chip(gs, "Proposed", 0.6, 5.55, 1.4, 0.32, 14, name="ICHIP")
    label(gs, 2.15, 5.42, 10.55, 0.75,
          "Target points: water, coal, exhaust, front coupler, rear coupler, cab. Names are suggestions.", 16, TEXT,
          align="l", name="target list")
    finish(s, "Every engine model has its own hatches. The machinery finds them.", 15)
    return s


# ---------------------------------------------------------------- slide 16
def s16(prs):
    s = new_slide(prs, "How long does it take?", "Provisional")
    sh = s.shapes
    g = group(sh, "Two time bars",
              "A short bar for a small top-up and a long bar for refilling empty tanks.")
    gs = g.shapes
    track = 5.6
    # clock icons
    for yy in (2.3, 4.3):
        oval(gs, 0.6, yy + 0.02, 0.4, 0.4, None, MUTED, 2.0, name="clock")
        line(gs, 0.8, yy + 0.22, 0.8, yy + 0.09, MUTED, 2.0, name="hand")
        line(gs, 0.8, yy + 0.22, 0.9, yy + 0.25, MUTED, 2.0, name="hand")
    for yy, frac, txt in ((2.3, 0.26, "Small top-up"), (4.3, 0.95, "Empty tanks")):
        label(gs, 1.2, yy - 0.55, track, 0.45, txt, 20, TEXT, True, align="l", name="bar label")
        rect(gs, 1.2, yy, track, 0.5, PANEL_ALT, LINE, 1.0, radius=0.06, name="time track")
        rect(gs, 1.2, yy, track * frac, 0.5, ORANGE, None, radius=0.06, name="time fill")
    cards = [("Provisional", "First example: 5 to 15 extra seconds"),
             ("Proposed", "Later idea: real transfer rates"),
             ("Undecided", "Rates and buffers: undecided (OQ08)")]
    for i, (kind, txt) in enumerate(cards):
        y = 1.5 + i * 1.5
        rect(gs, 7.4, y, 5.33, 1.35, PANEL, LINE, 1.0, radius=0.1, name="note card")
        chip(gs, kind, 7.6, y + 0.15, 1.7 if kind != "Provisional" else 1.7, 0.32, 14, name="ICHIP")
        label(gs, 7.6, y + 0.55, 4.95, 0.7, txt, 18, TEXT, align="l", anchor="t", name="note text")
    finish(s, "A small top-up should be quick. An empty refill takes longer.", 16)
    return s


SLIDES = [s09, s10, s11, s12, s13, s14, s15, s16]
