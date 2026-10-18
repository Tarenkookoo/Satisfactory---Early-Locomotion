"""Chunk 4: slides 32-42 (signal limits, later signals, monorail, packs, regions, guide, status, credits)."""
from pptx.enum.shapes import MSO_SHAPE

import lib
from lib import (C, IMAGES, MARGIN, RIGHT, add_base, arrow, badge, blend, box, box_building, chip,
                 chip_w, credit, finish, group, inline_chip, label, line, oval, photo, picture, pill,
                 poly, polyline, rails, signal, table, text_width_in, train)


# ------------------------------------------------------------------ 32
def s32(prs, n):
    b = add_base(prs, n, 'Signals', 'Early limits', 'Provisional',
                 'Early signals have limits: short blocks, a speed cap and a limited number per box. '
                 'Numbers are provisional.')
    sh = b.shapes
    tiles = [('Block length', 'about 400 to 500 m'), ('Speed cap', 'about 60 km/h'),
             ('Signals per box', '6 to 8 (station box), 12 to 16 (dedicated box)'),
             ('Box reach', 'about 1 to 1.5 km of track')]
    g = group(sh, 'Early limits tiles', 'Four provisional limits: block length about 400 to 500 m; '
              'speed cap about 60 km/h; 6 to 8 signals for a station box and 12 to 16 for a dedicated '
              'box; box reach about 1 to 1.5 km of track.')
    for k, (head, val) in enumerate(tiles):
        x = MARGIN + k * 3.11
        box(g.shapes, x, 1.5, 2.8, 2.2, fill=C['panel'], radius=0.1)
        label(g.shapes, x + 0.18, 1.62, 2.5, 0.36, head, size=18, bold=True, color=C['orange'])
        label(g.shapes, x + 0.18, 2.0, 2.5, 1.1, val, size=18, bold=True)
        inline_chip(g.shapes, 'Provisional', x + 0.18, 3.18)
    rg = group(sh, 'Ruler', 'A ruler under the track with a signal about every 450 metres, for illustration.')
    s = rg.shapes
    ty = 4.45
    rails(s, 0.9, ty, 11.5)
    for k in range(6):
        x = 1.1 + k * 2.16
        signal(s, x, ty + 0.4, 'stop', scale=0.6, show_label=False)
        line(s, x, ty + 0.45, x, ty + 0.6, C['muted'], 1.5)
        label(s, x - 0.6, ty + 0.6, 1.2, 0.3, '{:,} m'.format(k * 450), size=14, align='c',
              color=C['muted'])
    lbl = 'Block lengths and speed caps:'
    label(sh, MARGIN, 5.55, 4.0, 0.36, lbl, size=16, anchor='m')
    inline_chip(sh, 'Undecided', MARGIN + text_width_in(lbl, 16) + 0.15, 5.55, text='Undecided (OQ03)')
    finish(b)


# ------------------------------------------------------------------ 33
def s33(prs, n):
    b = add_base(prs, n, 'Signals', 'No wiring for you', 'Agreed',
                 'Boxes take control of connected signals automatically. Rods and wires are drawn for you, '
                 'as a visual layer.')
    sh = b.shapes
    ctext = 'Rod or wire look: undecided (OQ04)'
    inline_chip(sh, 'Undecided', RIGHT - chip_w(ctext), 0.98, text=ctext)
    photo(sh, 'P16', MARGIN, 1.5, 5.2, 3.47)
    steps = ['Place signals on connected track', 'A box with room takes control',
             'Rods and wires draw themselves']
    g = group(sh, 'Steps', 'Three steps: place a signal on connected track; a box with room takes '
              'control; rods and wires draw themselves and update.')
    for k, t in enumerate(steps):
        y = 1.55 + k * 0.95
        box(g.shapes, 6.2, y, 6.53, 0.8, fill=C['panel'], radius=0.08)
        badge(g.shapes, 6.6, y + 0.4, k + 1, d=0.46, size=18)
        label(g.shapes, 7.05, y, 5.6, 0.8, t, size=20, anchor='m')
    sg = group(sh, 'Box screen', 'The box screen lists its signals, their state, capacity and reach.')
    s = sg.shapes
    box(s, 6.3, 4.5, 0.75, 0.52, fill=C['panel_alt'], line=C['steel'], lw=1.5, radius=0.04)
    for k in range(3):
        box(s, 6.4, 4.58 + k * 0.13, 0.55, 0.06, fill=C['orange'] if k == 0 else C['steel'])
    box(s, 6.6, 5.02, 0.15, 0.1, fill=C['steel'])
    label(s, 7.25, 4.45, 5.4, 0.62, 'Box screen: signals, state, capacity, reach.', size=18, anchor='m')
    finish(b)


