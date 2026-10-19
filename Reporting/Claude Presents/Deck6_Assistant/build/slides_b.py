"""Chunk 2: slides 9 to 16."""
from lib import *
from lib import _ends

PLACEHOLDER = "Placeholder avatar. Her look is undecided (OQ15)."


# --- control icons (centred on cx, cy) ----------------------------------------------
def ic_pause(sh, cx, cy, c=ORANGE):
    rect(sh, cx - 0.11, cy - 0.13, 0.07, 0.26, c, None, name="pause bar")
    rect(sh, cx + 0.04, cy - 0.13, 0.07, 0.26, c, None, name="pause bar")


def ic_replay(sh, cx, cy, c=ORANGE):
    shp = poly(sh, arc_pts(cx, cy, 0.14, 70, 345), None, c, 3, closed=False, name="replay arc")
    _ends(shp, False, True)


def ic_prev(sh, cx, cy, c=ORANGE):
    rect(sh, cx - 0.13, cy - 0.13, 0.05, 0.26, c, None, name="prev bar")
    poly(sh, [(cx + 0.13, cy - 0.13), (cx + 0.13, cy + 0.13), (cx - 0.07, cy)], c, None, name="prev triangle")


def ic_next(sh, cx, cy, c=ORANGE):
    poly(sh, [(cx - 0.13, cy - 0.13), (cx - 0.13, cy + 0.13), (cx + 0.07, cy)], c, None, name="next triangle")
    rect(sh, cx + 0.08, cy - 0.13, 0.05, 0.26, c, None, name="next bar")


def control_pill(sh, x, y, text, icon, h=0.44):
    w = 0.55 + text_w(text, 14, True) + 0.25
    rect(sh, x, y, w, h, PANEL_ALT, LINE, 1.5, radius=h / 2, name="control button")
    icon(sh, x + 0.34, y + h / 2)
    label(sh, x + 0.58, y, w - 0.62, h, text, 14, TEXT, True, align="l", name="control label")
    return w


# ---------------------------------------------------------------- slide 9
def s09(prs):
    s = new_slide(prs, "How a lesson plays", "Agreed")
    sh = s.shapes
    g = group(sh, "Mock lesson window",
              "A mock lesson window. The miniature table is shown with the semaphore highlighted by an orange ring "
              "and a short caption bubble beside it. A control bar below has pause, replay, previous and next "
              "buttons.")
    gs = g.shapes
    rect(gs, 0.6, 1.45, 12.13, 4.7, PANEL_ALT, LINE, 2.0, radius=0.08, name="lesson window")
    rect(gs, 0.64, 1.49, 12.05, 0.32, LINE, None, name="window title bar")
    for k in range(3):
        oval(gs, 0.85 + k * 0.26, 1.58, 0.14, 0.14, MUTED, None, name="window dot")
    k = 0.926
    tx, ty = 1.99, 1.92
    pts = miniature_table(gs, tx, ty, k, labels=False, sem_state="stop")
    # highlight ring around the semaphore arm and lamp
    px, py = pts["pivot"]
    oval(gs, px - 0.55, py - 0.42, 1.55, 0.84, None, ORANGE, 4.5, name="highlight ring")
    # short caption bubble
    speech_bubble(gs, 8.75, 2.0, 2.3, 0.62, "Short caption", PANEL, TEXT, size=18, tail="bl", line_c=ORANGE,
                  name="caption bubble", tail_len=0.34, tail_w=0.3)
    # control bar
    rect(gs, 0.64, 5.52, 12.05, 0.59, PANEL, None, name="control bar")
    x = 1.0
    for text, icon in (("Pause", ic_pause), ("Replay", ic_replay), ("Previous", ic_prev), ("Next", ic_next)):
        x += control_pill(gs, x, 5.595, text, icon) + 0.2
    ichip(sh, "Undecided", 12.55 - ichip_w("Exact controls: undecided (OQ15, OQ18)"), 5.645,
          "Exact controls: undecided (OQ15, OQ18)")
    finish(s, "Lessons pause at the key moment and use short captions. No walls of text.", 9)
    return s


# ---------------------------------------------------------------- slide 10
OLD_BG = "#3A3F47"
OLD_LINE = "#6B7078"


