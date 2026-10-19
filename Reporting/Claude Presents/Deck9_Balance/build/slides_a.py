"""Deck 9, chunk 1: slides 1 to 9."""
import math
from lib import *

import os
IMG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "images") + os.sep


# 1 ---------------------------------------------------------------------------------
def s01(prs):
    s = prs.slides.add_slide(prs.slide_layouts[5])
    s.background.fill.solid(); s.background.fill.fore_color.rgb = rgb(BG)
    t = s.shapes.title
    t.left, t.top, t.width, t.height = E(0.6), E(1.35), E(6.5), E(2.1)
    fill_tf(t.text_frame, [[T("How the Mod Is Balanced", 54, True, TEXT)]], "l", "b", True, (0, 0, 0, 0),
            spacing=0.95)
    rect(s.shapes, 0.6, 3.68, 2.2, 0.09, fill=ORANGE, name="Orange rule")
    text(s.shapes, 0.6, 3.98, 6.3, 1.4,
         [[T("Why steam is cheap to start, and what keeps it from being too easy.", 20, False, TEXT)]],
         inset=(0, 0, 0, 0), name="Caption text")
    add_picture_cover(s, IMG + "R02_track_hero_hd_v004.jpg", 7.6, 0.55, 5.13, 6.2, cx=0.45,
                      descr="High-detail render of the mod's two-rail track. Visual development only: "
                            "not Unreal-tested, not production-ready.", name="Picture R02")
    text(s.shapes, 7.6, 6.82, 5.13, 0.4,
         [[T("Early Locomotion project render (visual development, not final art).", 10, False, MUTED)]],
         inset=(0, 0, 0, 0), name="Credit line R02")
    return s


# 2 ---------------------------------------------------------------------------------
def s02(prs):
    s = new_slide(prs, "How to read this guide")
    rows = [("A", "Decided."), ("P", "Suggested, not confirmed."), ("V", "A test number that may change."),
            ("U", "Still an open question."), ("B", "A real-world fact.")]
    for i, (st, meaning) in enumerate(rows):
        y = 1.5 + i * 0.9
        g = group(s, "Legend row: " + CHIPS[st][0].title(),
                  "Legend row: the %s tag means '%s'" % (CHIPS[st][0].title(), meaning))
        rrect(g.shapes, 0.6, y, 12.13, 0.75, radius=0.08, fill=PANEL, name="Row panel")
        chip_at(g.shapes, 0.95, y + 0.175, st, name="Legend chip: " + CHIPS[st][0].title())
        text(g.shapes, 3.0, y, 9.4, 0.75, [[T(meaning, 20, False, TEXT)]], anchor="m", inset=(0, 0, 0, 0),
             name="Legend meaning")
    add_caption(s, "Every idea carries a tag in the top-right corner.")
    add_number(s, 2)
    return s


# 3 ---------------------------------------------------------------------------------
def s03(prs):
    s = new_slide(prs, "Cheap to start", "A")
    g = group(s, "Diagram: cost against effort",
              "Two bars: the cost to build is short, the effort to run is long.")
    rrect(g.shapes, 0.6, 1.5, 12.13, 4.3, radius=0.08, fill=PANEL, name="Panel")
    for i, (lab, frac, col) in enumerate([("Cost to build", 0.2, STEEL), ("Effort to run", 0.86, ORANGE)]):
        y = 2.2 + i * 1.5
        text(g.shapes, 1.0, y, 3.1, 0.95, [[T(lab, 20, True, TEXT)]], anchor="m", inset=(0, 0, 0, 0),
             name="Bar label")
        rrect(g.shapes, 4.3, y, 8.0, 0.95, radius=0.1, fill=PANEL_ALT, name="Bar track")
        rrect(g.shapes, 4.3, y, 8.0 * frac, 0.95, radius=0.1, fill=col, name="Bar")
    text(g.shapes, 8.3, 5.2, 4.0, 0.4, [[T("Not to scale", 14, False, MUTED)]], align="r", anchor="m",
         inset=(0, 0, 0, 0), name="Scale note")
    add_caption(s, "Early rail is cheap and easy to build. The challenge is running it.")
    add_number(s, 3)
    return s