# ------------------------------------------------------------------ 34
def s34(prs, n):
    b = add_base(prs, n, 'Signals', 'Later signals and manual control', 'Agreed',
                 'Better signals come later. Drivers can also set points from a simple track diagram.')
    sh = b.shapes
    g = group(sh, 'Signal timeline', 'Timeline: start with semaphore blocks (agreed); later, better '
              'semaphores or interlocking (proposed); mature, electronic signals like vanilla (proposed).')
    s = g.shapes
    line(s, 1.05, 1.95, 1.05, 4.75, C['steel'], 3)
    nodes = [('Start: semaphore blocks', 'Agreed', True), ('Later: better semaphore or interlocking', 'Proposed', False),
             ('Mature: electronic signals like vanilla', 'Proposed', False)]
    for k, (t, kind, filled) in enumerate(nodes):
        y = 1.95 + k * 1.4
        oval(s, 1.05, y, 0.42, fill=C['orange'] if filled else C['bg'], line=C['orange'], lw=3)
        label(s, 1.5, y - 0.25, 5.8, 0.45, t, size=20, anchor='m')
        inline_chip(s, kind, 1.5, y + 0.25)
    # manual operations diagram mock-up
    pg = group(sh, 'Track diagram panel', 'A dark track-diagram panel with mode buttons AUTO, YARD and '
               'MAINLINE. Lines and nodes show the network; the chosen route is bright orange and the '
               'other routes are grey.')
    s = pg.shapes
    X, Y, W, H = 8.33, 1.45, 4.4, 3.3
    box(s, X, Y, W, H, fill=C['coal'], line=C['steel'], lw=1.5, radius=0.12)
    mx = X + 0.25
    for m in ('AUTO', 'YARD', 'MAINLINE'):
        w = chip_w(m)
        pill(s, mx, Y + 0.2, w, 0.36, m, C['panel_alt'], C['text'], 14, line=C['steel'])
        mx += w + 0.12
    grey, org = C['line'], C['orange']
    A, B, Cc, D = (X + 0.45, Y + 2.0), (X + 1.55, Y + 2.0), (X + 2.75, Y + 1.2), (X + 3.95, Y + 1.2)
    E, F, G2 = (X + 2.75, Y + 2.0), (X + 3.95, Y + 2.0), (X + 3.95, Y + 2.8)
    for p, q in ((B, E), (E, F), (E, G2)):
        line(s, p[0], p[1], q[0], q[1], grey, 5)
    for p, q in ((A, B), (B, Cc), (Cc, D)):
        line(s, p[0], p[1], q[0], q[1], org, 6)
    for p in (A, B, Cc, D, E, F, G2):
        oval(s, p[0], p[1], 0.24, fill='F2F2F2', line=C['coal'], lw=1)
    poly(s, [(A[0] - 0.12, A[1] - 0.32), (A[0] + 0.12, A[1] - 0.32), (A[0], A[1] - 0.16)], fill=org)
    t = 'Pick a destination and let the game set points:'
    label(sh, X, 4.85, W, 0.62, t, size=18)
    inline_chip(sh, 'Proposed', X, 5.5)
    finish(b)