def s10(prs):
    s = new_slide(prs, "An older FICSIT look", "Agreed")
    sh = s.shapes
    g = group(sh, "Mock library screen",
              "A mock library screen in a plain, boxy, muted style. It has a title bar, a list of lessons on the left "
              "and a lesson pane on the right showing a small model-railway table.")
    gs = g.shapes
    wx, wy, ww, wh = 0.6, 1.45, 12.13, 4.15
    rect(gs, wx, wy, ww, wh, OLD_BG, STEEL, 4.0, name="screen frame")
    rect(gs, wx + 0.1, wy + 0.1, ww - 0.2, wh - 0.2, None, OLD_LINE, 1.5, name="screen inner frame")
    rect(gs, wx + 0.1, wy + 0.1, ww - 0.2, 0.48, "#555C66", None, name="title bar",
         text="Railway library", size=18, color=TEXT, bold=True, align="l", margins=(0.2, 0, 0.1, 0))
    for k in range(3):
        rect(gs, wx + ww - 0.45 - k * 0.38, wy + 0.2, 0.26, 0.26, OLD_BG, STEEL, 1.5, name="title button")
    # list on the left
    lx, ly = wx + 0.3, wy + 0.85
    rect(gs, lx, ly, 3.5, 3.0, "#2F343B", OLD_LINE, 1.5, name="list box")
    for i in range(5):
        ry = ly + 0.15 + i * 0.55
        sel = i == 1
        rect(gs, lx + 0.15, ry, 3.2, 0.42, MUTED if sel else "#4A515B", None, name="list row")
        rect(gs, lx + 0.25, ry + 0.09, 0.24, 0.24, DARK if sel else MUTED, None, name="list icon")
        rect(gs, lx + 0.65, ry + 0.16, 1.7 if not sel else 1.9, 0.1, DARK if sel else MUTED, None,
             name="list text bar")
    # lesson pane
    px, py = lx + 3.8, wy + 0.85
    rect(gs, px, py, wx + ww - 0.3 - px, 3.0, "#2F343B", OLD_LINE, 1.5, name="lesson pane")
    rect(gs, px + 0.25, py + 0.25, 4.4, 2.5, TABLE_WHITE, None, name="preview table")
    stadium(gs, px + 0.75, py + 0.65, 3.4, 1.4, "#7A828C", 3, name="preview loop")
    mini_train(gs, px + 1.7, py + 0.52, 1.0, name="preview train")
    oval(gs, px + 2.25 - 0.26, py + 1.55 - 0.26, 0.52, 0.52, ORANGE, None, name="play disc")
    play_tri(gs, px + 2.28, py + 1.55, 0.28, DARK)
    tx0 = px + 4.9
    tw_ = wx + ww - 0.3 - 0.25 - tx0
    rect(gs, tx0, py + 0.3, tw_ * 0.8, 0.2, MUTED, None, name="pane title bar")
    for r in range(4):
        rect(gs, tx0, py + 0.8 + r * 0.3, tw_ * (1.0 if r != 3 else 0.6), 0.1, OLD_LINE, None, name="pane text bar")
    # step squares
    for r in range(5):
        rect(gs, tx0 + r * 0.32, py + 2.2, 0.2, 0.2, ORANGE if r < 2 else OLD_LINE, None, name="step square")
    # note and chip row
    rect(sh, 0.6, 5.72, 3.05, 0.45, PANEL, None, radius=0.08, name="note card", text="A look, not a story.",
         size=18, color=TEXT, bold=True)
    ichip(sh, "Undecided", 12.73 - ichip_w("Final layout: undecided (OQ15)"), 5.775, "Final layout: undecided (OQ15)")
    finish(s, "The library looks like an older, simpler FICSIT screen.", 10)
    return s


# ---------------------------------------------------------------- slide 11
def note_icon(sh, cx, cy, c=ORANGE):
    for dx, dy in ((-0.17, 0.12), (0.2, 0.05)):
        oval(sh, cx + dx - 0.12, cy + dy - 0.08, 0.24, 0.17, c, None, name="note head")
        rect(sh, cx + dx + 0.09, cy + dy - 0.5, 0.045, 0.52, c, None, name="note stem")
    poly(sh, [(cx - 0.08, cy - 0.38), (cx + 0.29, cy - 0.46), (cx + 0.29, cy - 0.34), (cx - 0.08, cy - 0.26)], c,
         None, name="note beam")