# 4 ---------------------------------------------------------------------------------
def s04(prs):
    s = new_slide(prs, "Cheap track and trains", "A")
    g = group(s, "Diagram: how track is made",
              "An iron plate and an iron rod arrow into a piece of two-rail track.")
    rrect(g.shapes, 0.6, 1.5, 6.0, 4.45, radius=0.08, fill=PANEL, name="Panel")
    # plate
    rrect(g.shapes, 1.0, 1.85, 1.7, 1.1, radius=0.06, fill=STEEL, name="Iron plate")
    rrect(g.shapes, 1.1, 1.95, 1.5, 0.9, radius=0.04, fill="B8BEC4", name="Plate face")
    for dx, dy in ((1.2, 2.05), (2.4, 2.05), (1.2, 2.65), (2.4, 2.65)):
        circle(g.shapes, dx, dy, 0.05, fill=STEEL, name="Rivet")
    label(g.shapes, 1.0, 3.0, 1.7, 0.4, "Iron plate", 18, True)
    # rod
    rrect(g.shapes, 1.0, 4.0, 1.7, 0.16, radius=0.08, fill=STEEL, name="Iron rod")
    rect(g.shapes, 1.0, 4.04, 1.7, 0.04, fill="B8BEC4", name="Rod highlight")
    label(g.shapes, 1.0, 4.3, 1.7, 0.4, "Iron rod", 18, True)
    # arrows into the track piece
    line(g.shapes, 2.9, 2.4, 3.75, 3.3, color=ORANGE, tail="triangle", name="Arrow plate")
    line(g.shapes, 2.9, 4.08, 3.75, 3.75, color=ORANGE, tail="triangle", name="Arrow rod")
    rails(g.shapes, 3.9, 3.15, 2.3, gauge=0.42, pitch=0.36)
    label(g.shapes, 3.9, 3.95, 2.3, 0.4, "Track", 18, True)
    inline_chip(g.shapes, 0.9, 5.3, "U", "Exact recipes: undecided (OQ02)")
    # trains
    g2 = group(s, "Diagram: steam train and pricier electric train",
               "A steam train with a short coin stack beside an electric train with a tall coin stack: "
               "steam trains cost less.")
    rrect(g2.shapes, 6.85, 1.5, 5.88, 4.45, radius=0.08, fill=PANEL, name="Panel")
    sc = 0.75
    base = 3.2
    x = 7.1
    loco(g2.shapes, x, base - 1.4 * sc, sc)
    x += 2.6 * sc + 0.06
    for _ in range(2):
        x += wagon(g2.shapes, x, base - 0.84 * sc, sc) + 0.06
    rect(g2.shapes, 7.0, base + 0.02, 4.5, 0.05, fill=LINE, name="Ground")
    label(g2.shapes, 7.1, 3.35, 3.0, 0.4, "Steam train", 18, True, align="l")
    coin_stack(g2.shapes, 11.6, base - 2 * 0.17, 2, w=0.85, h=0.17)
    line(g2.shapes, 7.0, 4.0, 12.5, 4.0, color=LINE, lw=1.5, name="Divider")
    electric_train(g2.shapes, 7.1, 4.3, 0.75, n_cars=2)
    label(g2.shapes, 7.1, 5.4, 3.0, 0.4, "Electric train", 18, True, align="l")
    coin_stack(g2.shapes, 11.6, 5.15 - 5 * 0.17, 5, w=0.85, h=0.17)
    add_caption(s, "Track is made from iron plates and rods. Trains cost less than the game's own.")
    add_number(s, 4)
    return s


# 5 ---------------------------------------------------------------------------------
def s05(prs):
    s = new_slide(prs, "Long pieces, few clicks", "A")
    g = group(s, "Diagram: one long track piece",
              "One long curved piece of track in a single placement.")
    rrect(g.shapes, 0.6, 1.5, 5.9, 4.45, radius=0.08, fill=PANEL, name="Panel")
    pts = arc_pts(6.3, 6.5, 4.5, 196, 262, n=30)
    curved_track(g.shapes, pts, gauge=0.34, sleeper_len=0.64, n_sleepers=15)
    label(g.shapes, 0.9, 5.45, 3.2, 0.4, "One long piece", 18, True, align="l", inset=(0, 0, 0, 0))
    g2 = group(s, "Diagram: many short pieces crossed out",
               "A pile of many short pieces of track with a red cross over it: not needed.")
    rrect(g2.shapes, 6.85, 1.5, 5.88, 4.45, radius=0.08, fill=PANEL, name="Panel")
    for i in range(6):
        gx = 7.9 + (0.25 if i % 2 else -0.1) 
        rails(g2.shapes, gx, 1.85 + i * 0.5, 2.7, gauge=0.22, pitch=0.3)
    x_mark(g2.shapes, 9.55, 3.55, 1.3, color=RED, lw=8)
    label(g2.shapes, 7.1, 5.45, 3.4, 0.4, "Many short pieces", 18, True, align="l", inset=(0, 0, 0, 0))
    add_caption(s, "Track can be laid in long pieces. The challenge is the trains, not the clicking.")
    add_number(s, 5)
    return s


