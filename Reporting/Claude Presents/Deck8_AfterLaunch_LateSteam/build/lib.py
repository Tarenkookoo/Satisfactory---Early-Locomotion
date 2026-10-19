"""Shape library for Deck 8 (python-pptx, native shapes only).

Every helper takes S, a shapes collection (slide.shapes or group.shapes), so the same
helper draws on a slide or inside a diagram group. Units are inches unless noted.
"""
import os
from lxml import etree
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR, MSO_AUTO_SIZE
from pptx.enum.dml import MSO_LINE
from pptx.opc.constants import RELATIONSHIP_TYPE as RT
from pptx.oxml.ns import qn
from PIL import Image, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.abspath(os.path.join(HERE, '..', '..', 'images'))
FONT_REG = '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
FONT_BOLD = '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'

C = dict(
    bg='1E2126', panel='2B2F36', panel_alt='343A43', line='4A515B', text='F2F2F2',
    muted='A9B0B8', orange='F28C28', red='E5484D', green='3FB950', amber='F2C14E',
    water='4DA3FF', electric='6CA0DC', coal='1B1D21', steel='9AA0A6',
    sleeper='6B5B4B', dark='101418', purple='B084F5', white='E8E8E8',
    wagon='6C7480', ballast='5A5F66',
)
CHIPS = {
    'Agreed': dict(fill='green', text='dark', line=None),
    'Proposed': dict(fill='purple', text='dark', line=None),
    'Provisional': dict(fill='water', text='dark', line=None),
    'Undecided': dict(fill=None, text='text', line='muted'),
    'Background': dict(fill='line', text='text', line=None),
}
LANG = 'en-GB'


def I(v):
    return Emu(int(round(v * 914400)))


def rgb(c):
    return RGBColor.from_string(C.get(c, c))


# ---------------------------------------------------------------- text measuring
_fonts = {}


def _font(bold):
    k = 'b' if bold else 'r'
    if k not in _fonts:
        _fonts[k] = ImageFont.truetype(FONT_BOLD if bold else FONT_REG, 200)
    return _fonts[k]


def text_w(text, size, bold=False):
    """Width in inches of a single line of Arial-metric text."""
    return _font(bold).getlength(text) / 200.0 * size / 72.0


def wrap_lines(text, size, width, bold=False):
    """Greedy wrap; returns the number of lines for text in width (inches)."""
    total = 0
    for para in text.split('\n'):
        for seg in para.split('\v'):
            words = seg.split(' ')
            cur = ''
            n = 1
            for w in words:
                t = (cur + ' ' + w).strip() if cur else w
                if text_w(t, size, bold) <= width or not cur:
                    cur = t
                else:
                    n += 1
                    cur = w
            total += n
    return total


# ---------------------------------------------------------------- low-level style
def _strip_style(sh):
    st = sh._element.find(qn('p:style'))
    if st is not None:
        sh._element.remove(st)


def _alpha(parent_fill_el, a):
    clr = parent_fill_el.find(qn('a:srgbClr'))
    if clr is not None:
        al = etree.SubElement(clr, qn('a:alpha'))
        al.set('val', str(int(a * 100000)))


def style(sh, fill=None, line=None, lw=1.5, dash=None, fill_alpha=None, line_alpha=None):
    if fill is None:
        sh.fill.background()
    else:
        sh.fill.solid()
        sh.fill.fore_color.rgb = rgb(fill)
        if fill_alpha is not None:
            _alpha(sh.fill._xPr.find(qn('a:solidFill')), fill_alpha)
    if line is None:
        sh.line.fill.background()
    else:
        sh.line.color.rgb = rgb(line)
        sh.line.width = Pt(lw)
        if dash:
            sh.line.dash_style = dash
        if line_alpha is not None:
            ln = sh.line._get_or_add_ln()
            _alpha(ln.find(qn('a:solidFill')), line_alpha)


def name_it(sh, name=None, descr=None):
    if name:
        sh.name = name
    if descr:
        sh._element.xpath('.//p:cNvPr')[0].set('descr', descr)


