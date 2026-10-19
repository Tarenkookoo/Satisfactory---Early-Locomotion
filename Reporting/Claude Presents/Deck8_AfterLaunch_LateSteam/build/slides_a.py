"""Slides 1 to 9."""
from lib import *


def diagram(S, name, descr):
    g = group(S, name, descr)
    return g.shapes


# ------------------------------------------------------------------ 1 title
def s01(prs):
    s = prs.slides.add_slide(prs.slide_layouts[5])
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = rgb('bg')
    t = s.shapes.title
    t.left, t.top, t.width, t.height = I(0.6), I(1.2), I(7.3), I(2.95)
    put_text(t, 'After Launch:\vLate Steam, Driving\vand Prestige', size=54, bold=True,
             anchor='t', margin=(0, 0, 0, 0))
    t.name = 'Title'
    rect(s.shapes, 0.6, 4.3, 1.8, 0.07, 'orange', None, name='Orange rule')
    tbox(s.shapes, 0.6, 4.6, 6.7, 1.1,
         'Ideas for after the first release, for people who love steam. All of it comes later.',
         size=20, anchor='t', margin=(0, 0, 0, 0), name='Caption')
    picture(s.shapes, 'P12_9f_92203.jpg', 8.1, 0.45, 4.63, 6.35,
            'A large black British steam locomotive seen from the front three-quarter, '
            'standing on a heritage railway.', focus=(0.82, 0.5))
    credit(s.shapes, 8.1, 6.88, 4.63,
           'A real steam locomotive, shown for illustration.\vPhoto: Tony Hisgett, CC BY 2.0.',
           h=0.4)


# ------------------------------------------------------------------ 2 legend
def s02(prs):
    s = base_slide(prs, 2, 'How to read this guide')
    S = s.shapes
    G = diagram(S, 'Diagram: tag legend', 'Five tags with their meanings: Agreed, Proposed, '
                'Provisional, Undecided and Background.')
    rows = [('Agreed', 'Decided.'), ('Proposed', 'Suggested, not confirmed.'),
            ('Provisional', 'A test number that may change.'), ('Undecided', 'Still an open question.'),
            ('Background', 'A real-world fact.')]
    y = 1.5
    for st, meaning in rows:
        panel(G, 0.6, y, 7.7, 0.76, 'panel')
        spec = CHIPS[st]
        c = shape(G, MSO_SHAPE.ROUNDED_RECTANGLE, 0.85, y + 0.13, 2.0, 0.5, spec['fill'], spec['line'],
                  lw=2, radius=0.14, name='Legend chip')
        put_text(c, st.upper(), size=16, bold=True, color=spec['text'], align='c', wrap=False,
                 margin=(0.04, 0.02, 0.04, 0.02))
        tbox(G, 3.15, y + 0.1, 5.0, 0.56, meaning, size=20, anchor='m', margin=(0, 0, 0, 0))
        y += 0.9
    # decorative sketch: a slide with a tag in its top-right corner
    Gs = diagram(S, 'Sketch: a slide with a tag in its corner',
                 'Sketch of a slide with a coloured tag in its top-right corner.')
    rrect(Gs, 8.9, 1.9, 3.83, 2.35, 'panel', 'line', lw=2, radius=0.1)
    rrect(Gs, 11.2, 2.05, 1.35, 0.3, 'green', None, radius=0.1)
    rect(Gs, 9.15, 2.1, 1.6, 0.18, 'text', None)
    rect(Gs, 9.15, 2.7, 3.3, 0.12, 'line', None)
    rect(Gs, 9.15, 2.95, 2.6, 0.12, 'line', None)
    rect(Gs, 9.15, 3.2, 3.0, 0.12, 'line', None)
    rect(Gs, 9.15, 3.45, 1.9, 0.12, 'line', None)
    rrect(Gs, 9.15, 3.75, 3.3, 0.3, 'panel_alt', None, radius=0.06)
    rect(Gs, 9.15, 3.75, 0.06, 0.3, 'orange', None)
    add_caption(s, 2, 'Every idea carries a tag in the top-right corner.')