# ------------------------------------------------------------------ 35
def _route(s, px, py, a_b='steam', b_rest='steam'):
    """Route A-B-C with branch B-D inside a panel at (px, py). Steam = orange double line,
    electric = single thick blue beam."""
    A, B, Cc, D = (px + 0.45, py + 1.7), (px + 1.75, py + 1.7), (px + 3.3, py + 1.7), (px + 2.85, py + 2.5)

    def seg(p, q, kind):
        if kind == 'steam':
            dx, dy = q[0] - p[0], q[1] - p[1]
            L = (dx * dx + dy * dy) ** 0.5
            ox, oy = -dy / L * 0.06, dx / L * 0.06
            line(s, p[0] + ox, p[1] + oy, q[0] + ox, q[1] + oy, C['orange'], 2.25)
            line(s, p[0] - ox, p[1] - oy, q[0] - ox, q[1] - oy, C['orange'], 2.25)
        else:
            line(s, p[0], p[1], q[0], q[1], C['electric'], 7)

    seg(A, B, a_b)
    seg(B, Cc, b_rest)
    seg(B, D, b_rest)
    return A, B, Cc, D


def s35(prs, n):
    b = add_base(prs, n, 'Later', 'Upgrading to the monorail', 'Agreed',
                 'Upgrade steam track in place. The route stays. Steam trains cannot use the converted part.')
    sh = b.shapes
    W, H, Y = 3.75, 3.85, 1.5
    xs = [MARGIN, MARGIN + W + 0.44, MARGIN + 2 * (W + 0.44)]
    for k, x in enumerate(xs[:2]):
        box(sh, x + W + 0.07, Y + 1.5, 0.3, 0.4, fill=C['orange'], shape=MSO_SHAPE.RIGHT_ARROW, deco=True)
    # panel 1: before
    g1 = group(sh, 'Before', 'Before: a steam route with a branch, all two-rail steam track, stations as circles.')
    s = g1.shapes
    box(s, xs[0], Y, W, H, fill=C['panel'], radius=0.1)
    label(s, xs[0] + 0.2, Y + 0.12, 2.5, 0.42, 'Before', size=20, bold=True)
    for p in _route(s, xs[0], Y):
        oval(s, p[0], p[1], 0.3, fill=C['bg'], line=C['text'], lw=2)
    # panel 2: upgrade
    g2 = group(sh, 'Upgrade', 'Upgrade: one section shows a translucent blue hologram of monorail with small '
               'pylons, and an amber warning that steam trains cannot use this section (proposed).')
    s = g2.shapes
    x = xs[1]
    box(s, x, Y, W, H, fill=C['panel'], radius=0.1)
    label(s, x + 0.2, Y + 0.12, 2.5, 0.42, 'Upgrade', size=20, bold=True)
    A, B, Cc, D = _route(s, x, Y)
    box(s, A[0] - 0.1, A[1] - 0.17, B[0] - A[0] + 0.2, 0.34, fill=blend(C['electric'], C['panel'], 0.4),
        line=C['electric'], lw=1, radius=0.08)
    for k in range(3):
        px_ = A[0] + 0.3 + k * 0.38
        line(s, px_, A[1] - 0.17, px_, A[1] - 0.45, C['electric'], 2)
        line(s, px_ - 0.1, A[1] - 0.45, px_ + 0.1, A[1] - 0.45, C['electric'], 2)
    for p in (A, B, Cc, D):
        oval(s, p[0], p[1], 0.3, fill=C['bg'], line=C['text'], lw=2)
    poly(s, [(x + 0.25, Y + 3.62), (x + 0.75, Y + 3.62), (x + 0.5, Y + 3.15)], fill=C['amber'],
         line=C['ink'], lw=1)
    box(s, x + 0.47, Y + 3.3, 0.06, 0.18, fill=C['ink'])
    oval(s, x + 0.5, Y + 3.54, 0.06, fill=C['ink'])
    label(s, x + 0.85, Y + 2.95, W - 0.95, 0.7, 'Steam trains cannot use this section', size=16, anchor='m')
    inline_chip(s, 'Proposed', x + W - chip_w('Proposed') - 0.12, Y + 0.15)
    # panel 3: mixed network
    g3 = group(sh, 'Mixed network', 'Mixed network (proposed): an electric monorail trunk with steam '
               'branches; at the junction an interchange where cargo moves between the two. A Transfer '
               'Station is possible but undecided.')
    s = g3.shapes
    x = xs[2]
    box(s, x, Y, W, H, fill=C['panel'], radius=0.1)
    label(s, x + 0.2, Y + 0.12, 2.6, 0.42, 'Mixed network', size=20, bold=True)
    inline_chip(s, 'Proposed', x + 0.2, Y + 0.6)
    A, B, Cc, D = _route(s, x, Y, a_b='electric', b_rest='steam')
    for p in (A, Cc, D):
        oval(s, p[0], p[1], 0.3, fill=C['bg'], line=C['text'], lw=2)
    box(s, B[0] - 0.22, B[1] - 0.22, 0.44, 0.44, fill=C['panel_alt'], line=C['amber'], lw=2.5)
    box(s, B[0] - 0.33, B[1] - 0.75, 0.22, 0.2, fill=C['sleeper'], line=C['amber'], lw=1)
    arrow(s, B[0] - 0.08, B[1] - 0.65, B[0] + 0.35, B[1] - 0.65, C['amber'], 2, hs='lg')
    label(s, x + 0.2, Y + 2.85, W - 0.4, 0.36, 'Interchange', size=16, bold=True)
    label(s, x + 0.2, Y + 3.2, W - 0.4, 0.55, '(possible Transfer Station: undecided)', size=14,
          color=C['text'])
    foot = 'Steam trains cannot move directly between the two track types.'
    label(sh, MARGIN, 5.5, 9.5, 0.36, foot, size=18, anchor='m')
    inline_chip(sh, 'Agreed', MARGIN + text_width_in(foot, 18) + 0.2, 5.5)
    finish(b)