def shape(S, kind, x, y, w, h, fill=None, line=None, lw=1.5, dash=None, radius=None,
          rot=0, name=None, descr=None, fill_alpha=None, line_alpha=None, adj=None):
    sh = S.add_shape(kind, I(x), I(y), I(w), I(h))
    _strip_style(sh)
    style(sh, fill, line, lw, dash, fill_alpha, line_alpha)
    if radius is not None and kind == MSO_SHAPE.ROUNDED_RECTANGLE:
        sh.adjustments[0] = min(0.5, radius / min(w, h))
    if adj is not None:
        for i, a in enumerate(adj):
            sh.adjustments[i] = a
    if rot:
        sh.rotation = rot
    name_it(sh, name, descr)
    return sh


def rect(S, x, y, w, h, fill=None, line=None, **kw):
    return shape(S, MSO_SHAPE.RECTANGLE, x, y, w, h, fill, line, **kw)


def rrect(S, x, y, w, h, fill=None, line=None, radius=0.08, **kw):
    return shape(S, MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h, fill, line, radius=radius, **kw)


def oval(S, x, y, w, h, fill=None, line=None, **kw):
    return shape(S, MSO_SHAPE.OVAL, x, y, w, h, fill, line, **kw)


def circle(S, cx, cy, d, fill=None, line=None, **kw):
    return oval(S, cx - d / 2, cy - d / 2, d, d, fill, line, **kw)


def tri(S, x, y, w, h, fill=None, line=None, **kw):
    return shape(S, MSO_SHAPE.ISOSCELES_TRIANGLE, x, y, w, h, fill, line, **kw)


# ---------------------------------------------------------------- text
def _runs(p, segs, base):
    for seg in segs:
        text, fmt = (seg, {}) if isinstance(seg, str) else seg
        f = dict(base)
        f.update(fmt)
        parts = text.split('\v')
        for i, part in enumerate(parts):
            if i > 0:
                p.add_line_break()
            if part == '':
                continue
            r = p.add_run()
            r.text = part
            fo = r.font
            fo.name = 'Arial'
            fo.size = Pt(f['size'])
            fo.bold = f['bold']
            fo.italic = f.get('italic', False)
            fo.color.rgb = rgb(f['color'])
            rPr = r._r.get_or_add_rPr()
            rPr.set('lang', LANG)
            if f.get('strike'):
                rPr.set('strike', 'sngStrike')
            if f.get('url'):
                r.hyperlink.address = f['url']
                if f.get('underline', True):
                    fo.underline = True


def put_text(sh, content, size=18, color='text', bold=False, align='l', anchor='m',
             margin=(0.08, 0.03, 0.08, 0.03), wrap=True, italic=False):
    tf = sh.text_frame
    tf.word_wrap = wrap
    tf.auto_size = MSO_AUTO_SIZE.NONE
    tf.margin_left, tf.margin_top, tf.margin_right, tf.margin_bottom = [I(m) for m in margin]
    tf.vertical_anchor = {'t': MSO_ANCHOR.TOP, 'm': MSO_ANCHOR.MIDDLE, 'b': MSO_ANCHOR.BOTTOM}[anchor]
    if isinstance(content, str):
        content = content.split('\n')
    base = dict(size=size, color=color, bold=bold, italic=italic)
    first = True
    for para in content:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.alignment = {'l': PP_ALIGN.LEFT, 'c': PP_ALIGN.CENTER, 'r': PP_ALIGN.RIGHT}[align]
        p.space_before = Pt(0)
        p.space_after = Pt(0)
        segs = [para] if isinstance(para, str) else para
        _runs(p, segs, base)
    return sh


def tbox(S, x, y, w, h, content, name=None, descr=None, **kw):
    tb = S.add_textbox(I(x), I(y), I(w), I(h))
    put_text(tb, content, **kw)
    name_it(tb, name, descr)
    return tb


def label(S, kind, x, y, w, h, content, fill=None, line=None, lw=1.5, radius=0.08,
          name=None, descr=None, dash=None, rot=0, fill_alpha=None, **tk):
    sh = shape(S, kind, x, y, w, h, fill, line, lw, dash, radius=radius, rot=rot,
               name=name, descr=descr, fill_alpha=fill_alpha)
    put_text(sh, content, **tk)
    return sh


