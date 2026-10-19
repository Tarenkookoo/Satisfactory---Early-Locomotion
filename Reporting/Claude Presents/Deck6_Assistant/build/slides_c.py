"""Chunk 3: slides 17 to 23."""
from lib import *

PLACEHOLDER = "Placeholder avatar. Her look is undecided (OQ15)."


def tab(sh, x, y, w, h, fill, line_c=None, lw=1.5, name="tab", dash=None):
    return shape(sh, MSO_SHAPE.ROUND_2_SAME_RECTANGLE, x, y, w, h, fill, line_c, lw, dash=dash, name=name,
                 adj=[0.22, 0])


# ---------------------------------------------------------------- slide 17
def s17(prs):
    s = new_slide(prs, "A home for rail", "Proposed")
    sh = s.shapes
    g = group(sh, "Mock build menu tab strip",
              "A mock build menu. A strip of grey tabs includes the vanilla Transport tab. Beside it is a "
              "highlighted extra tab with a train icon, labelled: Rail tab, name undecided. Below the strip is an "
              "empty grid of build items.")
    gs = g.shapes
    px, py, pw, ph = 0.9, 1.65, 11.53, 3.75
    rect(gs, px, py, pw, ph, PANEL, LINE, 2.0, radius=0.1, name="build menu panel")
    ty, th = 1.85, 0.85
    # unlabelled grey tabs (other tabs in the strip)
    for k in range(3):
        tab(gs, 1.2 + k * 1.27, ty, 1.15, th, PANEL_ALT, LINE, 1.5, name="other tab")
        rect(gs, 1.2 + k * 1.27 + 0.3, ty + 0.3, 0.55, 0.22, LINE, None, radius=0.05, name="other tab icon")
    # vanilla Transport tab
    tx = 1.2 + 3 * 1.27
    tab(gs, tx, ty, 2.1, th, "#4A515B", STEEL, 1.5, name="Transport tab")
    label(gs, tx, ty, 2.1, th, "Transport", 20, TEXT, True, name="tab label")
    # highlighted extra tab with a train icon
    ex = tx + 2.1 + 0.2
    tab(gs, ex, ty - 0.1, 4.85, th + 0.1, ORANGE, None, name="Rail tab")
    loco_side(gs, ex + 0.25, ty + 0.16, 0.95, DARK, name="tab train")
    label(gs, ex + 1.35, ty - 0.1, 3.4, th + 0.1, "Rail tab: name undecided", 18, DARK, True, align="l",
          name="tab label")
    # body: blank item grid, with a thin line under the strip
    rect(gs, 1.2, ty + th, ex - 1.2, 0.06, LINE, None, name="strip rule")
    rect(gs, ex, ty + th, 4.85, 0.06, ORANGE, None, name="active rule")
    for r in range(2):
        for c in range(9):
            rect(gs, 1.2 + c * 1.235, 3.3 + r * 1.0, 1.08, 0.8, PANEL_ALT, LINE, 1.0, radius=0.06, name="item slot")
    label(gs, tx, ty + th + 0.1, 2.1, 0.3, "The game's own tab", 14, MUTED, name="vanilla note")
    ichip(sh, "Undecided", 0.9, 5.6, "Exact layout: undecided (OQ19)")
    finish(s, "Rail could get its own build menu tab instead of hiding in Transport.", 17)
    return s


# ---------------------------------------------------------------- slide 18
def icon_track(sh, cx, cy):
    for k in range(7):
        rect(sh, cx - 0.9 + k * 0.3, cy - 0.35, 0.1, 0.9, SLEEPER, None, name="sleeper")
    rect(sh, cx - 1.0, cy - 0.15, 2.0, 0.08, STEEL, None, name="rail")
    rect(sh, cx - 1.0, cy + 0.25, 2.0, 0.08, STEEL, None, name="rail")


def icon_station(sh, cx, cy):
    station_building(sh, cx - 0.95, cy - 0.5, 1.1, 0.85, name="station")
    rect(sh, cx - 1.05, cy + 0.35, 1.3, 0.14, "#D5D9DE", None, name="platform")
    poly(sh, [(cx + 0.65, cy - 0.35), (cx + 0.9, cy + 0.05), (cx + 0.4, cy + 0.05)], WATER, None, name="drop point")
    oval(sh, cx + 0.4, cy - 0.12, 0.5, 0.5, WATER, None, name="drop body")


def icon_train(sh, cx, cy):
    mini_train(sh, cx - 1.0, cy - 0.3, 2.0, name="train icon")
    rect(sh, cx - 1.1, cy + 0.38, 2.2, 0.06, STEEL, None, name="rail")