def s11(prs):
    s = new_slide(prs, "A surprise on first unlock", "Proposed")
    sh = s.shapes
    g = group(sh, "Four-step storyboard",
              "A four-step storyboard. One: the usual announcement. Two: the screen glitches. Three: a retro jingle "
              "plays. Four: the guide says hello.")
    gs = g.shapes
    steps = ["Usual announcement", "Screen glitches", "A retro jingle plays", "The guide says hello"]
    cw, gap = 2.75, 0.376
    y0, chh = 1.55, 3.55
    for i, t in enumerate(steps):
        x = 0.6 + i * (cw + gap)
        rect(gs, x, y0, cw, chh, PANEL, LINE, 1.5, radius=0.08, name="step card")
        sx, sy, sw, sh_ = x + 0.2, y0 + 0.6, cw - 0.4, 1.8
        dy = 0.15
        rect(gs, sx, sy, sw, sh_, COAL, STEEL, 2.0, radius=0.06, name="mock screen")
        oval(gs, x + 0.1, y0 + 0.1, 0.5, 0.5, ORANGE, None, name="step badge", text=str(i + 1), size=18,
             color=DARK, bold=True)
        label(gs, x + 0.15, y0 + 2.55, cw - 0.3, 0.85, t, 20, TEXT, True, name="step label")
        cx = sx + sw / 2
        scr_bottom = sy + sh_
        sy = sy + dy
        if i == 0:  # usual announcement: a cool grey banner
            rect(gs, sx + 0.2, sy + 0.35, sw - 0.4, 0.8, COOL, None, radius=0.08, name="announcement banner")
            oval(gs, sx + 0.32, sy + 0.5, 0.5, 0.5, None, TEXT, 3, name="banner dot ring")
            oval(gs, sx + 0.5, sy + 0.68, 0.14, 0.14, TEXT, None, name="banner dot")
            rect(gs, sx + 1.0, sy + 0.55, 0.9, 0.1, TEXT, None, name="banner line")
            rect(gs, sx + 1.0, sy + 0.78, 0.65, 0.1, TEXT, None, name="banner line")
        elif i == 1:  # glitch: banner sliced and offset, plus noise
            offs = (0.0, 0.28, -0.2, 0.18, -0.1)
            for r, o in enumerate(offs):
                rect(gs, sx + 0.2 + o, sy + 0.25 + r * 0.17, sw - 0.4, 0.15, COOL if r % 2 == 0 else "#7C8896", None,
                     name="glitch slice")
            for r, (a, b) in enumerate(((0.1, 0.6), (1.2, 0.5), (0.5, 0.4))):
                rect(gs, sx + a, sy + 1.2 + r * 0.09, b, 0.04, ORANGE, None, name="glitch noise")
            poly(gs, [(sx + sw - 0.55, sy + 0.1), (sx + sw - 0.4, sy + 0.35), (sx + sw - 0.55, sy + 0.45),
                      (sx + sw - 0.35, sy + 0.8)], None, AMBER, 3, closed=False, name="glitch zigzag")
        elif i == 2:  # jingle
            note_icon(gs, cx - 0.2, sy + 0.95)
            for r, rad in enumerate((0.3, 0.5, 0.7)):
                poly(gs, arc_pts(cx + 0.2, sy + 0.78, rad, -40, 40), None, ORANGE, 3, closed=False, name="sound arc")
        else:  # the guide says hello
            d = 0.65
            avatar(gs, sx + 0.75, scr_bottom - 2.055 * d + 0.02, d, name="Placeholder avatar (small)")
            speech_bubble(gs, sx + 1.2, sy + 0.05, 0.85, 0.46, "...", TEXT, DARK, size=20, tail="bl", name="small bubble",
                          tail_len=0.22, tail_w=0.2)
        if i < 3:
            arrow(gs, x + cw + 0.03, y0 + 1.5, x + cw + gap - 0.03, y0 + 1.5, ORANGE, 3, name="step arrow")
    label(sh, 0.6, 5.4, 3.0, 0.4, "Funny, not sinister.", 18, TEXT, True, align="l", name="NOTE")
    ichip(sh, "Undecided", 3.55, 5.43, "Exact sequence: open")
    label(sh, 7.4, 5.35, 5.33, 0.5, PLACEHOLDER, 14, MUTED, align="r", anchor="m", name="PLACEHOLDER LABEL")
    finish(s, "On your first unlock, the game's usual announcer could be playfully interrupted.", 11)
    return s


