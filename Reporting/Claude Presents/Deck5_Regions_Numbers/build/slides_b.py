"""Chunk 2: slides 10 to 18."""
from lib import *
from lib import _ends


def right_chip(sh, kind, text, right, y, **kw):
    w = text_w(text, 14, True) + 0.34
    return ichip(sh, kind, right - w, y, text, w=w, **kw)


def qmark(sh, cx, cy, d, size=36):
    return oval(sh, cx - d / 2, cy - d / 2, d, d, BG, MUTED, 3.0, name="question mark", text="?", size=size,
                color=TEXT, bold=True)


# ---------------------------------------------------------------- slide 10
def s10(prs):
    s = new_slide(prs, "Which engine leads?", "Undecided")
    sh = s.shapes
    g = group(sh, "Two coupled engines",
              "Two coupled engines in one train, each with a question mark above it. Which one leads is not settled.")
    gs = g.shapes
    u, gy, x0 = 0.3, 4.6, 1.2
    W = 17.9 * u
    rails_strip(gs, 0.9, gy, 11.6)
    engine(gs, x0, gy, u, "tender", 2, ORANGE)
    x1 = x0 + W + 0.25
    engine(gs, x1, gy, u, "tender", 2, ORANGE)
    rect(gs, x0 + W - 0.02, gy - 2.0 * u, 0.29, 0.07, STEEL, None, name="coupling link")
    for xx in (x0, x1):
        qmark(gs, xx + 11.5 * u, 2.35, 0.95)
    label(sh, 0.6, 5.7, 3.0, 0.3, "OQ06, OQ27", 14, MUTED, align="l", name="open question codes")
    finish(s, "With two engines, which one leads? That is not settled.", 10)
    return s


# ---------------------------------------------------------------- slide 11
def mini_scale(sh, x, y, s=1.0):
    poly(sh, [(x + 0.5 * s, y + 0.25 * s), (x + 0.3 * s, y + 0.95 * s), (x + 0.7 * s, y + 0.95 * s)], STEEL, None,
         name="scale post")
    rect(sh, x + 0.02 * s, y + 0.2 * s, 0.96 * s, 0.07 * s, STEEL, None, name="scale beam")
    for px in (0.17, 0.83):
        line(sh, x + px * s, y + 0.25 * s, x + (px - 0.15) * s, y + 0.6 * s, STEEL, 1.5, name="string")
        line(sh, x + px * s, y + 0.25 * s, x + (px + 0.15) * s, y + 0.6 * s, STEEL, 1.5, name="string")
        rect(sh, x + (px - 0.17) * s, y + 0.6 * s, 0.34 * s, 0.06 * s, STEEL, None, name="pan")


def mini_train(sh, x, y, s=1.0):
    engine(sh, x + 0.35 * s, y + 0.8 * s, 0.075 * s, "tank", 1, ORANGE)
    for k in range(3):
        line(sh, x - 0.05 * s, y + (0.3 + k * 0.17) * s, x + (0.3 - k * 0.04) * s, y + (0.3 + k * 0.17) * s,
             MUTED, 2.0, name="speed line")


def mini_floppy(sh, x, y, s=1.0):
    rect(sh, x, y, s, s, STEEL, None, radius=0.08 * s, name="disk")
    rect(sh, x + 0.18 * s, y + 0.06 * s, 0.64 * s, 0.36 * s, TEXT, None, name="disk label")
    rect(sh, x + 0.28 * s, y + 0.6 * s, 0.44 * s, 0.34 * s, DARKMETAL, None, name="disk shutter")
    rect(sh, x + 0.55 * s, y + 0.66 * s, 0.1 * s, 0.22 * s, STEEL, None, name="disk slot")


def mini_weight(sh, x, y, s=1.0):
    oval(sh, x + 0.33 * s, y, 0.34 * s, 0.4 * s, None, STEEL, 4.0, name="weight ring")
    poly(sh, [(x + 0.2 * s, y + 0.3 * s), (x + 0.8 * s, y + 0.3 * s), (x + s, y + s), (x, y + s)], STEEL, None,
         name="weight")


