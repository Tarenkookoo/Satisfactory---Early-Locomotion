"""Slides 10 to 18 of Deck 2 (lever frame, rods, interlocking, boxes, the mod's blocks and limits)."""
from lib import *

RED_T, GREEN_T, AMBER_T = C["red_text"], C["green"], C["amber"]
GREY_LEVER = "#B8BEC6"


# ------------------------------------------------------------------------------------------ 10
def s10(d):
    c = d.slide(10, "The lever frame", "B")
    sh = c.shapes
    g = group(sh, "Lever frame cutaway",
              "A cutaway of a two-floor signal box. On the operating floor a signaller stands behind a row of "
              "eight colour-coded levers. On the lower floor eight thin rods leave the left wall towards the track.")
    gs = g.shapes
    bx, by, bw, bh = 5.2, 1.45, 7.53, 4.65
    rect(gs, bx, by, bw, bh, fill=C["panel"], line=C["orange"], line_w=2, radius=0.08)
    floor_y = 3.95
    line(gs, bx, floor_y, bx + bw, floor_y, C["steel"], 4)
    for i in range(4):  # window strip
        rect(gs, 7.3 + i * 1.3, 1.6, 1.2, 0.45, fill=C["blue"], alpha=40, line=C["post"], line_w=1.5)
    textbox(gs, bx + 0.15, 1.55, 1.9, 0.35, "Operating floor", 14, C["muted"], bold=True)
    # track-diagram board
    rect(gs, 7.4, 2.2, 4.45, 0.5, fill=C["post"], radius=0.04)
    line(gs, 7.6, 2.52, 11.65, 2.52, C["coal"], 2)
    poly(gs, [(9.0, 2.52), (9.4, 2.34), (11.2, 2.34)], line_c=C["coal"], line_w=2, close=False)
    person_icon(gs, 6.2, 3.9, scale=1.7)
    cols = [C["red"]] * 3 + [C["amber"]] * 2 + [GREY_LEVER] * 2 + [C["blue"]]
    xs = [7.5 + i * 0.62 for i in range(8)]
    for x, col in zip(xs, cols):
        lever(gs, x, 3.85, col, scale=1.15)
    # lower floor: eight thin lines leaving the left wall
    for i, x in enumerate(xs):
        y = 4.25 + i * 0.2
        poly(gs, [(x, floor_y + 0.02), (x, y), (bx - 0.3, y)], line_c=C["orange"], line_w=1.5, close=False)
    textbox(gs, bx + 0.15, 5.72, 1.9, 0.33, "Lower floor", 14, C["muted"], bold=True)
    # key
    rect(gs, 0.6, 1.45, 4.3, 2.52, fill=C["panel"], line=C["line"], line_w=1, radius=0.08)
    for i, (col, lab) in enumerate([(C["red"], "Stop signals"), (C["amber"], "Distant signals"),
                                    (GREY_LEVER, "Points"), (C["blue"], "Lock")]):
        y = 1.55 + i * 0.46
        rect(gs, 0.85, y + 0.04, 0.16, 0.34, fill=col, line=C["ink"], line_w=0.75)
        textbox(gs, 1.2, y, 3.5, 0.42, lab, 18, C["text"], bold=True)
    textbox(gs, 0.85, 3.52, 3.9, 0.35, "Example colours; not fixed", 14, C["muted"], bold=True)
    picture(sh, "P15_lever_frame_didcot.jpg", 1.45, 4.1, 2.6, 1.8,
            "Lever frame and workings inside a signal box at Didcot Railway Centre.")
    credit(sh, 1.45, 5.93, 2.6, "Nigel Brown, CC BY-SA 2.0. Wikimedia Commons.", h=0.3)
    c.finish("Each lever works one signal or one set of points.")


# ------------------------------------------------------------------------------------------ 11
def _node(gs, x, y, w, h, text, fill=None):
    r = rect(gs, x, y, w, h, fill=fill or C["panel"], line=C["orange"], line_w=2, radius=0.08)
    set_text(r, text, 18, C["text"], bold=True, align="c", margins=(0.03, 0.02, 0.03, 0.02))
    set_name(r, f"Step: {text}")
    return r


