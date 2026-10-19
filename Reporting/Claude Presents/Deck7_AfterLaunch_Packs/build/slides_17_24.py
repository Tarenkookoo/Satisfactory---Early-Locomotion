"""Chunk 3: slides 17 to 24."""
import os
from el_lib import *
import el_lib as L


# ------------------------------------------------------------------ 17 where do the unlocks live
def milestone_box(gs, x, y, w, h=0.55, dashed=False, tag=False, tag_w=0.95):
    rect(gs, x, y, w, h, fill=PANEL_ALT, line=STEEL, lw=1.5, radius=0.06)
    rect(gs, x + 0.15, y + h / 2 - 0.05, w * 0.35, 0.1, fill=MUTED, radius=0.05)
    if tag:
        rect(gs, x + w - tag_w - 0.12, y + 0.1, tag_w, h - 0.2, fill=ORANGE, alpha=22, line=ORANGE, lw=1.5, dash=DASH, radius=0.05)


def s17(prs):
    s = new_slide(prs, 'Where do the unlocks live?', 17, chip='Proposed')
    S = s.shapes
    cards = ((0.9, 'Inside existing milestones'), (6.83, 'Separate labelled milestones'))
    for i, (x, title) in enumerate(cards):
        g = group(s, 'Option: ' + title, 'Option ' + ('one' if i == 0 else 'two') + ': ' + title + '. ' +
                  ('Pack unlock tags sit inside the normal Core milestone boxes.' if i == 0 else
                   'Core milestones stay as they are, and a separate dashed column of milestones is labelled Pack.'))
        gs = g.shapes
        rect(gs, x, 1.55, 5.6, 3.45, fill=PANEL, line=LINE, lw=1.5, radius=0.08)
        label(gs, x + 0.3, 1.7, 5.0, 0.5, title, size=20, bold=True)
        if i == 0:
            for j in range(3):
                milestone_box(gs, x + 0.45, 2.45 + j * 0.8, 4.7, tag=True)
        else:
            for j in range(3):
                milestone_box(gs, x + 0.35, 2.45 + j * 0.8, 2.3)
            rect(gs, x + 2.95, 2.35, 2.3, 2.45, fill=None, line=ORANGE, lw=2, dash=DASH, radius=0.08)
            label(gs, x + 3.1, 2.4, 2.0, 0.34, 'Pack', size=14, bold=True, color=ORANGE)
            for j in range(3):
                rect(gs, x + 3.1, 2.8 + j * 0.65, 2.0, 0.5, fill=ORANGE, alpha=22, line=ORANGE, lw=1.5, dash=DASH, radius=0.05)
    lg = group(s, 'Legend', 'Key: a solid box is a Core milestone and a dashed box is a Pack unlock.')
    rect(lg.shapes, 0.9, 5.18, 0.45, 0.28, fill=PANEL_ALT, line=STEEL, lw=1.5, radius=0.04)
    label(lg.shapes, 1.45, 5.14, 0.9, 0.36, 'Core', size=14, bold=True)
    rect(lg.shapes, 2.5, 5.18, 0.45, 0.28, fill=ORANGE, alpha=22, line=ORANGE, lw=1.5, dash=DASH, radius=0.04)
    label(lg.shapes, 3.05, 5.14, 0.9, 0.36, 'Pack', size=14, bold=True)
    inline_chip(S, 6.83, 5.15, 'Undecided', 'Needs a technical check (OQ20)')
    caption(s, 'Pack unlocks would sit inside the normal milestones if possible, or in clearly labelled extras.')
    slide_number(s)
    return s