def s11(prs):
    s = new_slide(prs, "When the region changes", "Undecided")
    sh = s.shapes
    g = group(sh, "Four open questions",
              "Four question cards about engines already running when the region changes: weight and power, "
              "trains on the move, loading a saved game, and how train weight is shown. None is decided.")
    gs = g.shapes
    cards = [("Do weight and power change?", mini_scale), ("What about trains on the move?", mini_train),
             ("What happens on load?", mini_floppy), ("How is train weight shown?", mini_weight)]
    for k, (t, icon) in enumerate(cards):
        x = 0.6 + (k % 2) * 6.18
        y = 1.45 + (k // 2) * 2.1
        rect(gs, x, y, 5.95, 1.85, PANEL, LINE, 1.5, radius=0.1, name="question card")
        icon(gs, x + 0.4, y + 0.4, 1.05)
        label(gs, x + 1.85, y, 3.1, 1.85, t, 20, TEXT, True, align="l", name="question")
        label(gs, x + 5.0, y + 0.2, 0.8, 1.45, "?", 60, MUTED, True, name="question glyph")
    label(sh, 0.6, 5.75, 3.0, 0.3, "OQ06", 14, MUTED, align="l", name="open question codes")
    finish(s, "What happens to engines already running when the region changes? Not decided.", 11)
    return s


# ---------------------------------------------------------------- slide 12
def s12(prs):
    s = new_slide(prs, "A hidden identity", "Agreed")
    sh = s.shapes
    g = group(sh, "Engine with a visible number and a hidden ID",
              "An engine with a visible number plate, and beside it a lock tag for its hidden permanent Fleet ID. "
              "Three arrows (repaint, change region, renumber) pass the same Fleet ID through unchanged.")
    gs = g.shapes
    u, x0, gy = 0.28, 0.9, 3.2
    rails_strip(gs, 0.7, gy, 5.6)
    engine(gs, x0, gy, u, "tender", 2, ORANGE)
    cxp = x0 + 11.5 * u
    plate(gs, cxp - 0.75, gy - 2.95 * u - 0.21, 1.5, 0.42, "No. 1234", 16)
    label(gs, cxp - 1.0, gy + 0.22, 2.0, 0.28, "Example only", 14, MUTED, name="example label")
    # hidden ID tag
    rect(gs, 7.0, 1.65, 4.2, 1.0, PANEL, MUTED, 2.0, radius=0.1, dash=MSO_LINE.DASH, name="hidden id tag")
    padlock(gs, 7.3, 1.82, 0.5, AMBER)
    label(gs, 8.0, 1.65, 3.1, 1.0, "Fleet ID: hidden", 20, TEXT, True, align="l", name="tag label")
    line(gs, 6.0, 2.5, 7.0, 2.2, MUTED, 2.0, dash=MSO_LINE.DASH, name="tether")
    # three arrows passing the ID through unchanged
    for xx in (0.7, 11.0):
        rect(gs, xx, 3.9, 1.7, 2.1, PANEL_ALT, MUTED, 2.0, radius=0.2, dash=MSO_LINE.DASH, name="id pillar")
        padlock(gs, xx + 0.55, 4.15, 0.6, AMBER)
        label(gs, xx, 5.1, 1.7, 0.5, "Fleet ID", 18, TEXT, True, name="pillar label")
    for k, t in enumerate(["Repaint", "Change region", "Renumber"]):
        y = 4.55 + k * 0.7
        arrow(gs, 2.55, y, 10.85, y, ORANGE, 3.0, name="pass-through arrow")
        label(gs, 4.9, y - 0.4, 3.6, 0.36, t, 20, TEXT, True, name="arrow label")
    ichip(sh, "Undecided", 7.0, 2.9, "Where it is stored: undecided (OQ28)")
    finish(s, "Every engine has a hidden permanent ID. Its visible number can change.", 12)
    return s


# ---------------------------------------------------------------- slide 13
def s13(prs):
    s = new_slide(prs, "A number after placement", "Agreed")
    sh = s.shapes
    g = group(sh, "Three steps to a number",
              "Three steps. First a build hologram with no number. Then the engine is placed. Then the engine "
              "shows its number plate.")
    gs = g.shapes
    xs = [0.6, 4.78, 8.96]
    PW = 3.77
    u = 0.19
    gy = 4.0
    labels = ["Hologram: no number", "Placed", "Number appears"]
    for k, x in enumerate(xs):
        rect(gs, x, 1.5, PW, 3.2, PANEL, LINE, 1.5, radius=0.1, name="step panel")
        oval(gs, x + 0.15, 1.62, 0.42, 0.42, ORANGE, None, name="step badge", text=str(k + 1), size=18, color=DARK,
             bold=True)
        label(gs, x + 0.68, 1.6, PW - 0.8, 0.46, labels[k], 18, TEXT, True, align="l", name="step label")
        rails_strip(gs, x + 0.2, gy, PW - 0.4, sleepers=False)
        ex = x + (PW - 17.9 * u) / 2
        if k == 0:
            hg = group(gs, "hologram engine", "Translucent hologram of an engine, with no number plate.")
            engine(hg.shapes, ex, gy, u, "tender", 2, WATER)
            ghost(hg, WATER, 0.28, WATER)
        else:
            engine(gs, ex, gy, u, "tender", 2, ORANGE)
        px = ex + 13.5 * u
        if k == 1:
            rect(gs, px - 0.7, 2.2, 1.4, 0.46, None, MUTED, 2.0, radius=0.06, dash=MSO_LINE.DASH,
                 name="empty plate")
            line(gs, px, 2.66, px, gy - 3.95 * u, MUTED, 1.75, dash=MSO_LINE.DASH, name="leader")
        if k == 2:
            plate(gs, px - 0.7, 2.2, 1.4, 0.46, "No. 1234", 16)
            line(gs, px, 2.66, px, gy - 3.95 * u, ORANGE, 1.75, name="leader")
            label(gs, x + (PW - 2.0) / 2, 4.2, 2.0, 0.28, "Example only", 14, MUTED, name="example label")
    for k in range(2):
        arrow(gs, xs[k] + PW + 0.04, 3.1, xs[k + 1] - 0.04, 3.1, ORANGE, 3.0, name="step arrow")
    rect(gs, 0.6, 4.95, 12.13, 0.9, PANEL_ALT, LINE, 1.5, radius=0.1, name="note panel")
    label(gs, 0.9, 4.95, 11.6, 0.9, "Normal engines are class members and carry no personal names.", 20, TEXT, True,
          align="l", name="note")
    finish(s, "Your engine gets its number once it is placed.", 13)
    return s


# ---------------------------------------------------------------- slide 14
def reg_card(sh, x, y, w, h, region, num):
    rect(sh, x, y, w, h, PANEL_ALT, LINE, 1.5, radius=0.1, name="region card")
    label(sh, x, y + 0.08, w, 0.36, region, 16, TEXT, True, name="region name")
    plate(sh, x + 0.25, y + 0.5, w - 0.5, 0.52, "No. " + num, 24)


def s14(prs):
    s = new_slide(prs, "Numbers survive region changes", "Agreed")
    sh = s.shapes
    g = group(sh, "Two number loops",
              "Two loops. In the first, an engine is British No. 1111, becomes North American No. 2222 and returns "
              "to British No. 1111. In the second, you edit the British number to 3333, and after the same trip "
              "the British number is still 3333. Numbers are examples only.")
    gs = g.shapes
    # loop 1
    rect(gs, 0.6, 1.4, 12.13, 2.0, PANEL, None, radius=0.1, name="loop panel")
    cw, gap = 2.6, 1.35
    x1s = [1.4 + k * (cw + gap) for k in range(3)]
    for x, (r, n) in zip(x1s, [("British", "1111"), ("North American", "2222"), ("British", "1111")]):
        reg_card(gs, x, 1.6, cw, 1.15, r, n)
    for k in range(2):
        arrow(gs, x1s[k] + cw + 0.1, 2.17, x1s[k + 1] - 0.1, 2.17, ORANGE, 3.0, name="switch arrow")
    path(gs, [(x1s[2] + cw / 2, 2.78), (x1s[2] + cw / 2, 3.15), (x1s[0] + cw / 2, 3.15), (x1s[0] + cw / 2, 2.82)],
         ORANGE, 2.25, True, MSO_LINE.DASH, name="return arrow")
    # loop 2
    rect(gs, 0.6, 3.55, 12.13, 2.1, PANEL, None, radius=0.1, name="loop panel")
    cw2, gap2 = 2.2, 0.95
    x2s = [0.85 + k * (cw2 + gap2) for k in range(4)]
    cards = [("British", "1111"), ("British", "3333"), ("North American", "2222"), ("British", "3333")]
    for x, (r, n) in zip(x2s, cards):
        reg_card(gs, x, 3.78, cw2, 1.15, r, n)
    for k in range(3):
        arrow(gs, x2s[k] + cw2 + 0.1, 4.35, x2s[k + 1] - 0.1, 4.35, ORANGE, 3.0, name="switch arrow")
    pencil(gs, x2s[0] + cw2 + 0.32, 3.62, 0.3, AMBER)
    label(gs, x2s[0] + cw2 + 0.02, 4.42, gap2 - 0.04, 0.3, "You edit", 14, TEXT, True, name="edit label")
    path(gs, [(x2s[3] + cw2 / 2, 4.96), (x2s[3] + cw2 / 2, 5.3), (x2s[1] + cw2 / 2, 5.3), (x2s[1] + cw2 / 2, 5.0)],
         ORANGE, 2.25, True, MSO_LINE.DASH, name="return arrow")
    label(sh, 0.6, 5.78, 3.0, 0.3, "Example only", 14, MUTED, True, align="l", name="example label")
    finish(s, "Switch region and back, and your engine gets its old number back. A number you changed stays changed.",
           14)
    return s


# ---------------------------------------------------------------- slide 15
def s15(prs):
    s = new_slide(prs, "Two numbering styles", "Agreed")
    sh = s.shapes
    g = group(sh, "Standardised against Historical Operator",
              "Two cards. Standardised shows engines of three sizes with number plates in one consistent format. "
              "Historical Operator shows engines with plates in different formats and colours, like the old "
              "railway companies.")
    gs = g.shapes
    cards = [(0.6, "Standardised", "One consistent scheme", False),
             (6.88, "Historical Operator", "Rules like the old railway companies", True)]
    for x, head, desc, hist in cards:
        rect(gs, x, 1.45, 5.85, 3.4, PANEL, LINE, 1.5, radius=0.1, name="style card")
        label(gs, x + 0.3, 1.55, 5.3, 0.5, head, 24, TEXT, True, align="l", name="card heading")
        label(gs, x + 0.3, 2.05, 5.3, 0.7, desc, 18, MUTED, align="l", anchor="t", name="card description")
        cols = [STYLE_A, STYLE_B, STYLE_C] if hist else [ORANGE] * 3
        for k in range(3):
            cx = x + 1.15 + k * 1.78
            u = 0.088
            W = {0: 11.4, 1: 17.9, 2: 20.2}[k] * u
            style_ = "tank" if k == 0 else "tender"
            engine(gs, cx - W / 2, 3.4, u, style_, k + 1, cols[k] if hist else ORANGE)
            rect(gs, cx - 0.9, 3.4, 1.8, 0.04, STEEL, None, name="rail")
            if hist:
                digit_plate(gs, cx - 0.8, 3.7, 1.6, 0.8, [4, 3, 5][k], cols[k], band=cols[k] if k != 1 else None)
            else:
                digit_plate(gs, cx - 0.8, 3.7, 1.6, 0.8, 4, ORANGE)
    ichip(sh, "Undecided", 0.6, 5.1, "Exact data: undecided (OQ29)")
    finish(s, "The world picks how numbers look: simple and consistent, or like the old operators'.", 15)
    return s


# ---------------------------------------------------------------- slide 16
def s16(prs):
    s = new_slide(prs, "Changing the style", "Agreed")
    sh = s.shapes
    g = group(sh, "Number plate before and after switching style",
              "A number plate in two parts. Before, the first part is set by the scheme and the last part is your "
              "digits. After switching style, the first part changes and your digits stay the same.")
    gs = g.shapes
    label(gs, 1.2, 2.05, 3.0, 0.3, "Example only", 14, MUTED, True, align="l", name="example label")
    for x0, first, a_lab, b_lab, changed in ((1.2, "47", "Set by the scheme", "Your digits", False),
                                            (7.65, "31", "Changes", "Stays", True)):
        wa, wb = 1.6, 2.8
        rect(gs, x0, 2.85, wa, 1.3, ORANGE if changed else PANEL_ALT, ORANGE, 3.0, radius=0.1,
             name="plate part: scheme", text=first, size=54, color=DARK if changed else TEXT, bold=True)
        rect(gs, x0 + wa, 2.85, wb, 1.3, COAL, ORANGE, 3.0, radius=0.1, name="plate part: digits", text="298",
             size=54, color=TEXT, bold=True)
        for a, b, lab in ((x0, x0 + wa, a_lab), (x0 + wa, x0 + wa + wb, b_lab)):
            path(gs, [(a + 0.08, 4.3), (a + 0.08, 4.45), (b - 0.08, 4.45), (b - 0.08, 4.3)], MUTED, 2.0, False,
                 name="bracket")
            label(gs, (a + b) / 2 - 1.25, 4.53, 2.5, 0.4, lab, 18, TEXT, True, name="bracket label")
    arrow(gs, 5.8, 3.5, 7.45, 3.5, ORANGE, 4.0, name="switch arrow")
    label(gs, 5.6, 2.97, 2.05, 0.4, "Switch style", 18, TEXT, True, name="arrow label")
    finish(s, "Switching style keeps the digits you chose, where they still fit.", 16)
    return s


# ---------------------------------------------------------------- slide 17
def s17(prs):
    s = new_slide(prs, "No two the same", "Agreed")
    sh = s.shapes
    g = group(sh, "Number allocation flow",
              "A flow chart. Make a candidate number, then ask: is it taken? If yes, go back and make another. "
              "If no, reserve it.")
    gs = g.shapes
    rect(gs, 0.9, 2.85, 3.4, 1.3, PANEL_ALT, ORANGE, 2.5, radius=0.1, name="step: make", text="Make a candidate number",
         size=20, color=TEXT, bold=True)
    diamond(gs, 5.3, 2.4, 2.8, 2.2, text="Taken?")
    rect(gs, 9.7, 2.85, 3.0, 1.3, PANEL_ALT, GREEN, 2.5, radius=0.1, name="step: reserve", text="Reserve it", size=20,
         color=TEXT, bold=True)
    arrow(gs, 4.3, 3.5, 5.3, 3.5, ORANGE, 3.0, name="flow arrow")
    arrow(gs, 8.1, 3.5, 9.7, 3.5, ORANGE, 3.0, name="flow arrow")
    label(gs, 8.4, 3.07, 1.0, 0.36, "No", 18, TEXT, True, name="branch label")
    path(gs, [(6.7, 4.6), (6.7, 5.2), (2.6, 5.2), (2.6, 4.2)], ORANGE, 3.0, True, name="loop back arrow")
    label(gs, 6.85, 4.72, 1.0, 0.36, "Yes", 18, TEXT, True, align="l", name="branch label")
    ichip(sh, "Undecided", 0.9, 5.65, "Which pool: undecided (OQ29)")
    finish(s, "Two engines cannot share a number. The game retries until it finds a free one.", 17)
    return s


# ---------------------------------------------------------------- slide 18
def s18(prs):
    s = new_slide(prs, "Reuse and overflow", "Agreed")
    sh = s.shapes
    g = group(sh, "Number reuse and overflow",
              "Left: a dismantled engine's number returns to the number pool. Right: when a pool is full, a clearly "
              "modern overflow number such as X-00001 is used. The number is an example only.")
    gs = g.shapes
    line(gs, 6.65, 1.5, 6.65, 5.95, LINE, 2.0, dash=MSO_LINE.DASH, name="divider")
    # left: reuse
    hg = group(gs, "dismantled engine", "Faded outline of a dismantled engine.")
    engine(hg.shapes, 1.0, 2.65, 0.2, "tender", 2, STEEL)
    ghost(hg, STEEL, 0.25, MUTED)
    rails_strip(gs, 0.8, 2.65, 4.2, sleepers=False)
    label(gs, 1.0, 2.75, 3.6, 0.36, "Dismantled", 18, TEXT, True, name="engine label")
    pool_box(gs, 1.0, 4.1, 3.8, 1.4, 4, 3, filled={0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, empty_hl=1,
             name="number pool")
    plate_blank(gs, 1.75, 3.3, 0.9, 0.42)
    arrow(gs, 2.2, 3.74, 2.2, 4.28, ORANGE, 3.0, name="return arrow")
    label(gs, 1.0, 5.55, 3.8, 0.36, "Number pool", 18, TEXT, True, name="pool label")
    # right: overflow
    pool_box(gs, 7.4, 1.55, 3.8, 1.4, 4, 3, filled=12, name="full pool")
    label(gs, 7.4, 3.0, 3.8, 0.36, "Pool full", 18, TEXT, True, name="pool label")
    arrow(gs, 9.3, 3.45, 9.3, 3.95, ORANGE, 3.0, name="overflow arrow")
    plate(gs, 8.0, 4.0, 2.6, 0.85, "X-00001", 32, border=AMBER)
    label(gs, 10.8, 4.0, 1.9, 0.85, "Overflow", 18, TEXT, True, align="l", name="plate label")
    label(gs, 8.0, 4.9, 2.6, 0.3, "Example only", 14, MUTED, name="example label")
    ichip(sh, "Undecided", 8.0, 5.4, "Format: undecided")
    finish(s, "A dismantled engine's number goes back to the pool. If a pool is full, a clearly modern number is used.",
           18)
    return s


SLIDES = [s10, s11, s12, s13, s14, s15, s16, s17, s18]