# ------------------------------------------------------------------ 36
def s36(prs, n):
    b = add_base(prs, n, 'Later', 'After launch', 'Proposed',
                 'After launch, optional packs could add locomotives, regional looks and deeper driving. '
                 'The core game stays complete.')
    sh = b.shapes
    g = group(sh, 'Pack stack', 'A stack of blocks: a solid base, Core 1.0, a complete game (agreed); '
              'above it four dashed proposed blocks: regional packs, more locomotives, late-steam '
              'infrastructure and advanced manual driving (optional).')
    s = g.shapes
    base_t = 'Core 1.0: a complete game'
    box(s, MARGIN, 4.0, 7.4, 0.85, fill=C['orange'], radius=0.08, text=base_t, size=22, bold=True,
        color=C['ink'], align='l', margins=(0.25, 0.02, 0.1, 0.02))
    inline_chip(s, 'Agreed', MARGIN + 7.4 - chip_w('Agreed') - 0.2, 4.245)
    blocks = [('Regional packs', 0, 1), ('More locomotives', 1, 1), ('Late-steam infrastructure', 0, 0),
              ('Advanced manual driving (optional)', 1, 0)]
    for t, col, row in blocks:
        x = MARGIN + col * 3.75
        y = 1.55 + row * 1.2
        box(s, x, y, 3.65, 1.05, fill=C['panel'], line=C['purple'], lw=2, radius=0.08, dash='dash')
        label(s, x + 0.2, y + 0.42, 3.3, 0.6, t, size=18, anchor='m')
        inline_chip(s, 'Proposed', x + 0.2, y + 0.1)
    photo(sh, 'P19', 8.93, 1.55, 3.8, 2.53)
    label(sh, 8.93, 4.48, 3.8, 0.62, 'Real British locomotives like this could appear.', size=16)
    lbl = 'Which locomotives:'
    label(sh, MARGIN, 5.2, 3.0, 0.36, lbl, size=18, anchor='m')
    inline_chip(sh, 'Undecided', MARGIN + text_width_in(lbl, 18) + 0.15, 5.2, text='Undecided (OQ20)')
    finish(b)