def s18(prs):
    s = new_slide(prs, "Four groups?", "Proposed")
    sh = s.shapes
    g = group(sh, "Four proposed group cards",
              "Four proposed group cards with simple icons: Railway Infrastructure, Stations and Servicing, "
              "Signalling and Rolling Stock.")
    gs = g.shapes
    cards = [("Railway Infrastructure", icon_track), ("Stations and Servicing", icon_station),
             ("Signalling", None), ("Rolling Stock", icon_train)]
    tw, gap = 2.8, 0.31
    for i, (t, ic) in enumerate(cards):
        x = 0.6 + i * (tw + gap)
        y = 1.6
        rect(gs, x, y, tw, 4.1, PANEL, PURPLE, 2.5, radius=0.1, dash=MSO_LINE.DASH, name="proposed card")
        rect(gs, x + 0.25, y + 0.3, tw - 0.5, 2.4, PANEL_ALT, None, radius=0.08, name="icon panel")
        cx, cy = x + tw / 2, y + 1.5
        if ic:
            ic(gs, cx, cy)
        else:
            semaphore(gs, cx - 0.2, cy + 0.8, 1.35, "clear", name="icon semaphore")
        label(gs, x + 0.15, y + 2.9, tw - 0.3, 1.0, t, 22, TEXT, True, name="card label")
    finish(s, "Parts could sit in four groups: track, stations, signals and trains.", 18)
    return s


# ---------------------------------------------------------------- slide 19
def s19(prs):
    s = new_slide(prs, "Can the game do it?", "Undecided")
    sh = s.shapes
    g = group(sh, "Question card",
              "A question card with a big question mark: does the game allow a new top-level tab? Not yet checked.")
    gs = g.shapes
    rect(gs, 1.4, 1.75, 10.53, 3.55, PANEL, MUTED, 2.5, radius=0.12, dash=MSO_LINE.DASH, name="question card")
    # ghost tab strip icon
    for k in range(3):
        tab(gs, 1.8 + k * 1.1, 2.1, 1.0, 0.55, PANEL_ALT, LINE, 1.5, name="ghost tab")
    tab(gs, 1.8 + 3 * 1.1, 2.0, 1.5, 0.65, None, MUTED, 2.5, name="dashed new tab", dash=MSO_LINE.DASH)
    label(gs, 1.8, 3.1, 6.7, 1.7, "Does the game allow a new top-level tab?", 34, TEXT, True, align="l", anchor="m",
          name="QUESTION")
    oval(gs, 8.9, 2.25, 2.4, 2.4, None, MUTED, 4, name="question disc", text="?", size=96, color=TEXT, bold=True)
    label(sh, 1.4, 5.5, 2.0, 0.4, "OQ19", 18, MUTED, True, align="l", name="FOOTER")
    finish(s, "Whether the game allows a new tab is not yet checked.", 19)
    return s


# ---------------------------------------------------------------- slide 20
def s20(prs):
    s = new_slide(prs, "Reactions to your trains", "Proposed")
    sh = s.shapes
    avatar(sh, 4.6, 1.7, 1.75)
    speech_bubble(sh, 6.7, 2.2, 3.4, 1.35, "...", TEXT, DARK, size=48, tail="l", name="guide bubble",
                  tail_len=0.5, tail_w=0.4)
    rect(sh, 6.7, 3.95, 3.4, 0.55, PANEL, MUTED, 2.0, radius=0.08, dash=MSO_LINE.DASH, name="dialogue note",
         text="Dialogue not written yet.", size=18, color=TEXT, bold=True)
    label(sh, 2.3, 5.45, 4.6, 0.55, PLACEHOLDER, 14, MUTED, align="c", anchor="m", name="PLACEHOLDER LABEL")
    finish(s, "She might react to special liveries and famous engines. Rarely, not on every placement.", 20)
    return s


# ---------------------------------------------------------------- slide 21
def icon_doc(sh, cx, cy):
    rect(sh, cx - 0.3, cy - 0.4, 0.6, 0.8, TEXT, None, radius=0.05, name="script page")
    for r in range(4):
        rect(sh, cx - 0.2, cy - 0.28 + r * 0.17, 0.4 if r != 3 else 0.24, 0.07, MUTED, None, name="script line")


def icon_frame(sh, cx, cy):
    rect(sh, cx - 0.42, cy - 0.32, 0.84, 0.64, TEXT, None, radius=0.05, name="art frame")
    poly(sh, [(cx - 0.34, cy + 0.24), (cx - 0.08, cy - 0.06), (cx + 0.08, cy + 0.12), (cx + 0.2, cy - 0.02),
              (cx + 0.34, cy + 0.24)], MUTED, None, name="art hills")
    oval(sh, cx + 0.12, cy - 0.25, 0.16, 0.16, MUTED, None, name="art sun")