def pill(S, x, y, w, h, content, fill=None, line=None, **kw):
    return label(S, MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h, content, fill, line,
                 radius=h / 2, **kw)


# ---------------------------------------------------------------- lines and polylines
def _ends(ln, head, tail):
    for tag, kind in (('a:headEnd', head), ('a:tailEnd', tail)):
        if kind:
            e = etree.SubElement(ln, qn(tag))
            e.set('type', kind)
            e.set('w', 'med')
            e.set('len', 'med')


def line(S, x1, y1, x2, y2, color='steel', lw=2.25, dash=None, head=None, tail=None,
         name=None, line_alpha=None):
    c = S.add_connector(MSO_CONNECTOR.STRAIGHT, I(x1), I(y1), I(x2), I(y2))
    _strip_style(c)
    c.line.color.rgb = rgb(color)
    c.line.width = Pt(lw)
    if dash:
        c.line.dash_style = dash
    ln = c.line._get_or_add_ln()
    if line_alpha is not None:
        _alpha(ln.find(qn('a:solidFill')), line_alpha)
    _ends(ln, head, tail)
    name_it(c, name)
    return c


def arrow(S, x1, y1, x2, y2, color='orange', lw=2.25, **kw):
    return line(S, x1, y1, x2, y2, color, lw, tail='triangle', **kw)


def poly(S, pts, fill=None, line_c=None, lw=1.5, closed=True, dash=None, head=None,
         tail=None, name=None, fill_alpha=None, line_alpha=None):
    fb = S.build_freeform(I(pts[0][0]), I(pts[0][1]))
    fb.add_line_segments([(I(px), I(py)) for px, py in pts[1:]], close=closed)
    sh = fb.convert_to_shape()
    _strip_style(sh)
    style(sh, fill if closed else None, line_c, lw, dash, fill_alpha, line_alpha)
    if head or tail:
        _ends(sh.line._get_or_add_ln(), head, tail)
    name_it(sh, name)
    return sh


# ---------------------------------------------------------------- groups
def group(S, name, descr):
    g = S.add_group_shape()
    g.name = name
    g._element.nvGrpSpPr.cNvPr.set('descr', descr)
    return g


# ---------------------------------------------------------------- pictures
def picture(S, fname, x, y, w, h, descr, focus=(0.5, 0.5), radius=0.08, name=None):
    path = os.path.join(IMG_DIR, fname)
    iw, ih = Image.open(path).size
    tgt, src = w / h, iw / ih
    pic = S.add_picture(path, I(x), I(y), I(w), I(h))
    if src > tgt:
        vis = tgt / src
        left = (1 - vis) * focus[0]
        pic.crop_left, pic.crop_right = left, 1 - vis - left
    else:
        vis = src / tgt
        top = (1 - vis) * focus[1]
        pic.crop_top, pic.crop_bottom = top, 1 - vis - top
    pic.name = name or 'Picture ' + fname
    pic._element.xpath('.//p:cNvPr')[0].set('descr', descr)
    spPr = pic._element.spPr
    geom = spPr.find(qn('a:prstGeom'))
    geom.set('prst', 'roundRect')
    av = geom.find(qn('a:avLst'))
    if av is None:
        av = etree.SubElement(geom, qn('a:avLst'))
    for g in list(av):
        av.remove(g)
    gd = etree.SubElement(av, qn('a:gd'))
    gd.set('name', 'adj')
    gd.set('fmla', 'val %d' % int(min(0.5, radius / min(w, h)) * 100000))
    return pic