# ------------------------------------------------------------------ 37
def s37(prs, n):
    b = add_base(prs, n, 'Extras', 'Regions and running numbers', 'Agreed',
                 'The world picks a regional style. Each engine has a hidden permanent ID and a number you can change.')
    sh = b.shapes
    g = group(sh, 'Regional styles', 'Three example regional styles: British, North American and '
              'Continental European. Examples only; launch regions are undecided.')
    s = g.shapes
    for k, t in enumerate(('British', 'North American', 'Continental European')):
        pill(s, MARGIN, 1.6 + k * 0.78, 4.6, 0.6, t, C['panel'], C['text'], 20, line=C['orange'], lw=2)
    l1 = 'Examples only. Launch regions:'
    label(sh, MARGIN, 4.0, 4.0, 0.4, l1, size=18, anchor='m')
    inline_chip(sh, 'Undecided', MARGIN, 4.45, text='Undecided (OQ06)')
    # nameplate
    ng = group(sh, 'Number plate', 'A locomotive number plate reading No. 1234: the visible running '
               'number, which you can change. Under it, a small hidden Fleet ID that never changes.')
    s = ng.shapes
    box(s, 6.3, 1.55, 6.43, 3.4, fill=C['panel'], radius=0.12)
    box(s, 7.2, 1.85, 4.6, 1.45, fill=C['coal'], line=C['orange'], lw=4, radius=0.2,
        text='No. 1234', size=54, bold=True, color=C['orange'])
    label(s, 7.2, 3.36, 4.6, 0.42, 'Visible number', size=18, bold=True, align='c')
    box(s, 7.2, 4.0, 4.6, 0.55, fill=C['panel_alt'], line=C['line'], lw=1, radius=0.08, dash='dash',
        text='Fleet ID: hidden, never changes', size=16, color=C['text'])
    l2 = 'Changing region restyles Core stock. Migration:'
    label(sh, MARGIN, 5.25, 7.0, 0.4, l2, size=18, anchor='m')
    inline_chip(sh, 'Undecided', MARGIN + text_width_in(l2, 18) + 0.15, 5.27)
    finish(b)