# 6 ---------------------------------------------------------------------------------
def s06(prs):
    s = new_slide(prs, "A 150 metre experiment", "P")
    g = group(s, "Diagram: a ruler along a curved track",
              "A ruler marked 150 m laid along a curved piece of track, with a question mark: "
              "the limit is only an experiment.")
    rrect(g.shapes, 0.6, 1.5, 12.13, 4.45, radius=0.08, fill=PANEL, name="Panel")
    cx, cy = 6.55, 9.3
    a0, a1 = 236, 304
    curved_track(g.shapes, arc_pts(cx, cy, 6.9, a0, a1, n=36), gauge=0.34, sleeper_len=0.64, n_sleepers=26)
    ro, ri = 6.1, 5.55
    outer = arc_pts(cx, cy, ro, a0, a1, n=36)
    inner = arc_pts(cx, cy, ri, a1, a0, n=36)
    poly(g.shapes, outer + inner, fill=AMBER, line=DARK, lw=1.5, name="Ruler")
    for k in range(0, 31):
        a = a0 + (a1 - a0) * k / 30
        rr = ro - (0.34 if k % 5 == 0 else 0.2)
        line(g.shapes, cx + ro * math.cos(math.radians(a)), cy + ro * math.sin(math.radians(a)),
             cx + rr * math.cos(math.radians(a)), cy + rr * math.sin(math.radians(a)), color=DARK, lw=1.5,
             name="Tick")
    label(g.shapes, 5.35, 3.95, 2.4, 0.5, "150 m", 20, True, color=AMBER)
    q = circle(g.shapes, 11.55, 2.85, 0.45, fill=None, line=ORANGE, lw=3, name="Question mark")
    box_text(q, [[T("?", 32, True, ORANGE)]], inset=(0, 0, 0, 0), wrap_=False)
    label(g.shapes, 11.6, 5.35, 0.95, 0.4, "OQ02", 14, False, color=MUTED, align="r")
    add_caption(s, "A 150 metre piece limit is only an experiment. It may not work.")
    add_number(s, 6)
    return s


# 7 ---------------------------------------------------------------------------------
def s07(prs):
    s = new_slide(prs, "Every transport has a job", "A")
    lanes = [("Belts:", " permanent short and medium links", STEEL, "belt"),
             ("Tractors:", " flexible, little infrastructure", AMBER, "tractor"),
             ("Steam:", " early long-distance bulk", ORANGE, "steam"),
             ("Electric:", " mature speed and throughput", ELEC, "electric")]
    for i, (nm, desc, col, kind) in enumerate(lanes):
        y = 1.45 + i * 1.17
        g = group(s, "Lane: " + nm.strip(":"), "%s%s" % (nm, desc))
        rrect(g.shapes, 0.6, y, 12.13, 1.05, radius=0.08, fill=PANEL, name="Lane panel")
        rect(g.shapes, 0.6, y + 0.1, 0.1, 0.85, fill=col, name="Lane accent")
        ix = 1.05
        if kind == "belt":
            rrect(g.shapes, ix, y + 0.55, 2.5, 0.3, radius=0.15, fill=COAL, line=STEEL, lw=1.5, name="Belt")
            for k in range(6):
                shape(g.shapes, MSO_SHAPE.CHEVRON, ix + 0.2 + k * 0.38, y + 0.62, 0.18, 0.16, fill=STEEL,
                      name="Chevron")
            rect(g.shapes, ix + 0.4, y + 0.3, 0.3, 0.25, fill=AMBER, line=DARK, lw=1, name="Crate")
            rect(g.shapes, ix + 1.5, y + 0.3, 0.3, 0.25, fill=AMBER, line=DARK, lw=1, name="Crate")
        elif kind == "tractor":
            rrect(g.shapes, ix + 0.3, y + 0.5, 1.5, 0.3, radius=0.06, fill=AMBER, name="Tractor body")
            rrect(g.shapes, ix + 0.4, y + 0.22, 0.65, 0.3, radius=0.05, fill=AMBER, line=DARK, lw=1,
                  name="Cab")
            rect(g.shapes, ix + 1.55, y + 0.3, 0.07, 0.25, fill=COAL, name="Exhaust")
            wheel(g.shapes, ix + 0.62, y + 0.75, 0.24)
            wheel(g.shapes, ix + 1.55, y + 0.82, 0.16)
        elif kind == "steam":
            loco(g.shapes, ix + 0.35, y + 0.17, 0.6)
        else:
            electric_train(g.shapes, ix + 0.3, y + 0.15, 0.6)
        text(g.shapes, 4.0, y, 8.5, 1.05, [[T(nm, 20, True, TEXT), T(desc, 20, False, TEXT)]], anchor="m",
             inset=(0, 0, 0, 0), name="Lane label")
    add_caption(s, "Belts, tractors, steam and electric rail each have a job. "
                   "Electric leads when the factory matures.")
    add_number(s, 7)
    return s