# ---------------------------------------------------------------- slide furniture
def new_deck():
    prs = Presentation()
    prs.slide_width = Emu(12192000)
    prs.slide_height = Emu(6858000)
    th = prs.slide_master.part.part_related_by(RT.THEME)
    blob = th.blob.decode('utf-8')
    blob = blob.replace('typeface="Calibri"', 'typeface="Arial"')
    import re
    blob = re.sub(r'(<a:hlink>)<a:srgbClr val="[0-9A-Fa-f]{6}"/>', r'\1<a:srgbClr val="4DA3FF"/>', blob)
    blob = re.sub(r'(<a:folHlink>)<a:srgbClr val="[0-9A-Fa-f]{6}"/>', r'\1<a:srgbClr val="B084F5"/>', blob)
    th._blob = blob.encode('utf-8')
    cp = prs.core_properties
    cp.title = 'After Launch, Part 2: Late Steam, Advanced Driving and Prestige, Explained'
    cp.author = 'Claude (Early Locomotion project)'
    cp.last_modified_by = 'Claude (Early Locomotion project)'
    cp.language = LANG
    cp.subject = 'Explainer deck about post-launch late steam, advanced driving and prestige ideas'
    return prs


CAP_Y, CAP_H = 6.28, 0.76


def status_chip(S, status, name='Status chip'):
    spec = CHIPS[status]
    sh = shape(S, MSO_SHAPE.ROUNDED_RECTANGLE, 11.2, 0.5, 1.5, 0.4, spec['fill'], spec['line'],
               lw=2, radius=0.12, name=name)
    put_text(sh, status.upper(), size=14, bold=True, color=spec['text'], align='c', anchor='m',
             margin=(0.04, 0.02, 0.04, 0.02), wrap=False)
    return sh


def inline_chip(S, x, y, status, text=None, size=14, h=0.36, prefix=True, name='Inline chip'):
    """Pill with the status word and the briefed text. Returns its width."""
    spec = CHIPS[status]
    segs = []
    if prefix:
        segs.append((status.upper() + ('  ' if text else ''), dict(bold=True)))
    if text:
        segs.append((text, dict(bold=False)))
    full = ''.join(s[0] for s in segs)
    wb = text_w(status.upper(), size, True) if prefix else 0
    w = (wb + text_w('  ', size) if prefix and text else 0) + (text_w(text, size) if text else 0) + 0.34
    sh = shape(S, MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h, spec['fill'], spec['line'], lw=2,
               radius=h / 2, name=name)
    put_text(sh, [segs], size=size, color=spec['text'], align='c', anchor='m',
             margin=(0.08, 0.02, 0.08, 0.02), wrap=False)
    return sh, w


def plain_chip(S, x, y, status, w=1.3, h=0.32, size=14, name='Inline chip'):
    spec = CHIPS[status]
    sh = shape(S, MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h, spec['fill'], spec['line'], lw=2,
               radius=h / 2, name=name)
    put_text(sh, status.upper(), size=size, bold=True, color=spec['text'], align='c', anchor='m',
             margin=(0.03, 0.0, 0.03, 0.0), wrap=False)
    return sh


def base_slide(prs, n, title, chip=None, caption=None, bg='bg'):
    s = prs.slides.add_slide(prs.slide_layouts[5])
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = rgb(bg)
    t = s.shapes.title
    t.left, t.top, t.width, t.height = I(0.6), I(0.45), I(10.4), I(0.8)
    put_text(t, title, size=36, bold=True, color='text', anchor='t', margin=(0, 0, 0, 0))
    t.name = 'Title'
    if chip:
        status_chip(s.shapes, chip)
    return s


def add_caption(s, n, text, size=20):
    bar = shape(s.shapes, MSO_SHAPE.ROUNDED_RECTANGLE, 0.6, CAP_Y, 12.13, CAP_H, 'panel', None,
                radius=0.08, name='Caption')
    put_text(bar, text, size=size, color='text', anchor='m', margin=(0.3, 0.03, 0.2, 0.03))
    shape(s.shapes, MSO_SHAPE.ROUNDED_RECTANGLE, 0.6, CAP_Y, 0.08, CAP_H, 'orange', None,
          radius=0.04, name='Caption rule')
    tbox(s.shapes, 12.1, 7.08, 0.63, 0.3, str(n), size=14, color='muted', align='r', anchor='m',
         margin=(0, 0, 0, 0), name='Slide number')


