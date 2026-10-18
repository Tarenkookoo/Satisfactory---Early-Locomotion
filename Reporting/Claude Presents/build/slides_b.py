"""Chunk 2: slides 11-20 (coal, signals primer, glossary, the mod's idea, locomotives)."""
from pptx.enum.shapes import MSO_SHAPE

from lib import (C, MARGIN, RIGHT, add_base, arrow, blend, block_band, box, chip_w, coal_heap,
                 credit, drop, engine, finish, group, icon, inline_chip, label, line, list_row,
                 oval, photo, picture, poly, polyline, rails, signal, state_pill, text_width_in,
                 train, train_width, bar_row)


# ------------------------------------------------------------------ 11
def s11(prs, n):
    b = add_base(prs, n, 'Steam railways', 'Taking on coal', 'Background',
                 'Coal starts higher than the tender. A ramp or tower lets gravity fill it.')
    sh = b.shapes
    photo(sh, 'P08', MARGIN, 1.5, 4.5, 3.375)
    # coal stage (top)
    label(sh, 5.6, 1.42, 3.0, 0.4, 'Coal stage', size=18, bold=True, color=C['orange'])
    g = group(sh, 'Coal stage diagram', 'Coal stage: coal sits on a raised platform and slides down '
              'a chute into the tender below, by gravity.')
    s = g.shapes
    ry = 3.6
    box(s, 5.6, ry, 6.2, 0.07, fill=C['steel'])
    for px in (5.75, 6.75, 7.75, 8.6):
        box(s, px, 2.5, 0.1, ry - 2.5, fill=C['steel'])
    box(s, 5.6, 2.35, 3.2, 0.15, fill=C['sleeper'], line=C['ink'], lw=0.75)
    coal_heap(s, 7.3, 2.35, 1.5, 0.45)
    poly(s, [(8.8, 2.35), (8.8, 2.55), (10.05, 2.95), (10.05, 2.75)], fill=C['steel'], line=C['ink'], lw=0.75)
    box(s, 9.35, 2.85, 2.2, 0.68, fill=C['wagon'], line=C['ink'], lw=1)
    coal_heap(s, 10.0, 2.85, 0.6, 0.12)
    for wx in (9.75, 11.15):
        oval(s, wx, ry - 0.1, 0.2, fill=C['coal'], line=C['steel'], lw=1)
    arrow(s, 8.95, 2.25, 9.9, 2.56, C['orange'], 2.25, hs='lg')
    label(s, 9.0, 1.82, 1.4, 0.36, 'Gravity', size=16, anchor='b')
    # coaling tower (bottom)
    label(sh, 5.6, 3.8, 3.0, 0.4, 'Coaling tower', size=18, bold=True, color=C['orange'])
    g2 = group(sh, 'Coaling tower diagram', 'Coaling tower: coal is lifted to the top of a tall tower '
               'and drops through a hopper into the tender.')
    s = g2.shapes
    ry2 = 6.12
    box(s, 5.6, ry2, 4.6, 0.07, fill=C['steel'])
    box(s, 6.1, 4.3, 1.0, 1.82, fill=C['panel_alt'], line=C['steel'], lw=1.5)
    box(s, 6.18, 4.38, 0.84, 0.45, fill=C['coal'], line=C['coal_line'], lw=1.5)
    poly(s, [(7.1, 4.85), (7.95, 4.85), (7.65, 5.28), (7.4, 5.28)], fill=C['steel'], line=C['ink'], lw=0.75)
    box(s, 7.0, 5.37, 2.2, 0.68, fill=C['wagon'], line=C['ink'], lw=1)
    for wx in (7.4, 8.8):
        oval(s, wx, ry2 - 0.1, 0.2, fill=C['coal'], line=C['steel'], lw=1)
    arrow(s, 8.2, 4.75, 8.2, 5.3, C['orange'], 2.25, hs='lg')
    label(s, 8.35, 4.78, 1.4, 0.4, 'Gravity', size=16, anchor='m')
    photo(sh, 'P09', 10.33, 4.95, 2.4, 0.9)
    finish(b)


