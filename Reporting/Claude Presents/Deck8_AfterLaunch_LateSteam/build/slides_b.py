"""Slides 10 to 17."""
import math
from lib import *
from slides_a import diagram

LIV = ['2E6B45', '8C2F39', 'F28C28', '2FA3A0']          # example livery colours only
LIV_LABELS = ['Historical', 'Historical', 'Corporate', 'Custom']


def swatch_strip(G, x, y, w, h, gap, labels=None, label_h=0.45):
    for i, col in enumerate(LIV):
        sx = x + i * (w + gap)
        rrect(G, sx, y, w, h, col, 'steel', lw=1.5, radius=0.1)
        if labels:
            tbox(G, sx, y + h + 0.05, w, label_h, labels[i], size=18, bold=True, align='c',
                 anchor='m', margin=(0, 0, 0, 0))


# ------------------------------------------------------------------ 10 choosing at first use
def s10(prs):
    s = base_slide(prs, 10, 'Choosing at first use', 'Agreed')
    S = s.shapes
    G = diagram(S, 'Mock-up: first-use driving style choice',
                'A mock dialog with two buttons, Simple, which is preselected, and Advanced, and a note '
                'that the choice can be changed later.')
    dx, dy, dw, dh = 3.17, 1.65, 7.0, 3.5
    rrect(G, dx, dy, dw, dh, 'panel', 'steel', lw=2, radius=0.12)
    rrect(G, dx, dy, dw, 0.42, 'panel_alt', None, radius=0.12)
    rect(G, dx + 0.02, dy + 0.25, dw - 0.04, 0.17, 'panel_alt', None)
    for i in range(3):
        circle(G, dx + 0.3 + i * 0.3, dy + 0.21, 0.15, 'line')
    label(G, MSO_SHAPE.ROUNDED_RECTANGLE, dx + 0.5, dy + 0.85, 2.85, 1.15, 'Simple', 'orange', 'white',
          lw=3, radius=0.14, size=26, bold=True, color='dark', align='c')
    label(G, MSO_SHAPE.ROUNDED_RECTANGLE, dx + 3.65, dy + 0.85, 2.85, 1.15, 'Advanced', 'panel_alt',
          'steel', lw=2, radius=0.14, size=26, bold=True, align='c')
    checkmark(G, dx + 3.35, dy + 0.85, 0.46)
    tbox(G, dx + 0.5, dy + 2.05, 2.85, 0.36, 'Preselected', size=14, bold=True, color='orange',
         align='c', anchor='m', margin=(0, 0, 0, 0))
    tbox(G, dx + 0.3, dy + 2.65, dw - 0.6, 0.5, 'You can change this later.', size=20, color='muted',
         align='c', anchor='m', margin=(0, 0, 0, 0))
    c, w = inline_chip(S, 0, 5.45, 'Undecided', 'Exact screens: undecided', prefix=False)
    c.left = I((13.333 - w) / 2)
    add_caption(s, 10, 'The first time, the game asks which style you want. You can switch later.')


# ------------------------------------------------------------------ 11 simple: a good crew
def s11(prs):
    s = base_slide(prs, 11, 'Simple: a good crew', 'Agreed')
    S = s.shapes
    G = diagram(S, 'Diagram: one Go lever and a crew handling fire, steam and valves',
                'One Go lever on the left. On the right a crew of two people handle fire, steam and '
                'valves for you.')
    panel(G, 0.6, 1.45, 3.7, 4.6, 'panel')
    tbox(G, 0.6, 1.55, 3.7, 0.65, 'Go', size=30, bold=True, color='orange', align='c', anchor='m',
         margin=(0, 0, 0, 0))
    lever(G, 2.45, 2.4, 3.3, w=1.2)
    arrow(G, 4.4, 3.75, 5.2, 3.75, 'orange', 4)
    panel(G, 5.3, 1.45, 7.43, 4.6, 'panel')
    rrect(G, 5.75, 2.35, 2.55, 2.7, 'panel_alt', 'steel', lw=1.5, radius=0.12, dash=MSO_LINE.DASH)
    cap_person(G, 6.5, 2.75, 1.5, body='steel', cap='orange')
    cap_person(G, 7.6, 2.75, 1.5, body='white', cap='amber')
    tbox(G, 5.75, 4.45, 2.55, 0.5, 'Crew', size=16, bold=True, color='muted', align='c', anchor='m',
         margin=(0, 0, 0, 0))
    for i, (t, col) in enumerate((('Fire', 'orange'), ('Steam', 'white'), ('Valves', 'steel'))):
        ty = 2.45 + i * 0.9
        pill(G, 9.6, ty, 2.6, 0.62, t, fill='panel_alt', line=col, lw=2, size=20, bold=True, align='c')
        arrow(G, 8.4, 3.7, 9.55, ty + 0.31, 'orange', 2.25)
    add_caption(s, 11, 'Simple works like a skilled crew. You say go and the crew does the rest.')