# ------------------------------------------------------------------ 3 electric still wins
def s03(prs):
    s = base_slide(prs, 3, 'Electric still wins', 'Agreed')
    S = s.shapes
    G = diagram(S, 'Diagram: steam and electric compared',
                'Paired bars show electric rail ahead of steam on speed, throughput, traffic density '
                'and convenience. The bars show shape only.')
    rows = [('Speed', 0.45, 0.90), ('Throughput', 0.40, 0.90), ('Traffic density', 0.35, 0.90),
            ('Convenience', 0.45, 0.90)]
    x0, L = 3.9, 7.8
    y = 1.55
    for name, st, el in rows:
        tbox(G, 0.6, y, 3.1, 0.9, name, size=20, bold=True, anchor='m', margin=(0, 0, 0, 0))
        for k, (frac, col) in enumerate(((st, 'orange'), (el, 'electric'))):
            by = y + 0.06 + k * 0.44
            rrect(G, x0, by, L, 0.36, 'panel', None, radius=0.1)
            rrect(G, x0, by, L * frac, 0.36, col, None, radius=0.1)
        y += 1.0
    # legend and note
    rrect(G, 3.9, 5.72, 0.3, 0.26, 'orange', None, radius=0.06)
    tbox(G, 4.3, 5.64, 1.3, 0.42, 'Steam', size=18, anchor='m', margin=(0, 0, 0, 0))
    rrect(G, 5.7, 5.72, 0.3, 0.26, 'electric', None, radius=0.06)
    tbox(G, 6.1, 5.64, 1.5, 0.42, 'Electric', size=18, anchor='m', margin=(0, 0, 0, 0))
    tbox(G, 8.4, 5.64, 3.3, 0.42, 'Shape only. Not measured.', size=14, color='muted', align='r',
         anchor='m', margin=(0, 0, 0, 0), italic=True)
    add_caption(s, 3, 'Even with packs, electric rail stays the better railway. '
                      'Steam is a choice, not an upgrade.')


# ------------------------------------------------------------------ 4 scale
def s04(prs):
    s = base_slide(prs, 4, "Steam's strength: scale", 'Agreed')
    S = s.shapes
    G = diagram(S, 'Diagram: late steam terminal beside an electric station',
                'Top-down plan of a large steam terminal with six tracks, platforms and many trains, '
                'next to a small compact electric station.')
    panel(G, 0.6, 1.45, 8.6, 4.65, 'panel')
    tbox(G, 0.85, 1.55, 5.0, 0.4, 'Late steam terminal', size=18, bold=True, color='orange',
         anchor='m', margin=(0, 0, 0, 0))
    ys = [2.55, 3.1, 3.65, 4.2, 4.75, 5.3]
    mid = (ys[0] + ys[-1]) / 2
    top_track(G, 0.8, 2.5, mid)
    for y in ys:
        line(G, 2.5, mid, 3.4, y, 'steel', 3)
        top_track(G, 3.4, 8.25, y)
        rect(G, 8.25, y - 0.12, 0.08, 0.24, 'red', None)           # buffer stop
    rect(G, 8.45, 2.3, 0.55, 3.25, 'panel_alt', 'steel', lw=1.5)    # terminal building
    for py in (2.825, 3.925, 5.025):
        rect(G, 4.4, py - 0.11, 3.6, 0.22, 'panel_alt', 'steel', lw=1.0)
    for ti, tx, n in ((0, 4.5, 3), (1, 5.8, 2), (2, 6.7, 0), (3, 4.2, 4), (4, 6.4, 1), (5, 4.9, 2)):
        top_train(G, tx, ys[ti], n=n)
    rect(G, 0.9, 2.35, 1.5, 0.75, 'panel_alt', 'steel', lw=1.5)     # depot
    circle(G, 1.65, 5.15, 1.2, 'panel_alt', 'steel', lw=1.5)        # turntable
    line(G, 1.05, 5.15, 2.25, 5.15, 'steel', 3)
    circle(G, 1.65, 5.15, 0.2, 'steel')
    # compact electric station
    panel(G, 9.5, 1.45, 3.23, 4.65, 'panel')
    tbox(G, 9.7, 1.55, 2.9, 0.4, 'Electric station', size=18, bold=True, color='electric',
         anchor='m', margin=(0, 0, 0, 0))
    rrect(G, 9.8, 3.93, 2.6, 0.1, 'electric', None, radius=0.05)
    for px in (10.1, 11.0, 12.0):
        rect(G, px, 4.03, 0.1, 0.35, 'steel', None)
    rrect(G, 10.45, 3.45, 1.15, 0.38, 'electric', 'coal', lw=1.0, radius=0.1)
    for wx in (10.6, 10.95, 11.3):
        rect(G, wx, 3.52, 0.2, 0.14, 'coal', None)
    rect(G, 10.35, 4.45, 1.5, 0.22, 'panel_alt', 'steel', lw=1.0)
    rect(G, 10.55, 4.78, 1.1, 0.5, 'panel_alt', 'steel', lw=1.5)
    add_caption(s, 4, 'Late steam is about scale: big terminals, many tracks, busy yards.')


