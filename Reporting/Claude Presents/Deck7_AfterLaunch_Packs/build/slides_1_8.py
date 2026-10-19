"""Chunk 1: slides 1 to 8."""
import os
from el_lib import *
import el_lib as L


# ------------------------------------------------------------------ 1 title
def s01(prs):
    s = new_slide(prs, 'After Launch: Packs, Locomotives and History', 1, chip=None)
    t = s.shapes.title
    t.left, t.top, t.width, t.height = Inches(0.6), Inches(0.35), Inches(6.5), Inches(3.8)
    put_text(t, 'After Launch: Packs, Locomotives and History', size=54, bold=True, color=TEXT,
             align='l', anchor='b', inset=(0, 0, 0, 0))
    name_it(t, 'Title')
    S = s.shapes
    rect(S, 0.6, 4.35, 2.4, 0.07, fill=ORANGE)
    label(S, 0.6, 4.65, 6.3, 1.0, 'How the mod could grow after the first release. All of it comes later.',
          size=20, color=TEXT, anchor='t', name='Caption')
    img = os.path.join(L.IMG_DIR, 'P19_west_country_34007.jpg')
    picture(S, img, 7.4, 0.5, 5.33, 6.35,
            'A real British steam locomotive, seen from the front and side, trailing smoke beside a '
            'semaphore signal. A photograph for illustration only.', focus=0.80, name='Photo: real locomotive')
    credit(S, 7.4, 6.95, 5.33, 'A real locomotive, for illustration. Photo: Ben Salter, CC BY 2.0.')
    return s


# ------------------------------------------------------------------ 2 legend
def s02(prs):
    s = new_slide(prs, 'How to read this guide', 2, chip=None)
    S = s.shapes
    rows = [('Agreed', 'Decided.'), ('Proposed', 'Suggested, not confirmed.'),
            ('Provisional', 'A test number that may change.'), ('Undecided', 'Still an open question.'),
            ('Background', 'A real-world fact.')]
    for i, (st, meaning) in enumerate(rows):
        y = 1.55 + i * 0.9
        rect(S, 0.6, y, 12.13, 0.72, fill=PANEL, radius=0.08)
        fill, tc, outline = STATUS_STYLE[st]
        chip = rect(S, 0.9, y + 0.16, 1.5, 0.4, fill=fill, line=outline, lw=2, radius=0.1)
        put_text(chip, st.upper(), size=14, bold=True, color=tc, align='c', anchor='m', inset=(0, 0, 0, 0), wrap=False)
        name_it(chip, 'Legend chip: ' + st)
        label(S, 2.85, y, 9.5, 0.72, meaning, size=20, color=TEXT, name='Legend meaning: ' + st)
    caption(s, 'Every idea carries a tag in the top-right corner.')
    slide_number(s)
    return s


# ------------------------------------------------------------------ 3 core first
def s03(prs):
    s = new_slide(prs, 'Core comes first', 3, chip='Agreed')
    g = group(s, 'Later packs (dashed blocks)', 'Three dashed blocks labelled Later packs float above the core block, '
              'not touching it: packs come later.')
    for x, y, w, h in ((1.55, 1.75, 3.1, 1.15), (5.1, 1.55, 3.1, 1.15), (8.65, 1.95, 3.1, 1.15)):
        boxed(g.shapes, x, y, w, h, 'Later packs', size=20, fill=ORANGE, alpha=14, line=ORANGE, lw=2,
              dash=DASH, bold=True, radius=0.1)
    g2 = group(s, 'Core block (solid)', 'A tall solid orange block labelled Core 1.0: complete, standing at the bottom.')
    boxed(g2.shapes, 2.85, 3.95, 7.6, 2.15, 'Core 1.0: complete', size=32, fill=ORANGE, color=INK, bold=True, radius=0.1)
    caption(s, 'The core game is finished first. Nothing is held back to sell packs.')
    slide_number(s)
    return s