# ------------------------------------------------------------------ 12 advanced: three things
def s12(prs):
    s = base_slide(prs, 12, 'Advanced: three things to manage', 'Agreed')
    S = s.shapes
    G = diagram(S, 'Diagram: four driver controls',
                'Four control icons: a fire, a regulator slider, a reverser lever and a brake on a wheel.')
    cw = 2.85
    names = ['Fire', 'Regulator', 'Reverser', 'Brake']
    for i, nm in enumerate(names):
        x = 0.6 + i * (cw + 0.243)
        cx = x + cw / 2
        panel(G, x, 1.55, cw, 4.45, 'panel')
        if i < 3:
            circle(G, x + 0.42, 1.97, 0.5, 'orange')
            tbox(G, x + 0.17, 1.72, 0.5, 0.5, str(i + 1), size=18, bold=True, color='dark', align='c',
                 anchor='m', margin=(0, 0, 0, 0), name='Badge')
        else:
            circle(G, x + 0.42, 1.97, 0.5, None, 'steel', lw=2)
            tbox(G, x + 0.17, 1.72, 0.5, 0.5, '+', size=20, bold=True, color='steel', align='c',
                 anchor='m', margin=(0, 0, 0, 0), name='Badge')
        d = 0.3
        if i == 0:
            coal_lumps(G, cx, 3.95 + d, 1.9)
            flame(G, cx, 3.98 + d, 1.65)
        elif i == 1:
            rrect(G, cx - 1.0, 3.45 + d, 2.0, 0.2, 'coal', 'steel', lw=1.5, radius=0.1)
            for t in range(5):
                line(G, cx - 0.8 + 0.4 * t, 3.18 + d, cx - 0.8 + 0.4 * t, 3.38 + d, 'steel', 1.5)
            line(G, cx - 0.2, 3.55 + d, cx - 0.2, 2.7 + d, 'steel', 8)
            circle(G, cx - 0.2, 2.65 + d, 0.5, 'orange', 'dark', lw=1.5)
            line(G, cx - 0.8, 4.0 + d, cx + 0.8, 4.0 + d, 'orange', 3, head='triangle', tail='triangle')
        elif i == 2:
            lever(G, cx - 0.25, 2.45 + d, 1.95, notches=3, w=0.8)
            line(G, cx + 0.7, 2.6 + d, cx + 0.7, 4.2 + d, 'orange', 3, head='triangle', tail='triangle')
        else:
            wheel(G, cx - 0.1, 3.3 + d, 1.6)
            rrect(G, cx + 0.72, 2.95 + d, 0.3, 0.7, 'red', 'dark', lw=1.5, radius=0.06)
            arrow(G, cx + 1.3, 3.3 + d, cx + 1.08, 3.3 + d, 'red', 3)
        tbox(G, x, 5.1, cw, 0.6, nm, size=22, bold=True, align='c', anchor='m', margin=(0, 0, 0, 0))
    add_caption(s, 12, 'You manage the fire, the regulator and the reverser. Braking stays too.')