# ---------------------------------------------------------------- slide 12
def s12(prs):
    s = new_slide(prs, "An original jingle", "Agreed")
    sh = s.shapes
    g = group(sh, "Sound-wave icon and jingle card",
              "A sound-wave icon, a speaker with an audio waveform, beside a card reading: Original retro start-up "
              "jingle.")
    gs = g.shapes
    rect(gs, 0.9, 1.9, 5.6, 3.6, PANEL, None, radius=0.1, name="icon panel")
    # speaker
    rect(gs, 1.4, 3.35, 0.45, 0.7, ORANGE, None, name="speaker box")
    poly(gs, [(1.85, 3.35), (2.55, 2.85), (2.55, 4.55), (1.85, 4.05)], ORANGE, None, name="speaker cone")
    # waveform bars
    heights = (0.5, 1.1, 0.8, 1.7, 1.2, 2.1, 1.4, 0.9, 1.5, 0.7, 0.4)
    for k, h in enumerate(heights):
        rect(gs, 2.95 + k * 0.32, 3.7 - h / 2, 0.18, h, ORANGE, None, radius=0.09, name="wave bar")
    # card
    rect(gs, 7.2, 2.5, 5.5, 2.4, PANEL, ORANGE, 3.0, radius=0.12, name="jingle card",
         text=["Original retro", "start-up jingle"], size=30, color=TEXT, bold=True, margins=(0.35, 0.1, 0.35, 0.1))
    arrow(gs, 6.6, 3.7, 7.1, 3.7, ORANGE, 3, name="link arrow")
    finish(s, "The start-up jingle is original. No borrowed sounds.", 12)
    return s


# ---------------------------------------------------------------- slide 13
def s13(prs):
    s = new_slide(prs, "Can the surprise be done?", "Undecided")
    sh = s.shapes
    g = group(sh, "Two undecided paths",
              "Two possible paths, each with a question mark: intercept the game's announcer, or recreate it "
              "ourselves. Neither is decided or tested.")
    gs = g.shapes
    rect(gs, 0.7, 3.2, 2.7, 0.9, PANEL, ORANGE, 2.5, radius=0.45, name="origin", text="The surprise", size=20,
         color=TEXT, bold=True)
    for (cy, txt) in ((2.55, "Intercept the game's announcer?"), (4.75, "Recreate it ourselves?")):
        pts = [(3.4, 3.65), (4.2, 3.65), (4.2, cy), (5.1, cy)]
        shp = poly(gs, pts, None, ORANGE, 3, closed=False, dash=MSO_LINE.DASH, name="path")
        _ends(shp, False, True)
        rect(gs, 5.2, cy - 0.8, 7.5, 1.6, PANEL, MUTED, 2.5, radius=0.1, dash=MSO_LINE.DASH, name="path card",
             text=txt, size=26, color=TEXT, bold=True, align="l", margins=(0.4, 0.1, 1.5, 0.1))
        oval(gs, 11.2, cy - 0.45, 0.9, 0.9, None, MUTED, 3, name="question disc", text="?", size=36, color=TEXT,
             bold=True)
    label(sh, 0.7, 5.6, 2.0, 0.4, "OQ18", 18, MUTED, True, align="l", name="FOOTER")
    finish(s, "How to pull off the surprise is not decided or tested.", 13)
    return s


