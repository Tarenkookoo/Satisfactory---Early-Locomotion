"""Chunk 2: slides 9 to 16."""
from el_lib import *
import el_lib as L


def bar_row(S, x, y, w, name, frac):
    label(S, x, y - 0.05, 1.1, 0.4, name, size=16, bold=True)
    rect(S, x + 1.25, y + 0.04, w, 0.24, fill=LINE, radius=0.12)
    rect(S, x + 1.25, y + 0.04, max(0.25, w * frac), 0.24, fill=ORANGE, radius=0.12)


# ------------------------------------------------------------------ 9 jobs, not a ladder
def s09(prs):
    s = new_slide(prs, 'Jobs, not a ladder', 9, chip='Agreed')
    S = s.shapes
    # "Same category" bracket made of two segments either side of the label
    cy = 1.72
    label(S, 5.2, cy - 0.2, 2.93, 0.4, 'Same category', size=16, bold=True, color=MUTED, align='c', name='Label: same category')
    for (xa, xb) in ((0.9, 5.05), (8.28, 12.43)):
        line(S, xa, cy, xb, cy, color=MUTED, lw=1.5)
    line(S, 0.9, cy, 0.9, cy + 0.2, color=MUTED, lw=1.5)
    line(S, 12.43, cy, 12.43, cy + 0.2, color=MUTED, lw=1.5)
    specs = ((0.9, dict(n_wheels=4, boiler=1.0, tender=0.0, tank=True), 1.15, (('Pull', 0.88), ('Speed', 0.34), ('Range', 0.52)),
              'A stocky tank engine with a bar profile: strong pull, low speed, middling range.'),
             (6.83, dict(n_wheels=5, boiler=1.3, tender=0.9), 1.0, (('Pull', 0.46), ('Speed', 0.9), ('Range', 0.72)),
              'A longer engine with a tender and a different bar profile: lighter pull, high speed, long range.'))
    for x, kw, u, bars, alt in specs:
        g = group(s, 'Engine card', alt + ' Shape only.')
        gs = g.shapes
        rect(gs, x, 2.1, 5.6, 3.5, fill=PANEL, line=STEEL, lw=1.5, radius=0.08)
        gw = engine_geom(0, u, boiler=kw['boiler'], tender=kw.get('tender', 0.0))['width']
        engine(gs, x + (5.6 - gw) / 2, 2.3, u, **kw)
        for i, (nm, fr) in enumerate(bars):
            bar_row(gs, x + 0.35, 3.82 + i * 0.55, 3.7, nm, fr)
    label(S, 0.9, 5.72, 11.53, 0.4, 'Shape only. Not measured.', size=14, italic=True, color=MUTED, align='c', name='Note: shape only')
    caption(s, 'Every engine has its own strengths. They are not simply reskins.')
    slide_number(s)
    return s


# ------------------------------------------------------------------ 10 express
def s10(prs):
    s = new_slide(prs, 'What “express” means here', 10, chip='Agreed')
    base = 4.95
    g = group(s, 'Fast freight train', 'A steam engine pulling two freight wagons to the right, with speed lines trailing behind it: fast freight.')
    gs = g.shapes
    ground(gs, 0.8, base, 7.6)
    u = 1.5
    ex = 3.95
    engine(gs, ex, base - u, u, n_wheels=4, boiler=1.2, tender=0.95)
    freight_wagon(gs, 2.45, base, 1.4, 0.75)
    freight_wagon(gs, 0.95, base, 1.4, 0.75)
    for (xa, xb, yy) in ((0.95, 2.95, 3.35), (1.25, 2.55, 3.65), (0.95, 2.2, 3.95)):
        line(gs, xa, yy, xb, yy, color=TEXT, lw=2.25)
    label(s.shapes, 0.8, 5.4, 7.6, 0.45, 'Fast freight', size=18, bold=True, align='c', name='Label: fast freight')
    c = group(s, 'Passenger coach with crossed-out ticket sales', 'A passenger coach, with a ticket icon above it crossed out by a red X: the game has no passenger economy.')
    cs = c.shapes
    ground(cs, 8.9, base, 3.8)
    coach(cs, 9.2, base, w=3.2, h=0.85)
    # ticket icon with notches, crossed out
    tx, ty = 10.0, 2.2
    rect(cs, tx, ty, 1.6, 0.85, fill=AMBER, radius=0.08)
    oval(cs, tx - 0.12, ty + 0.3, 0.24, 0.24, fill=BG)
    oval(cs, tx + 1.48, ty + 0.3, 0.24, 0.24, fill=BG)
    line(cs, tx + 0.35, ty + 0.3, tx + 1.25, ty + 0.3, color=INK, lw=2)
    line(cs, tx + 0.35, ty + 0.55, tx + 1.0, ty + 0.55, color=INK, lw=2)
    line(cs, tx - 0.25, ty - 0.15, tx + 1.85, ty + 1.0, color=RED, lw=6)
    line(cs, tx + 1.85, ty - 0.15, tx - 0.25, ty + 1.0, color=RED, lw=6)
    label(cs, 9.2, 3.22, 3.2, 0.4, 'Ticket sales', size=16, bold=True, align='c', name='Label: ticket sales')
    label(s.shapes, 8.9, 5.4, 3.8, 0.45, 'Passenger coach', size=18, bold=True, align='c', name='Label: passenger coach')
    caption(s, 'Here, express means fast freight. The game has no passenger economy.')
    slide_number(s)
    return s