def s11(d):
    c = d.slide(11, "Rods and wires", "B")
    sh = c.shapes
    picture(sh, "P16_williton_rods_wires.jpg", 0.6, 1.5, 5.2, 3.5,
            "Pulleys, rods and wires of mechanical signal linkage beside the track at Williton station.")
    credit(sh, 0.6, 5.04, 5.2, "mattbuck (category), CC BY-SA 3.0. Wikimedia Commons.", h=0.3)
    g = group(sh, "From lever to arm",
              "A chain from left to right: lever, rod, pulley, wire, arm. A second branch runs from the rod to "
              "the points.")
    gs = g.shapes
    w, gap, y = 1.1, 0.27, 2.55
    xs = [6.15 + i * (w + gap) for i in range(5)]
    for x, t in zip(xs, ["Lever", "Rod", "Pulley", "Wire", "Arm"]):
        _node(gs, x, y, w, 0.75, t)
    for a, b in zip(xs[:-1], xs[1:]):
        arrow(gs, a + w + 0.02, y + 0.375, b - 0.02, y + 0.375, C["orange"], 2.25)
    _node(gs, xs[1], 4.2, w, 0.75, "Points")
    arrow(gs, xs[1] + w / 2, y + 0.75 + 0.02, xs[1] + w / 2, 4.18, C["orange"], 2.25)
    c.finish("Rods and wires carry the movement out to the track.")


# ------------------------------------------------------------------------------------------ 12
def _track_line(gs, p1, p2, off=0.14):
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    n = math.hypot(dx, dy)
    ox, oy = -dy / n * off, dx / n * off
    for s in (1, -1):
        line(gs, p1[0] + s * ox, p1[1] + s * oy, p2[0] + s * ox, p2[1] + s * oy, C["steel"], 3)
    steps = int(n / 0.3)
    for k in range(steps + 1):
        t = k / steps
        px, py = p1[0] + dx * t, p1[1] + dy * t
        line(gs, px + ox * 1.5, py + oy * 1.5, px - ox * 1.5, py - oy * 1.5, C["sleeper"], 2)


def _padlock(gs, x, y):
    g = group(gs, "Padlock", "A padlock icon showing that the lever is locked.")
    rect(g.shapes, x + 0.07, y, 0.2, 0.24, fill=None, line=C["text"], line_w=3, radius=0.1)
    rect(g.shapes, x, y + 0.17, 0.34, 0.27, fill=C["amber"], line=C["ink"], line_w=1, radius=0.04)


def s12(d):
    c = d.slide(12, "Interlocking", "B")
    sh = c.shapes
    g = group(sh, "Locked levers",
              "Two tracks cross, each with a signal. Below, two levers are joined by a locking bar. Lever 1 is "
              "pulled so signal 1 is clear. Lever 2 is locked so signal 2 stays at stop.")
    gs = g.shapes
    dx = 1.2
    _track_line(gs, (4.6 + dx, 2.45), (9.2 + dx, 4.25))
    _track_line(gs, (4.6 + dx, 4.25), (9.2 + dx, 2.45))
    semaphore(gs, 4.0 + dx, 2.85, "clear", 0.8, name="Signal 1 (clear)")
    semaphore(gs, 4.0 + dx, 4.7, "stop", 0.8, name="Signal 2 (stop)")
    textbox(gs, 1.2 + dx, 2.0, 2.3, 0.4, "Signal 1: CLEAR", 18, GREEN_T, bold=True, align="r")
    textbox(gs, 1.2 + dx, 3.85, 2.3, 0.4, "Signal 2: STOP", 18, RED_T, bold=True, align="r")
    # lever frame
    base = 5.88
    rect(gs, 4.6 + dx, base, 4.6, 0.1, fill=C["steel"])
    lever(gs, 5.6 + dx, base, C["red"], pulled=True, h=0.85)
    lever(gs, 7.6 + dx, base, C["red"], pulled=False, h=0.85)
    rect(gs, 5.75 + dx, 5.42, 1.85, 0.1, fill=C["steel"], line=C["ink"], line_w=0.75, name="Locking bar")
    rect(gs, 7.48 + dx, 5.36, 0.24, 0.22, fill=C["amber"], line=C["ink"], line_w=0.75)
    _padlock(gs, 7.88 + dx, 5.0)
    textbox(gs, 8.3 + dx, 5.0, 1.6, 0.42, "Locked", 18, AMBER_T, bold=True)
    textbox(gs, 4.9 + dx, 5.98, 1.4, 0.3, "Lever 1", 14, C["text"], bold=True, align="c")
    textbox(gs, 6.9 + dx, 5.98, 1.4, 0.3, "Lever 2", 14, C["text"], bold=True, align="c")
    c.finish("Levers lock each other. Two clashing signals cannot both be clear.")