# ------------------------------------------------------------------ 18 regional buildings
def station_sketch(gs, x, base, advanced):
    """Front view of a station building on a platform. x is the left edge of the sketch area (5.0 in wide)."""
    rect(gs, x, base, 5.0, 0.18, fill=STEEL, radius=0.03)          # platform edge
    if not advanced:
        bx, bw, bh = x + 1.4, 2.2, 1.0
        rect(gs, bx, base - bh, bw, bh, fill=PANEL_ALT, line=STEEL, lw=1.5)
        rect(gs, bx - 0.1, base - bh - 0.1, bw + 0.2, 0.1, fill=STEEL)
        rect(gs, bx + 0.25, base - 0.75, 0.55, 0.4, fill=BG, line=STEEL, lw=1)
        rect(gs, bx + 1.4, base - 0.8, 0.5, 0.8, fill=BG, line=STEEL, lw=1)
        rect(gs, x + 0.45, base - 0.7, 0.07, 0.7, fill=STEEL)
        rect(gs, x + 0.25, base - 0.85, 0.47, 0.22, fill=PANEL_ALT, line=STEEL, lw=1)
    else:
        bx, bw, bh = x + 0.95, 3.0, 1.4
        rect(gs, bx, base - bh, bw, bh, fill=PANEL_ALT, line=ORANGE, lw=1.75)
        poly(gs, [(bx - 0.15, base - bh), (bx + bw / 2, base - bh - 0.8), (bx + bw + 0.15, base - bh)], fill=ORANGE, line=ORANGE, lw=1.5)
        rect(gs, bx + bw - 0.7, base - bh - 0.75, 0.22, 0.55, fill=COAL, line=STEEL, lw=1)
        oval(gs, bx + bw / 2 - 0.2, base - bh - 0.58, 0.4, 0.4, fill=BG, line=AMBER, lw=1.5)
        for k in range(3):
            rect(gs, bx + 0.2 + k * 0.92, base - 1.15, 0.6, 0.55, fill=BG, line=STEEL, lw=1)
        rect(gs, bx + bw / 2 - 0.3, base - 0.75, 0.6, 0.75, fill=BG, line=STEEL, lw=1, radius=0.25)
        # canopies along the platform, either side of the building
        for cx0, cw in ((x + 0.05, 0.8), (bx + bw + 0.1, 0.9)):
            rect(gs, cx0, base - 1.05, cw, 0.1, fill=ORANGE)
            rect(gs, cx0 + 0.08, base - 0.95, 0.06, 0.95, fill=STEEL)
            rect(gs, cx0 + cw - 0.14, base - 0.95, 0.06, 0.95, fill=STEEL)


def s18(prs):
    s = new_slide(prs, 'Regional buildings', 18, chip='Proposed')
    specs = ((0.9, 'Basic (Core)', False, 'A plain station sketch: a small flat-roofed building with a door, a window and a sign.'),
             (6.83, 'Advanced (pack)', True, 'A richer station sketch: a larger building with a pitched roof, chimney, clock, several windows and a canopy.'))
    for x, title, adv, alt in specs:
        g = group(s, 'Station: ' + title, alt)
        gs = g.shapes
        rect(gs, x, 1.55, 5.6, 3.5, fill=PANEL, line=ORANGE if adv else LINE, lw=1.75 if adv else 1.5, radius=0.08,
             dash=DASH if adv else None)
        label(gs, x + 0.3, 1.65, 5.0, 0.5, title, size=20, bold=True)
        station_sketch(gs, x + 0.3, 4.55, adv)
    nb = boxed(s.shapes, 6.83, 5.25, 5.6, 0.5, 'Not owned means not shown.', size=18, bold=True, fill=None, line=MUTED, lw=1.5, dash=DASH, radius=0.08)
    name_it(nb, 'Note: not owned means not shown')
    inline_chip(s.shapes, 0.9, 5.33, 'Undecided', 'If a pack is missing: undecided (OQ23)')
    caption(s, 'Core gives basic regional looks. A pack adds the fancier ones.')
    slide_number(s)
    return s