def credit(S, x, y, w, text, h=0.3, align='l'):
    return tbox(S, x, y, w, h, text, size=10, color='muted', anchor='t', align=align,
                margin=(0, 0, 0, 0), name='Credit line')


# ---------------------------------------------------------------- icons and objects
def person(S, cx, y, h, body='white', head=None):
    """Head and shoulders icon: circle head, rounded body. y = top, h = total height."""
    head = head or body
    d = h * 0.40
    circle(S, cx, y + d / 2, d, head)
    rrect(S, cx - h * 0.30, y + d + h * 0.05, h * 0.60, h * 0.55, body, radius=h * 0.2)


def cap_person(S, cx, y, h, body='steel', cap='orange'):
    person(S, cx, y, h, body)
    d = h * 0.40
    rect(S, cx - d * 0.62, y + d * 0.10, d * 1.24, d * 0.22, cap)
    rect(S, cx - d * 0.40, y - d * 0.05, d * 0.80, d * 0.18, cap)


def lever(S, cx, y, h, knob='orange', slot_w=0.14, notches=0, w=0.7):
    """A lever in a slot: dark slot, handle leaning from the bottom, round knob."""
    rrect(S, cx - slot_w / 2, y, slot_w, h, 'coal', 'steel', lw=1.5, radius=slot_w / 2)
    for i in range(notches):
        ny = y + h * (i + 1) / (notches + 1)
        line(S, cx - w * 0.35, ny, cx - slot_w / 2 - 0.02, ny, 'steel', 1.5)
    base_y = y + h * 0.85
    top_y = y + h * 0.18
    line(S, cx, base_y, cx, top_y, 'steel', 6)
    circle(S, cx, top_y, w * 0.55, knob, 'dark', lw=1.5)
    rrect(S, cx - w * 0.4, base_y - 0.06, w * 0.8, 0.14, 'panel_alt', 'steel', lw=1.5, radius=0.05)


def wheel(S, cx, cy, d, rim='steel', fill='coal', spokes=True):
    circle(S, cx, cy, d, fill, rim, lw=2)
    if spokes:
        r = d / 2 * 0.85
        line(S, cx - r, cy, cx + r, cy, rim, 1.25)
        line(S, cx, cy - r, cx, cy + r, rim, 1.25)
    circle(S, cx, cy, d * 0.18, rim)


def loco(S, x, y, w, body='orange', tender=False, face='left', accent=None, band=None, plate=None):
    """Generic side-view steam locomotive silhouette (not a model from the mod).

    x, y is the top-left; w is the full width including the tender; height = w * 0.36.
    face='left' puts the chimney on the left. plate/band: optional prestige details.
    """
    total_u = 148.0 if tender else 100.0
    s = w / total_u
    flip = face == 'right'

    def X(u, wu=0):
        return x + (total_u - u - wu) * s if flip else x + u * s

    def R(u, v, wu, hu, fill=None, line_c=None, lw=1.0, rad=None, **kw):
        if rad is not None:
            return rrect(S, X(u, wu), y + v * s, wu * s, hu * s, fill, line_c, radius=rad * s, lw=lw, **kw)
        return rect(S, X(u, wu), y + v * s, wu * s, hu * s, fill, line_c, lw=lw, **kw)

    dark = 'coal'
    # frame and boiler
    R(4, 29, 94, 6, 'panel_alt', 'steel', 1.0)
    R(12, 11, 58, 19, body, dark, 1.0, rad=6)
    R(5, 11, 9, 19, dark, None)                       # smokebox
    R(7, 3, 6, 8, dark, None)                          # chimney
    R(5, 1.5, 10, 3, dark, None)
    R(38, 6, 11, 6, body, dark, 1.0, rad=3)           # dome
    if band:
        R(14, 20, 54, 4, band, None)
    R(66, 2, 31, 28, accent or body, dark, 1.0)       # cab
    R(63, 0, 37, 3, dark, None)                        # roof
    R(73, 8, 13, 11, dark, 'steel', 1.0)               # cab window
    R(14, 29, 14, 6, dark, 'steel', 1.0)               # cylinder
    if plate:
        R(46, 14, 15, 7, plate, dark, 1.0)
    for cxu in (30, 46, 62):
        wheel(S, X(cxu), y + 38 * s, 15 * s, rim='steel', fill=dark, spokes=False)
    line(S, X(30), y + 38 * s, X(62), y + 38 * s, 'steel', 2)
    wheel(S, X(14), y + 41 * s, 9 * s, rim='steel', fill=dark, spokes=False)
    if tender:
        R(98, 29, 49, 6, 'panel_alt', 'steel', 1.0)
        R(100, 14, 46, 16, 'wagon', dark, 1.0, rad=2)
        R(102, 8, 42, 7, dark, 'steel', 1.0)           # coal
        for cxu in (110, 135):
            wheel(S, X(cxu), y + 40 * s, 11 * s, rim='steel', fill=dark, spokes=False)
    return 0.46 * w * (100.0 / total_u)  # nominal height


