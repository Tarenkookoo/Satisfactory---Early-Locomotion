"""Slides 18 to 25."""
from lib import *
from lib import _runs
from slides_a import diagram
from slides_b import LIV

EXTRA = ['5A4A7A', 'C9A227', '2F4F7F', '7A2E1D', '4A4A4A', 'B5B5B5', '1F5F5B', 'D9D2B0']
BRASS = 'C9A227'


# ------------------------------------------------------------------ 18 picking a livery
def s18(prs):
    s = base_slide(prs, 18, 'Picking a livery', 'Proposed')
    S = s.shapes
    G = diagram(S, 'Mock-up: a livery customiser panel',
                'A mock customiser panel with an engine preview on the left and a grid of twelve colour '
                'swatches on the right, one of them selected.')
    px, py, pw, ph = 1.8, 1.55, 9.73, 3.75
    rrect(G, px, py, pw, ph, 'panel', 'steel', lw=2, radius=0.12)
    rrect(G, px, py, pw, 0.42, 'panel_alt', None, radius=0.12)
    rect(G, px + 0.02, py + 0.25, pw - 0.04, 0.17, 'panel_alt', None)
    for i in range(3):
        circle(G, px + 0.3 + i * 0.3, py + 0.21, 0.15, 'line')
    rrect(G, px + 0.25, py + 0.65, 5.0, 2.85, 'bg', 'line', lw=1.5, radius=0.1)
    loco(G, px + 0.55, py + 1.1, 4.4, body=LIV[0], tender=True, accent=LIV[0], band='amber')
    line(G, px + 0.4, py + 2.95, px + 5.1, py + 2.95, 'steel', 3)
    cols = LIV + EXTRA
    for i, col in enumerate(cols):
        r, c = divmod(i, 4)
        sx, sy = px + 5.75 + c * 0.97, py + 0.7 + r * 0.97
        rrect(G, sx, sy, 0.8, 0.8, col, 'white' if i == 0 else 'line', lw=4 if i == 0 else 1.5, radius=0.1)
    c, w = inline_chip(S, 0, 5.5, 'Undecided', 'Licensing: undecided (OQ25)', prefix=False)
    c.left = I((13.333 - w) / 2)
    add_caption(s, 18, "You might pick liveries in the game's own customiser. That is not checked yet.")


# ------------------------------------------------------------------ 19 prestige engines
def s19(prs):
    s = base_slide(prs, 19, 'Prestige engines', 'Agreed')
    S = s.shapes
    G = diagram(S, 'Diagram: a prestige engine on a pedestal with a tag and a card',
                'A steam locomotive on a display pedestal with a tag reading Extremely expensive, and a '
                'card reading Not better at hauling. A small golden cup stands for the game trophies.')
    rrect(G, 0.9, 5.2, 5.6, 0.4, 'line', None, radius=0.06)
    rrect(G, 1.3, 4.78, 4.8, 0.45, 'panel_alt', 'steel', lw=1.5, radius=0.06)
    loco(G, 1.45, 3.15, 4.5, body='amber', tender=True, accent='amber', band='orange')
    line(G, 1.3, 4.78, 6.1, 4.78, 'steel', 3)
    poly(G, [(1.1, 1.8), (4.2, 1.8), (4.2, 2.55), (1.1, 2.55), (0.75, 2.175)], fill='amber', line_c='dark', lw=1.5)
    circle(G, 1.12, 2.175, 0.16, 'bg', 'dark', lw=1.5)
    tbox(G, 1.4, 1.85, 2.75, 0.65, 'Extremely expensive', size=18, bold=True, color='dark', align='c',
         anchor='m', margin=(0, 0, 0, 0))
    label(G, MSO_SHAPE.ROUNDED_RECTANGLE, 7.3, 1.8, 5.4, 1.25, 'Not better at hauling', 'panel_alt',
          'orange', lw=2.5, radius=0.1, size=24, bold=True, align='c')
    c, w = inline_chip(S, 7.3, 3.5, 'Background', "Like the game's golden trophies")
    trophy(G, 8.2, 4.1, 1.35)
    add_caption(s, 19, 'Prestige engines are trophies for display. They are not better at hauling.')