# ------------------------------------------------------------------ 38
def s38(prs, n):
    b = add_base(prs, n, 'Extras', 'Your railway guide', 'Agreed',
                 'A friendly railway guide teaches with short animated lessons. Lessons are optional and can be replayed.')
    sh = b.shapes
    g = group(sh, 'Lesson table', 'A miniature lesson scene on a clean white model-railway table: an oval of '
              'track, a tiny train, a semaphore and a signal box, with a caption bubble and playback '
              'controls (pause, replay, back, next).')
    s = g.shapes
    box(s, MARGIN, 1.5, 7.6, 3.5, fill='F2F2F2', radius=0.15)
    oval(s, 4.4, 3.45, 5.3, fill=None, line='5A6068', lw=3, dh=2.45)
    oval(s, 4.4, 3.45, 4.8, fill=None, line='5A6068', lw=3, dh=1.95)
    train(s, 3.55, 4.62, 1, 0.55, name='Tiny train')
    signal(s, 7.6, 3.85, 'clear', scale=0.75, show_label=False, post_col='5A6068')
    box_building(s, 1.15, 2.35, 0.8, 0.55, outline=C['orange'], with_person=False)
    box(s, 2.6, 1.72, 3.6, 0.55, fill=C['panel'], line=C['orange'], lw=1.5,
        shape=MSO_SHAPE.ROUNDED_RECTANGULAR_CALLOUT, text='Short caption here', size=16, color=C['text'])
    # controls
    box(s, MARGIN, 5.12, 7.6, 0.68, fill=C['panel'], radius=0.1)
    cy = 5.46
    x0 = 2.4
    for k in range(4):
        cx = x0 + k * 1.3
        oval(s, cx, cy, 0.5, fill=C['panel_alt'], line=C['steel'], lw=1.5)
        if k == 0:      # pause
            box(s, cx - 0.1, cy - 0.12, 0.07, 0.24, fill=C['text'])
            box(s, cx + 0.03, cy - 0.12, 0.07, 0.24, fill=C['text'])
        elif k == 1:    # replay
            from lib import arc_pts
            polyline(s, arc_pts(cx, cy, 0.12, 0.12, 120, 420, 16), color=C['text'], lw=2, head='end')
        elif k == 2:    # back
            box(s, cx - 0.12, cy - 0.11, 0.04, 0.22, fill=C['text'])
            poly(s, [(cx + 0.11, cy - 0.11), (cx + 0.11, cy + 0.11), (cx - 0.06, cy)], fill=C['text'])
        else:           # next
            box(s, cx + 0.08, cy - 0.11, 0.04, 0.22, fill=C['text'])
            poly(s, [(cx - 0.11, cy - 0.11), (cx - 0.11, cy + 0.11), (cx + 0.06, cy)], fill=C['text'])
    inline_chip(sh, 'Proposed', 8.7, 1.6)
    label(sh, 8.7, 2.05, 4.0, 0.9, 'A playful takeover when you first unlock rail', size=20)
    finish(b)


# ------------------------------------------------------------------ 39
def s39(prs, n):
    b = add_base(prs, n, 'Status', 'Where we are', 'Provisional',
                 "A test engine runs on the game's real rails. Next come the other railway pieces. "
                 'Singleplayer first. Multiplayer after release.')
    sh = b.shapes
    nodes = ['Engine', 'Rolling stock', 'Track', 'Stations', 'Signals', 'Unlocks', 'Tutorials',
             'Release 1.0: singleplayer']
    under_way = {'Engine', 'Track'}
    ly = 4.15
    xs = [1.15 + k * 1.37 for k in range(8)]
    photo(sh, 'R01', 0.6, 1.5, 2.0, 1.3, focus=(0.47, 0.5))
    photo(sh, 'R02', xs[2] - 1.0, 1.5, 2.0, 1.3)
    g = group(sh, 'Roadmap', 'Roadmap: engine and track are under way; rolling stock, stations, signals, '
              'unlocks, tutorials and Release 1.0 for singleplayer are planned; multiplayer comes later.')
    s = g.shapes
    line(s, xs[0], ly, xs[-1], ly, C['steel'], 4)
    line(s, xs[-1], ly, 12.2, ly, C['steel'], 3, dash='dash')
    line(s, 1.6, 3.22, xs[0], ly - 0.25, C['orange'], 1.5)
    line(s, xs[2], 3.22, xs[2], ly - 0.25, C['orange'], 1.5)
    for x, t in zip(xs, nodes):
        if t in under_way:
            oval(s, x, ly, 0.44, fill=C['orange'], line=C['orange'], lw=2.5)
        else:
            oval(s, x, ly, 0.44, fill=C['bg'], line=C['steel'], lw=2.5)
        label(s, x - 0.66, ly + 0.32, 1.32, 0.9, t, size=16, align='c', bold=t in under_way)
    oval(s, 12.2, ly, 0.44, fill=C['bg'], line=C['steel'], lw=2.5, dash='dash')
    label(s, 11.6, ly + 0.32, 1.13, 0.9, 'Later: multiplayer', size=16, align='c')
    lg = group(sh, 'Legend', 'Legend: a filled orange circle means under way; an empty grey circle means planned.')
    oval(lg.shapes, 8.85, 2.42, 0.36, fill=C['orange'], line=C['orange'], lw=2.5)
    label(lg.shapes, 9.15, 2.22, 2.5, 0.4, 'Under way', size=18, anchor='m')
    oval(lg.shapes, 8.85, 2.92, 0.36, fill=C['bg'], line=C['steel'], lw=2.5)
    label(lg.shapes, 9.15, 2.72, 2.5, 0.4, 'Planned', size=18, anchor='m')
    lbl = 'Plans can change.'
    label(sh, 8.65, 1.5, 2.6, 0.4, lbl, size=18, anchor='m')
    inline_chip(sh, 'Provisional', 8.65 + text_width_in(lbl, 18) + 0.15, 1.52)
    finish(b)


