"""Slides 1 to 9 of Deck 2 (signals and signal boxes)."""
from lib import *

RED_T, GREEN_T, AMBER_T = C["red_text"], C["green"], C["amber"]
# block boundaries shared by slides 4 and 5 (SIG-28 spec: signals at x 3.7, 6.7, 9.7)
BX = [0.8, 3.7, 6.7, 9.7, 12.5]


def s01(d):
    c = d.slide(1, "Signals and Signal Boxes", None, title_box=(0.6, 1.95, 6.6, 2.1), size=54)
    sh = c.shapes
    textbox(sh, 0.6, 1.45, 6.4, 0.4, "Early Locomotion: a mod for Satisfactory", 14, C["muted"], name="Series line")
    rect(sh, 0.6, 4.2, 1.6, 0.08, fill=C["orange"], name="Orange rule")
    textbox(sh, 0.6, 4.5, 6.2, 1.2, "How steam railways keep trains apart, and how the mod plans to do it.",
            20, C["text"], anchor="t", name="Caption")
    picture(sh, "R03_semaphore_stop.jpg", 7.55, 0.45, 5.18, 6.2,
            "The mod's semaphore stop signal model with its arm flat (stop).", focus=(0.55, 0.5))
    credit(sh, 7.55, 6.72, 5.18, "Early Locomotion project render. Blender model, not yet in the game.", h=0.4)


def s02(d):
    c = d.slide(2, "How to read this guide", None)
    sh = c.shapes
    rows = [("A", "Decided."), ("P", "Suggested, not confirmed."), ("V", "A test number that may change."),
            ("U", "Still an open question."), ("B", "A real-world fact.")]
    g = group(sh, "Tag legend", "A legend of the five status tags and what each one means.")
    for i, (tag, meaning) in enumerate(rows):
        y = 1.55 + i * 0.95
        rect(g.shapes, 1.6, y, 10.1, 0.74, fill=C["panel"], radius=0.08)
        chip(g.shapes, tag, x=1.9, y=y + 0.17)
        textbox(g.shapes, 3.8, y, 7.7, 0.74, meaning, 20, C["text"], name=f"Meaning: {TAGS[tag][0]}")
    c.finish("Every idea carries a tag in the top-right corner.")


def s03(d):
    c = d.slide(3, "The problem", "B")
    sh = c.shapes
    g = group(sh, "Why signals exist",
              "Top: two trains head towards each other with no warning. Bottom: a train needs a long distance "
              "to stop, much more than the driver can see.")
    gs = g.shapes
    rect(gs, 0.6, 1.4, 12.13, 2.35, fill=C["panel"], line=C["line"], line_w=1, radius=0.08)
    rect(gs, 0.6, 3.85, 12.13, 2.4, fill=C["panel"], line=C["line"], line_w=1, radius=0.08)
    # top: head-on
    ty = 3.0
    rails(gs, 0.8, ty, 11.7)
    train(gs, 2.9, ty, "right", 2)
    train(gs, 7.67, ty, "left", 2)
    cx, cy = 6.67, 2.62
    for ang in (45, -45):
        r = rect(gs, cx - 0.45, cy - 0.07, 0.9, 0.14, fill=C["red"])
        r.rotation = ang % 360
    textbox(gs, 4.67, 1.5, 4.0, 0.45, "No warning: crash", 18, RED_T, bold=True, align="c")
    # bottom: stopping distance
    by = 5.55
    rails(gs, 0.8, by, 11.7)
    train(gs, 0.9, by, "right", 2)
    nose = 3.66
    textbox(gs, nose, 3.95, 6.6, 0.4, "Long stopping distance", 18, AMBER_T, bold=True)
    rect(gs, nose, 4.4, 10.3 - nose, 0.18, fill=C["amber"], radius=0.05)
    rect(gs, nose, 4.7, 2.55, 0.18, fill=C["elec"], radius=0.05)
    textbox(gs, nose + 2.7, 4.6, 4.5, 0.38, "How far the driver can see", 18, C["elec"], bold=True)
    line(gs, 10.3, 4.3, 10.3, 6.1, C["text"], 2, dash=MSO_LINE.DASH)
    c.finish("Trains cannot swerve. They need a long way to stop. Signals keep them apart.")


def _blocks_track(gs, ty):
    rails(gs, 0.8, ty, 11.7)
    for x in BX[1:-1]:
        line(gs, x, ty - 1.15, x, ty + 1.35, C["muted"], 1.5, dash=MSO_LINE.DASH)