# ------------------------------------------------------------------ 12
def s12(prs, n):
    b = add_base(prs, n, 'Steam railways', 'Why trains need signals', 'Background',
                 'Trains cannot swerve. They need a long way to stop. Signals keep them apart.')
    sh = b.shapes
    # top: no signals
    g = group(sh, 'No signals', 'Without signals: two trains on the same track head for each other '
              'with no warning, and crash.')
    s = g.shapes
    box(s, MARGIN, 1.45, 12.13, 1.85, fill=C['panel'], radius=0.08)
    rails(s, 0.9, 2.62, 11.5)
    train(s, 2.1, 2.62, 2, 0.9, facing='right', name='Train A')
    train(s, 7.65, 2.62, 2, 0.9, facing='left', name='Train B')
    cx = (2.1 + train_width(2, 0.9) + 7.65) / 2
    box(s, cx - 0.32, 1.85, 0.64, 0.64, fill=C['red'], shape=MSO_SHAPE.MATH_MULTIPLY)
    box(s, cx + 0.45, 1.6, 2.6, 0.45, fill=C['red_dark'], radius=0.08, text='No warning: crash',
        size=18, bold=True, color=C['text'], align='c')
    # bottom: blocks and signals
    g2 = group(sh, 'With signals', 'With signals: the track is split into three blocks with one train '
               'in each. The second train waits at a stop signal. The lead train needs a long '
               'distance to stop.')
    s = g2.shapes
    box(s, MARGIN, 3.5, 12.13, 2.65, fill=C['panel'], radius=0.08)
    ry = 4.6
    rails(s, 0.9, ry, 11.5)
    xs = (4.6, 8.6)
    lead_x = 4.95
    train(s, lead_x, ry, 2, 0.9, name='Lead train')
    train(s, 1.55, ry, 2, 0.75, name='Following train')
    signal(s, xs[0], ry + 0.38, 'stop', h=1.1, label_pos='topright')
    signal(s, xs[1], ry + 0.38, 'clear', h=1.1, label_pos='topright')
    nose = lead_x + train_width(2, 0.9)
    stop_x = 11.4
    box(s, nose, 5.06, stop_x - nose, 0.18, fill=C['amber'])
    line(s, stop_x, 4.1, stop_x, 5.4, C['amber'], 2.25, dash='dash')
    label(s, nose + 0.1, 5.26, stop_x - nose, 0.35, 'Long stopping distance', size=16, anchor='t')
    for x0, x1, t in ((0.9, xs[0], 'Block 1'), (xs[0], xs[1], 'Block 2'), (xs[1], 12.4, 'Block 3')):
        box(s, x0 + 0.04, 5.72, x1 - x0 - 0.08, 0.34, fill=C['panel_alt'], line=C['steel'], lw=1,
            text=t, size=14, bold=True)
    finish(b)