# ------------------------------------------------------------------ 13 what you do not have to do
def s13(prs):
    s = base_slide(prs, 13, 'What you do not have to do', 'Agreed')
    S = s.shapes
    G = diagram(S, 'Diagram: crossed-out list of controls you do not manage',
                'A list of five crossed-out items: injectors, detailed boiler water, blower and damper, '
                'dozens of cab valves and procedures, beside a crowded panel of gauges and valves '
                'marked with a prohibition sign.')
    items = ['Injectors', 'Detailed boiler water', 'Blower and damper', 'Dozens of cab valves', 'Procedures']
    for i, t in enumerate(items):
        y = 1.55 + i * 0.9
        panel(G, 0.6, y, 7.0, 0.76, 'panel')
        x_badge(G, 1.1, y + 0.38, 0.46)
        tbox(G, 1.55, y + 0.05, 5.9, 0.66, [[(t, dict(strike=True))]], size=22, color='muted',
             anchor='m', margin=(0, 0, 0, 0))
    panel(G, 8.0, 1.55, 4.73, 4.4, 'panel')
    for r in range(5):
        for c in range(5):
            cx, cy = 8.55 + c * 0.9, 2.0 + r * 0.78
            circle(G, cx, cy, 0.5, 'coal', 'steel', lw=1.5)
            if (r + c) % 2 == 0:
                line(G, cx, cy, cx + 0.14, cy - 0.12, 'amber', 2)
            else:
                line(G, cx - 0.14, cy, cx + 0.14, cy, 'steel', 2.5)
                line(G, cx, cy - 0.14, cx, cy + 0.14, 'steel', 2.5)
    shape(G, MSO_SHAPE.NO_SYMBOL, 8.6, 2.0, 3.55, 3.55, 'red', None, fill_alpha=0.9)
    add_caption(s, 13, 'No injectors and no dozens of valves. It is steam driving, not a full simulator.')


# ------------------------------------------------------------------ 14 mistakes have natural results
def s14(prs):
    s = base_slide(prs, 14, 'Mistakes have natural results', 'Agreed')
    S = s.shapes
    G = diagram(S, 'Diagram: four mistakes and their natural results, and a crossed-out card',
                'Four cause and effect pairs: wrong settings give weaker pull, too much power makes '
                'wheels slip, low steam pressure gives less power, a weak fire gives a weaker engine. '
                'A crossed-out card reads Explosions and permanent damage.')
    pairs = [('Wrong settings', 'Weaker pull'), ('Too much power', 'Wheels slip'),
             ('Low steam pressure', 'Less power'), ('Weak fire', 'Weaker engine')]
    for i, (cause, effect) in enumerate(pairs):
        y = 1.55 + i * 0.97
        label(G, MSO_SHAPE.ROUNDED_RECTANGLE, 0.6, y, 3.5, 0.8, cause, 'panel', 'steel', lw=1.5,
              radius=0.1, size=20, bold=True, align='c')
        arrow(G, 4.2, y + 0.4, 4.95, y + 0.4, 'orange', 3)
        label(G, MSO_SHAPE.ROUNDED_RECTANGLE, 5.05, y, 3.5, 0.8, effect, 'panel_alt', 'orange', lw=2,
              radius=0.1, size=20, bold=True, color='text', align='c')
    rrect(G, 9.1, 1.55, 3.63, 2.9, 'panel', 'red', lw=3, radius=0.1)
    cross_over(G, 9.1, 1.55, 3.63, 2.9, lw=5, alpha=0.75)
    tbox(G, 9.3, 2.15, 3.23, 1.7, 'Explosions and permanent damage', size=22, bold=True, align='c',
         anchor='m', margin=(0, 0, 0, 0))
    inline_chip(S, 0.6, 5.5, 'Undecided', 'Exact rules: undecided (OQ24)', prefix=False)
    add_caption(s, 14, 'Bad driving costs speed and pulling power. It never wrecks your engine.')