# 8 ---------------------------------------------------------------------------------
def s08(prs):
    s = new_slide(prs, "Pick the right engine", "A")
    specs = [("Struggles", RED, "A small engine with a very long train: it struggles."),
             ("Wasteful", AMBER, "A large engine with a single wagon: wasteful."),
             ("Fits", GREEN, "A well-matched engine and train: it fits.")]
    for i, (word, col, descr) in enumerate(specs):
        y = 1.45 + i * 1.57
        g = group(s, "Row: " + word, descr)
        rrect(g.shapes, 0.6, y, 12.13, 1.45, radius=0.08, fill=PANEL, name="Row panel")
        pill = rrect(g.shapes, 0.85, y + 0.47, 1.9, 0.5, radius=0.25, fill=col, name="Verdict: " + word)
        box_text(pill, [[T(word, 18, True, DARK)]], inset=(0, 0, 0, 0), wrap_=False)
        base = y + 1.28
        rect(g.shapes, 3.1, base + 0.01, 9.4, 0.05, fill=LINE, name="Rail")
        x = 3.15
        if i == 0:
            sc = 0.45
            loco(g.shapes, x, base - 1.4 * sc, sc)
            x += 2.6 * sc + 0.05
            for _ in range(11):
                x += wagon(g.shapes, x, base - 0.84 * sc, sc) + 0.04
        elif i == 1:
            sc = 0.8
            loco(g.shapes, x, base - 1.4 * sc, sc, tender=True)
            x += 4.0 * sc + 0.05
            wagon(g.shapes, x, base - 0.84 * sc, sc)
        else:
            sc = 0.65
            loco(g.shapes, x, base - 1.4 * sc, sc, tender=True)
            x += 4.0 * sc + 0.05
            for _ in range(4):
                x += wagon(g.shapes, x, base - 0.84 * sc, sc) + 0.05
    add_caption(s, "Pick the engine for the load. A big engine on one wagon wastes effort.")
    add_number(s, 8)
    return s


# 9 ---------------------------------------------------------------------------------
def s09(prs):
    s = new_slide(prs, "How engines may feel", "P")
    cards = [("Small", "A few wagons, confidently; struggles on hills", 0.7, False),
             ("Medium", "Speed and range; burns more", 0.78, True),
             ("Large", "Heavy hauling; slow to speed up; thirsty", 0.85, True)]
    for i, (nm, desc, sc, tender) in enumerate(cards):
        x = 0.6 + i * (3.85 + 0.29)
        g = group(s, "Card: " + nm, "%s engine: %s." % (nm, desc))
        rrect(g.shapes, x, 1.5, 3.85, 3.35, radius=0.08, fill=PANEL, name="Card panel")
        text(g.shapes, x + 0.25, 1.62, 3.35, 0.5, [[T(nm, 22, True, ORANGE)]], anchor="m", inset=(0, 0, 0, 0),
             name="Card title")
        w = (4.0 if tender else 2.6) * sc
        loco(g.shapes, x + (3.85 - w) / 2, 3.45 - 1.4 * sc, sc, tender=tender)
        rect(g.shapes, x + 0.25, 3.47, 3.35, 0.04, fill=LINE, name="Rail")
        text(g.shapes, x + 0.25, 3.75, 3.35, 1.0, [[T(desc, 18, False, TEXT)]], anchor="t",
             inset=(0, 0, 0, 0), name="Card text")
    label(s.shapes, 0.6, 5.12, 4.5, 0.4, "Shape only. Not measured.", 14, False, color=MUTED, align="l", inset=(0, 0, 0, 0))
    inline_chip(s.shapes, 12.73, 5.1, "U", "Exact curves: undecided", right=True)
    add_caption(s, "Small is nimble, Medium is quick, Large is strong. These are ideas about their character.")
    add_number(s, 9)
    return s


ALL = [s01, s02, s03, s04, s05, s06, s07, s08, s09]
