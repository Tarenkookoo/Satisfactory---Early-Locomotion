"""Deck 9, chunk 2: slides 10 to 18."""
import math
from lib import *


# 10 --------------------------------------------------------------------------------
def _ladder(c, x0, title, heights, hi, descr_name):
    """One panel with three speed bars (Small, Medium, Large). Shape only, no numbers."""
    W = 5.15
    rrect(c, x0, 1.5, W, 4.1, radius=0.08, fill=PANEL, name="Panel")
    text(c, x0 + 0.3, 1.6, W - 0.6, 0.5, [[T(title, 20, True, ORANGE)]], anchor="m", inset=(0, 0, 0, 0),
         name="Ladder title")
    base = 4.95
    line(c, x0 + 0.45, base, x0 + 0.45, 2.35, color=STEEL, lw=2, tail="triangle", name="Speed axis")
    text(c, x0 + 0.6, 2.2, 1.2, 0.3, [[T("Speed", 14, False, MUTED)]], anchor="m", inset=(0, 0, 0, 0),
         name="Axis label")
    rect(c, x0 + 0.45, base, W - 0.8, 0.04, fill=LINE, name="Baseline")
    for i, (nm, h) in enumerate(zip(("Small", "Medium", "Large"), heights)):
        bx = x0 + 1.0 + i * 1.3
        rrect(c, bx, base - h, 1.0, h, radius=0.06, fill=ORANGE if i == hi else STEEL, name="Bar " + nm)
        label(c, bx - 0.15, base + 0.08, 1.3, 0.4, nm, 18, True)


def s10(prs):
    s = new_slide(prs, "The speed question", "U")
    g1 = group(s, "Ladder: earlier idea",
               "Earlier idea: three bars rising from Small to Medium to Large, shape only, no numbers.")
    _ladder(g1.shapes, 0.6, "Earlier idea", (1.0, 1.75, 2.5), 2, "earlier")
    g2 = group(s, "Ladder: later idea",
               "Later idea: three bars with the Medium bar tallest, shape only, no numbers.")
    _ladder(g2.shapes, 7.58, "Later idea", (1.35, 2.5, 1.35), 1, "later")
    g3 = group(s, "Question mark", "A question mark between the two ideas: which is right is undecided.")
    q = circle(g3.shapes, 6.665, 3.45, 0.55, fill=None, line=ORANGE, lw=3, name="Question circle")
    box_text(q, [[T("?", 40, True, ORANGE)]], inset=(0, 0, 0, 0), wrap_=False)
    label(s.shapes, 0.6, 5.72, 3.0, 0.35, "Not to scale", 14, False, color=MUTED, align="l", inset=(0, 0, 0, 0))
    label(s.shapes, 11.73, 5.72, 1.0, 0.35, "OQ05", 14, False, color=MUTED, align="r", inset=(0, 0, 0, 0))
    add_caption(s, "Is Medium the fastest, or Large? That is still undecided.")
    add_number(s, 10)
    return s


# 11 --------------------------------------------------------------------------------
def _wagon_grid(c, x, y, cols, rows, col, name):
    cell, gap, pad = 0.4, 0.07, 0.22
    gw = cols * (cell + gap) - gap
    gh = rows * (cell + gap) - gap
    bw, bh = gw + 2 * pad, gh + 2 * pad
    rrect(c, x, y, bw, bh, radius=0.08, fill=PANEL_ALT, line=col, lw=2.5, name=name + " body")
    for r in range(rows):
        for k in range(cols):
            rrect(c, x + pad + k * (cell + gap), y + pad + r * (cell + gap), cell, cell, radius=0.05, fill=col,
                  name="Stack cell")
    for wx in (0.55, bw - 0.55):
        wheel(c, x + wx, y + bh + 0.2, 0.2)
    return bw, bh


