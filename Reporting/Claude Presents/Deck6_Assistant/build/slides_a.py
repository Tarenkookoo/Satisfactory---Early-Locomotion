"""Chunk 1: slides 1 to 8."""
from lib import *

PLACEHOLDER = "Placeholder avatar. Her look is undecided (OQ15)."


# ---------------------------------------------------------------- slide 1
def s01(prs):
    s = new_slide(prs, "Your Railway Guide", None, title_size=54, title_box=(0.6, 1.4, 6.6, 2.2))
    s.shapes.title.text_frame.vertical_anchor = MSO_ANCHOR.BOTTOM
    sh = s.shapes
    rect(sh, 7.55, 0.5, 5.18, 6.4, PANEL, None, radius=0.08, name="avatar panel")
    bottom = avatar(sh, 10.14, 2.55, 1.7)
    speech_bubble(sh, 8.05, 0.95, 2.2, 1.0, "...", TEXT, DARK, size=36, tail="br", name="guide bubble",
                  tail_len=0.42, tail_w=0.4)
    label(sh, 7.85, 6.0, 4.58, 0.6, PLACEHOLDER, 14, MUTED, align="c", anchor="m", name="PLACEHOLDER LABEL")
    rect(sh, 0.6, 3.8, 1.8, 0.08, ORANGE, None, name="orange rule")
    label(sh, 0.6, 4.1, 6.5, 1.5,
          "Meet the mod's friendly guide, her lessons, and where rail parts could live in the build menu.",
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
def mic_icon(sh, cx, cy, h=0.8, color=ORANGE):
    u = h / 10
    rect(sh, cx - 1.6 * u, cy - 5 * u, 3.2 * u, 6.0 * u, color, None, radius=1.6 * u, name="mic head")
    poly(sh, ring_pts(cx, cy - 0.4 * u, 3.1 * u, 2.3 * u, 180, 360), color, None, name="mic cradle")
    rect(sh, cx - 0.4 * u, cy + 2.6 * u, 0.8 * u, 1.8 * u, color, None, name="mic stem")
    rect(sh, cx - 2.2 * u, cy + 4.4 * u, 4.4 * u, 0.7 * u, color, None, name="mic base")


def s03(prs):
    s = new_slide(prs, "Meet the guide", "Agreed")
    sh = s.shapes
    rect(sh, 0.6, 1.5, 4.8, 4.6, PANEL, None, radius=0.08, name="avatar panel")
    avatar(sh, 3.0, 1.72, 1.7)
    label(sh, 0.85, 5.38, 4.3, 0.6, PLACEHOLDER, 14, MUTED, align="c", anchor="m", name="PLACEHOLDER LABEL")
    # four trait tags
    g = group(sh, "Trait tags", "Four small trait tags for the guide: Warm, Bubbly, Expressive, Good teacher.")
    gs = g.shapes
    traits = [("Warm", 5.9, 1.6), ("Bubbly", 7.6, 1.6), ("Expressive", 5.9, 2.5), ("Good teacher", 8.2, 2.5)]
    for t, x, y in traits:
        w = text_w(t, 20, True) + 0.6
        rect(gs, x, y, w, 0.62, PANEL, ORANGE, 2.5, radius=0.31, name="trait tag", text=t, size=20, color=TEXT,
             bold=True, margins=(0.05, 0, 0.05, 0))
    # note with microphone icon
    n = group(sh, "Voice note", "A note with a microphone icon: voiced by the project's creator.")
    ns = n.shapes
    rect(ns, 5.9, 3.5, 6.83, 1.1, PANEL, None, radius=0.08, name="note card")
    mic_icon(ns, 6.55, 4.0, 0.85)
    label(ns, 7.2, 3.5, 5.4, 1.1, "Voiced by the project's creator.", 20, TEXT, align="l", anchor="m", name="NOTE")
    ichip(sh, "Undecided", 5.9, 5.1, "Name and look: undecided (OQ15)")
    finish(s, "Early Locomotion has its own friendly railway guide. She loves trains and loves teaching.", 3)
    return s


# ---------------------------------------------------------------- slide 4
def s04(prs):
    s = new_slide(prs, "Not the game's ADA", "Agreed")
    sh = s.shapes
    g = group(sh, "Two speech bubbles",
              "Two speech bubbles. On the left, a cool grey bubble: ADA is colder and corporate. On the right, a "
              "warm orange bubble: the guide is warm and friendly. They are separate characters.")
    gs = g.shapes
    speech_bubble(gs, 0.9, 2.3, 5.2, 1.9, "ADA: colder, corporate", COOL, TEXT, size=26, tail="bl",
                  name="ADA bubble", tail_len=0.5)
    speech_bubble(gs, 7.2, 2.3, 5.2, 1.9, "The guide: warm, friendly", ORANGE, DARK, size=26, tail="br",
                  name="guide bubble", tail_len=0.5)
    # abstract speaker dots (no character art)
    oval(gs, 1.0, 4.85, 0.95, 0.95, None, COOL, 6, name="ADA dot ring")
    oval(gs, 1.33, 5.18, 0.29, 0.29, COOL, None, name="ADA dot")
    oval(gs, 11.35, 4.85, 0.95, 0.95, None, ORANGE, 6, name="guide dot ring")
    oval(gs, 11.68, 5.18, 0.29, 0.29, ORANGE, None, name="guide dot")
    # "not equal" sign from shapes
    line(gs, 6.28, 3.0, 7.02, 3.0, MUTED, 5, name="not equal bar", round_cap=True)
    line(gs, 6.28, 3.5, 7.02, 3.5, MUTED, 5, name="not equal bar", round_cap=True)
    line(gs, 6.5, 3.85, 6.8, 2.65, MUTED, 5, name="not equal slash", round_cap=True)
    ichip(sh, "Background", 0.9, 1.65, "ADA is the game's own assistant")
    finish(s, "She is a separate character from ADA. Warmer, friendlier and railway-mad.", 4)
    return s


# ---------------------------------------------------------------- slide 5
def icon_chat(sh, cx, cy, c=STEEL):
    rect(sh, cx - 0.42, cy - 0.34, 0.84, 0.54, c, None, radius=0.14, name="chat bubble")
    poly(sh, [(cx - 0.22, cy + 0.18), (cx - 0.06, cy + 0.18), (cx - 0.28, cy + 0.44)], c, None, name="chat tail")
    for k in (-1, 0, 1):
        oval(sh, cx + k * 0.2 - 0.05, cy - 0.12, 0.1, 0.1, DARK, None, name="chat dot")


def icon_magnifier(sh, cx, cy, c=STEEL):
    oval(sh, cx - 0.4, cy - 0.4, 0.58, 0.58, None, c, 5, name="lens")
    line(sh, cx + 0.07, cy + 0.07, cx + 0.42, cy + 0.42, c, 7, name="handle", round_cap=True)
    for dx, dy in ((-0.32, -0.28), (-0.12, -0.18), (-0.2, -0.04)):
        oval(sh, cx + dx - 0.03, cy + dy - 0.03, 0.06, 0.06, c, None, name="node")


def icon_calculator(sh, cx, cy, c=STEEL):
    rect(sh, cx - 0.32, cy - 0.44, 0.64, 0.88, c, None, radius=0.07, name="calculator")
    rect(sh, cx - 0.24, cy - 0.36, 0.48, 0.18, DARK, None, name="display")
    for r in range(3):
        for k in range(3):
            rect(sh, cx - 0.22 + k * 0.17, cy - 0.1 + r * 0.17, 0.12, 0.12, DARK, None, name="key")


def icon_gear(sh, cx, cy, c=STEEL):
    for i in range(8):
        a = i * 45
        tx = cx + 0.33 * math.sin(math.radians(a))
        ty = cy - 0.33 * math.cos(math.radians(a))
        shape(sh, MSO_SHAPE.RECTANGLE, tx - 0.07, ty - 0.1, 0.14, 0.2, c, None, name="tooth", rot=a)
    oval(sh, cx - 0.27, cy - 0.27, 0.54, 0.54, c, None, name="gear")
    oval(sh, cx - 0.11, cy - 0.11, 0.22, 0.22, PANEL, None, name="gear hole")


def s05(prs):
    s = new_slide(prs, "What she is not", "Agreed")
    sh = s.shapes
    g = group(sh, "Six crossed-out cards",
              "Six cards, each crossed out with a red cross: Live AI, Network checker, Route calculator, "
              "Signal placer, Automatic fixer and Train driver. She is none of these.")
    gs = g.shapes
    cards = ["Live AI", "Network checker", "Route calculator", "Signal placer", "Automatic fixer", "Train driver"]
    icons = [icon_chat, icon_magnifier, icon_calculator, None, icon_gear, None]
    cw, ch, gap = 3.85, 2.0, 0.29
    for i, t in enumerate(cards):
        col, row = i % 3, i // 3
        x = 0.6 + col * (cw + gap)
        y = 1.6 + row * (ch + 0.28)
        rect(gs, x, y, cw, ch, PANEL, LINE, 1.5, radius=0.08, name="card")
        ix, iy = x + 0.8, y + ch / 2
        if icons[i]:
            icons[i](gs, ix, iy)
        elif t == "Signal placer":
            semaphore(gs, ix - 0.1, iy + 0.45, 0.95, "clear", name="icon semaphore")
        else:
            loco_side(gs, ix - 0.45, iy - 0.25, 0.95, STEEL, name="icon engine")
        label(gs, x + 1.55, y + 0.2, cw - 1.7, ch - 0.4, [[(t, {"strike": True})]], 22, TEXT, True, align="l",
              name="card label")
        cross(gs, x + cw - 0.12, y + 0.12, 0.62, name="cross")
    finish(s, "She teaches. She does not run, check or fix your railway.", 5)
    return s


# ---------------------------------------------------------------- slide 6
def s06(prs):
    s = new_slide(prs, "Lessons, not answers", "Agreed")
    sh = s.shapes
    g = group(sh, "Lesson card and refused button",
              "A lesson card titled How blocks work, with a green tick. Beside it, a Fix my railway button with a "
              "red cross: she does not fix your railway for you.")
    gs = g.shapes
    # lesson card
    cx0, cy0, cw, chh = 1.1, 1.7, 4.9, 4.1
    rect(gs, cx0, cy0, cw, chh, PANEL, ORANGE, 2.5, radius=0.1, name="lesson card")
    rect(gs, cx0 + 0.4, cy0 + 0.4, cw - 0.8, 1.9, TABLE_WHITE, None, radius=0.08, name="lesson preview")
    stadium(gs, cx0 + 0.9, cy0 + 0.75, cw - 1.8, 1.2, "#7A828C", 3, name="preview loop")
    oval(gs, cx0 + cw / 2 - 0.3, cy0 + 1.35 - 0.3, 0.6, 0.6, ORANGE, None, name="play disc")
    play_tri(gs, cx0 + cw / 2 + 0.03, cy0 + 1.35, 0.32, DARK)
    label(gs, cx0 + 0.2, cy0 + 2.6, cw - 0.4, 0.8, "How blocks work", 28, TEXT, True, name="lesson title")
    tick(gs, cx0 + cw - 0.1, cy0 + 0.1, 0.85)
    # refused button
    bx, by, bw, bh = 7.5, 3.0, 4.9, 1.6
    rect(gs, bx, by, bw, bh, PANEL_ALT, MUTED, 2.5, radius=0.3, dash=MSO_LINE.DASH, name="refused button",
         text="Fix my railway", size=28, color=MUTED, bold=True)
    cross(gs, bx + bw - 0.1, by + 0.1, 0.85)
    finish(s, "Lessons explain how railways work. You still solve your own problems.", 6)
    return s


# ---------------------------------------------------------------- slide 7
def s07(prs):
    s = new_slide(prs, "The railway library", "Agreed")
    sh = s.shapes
    g = group(sh, "Shelf of lesson tiles",
              "A shelf of seven lesson tiles. The first four are open and orange. The last three are locked, grey, "
              "with padlocks. An arrow shows that tiles open as you unlock technology.")
    gs = g.shapes
    tw, th, gap = 1.4, 1.9, 0.3
    total = 7 * tw + 6 * gap
    x0 = 0.6 + (12.13 - total) / 2
    ty = 2.5
    for i in range(7):
        x = x0 + i * (tw + gap)
        if i < 4:
            rect(gs, x, ty, tw, th, ORANGE, None, radius=0.1, name="open tile")
            rect(gs, x + 0.2, ty + 0.25, tw - 0.4, 0.9, TABLE_WHITE, None, radius=0.05, name="tile screen")
            play_tri(gs, x + tw / 2 + 0.03, ty + 0.7, 0.4, ORANGE)
            rect(gs, x + 0.2, ty + 1.35, tw - 0.4, 0.1, DARK, None, name="tile line")
            rect(gs, x + 0.2, ty + 1.55, (tw - 0.4) * 0.6, 0.1, DARK, None, name="tile line")
        else:
            rect(gs, x, ty, tw, th, LINE, MUTED, 1.5, radius=0.1, name="locked tile")
            padlock(gs, x + tw / 2, ty + 0.75, 0.62, TEXT)
            rect(gs, x + 0.2, ty + 1.45, tw - 0.4, 0.1, MUTED, None, name="tile line")
    # shelf board
    rect(gs, x0 - 0.2, ty + th, total + 0.4, 0.2, SLEEPER, None, radius=0.04, name="shelf board")
    # brackets with words above the tiles
    ox1, ox2 = x0, x0 + 4 * tw + 3 * gap
    lx1, lx2 = x0 + 4 * (tw + gap), x0 + total
    for (a, b, t, c) in ((ox1, ox2, "Open", ORANGE), (lx1, lx2, "Locked", MUTED)):
        line(gs, a, 2.3, b, 2.3, c, 3, name="bracket")
        line(gs, a, 2.3, a, 2.44, c, 3, name="bracket tick")
        line(gs, b, 2.3, b, 2.44, c, 3, name="bracket tick")
        label(gs, (a + b) / 2 - 0.7, 1.78, 1.4, 0.42, t, 20, TEXT, True, name="bracket label")
    # arrow labelled
    arrow(gs, x0, 4.85, x0 + total, 4.85, ORANGE, 3, name="unlock arrow")
    label(gs, x0 + total / 2 - 1.6, 4.92, 3.2, 0.4, "Opens as you unlock", 18, ORANGE, True, name="arrow label")
    # note with open book
    nx, ny = x0 + total / 2 - 3.2, 5.5
    book = group(sh, "Library note", "Note with an open book icon: the library is always open to browse.")
    bs = book.shapes
    rect(bs, nx, ny, 6.4, 0.58, PANEL, None, radius=0.08, name="note card")
    poly(bs, [(nx + 0.2, ny + 0.12), (nx + 0.45, ny + 0.06), (nx + 0.7, ny + 0.12), (nx + 0.7, ny + 0.42),
              (nx + 0.45, ny + 0.36), (nx + 0.2, ny + 0.42)], TEXT, None, name="book left")
    poly(bs, [(nx + 0.72, ny + 0.12), (nx + 0.97, ny + 0.06), (nx + 1.22, ny + 0.12), (nx + 1.22, ny + 0.42),
              (nx + 0.97, ny + 0.36), (nx + 0.72, ny + 0.42)], MUTED, None, name="book right")
    label(bs, nx + 1.4, ny, 4.9, 0.58, "The library is always open to browse.", 18, TEXT, align="l", name="NOTE")
    finish(s, "Lessons are optional and can be replayed. New ones open as you unlock technology.", 7)
    return s


# ---------------------------------------------------------------- slide 8
def s08(prs):
    s = new_slide(prs, "The miniature table", "Agreed")
    sh = s.shapes
    g = group(sh, "Miniature model-railway table",
              "A clean white model-railway table on a dark panel. It holds a small loop of track, a tiny train, a "
              "semaphore signal, a signal box and a small station, all drawn from simple shapes.")
    gs = g.shapes
    rect(gs, 0.6, 1.45, 12.13, 4.7, COAL, LINE, 1.5, radius=0.08, name="dark panel")
    miniature_table(gs, 1.11, 1.7, 1.1, labels=True, sem_state="stop")
    finish(s, "Lessons play out on a clean white model-railway table.", 8)
    return s


SLIDES = [s01, s02, s03, s04, s05, s06, s07, s08]