# ------------------------------------------------------------------------------------------ 13
def s13(d):
    c = d.slide(13, "Boxes talk to each other", "B")
    sh = c.shapes
    g = group(sh, "Two boxes exchange bell codes",
              "Two neighbouring signal boxes joined by a dashed double arrow labelled bell codes. Between them "
              "a block instrument with three positions: normal, line clear, train on line. Line clear is "
              "highlighted.")
    gs = g.shapes
    box_building(gs, 0.9, 1.75, 2.3, 2.2, name="Signal box (left)")
    box_building(gs, 10.1, 1.75, 2.3, 2.2, name="Signal box (right)")
    line(gs, 3.4, 2.95, 9.9, 2.95, C["orange"], 2.25, dash=MSO_LINE.DASH, head=True, tail=True)
    textbox(gs, 5.17, 2.4, 3.0, 0.45, "Bell codes", 18, C["orange"], bold=True, align="c")
    rect(gs, 3.67, 3.6, 6.0, 1.35, fill=C["panel"], line=C["steel"], line_w=2, radius=0.12, name="Block instrument")
    labels = ["Normal", "Line clear", "Train on line"]
    for i, lab in enumerate(labels):
        x = 3.82 + i * 1.95
        on = i == 1
        r = rect(gs, x, 3.8, 1.85, 0.95, fill=C["orange"] if on else C["panel_alt"],
                 line=C["orange"] if on else C["line"], line_w=2, radius=0.08)
        set_text(r, lab, 16, C["ink"] if on else C["text"], bold=True, align="c", margins=(0.03, 0, 0.03, 0))
        set_name(r, f"Position: {lab}")
    poly(gs, [(6.52, 3.62), (6.82, 3.62), (6.67, 3.8)], fill=C["orange"], line_c=None)
    textbox(gs, 3.67, 5.1, 6.0, 0.4, "Example: British absolute block", 16, C["muted"], bold=True, align="c")
    c.finish("Neighbouring boxes ask each other: is the line clear?")


# ------------------------------------------------------------------------------------------ 14
def _step_card(gs, x, y, w, h, n, text):
    rect(gs, x, y, w, h, fill=C["panel"], line=C["line"], line_w=1, radius=0.08)
    ellipse(gs, x + 0.33, y + h / 2, 0.42, fill=C["orange"])
    t = textbox(gs, x + 0.12, y + h / 2 - 0.21, 0.42, 0.42, str(n), 16, C["ink"], bold=True, align="c",
                margins=(0, 0, 0, 0), name="Step number")
    textbox(gs, x + 0.62, y, w - 0.7, h, text, 14, C["text"], bold=True, name="Step text")