def s04(d):
    c = d.slide(4, "Blocks", "B")
    sh = c.shapes
    ty = 3.75
    g = group(sh, "Track split into blocks",
              "A straight track split into four blocks, A to D. One train sits in block B, so B is occupied "
              "and the other three are free.")
    gs = g.shapes
    _blocks_track(gs, ty)
    train(gs, 4.05, ty, "right", 2, scale=0.87)
    dimension(gs, BX[2], BX[3], ty - 0.85, "One block")
    names = "ABCD"
    for i in range(4):
        occ = i == 1
        block_band(gs, BX[i] + 0.04, ty + 0.7, BX[i + 1] - BX[i] - 0.08, "occupied" if occ else "free",
                   f"{names[i]}: {'Occupied' if occ else 'Free'}")
    c.finish("Split the track into blocks. Keep one train in each block.")


def s05(d):
    c = d.slide(5, "Signals guard the blocks", "B")
    sh = c.shapes
    ty = 3.75
    g = group(sh, "Blocks and signals",
              "Four blocks, A to D, with three signals. The signal before occupied block B shows stop; the "
              "other two show clear. A second train in block A waits.")
    gs = g.shapes
    rails(gs, 0.8, ty, 11.7)
    names = "ABCD"
    for i in range(4):
        occ = i == 1
        block_band(gs, BX[i] + 0.04, ty + 0.7, BX[i + 1] - BX[i] - 0.08, "occupied" if occ else "free",
                   f"{names[i]}: {'Occupied' if occ else 'Free'}")
    train(gs, 4.1, ty, "right", 2, scale=0.87)
    train(gs, 1.1, ty, "right", 2, scale=0.7)
    base = ty + 0.34
    for x, st in zip(BX[1:4], ("stop", "clear", "clear")):
        semaphore(gs, x, base, st)
        textbox(gs, x - 0.7, 2.0, 1.4, 0.4, "STOP" if st == "stop" else "CLEAR", 18,
                RED_T if st == "stop" else GREEN_T, bold=True, align="c")
    textbox(gs, 2.0, 2.5, 1.4, 0.4, "Waits", 18, AMBER_T, bold=True, align="c")
    arrow(gs, 2.7, 2.92, 2.7, 3.2, C["amber"], 2.25)
    leg = rect(gs, 0.8, 5.5, 5.2, 0.5, fill=C["panel"], line=C["line"], line_w=1, radius=0.08)
    set_text(leg, "Arm flat = stop. Arm raised = go.", 16, C["text"], bold=True, margins=(0.15, 0, 0.1, 0))
    set_name(leg, "Legend")
    c.finish("A signal at the start of each block says stop or go.")


def s06(d):
    c = d.slide(6, "A semaphore", "B")
    sh = c.shapes
    g = group(sh, "Semaphore parts",
              "A large semaphore signal with its arm flat. Labels point to the post, arm, pivot, lamp and wire. "
              "Two small copies show the stop and clear positions.")
    gs = g.shapes
    base = 5.37
    line(gs, 0.9, base, 8.3, base, C["steel"], 1.5)
    px = 4.0
    semaphore(gs, px, base, "stop", scale=3.2, name="Large signal")
    pivot = (px, base - 3.52 + 0.32)
    # wire: down from the arm, then along the ground
    poly(gs, [(5.6, pivot[1] + 0.224), (5.6, 5.2), (8.2, 5.2)], line_c=C["orange"], line_w=2.25,
         close=False, dash=MSO_LINE.DASH, name="Wire")
    callout(gs, "Lamp", (1.0, 1.97, 1.3, 0.4), (2.35, pivot[1]), (3.08, pivot[1]), align="r")
    callout(gs, "Post", (1.0, 3.5, 1.3, 0.4), (2.35, 3.7), (3.81, 3.7), align="r")
    callout(gs, "Pivot", (4.7, 3.1, 1.2, 0.4), (4.68, 3.2), (px + 0.03, pivot[1] + 0.03))
    callout(gs, "Arm", (6.6, pivot[1] - 0.2, 1.0, 0.4), (6.55, pivot[1]), (6.2, pivot[1]))
    callout(gs, "Wire", (5.85, 3.55, 1.0, 0.4), (5.83, 3.75), (5.62, 3.75))
    # two small copies
    rect(gs, 8.7, 1.6, 4.03, 3.2, fill=C["panel"], line=C["line"], line_w=1, radius=0.08)
    semaphore(gs, 9.7, 4.0, "stop", scale=1.5, name="Small signal: stop")
    semaphore(gs, 11.4, 4.0, "clear", scale=1.5, name="Small signal: clear")
    textbox(gs, 9.2, 4.15, 1.6, 0.4, "STOP", 18, RED_T, bold=True, align="c")
    textbox(gs, 11.2, 4.15, 1.4, 0.4, "CLEAR", 18, GREEN_T, bold=True, align="c")
    chip(sh, "U", x=8.5, y=5.45, w=4.23, h=0.45, text="Arm style (rises or drops): undecided",
         name="Chip: Undecided (arm style)")
    c.finish("A semaphore is a post with a moving arm. The arm is the message.")