def s11(prs):
    s = new_slide(prs, "How big is a wagon?", "V")
    g = group(s, "Diagram: two wagons and their stack grids",
              "A steam wagon holding a grid of 20 stacks beside a taller-capacity vanilla wagon holding "
              "a grid of 32 stacks.")
    rrect(g.shapes, 0.6, 1.5, 12.13, 4.55, radius=0.08, fill=PANEL, name="Panel")
    x1 = 1.35
    bw1, bh1 = _wagon_grid(g.shapes, x1, 1.85, 5, 4, ORANGE, "Steam wagon")
    x2 = x1 + bw1 + 0.75
    bw2, bh2 = _wagon_grid(g.shapes, x2, 1.85, 8, 4, ELEC, "Vanilla wagon")
    rect(g.shapes, x1 - 0.15, 1.85 + bh1 + 0.4, x2 + bw2 - x1 + 0.3, 0.05, fill=LINE, name="Rail")
    ly = 1.85 + bh1 + 0.5
    label(g.shapes, x1 + bw1 / 2 - 1.9, ly, 3.8, 0.45, "Steam wagon: about 20 stacks", 18, True)
    label(g.shapes, x2 + bw2 / 2 - 1.9, ly, 3.8, 0.45, "Vanilla wagon: 32 stacks", 18, True)
    inline_chip(g.shapes, 0.95, 5.3, "U", "Wagon catalogue: undecided (OQ07)")
    # what a stack is
    g2 = group(s, "Note: what a stack is", "A stack is a pile of one item, drawn as one cell holding a pile.")
    rrect(g2.shapes, 10.05, 1.85, 2.4, 2.6, radius=0.08, fill=PANEL_ALT, name="Note panel")
    cx = 11.25
    rrect(g2.shapes, cx - 0.45, 2.05, 0.9, 0.9, radius=0.08, fill=None, line=STEEL, lw=2, name="Example cell")
    for dx, dy in ((-0.17, 0.12), (0.17, 0.12), (0.0, -0.1)):
        circle(g2.shapes, cx + dx, 2.5 + dy, 0.14, fill=AMBER, line=DARK, lw=1, name="Item")
    text(g2.shapes, 10.2, 3.1, 2.1, 1.2, [[T("A stack is a pile of one item.", 18, False, TEXT)]], align="c",
         anchor="t", inset=(0, 0, 0, 0), name="Note text")
    add_caption(s, "Steam wagons are cheaper and hold less. About 20 stacks against 32 in a vanilla wagon.")
    add_number(s, 11)
    return s