# ---------------------------------------------------------------- slide 14
def s14(prs):
    s = new_slide(prs, "A hint of an older FICSIT", "Proposed")
    sh = s.shapes
    g = group(sh, "Older look and modern look",
              "Two mock panels. On the left, an older look: boxy and plain. On the right, a modern look: sleek. A "
              "dotted double arrow with a question mark sits between them, and a note says it is a hint only, not a "
              "backstory.")
    gs = g.shapes
    py, ph, pw = 2.1, 3.05, 4.6
    # older (left): square corners, thick frame, muted
    lx = 0.9
    label(gs, lx, 1.55, pw, 0.45, "Older look", 20, TEXT, True, name="panel label")
    rect(gs, lx, py, pw, ph, OLD_BG, STEEL, 4.0, name="older panel")
    rect(gs, lx + 0.1, py + 0.1, pw - 0.2, 0.4, OLD_LINE, None, name="older title bar")
    for r in range(3):
        rect(gs, lx + 0.3, py + 0.8 + r * 0.55, 1.6, 0.35, "#4A515B", OLD_LINE, 1.5, name="older list row")
    rect(gs, lx + 2.1, py + 0.8, 2.3, 1.6, "#2F343B", OLD_LINE, 1.5, name="older pane")
    rect(gs, lx + 0.3, py + 2.55, 4.1, 0.3, OLD_LINE, None, name="older footer bar")
    # modern (right): rounded, thin, sleek
    rx = 12.73 - 0.3 - pw
    label(gs, rx, 1.55, pw, 0.45, "Modern look", 20, TEXT, True, name="panel label")
    rect(gs, rx, py, pw, ph, COAL, ORANGE, 1.5, radius=0.3, name="modern panel")
    rect(gs, rx + 0.3, py + 0.25, 1.4, 0.12, ORANGE, None, radius=0.06, name="modern header")
    for r in range(3):
        rect(gs, rx + 0.3, py + 0.8 + r * 0.55, 1.6, 0.35, PANEL, None, radius=0.17, name="modern list row")
    rect(gs, rx + 2.1, py + 0.8, 2.2, 1.6, PANEL, None, radius=0.2, name="modern pane")
    rect(gs, rx + 0.3, py + 2.55, 4.0, 0.14, PANEL_ALT, None, radius=0.07, name="modern footer bar")
    oval(gs, rx + 4.0, py + 0.22, 0.2, 0.2, ORANGE, None, name="modern dot")
    # dotted question arrow between
    mx = (lx + pw + rx) / 2
    my = py + ph / 2
    line(gs, lx + pw + 0.12, my, mx - 0.5, my, MUTED, 3, dash=MSO_LINE.ROUND_DOT, head=True, name="dotted arrow left")
    line(gs, rx - 0.12, my, mx + 0.5, my, MUTED, 3, dash=MSO_LINE.ROUND_DOT, head=True, name="dotted arrow right")
    oval(gs, mx - 0.4, my - 0.4, 0.8, 0.8, PANEL, MUTED, 2.5, name="question disc", text="?", size=28, color=TEXT,
         bold=True)
    label(gs, mx - 1.05, my + 0.55, 2.1, 0.8, "A hint only, not a backstory.", 14, TEXT, True, name="hint note")
    ichip(sh, "Undecided", 6.67 - ichip_w("Lore: undecided (OQ16)") / 2, 5.4, "Lore: undecided (OQ16)")
    finish(s, "Her style could hint at an older FICSIT. It is not a story.", 14)
    return s


# ---------------------------------------------------------------- slide 15
def icon_warning(sh, cx, cy):
    poly(sh, [(cx, cy - 0.6), (cx + 0.65, cy + 0.5), (cx - 0.65, cy + 0.5)], AMBER, None, name="warning triangle")
    rect(sh, cx - 0.05, cy - 0.2, 0.1, 0.38, DARK, None, radius=0.04, name="warning bar")
    oval(sh, cx - 0.06, cy + 0.24, 0.12, 0.12, DARK, None, name="warning dot")


def icon_junction(sh, cx, cy):
    line(sh, cx - 0.75, cy + 0.25, cx - 0.05, cy + 0.25, STEEL, 6, name="trunk", round_cap=True)
    line(sh, cx - 0.05, cy + 0.25, cx + 0.75, cy - 0.35, STEEL, 6, name="branch up", round_cap=True)
    line(sh, cx - 0.05, cy + 0.25, cx + 0.75, cy + 0.25, STEEL, 6, name="branch straight", round_cap=True)
    oval(sh, cx - 0.14, cy + 0.11, 0.28, 0.28, ORANGE, None, name="junction point")