# ------------------------------------------------------------------ 19 changing region
def s19(prs):
    s = new_slide(prs, 'Changing region with pack engines', 19, chip='Agreed')
    rows_y = (1.55, 2.87, 4.19)
    rh = 1.2
    lab_x, lab_w = 1.1, 2.55
    before_cx, after_cx = 5.3, 10.45
    bands = group(s, 'Row backgrounds', 'Three horizontal bands, one for each kind of engine.')
    for y in rows_y:
        rect(bands.shapes, 0.9, y, 11.53, rh, fill=PANEL, radius=0.08)
    ar = rect(s.shapes, 6.95, 1.55, 1.6, 3.84, fill=ORANGE, shape=MSO_SHAPE.RIGHT_ARROW)
    ar.adjustments[0] = 0.78
    ar.adjustments[1] = 0.22
    put_text(ar, 'Switch\nregion', size=16, bold=True, color=INK, align='c', anchor='m', inset=(0.02, 0, 0.02, 0))
    set_alt(ar, 'A large arrow labelled Switch region, pointing from the engines before the switch to the engines after it.', 'Region switch arrow')
    u = 0.72
    tender_kw = dict(n_wheels=4, boiler=1.25, tender=0.95)
    tank_kw = dict(n_wheels=3, boiler=1.15, tank=True)

    def put_engine(gs, cx, y, kw, **style):
        gw = engine_geom(0, u, boiler=kw['boiler'], tender=kw.get('tender', 0.0))['width']
        engine(gs, cx - gw / 2, y, u, **kw, **style)

    defs = (
        ('Core engine', 'Changes look', 'A Core engine before the switch is orange; after the switch it has a different look, amber and a different shape.',
         (tender_kw, dict(body=ORANGE)), (tank_kw, dict(body=AMBER)), False),
        ('Pack engine, no match', 'Unchanged', 'A pack engine with no match in the new region looks exactly the same after the switch.',
         (tender_kw, dict(body=ORANGE, outline=ORANGE, dashed=True)), (tender_kw, dict(body=ORANGE, outline=ORANGE, dashed=True)), False),
        ('Pack engine, with match', 'May change when a match exists', 'A second pack engine, which has a match, may change look after the switch: the dashed amber engine with a question mark shows this is not certain.',
         (tank_kw, dict(body=ORANGE, outline=ORANGE, dashed=True)), (tank_kw, dict(body=AMBER, outline=AMBER, dashed=True)), True),
    )
    for y, (lab, note, alt, (kb, sb), (ka, sa), q) in zip(rows_y, defs):
        g = group(s, 'Row: ' + lab, alt)
        gs = g.shapes
        label(gs, lab_x, y, lab_w, rh, lab, size=16, bold=True)
        put_engine(gs, before_cx, y + 0.12, kb, **sb)
        put_engine(gs, after_cx, y + 0.12, ka, **sa)
        label(gs, after_cx - 1.85, y + 0.86, 3.7, 0.3, note, size=14, bold=True, color=AMBER if q else TEXT, align='c')
        if q:
            question_mark(gs, after_cx + 1.55, y + 0.34, 0.5, color=AMBER, size=20, fill=BG)
    inline_chip(s.shapes, 0.9, 5.6, 'Undecided', 'Match rules: undecided (OQ23)')
    caption(s, 'Switch region and a pack engine without a match keeps its original look and number.')
    slide_number(s)
    return s


# ------------------------------------------------------------------ 20 friends and packs
def s20(prs):
    s = new_slide(prs, 'Friends and packs', 20, chip='Agreed')
    py = 1.85
    ph = 1.45
    g1 = group(s, 'Player with a pack', 'A player figure with a dashed pack box beside it: this player owns a pack.')
    pw = person(g1.shapes, 1.3, py, ph, body=TEXT)
    pack_box_icon(g1.shapes, 1.3 + pw + 0.25, py + 0.5, 0.75, 0.6)
    label(s.shapes, 0.9, py + ph + 0.1, 3.0, 0.4, 'Has a pack', size=16, bold=True, align='c', name='Label: has a pack')
    g2 = group(s, 'Player without a pack', 'A player figure with no pack: this player does not own a pack.')
    person(g2.shapes, 11.3, py, ph, body=MUTED)
    label(s.shapes, 10.1, py + ph + 0.1, 3.0, 0.4, 'No pack', size=16, bold=True, align='c', name='Label: no pack')
    w = group(s, 'One world', 'A globe labelled One world, the shared game world both players join.')
    cx, cy, d = 6.667, 2.65, 2.0
    oval(w.shapes, cx - d / 2, cy - d / 2, d, d, fill=PANEL, line=WATER, lw=2.5)
    oval(w.shapes, cx - d * 0.22, cy - d / 2, d * 0.44, d, fill=None, line=WATER, lw=1.25)
    line(w.shapes, cx - d / 2, cy, cx + d / 2, cy, color=WATER, lw=1.25)
    label(w.shapes, cx - 1.0, cy + d / 2 + 0.08, 2.0, 0.4, 'One world', size=16, bold=True, align='c')
    jy = cy
    jn = group(s, 'Joining arrows', 'Dashed arrows from each player to the world. A question mark on the second arrow shows it is not known whether a player without a pack can join.')
    arrow(jn.shapes, 3.65, jy, cx - d / 2 - 0.08, jy, color=ORANGE, dash=DASH)
    line(jn.shapes, 10.9, jy, 9.3, jy, color=ORANGE, lw=2.25, dash=DASH)
    arrow(jn.shapes, 8.5, jy, cx + d / 2 + 0.08, jy, color=ORANGE, dash=DASH)
    question_mark(jn.shapes, 8.9, jy, 0.75, color=AMBER, size=28, fill=BG)
    nb = boxed(s.shapes, 3.4, 4.65, 6.53, 0.55, 'Multiplayer comes after release.', size=20, bold=True, fill=None, line=AMBER, lw=2, radius=0.08)
    name_it(nb, 'Note: multiplayer comes after release')
    chip, w_ = inline_chip(s.shapes, (13.333 - 3.3) / 2, 5.4, 'Undecided', 'Not checked (OQ27)')
    caption(s, 'Ideally friends could join without buying a pack. That is only a hope for now.')
    slide_number(s)
    return s