# ------------------------------------------------------------------ 5 for people who love steam
def s05(prs):
    s = base_slide(prs, 5, 'For people who love steam', 'Agreed')
    S = s.shapes
    G = diagram(S, 'Diagram: core buildings beside locked pack buildings',
                'A split panel: small basic buildings in the core game on the left, and larger advanced '
                'buildings behind a padlock on the right, marked as needing a pack.')
    panel(G, 0.6, 1.45, 5.95, 4.65, 'panel')
    panel(G, 6.78, 1.45, 5.95, 4.65, 'panel')
    d = -0.55   # lift the scene so the label sits clear of the tracks
    gy = 5.0 + d
    # core: small station
    rect(G, 0.8, gy, 5.55, 0.1, 'sleeper', None)
    top_track(G, 0.8, 6.35, gy + 0.5)
    rect(G, 1.2, 4.55 + d, 2.6, 0.2, 'panel_alt', 'steel', lw=1.0)         # platform
    rect(G, 1.5, 3.6 + d, 1.2, 0.95, 'panel_alt', 'steel', lw=1.5)         # small signal box
    tri(G, 1.4, 3.2 + d, 1.4, 0.4, 'sleeper', None)
    rect(G, 1.8, 3.95 + d, 0.35, 0.3, 'coal', None)
    rrect(G, 4.2, 3.0 + d, 0.95, 0.6, 'water', 'white', lw=1.5, radius=0.1)  # small water tank
    for lx in (4.3, 4.95):
        rect(G, lx, 3.6 + d, 0.08, 1.4, 'steel', None)
    # pack: large terminal complex
    rect(G, 7.0, gy, 5.55, 0.1, 'sleeper', None)
    for ty in (gy + 0.4, gy + 0.65):
        top_track(G, 7.0, 12.55, ty)
    rect(G, 7.25, 4.45 + d, 4.0, 0.25, 'panel_alt', 'steel', lw=1.0)       # long platform
    rect(G, 7.4, 3.3 + d, 2.7, 1.15, 'panel_alt', 'steel', lw=1.5)         # large hall
    tri(G, 7.3, 2.65 + d, 2.9, 0.65, 'sleeper', None)
    for wx in (7.7, 8.4, 9.1):
        rect(G, wx, 3.65 + d, 0.35, 0.5, 'coal', None)
    rect(G, 10.3, 3.35 + d, 0.95, 1.1, 'panel_alt', 'steel', lw=1.5)       # big signal box
    tri(G, 10.2, 3.0 + d, 1.15, 0.35, 'sleeper', None)
    rrect(G, 11.55, 2.55 + d, 1.0, 0.85, 'water', 'white', lw=1.5, radius=0.1)  # tall water tank
    for lx in (11.62, 12.38):
        rect(G, lx, 3.4 + d, 0.08, 1.6, 'steel', None)
    # veil, padlock, then headings and label on top
    rrect(G, 6.78, 1.45, 5.95, 4.65, 'bg', None, radius=0.08, fill_alpha=0.62)
    padlock(G, 9.75, 3.45, 1.15)
    pill(G, 8.45, 5.35, 2.6, 0.5, 'Needs a pack', fill='panel', line='amber', lw=2, size=18, bold=True,
         align='c')
    tbox(G, 0.85, 1.55, 5.4, 0.45, 'Core: basic buildings', size=20, bold=True, anchor='m',
         margin=(0, 0, 0, 0))
    tbox(G, 7.03, 1.55, 5.4, 0.45, 'Pack: advanced buildings', size=20, bold=True, color='orange',
         anchor='m', margin=(0, 0, 0, 0))
    add_caption(s, 5, 'Advanced steam buildings come only with packs. '
                      'They are for people who keep steam on purpose.')