# ------------------------------------------------------------------ 20 famous, named engines
def s20(prs):
    s = base_slide(prs, 20, 'Famous, named engines', 'Agreed')
    S = s.shapes
    G = diagram(S, 'Diagram: a nameplate card with a fixed name, a fixed number and one per world',
                'A brass nameplate reading Fixed name, a number plate reading Fixed number, and a globe '
                'marked one, reading One per world.')
    rrect(G, 0.8, 1.6, 7.3, 3.5, 'panel', None, radius=0.12)
    rrect(G, 1.2, 1.95, 6.5, 1.55, 'coal', BRASS, lw=6, radius=0.5)
    rrect(G, 1.38, 2.13, 6.14, 1.19, None, BRASS, lw=1.5, radius=0.4)
    tbox(G, 1.6, 2.15, 5.7, 1.15, 'Fixed name', size=40, bold=True, color=BRASS, align='c', anchor='m',
         margin=(0, 0, 0, 0))
    rrect(G, 2.55, 3.8, 3.8, 1.0, 'coal', 'white', lw=3, radius=0.1)
    tbox(G, 2.65, 3.85, 3.6, 0.9, 'Fixed number', size=26, bold=True, align='c', anchor='m',
         margin=(0, 0, 0, 0))
    globe(G, 10.5, 2.95, 2.2)
    circle(G, 11.45, 1.95, 0.7, 'orange', 'dark', lw=2)
    tbox(G, 11.1, 1.6, 0.7, 0.7, '1', size=26, bold=True, color='dark', align='c', anchor='m',
         margin=(0, 0, 0, 0), name='Badge')
    tbox(G, 8.7, 4.25, 3.6, 0.6, 'One per world', size=24, bold=True, align='c', anchor='m',
         margin=(0, 0, 0, 0))
    c, w = inline_chip(S, 0, 5.45, 'Undecided', 'Which engines: undecided (OQ25)', prefix=False)
    c.left = I((13.333 - w) / 2)
    add_caption(s, 20, 'A prestige engine is one real, famous machine. Its name and number never change.')


# ------------------------------------------------------------------ 21 prestige in the core game
def s21(prs):
    s = base_slide(prs, 21, 'Prestige in the core game', 'Agreed')
    S = s.shapes
    G = diagram(S, 'Diagram: a normal engine beside a prestige engine',
                'A normal orange engine beside a special engine of the same class with a white colour '
                'band and a fixed plate, labelled Fixed name and number.')
    rail_y = 4.7
    lw_ = 4.8
    loco(G, 0.9, 2.55, lw_, body='orange')
    loco(G, 7.2, 2.55, lw_, body='orange', band='white', plate='amber')
    line(G, 0.6, rail_y, 5.9, rail_y, 'steel', 3)
    line(G, 6.9, rail_y, 12.5, rail_y, 'steel', 3)
    tbox(G, 0.9, 5.0, lw_, 0.5, 'Normal engine', size=20, bold=True, align='c', anchor='m', margin=(0, 0, 0, 0))
    tbox(G, 7.2, 5.0, lw_, 0.5, 'Prestige engine', size=20, bold=True, color='amber', align='c', anchor='m',
         margin=(0, 0, 0, 0))
    tbox(G, 8.1, 1.55, 2.9, 0.45, 'Fixed name and number', size=18, bold=True, color='amber', align='c',
         anchor='m', margin=(0, 0, 0, 0))
    plate_cx = 7.2 + (46 + 7.5) * lw_ / 100
    arrow(G, plate_cx, 2.02, plate_cx, 3.17, 'amber', 2.25)
    add_caption(s, 21, 'Even the core game could have a prestige engine: one special member of a core class.')