def s07(d):
    c = d.slide(7, "Stop arm and distant arm", "B")
    sh = c.shapes
    g = group(sh, "Stop arm and distant arm",
              "A red stop arm shown flat (stop) and raised (go). An amber distant arm with a notched end shown "
              "flat (be ready to stop) and raised (next signal clear). Three night lamps: red, yellow, green.")
    gs = g.shapes
    base = 3.85
    textbox(gs, 0.8, 1.45, 2.4, 0.35, "Stop arm", 16, C["muted"], bold=True)
    textbox(gs, 4.4, 1.45, 3.0, 0.35, "Distant arm", 16, C["muted"], bold=True)
    semaphore(gs, 1.3, base, "stop", 1.5, "stop", name="Stop arm flat")
    semaphore(gs, 3.2, base, "clear", 1.5, "stop", name="Stop arm raised")
    textbox(gs, 0.6, 3.97, 1.5, 0.4, "STOP", 18, RED_T, bold=True, align="c")
    textbox(gs, 2.5, 3.97, 1.4, 0.4, "GO", 18, GREEN_T, bold=True, align="c")
    semaphore(gs, 5.3, base, "stop", 1.5, "distant", name="Distant arm flat")
    semaphore(gs, 7.5, base, "clear", 1.5, "distant", name="Distant arm raised")
    textbox(gs, 4.35, 3.97, 2.1, 0.8, "Be ready to stop at the next signal", 14, AMBER_T, bold=True,
            align="c", anchor="t")
    textbox(gs, 6.5, 3.97, 2.1, 0.8, "Next signal is clear", 14, GREEN_T, bold=True, align="c", anchor="t")
    # night lamps strip
    rect(gs, 0.6, 5.1, 12.13, 0.9, fill=C["panel"], line=C["line"], line_w=1, radius=0.08)
    textbox(gs, 0.85, 5.1, 2.0, 0.9, "Night lamps", 16, C["muted"], bold=True)
    for cx, col, lab, w in ((3.4, C["red"], "Stop", 1.5), (6.2, C["amber"], "Distant warning", 3.0),
                            (10.4, C["green"], "Clear", 1.5)):
        ellipse(gs, cx, 5.55, 0.5, fill=col, line="#FFFFFF", line_w=1.5)
        textbox(gs, cx + 0.4, 5.3, w, 0.5, lab, 18, C["text"], bold=True)
    picture(sh, "P13_distant_signal_henley.jpg", 9.75, 1.45, 2.8, 2.1,
            "A semaphore distant signal beside the line near Henley-in-Arden, arm raised.")
    credit(sh, 9.75, 3.6, 2.8, "Richard Dunn, CC BY-SA 2.0. Wikimedia Commons.", h=0.3)
    textbox(sh, 9.75, 4.0, 2.8, 0.6, "A real distant signal, arm raised.", 14, C["text"], anchor="t")
    c.finish("A stop arm orders a stop. A distant arm only warns you.")