# ------------------------------------------------------------------ 6 bigger buildings
def s06(prs):
    s = base_slide(prs, 6, 'Bigger buildings', 'Proposed')
    S = s.shapes
    G = diagram(S, 'Diagram: a smaller and a bigger terminal',
                'Top-down plans of a smaller terminal with one platform and a bigger terminal with extra '
                'platforms and a larger service yard.')
    panel(G, 0.6, 1.45, 4.3, 4.1, 'panel')
    panel(G, 5.1, 1.45, 7.63, 4.1, 'panel')
    tbox(G, 0.85, 1.55, 3.8, 0.4, 'Smaller terminal', size=18, bold=True, anchor='m', margin=(0, 0, 0, 0))
    tbox(G, 5.35, 1.55, 4.8, 0.4, 'Bigger terminal', size=18, bold=True, color='orange', anchor='m',
         margin=(0, 0, 0, 0))
    # small
    for y in (3.0, 3.5):
        top_track(G, 0.8, 4.7, y)
    rect(G, 1.5, 3.14, 2.8, 0.22, 'panel_alt', 'steel', lw=1.0)
    top_train(G, 1.6, 3.5, n=1)
    rrect(G, 0.8, 4.2, 3.9, 1.1, None, 'steel', lw=1.5, radius=0.1, dash=MSO_LINE.DASH)
    top_track(G, 0.95, 3.6, 4.6)
    circle(G, 4.1, 4.75, 0.5, 'water', 'white', lw=1.5)
    # big
    ys = [2.35, 2.85, 3.35, 3.85]
    for y in ys:
        top_track(G, 5.35, 10.6, y)
    for py in (2.6, 3.1, 3.6):
        rect(G, 5.9, py - 0.11, 4.2, 0.22, 'panel_alt', 'steel', lw=1.0)
    top_train(G, 6.0, ys[0], n=3)
    top_train(G, 6.8, ys[2], n=2)
    top_train(G, 5.6, ys[3], n=4)
    rrect(G, 5.3, 2.15, 5.4, 2.0, None, 'orange', lw=1.5, radius=0.1, dash=MSO_LINE.DASH)
    tbox(G, 10.8, 2.7, 1.8, 0.7, 'Extra\vplatforms', size=14, bold=True, color='orange', anchor='m',
         margin=(0, 0, 0, 0))
    rrect(G, 5.3, 4.3, 5.4, 1.1, None, 'steel', lw=1.5, radius=0.1, dash=MSO_LINE.DASH)
    for y in (4.5, 4.8, 5.1):
        top_track(G, 5.45, 9.4, y)
    circle(G, 9.9, 4.65, 0.5, 'water', 'white', lw=1.5)
    rect(G, 10.0, 4.95, 0.5, 0.3, 'coal', 'steel', lw=1.0)
    tbox(G, 10.8, 4.4, 1.85, 0.9, 'Larger service\vyard', size=14, bold=True, anchor='m',
         margin=(0, 0, 0, 0))
    # chip row
    _chip, _w = inline_chip(S, 0.0, 5.7, 'Undecided', 'Exact list: undecided (OQ22)', prefix=False)
    _chip.left = I(12.73 - _w)
    add_caption(s, 6, 'Bigger terminals and faster servicing could appear.')