# ------------------------------------------------------------------ 21 money and delivery
def s21(prs):
    s = new_slide(prs, 'Money and delivery', 21, chip='Undecided')
    for i, q in enumerate(('Price?', 'Where is it sold?', 'What rules apply?')):
        x = 0.6 + i * 4.165
        g = group(s, 'Question card: ' + q, 'A question card: ' + q + ' This is not decided.')
        gs = g.shapes
        rect(gs, x, 1.8, 3.8, 3.1, fill=PANEL, line=MUTED, lw=2, radius=0.1)
        question_mark(gs, x + 1.9, 2.75, 1.2, color=MUTED, size=48)
        label(gs, x + 0.2, 3.7, 3.4, 0.8, q, size=24, bold=True, align='c')
    label(s.shapes, 0.6, 5.3, 3.0, 0.4, 'OQ26', size=16, bold=True, color=MUTED, name='Footer: OQ26')
    caption(s, 'Prices and how packs are delivered are not decided. Nothing is promised.')
    slide_number(s)
    return s


# ------------------------------------------------------------------ 22 where this stands
def s22(prs):
    s = new_slide(prs, 'Where this stands', 22, chip='Provisional')
    steps = (('Core game for one player:', 'first', True), ('Regional packs:', 'an idea', False),
             ('More engines by update:', 'an idea', False), ('Historical cards:', 'an idea', False))
    w, gap, x0, y0, h = 2.65, 0.51, 0.6, 2.1, 2.45
    for i, (txt, state, first) in enumerate(steps):
        x = x0 + i * (w + gap)
        g = group(s, 'Step: ' + txt, 'Step: ' + txt + ' ' + state + '.')
        gs = g.shapes
        sp = rect(gs, x, y0, w, h, fill=PANEL, line=ORANGE if first else MUTED, lw=3 if first else 1.75,
                  dash=None if first else DASH, radius=0.1)
        put_text(sp, [[(txt, {'size': 18, 'bold': True, 'color': TEXT})], [(state, {'size': 26, 'bold': True,
                  'color': ORANGE if first else MUTED})]], align='c', anchor='m', inset=(0.15, 0.1, 0.15, 0.1), space_after=6)
        if i < 3:
            arrow(gs, x + w + 0.07, y0 + h / 2, x + w + gap - 0.07, y0 + h / 2, color=ORANGE)
    inline_chip(s.shapes, 0.6, 5.0, 'Provisional', 'Plans can change.')
    caption(s, 'Packs are an idea for after launch. The core game comes first.')
    slide_number(s)
    return s