def coach(S, x, y, w, body='purple', windows=5):
    """Side-view coach, height = w * 0.30."""
    h = w * 0.30
    rrect(S, x, y, w, h * 0.78, body, 'coal', lw=1.0, radius=0.08)
    ww = w * 0.9 / windows
    for i in range(windows):
        rrect(S, x + w * 0.05 + i * ww + ww * 0.12, y + h * 0.15, ww * 0.72, h * 0.28, 'coal', 'steel',
              lw=0.75, radius=0.03)
    rect(S, x + w * 0.02, y + h * 0.80, w * 0.96, h * 0.06, 'panel_alt', 'steel', lw=0.75)
    for cx in (x + w * 0.16, x + w * 0.84):
        wheel(S, cx, y + h * 0.92, h * 0.24, spokes=False)
    return h


def wagon(S, x, y, w, body='wagon'):
    h = w * 0.34
    rect(S, x, y, w, h * 0.78, body, 'coal', lw=1.0)
    rect(S, x, y + h * 0.80, w, h * 0.06, 'panel_alt', 'steel', lw=0.75)
    for cx in (x + w * 0.18, x + w * 0.82):
        wheel(S, cx, y + h * 0.93, h * 0.24, spokes=False)
    return h


def semaphore(S, x, y_top, h=1.1, state='stop', scale=1.0, lamp=True):
    """Signal post with arm. x = centre of post. STOP flat; CLEAR raised 45 deg."""
    pw = 0.12 * scale
    rect(S, x - pw / 2, y_top, pw, h, 'white', None)
    L, ah = 0.7 * scale, 0.14 * scale
    py = y_top + 0.10 * scale
    pivot_x = x + pw / 2
    if state == 'stop':
        rect(S, pivot_x, py - ah / 2, L, ah, 'red', 'white', lw=1.0)
        rect(S, pivot_x + L * 0.62, py - ah / 2, L * 0.12, ah, 'white', None)
    else:
        import math
        th = math.radians(45)
        cx = pivot_x + (L / 2) * math.cos(th)
        cy = py - (L / 2) * math.sin(th)
        rect(S, cx - L / 2, cy - ah / 2, L, ah, 'red', 'white', lw=1.0, rot=-45)
    if lamp:
        circle(S, x - pw / 2 - 0.12 * scale, py, 0.14 * scale, 'red' if state == 'stop' else 'green', 'white', lw=1.0)


def padlock(S, cx, cy, size=1.0, body='amber'):
    sw = size * 0.55
    rrect(S, cx - sw / 2, cy - size * 0.62, sw, size * 0.8, None, 'steel', lw=7, radius=sw / 2)
    rrect(S, cx - size * 0.5, cy - size * 0.08, size, size * 0.72, body, 'dark', lw=2, radius=size * 0.1)
    circle(S, cx, cy + size * 0.20, size * 0.16, 'dark')
    rect(S, cx - size * 0.035, cy + size * 0.22, size * 0.07, size * 0.2, 'dark')