# ------------------------------------------------------------------ 4 one shared engine
def s04(prs):
    s = new_slide(prs, 'One shared engine', 4, chip='Agreed')
    u = 1.7
    base_y = 5.1
    top_y = base_y - u
    bar = group(s, 'Shared rules bar', 'A long bar labelled Shared rules. Both engines stand on it.')
    boxed(bar.shapes, 0.9, base_y, 11.53, 0.8, 'Shared rules', size=22, bold=True, fill=PANEL_ALT, line=ORANGE, lw=2, radius=0.08)
    specs = (
        ('Core engine', 1.4, dict(n_wheels=3, boiler=1.15, tank=True), False,
         'A Core engine, a small tank engine, with its own data card.'),
        ('Pack engine', 6.6, dict(n_wheels=4, boiler=1.25, tender=0.95), True,
         'A Pack engine, a larger engine with a tender, with its own data card (dashed because packs come later).'),
    )
    for lab, x0, kw, later, alt in specs:
        g = group(s, lab + ' and data card', alt)
        gs = g.shapes
        engine(gs, x0, top_y, u, dashed=later, outline=ORANGE if later else None, **kw)
        geo = engine_geom(x0, u, boiler=kw['boiler'], tender=kw.get('tender', 0.0))
        cx = geo['boil_x0'] + 0.62 * kw['boiler'] * u
        label(gs, x0, top_y - 0.5, cx - x0 - 0.2, 0.38, lab, size=16, bold=True, anchor='m')
        card_w = 2.3
        cx0 = cx - card_w / 2
        rect(gs, cx0, 1.65, card_w, 1.15, fill=PANEL, line=ORANGE if later else STEEL, lw=1.75, radius=0.08,
             dash=DASH if later else None)
        label(gs, cx0 + 0.15, 1.7, card_w - 0.3, 0.36, 'Data card', size=14, bold=True)
        for i, bw in enumerate((1.7, 1.3, 1.5)):
            rect(gs, cx0 + 0.15, 2.17 + i * 0.2, bw, 0.1, fill=MUTED, radius=0.05)
        line(gs, cx, 2.8, cx, top_y + 0.24 * u, color=ORANGE, lw=2.25)
    caption(s, 'Packs add new engines, not new physics. Everything runs on the same rules.')
    slide_number(s)
    return s


# ------------------------------------------------------------------ 5 packs by region
def _icon_engine(S, x, y):
    engine(S, x, y, 0.42, n_wheels=2, boiler=0.8, simple=True, body=STEEL)


def _icon_building(S, x, y):
    rect(S, x + 0.05, y + 0.18, 0.5, 0.26, fill=STEEL)
    poly(S, [(x, y + 0.18), (x + 0.3, y), (x + 0.6, y + 0.18)], fill=STEEL)
    rect(S, x + 0.25, y + 0.28, 0.1, 0.16, fill=PANEL)


def _icon_book(S, x, y):
    rect(S, x + 0.04, y, 0.52, 0.42, fill=STEEL, radius=0.03)
    rect(S, x + 0.28, y, 0.04, 0.42, fill=PANEL)
    for i in range(2):
        rect(S, x + 0.1, y + 0.1 + i * 0.12, 0.14, 0.04, fill=PANEL)
        rect(S, x + 0.36, y + 0.1 + i * 0.12, 0.14, 0.04, fill=PANEL)