# 12 --------------------------------------------------------------------------------
def _icon(c, kind, cx, cy):
    if kind == "cost":
        circle(c, cx, cy, 0.4, fill=AMBER, line=DARK, lw=1.5, name="Coin")
        circle(c, cx, cy, 0.27, fill=None, line=DARK, lw=2, name="Coin ring")
    elif kind == "cargo":
        rect(c, cx - 0.4, cy - 0.35, 0.8, 0.7, fill=AMBER, line=DARK, lw=1.5, name="Crate")
        line(c, cx - 0.4, cy - 0.35, cx + 0.4, cy + 0.35, color=DARK, lw=2)
        line(c, cx - 0.4, cy + 0.35, cx + 0.4, cy - 0.35, color=DARK, lw=2)
    elif kind == "time":
        circle(c, cx, cy, 0.4, fill=None, line=STEEL, lw=3, name="Clock")
        line(c, cx, cy, cx, cy - 0.27, color=TEXT, lw=3, name="Clock hand")
        line(c, cx, cy, cx + 0.2, cy + 0.1, color=TEXT, lw=3, name="Clock hand")
    elif kind == "fuel":
        poly(c, [(cx - 0.62, cy + 0.32), (cx - 0.5, cy), (cx - 0.3, cy - 0.2), (cx - 0.05, cy - 0.1),
                 (cx + 0.05, cy + 0.32)], fill=COAL, line=STEEL, lw=1.5, name="Coal heap")
        shape(c, MSO_SHAPE.TEAR, cx + 0.15, cy - 0.28, 0.5, 0.5, fill=WATER, name="Water drop", rot=315)
    elif kind == "stopped":
        circle(c, cx, cy, 0.4, fill=None, line=ORANGE, lw=3, name="Pause ring")
        rect(c, cx - 0.15, cy - 0.18, 0.1, 0.36, fill=ORANGE, name="Pause bar")
        rect(c, cx + 0.05, cy - 0.18, 0.1, 0.36, fill=ORANGE, name="Pause bar")
    elif kind == "track":
        rails(c, cx - 0.55, cy - 0.2, 1.1, gauge=0.4, pitch=0.28)
    elif kind == "weight":
        shape(c, MSO_SHAPE.TRAPEZOID, cx - 0.42, cy - 0.12, 0.84, 0.52, fill=STEEL, name="Weight")
        shape(c, MSO_SHAPE.DONUT, cx - 0.17, cy - 0.42, 0.34, 0.34, fill=STEEL, name="Weight ring")
    elif kind == "station":
        rect(c, cx - 0.45, cy - 0.12, 0.9, 0.5, fill=STEEL, name="Station")
        shape(c, MSO_SHAPE.ISOSCELES_TRIANGLE, cx - 0.55, cy - 0.45, 1.1, 0.36, fill=ORANGE, name="Roof")
        rect(c, cx - 0.1, cy + 0.08, 0.2, 0.3, fill=COAL, name="Door")


def s12(prs):
    s = new_slide(prs, "Judge the whole route", "A")
    items = [("Cost", "cost"), ("Cargo per trip", "cargo"), ("Journey time", "time"), ("Coal and water", "fuel"),
             ("Time stopped", "stopped"), ("Track used", "track"), ("Tender weight", "weight"),
             ("Station size", "station")]
    for i, (lab, kind) in enumerate(items):
        col, row = i % 4, i // 4
        x = 0.6 + col * (2.9 + 0.177)
        y = 1.5 + row * 2.3
        g = group(s, "Scorecard item: " + lab, "Scorecard item: " + lab + ".")
        rrect(g.shapes, x, y, 2.9, 2.05, radius=0.08, fill=PANEL, name="Tile")
        _icon(g.shapes, kind, x + 1.45, y + 0.78)
        label(g.shapes, x + 0.1, y + 1.45, 2.7, 0.5, lab, 18, True)
    add_caption(s, "A good route is judged as a whole, not by one number.")
    add_number(s, 12)
    return s


# 13 --------------------------------------------------------------------------------
def s13(prs):
    s = new_slide(prs, "Stops cost time", "A")
    g = group(s, "Diagram: a short stop and a long stop on a timeline",
              "A timeline with an engine running, a short stop, more running and a long stop. "
              "Stops take time and buy reliability.")
    rrect(g.shapes, 0.6, 1.5, 12.13, 4.5, radius=0.08, fill=PANEL, name="Panel")
    ax = 4.6
    line(g.shapes, 0.95, ax + 0.02, 12.3, ax + 0.02, color=STEEL, lw=3, tail="triangle", name="Time axis")
    label(g.shapes, 10.8, ax + 0.12, 1.5, 0.4, "Time", 18, True, color=MUTED, align="r", inset=(0, 0, 0, 0))
    # running engines on the axis
    for lx in (0.95, 4.55, 10.0):
        loco(g.shapes, lx, ax - 1.4 * 0.45 - 0.02, 0.45)
    # stops
    sx, sw = 2.55, 1.7
    lx_, lw_ = 6.15, 3.5
    for x, w, nm in ((sx, sw, "Short stop"), (lx_, lw_, "Long stop")):
        b = rrect(g.shapes, x, ax - 0.62, w, 0.6, radius=0.08, fill=AMBER, name=nm)
        box_text(b, [[T(nm, 18, True, DARK)]], inset=(0, 0, 0, 0), wrap_=False)
    # reliability
    ry = 2.85
    line(g.shapes, sx + sw / 2, ax - 0.7, sx + sw / 2, ry + 0.05, color=GREEN, lw=3, tail="triangle",
         name="Reliability arrow")
    line(g.shapes, lx_ + lw_ / 2, ax - 0.7, lx_ + lw_ / 2, ry + 0.05, color=GREEN, lw=3, tail="triangle",
         name="Reliability arrow")
    line(g.shapes, sx + sw / 2 - 0.4, ry, lx_ + lw_ / 2 + 0.4, ry, color=GREEN, lw=3, name="Reliability bar")
    label(g.shapes, 4.2, ry - 0.5, 4.0, 0.42, "Reliability", 20, True, color=GREEN)
    inline_chip(g.shapes, sx, ax + 0.4, "U", "To be tested")
    add_caption(s, "Service stops trade time for reliability. Whether top-ups help throughput is still to be tested.")
    add_number(s, 13)
    return s