# ------------------------------------------------------------------ shelf helpers
def tile_engine(gs, x, y, w, h, kind, dashed=False):
    """A shelf slot (w x h) holding a small engine icon of the given kind."""
    kinds = {
        'tank': dict(n_wheels=3, boiler=0.95, tank=True),
        'tender': dict(n_wheels=4, boiler=1.1, tender=0.85),
        'heavy': dict(n_wheels=5, boiler=1.3, tender=0.95),
        'small': dict(n_wheels=2, boiler=0.8),
        'mid': dict(n_wheels=3, boiler=1.0, tender=0.6),
    }
    kw = kinds[kind]
    rect(gs, x, y, w, h, fill=PANEL, line=MUTED if dashed else STEEL, lw=1.5, radius=0.08, dash=DOT if dashed else None)
    if dashed:
        return
    u = min(0.5, (h - 0.3) * 0.62)
    gw = engine_geom(0, u, boiler=kw['boiler'], tender=kw.get('tender', 0.0))['width']
    if gw > w - 0.16:
        u = u * (w - 0.16) / gw
        gw = engine_geom(0, u, boiler=kw['boiler'], tender=kw.get('tender', 0.0))['width']
    engine(gs, x + (w - gw) / 2, y + (h - u) / 2, u, **kw)


# ------------------------------------------------------------------ 11 cap on the roster
def s11(prs):
    s = new_slide(prs, 'A cap on the roster', 11, chip='Agreed')
    g = group(s, 'Shelf with a cap', 'A shelf with a limited number of engine slots, then a bookend, then dotted empty slots beyond it: the roster is capped.')
    gs = g.shapes
    tw, th, gap = 1.05, 1.55, 0.15
    x0 = 1.15
    y0 = 2.7
    kinds = ['small', 'tank', 'tender', 'mid', 'heavy', 'tank']
    x = x0
    for k in kinds:
        tile_engine(gs, x, y0, tw, th, k)
        x += tw + gap
    stop_x = x + 0.05
    rect(gs, stop_x, y0 - 0.2, 0.16, th + 0.4, fill=STEEL, radius=0.04)
    x = stop_x + 0.16 + 0.3
    for _ in range(3):
        tile_engine(gs, x, y0, tw, th, 'tank', dashed=True)
        x += tw + gap
    end_x = x - gap
    rect(gs, x0 - 0.2, y0 + th + 0.05, end_x - x0 + 0.4, 0.16, fill=SLEEPER, radius=0.04)
    inline_chip(s.shapes, x0, 4.95, 'Proposed', 'Lots of variety: an aspiration')
    inline_chip(s.shapes, stop_x + 0.16 + 0.3, 4.95, 'Undecided', 'Total: undecided (OQ20)')
    caption(s, 'The number of engines is capped on purpose, so choice stays clear.')
    slide_number(s)
    return s


# ------------------------------------------------------------------ 12 regions need not match
def s12(prs):
    s = new_slide(prs, 'Regions need not match', 12, chip='Agreed')
    tw, th, gap = 1.6, 1.3, 0.14
    rows = (('Region A', ['tank', 'tender', 'heavy', 'small', 'tender', 'mid'], 1.55),
            ('Region B', ['mid', 'heavy', 'tank', 'small'], 3.85))
    for nm, kinds, y in rows:
        label(s.shapes, 0.9, y, 3.0, 0.4, nm, size=18, bold=True, name='Label: ' + nm)
        g = group(s, nm + ' shelf', nm + ': a shelf of ' + 'engines of different shapes. The two regions have shelves of different lengths.')
        gs = g.shapes
        x = 0.9
        for k in kinds:
            tile_engine(gs, x, y + 0.5, tw, th, k)
            x += tw + gap
        rect(gs, 0.7, y + 0.5 + th + 0.05, x - 0.9 + 0.4 - gap, 0.16, fill=SLEEPER, radius=0.04)
    caption(s, 'Each region gets the engines that suit its own tradition. Counts need not match.')
    slide_number(s)
    return s