def s05(prs):
    s = new_slide(prs, 'Packs by region', 5, chip='Proposed')
    w, gap, x0, y0 = 3.6, 0.45, 0.82, 1.6
    for i, nm in enumerate(('Region A pack', 'Region B pack', 'Region C pack')):
        x = x0 + i * (w + gap)
        g = group(s, nm, nm + ': a dashed box listing Engines, Buildings and History. Packs come after launch.')
        gs = g.shapes
        rect(gs, x, y0, w, 3.5, fill=PANEL, line=ORANGE, lw=2, dash=DASH, radius=0.08)
        boxed(gs, x - 0.06, y0, w + 0.12, 0.7, nm, size=20, bold=True, fill=ORANGE, color=INK, radius=0.08)
        for j, (txt, icon) in enumerate((('Engines', _icon_engine), ('Buildings', _icon_building), ('History', _icon_book))):
            ry = y0 + 0.95 + j * 0.82
            icon(gs, x + 0.45, ry + 0.08)
            label(gs, x + 1.35, ry, w - 1.6, 0.58, txt, size=18, bold=True)
            if j < 2:
                line(gs, x + 0.4, ry + 0.7, x + w - 0.4, ry + 0.7, color=LINE, lw=1)
    cy = 5.55
    c1, w1 = inline_chip(s.shapes, 0.82, cy, 'Undecided', 'Pack names: undecided (OQ20)')
    c2, w2 = inline_chip(s.shapes, 0.82 + w1 + 0.3, cy, 'Undecided', 'Price: undecided (OQ26)')
    caption(s, 'Separate regional packs could add fleets, buildings and history.')
    slide_number(s)
    return s


# ------------------------------------------------------------------ 6 growing by updates
def s06(prs):
    s = new_slide(prs, 'Growing by updates', 6, chip='Proposed')
    g = group(s, 'Staircase of updates', 'A staircase of three dashed blocks rising left to right: Launch (small), '
              'then Update, then a bigger Update.')
    bottom = 5.35
    for i, (txt, h, al) in enumerate((('Launch', 1.3, 14), ('Update', 2.4, 24), ('Update', 3.5, 34))):
        x = 0.9 + i * 2.85
        boxed(g.shapes, x, bottom - h, 2.7, h, txt, size=22, bold=True, fill=ORANGE, alpha=al, line=ORANGE, lw=2,
              dash=DASH, anchor='t', inset=(0.1, 0.18, 0.1, 0.05), radius=0.08)
    n = group(s, 'No charge note', 'A price tag crossed out, with the note: no charge per locomotive.')
    ns = n.shapes
    rect(ns, 9.8, 2.2, 2.93, 2.4, fill=PANEL, radius=0.08)
    poly(ns, [(10.78, 2.9), (11.05, 2.55), (11.75, 2.55), (11.75, 3.25), (11.05, 3.25)], fill=None, line=STEEL, lw=2)
    oval(ns, 10.95, 2.76, 0.12, 0.12, fill=STEEL)
    line(ns, 10.7, 3.35, 11.85, 2.45, color=RED, lw=3)
    label(ns, 9.95, 3.5, 2.63, 0.95, 'No charge per locomotive.', size=18, bold=True, align='c', anchor='m')
    inline_chip(s.shapes, 0.9, 5.6, 'Undecided', 'Early-access pricing: undecided (OQ26)')
    caption(s, 'A pack could start small and grow through updates, free to its owners.')
    slide_number(s)
    return s