def s14(d):
    c = d.slide(14, "All together on a real railway", "B")
    sh = c.shapes
    g = group(sh, "A real railway with signals",
              "A track with three blocks. A signal box at the top left, with levers and a signaller, works "
              "three signals through dashed rods with counterweights. A locomotive and wagons sit in block 2, "
              "so the signal before it shows stop. A second box at the far right is joined by bell codes. Four "
              "steps below explain the order of events.")
    gs = g.shapes
    ty = 4.0
    base = ty + 0.34
    rails(gs, 0.8, ty, 11.7)
    bounds = [0.8, 5.0, 8.0, 11.0]
    states = [("free", "Free"), ("occupied", "Occupied"), ("free", "Free")]
    for i in range(3):
        block_band(gs, bounds[i] + 0.04, 4.58, bounds[i + 1] - bounds[i] - 0.08, states[i][0], states[i][1],
                   size=16, h=0.4)
    train(gs, 5.4, ty, "right", 2, scale=0.8)
    # box, levers, signaller
    box_building(gs, 0.8, 1.5, 2.6, 1.8, windows=True, door=False, name="Signal box (main)")
    for x, col in zip((1.2, 1.55, 1.9), (C["red"], C["red"], C["amber"])):
        lever(gs, x, 3.25, col, h=0.62, scale=0.9)
    person_icon(gs, 2.85, 3.25, scale=0.85)
    box_building(gs, 11.6, 1.5, 1.1, 1.0, windows=True, door=False, color=C["panel"], line_c=C["steel"],
                 name="Signal box (neighbour)")
    line(gs, 3.55, 2.0, 11.45, 2.0, C["orange"], 2.25, dash=MSO_LINE.DASH, head=True, tail=True)
    textbox(gs, 5.7, 1.5, 3.4, 0.4, "Bell codes", 16, C["orange"], bold=True, align="c")
    # three signals, rods and counterweights
    sig = [(5.0, "stop", 3.0), (8.0, "clear", 2.75), (11.0, "clear", 2.5)]
    for x, st, ry in sig:
        semaphore(gs, x, base, st)
        vx = x - 0.45
        poly(gs, [(3.4, ry), (vx, ry), (vx, base - 0.02)], line_c=C["orange"], line_w=2.25, close=False,
             dash=MSO_LINE.DASH, name="Rod")
        rect(gs, vx - 0.08, base - 0.2, 0.16, 0.16, fill=C["steel"], line="#FFFFFF", line_w=0.75, name="Counterweight")
    # step strip
    steps = ["Train is in the block.", "Signaller keeps the signal at stop.", "Train leaves; the block is free.",
             "Signaller pulls the lever; the arm lifts."]
    for i, t in enumerate(steps):
        _step_card(gs, 0.6 + i * 3.077, 5.35, 2.9, 0.85, i + 1, t)
    c.finish("The signaller watches the blocks, sets the signals and keeps trains apart.")


# ------------------------------------------------------------------------------------------ 15
def s15(d):
    c = d.slide(15, "In the mod: blocks and semaphores", "A")
    sh = c.shapes
    g = group(sh, "Blocks and semaphores in the mod",
              "A track with three blocks and three small mechanical semaphores. A train sits in the middle "
              "block, which is occupied; the signal before it shows stop.")
    gs = g.shapes
    ty = 4.2
    base = ty + 0.34
    rails(gs, 0.8, ty, 11.7)
    bounds = [0.8, 4.7, 8.6, 12.5]
    states = [("free", "Free"), ("occupied", "Occupied"), ("free", "Free")]
    for i in range(3):
        block_band(gs, bounds[i] + 0.04, ty + 0.75, bounds[i + 1] - bounds[i] - 0.08, states[i][0], states[i][1])
        if 0 < i:
            line(gs, bounds[i], ty - 1.0, bounds[i], ty + 1.3, C["muted"], 1.5, dash=MSO_LINE.DASH)
    train(gs, 5.2, ty, "right", 2, scale=1.1)
    for x, st in ((1.15, "clear"), (4.7, "stop"), (8.6, "clear")):
        semaphore(gs, x, base, st, 1.5)
        textbox(gs, x - 0.7, 1.85, 1.4, 0.4, "STOP" if st == "stop" else "CLEAR", 18,
                RED_T if st == "stop" else GREEN_T, bold=True, align="c")
    textbox(gs, 0.8, 1.4, 5.0, 0.45, "Mechanical semaphores", 20, C["orange"], bold=True)
    c.finish("In the mod, semaphores divide the line into blocks.")


# ------------------------------------------------------------------------------------------ 16
def s16(d):
    c = d.slide(16, "A box at every station", "A")
    sh = c.shapes
    g = group(sh, "Station boxes and a dedicated box",
              "A plan view of two stations, each with a platform and a signal box, joined by a long track. A "
              "free-standing dedicated box stands between them. Dotted outlines show the stretch of track each "
              "box reaches.")
    gs = g.shapes
    oy = 0.45
    ty = 3.7 + oy
    rails(gs, 0.8, ty, 11.7)
    reaches = [(0.7, 4.4, "Station box"), (4.55, 8.75, "Dedicated box"), (8.9, 12.6, "Station box")]
    for x1, x2, lab in reaches:
        rect(gs, x1, 1.85 + oy, x2 - x1, 2.7, fill=C["orange"], alpha=8, line=C["orange"], line_w=2,
             dash=MSO_LINE.ROUND_DOT, radius=0.25, name="Box reach")
        textbox(gs, x1, 1.95 + oy, x2 - x1, 0.4, lab, 18, C["orange"], bold=True, align="c")
    for px in (1.55, 9.75):
        rect(gs, px, 3.3 + oy, 2.0, 0.34, fill=C["steel"], line=C["post"], line_w=1.5, name="Platform")
    for x1, x2, lab in reaches:
        cx = (x1 + x2) / 2
        box_building(gs, cx - 0.65, 2.4 + oy, 1.3, 1.25, windows=True, door=False, name=f"Box icon: {lab}")
    c.finish("Every steam station has a signal box. Dedicated boxes extend control along the line.")