# ------------------------------------------------------------------ 13 two sides of a card
def s13(prs):
    s = new_slide(prs, 'Two sides of a card', 13, chip='Agreed')
    cx0, cy0, cw, ch = 0.9, 1.5, 11.53, 4.6
    mid = cx0 + cw / 2
    base = group(s, 'Card frame', 'A mock engine card split into two halves by a vertical line.')
    rect(base.shapes, cx0, cy0, cw, ch, fill=PANEL, line=STEEL, lw=1.5, radius=0.1)
    line(base.shapes, mid, cy0 + 0.2, mid, cy0 + ch - 0.2, color=LINE, lw=2)
    halves = (
        (cx0 + 0.25, mid - cx0 - 0.5, 'History and character', LINE, TEXT,
         ['Class', 'Builder', 'Operator', 'Era', 'Purpose', 'Reputation'], 0.56, 1),
        (mid + 0.25, mid - cx0 - 0.5, 'Early Locomotion gameplay', ORANGE, INK,
         ['Duties', 'Strengths', 'Weaknesses', 'Role'], 0.85, 2))
    for hx, hw, title, hfill, htc, items, pitch, nbars in halves:
        g = group(s, 'Card side: ' + title, 'The ' + title + ' side of the card, with labelled grey placeholder bars. No real facts are shown.')
        gs = g.shapes
        boxed(gs, hx, cy0 + 0.25, hw, 0.6, title, size=20, bold=True, fill=hfill, color=htc, radius=0.08)
        for i, it in enumerate(items):
            ry = cy0 + 1.1 + i * pitch
            label(gs, hx + 0.1, ry - 0.02, 1.5, 0.34, it, size=16, bold=True)
            for b in range(nbars):
                bw = (3.3, 2.6)[b] if nbars == 2 else (3.3, 2.7, 3.0, 2.2, 3.1, 2.5)[i]
                rect(gs, hx + 1.75, ry + 0.06 + b * 0.3, bw, 0.18, fill=MUTED, alpha=45, radius=0.09)
    caption(s, 'Each card tells the real history, then what the engine does in the game.')
    slide_number(s)
    return s


# ------------------------------------------------------------------ 14 honest history
def s14(prs):
    s = new_slide(prs, 'Honest history', 14, chip='Agreed')
    g = group(s, 'Two lines: real purpose and in the game',
              'Two rows. Real purpose shows a passenger coach. In the game shows a fast freight engine with wagons.')
    gs = g.shapes
    boxed(gs, 0.9, 1.95, 2.5, 0.65, 'Real purpose', size=20, bold=True, fill=PANEL_ALT, line=STEEL, lw=1.75, radius=0.32)
    boxed(gs, 0.9, 3.85, 2.5, 0.65, 'In the game', size=20, bold=True, fill=PANEL_ALT, line=ORANGE, lw=2, radius=0.32)
    arrow(gs, 2.15, 2.72, 2.15, 3.73, color=ORANGE)
    # row 1: passenger coach
    b1 = 2.6
    ground(gs, 4.0, b1, 8.4)
    coach(gs, 6.2, b1, w=3.4, h=0.9)
    # row 2: fast freight
    b2 = 4.5
    ground(gs, 4.0, b2, 8.4)
    u = 0.95
    engine(gs, 8.2, b2 - u, u, n_wheels=4, boiler=1.15, tender=0.9)
    freight_wagon(gs, 6.7, b2, 1.4, 0.7)
    freight_wagon(gs, 5.2, b2, 1.4, 0.7)
    for (xa, xb, yy) in ((4.2, 5.0, 3.85), (4.4, 5.1, 4.15)):
        line(gs, xa, yy, xb, yy, color=TEXT, lw=2.25)
    banner = boxed(s.shapes, 0.9, 5.35, 11.53, 0.62, 'Example only: built for passengers, used here for fast freight.', size=18,
                   bold=True, fill=None, line=AMBER, lw=2, radius=0.08)
    name_it(banner, 'Label: example only')
    caption(s, 'History says what an engine was really built for, even if the game uses it differently.')
    slide_number(s)
    return s