# ------------------------------------------------------------------ 40
def s40(prs, n):
    b = add_base(prs, n, 'Status', 'Still undecided', 'Undecided',
                 'These questions are open. Nothing here has been chosen yet.')
    sh = b.shapes
    qs = ['Exact unlock tiers (OQ01)', 'Longest track piece (OQ02)', 'Block lengths and speed caps (OQ03)',
          'How boxes measure their reach (OQ04)', 'Is Medium the fastest? (OQ05)',
          'Which regions at launch? (OQ06)', 'Which extra locomotives? (OQ20)',
          'Pricing and release of packs (OQ26)']
    g = group(sh, 'Open questions', 'Eight open questions, none decided: ' + '; '.join(qs) + '.')
    for k, q in enumerate(qs):
        x = MARGIN + (k % 4) * 3.077
        y = 1.6 + (k // 4) * 1.95
        box(g.shapes, x, y, 2.9, 1.75, fill=C['panel'], radius=0.1)
        inline_chip(g.shapes, 'Undecided', x + 0.18, y + 0.18)
        label(g.shapes, x + 0.18, y + 0.65, 2.6, 1.0, q, size=18)
    finish(b)


# ------------------------------------------------------------------ 41-42
def _credit_rows(slots):
    rows = [['Slot', 'Slide', 'Author', 'Licence', 'Source']]
    for slot in slots:
        info = IMAGES[slot]
        used = ', '.join(str(x) for x in sorted(lib.USAGE.get(slot, [])))
        if info['kind'] == 'photo':
            author, lic = info['credit'].rsplit(', ', 1)
            src = [('Wikimedia ', None), ('Commons', info['url'])]
        else:
            author, lic = 'Early Locomotion project (test model, not final art)', 'No third-party licence'
            src = 'Project render'
        rows.append([slot, used, author, lic, src])
    return rows


def credits_slide(prs, n, title, caption, slots, alt):
    b = add_base(prs, n, 'Credits', title, None, caption)
    sh = b.shapes
    rows = _credit_rows(slots)
    t = table(sh, MARGIN, 1.45, [0.75, 1.05, 5.4, 2.4, 2.53], 0.305, rows, size=11, alt=alt,
              name='Credit table', aligns=['l', 'l', 'l', 'l', 'l'])
    label(sh, MARGIN, 1.45 + 0.305 * len(rows) + 0.12, 9.0, 0.32,
          'CC BY-SA photos are shown unmodified except for resizing.', size=14, color=C['text'])
    finish(b)
    return b


def s41(prs, n):
    credits_slide(prs, n, 'Image credits (1 of 2)',
                  'Photographs come from Wikimedia Commons under Creative Commons licences.',
                  ['P%02d' % k for k in range(1, 13)],
                  'Credit table for photographs P01 to P12: slot, slide, author, licence and a link to the '
                  'source page on Wikimedia Commons.')


def s42(prs, n):
    credits_slide(prs, n, 'Image credits (2 of 2)',
                  'Mod renders belong to the project. They show early test models.',
                  ['P%02d' % k for k in range(13, 20)] + ['R%02d' % k for k in range(1, 6)],
                  'Credit table for photographs P13 to P19 and project renders R01 to R05: slot, slide, '
                  'author, licence and source.')


SLIDES = [s32, s33, s34, s35, s36, s37, s38, s39, s40, s41, s42]