# ------------------------------------------------------------------ 15 skill can pay
def s15(prs):
    s = base_slide(prs, 15, 'Skill can pay', 'Agreed')
    S = s.shapes
    G = diagram(S, 'Diagram: a hill with two speed lines',
                'A hill profile. Two speed lines run across it: Simple is steady and Advanced is slightly '
                'higher. A marker shows where to prepare before the climb. Shape only, not measured.')
    panel(G, 0.6, 1.45, 12.13, 4.1, 'panel')
    base = 4.85

    def bump(x):
        if x < 5.4 or x > 9.4:
            return 0.0
        return 0.5 * (1 + math.cos(math.pi * (x - 7.4) / 2.0))

    xs = [1.1 + 0.1 * i for i in range(0, 103)]            # 1.1 .. 11.3
    hill = [(1.0, base)] + [(x, base - 1.0 * bump(x)) for x in [1.0 + 0.1 * i for i in range(0, 114)]] \
        + [(12.3, base), (12.3, 5.4), (1.0, 5.4)]
    poly(G, hill, fill='panel_alt', line_c=None)
    poly(G, hill[1:115], line_c='steel', lw=2.5, closed=False)
    tbox(G, 6.6, 4.9, 1.6, 0.4, 'Hill', size=14, bold=True, color='muted', align='c', anchor='m',
         margin=(0, 0, 0, 0))
    simple = [(x, 3.05 + 0.32 * bump(x)) for x in xs]
    adv = [(x, 2.72 + 0.22 * bump(x)) for x in xs]
    poly(G, simple, line_c='white', lw=4, closed=False)
    poly(G, adv, line_c='orange', lw=4, closed=False)
    tbox(G, 11.4, 2.5, 1.3, 0.4, 'Advanced', size=14, bold=True, color='orange', anchor='m',
         margin=(0, 0, 0, 0))
    tbox(G, 11.4, 3.0, 1.3, 0.4, 'Simple', size=14, bold=True, anchor='m', margin=(0, 0, 0, 0))
    line(G, 4.6, 1.62, 4.6, base, 'amber', 2.25, dash=MSO_LINE.DASH)
    tbox(G, 4.72, 1.55, 4.0, 0.4, 'Prepare before the climb', size=14, bold=True, color='amber', anchor='m',
         margin=(0, 0, 0, 0))
    line(G, 0.95, base, 0.95, 2.05, 'steel', 2.25, tail='triangle')
    tbox(G, 1.05, 1.55, 1.6, 0.4, 'Speed', size=14, bold=True, color='muted', anchor='m', margin=(0, 0, 0, 0))
    tbox(S, 0.6, 5.62, 4.0, 0.36, 'Shape only. Not measured.', size=14, color='muted', italic=True,
         anchor='m', margin=(0, 0, 0, 0))
    c, w = inline_chip(S, 0, 5.62, 'Undecided', 'How much better: undecided (OQ24)', prefix=False)
    c.left = I(12.73 - w)
    add_caption(s, 15, 'Skilled drivers can prepare for hills and squeeze out a little more. Simple stays fine.')


# ------------------------------------------------------------------ 16 liveries: history first
def s16(prs):
    s = base_slide(prs, 16, 'Liveries: history first', 'Agreed')
    S = s.shapes
    G = diagram(S, 'Diagram: a locomotive silhouette and four example livery swatches',
                'A steam locomotive with four colour swatches labelled Historical, Historical, Corporate '
                'and Custom. Examples only.')
    loco(G, 2.55, 1.6, 8.2, body=LIV[0], tender=True, accent=LIV[0], band='amber')
    line(G, 2.2, 4.15, 11.1, 4.15, 'steel', 3)
    swatch_strip(G, 1.2, 4.55, 2.4, 0.8, 0.43, labels=LIV_LABELS)
    tbox(G, 0.6, 1.5, 2.6, 0.36, 'Examples only.', size=14, color='muted', italic=True, anchor='m',
         margin=(0, 0, 0, 0))
    add_caption(s, 16, 'Engines come in historical liveries. Corporate or custom looks stay possible.')


# ------------------------------------------------------------------ 17 not sold separately
def s17(prs):
    s = base_slide(prs, 17, 'Not sold separately', 'Agreed')
    S = s.shapes
    G = diagram(S, 'Diagram: livery swatches in the pack, with a crossed-out price tag',
                'Four livery swatches inside a box marked as the pack you own. A blank price tag beside '
                'it is crossed out with a red cross.')
    rrect(G, 0.6, 1.65, 9.8, 4.1, None, 'orange', lw=2.5, radius=0.12, dash=MSO_LINE.DASH)
    swatch_strip(G, 1.1, 2.2, 1.9, 1.8, 0.4)
    tbox(G, 0.8, 4.45, 9.4, 0.6, 'The pack you own', size=22, bold=True, color='orange', align='c',
         anchor='m', margin=(0, 0, 0, 0))
    price_tag(G, 10.85, 3.1, 1.7, 0.95)
    cross_over(G, 10.7, 2.8, 2.0, 1.55, lw=8, alpha=0.9)
    add_caption(s, 17, 'Historical liveries come with the pack you own. They are not sold one by one.')


def build(prs):
    for f in (s10, s11, s12, s13, s14, s15, s16, s17):
        f(prs)