# ------------------------------------------------------------------ 15 the golden age
def s15(prs):
    s = new_slide(prs, 'The golden age', 15, chip='Proposed')
    ty = 2.4
    g = group(s, 'Golden Era timeline', 'A timeline with a band labelled Golden Era. A question mark sits at each end because the dates are not set.')
    gs = g.shapes
    line(gs, 0.9, ty, 2.05, ty, color=STEEL, lw=2.25)
    line(gs, 2.75, ty, 3.6, ty, color=STEEL, lw=2.25, dash=DASH)
    line(gs, 9.7, ty, 10.55, ty, color=STEEL, lw=2.25, dash=DASH)
    arrow(gs, 11.25, ty, 12.4, ty, color=STEEL)
    for cx in (2.4, 10.9):
        question_mark(gs, cx, ty, 0.7, color=MUTED, size=28, fill=BG)
    boxed(gs, 3.6, ty - 0.45, 6.1, 0.9, 'Golden Era', size=26, bold=True, fill=ORANGE, color=INK, radius=0.1)
    chip, cw = inline_chip(s.shapes, (13.333 - 2.9) / 2, 3.15, 'Undecided', 'Dates: undecided (OQ21)')
    names = ('Great Western', 'LNER', 'LMS', 'Southern', 'British Railways')
    widths = [text_w(n, 18, True) + 0.6 for n in names]
    total = sum(widths) + 0.25 * (len(names) - 1)
    bx = (13.333 - total) / 2
    b = group(s, 'Operator badges', 'Five text badges for railway operators: Great Western, LNER, LMS, Southern and British Railways.')
    for n, w in zip(names, widths):
        boxed(b.shapes, bx, 4.0, w, 0.6, n, size=18, bold=True, fill=PANEL_ALT, line=STEEL, lw=1.5, radius=0.3)
        bx += w + 0.25
    label(s.shapes, 0.9, 4.95, 11.53, 0.5, 'Operators shape history and looks, not menus.', size=20, bold=True, color=TEXT, align='c',
          name='Label: operators')
    caption(s, 'Fleets would mostly come from steam’s golden age. The exact dates are not set.')
    slide_number(s)
    return s


# ------------------------------------------------------------------ 16 unlocks keep pace
def s16(prs):
    s = new_slide(prs, 'Unlocks keep pace', 16, chip='Agreed')
    xs = [3.0, 5.2, 7.4, 9.6, 11.7]
    core_y, pack_y = 2.75, 5.0
    label(s.shapes, 2.6, 1.55, 2.0, 0.35, 'Early', size=14, bold=True, color=MUTED, name='Label: early')
    label(s.shapes, 10.4, 1.55, 2.0, 0.35, 'Later', size=14, bold=True, color=MUTED, align='r', name='Label: later')
    lbl = group(s, 'Track names', 'Two parallel tier tracks, one named Core and one named Pack.')
    label(lbl.shapes, 0.9, core_y - 0.25, 1.4, 0.5, 'Core', size=22, bold=True, color=ORANGE)
    label(lbl.shapes, 0.9, pack_y - 0.25, 1.4, 0.5, 'Pack', size=22, bold=True, color=TEXT)
    # guides first (behind), then tracks
    gd = group(s, 'Stage guides', 'Dashed vertical guides line the stages of the two tracks up.')
    for x in xs:
        line(gd.shapes, x, core_y + 0.2, x, pack_y - 1.1, color=MUTED, lw=1.25, dash=DASH)
    ct = group(s, 'Core track', 'The Core track: a line with five stage markers, early on the left and later on the right.')
    arrow(ct.shapes, 2.4, core_y, 12.5, core_y, color=STEEL, lw=3)
    for x in xs:
        oval(ct.shapes, x - 0.17, core_y - 0.17, 0.34, 0.34, fill=ORANGE, line=BG, lw=2)
    pt = group(s, 'Pack track', 'The Pack track: a line with engines standing at the stages. Small engines sit at the early stages and larger ones at the later stages.')
    arrow(pt.shapes, 2.4, pack_y, 12.5, pack_y, color=STEEL, lw=3)
    plan = ((0, dict(n_wheels=3, boiler=0.9, tank=True), 0.5), (1, dict(n_wheels=4, boiler=1.0, tender=0.8), 0.56),
            (3, dict(n_wheels=4, boiler=1.15, tender=0.9), 0.62), (4, dict(n_wheels=5, boiler=1.3, tender=1.0), 0.68))
    for i, kw, u in plan:
        gw = engine_geom(0, u, boiler=kw['boiler'], tender=kw.get('tender', 0.0))['width']
        engine(pt.shapes, xs[i] - gw / 2, pack_y - u - 0.0, u, dashed=True, outline=ORANGE, **kw)
    inline_chip(s.shapes, 2.4, 5.5, 'Undecided', 'Exact stages: undecided (OQ20)')
    caption(s, 'Owning a pack does not skip the game. Its engines unlock alongside the core ones.')
    slide_number(s)
    return s


BUILDERS = [s09, s10, s11, s12, s13, s14, s15, s16]