def icon_lesson(sh, cx, cy):
    rect(sh, cx - 0.4, cy - 0.35, 0.8, 0.7, TEXT, None, radius=0.06, name="lesson screen")
    play_tri(sh, cx + 0.02, cy, 0.34, MUTED)


def icon_menu_tab(sh, cx, cy):
    tab(sh, cx - 0.42, cy - 0.35, 0.5, 0.26, TEXT, None, name="menu tab")
    tab(sh, cx + 0.12, cy - 0.35, 0.3, 0.26, MUTED, None, name="menu tab")
    rect(sh, cx - 0.42, cy - 0.09, 0.84, 0.46, TEXT, None, radius=0.04, name="menu body")


def s21(prs):
    s = new_slide(prs, "Where this stands", "Provisional")
    sh = s.shapes
    g = group(sh, "Four planned steps",
              "A row of four steps, all planned and none built yet: guide script, character art, lessons and "
              "build menu tab. Dashed outlines show they are not built.")
    gs = g.shapes
    items = [("Guide script: planned", icon_doc), ("Character art: planned", icon_frame),
             ("Lessons: planned", icon_lesson), ("Build menu tab: planned", icon_menu_tab)]
    tw, gap = 2.8, 0.31
    for i, (t, ic) in enumerate(items):
        x = 0.6 + i * (tw + gap)
        y = 1.7
        rect(gs, x, y, tw, 3.4, PANEL, MUTED, 2.5, radius=0.1, dash=MSO_LINE.DASH, name="planned step")
        oval(gs, x + tw / 2 - 0.65, y + 0.35, 1.3, 1.3, PANEL_ALT, MUTED, 2.5, dash=MSO_LINE.DASH, name="planned disc")
        ic(gs, x + tw / 2, y + 1.0)
        label(gs, x + 0.15, y + 2.0, tw - 0.3, 1.2, t, 22, TEXT, True, name="step label")
        if i < 3:
            line(gs, x + tw + 0.04, y + 1.0, x + tw + gap - 0.04, y + 1.0, MUTED, 3, dash=MSO_LINE.SQUARE_DOT,
                 tail=True, name="planned link")
    ichip(sh, "Provisional", 0.6, 5.5, "Plans can change.")
    finish(s, "The guide, lessons and menu are planned. They are not built yet.", 21)
    return s


# ---------------------------------------------------------------- slide 22
def s22(prs):
    s = new_slide(prs, "Still undecided", "Undecided")
    sh = s.shapes
    g = group(sh, "Eight open questions",
              "A grid of eight cards, each with an Undecided tag and an open question: her name, her look, library "
              "layout, origin story, which lessons and when, milestone voice lines, how the surprise works, and "
              "build menu layout.")
    gs = g.shapes
    qs = ["Her name (OQ15)", "Her look (OQ15)", "Library layout (OQ15)", "Origin story (OQ16)",
          "Which lessons, and when (OQ17)", "Milestone voice lines (OQ17)", "How the surprise works (OQ18)",
          "Build menu layout (OQ19)"]
    tw, th, gap, gy = 2.8, 2.0, 0.31, 0.3
    for i, q in enumerate(qs):
        col, row = i % 4, i // 4
        x = 0.6 + col * (tw + gap)
        y = 1.6 + row * (th + gy)
        rect(gs, x, y, tw, th, PANEL, MUTED, 2.0, radius=0.1, name="question card")
        chip(gs, "Undecided", x + 0.2, y + 0.2, 1.55, 0.34, 14, name="CHIP CARD")
        label(gs, x + 0.2, y + 0.7, tw - 0.4, 1.15, q, 20, TEXT, True, align="l", anchor="m", name="question")
    finish(s, "These questions are open. Nothing here has been chosen yet.", 22)
    return s


# ---------------------------------------------------------------- slide 23
def s23(prs):
    s = new_slide(prs, "Image credits", None)
    sh = s.shapes
    rect(sh, 0.6, 2.95, 12.13, 1.7, PANEL, None, radius=0.08, name="second line panel")
    label(sh, 0.9, 2.95, 11.53, 1.7, "All drawings are native shapes made for this deck.", 28, TEXT, True,
          name="SECOND LINE")
    finish(s, "This deck uses no photographs.", 23)
    return s


SLIDES = [s17, s18, s19, s20, s21, s22, s23]