# ------------------------------------------------------------------ 22 showpiece coaches
def s22(prs):
    s = base_slide(prs, 22, 'Showpiece coaches', 'Proposed')
    S = s.shapes
    G = diagram(S, 'Diagram: an engine with two display coaches',
                'A steam locomotive with its tender pulling two coaches, with a bracket labelled '
                'Display only.')
    rail = 4.1
    loco(G, 0.8, 2.55, 5.0, body=LIV[0], tender=True, accent=LIV[0], band='amber')
    cx = 5.9
    for _ in range(2):
        coach(G, cx, rail - 0.94, 3.1, body=LIV[1], windows=5)
        cx += 3.2
    line(G, 0.5, rail, 12.8, rail, 'steel', 3)
    br_y = 4.55
    line(G, 0.9, br_y, 12.2, br_y, 'amber', 2.25)
    line(G, 0.9, br_y - 0.12, 0.9, br_y + 0.12, 'amber', 2.25)
    line(G, 12.2, br_y - 0.12, 12.2, br_y + 0.12, 'amber', 2.25)
    pill(G, 5.37, 4.78, 2.6, 0.5, 'Display only', fill='panel', line='amber', lw=2, size=20, bold=True, align='c')
    c, w = inline_chip(S, 0, 5.5, 'Undecided', 'Which coaches: undecided (OQ25)', prefix=False)
    c.left = I((13.333 - w) / 2)
    add_caption(s, 22, 'Historic coaches might join a prestige engine for show. There is still no passenger economy.')


# ------------------------------------------------------------------ 23 where this stands
def s23(prs):
    s = base_slide(prs, 23, 'Where this stands', 'Provisional')
    S = s.shapes
    G = diagram(S, 'Diagram: four post-launch ideas, none started',
                'A row of four steps, each marked as an idea: advanced buildings, advanced driving, '
                'liveries and prestige engines.')
    items = ['Advanced buildings:', 'Advanced driving:', 'Liveries:', 'Prestige engines:']
    cw, gap = 2.8, 0.31
    xs = [0.6 + i * (cw + gap) for i in range(4)]
    for x, t in zip(xs, items):
        panel(G, x, 1.65, cw, 3.2, 'panel')
        circle(G, x + cw / 2, 2.55, 1.15, 'panel', 'muted', lw=2.5, dash=MSO_LINE.DASH)
        bulb(G, x + cw / 2, 2.47, 0.5)
        tbox(G, x + 0.12, 3.5, cw - 0.24, 1.2, [[(t, dict(bold=True))], [('an idea', dict(color='amber', bold=True))]],
             size=20, align='c', anchor='t', margin=(0, 0, 0, 0))
    for x in xs[:3]:
        shape(G, MSO_SHAPE.CHEVRON, x + cw + 0.08, 3.1, 0.15, 0.36, 'muted', None)
    c, w = inline_chip(S, 0, 5.4, 'Provisional', 'Plans can change.')
    c.left = I((13.333 - w) / 2)
    add_caption(s, 23, 'Late steam, advanced driving and prestige are ideas for after launch.')