# ------------------------------------------------------------------ 7 packs work together
def s07(prs):
    s = new_slide(prs, 'Packs work together', 7, chip='Agreed')
    bar_y = 5.15
    g0 = group(s, 'Shared rules bar', 'A long bar labelled Shared rules beneath the core game and all three packs.')
    boxed(g0.shapes, 0.9, bar_y, 11.53, 0.75, 'Shared rules', size=22, bold=True, fill=PANEL_ALT, line=ORANGE, lw=2, radius=0.08)
    g1 = group(s, 'Core game hub and packs', 'A central block labelled Core game with three dashed Pack blocks '
               'plugged into it: left, right and above.')
    gs = g1.shapes
    hub = (5.07, 2.95, 3.2, 1.4)
    # ties to the bar
    for tx in (2.3, 6.67, 11.03):
        line(gs, tx, 4.35, tx, bar_y, color=STEEL, lw=1.5, dash=DASH)
    packs = ((0.9, 2.95, 2.8, 1.4), (9.63, 2.95, 2.8, 1.4), (5.07, 1.65, 3.2, 0.8))
    for (x, y, w, h) in packs:
        boxed(gs, x, y, w, h, 'Pack', size=20, bold=True, fill=ORANGE, alpha=14, line=ORANGE, lw=2, dash=DASH, radius=0.08)
    boxed(gs, *hub, 'Core game', size=24, bold=True, fill=ORANGE, color=INK, radius=0.1)
    # plugs: line with a round plug at each end
    for (x1, y1, x2, y2) in ((3.7, 3.65, 5.07, 3.65), (9.63, 3.65, 8.27, 3.65), (6.67, 2.45, 6.67, 2.95)):
        line(gs, x1, y1, x2, y2, color=TEXT, lw=2.25)
        for (px, py) in ((x1, y1), (x2, y2)):
            oval(gs, px - 0.09, py - 0.09, 0.18, 0.18, fill=TEXT)
    caption(s, 'Packs need the core game and can be mixed. They share the same rules.')
    slide_number(s)
    return s


# ------------------------------------------------------------------ 8 beyond S/M/L
def s08(prs):
    s = new_slide(prs, 'Beyond Small, Medium, Large', 8, chip='Agreed')
    g = group(s, 'Small, Medium and Large cards', 'Three cards, Small, Medium and Large, each with a small engine '
              'icon that grows with the size.')
    gs = g.shapes
    specs = (('Small', dict(n_wheels=3, boiler=0.9, tank=True), 0.5),
             ('Medium', dict(n_wheels=4, boiler=1.0, tender=0.9), 0.55),
             ('Large', dict(n_wheels=5, boiler=1.2, tender=1.0), 0.62))
    for i, (nm, kw, u) in enumerate(specs):
        y = 1.7 + i * 1.3
        rect(gs, 0.9, y, 3.6, 1.1, fill=PANEL, line=STEEL, lw=1.5, radius=0.08)
        label(gs, 1.15, y, 1.4, 1.1, nm, size=20, bold=True)
        gw = engine_geom(0, u, boiler=kw['boiler'], tender=kw.get('tender', 0.0))['width']
        engine(gs, 4.3 - gw, y + 0.55 - u / 2, u, **kw)
    ar = rect(s.shapes, 4.85, 3.2, 1.2, 0.8, fill=ORANGE, shape=MSO_SHAPE.RIGHT_ARROW)
    set_alt(ar, 'An arrow pointing from the three size cards to the job categories.', 'Arrow')
    label(s.shapes, 6.45, 1.55, 6.2, 0.35, 'Candidate names only', size=14, italic=True, color=MUTED, name='Note: candidate names')
    sh = group(s, 'Shelf of four categories', 'A two-shelf rack holding four category chips: Shunters, Mixed Traffic, '
               'Fast Freight and Heavy Freight. These are candidate names only.')
    ss = sh.shapes
    rect(ss, 6.45, 2.0, 6.28, 3.2, fill=PANEL, line=LINE, lw=1.5, radius=0.08)
    names = (('Shunters', 0, 0), ('Mixed Traffic', 1, 0), ('Fast Freight', 0, 1), ('Heavy Freight', 1, 1))
    for nm, cx, cy in names:
        x = 6.75 + cx * 3.0
        y = 2.3 + cy * 1.45
        boxed(ss, x, y, 2.75, 0.8, nm, size=18, bold=True, fill=PANEL_ALT, line=ORANGE, lw=2, radius=0.4)
        rect(ss, 6.65, y + 0.95, 5.88, 0.12, fill=SLEEPER)
    inline_chip(s.shapes, 6.45, 5.45, 'Undecided', 'Names: undecided (OQ20)')
    caption(s, 'With many engines, you browse by job instead of only by size.')
    slide_number(s)
    return s


BUILDERS = [s01, s02, s03, s04, s05, s06, s07, s08]