# ------------------------------------------------------------------ 13
def s13(prs, n):
    b = add_base(prs, n, 'Steam railways', 'Words you will meet', 'Background',
                 'Short meanings for the words in this guide.')
    sh = b.shapes
    terms = [('Vanilla', 'The game without mods.'), ('Tier', 'A step of unlocks.'),
             ('Wagon', 'A vehicle that carries cargo.'),
             ('Tender', 'A coal and water wagon behind an engine.'),
             ('Block', 'A stretch of track that holds one train.'),
             ('Semaphore', 'A signal with a moving arm.'),
             ('Signal box', 'Where a signaller works the signals.'),
             ('Service stop', 'A stop to refill coal and water.')]
    g = group(sh, 'Glossary', 'Eight glossary cards: vanilla, tier, wagon, tender, block, semaphore, '
              'signal box and service stop, each with a short meaning.')
    for k, (term, meaning) in enumerate(terms):
        x = MARGIN + (k % 4) * (2.9 + 0.177)
        y = 1.7 + (k // 4) * 2.0
        box(g.shapes, x, y, 2.9, 1.75, fill=C['panel'], radius=0.08,
            text=[[(term, {'bold': True, 'color': C['orange'], 'size': 20})], meaning],
            size=18, align='l', anchor='t', margins=(0.18, 0.15, 0.15, 0.1), space_after=4)
    finish(b)


# ------------------------------------------------------------------ 14
def _cmp_icon(s, row, side, cx, cy):
    blue, org = C['electric'], C['orange']
    if row == 0:
        if side == 'v':
            box(s, cx - 0.32, cy - 0.06, 0.64, 0.16, fill=blue)
            box(s, cx - 0.05, cy + 0.1, 0.1, 0.18, fill=blue)
        else:
            for dx in (-0.22, 0.0, 0.22):
                box(s, cx + dx - 0.03, cy - 0.2, 0.06, 0.4, fill=C['sleeper'])
            box(s, cx - 0.32, cy - 0.11, 0.64, 0.05, fill=C['steel'])
            box(s, cx - 0.32, cy + 0.07, 0.64, 0.05, fill=C['steel'])
    elif row == 1:
        if side == 'v':
            box(s, cx - 0.17, cy - 0.25, 0.34, 0.5, fill=blue, shape=MSO_SHAPE.LIGHTNING_BOLT)
        else:
            drop(s, cx - 0.12, cy + 0.02, 0.38)
            poly(s, [(cx + 0.02, cy + 0.2), (cx + 0.32, cy + 0.2), (cx + 0.28, cy - 0.02),
                     (cx + 0.15, cy - 0.12), (cx + 0.05, cy)], fill=C['coal'], line=C['coal_line'], lw=1)
    elif row == 2:
        if side == 'v':
            box(s, cx - 0.22, cy - 0.22, 0.44, 0.44, fill=blue, shape=MSO_SHAPE.NO_SYMBOL)
        else:
            polyline(s, [(cx - 0.2, cy + 0.25), (cx - 0.2, cy - 0.2), (cx + 0.22, cy - 0.2), (cx + 0.22, cy)],
                     color=org, lw=4)
            oval(s, cx + 0.22, cy + 0.12, 0.1, fill=C['water'], dh=0.14)
    elif row == 3:
        if side == 'v':
            box(s, cx - 0.12, cy - 0.27, 0.24, 0.54, fill=C['panel_alt'], line=blue, lw=1.5, radius=0.08)
            oval(s, cx, cy - 0.12, 0.13, fill=C['green'])
            oval(s, cx, cy + 0.12, 0.13, fill=C['red'])
        else:
            box(s, cx - 0.03, cy - 0.27, 0.06, 0.54, fill=C['post'])
            box(s, cx + 0.03, cy - 0.22, 0.3, 0.08, fill=C['red'])
    else:
        if side == 'v':
            box(s, cx - 0.15, cy - 0.12, 0.3, 0.24, fill=None, line=blue, lw=2)
        else:
            box(s, cx - 0.33, cy - 0.12, 0.66, 0.24, fill=None, line=org, lw=2)


def s14(prs, n):
    b = add_base(prs, n, "The mod's idea", 'Not "trains, but earlier"', 'Agreed',
                 'Steam rail is not electric trains with an early unlock. It works in its own way.')
    sh = b.shapes
    rows = [('Monorail beam', 'Two-rail track'), ('Electricity', 'Coal and water'),
            ('No refuelling', 'Service stops'), ('Block and path', 'Semaphores and boxes'),
            ('Compact', 'Large')]
    colw, gap = 5.9, 0.33
    xv, xs = MARGIN, MARGIN + colw + gap
    label(sh, xv, 1.42, colw, 0.45, 'Vanilla electric (later)', size=20, bold=True, color=C['electric'])
    label(sh, xs, 1.42, colw, 0.45, 'Early steam (this mod)', size=20, bold=True, color=C['orange'])
    g = group(sh, 'Comparison', 'Comparison in five rows. Vanilla electric: monorail beam, electricity, '
              'no refuelling, block and path signals, compact stations. Early steam: two-rail track, '
              'coal and water, service stops, semaphores and signal boxes, large stations.')
    s = g.shapes
    for k, (v, st) in enumerate(rows):
        y = 1.98 + k * 0.82
        for x, txt, side, col in ((xv, v, 'v', C['electric']), (xs, st, 's', C['orange'])):
            box(s, x, y, colw, 0.7, fill=C['panel'], line=col, lw=1, radius=0.08)
            _cmp_icon(s, k, side, x + 0.5, y + 0.35)
            label(s, x + 1.05, y, colw - 1.2, 0.7, txt, size=20, anchor='m')
    finish(b)


# ------------------------------------------------------------------ 15
def s15(prs, n):
    b = add_base(prs, n, "The mod's idea", 'Every limit has an answer', 'Agreed',
                 'Short range, small loads, a busy line, slow trips: each has a fix.')
    sh = b.shapes
    g = group(sh, 'Limits and answers', 'Four limits, each with arrows to its answers. Short range: '
              'auxiliary tender, service stop or bigger engine. Small loads: a suitable engine and '
              'train length. Busy line: more signals and boxes. Slow overall: convert to monorail later.')
    s = g.shapes
    lx, lw_, ax = MARGIN, 2.8, 4.6

    def limit(y, h, txt):
        box(s, lx, y, lw_, h, fill=C['line'], radius=0.08, text=txt, size=20, bold=True)

    def answer(x, y, w, h, txt):
        box(s, x, y, w, h, fill=C['panel'], line=C['orange'], lw=2, radius=0.08, text=txt, size=18)

    # row 1 fans out to three answers
    limit(2.05, 0.7, 'Short range')
    for k, t in enumerate(('Auxiliary tender', 'Service stop', 'Bigger engine')):
        y = 1.5 + k * 0.62
        answer(ax, y, 3.6, 0.5, t)
        arrow(s, lx + lw_ + 0.05, 2.4, ax - 0.06, y + 0.25, hs='lg')
    rows = [('Small loads', 'A suitable engine and train length'), ('Busy line', 'More signals and boxes'),
            ('Slow overall', 'Convert to monorail later')]
    for k, (lim, ans) in enumerate(rows):
        y = 3.55 + k * 0.85
        limit(y, 0.65, lim)
        arrow(s, lx + lw_ + 0.05, y + 0.325, ax - 0.06, y + 0.325, hs='lg')
        answer(ax, y, 5.4 if k == 0 else 4.2, 0.65, ans)
    finish(b)


# ------------------------------------------------------------------ 16
def s16(prs, n):
    b = add_base(prs, n, "The mod's idea", 'Why steam stays behind electric', 'Agreed',
                 'Steam is cheap and early. Electric wins on speed, throughput, traffic and convenience.')
    sh = b.shapes
    rows = [('Cheap to start', 0.85, 0.45), ('Speed', 0.40, 0.90), ('Throughput', 0.35, 0.90),
            ('Traffic density', 0.35, 0.90), ('Convenience', 0.45, 0.90)]
    g = group(sh, 'Steam against electric', 'Qualitative bars, not measured: steam scores high on cheap '
              'to start; electric scores high on speed, throughput, traffic density and convenience.')
    s = g.shapes
    for k, (name, st, el) in enumerate(rows):
        y = 1.6 + k * 0.86
        label(s, MARGIN, y, 2.35, 0.6, name, size=18, anchor='m')
        box(s, 3.0, y, 6.0, 0.26, fill=C['panel_alt'], radius=0.05)
        box(s, 3.0, y, 6.0 * st, 0.26, fill=C['orange'], radius=0.05)
        box(s, 3.0, y + 0.33, 6.0, 0.26, fill=C['panel_alt'], radius=0.05)
        box(s, 3.0, y + 0.33, 6.0 * el, 0.26, fill=C['electric'], radius=0.05)
    label(s, 3.0, 5.92, 6.0, 0.32, 'Shape only. Not measured.', size=14, color=C['muted'])
    lg = group(sh, 'Legend', 'Legend: orange is steam, blue is electric.')
    box(lg.shapes, 9.6, 1.65, 0.4, 0.26, fill=C['orange'], radius=0.05)
    label(lg.shapes, 10.1, 1.58, 2.5, 0.4, 'Steam', size=18, anchor='m')
    box(lg.shapes, 9.6, 2.15, 0.4, 0.26, fill=C['electric'], radius=0.05)
    label(lg.shapes, 10.1, 2.08, 2.5, 0.4, 'Electric', size=18, anchor='m')
    box(sh, 9.6, 3.1, 3.13, 1.9, fill=C['panel'], line=C['orange'], lw=1.5, radius=0.08,
        text='Steam gets there first. Electric wins when the network matures.', size=20,
        align='l', margins=(0.2, 0.1, 0.15, 0.1))
    finish(b)


# ------------------------------------------------------------------ 17
def s17(prs, n):
    b = add_base(prs, n, "The mod's idea", "The mod's track", 'Agreed',
                 'Two thin rails on sleepers, built from iron plates and rods. Speed is the lowest of three limits.')
    sh = b.shapes
    photo(sh, 'R02', MARGIN, 1.45, 5.6, 3.15)
    photo(sh, 'R05', 6.4, 1.45, 2.5, 1.875)
    label(sh, 6.4, 3.75, 2.5, 0.65, 'Close-up: chairs and rails', size=16)
    photo(sh, 'P02', 9.13, 1.45, 3.6, 2.7)
    label(sh, 9.13, 4.55, 3.6, 0.35, 'Real railway, for comparison', size=16)
    rule = 'Speed = lowest of: track limit, signal limit, engine limit'
    box(sh, MARGIN, 4.98, 12.13, 0.55, fill=C['panel'], line=C['orange'], lw=1.5, radius=0.08,
        text=rule, size=18, bold=True, align='l', margins=(0.25, 0.02, 0.1, 0.02), name='Speed rule')
    inline_chip(sh, 'Proposed', MARGIN + 0.25 + text_width_in(rule, 18, True) + 0.25, 5.075)
    label(sh, MARGIN, 5.62, 2.6, 0.36, 'Longest track piece:', size=16, anchor='m')
    inline_chip(sh, 'Undecided', MARGIN + text_width_in('Longest track piece:', 16) + 0.15, 5.62,
                text='Undecided (OQ02)')
    finish(b)


# ------------------------------------------------------------------ 18
def s18(prs, n):
    b = add_base(prs, n, 'Locomotives', 'Three roles', 'Agreed',
                 'Small, Medium and Large each have a job. Bigger is not simply better.')
    sh = b.shapes
    cards = [('Small', 0.6, (0.25, 0.35, 0.25, 0.25), 'Local branches', dict(body_w=1.5, n_wheels=3)),
             ('Medium', 4.75, (0.55, 0.80, 0.70, 0.65), 'Fast mixed freight',
              dict(body_w=1.9, n_wheels=4, tender_w=0.75)),
             ('Large', 8.9, (0.95, 0.60, 0.90, 0.90), 'Heavy freight',
              dict(body_w=2.15, n_wheels=5, tender_w=0.85))]
    for name, x, vals, duty, eng in cards:
        g = group(sh, name + ' card', '%s locomotive card. Qualitative bars: haul %s, speed %s, range %s, '
                  'servicing needs %s. Best for: %s.' % (name, *(['low', 'medium', 'high'][min(2, int(v * 3))]
                                                              for v in vals), duty.lower()))
        s = g.shapes
        box(s, x, 1.45, 3.8, 4.25, fill=C['panel'], radius=0.1)
        box(s, x, 1.75, 3.8, 0.2, fill=C['orange'])
        box(s, x, 1.45, 3.8, 0.5, fill=C['orange'], radius=0.1, text=name, size=20, bold=True,
            color=C['ink'])
        ew = eng['body_w'] + eng.get('tender_w', 0) + (0.07 if eng.get('tender_w') else 0)
        engine(s, x + (3.8 - ew) / 2, 3.0, **eng, name=name + ' engine',
               alt='Side view of the %s steam engine%s.' % (name.lower(), ' with its tender' if eng.get('tender_w') else ''))
        for k, (bl, v) in enumerate(zip(('Haul', 'Speed', 'Range', 'Servicing needs'), vals)):
            y = 3.12 + k * 0.5
            label(s, x + 0.25, y, 1.6, 0.26, bl, size=14)
            hatch = name == 'Medium' and bl == 'Speed'
            f = ('hatch', C['orange'], C['panel_alt']) if hatch else C['orange']
            box(s, x + 0.25, y + 0.26, 3.3, 0.16, fill=C['panel_alt'], radius=0.04)
            box(s, x + 0.25, y + 0.26, 3.3 * v, 0.16, fill=f, radius=0.04,
                line=C['orange'] if hatch else None, lw=1)
            if hatch:
                # same row as the "Speed" label (0.26 in), so it clears both bars
                inline_chip(s, 'Undecided', x + 3.55 - chip_w('Fastest? Undecided'), y - 0.03,
                            text='Fastest? Undecided', h=0.26)
        label(s, x + 0.25, 5.15, 3.3, 0.42, duty, size=18, bold=True, anchor='m')
    label(sh, MARGIN, 5.82, 6, 0.32, 'Shape only. Not measured.', size=14, color=C['muted'])
    finish(b)


# ------------------------------------------------------------------ 19-21 helper
def role_slide(prs, n, title, caption, slot, ref_label, rows, note=None, photo_h=3.7, focus=(0.5, 0.5)):
    b = add_base(prs, n, 'Locomotives', title, 'Agreed', caption)
    sh = b.shapes
    photo(sh, slot, MARGIN, 1.45, 5.6, photo_h, focus=focus)
    y = 1.45 + photo_h + 0.25
    if ref_label:
        label(sh, MARGIN, y, 5.6, 0.36, ref_label, size=16, color=C['text'])
    if note:
        label(sh, MARGIN, y, 5.6, 0.7, note, size=16, color=C['text'])
    g = group(sh, 'Traits', 'Traits: ' + '; '.join(r[1] for r in rows) + '.')
    yy = 1.5
    for row in rows:
        kind, text, chips = row[:3]
        below = len(row) > 3 and row[3]
        h = 1.02 if below else 0.82
        list_row(g.shapes, 6.55, yy, 6.18, h, kind, text, 20, chips, below=below)
        yy += h + 0.16
    finish(b)
    return b


def s19(prs, n):
    role_slide(prs, n, 'Small: the branch-line tank',
               'Small carries its own coal and water. It is cheap, light and best on short branches.',
               'P10', None,
               [('no_tender', 'No tender', ()), ('weight', 'Weakest hauler', ()),
                ('coin', 'Cheap to run', ()),
                ('hill', 'Struggles with long trains and hills', ('Proposed',))],
               note='A related Fowler tank engine (a Jinty). The design\'s reference, the Dock Tank, '
                    'has no survivor.', photo_h=3.6)


def s20(prs, n):
    role_slide(prs, n, 'Medium: the long-range runner',
               'Medium has a tender and more range. It uses more coal and water. It may be the fastest class.',
               'P11', 'Reference: Merchant Navy class',
               [('tender', 'Normal tender: more coal and water', ()), ('flame', 'Burns more', ()),
                ('aux_tender', 'Auxiliary tender: a practical extra', ()),
                ('speed', 'Fastest class', ('Proposed', ('Undecided', 'Undecided (OQ05)')), True)],
               photo_h=3.45)


SLIDES = [s11, s12, s13, s14, s15, s16, s17, s18, s19, s20]