def price_tag(S, x, y, w, h, fill='amber'):
    """Blank price tag (no price shown): pentagon-ish tag with a hole."""
    poly(S, [(x + h * 0.45, y), (x + w, y), (x + w, y + h), (x + h * 0.45, y + h), (x, y + h / 2)],
         fill=fill, line_c='dark', lw=1.5)
    circle(S, x + h * 0.42, y + h / 2, h * 0.16, 'bg', 'dark', lw=1.25)
    line(S, x + w * 0.45, y + h * 0.3, x + w * 0.85, y + h * 0.3, 'dark', 2)
    line(S, x + w * 0.45, y + h * 0.7, x + w * 0.75, y + h * 0.7, 'dark', 2)


def cross_over(S, x, y, w, h, color='red', lw=7, alpha=0.85, pad=0.0):
    line(S, x + pad, y + pad, x + w - pad, y + h - pad, color, lw, line_alpha=alpha, name='Cross')
    line(S, x + w - pad, y + pad, x + pad, y + h - pad, color, lw, line_alpha=alpha, name='Cross')


def x_badge(S, cx, cy, d=0.42, fill='red'):
    circle(S, cx, cy, d, fill, None)
    r = d * 0.24
    line(S, cx - r, cy - r, cx + r, cy + r, 'white', 3)
    line(S, cx - r, cy + r, cx + r, cy - r, 'white', 3)


def flame(S, cx, base_y, size=1.0):
    """Orange flame from teardrops, rotated so the point faces up."""
    shape(S, MSO_SHAPE.TEAR, cx - size * 0.35, base_y - size * 0.95, size * 0.7, size * 0.7,
          'orange', None, rot=-45)
    shape(S, MSO_SHAPE.TEAR, cx - size * 0.2, base_y - size * 0.70, size * 0.4, size * 0.4,
          'amber', None, rot=-45)


def coal_lumps(S, cx, y, w, n=5):
    xs = [(-0.34, 0.0), (-0.12, -0.05), (0.12, 0.0), (0.32, -0.02), (0.0, 0.07)][:n]
    for dx, dy in xs:
        shape(S, MSO_SHAPE.OVAL, cx + dx * w - w * 0.12, y + dy * w, w * 0.26, w * 0.2,
              'coal', 'steel', lw=1.0)


def top_track(S, x1, x2, y, color_rail='steel', bed=True):
    """Top-down plan of one track: sleeper band and two rails. y = centre line."""
    if bed:
        line(S, x1, y, x2, y, 'sleeper', 9, dash=MSO_LINE.SQUARE_DOT)
    line(S, x1, y - 0.045, x2, y - 0.045, color_rail, 2)
    line(S, x1, y + 0.045, x2, y + 0.045, color_rail, 2)


def top_train(S, x, y, n=2, body='orange', scale=1.0, face='left'):
    """Top-down loco and wagons. y = centre of the track. Faces left (loco leftmost)."""
    lw_, lh = 0.8 * scale, 0.26 * scale
    ww, wh = 0.55 * scale, 0.24 * scale
    gap = 0.05 * scale
    rrect(S, x, y - lh / 2, lw_, lh, body, 'coal', lw=1.0, radius=0.06 * scale)
    circle(S, x + 0.13 * scale, y, 0.09 * scale, 'coal')
    rect(S, x + lw_ * 0.62, y - lh * 0.4, lw_ * 0.3, lh * 0.8, 'coal', None)
    cx = x + lw_ + gap
    for _ in range(n):
        rect(S, cx, y - wh / 2, ww, wh, 'wagon', 'coal', lw=1.0)
        cx += ww + gap
    return cx - x


def panel(S, x, y, w, h, fill='panel', line_c=None, radius=0.08, **kw):
    return rrect(S, x, y, w, h, fill, line_c, radius=radius, **kw)


def checkmark(S, cx, cy, d=0.34, fill='green'):
    circle(S, cx, cy, d, fill, None)
    poly(S, [(cx - d * 0.24, cy), (cx - d * 0.05, cy + d * 0.2), (cx + d * 0.27, cy - d * 0.2)],
         closed=False, line_c='dark', lw=3)


def save(prs, path):
    prs.save(path)