# 14 --------------------------------------------------------------------------------
def s14(prs):
    s = new_slide(prs, "Test targets for range", "V")
    g = group(s, "Table: route-dependent range targets",
              "Table of test targets for range per tank. Small: water 2 to 3 km, coal 4 to 5 km. "
              "Medium: water 4 to 5 km, coal about 7 km. Large: water 6 to 7 km, coal about 10 km.")
    x0, widths = 1.9, (2.5, 3.5, 3.5)
    text(g.shapes, x0, 1.5, 9.5, 0.5, [[T("Route-dependent targets", 20, True, ORANGE)]], anchor="m",
         inset=(0, 0, 0, 0), name="Table header")
    cols = [x0, x0 + widths[0] + 0.1, x0 + widths[0] + widths[1] + 0.2]
    # column headings with icons
    hy = 2.1
    for k, (nm, ic) in enumerate((("Water", "water"), ("Coal", "coal"))):
        cx = cols[k + 1]
        rrect(g.shapes, cx, hy, widths[k + 1], 0.7, radius=0.08, fill=PANEL_ALT, name="Column heading")
        if ic == "water":
            shape(g.shapes, MSO_SHAPE.TEAR, cx + 0.3, hy + 0.17, 0.34, 0.34, fill=WATER, name="Water drop", rot=315)
        else:
            poly(g.shapes, [(cx + 0.25, hy + 0.52), (cx + 0.33, hy + 0.3), (cx + 0.47, hy + 0.17),
                            (cx + 0.62, hy + 0.3), (cx + 0.72, hy + 0.52)], fill=COAL, line=STEEL, lw=1.5,
                 name="Coal heap")
        text(g.shapes, cx + 0.9, hy, widths[k + 1] - 1.0, 0.7, [[T(nm, 20, True, TEXT)]], anchor="m",
             inset=(0, 0, 0, 0), name="Column label")
    data = [("Small", "2–3 km", "4–5 km"), ("Medium", "4–5 km", "about 7 km"), ("Large", "6–7 km", "about 10 km")]
    for i, (nm, wv, cv) in enumerate(data):
        y = 2.9 + i * 0.85
        rrect(g.shapes, cols[0], y, widths[0], 0.75, radius=0.08, fill=PANEL, name="Row heading")
        text(g.shapes, cols[0] + 0.25, y, widths[0] - 0.3, 0.75, [[T(nm, 20, True, ORANGE)]], anchor="m",
             inset=(0, 0, 0, 0), name="Row label")
        for k, v in enumerate((wv, cv)):
            rrect(g.shapes, cols[k + 1], y, widths[k + 1], 0.75, radius=0.08, fill=PANEL, name="Cell")
            text(g.shapes, cols[k + 1], y, widths[k + 1], 0.75, [[T(v, 22, False, TEXT)]], align="c", anchor="m",
                 inset=(0, 0, 0, 0), name="Cell value")
    label(g.shapes, x0, 5.55, 9.5, 0.45, "Not guaranteed distances or tank sizes.", 18, False, color=MUTED,
          align="l", inset=(0, 0, 0, 0))
    add_caption(s, "Test targets for range per tank. They depend on the route and may change.")
    add_number(s, 14)
    return s