# ------------------------------------------------------------------ 23 still undecided
def s23(prs):
    s = new_slide(prs, 'Still undecided', 23, chip='Undecided')
    items = ('Pack names and roster (OQ20)', 'Total engine cap (OQ20)', 'Category names (OQ20)', 'Golden Era dates (OQ21)',
             'Pack unlock stages (OQ20)', 'Buildings when a pack is missing (OQ23)', 'Joining without a pack (OQ27)',
             'Price and delivery (OQ26)')
    w, h, gx, gy = 2.85, 2.0, 0.243, 0.25
    for i, it in enumerate(items):
        r, c = divmod(i, 4)
        x = 0.6 + c * (w + gx)
        y = 1.5 + r * (h + gy)
        g = group(s, 'Open question: ' + it, 'An open question card with an Undecided chip: ' + it)
        gs = g.shapes
        rect(gs, x, y, w, h, fill=PANEL, radius=0.1)
        question_mark(gs, x + 0.45, y + 0.42, 0.5, color=MUTED, size=20)
        chip = rect(gs, x + 0.15, y + 0.8, w - 0.3, 1.0, fill=None, line=MUTED, lw=2, radius=0.12)
        put_text(chip, it, size=16, bold=True, color=TEXT, align='c', anchor='m', inset=(0.1, 0.04, 0.1, 0.04))
        name_it(chip, 'Undecided chip: ' + it)
    caption(s, 'These questions are open. Nothing here has been chosen yet.')
    slide_number(s)
    return s


# ------------------------------------------------------------------ 24 credits
CREDITS = [('P19', '1', 'Ben Salter', 'CC BY 2.0',
            'https://commons.wikimedia.org/wiki/File:Out_in_the_open_(530236847)_(2).jpg')]


def s24(prs):
    s = new_slide(prs, 'Image credits', 24, chip=None)
    S = s.shapes
    cols = ('Slot', 'Slide', 'Author', 'Licence', 'Source link')
    cw = (1.2, 1.2, 4.0, 2.6, 3.13)
    rows = 1 + len(CREDITS)
    gf = S.add_table(rows, len(cols), Inches(0.6), Inches(1.6), Inches(sum(cw)), Inches(0.45 * rows))
    set_alt(gf, 'Image credits table: slot, slide, author, licence and a Commons link for the one photograph in this deck.', 'Credits table')
    tbl = gf.table
    tblPr = tbl._tbl.tblPr
    sid = tblPr.find(qn('a:tableStyleId'))
    if sid is None:
        sid = etree.SubElement(tblPr, qn('a:tableStyleId'))
    sid.text = '{2D5ABB26-0587-4C30-8999-92F81FD0307C}'
    tbl.first_row = True
    tbl.horz_banding = False
    for i, wcol in enumerate(cw):
        tbl.columns[i].width = Inches(wcol)
    for r in range(rows):
        tbl.rows[r].height = Inches(0.45)
    def fill_cell(cell, text, bold=False, color=TEXT, bg=PANEL, link=None):
        cell.fill.solid(); cell.fill.fore_color.rgb = rgb(bg)
        cell.margin_left = cell.margin_right = Inches(0.12)
        cell.margin_top = cell.margin_bottom = Inches(0.05)
        cell.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf = cell.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        r = p.add_run(); r.text = text
        r.font.size = Pt(11); r.font.bold = bold; r.font.name = FONT
        r.font.color.rgb = rgb(color)
        r._r.get_or_add_rPr().set('lang', LANG)
        if link:
            r.hyperlink.address = link
            r.font.underline = True
        table_borders(cell)
    for c, name in enumerate(cols):
        fill_cell(tbl.cell(0, c), name, bold=True, bg=PANEL_ALT)
    for ri, (slot, slide, author, lic, url) in enumerate(CREDITS, start=1):
        for c, val in enumerate((slot, slide, author, lic)):
            fill_cell(tbl.cell(ri, c), val)
        fill_cell(tbl.cell(ri, 4), 'Commons', link=url, color=ORANGE)
    label(S, 0.6, 2.7, 12.13, 0.4, 'CC BY-SA photos are shown unmodified except for resizing.', size=14, color=TEXT, name='Note: licence')
    label(S, 0.6, 3.15, 12.13, 0.4, 'The photograph on slide 1 is cropped to fit.', size=14, color=TEXT, name='Note: crop')
    caption(s, 'Photographs come from Wikimedia Commons under Creative Commons licences.')
    slide_number(s)
    return s


BUILDERS = [s17, s18, s19, s20, s21, s22, s23, s24]
