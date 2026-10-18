"""Chunk 1: slides 1 to 8."""
from lib import *


def dot(sh, x, y, d=0.16, color=ORANGE):
    return oval(sh, x - d / 2, y - d / 2, d, d, color, None, name="leader dot")


def badge(sh, cx, cy, n, d=0.45):
    return oval(sh, cx - d / 2, cy - d / 2, d, d, ORANGE, None, name="badge", text=str(n), size=18, color=DARK, bold=True)


# ---------------------------------------------------------------- slide 1
def s01(prs):
    s = new_slide(prs, "Coal, Water and Servicing", None, title_size=54,
                  title_box=(0.6, 1.55, 6.6, 2.0))
    s.shapes.title.text_frame.vertical_anchor = MSO_ANCHOR.BOTTOM
    sh = s.shapes
    add_picture_fit(sh, "P17_coal_stage_water_tank_didcot.jpg", 7.55, 0.5, 5.18, 6.4,
                    "A coal stage and a water tank at Didcot Railway Centre.", focus=(0.62, 0.5))
    credit(sh, 7.55, 6.96, 5.18, "Rosser1954, CC BY-SA 4.0. Coal stage and water tank, Didcot.", h=0.22)
    rect(sh, 0.6, 3.75, 1.8, 0.08, ORANGE, None, name="orange rule")
    label(sh, 0.6, 4.05, 6.5, 1.3,
          "How steam locomotives eat, drink and get serviced, and how the mod plans to do it.",
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
    rect(gs, 0.6, 1.5, 8.0, 4.6, PANEL, None, radius=0.08, name="legend panel")
    for i, (k, m) in enumerate(rows):
        y = 1.72 + i * 0.86
        chip(gs, k, 0.95, y, 1.7, 0.4, name="CHIP LEGEND")
        label(gs, 3.0, y - 0.1, 5.4, 0.6, m, 20, TEXT, align="l", name="LEGEND TEXT")
    # sketch of a slide with a tag in the top-right corner
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
    s = new_slide(prs, "What an engine needs", "Background")
    sh = s.shapes
    g = group(sh, "Engine cutaway",
              "Side cutaway of a steam engine. Coal burns in the firebox and heats water in the boiler. "
              "Steam drives a piston and rods turn the wheels. Water is fed into the boiler.")
    gs = g.shapes
    ox, oy = 1.5, 0.78
    X = lambda d: ox + d
    Y = lambda d: oy + d
    # rail and sleepers
    rect(gs, 1.2, Y(5.0), 10.0, 0.07, STEEL, None, name="rail")
    for k in range(25):
        rect(gs, 1.3 + k * 0.4, Y(5.07), 0.12, 0.1, SLEEPER, None, name="sleeper")
    # cab
    rect(gs, X(0.0), Y(1.4), 1.5, 1.9, PANEL_ALT, STEEL, 2.0, name="cab")
    rect(gs, X(-0.12), Y(1.28), 1.74, 0.14, STEEL, None, name="cab roof")
    rect(gs, X(0.25), Y(1.7), 0.55, 0.55, COAL, COAL_LINE, 1.0, name="cab window")
    # boiler shell, steam space, water
    rect(gs, X(1.5), Y(1.9), 6.6, 1.4, "#4F5762", STEEL, 2.5, radius=0.25, name="boiler shell")
    rect(gs, X(2.1), Y(2.5), 5.9, 0.7, WATER, None, radius=0.15, name="water")
    # smokebox, chimney, dome
    rect(gs, X(8.0), Y(1.9), 0.9, 1.4, "#6B7078", STEEL, 2.0, radius=0.12, name="smokebox")
    poly(gs, [(X(8.2), Y(1.9)), (X(8.2), Y(1.25)), (X(8.05), Y(0.95)), (X(8.85), Y(0.95)), (X(8.7), Y(1.25)),
              (X(8.7), Y(1.9))], "#3A3F47", STEEL, 2.0, name="chimney")
    rect(gs, X(3.9), Y(1.68), 0.9, 0.26, STEEL, None, radius=0.1, name="dome")
    # steam puffs from chimney
    oval(gs, X(8.3), Y(0.55), 0.55, 0.3, TEXT, None, alpha=0.85, name="puff")
    oval(gs, X(8.55), Y(0.15), 0.75, 0.38, TEXT, None, alpha=0.85, name="puff")
    # firebox (orange) and coal
    rect(gs, X(0.2), Y(2.2), 1.8, 1.1, ORANGE, None, radius=0.08, name="firebox")
    poly(gs, [(X(0.4), Y(3.3)), (X(0.65), Y(2.98)), (X(0.95), Y(2.86)), (X(1.25), Y(2.98)), (X(1.55), Y(2.92)),
              (X(1.85), Y(3.3))], COAL, COAL_LINE, 1.25, name="coal on grate")
    # steam path: boiler steam space -> smokebox -> cylinder
    poly(gs, [(X(5.0), Y(2.2)), (X(8.45), Y(2.2)), (X(8.45), Y(3.5))], None, TEXT, 3.0, closed=False, name="steam path")
    _ends_tail = gs[-1]
    from lib import _ends
    _ends(_ends_tail, False, True)
    # cylinder and piston
    rect(gs, X(7.8), Y(3.55), 1.1, 0.55, STEEL, None, radius=0.1, name="cylinder")
    rect(gs, X(8.0), Y(3.62), 0.14, 0.41, TEXT, None, name="piston head")
    rect(gs, X(6.8), Y(3.8), 1.2, 0.1, "#D0D4D8", None, name="piston rod")
    rect(gs, X(6.72), Y(3.7), 0.16, 0.3, STEEL, None, name="crosshead")
    # wheels and rods
    centres = [2.3, 3.8, 5.3]
    pins = []
    for cx in centres:
        oval(gs, X(cx) - 0.55, Y(4.45) - 0.55, 1.1, 1.1, COAL, STEEL, 3.0, name="wheel")
        oval(gs, X(cx) - 0.1, Y(4.45) - 0.1, 0.2, 0.2, STEEL, None, name="hub")
        pins.append((X(cx), Y(4.45) - 0.36))
    rect(gs, pins[0][0], pins[0][1] - 0.05, pins[2][0] - pins[0][0], 0.1, "#D0D4D8", None, name="coupling rod")
    line(gs, X(6.8), Y(3.85), pins[2][0], pins[2][1], "#D0D4D8", 6.0, name="connecting rod")
    for px, py in pins:
        oval(gs, px - 0.09, py - 0.09, 0.18, 0.18, ORANGE, None, name="crank pin")
    # water arrow into boiler
    arrow(gs, X(4.0), Y(0.6), X(4.0), Y(1.85), WATER, 4.5, name="water arrow")
    label(gs, X(2.2), Y(0.55), 1.65, 0.4, "Water", 18, WATER, True, align="r", name="water label")
    # badges
    badge(gs, X(0.55), Y(4.05), 1)
    line(gs, X(0.55), Y(3.83), X(0.9), Y(3.1), ORANGE, 2.0, name="leader")
    label(gs, X(0.85), Y(3.82), 1.0, 0.45, "Coal", 18, TEXT, True, align="l", name="badge label")
    badge(gs, X(5.9), Y(1.2), 2)
    line(gs, X(5.9), Y(1.43), X(5.9), Y(2.15), ORANGE, 2.0, name="leader")
    label(gs, X(6.2), Y(0.98), 1.2, 0.45, "Steam", 18, TEXT, True, align="l", name="badge label")
    badge(gs, X(8.6), Y(4.6), 3)
    line(gs, X(8.6), Y(4.38), X(8.6), Y(4.1), ORANGE, 2.0, name="leader")
    label(gs, X(8.9), Y(4.37), 1.2, 0.45, "Piston", 18, TEXT, True, align="l", name="badge label")
    badge(gs, X(6.75), Y(4.6), 4)
    line(gs, X(6.53), Y(4.6), X(5.9), Y(4.6), ORANGE, 2.0, name="leader")
    label(gs, X(7.05), Y(4.37), 1.2, 0.45, "Wheels", 18, TEXT, True, align="l", name="badge label")
    finish(s, "Coal heats water. Steam pushes pistons. The engine needs both coal and water.", 3)
    return s


# ---------------------------------------------------------------- slide 4 (SPEC-A)
def s04(prs):
    s = new_slide(prs, "Steam is used once", "Agreed")
    sh = s.shapes
    g = group(sh, "Tanks before and after",
              "Before a long trip the coal tank and water tank are both nearly full. After it, coal is "
              "about half full and water is almost empty. Steam leaves the chimney and is not used again.")
    gs = g.shapes
    TY, TH, TW = 2.0, 2.6, 1.6
    label(gs, 0.9, 1.5, 3.7, 0.4, "Before", 14, MUTED, True, name="state label")
    label(gs, 7.0, 1.5, 3.7, 0.4, "After", 14, MUTED, True, name="state label")
    # before
    tank_gauge(gs, 0.9, TY, TW, TH, 0.80, COAL, name="coal tank before")
    tank_gauge(gs, 3.0, TY, TW, TH, 0.80, WATER, name="water tank before")
    label(gs, 0.9, TY + TH + 0.05, TW, 0.4, "Coal", 18, TEXT, True, name="tank label")
    label(gs, 3.0, TY + TH + 0.05, TW, 0.4, "Water", 18, TEXT, True, name="tank label")
    # arrow
    arrow(gs, 4.95, 3.3, 6.7, 3.3, ORANGE, 4.5, name="trip arrow")
    label(gs, 4.8, 2.75, 2.05, 0.45, "One long trip", 18, ORANGE, True, name="trip label")
    # after
    tank_gauge(gs, 7.0, TY, TW, TH, 0.45, COAL, name="coal tank after")
    tank_gauge(gs, 9.1, TY, TW, TH, 0.15, WATER, name="water tank after")
    label(gs, 7.0, TY + TH + 0.05, TW, 0.4, "Coal", 18, TEXT, True, name="tank label")
    label(gs, 9.1, TY + TH + 0.05, TW, 0.4, "Water", 18, TEXT, True, name="tank label")
    # red tag on the water tank
    rect(gs, 9.25, 2.3, 1.3, 0.4, RED, None, radius=0.1, name="empty tag", text="Empty first", size=14, color=DARK,
         bold=True)
    arrow(gs, 9.9, 2.72, 9.9, 3.95, RED, 2.25, name="tag pointer")
    # chimney and steam
    rect(gs, 11.55, 3.55, 0.5, 1.05, STEEL, None, name="chimney")
    rect(gs, 11.4, 3.45, 0.8, 0.14, STEEL, None, name="chimney lip")
    oval(gs, 11.55, 3.0, 0.5, 0.28, TEXT, None, alpha=0.85, name="steam")
    oval(gs, 11.65, 2.55, 0.7, 0.36, TEXT, None, alpha=0.85, name="steam")
    oval(gs, 11.75, 2.0, 0.9, 0.46, TEXT, None, alpha=0.85, name="steam")
    label(gs, 10.9, 4.68, 1.85, 1.1, "Steam leaves the chimney. It is not used again.", 14, TEXT, align="c",
          anchor="t", name="steam label")
    # note
    rect(gs, 1.5, 5.45, 7.8, 0.55, PANEL, ORANGE, 1.5, radius=0.1, name="note",
         text="In the mod, water is usually the tighter limit.", size=18, color=TEXT)
    finish(s, "Steam is used once and lost. So water runs out first. Coal lasts longer.", 4)
    return s


# ---------------------------------------------------------------- slide 5
def s05(prs):
    s = new_slide(prs, "Tender or tank?", "Background")
    sh = s.shapes
    cy, cw, ch = 1.45, 5.8, 3.9
    # left card
    add_picture_fit(sh, "P04_tender_engine_73082.jpg", 0.6, cy, cw, ch,
                    "BR Standard Class 5 No. 73082 'Camelot', a tender engine, seen from the side.")
    add_picture_fit(sh, "P05_tank_engine_80151.jpg", 6.93, cy, cw, ch,
                    "BR Standard Class 4 tank engine No. 80151 from the side, showing side tanks and rear bunker.")
    g = group(sh, "Photo labels", "Labels pointing at the tender behind the cab, and at the side tanks and bunker.")
    gs = g.shapes
    rect(gs, 0.8, cy + 0.15, 2.4, 0.45, PANEL, ORANGE, 2.0, radius=0.08, name="card name", text="Tender engine",
         size=18, color=TEXT, bold=True)
    rect(gs, 7.13, cy + 0.15, 2.2, 0.45, PANEL, ORANGE, 2.0, radius=0.08, name="card name", text="Tank engine",
         size=18, color=TEXT, bold=True)
    # tender label + leader (tender is the wagon behind the cab, at the left of photo 1)
    rect(gs, 0.85, 4.45, 3.1, 0.75, PANEL, ORANGE, 2.0, radius=0.08, name="callout",
         text="Tender: coal and water behind the cab", size=16, color=TEXT)
    line(gs, 1.9, 4.45, 1.55, 3.55, ORANGE, 2.25, name="leader")
    dot(gs, 1.55, 3.55)
    # tank label + leaders
    rect(gs, 7.1, 4.45, 4.0, 0.75, PANEL, ORANGE, 2.0, radius=0.08, name="callout",
         text="Side tanks: water. Bunker: coal.", size=16, color=TEXT)
    line(gs, 8.4, 4.45, 9.3, 3.5, ORANGE, 2.25, name="leader")
    dot(gs, 9.3, 3.5)
    line(gs, 10.4, 4.45, 10.95, 3.5, ORANGE, 2.25, name="leader")
    dot(gs, 10.95, 3.5)
    credit(sh, 0.6, cy + ch + 0.05, cw, "www.mgaylard.co.uk, CC BY 2.0. BR Standard Class 5 No. 73082.")
    credit(sh, 6.93, cy + ch + 0.05, cw, "www.mgaylard.co.uk, CC BY 2.0. BR Standard Class 4 No. 80151.")
    finish(s, "A tender engine pulls a coal and water wagon. A tank engine carries both itself.", 5)
    return s


# ---------------------------------------------------------------- slide 6 (SPEC-B)
def s06(prs):
    s = new_slide(prs, "Taking on water", "Background")
    sh = s.shapes
    add_picture_fit(sh, "P06_water_crane_didcot.jpg", 0.6, 1.45, 3.7, 4.4,
                    "A water crane at Didcot Railway Centre.", focus=(0.5, 0.0))
    credit(sh, 0.6, 5.9, 3.7, "Barry Skeates, CC BY 2.0. A water crane, Didcot.")
    g = group(sh, "Water tower and crane",
              "A water tank on legs feeds a pipe down to a crane. The crane arm swings over the "
              "tender hatch and water flows down by gravity.")
    gs = g.shapes
    # tower
    rect(gs, 4.9, 1.7, 1.9, 1.2, WATER, "#FFFFFF", 2.0, radius=0.12, name="tank", text="Water tank", size=14,
         color=DARK, bold=True)
    for lx in (5.0, 5.4, 6.2, 6.6):
        rect(gs, lx, 2.9, 0.1, 1.6, STEEL, None, name="leg")
    line(gs, 5.05, 3.0, 6.65, 4.4, STEEL, 1.5, name="brace")
    line(gs, 6.65, 3.0, 5.05, 4.4, STEEL, 1.5, name="brace")
    # pipe from tank to crane column
    rect(gs, 6.8, 2.58, 0.9, 0.12, WATER, None, name="pipe")
    rect(gs, 7.55, 2.58, 0.15, 2.55, WATER, None, name="crane column")
    # swing arm and spout
    rect(gs, 7.55, 3.0, 1.6, 0.14, WATER, None, name="swing arm")
    rect(gs, 9.05, 3.0, 0.12, 0.62, WATER, None, name="spout")
    # tender with hatch, wheels, rail
    rect(gs, 7.95, 3.95, 2.4, 0.8, STEEL, None, radius=0.04, name="tender")
    label(gs, 7.95, 4.35, 1.0, 0.35, "Tender", 14, DARK, True, name="tender label")
    oval(gs, 8.89, 3.78, 0.35, 0.35, COAL, TEXT, 2.0, name="hatch")
    rect(gs, 7.7, 5.15, 3.0, 0.07, STEEL, None, name="rail")
    for wx in (8.5, 9.8):
        oval(gs, wx - 0.2, 4.75, 0.4, 0.4, COAL, STEEL, 2.0, name="wheel")
    # gravity arrows
    arrow(gs, 7.25, 3.2, 7.25, 3.95, TEXT, 2.25, name="gravity arrow")
    arrow(gs, 7.4, 3.2, 7.4, 3.95, TEXT, 2.25, name="gravity arrow")
    label(gs, 6.4, 4.05, 1.4, 0.35, "Gravity", 14, TEXT, True, align="c", name="gravity label")
    # curved arrow over the crane top
    curve(gs, (7.5, 2.4), (8.35, 1.5), (9.2, 2.4), ORANGE, 2.5, name="swing arrow")
    label(gs, 7.2, 1.45, 3.3, 0.4, "Arm swings over the hatch", 14, ORANGE, True, name="swing label")
    # P07 inset
    add_picture_fit(sh, "P07_water_tower_signal.jpg", 10.5, 3.9, 2.23, 1.6,
                    "A water tower with a signal beside it.", focus=(0.5, 0.33))
    credit(sh, 10.5, 5.53, 2.23, "David Merrett, CC BY 2.0")
    finish(s, "A water crane swings over the engine. Water flows down from a tank above.", 6)
    return s


# ---------------------------------------------------------------- slide 7 (SPEC-C)
def s07(prs):
    s = new_slide(prs, "Taking on coal", "Background")
    sh = s.shapes
    add_picture_fit(sh, "P08_coaling_stage_didcot.jpg", 0.6, 1.45, 4.6, 4.4,
                    "A raised coaling stage at the Great Western Society site, Didcot.", focus=(0.4, 0.5))
    credit(sh, 0.6, 5.9, 4.6, "Gillett's Crossing, CC BY 2.0. A coaling stage, Didcot.")
    g = group(sh, "Coal stage and coaling tower",
              "Two ways to fill a tender with coal. A coal stage is a raised platform with a chute. "
              "A coaling tower has a hopper above the tender. Gravity does the work.")
    gs = g.shapes
    # --- coal stage
    label(gs, 5.5, 1.4, 3.0, 0.35, "Coal stage", 18, ORANGE, True, align="l", name="diagram title")
    rect(gs, 5.5, 3.25, 7.2, 0.07, STEEL, None, name="rail")
    poly(gs, [(6.0, 2.2), (6.5, 1.95), (6.9, 1.8), (7.3, 1.9), (7.7, 1.85), (8.1, 2.2)], COAL, "#B5BBC2", 2.0,
         name="coal heap")
    rect(gs, 5.6, 2.2, 3.2, 0.14, STEEL, None, name="platform")
    for px in (5.7, 6.7, 7.7, 8.6):
        rect(gs, px, 2.34, 0.1, 0.91, STEEL, None, name="post")
    poly(gs, [(8.8, 2.2), (10.2, 2.6), (10.2, 2.74), (8.8, 2.34)], WAGON, STEEL, 1.5, name="chute")
    rect(gs, 9.2, 2.8, 2.2, 0.45, STEEL, None, radius=0.04, name="tender")
    rect(gs, 9.3, 2.75, 2.0, 0.08, COAL, COAL_LINE, 1.0, name="coal in tender")
    for wx in (9.6, 11.0):
        oval(gs, wx - 0.16, 3.1, 0.32, 0.32, COAL, STEEL, 1.5, name="wheel")
    arrow(gs, 9.15, 2.0, 9.9, 2.22, TEXT, 2.25, name="gravity arrow")
    label(gs, 8.6, 1.5, 1.6, 0.4, "Gravity", 14, TEXT, True, name="gravity label")
    # --- coaling tower
    label(gs, 5.5, 3.5, 3.0, 0.35, "Coaling tower", 18, ORANGE, True, align="l", name="diagram title")
    rect(gs, 5.5, 5.98, 4.2, 0.07, STEEL, None, name="rail")
    rect(gs, 6.35, 3.9, 1.0, 1.3, STEEL, None, name="tower")
    rect(gs, 6.45, 3.8, 0.8, 0.12, "#6B7078", None, name="tower cap")
    rect(gs, 6.55, 4.1, 0.25, 0.3, COAL, COAL_LINE, 1.0, name="tower window")
    poly(gs, [(6.35, 5.2), (7.35, 5.2), (7.0, 5.55), (6.7, 5.55)], "#6B7078", STEEL, 1.5, name="hopper")
    rect(gs, 5.75, 5.6, 2.2, 0.38, STEEL, None, radius=0.04, name="tender")
    rect(gs, 5.85, 5.55, 2.0, 0.07, COAL, COAL_LINE, 1.0, name="coal in tender")
    for wx in (6.1, 7.55):
        oval(gs, wx - 0.14, 5.82, 0.28, 0.28, COAL, STEEL, 1.5, name="wheel")
    # P09 inset
    add_picture_fit(sh, "P09_coaling_tower_carnforth.jpg", 10.3, 4.75, 2.43, 0.92,
                    "A tall coaling tower and a water tower at Carnforth.")
    credit(sh, 10.3, 5.7, 2.43, "kitmasterbloke, CC BY 4.0")
    finish(s, "Coal starts higher than the tender. A ramp or tower lets gravity fill it.", 7)
    return s


# ---------------------------------------------------------------- slide 8
def s08(prs):
    s = new_slide(prs, "How far can an engine go?", "Agreed")
    sh = s.shapes
    g = group(sh, "Gauges and range card",
              "A coal gauge and a water gauge for one engine feed a card called Range left, "
              "shown as a dial with no number.")
    gs = g.shapes
    TY, TH, TW = 1.7, 3.1, 1.5
    tank_gauge(gs, 1.2, TY, TW, TH, 0.60, COAL, name="coal gauge")
    tank_gauge(gs, 3.4, TY, TW, TH, 0.40, WATER, name="water gauge")
    label(gs, 1.2, TY + TH + 0.08, TW, 0.4, "Coal", 18, TEXT, True, name="gauge label")
    label(gs, 3.4, TY + TH + 0.08, TW, 0.4, "Water", 18, TEXT, True, name="gauge label")
    arrow(gs, 5.25, 3.25, 6.55, 3.25, ORANGE, 4.5, name="flow arrow")
    # card
    rect(gs, 6.8, 1.7, 5.7, 3.9, PANEL, ORANGE, 2.0, radius=0.1, name="card")
    label(gs, 7.1, 1.85, 5.1, 0.55, "Range left", 24, TEXT, True, align="l", name="card title")
    cx, cy = 9.65, 4.15
    poly(gs, arc_poly(cx, cy, 1.55, 1.2, 0, 180), STEEL, None, name="dial ring")
    for a in (180, 135, 90, 45, 0):
        import math
        r = math.radians(a)
        line(gs, cx + 1.02 * math.cos(r), cy - 1.02 * math.sin(r), cx + 1.18 * math.cos(r),
             cy - 1.18 * math.sin(r), TEXT, 2.5, name="tick")
    r = math.radians(60)
    line(gs, cx, cy, cx + 1.0 * math.cos(r), cy - 1.0 * math.sin(r), ORANGE, 5.0, name="needle")
    oval(gs, cx - 0.14, cy - 0.14, 0.28, 0.28, ORANGE, None, name="hub")
    ichip(gs, "Agreed", 7.35, 4.85, 4.6, "Range estimate: Agreed direction", h=0.4)
    finish(s, "Range comes from real tank sizes and real use, not a distance countdown.", 8)
    return s


SLIDES = [s01, s02, s03, s04, s05, s06, s07, s08]