def icon_loop(sh, cx, cy):
    line(sh, cx - 0.8, cy + 0.3, cx + 0.8, cy + 0.3, STEEL, 6, name="main line", round_cap=True)
    poly(sh, [(cx - 0.4, cy + 0.3), (cx - 0.2, cy - 0.25), (cx + 0.2, cy - 0.25), (cx + 0.4, cy + 0.3)], None, STEEL,
         6, closed=False, name="passing loop")
    oval(sh, cx - 0.14, cy - 0.39, 0.28, 0.28, ORANGE, None, name="loop train")


def s15(prs):
    s = new_slide(prs, "More lessons later", "Proposed")
    sh = s.shapes
    g = group(sh, "Four proposed lesson tiles",
              "Four proposed lesson tiles with simple icons: Common mistakes, Junctions, Passing loops and "
              "Advanced signalling.")
    gs = g.shapes
    tiles = [("Common mistakes", icon_warning), ("Junctions", icon_junction), ("Passing loops", icon_loop),
             ("Advanced signalling", None)]
    tw, gap = 2.8, 0.31
    for i, (t, ic) in enumerate(tiles):
        x = 0.6 + i * (tw + gap)
        y = 1.6
        rect(gs, x, y, tw, 4.1, PANEL, PURPLE, 2.5, radius=0.1, dash=MSO_LINE.DASH, name="proposed tile")
        rect(gs, x + 0.25, y + 0.3, tw - 0.5, 2.4, PANEL_ALT, None, radius=0.08, name="icon panel")
        cx, cy = x + tw / 2, y + 1.5
        if ic:
            ic(gs, cx, cy)
        else:
            semaphore(gs, cx - 0.2, cy + 0.8, 1.35, "clear", name="icon semaphore")
        label(gs, x + 0.15, y + 2.9, tw - 0.3, 1.0, t, 20, TEXT, True, name="tile label")
    finish(s, "More lessons could cover common mistakes, junctions and passing loops.", 15)
    return s


# ---------------------------------------------------------------- slide 16
def s16(prs):
    s = new_slide(prs, "How the list could look", "Proposed")
    sh = s.shapes
    g = group(sh, "Vertical list of subjects",
              "A simple vertical list of five subject rows drawn as grey bars, each with a small plain icon and a "
              "scroll bar on the right. The subject names are not decided.")
    gs = g.shapes
    px, pw = 3.2, 6.9
    rect(gs, px, 1.5, pw, 3.95, PANEL, LINE, 2.0, radius=0.1, name="list panel")
    kinds = [MSO_SHAPE.OVAL, MSO_SHAPE.RECTANGLE, MSO_SHAPE.ISOSCELES_TRIANGLE, MSO_SHAPE.DIAMOND, MSO_SHAPE.HEXAGON]
    for i, kd in enumerate(kinds):
        ry = 1.68 + i * 0.76
        rect(gs, px + 0.25, ry, pw - 0.95, 0.6, LINE, None, radius=0.08, name="subject bar")
        shape(gs, kd, px + 0.4, ry + 0.12, 0.36, 0.36, ORANGE, None, name="subject icon")
        rect(gs, px + 1.0, ry + 0.25, 2.2 + (i % 3) * 0.5, 0.1, MUTED, None, name="subject text bar")
    # scroll bar
    rect(gs, px + pw - 0.5, 1.68, 0.16, 3.6, LINE, None, radius=0.08, name="scroll track")
    rect(gs, px + pw - 0.5, 1.68, 0.16, 1.5, MUTED, None, radius=0.08, name="scroll thumb")
    ichip(sh, "Undecided", 6.65 - ichip_w("Subjects: undecided (OQ17)") / 2, 5.65, "Subjects: undecided (OQ17)")
    finish(s, "One idea is a simple vertical list of subjects.", 16)
    return s


SLIDES = [s09, s10, s11, s12, s13, s14, s15, s16]