# ------------------------------------------------------------------------------------------ 17
def s17(d):
    c = d.slide(17, "Every signal needs a box", "A")
    sh = c.shapes
    g = group(sh, "A box has limited room",
              "One signal box with a row of eight slots. Six are filled and controlled; two are free. A signal "
              "on the right has a dashed red outline: no box is in reach, so it is not controlled.")
    gs = g.shapes
    box_building(gs, 2.15, 1.55, 2.8, 2.2, windows=True, door=False, name="Signal box")
    for i in range(8):
        x = 0.8 + i * 0.7
        on = i < 6
        rect(gs, x, 4.35, 0.6, 0.6, fill=C["orange"] if on else None, line=C["orange"], line_w=2, radius=0.06,
             name="Slot (controlled)" if on else "Slot (free)")
    textbox(gs, 0.8, 3.92, 4.1, 0.38, "Controlled", 16, C["orange"], bold=True, align="c")
    textbox(gs, 5.0, 3.92, 1.3, 0.38, "Free", 16, C["muted"], bold=True, align="c")
    semaphore(gs, 9.4, 4.9, "stop", 1.8, name="Signal without a box", lamp=False,
              alt="A semaphore signal that no signal box controls.")
    rect(gs, 8.25, 2.55, 3.1, 2.65, fill=None, line=C["red"], line_w=2.25, dash=MSO_LINE.DASH, radius=0.1,
         name="Dashed red outline")
    textbox(gs, 7.2, 5.3, 5.3, 0.45, "No box in reach: not controlled", 18, RED_T, bold=True, align="c")
    c.finish("A signal must belong to a signal box. A box can only control so much.")


# ------------------------------------------------------------------------------------------ 18
def s18(d):
    c = d.slide(18, "Early limits", "V")
    sh = c.shapes
    g = group(sh, "Four provisional limits",
              "Four tiles, each marked provisional: block length about 400 to 500 metres, speed cap about 60 "
              "kilometres an hour, 6 to 8 signals per station box and 12 to 16 per dedicated box, and box reach "
              "about 1 to 1.5 kilometres. A ruler strip shows a signal every 450 metres.")
    gs = g.shapes
    tiles = [("Block: about", ["400–500 m"]), ("Speed cap: about", ["60 km/h"]),
             ("Signals per box", ["6–8 station", "12–16 dedicated"]), ("Reach: about", ["1–1.5 km"])]
    for i, (lab, vals) in enumerate(tiles):
        x = 0.6 + i * 3.11
        rect(gs, x, 1.5, 2.8, 2.2, fill=C["panel"], line=C["line"], line_w=1, radius=0.08)
        chip(gs, "V", x=x + 0.15, y=1.65, w=1.55, h=0.32, text="PROVISIONAL", name="Chip: Provisional (inline)")
        paras = [[(lab, {"size": 16, "color": C["muted"]})]] + [[(v, {"size": 22, "color": C["orange"]})] for v in vals]
        textbox(gs, x + 0.15, 2.12, 2.5, 1.5, paras, 22, C["text"], bold=True, anchor="t", margins=(0, 0.02, 0, 0))
    # ruler strip: a signal every 450 m
    ty = 5.0
    rails(gs, 0.8, ty, 11.7)
    xs = [1.2 + i * 2.15 for i in range(6)]
    for x in xs:
        semaphore(gs, x, ty + 0.34, "stop", 0.6, lamp=False)
    dimension(gs, xs[1], xs[2], 4.2, "450 m", size=16)
    textbox(gs, 0.6, 5.7, 7.0, 0.4, "Final values: undecided (OQ03).", 16, C["muted"], bold=True)
    c.finish("Early signals have limits: short blocks, a speed cap and a limited number per box. "
             "Numbers are provisional.")


SLIDES = [s10, s11, s12, s13, s14, s15, s16, s17, s18]