# 15 --------------------------------------------------------------------------------
def s15(prs):
    s = new_slide(prs, "Behind the scenes", "P")
    layers = [("Shared base:", " fuel, water, traction, steam, signals", ORANGE, "gear"),
              ("Data card:", " numbers for this engine", AMBER, "card"),
              ("Model:", " look, wheels, sound", STEEL, "model")]
    for i, (nm, desc, col, icon) in enumerate(layers):
        y = 1.5 + i * 1.4
        g = group(s, "Layer: " + nm.strip(":"), "Layer %d of 3: %s%s" % (i + 1, nm, desc))
        rrect(g.shapes, 0.6, y, 12.13, 1.1, radius=0.08, fill=PANEL, line=col, lw=2, name="Layer slab")
        if icon == "gear":
            shape(g.shapes, MSO_SHAPE.GEAR_6, 1.0, y + 0.2, 0.7, 0.7, fill=col, name="Gear")
        elif icon == "card":
            rrect(g.shapes, 1.0, y + 0.25, 0.85, 0.6, radius=0.06, fill=None, line=col, lw=2.5, name="Card")
            for k in range(3):
                line(g.shapes, 1.15, y + 0.4 + k * 0.14, 1.7, y + 0.4 + k * 0.14, color=col, lw=2)
        else:
            loco(g.shapes, 0.95, y + 0.26, 0.42)
        text(g.shapes, 2.55, y, 9.9, 1.1, [[T(nm, 20, True, TEXT), T(desc, 20, False, TEXT)]], anchor="m",
             inset=(0, 0, 0, 0), name="Layer label")
        if i < 2:
            shape(g.shapes, MSO_SHAPE.DOWN_ARROW, 6.5, y + 1.12, 0.3, 0.26, fill=MUTED, name="Down arrow")
    inline_chip(s.shapes, 12.73, 5.62, "U", "How it is built: undecided", right=True)
    add_caption(s, "One shared base could run every steam engine. Each engine is described by data.")
    add_number(s, 15)
    return s


# 16 --------------------------------------------------------------------------------
def s16(prs):
    s = new_slide(prs, "Where this stands", "V")
    steps = [("Test engine on the game's rails", "Under way"), ("Cost and recipes", "Planned"),
             ("Range tuning", "Planned"), ("Play-testing", "Planned")]
    pitch = 2.85 + (12.13 - 4 * 2.85) / 3
    cxs = [0.6 + i * pitch + 2.85 / 2 for i in range(4)]
    gl = group(s, "Roadmap line", "A line joining four steps: the first is under way, the rest are planned.")
    line(gl.shapes, cxs[0], 2.1, cxs[-1], 2.1, color=LINE, lw=3, name="Roadmap line")
    for i, cx in enumerate(cxs):
        on = steps[i][1] == "Under way"
        circle(gl.shapes, cx, 2.1, 0.28, fill=ORANGE if on else PANEL, line=ORANGE if on else STEEL, lw=3,
               name="Step marker")
    for i, ((lab, state), cx) in enumerate(zip(steps, cxs)):
        on = state == "Under way"
        g = group(s, "Step: " + lab, "%s: %s." % (lab, state.lower()))
        x = cx - 2.85 / 2
        rrect(g.shapes, x, 2.75, 2.85, 2.45, radius=0.08, fill=PANEL, line=ORANGE if on else None, lw=2,
              name="Step card")
        text(g.shapes, x + 0.22, 2.9, 2.41, 1.3, [[T(lab, 20, True, TEXT)]], anchor="t", inset=(0, 0, 0, 0),
             name="Step label")
        pill = rrect(g.shapes, x + 0.22, 4.4, 1.7, 0.5, radius=0.25, fill=ORANGE if on else None,
                     line=None if on else STEEL, lw=2, name="State: " + state)
        box_text(pill, [[T(state, 18, True, DARK if on else TEXT)]], inset=(0, 0, 0, 0), wrap_=False)
    inline_chip(s.shapes, 12.73, 5.5, "V", "Plans can change.", right=True)
    add_caption(s, "Balance is a plan. It will be tested and tuned by playing.")
    add_number(s, 16)
    return s