# ------------------------------------------------------------------ 24 still undecided
def s24(prs):
    s = base_slide(prs, 24, 'Still undecided', 'Undecided')
    S = s.shapes
    G = diagram(S, 'Diagram: eight open questions',
                'A grid of eight cards, each marked Undecided, listing the open questions about advanced '
                'buildings, balance, driving formulas, the Advanced bonus, liveries, prestige engines, '
                'prestige prices and names and licences.')
    qs = [('Which advanced buildings?', 'OQ22'), ('Balance against electric', 'OQ22'),
          ('Driving formulas', 'OQ24'), ('Size of the Advanced bonus', 'OQ24'),
          ('Livery integration', 'OQ25'), ('Which prestige engines?', 'OQ25'),
          ('Prestige prices', 'OQ25'), ('Names and licences', 'OQ25')]
    cw, gap = 2.9, (12.13 - 4 * 2.9) / 3
    for i, (q, oq) in enumerate(qs):
        r, c = divmod(i, 4)
        x, y = 0.6 + c * (cw + gap), 1.55 + r * 2.15
        panel(G, x, y, cw, 1.95, 'panel')
        plain_chip(G, x + 0.2, y + 0.2, 'Undecided', w=1.4, h=0.34)
        tbox(G, x + 0.2, y + 0.7, cw - 0.4, 1.15, [[(q + ' ', dict(bold=True)), ('(' + oq + ')', dict(color='muted'))]],
             size=18, anchor='t', margin=(0, 0, 0, 0))
    add_caption(s, 24, 'These questions are open. Nothing here has been chosen yet.')


# ------------------------------------------------------------------ 25 image credits
def s25(prs):
    s = base_slide(prs, 25, 'Image credits')
    S = s.shapes
    cols = [1.0, 1.0, 3.2, 2.4, 4.53]
    rows = [('Slot', 'Slide', 'Author', 'Licence', 'Source link'),
            ('P12', '1', 'Tony Hisgett', 'CC BY 2.0', 'Commons')]
    gf = S.add_table(len(rows), 5, I(0.6), I(1.6), I(sum(cols)), I(1.2))
    gf.name = 'Table: image credits'
    gf._element.xpath('.//p:cNvPr')[0].set('descr', 'Credit table for the one photograph in this deck: '
                                                    'slot P12, shown on slide 1, by Tony Hisgett, licence '
                                                    'CC BY 2.0, with a link to Wikimedia Commons.')
    tbl = gf.table
    tblPr = tbl._tbl.tblPr
    for a in ('bandRow', 'bandCol', 'firstCol', 'lastRow', 'lastCol'):
        tblPr.set(a, '0')
    tblPr.set('firstRow', '1')
    for i, w in enumerate(cols):
        tbl.columns[i].width = I(w)
    url = 'https://commons.wikimedia.org/wiki/File:92203_at_Toddington_on_the_Gloucestershire_and_Warwickshire_Railway_(3).jpg'
    for r, row in enumerate(rows):
        tbl.rows[r].height = I(0.6)
        for c, val in enumerate(row):
            cell = tbl.cell(r, c)
            cell.fill.solid()
            cell.fill.fore_color.rgb = rgb('panel_alt' if r == 0 else 'panel')
            cell.margin_left = cell.margin_right = I(0.12)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            tf = cell.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            if r == 1 and c == 4:
                seg = (val, dict(color='water', url=url))
            else:
                seg = (val, dict(bold=(r == 0)))
            _runs(p, [seg], dict(size=11, color='text', bold=False))
            tcPr = cell._tc.get_or_add_tcPr()
            for k, tag in enumerate(('a:lnL', 'a:lnR', 'a:lnT', 'a:lnB')):
                ln = etree.Element(qn(tag))
                ln.set('w', '12700')
                sf = etree.SubElement(ln, qn('a:solidFill'))
                clr = etree.SubElement(sf, qn('a:srgbClr'))
                clr.set('val', C['line'])
                tcPr.insert(k, ln)
    tbox(S, 0.6, 3.25, 12.13, 0.45, 'CC BY-SA photos are shown unmodified except for resizing.', size=14,
         color='muted', anchor='m', margin=(0, 0, 0, 0), name='Table note')
    tbox(S, 0.6, 3.75, 12.13, 0.45, 'The photograph shows a real steam locomotive. It is not a model from the mod.',
         size=14, color='muted', anchor='m', margin=(0, 0, 0, 0), name='Table note')
    add_caption(s, 25, 'Photographs come from Wikimedia Commons under Creative Commons licences.')


def build(prs):
    for f in (s18, s19, s20, s21, s22, s23, s24, s25):
        f(prs)