def _panel_wire(gs, ox, broken):
    oy = 1.45
    rect(gs, ox, oy, 5.9, 3.85, fill=C["panel"], line=C["line"], line_w=1, radius=0.08)
    textbox(gs, ox + 0.25, oy + 0.07, 3.5, 0.4, "Wire broken" if broken else "Wire intact", 18, C["text"], bold=True)
    box_building(gs, ox + 0.3, 3.0, 1.6, 2.15, windows=False, door=False, name="Signal box (lever)")
    lever(gs, ox + 1.05, 4.95, C["red"], pulled=True)
    post_x, base_y, sc = ox + 3.9, 5.15, 1.8
    pivot_y = base_y - 1.1 * sc + 0.1 * sc
    semaphore(gs, post_x, base_y, "stop" if broken else "clear", sc, "stop", name="Signal")
    tail = (post_x - 0.4, pivot_y) if broken else (post_x - 0.28, pivot_y + 0.28)
    line(gs, post_x, pivot_y, tail[0], tail[1], C["steel"], 4)
    lev_top = (ox + 1.43, 4.13)
    if not broken:
        poly(gs, [lev_top, (tail[0], 4.13), tail], line_c=C["orange"], line_w=2.25, close=False,
             dash=MSO_LINE.DASH, name="Wire")
        textbox(gs, post_x + 0.3, 4.3, 1.5, 0.4, "CLEAR", 18, GREEN_T, bold=True)
    else:
        line(gs, lev_top[0], 4.13, ox + 2.55, 4.13, C["orange"], 2.25, dash=MSO_LINE.DASH)
        poly(gs, [(ox + 3.2, 4.13), (tail[0], 4.13), tail], line_c=C["orange"], line_w=2.25, close=False,
             dash=MSO_LINE.DASH, name="Wire (far piece)")
        bx, by = ox + 2.87, 4.13
        for ang in (45, -45):
            r = rect(gs, bx - 0.28, by - 0.05, 0.56, 0.1, fill=C["red"])
            r.rotation = ang % 360
        # counterweight hanging under the arm, pulling it flat
        line(gs, post_x + 0.3, pivot_y + 0.12, post_x + 0.3, pivot_y + 0.5, C["steel"], 2)
        rect(gs, post_x + 0.3 - 0.15, pivot_y + 0.5, 0.3, 0.3, fill=C["steel"], line="#FFFFFF", line_w=1,
             name="Counterweight")
        arrow(gs, post_x + 0.3, pivot_y + 0.9, post_x + 0.3, pivot_y + 1.35, C["orange"], 2.25)
        textbox(gs, post_x + 0.6, 4.3, 1.4, 0.4, "STOP", 18, RED_T, bold=True)


def s08(d):
    c = d.slide(8, "If the wire breaks", "B")
    sh = c.shapes
    g = group(sh, "Wire intact and wire broken",
              "Left: a lever in a signal box pulls a wire and the arm rises. Right: the wire is broken, so "
              "a counterweight pulls the arm flat to stop.")
    _panel_wire(g.shapes, 0.6, broken=False)
    _panel_wire(g.shapes, 6.83, broken=True)
    chip(sh, "U", x=4.39, y=5.5, w=4.55, h=0.45, text="The mod's failure rule: undecided (OQ03)",
         name="Chip: Undecided (failure rule)")
    c.finish("On real railways, a broken wire drops the arm to stop.")


def _icon_window(gs, x, y, s=1.1):
    g = group(gs, "Window icon", "An icon of a high window with several panes.")
    rect(g.shapes, x, y + 0.1, s, s - 0.2, fill=C["blue"], alpha=40, line=C["post"], line_w=2)
    for k in (1, 2):
        line(g.shapes, x + s * k / 3, y + 0.1, x + s * k / 3, y + s - 0.1, C["post"], 1.5)
    line(g.shapes, x, y + s / 2, x + s, y + s / 2, C["post"], 1.5)


def _icon_levers(gs, x, y, s=1.1):
    g = group(gs, "Lever frame icon", "An icon of a row of levers.")
    cols = [C["red"], C["amber"], C["red"], C["blue"]]
    for i, col in enumerate(cols):
        lever(g.shapes, x + 0.15 + i * 0.27, y + s - 0.1, col, pulled=False, h=0.8)


def s09(d):
    c = d.slide(9, "The signal box", "B")
    sh = c.shapes
    picture(sh, "P14_williton_signal_box.jpg", 0.6, 1.4, 4.0, 4.7,
            "Williton signal box on the West Somerset Railway.", focus=(0.5, 0.2))
    credit(sh, 0.6, 6.13, 4.0, "Reading Tom, CC BY 2.0. Wikimedia Commons.")
    g = group(sh, "Three parts of a signal box",
              "Three rows with icons: high windows give a good view of the track; the signaller works the "
              "levers; the lever frame is inside.")
    gs = g.shapes
    rows = [("High windows", ": a good view of the track", "window"),
            ("The signaller", ": works the levers", "person"),
            ("Lever frame", ": inside", "levers")]
    for i, (head, rest, icon) in enumerate(rows):
        y = 1.4 + i * 1.65
        rect(gs, 5.1, y, 7.63, 1.4, fill=C["panel"], radius=0.08)
        ix, iy = 5.4, y + 0.15
        if icon == "window":
            _icon_window(gs, ix, iy)
        elif icon == "person":
            person_icon(gs, ix + 0.55, iy + 1.05, scale=1.8)
        else:
            _icon_levers(gs, ix, iy)
        textbox(gs, 6.9, y, 5.6, 1.4, [[(head, {"bold": True}), (rest, {})]], 20, C["text"])
    c.finish("A signal box is a small building. A signaller works the signals from it.")


SLIDES = [s01, s02, s03, s04, s05, s06, s07, s08, s09]