# 17 --------------------------------------------------------------------------------
def s17(prs):
    s = new_slide(prs, "Still undecided", "U")
    qs = [("Recipes and costs", "OQ02"), ("Longest track piece", "OQ02"), ("Is Medium the fastest?", "OQ05"),
          ("Engine curves", "OQ05"), ("Wagon list", "OQ07"), ("Which fuels work?", "OQ08"),
          ("Station size", "OQ09"), ("Service stop rules", "OQ11")]
    for i, (q, oq) in enumerate(qs):
        col, row = i % 4, i // 4
        x = 0.6 + col * (2.9 + 0.177)
        y = 1.5 + row * 2.3
        g = group(s, "Open question: " + q, "Undecided: %s (%s)." % (q, oq))
        rrect(g.shapes, x, y, 2.9, 2.05, radius=0.08, fill=PANEL, name="Card")
        inline_chip(g.shapes, x + 0.2, y + 0.2, "U", None, name="Inline chip: Undecided")
        text(g.shapes, x + 0.2, y + 0.78, 2.5, 1.2, [[T(q, 20, True, TEXT), T(" (%s)" % oq, 20, False, MUTED)]],
             anchor="t", inset=(0, 0, 0, 0), name="Question")
    add_caption(s, "These questions are open. Nothing here has been chosen yet.")
    add_number(s, 17)
    return s


# 18 --------------------------------------------------------------------------------
def s18(prs):
    s = new_slide(prs, "Image credits")
    rows = [("Slot", "Slide", "What it shows", "Credit"),
            ("R02", "1", "Render of the mod's two-rail track.",
             "Early Locomotion project (visual development, not final art).")]
    widths = [1.0, 1.0, 4.6, 5.53]
    gf = s.shapes.add_table(len(rows), 4, E(0.6), E(1.5), E(sum(widths)), E(0.7 * len(rows)))
    gf.name = "Credits table"
    set_alt(gf, "Credits table: image R02 on slide 1, an Early Locomotion project render.")
    tbl = gf.table
    tblPr = tbl._tbl.tblPr
    for a in ("firstRow", "bandRow"):
        tblPr.set(a, "0")
    sid = tblPr.find(qn("a:tableStyleId"))
    if sid is None:
        sid = etree.SubElement(tblPr, qn("a:tableStyleId"))
    sid.text = "{2D5ABB26-0587-4C30-8999-92F81FD0307C}"
    for k, w in enumerate(widths):
        tbl.columns[k].width = E(w)
    for r, row in enumerate(rows):
        tbl.rows[r].height = E(0.7)
        for k, val in enumerate(row):
            cell = tbl.cell(r, k)
            cell.fill.solid()
            cell.fill.fore_color.rgb = rgb(PANEL_ALT if r == 0 else PANEL)
            cell.margin_left = cell.margin_right = E(0.12)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            fill_tf(cell.text_frame, [[T(val, 11, r == 0, TEXT)]], "l", "m", True, (0.12, 0.05, 0.12, 0.05))
    add_caption(s, "This deck uses no photographs.")
    add_number(s, 18)
    return s


ALL = [s10, s11, s12, s13, s14, s15, s16, s17, s18]