# ------------------------------------------------------------------ 7 bigger signalling
def s07(prs):
    s = base_slide(prs, 7, 'Bigger signalling', 'Proposed')
    S = s.shapes
    G = diagram(S, 'Diagram: small and large signal box reach',
                'A small signal box with a short reach ring and three signal posts, and a large signal '
                'box with a wide reach ring and six signal posts.')
    panel(G, 0.6, 1.45, 4.7, 4.65, 'panel')
    panel(G, 5.5, 1.45, 7.23, 4.65, 'panel')
    tbox(G, 0.85, 1.52, 4.3, 0.8, [[('Small signal box', dict(size=18, bold=True))],
                                   [('Short reach', dict(size=14, bold=True, color='steel'))]],
         anchor='t', margin=(0, 0, 0, 0))
    tbox(G, 5.75, 1.52, 6.0, 0.8, [[('Large signal box', dict(size=18, bold=True, color='orange'))],
                                   [('Wide reach', dict(size=14, bold=True, color='orange'))]],
         anchor='t', margin=(0, 0, 0, 0))
    ty = 4.8
    for cx, cy, R, posts, col, t1, t2 in (
            (2.95, 4.1, 1.3, [2.2, 2.9, 3.6], 'steel', 0.8, 5.1),
            (9.1, 4.2, 1.8, [7.55, 8.1, 8.65, 9.2, 9.75, 10.3], 'orange', 5.7, 12.5)):
        circle(G, cx, cy, 2 * R, col, col, lw=2, dash=MSO_LINE.DASH, fill_alpha=0.14)
        top_track(G, t1, t2, ty)
        rect(G, cx - 0.4, 3.4, 0.8, 0.55, 'panel_alt', 'white', lw=1.5)
        tri(G, cx - 0.5, 3.1, 1.0, 0.3, 'sleeper', None)
        for px in posts:
            semaphore(G, px, ty - 0.82, h=0.72, state='stop', scale=0.6, lamp=False)
    add_caption(s, 7, 'Bigger signal boxes and better interlocking could manage larger networks.')


# ------------------------------------------------------------------ 8 a line that stays
def s08(prs):
    s = base_slide(prs, 8, 'A line that stays', 'Agreed')
    S = s.shapes
    G = diagram(S, 'Diagram: semaphore post and crossed-out electronic powers',
                'A tall semaphore signal post beside a card reading Electronic-signal powers, crossed out '
                'with a red cross.')
    rect(G, 2.2, 5.62, 2.6, 0.12, 'sleeper', None)
    semaphore(G, 3.5, 1.7, h=3.95, state='stop', scale=3.5)
    # card with lightning bolt
    rrect(G, 6.0, 2.7, 6.2, 1.9, 'panel_alt', 'electric', lw=3, radius=0.1)
    poly(G, [(6.6, 3.0), (7.35, 3.0), (7.0, 3.5), (7.6, 3.5), (6.75, 4.35), (6.95, 3.75), (6.4, 3.75)],
         fill='electric', line_c=None)
    cross_over(G, 6.0, 2.7, 6.2, 1.9, lw=5, alpha=0.75)
    tbox(G, 7.8, 2.85, 4.2, 1.6, 'Electronic-signal powers', size=24, bold=True, anchor='m',
         margin=(0, 0, 0, 0))
    add_caption(s, 8, "Late steam must not simply copy electric rail's abilities.")


# ------------------------------------------------------------------ 9 two ways to drive
def s09(prs):
    s = base_slide(prs, 9, 'Two ways to drive', 'Agreed')
    S = s.shapes
    G = diagram(S, 'Diagram: simple and advanced driver cards',
                'Two driver cards. Simple shows one lever because the crew handles the details. '
                'Advanced shows three levers because you handle the engine, and is for packs only.')
    panel(G, 0.6, 1.45, 5.95, 4.65, 'panel')
    panel(G, 6.78, 1.45, 5.95, 4.65, 'panel')
    tbox(G, 0.85, 1.6, 5.45, 0.9, [[('Simple:', dict(bold=True, color='orange')),
                                    (' the crew handles the details', {})]], size=20, anchor='t',
         margin=(0, 0, 0, 0))
    tbox(G, 7.03, 1.6, 5.45, 0.9, [[('Advanced:', dict(bold=True, color='orange')),
                                    (' you handle the engine', {})]], size=20, anchor='t',
         margin=(0, 0, 0, 0))
    lever(G, 3.575, 2.55, 3.0, w=1.0)
    for cx in (8.4, 9.755, 11.1):
        lever(G, cx, 2.65, 2.4, w=0.85)
    pill(G, 8.45, 5.38, 2.6, 0.5, 'Advanced: packs only', fill='amber', size=16, bold=True, color='dark',
         align='c', wrap=False)
    add_caption(s, 9, 'Simple is the default. Advanced driving is optional and comes with packs.')


def build(prs):
    for f in (s01, s02, s03, s04, s05, s06, s07, s08, s09):
        f(prs)
