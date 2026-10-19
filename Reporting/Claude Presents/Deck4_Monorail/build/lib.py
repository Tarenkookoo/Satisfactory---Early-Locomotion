"""Shape library for Deck 4 ("The Monorail Transition, Explained").

Every helper takes `sh`, a shapes collection (slide.shapes or group.shapes), so the
same call works on a slide or inside a group. Sizes are in inches, canvas 13.333 x 7.5.
Colours and sizes come from the style tokens in OUTLINE.md.
"""
import math
import os
import re

from lxml import etree
from PIL import Image, ImageFont
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.dml import MSO_LINE, MSO_PATTERN
from pptx.enum.lang import MSO_LANGUAGE_ID
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, MSO_AUTO_SIZE, PP_ALIGN
from pptx.opc.constants import RELATIONSHIP_TYPE as RT
from pptx.oxml.ns import qn
from pptx.util import Emu, Inches, Pt

HERE = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.abspath(os.path.join(HERE, "..", "..", "images"))

# --- style tokens (OUTLINE.md) -------------------------------------------
BG = "#1E2126"
PANEL = "#2B2F36"
PANEL_ALT = "#343A43"
LINE = "#4A515B"
TEXT = "#F2F2F2"
MUTED = "#A9B0B8"
ORANGE = "#F28C28"
RED = "#E5484D"
GREEN = "#3FB950"
AMBER = "#F2C14E"
WATER = "#4DA3FF"
ELEC = "#6CA0DC"
COAL = "#1B1D21"
COAL_LINE = "#6B7078"
STEEL = "#9AA0A6"
SLEEPER = "#6B5B4B"
PURPLE = "#B084F5"
DARK = "#101418"  # text on bright fills
WAGON = "#6C7480"
LIGHT = "#E8E8E8"

# kind -> (fill, text colour, outline colour)
CHIPS = {
    "Agreed": (GREEN, DARK, None),
    "Proposed": (PURPLE, DARK, None),
    "Provisional": (WATER, DARK, None),
    "Undecided": (None, TEXT, MUTED),
    "Background": (LINE, TEXT, None),
}

FONT = "Arial"
FONT_R = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
FONT_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
_fcache = {}

SLIDE_W = 13.333
SLIDE_H = 7.5
MARGIN = 0.6
RIGHT = SLIDE_W - MARGIN  # 12.733


def rgb(h):
    h = h.lstrip("#")
    return RGBColor(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


def I(v):
    return Inches(v)


# --- text measuring (Liberation Sans has Arial metrics) ----------------------
def text_w(s, size, bold=False):
    if bold not in _fcache:
        _fcache[bold] = ImageFont.truetype(FONT_B if bold else FONT_R, 200)
    return _fcache[bold].getlength(s) * size / 200.0 / 72.0


def wrap_count(s, size, width, bold=False):
    """Number of lines `s` takes at `size` pt in `width` inches."""
    lines = 0
    for para in s.split("\n"):
        cur = ""
        n = 1
        for w in para.split(" "):
            t = (cur + " " + w).strip()
            if text_w(t, size, bold) <= width or not cur:
                cur = t
            else:
                n += 1
                cur = w
        lines += n
    return lines


# --- deck ----------------------------------------------------------------------
def new_deck(title, subject=""):
    prs = Presentation()
    prs.slide_width = Emu(12192000)
    prs.slide_height = Emu(6858000)
    cp = prs.core_properties
    cp.title = title
    cp.author = "Claude (Early Locomotion project)"
    cp.last_modified_by = "Claude (Early Locomotion project)"
    cp.language = "en-GB"
    cp.subject = subject
    cp.keywords = "Satisfactory; Early Locomotion; steam; monorail; transition"
    master = prs.slide_masters[0]
    theme_part = master.part.part_related_by(RT.THEME)
    xml = theme_part.blob.decode("utf8")
    xml = re.sub(r'(<a:(?:major|minor)Font>\s*<a:latin typeface=")[^"]*(")', r"\1Arial\2", xml)
    xml = re.sub(r'(<a:hlink>\s*<a:srgbClr val=")[0-9A-Fa-f]{6}(")', r"\g<1>8FC7FF\2", xml)
    xml = re.sub(r'(<a:folHlink>\s*<a:srgbClr val=")[0-9A-Fa-f]{6}(")', r"\g<1>C9B2F5\2", xml)
    theme_part._blob = xml.encode("utf8")
    return prs


def new_slide(prs, title, chip_kind=None, title_size=36, title_box=None):
    """Title Only layout: real title placeholder first, then the status chip (reading order)."""
    s = prs.slides.add_slide(prs.slide_layouts[5])
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = rgb(BG)
    t = s.shapes.title
    bx = title_box or (MARGIN, 0.4, 10.2, 0.8)
    t.left, t.top, t.width, t.height = I(bx[0]), I(bx[1]), I(bx[2]), I(bx[3])
    t.name = "TITLE"
    tf = t.text_frame
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.NONE
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.LEFT
    r = p.add_run()
    r.text = title
    _font(r, title_size, TEXT, True)
    if chip_kind:
        chip(s.shapes, chip_kind, RIGHT - 1.7, 0.6, 1.7, 0.4, 14, name="CHIP")
    return s


def finish(slide, caption, n):
    """Caption bar (20 pt) then the slide number: added last so they read last."""
    sh = slide.shapes
    bar_y, bar_h = 6.3, 0.8
    rect(sh, MARGIN, bar_y, 12.13, bar_h, PANEL, None, radius=0.08, name="CAPTION BAR")
    rect(sh, MARGIN, bar_y + 0.06, 0.08, bar_h - 0.12, ORANGE, None, name="CAPTION RULE")
    tb = label(sh, 0.85, bar_y, 11.75, bar_h, caption, 20, TEXT, align="l", anchor="m", name="CAPTION",
               spacing=0.95)
    if n is not None:
        label(sh, RIGHT - 1.0, 7.14, 1.0, 0.3, str(n), 14, MUTED, align="r", name="NUM")
    return tb


# --- low-level styling -----------------------------------------------------------
def _font(run, size, color, bold=False, italic=False):
    f = run.font
    f.name = FONT
    f.size = Pt(size)
    f.bold = bold
    f.italic = italic
    f.color.rgb = rgb(color)
    f.language_id = MSO_LANGUAGE_ID.ENGLISH_UK


def _strip_style(shape):
    el = shape._element
    for st in el.findall(qn("p:style")):
        el.remove(st)


def _set_alpha(fill_parent_elm, alpha):
    clr = fill_parent_elm.find(".//" + qn("a:srgbClr"))
    if clr is not None:
        for a in clr.findall(qn("a:alpha")):
            clr.remove(a)
        a = etree.SubElement(clr, qn("a:alpha"))
        a.set("val", str(int(alpha * 100000)))


def style(shape, fill=None, line=None, lw=1.5, dash=None, alpha=None):
    _strip_style(shape)
    if fill is None:
        shape.fill.background()
    else:
        shape.fill.solid()
        shape.fill.fore_color.rgb = rgb(fill)
        if alpha is not None:
            _set_alpha(shape._element.spPr.find(qn("a:solidFill")), alpha)
    if line is None:
        shape.line.fill.background()
    else:
        shape.line.color.rgb = rgb(line)
        shape.line.width = Pt(lw)
        if dash:
            shape.line.dash_style = dash


def set_alt(shape, descr, name=None):
    el = shape._element
    found = el.xpath(
        "./p:nvSpPr/p:cNvPr | ./p:nvGrpSpPr/p:cNvPr | ./p:nvPicPr/p:cNvPr | "
        "./p:nvCxnSpPr/p:cNvPr | ./p:nvGraphicFramePr/p:cNvPr"
    )
    c = found[0]
    c.set("descr", descr)
    if name:
        c.set("name", name)


def _fill_tf(tf, text, size, color, bold, align, anchor, margins, spacing=None):
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.NONE
    tf.vertical_anchor = {"t": MSO_ANCHOR.TOP, "m": MSO_ANCHOR.MIDDLE, "b": MSO_ANCHOR.BOTTOM}[anchor]
    tf.margin_left, tf.margin_top, tf.margin_right, tf.margin_bottom = [I(m) for m in margins]
    paras = text if isinstance(text, list) else [text]
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = {"l": PP_ALIGN.LEFT, "c": PP_ALIGN.CENTER, "r": PP_ALIGN.RIGHT}[align]
        if spacing:
            p.line_spacing = spacing
        runs = para if isinstance(para, list) else [para]
        for rn in runs:
            t, o = (rn if isinstance(rn, tuple) else (rn, {}))
            r = p.add_run()
            r.text = t
            _font(r, o.get("size", size), o.get("color", color), o.get("bold", bold), o.get("italic", False))
            if o.get("link"):
                r.hyperlink.address = o["link"]


# --- primitives --------------------------------------------------------------------
def rect(sh, x, y, w, h, fill=None, line=None, lw=1.5, radius=None, dash=None, alpha=None, name=None,
         text=None, size=14, color=TEXT, bold=False, align="c", anchor="m", margins=(0.06, 0.03, 0.06, 0.03)):
    shp = sh.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE, I(x), I(y), I(w), I(h))
    if radius:
        shp.adjustments[0] = min(0.5, radius / min(w, h))
    style(shp, fill, line, lw, dash, alpha)
    if name:
        shp.name = name
    if text is not None:
        _fill_tf(shp.text_frame, text, size, color, bold, align, anchor, margins)
    return shp


def hatch(sh, x, y, w, h, fore, back, line=None, lw=1.5, dash=None, radius=None, name=None,
          pattern=MSO_PATTERN.WIDE_UPWARD_DIAGONAL):
    """Rectangle with a diagonal hatch pattern fill."""
    shp = sh.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE, I(x), I(y), I(w), I(h))
    if radius:
        shp.adjustments[0] = min(0.5, radius / min(w, h))
    _strip_style(shp)
    shp.fill.patterned()
    shp.fill.pattern = pattern
    shp.fill.fore_color.rgb = rgb(fore)
    shp.fill.back_color.rgb = rgb(back)
    if line is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = rgb(line)
        shp.line.width = Pt(lw)
        if dash:
            shp.line.dash_style = dash
    if name:
        shp.name = name
    return shp


def oval(sh, x, y, w, h, fill=None, line=None, lw=1.5, alpha=None, name=None, text=None, size=14, color=TEXT,
         bold=False, dash=None):
    shp = sh.add_shape(MSO_SHAPE.OVAL, I(x), I(y), I(w), I(h))
    style(shp, fill, line, lw, dash, alpha)
    if name:
        shp.name = name
    if text is not None:
        _fill_tf(shp.text_frame, text, size, color, bold, "c", "m", (0, 0, 0, 0))
    return shp


def label(sh, x, y, w, h, text, size=14, color=TEXT, bold=False, align="c", anchor="m", name=None,
          margins=(0.02, 0.01, 0.02, 0.01), spacing=None):
    tb = sh.add_textbox(I(x), I(y), I(w), I(h))
    _fill_tf(tb.text_frame, text, size, color, bold, align, anchor, margins, spacing)
    if name:
        tb.name = name
    return tb


def poly(sh, pts, fill=None, line=None, lw=1.5, closed=True, alpha=None, name=None, dash=None):
    """Freeform polygon / polyline through `pts` (inches)."""
    e = [(int(Inches(px)), int(Inches(py))) for px, py in pts]
    fb = sh.build_freeform(e[0][0], e[0][1], scale=1.0)
    fb.add_line_segments(e[1:], close=closed)
    shp = fb.convert_to_shape()
    style(shp, fill, line, lw, dash, alpha)
    if name:
        shp.name = name
    return shp


def _ends(conn, head, tail):
    ln = conn.line._get_or_add_ln()
    for tag, on in (("a:headEnd", head), ("a:tailEnd", tail)):
        if on:
            e = etree.SubElement(ln, qn(tag))
            e.set("type", "triangle")
            e.set("w", "med")
            e.set("len", "med")


def line(sh, x1, y1, x2, y2, color=STEEL, w=2.25, dash=None, head=False, tail=False, name=None):
    c = sh.add_connector(MSO_CONNECTOR.STRAIGHT, I(x1), I(y1), I(x2), I(y2))
    _strip_style(c)
    c.line.color.rgb = rgb(color)
    c.line.width = Pt(w)
    if dash:
        c.line.dash_style = dash
    _ends(c, head, tail)
    if name:
        c.name = name
    return c


def arrow(sh, x1, y1, x2, y2, color=ORANGE, w=2.25, dash=None, name=None):
    return line(sh, x1, y1, x2, y2, color, w, dash, False, True, name)


def darrow(sh, x1, y1, x2, y2, color=ORANGE, w=2.25, dash=None, name=None):
    return line(sh, x1, y1, x2, y2, color, w, dash, True, True, name)


def curve(sh, p0, p1, p2, color=ORANGE, w=2.25, n=28, head=True, dash=None, name=None):
    """Quadratic Bezier polyline p0 -> p2 bending towards p1, optional arrow head at the end."""
    pts = []
    for i in range(n + 1):
        t = i / n
        pts.append(((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0],
                    (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]))
    shp = poly(sh, pts, None, color, w, closed=False, name=name, dash=dash)
    if head:
        _ends(shp, False, True)
    return shp


def group(sh, name, alt):
    g = sh.add_group_shape()
    g.name = name
    set_alt(g, alt, name)
    return g


# --- chips ------------------------------------------------------------------------------
def chip(sh, kind, x, y, w=None, h=0.4, size=14, name="CHIP", text=None):
    fill, tcol, outline = CHIPS[kind]
    txt = text or kind.upper()
    if w is None:
        w = text_w(txt, size, True) + 0.5
    shp = rect(sh, x, y, w, h, fill, outline, lw=2, radius=h / 2, name=name, text=txt, size=size, color=tcol,
               bold=True, margins=(0.04, 0.0, 0.04, 0.0))
    return shp


def inline_chip(sh, kind, x, y, h=0.34, size=14, name="ICHIP"):
    return chip(sh, kind, x, y, None, h, size, name)


def chip_w(kind, size=14):
    return text_w(kind.upper(), size, True) + 0.5


# --- pictures ---------------------------------------------------------------------------
def picture(sh, key_file, x, y, w, h, alt, focus=(0.5, 0.5), radius=0.08, name=None):
    """Picture filling a w x h box: cropped, never stretched. `focus` = crop centre (0..1)."""
    path = os.path.join(IMG_DIR, key_file)
    iw, ih = Image.open(path).size
    box = w / h
    img = iw / ih
    pic = sh.add_picture(path, I(x), I(y), I(w), I(h))
    if img > box:  # too wide: crop sides
        keep = box / img
        left = min(max(focus[0] - keep / 2, 0), 1 - keep)
        pic.crop_left, pic.crop_right = left, 1 - keep - left
    else:  # too tall: crop top and bottom
        keep = img / box
        top = min(max(focus[1] - keep / 2, 0), 1 - keep)
        pic.crop_top, pic.crop_bottom = top, 1 - keep - top
    if radius:
        pic.auto_shape_type = MSO_SHAPE.ROUNDED_RECTANGLE
        geom = pic._element.spPr.find(qn("a:prstGeom"))
        av = geom.find(qn("a:avLst"))
        if av is None:
            av = etree.SubElement(geom, qn("a:avLst"))
        for g in list(av):
            av.remove(g)
        gd = etree.SubElement(av, qn("a:gd"))
        gd.set("name", "adj")
        gd.set("fmla", "val %d" % int(radius / min(w, h) * 100000))
    set_alt(pic, alt, name or "PICTURE")
    return pic


def credit(sh, x, y, w, text, align="l", h=0.22, name="CREDIT"):
    return label(sh, x, y, w, h, text, 10, MUTED, align=align, anchor="t", name=name, margins=(0, 0, 0, 0))


# --- icons --------------------------------------------------------------------------------
def tick(sh, cx, cy, d=0.5, name="TICK"):
    g = sh.add_group_shape()
    g.name = name
    oval(g.shapes, cx - d / 2, cy - d / 2, d, d, GREEN, None)
    poly(g.shapes, [(cx - d * 0.24, cy + d * 0.0), (cx - d * 0.07, cy + d * 0.2), (cx + d * 0.26, cy - d * 0.18)],
         None, DARK, 3.5, closed=False)
    set_alt(g, "Green tick", name)
    return g


def cross(sh, cx, cy, s=0.5, color=RED, w=5, name="CROSS"):
    g = sh.add_group_shape()
    g.name = name
    h = s / 2
    line(g.shapes, cx - h, cy - h, cx + h, cy + h, color, w)
    line(g.shapes, cx - h, cy + h, cx + h, cy - h, color, w)
    set_alt(g, "Red cross", name)
    return g


def qbadge(sh, cx, cy, d=0.5, size=22, fill=None, name="QBADGE"):
    return oval(sh, cx - d / 2, cy - d / 2, d, d, fill, MUTED, 2, name=name, text="?", size=size, color=TEXT,
                bold=True)


def num_badge(sh, cx, cy, n, d=0.46, size=16):
    return oval(sh, cx - d / 2, cy - d / 2, d, d, ORANGE, None, name="BADGE", text=str(n), size=size, color=DARK,
                bold=True)


def cursor(sh, x, y, s=1.0, name="CURSOR"):
    """Mouse pointer; (x, y) is the tip."""
    pts = [(0, 0), (0, 0.78), (0.19, 0.62), (0.32, 0.92), (0.44, 0.87), (0.32, 0.58), (0.56, 0.58)]
    p = poly(sh, [(x + a * s, y + b * s) for a, b in pts], TEXT, DARK, 1.5, name=name)
    return p


def warning_triangle(sh, x, y, w=0.7, h=0.62, fill=AMBER, edge=DARK, bang=DARK, name="WARNING"):
    g = sh.add_group_shape()
    g.name = name
    poly(g.shapes, [(x + w / 2, y), (x + w, y + h), (x, y + h)], fill, edge, 2)
    label(g.shapes, x, y + h * 0.3, w, h * 0.7, "!", 26, bang, True, anchor="m", margins=(0, 0, 0, 0))
    set_alt(g, "Warning triangle", name)
    return g


def wheel(sh, cx, cy, r, color=STEEL, hub=None, lw=None, spokes=6):
    """Side-view spoked wheel."""
    lw = lw or max(2.0, r * 8)
    oval(sh, cx - r, cy - r, 2 * r, 2 * r, None, color, lw)
    for i in range(spokes):
        a = math.pi * i / spokes
        line(sh, cx - math.cos(a) * r * 0.9, cy - math.sin(a) * r * 0.9, cx + math.cos(a) * r * 0.9,
             cy + math.sin(a) * r * 0.9, color, max(1.5, r * 3))
    hr = r * 0.22
    oval(sh, cx - hr, cy - hr, 2 * hr, 2 * hr, hub or color, None)


# --- railway objects (top-down and side) ----------------------------------------------------
def rails_h(sh, x, y, length, color=STEEL, gap=0.26, sleepers=True, step=0.35, rw=0.06):
    """Top-down horizontal track: two rails at y and y+gap, sleepers between."""
    if sleepers:
        sx = x + 0.1
        while sx < x + length - 0.03:
            rect(sh, sx, y - 0.07, 0.06, gap + 0.14 + rw, SLEEPER, None)
            sx += step
    rect(sh, x, y, length, rw, color, None)
    rect(sh, x, y + gap, length, rw, color, None)


def loco_side(sh, x, y, w=1.7, color=ORANGE, facing="right"):
    """Generic orange tank-style engine silhouette, side view. (x, y) = top-left, height = 0.62 * w / 1.7 * ... ."""
    k = w / 1.7
    h = 0.95 * k
    body_y = y + 0.28 * k
    flip = facing == "left"

    def X(a, wd=0.0):
        return x + (w - a - wd) if flip else x + a

    # boiler / tank
    rect(sh, X(0.55, 1.05 * k), body_y + 0.05 * k, 1.05 * k, 0.45 * k, color, None, radius=0.08 * k)
    # cab
    rect(sh, X(0.0, 0.5 * k), y + 0.02 * k, 0.5 * k, 0.78 * k, color, None, radius=0.05 * k)
    rect(sh, X(0.08 * k, 0.3 * k), y + 0.12 * k, 0.3 * k, 0.26 * k, COAL, None)
    # chimney and dome
    rect(sh, X(1.4 * k, 0.16 * k), y + 0.02 * k, 0.16 * k, 0.34 * k, COAL, None)
    oval(sh, X(0.85 * k, 0.26 * k), body_y - 0.06 * k, 0.26 * k, 0.2 * k, color, None)
    # frame and wheels
    rect(sh, x, y + 0.72 * k, w, 0.09 * k, COAL, None)
    for wx in (0.38, 0.78, 1.18):
        oval(sh, X(wx * k, 0.34 * k), y + 0.62 * k, 0.34 * k, 0.34 * k, DARK, STEEL, 1.5)
    return h


def wagon_side(sh, x, y, w=1.3, color=WAGON, h=None):
    h = h or 0.5
    rect(sh, x, y, w, h * 0.8, color, None, radius=0.04)
    rect(sh, x - 0.03, y + h * 0.8, w + 0.06, 0.06, COAL, None)
    for wx in (0.2, w - 0.45):
        oval(sh, x + wx, y + h * 0.7, 0.25, 0.25, DARK, STEEL, 1.5)


def carriage_side(sh, x, y, w=2.0, color=ELEC):
    """Electric carriage, side view, wrapped round a beam below it."""
    h = 0.62
    rect(sh, x, y, w, h, color, None, radius=0.16)
    n = 4
    ww = (w - 0.3) / n
    for i in range(n):
        rect(sh, x + 0.15 + i * ww + 0.04, y + 0.12, ww - 0.08, 0.22, BG, None, radius=0.04)
    return h


# --- table (credits) --------------------------------------------------------------------------
def _cell_border(cell, color, w_pt=0.75):
    tcPr = cell._tc.get_or_add_tcPr()
    for tag in ("a:lnL", "a:lnR", "a:lnT", "a:lnB"):
        for old in tcPr.findall(qn(tag)):
            tcPr.remove(old)
        ln = etree.SubElement(tcPr, qn(tag))
        ln.set("w", str(int(w_pt * 12700)))
        sf = etree.SubElement(ln, qn("a:solidFill"))
        c = etree.SubElement(sf, qn("a:srgbClr"))
        c.set("val", color.lstrip("#"))
    # borders must come before the fill in tcPr: move any fill to the end
    for f in tcPr.findall(qn("a:solidFill")):
        tcPr.remove(f)
        tcPr.append(f)


def table(sh, x, y, col_w, rows, size=11, header_fill=PANEL_ALT, row_h=0.42, header=True, alt=""):
    """rows: list of lists of strings (or (text, opts) tuples). Returns the graphic frame."""
    nr, nc = len(rows), len(col_w)
    gf = sh.add_table(nr, nc, I(x), I(y), I(sum(col_w)), I(row_h * nr))
    tbl = gf.table
    tblPr = tbl._tbl.tblPr
    for a in ("bandRow", "firstRow"):
        if a in tblPr.attrib:
            del tblPr.attrib[a]
    for sid in tblPr.findall(qn("a:tableStyleId")):
        tblPr.remove(sid)
    for i, wd in enumerate(col_w):
        tbl.columns[i].width = I(wd)
    for r in range(nr):
        tbl.rows[r].height = I(row_h)
        for c in range(nc):
            cell = tbl.cell(r, c)
            val = rows[r][c]
            txt, o = (val if isinstance(val, tuple) else (val, {}))
            is_head = header and r == 0
            cell.fill.solid()
            cell.fill.fore_color.rgb = rgb(header_fill if is_head else (PANEL if r % 2 else BG))
            cell.margin_left = cell.margin_right = I(0.1)
            cell.margin_top = cell.margin_bottom = I(0.04)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            tf = cell.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            run = p.add_run()
            run.text = txt
            _font(run, size, o.get("color", TEXT), o.get("bold", is_head))
            _cell_border(cell, LINE)
    set_alt(gf, alt or "Table", "CREDITS TABLE")
    return gf


# --- shared composites ----------------------------------------------------------------------
def note_strip(sh, kind, text, y, h=0.65, size=20, name="NOTE"):
    """Panel strip with an inline status chip at the left and a one-line note."""
    g = sh.add_group_shape()
    g.name = name
    set_alt(g, "Note: %s (%s)." % (text, kind), name)
    rect(g.shapes, MARGIN, y, 12.13, h, PANEL, None, radius=0.08)
    chip(g.shapes, kind, 0.85, y + (h - 0.34) / 2, None, 0.34, 14, name="ICHIP")
    label(g.shapes, 0.85 + chip_w(kind) + 0.25, y, 12.13 - chip_w(kind) - 0.9, h, text, size, TEXT, align="l")
    return g


def path_pts(x0, x1, y_fn, n=80):
    return [(x0 + (x1 - x0) * i / n, y_fn(x0 + (x1 - x0) * i / n)) for i in range(n + 1)]


def offset_pts(pts, d):
    out = []
    for i, (x, y) in enumerate(pts):
        a = pts[max(i - 1, 0)]
        b = pts[min(i + 1, len(pts) - 1)]
        dx, dy = b[0] - a[0], b[1] - a[1]
        n = math.hypot(dx, dy)
        out.append((x - dy / n * d, y + dx / n * d))
    return out


def arc(sh, cx, cy, r, a0, a1, color=ORANGE, w=3.5, head=True, n=36, name=None):
    """Circular arc from angle a0 to a1 (degrees, counter-clockwise on screen), optional arrow head at the end."""
    pts = []
    for i in range(n + 1):
        a = math.radians(a0 + (a1 - a0) * i / n)
        pts.append((cx + r * math.cos(a), cy - r * math.sin(a)))
    shp = poly(sh, pts, None, color, w, closed=False, name=name)
    if head:
        _ends(shp, False, True)
    return shp


def note_strip_at(sh, kind, text, x, y, w, h=0.65, size=20, name="NOTE"):
    """Like note_strip, but with an explicit x and width."""
    g = sh.add_group_shape()
    g.name = name
    set_alt(g, "Note: %s (%s)." % (text, kind), name)
    rect(g.shapes, x, y, w, h, PANEL, None, radius=0.08)
    chip(g.shapes, kind, x + 0.25, y + (h - 0.34) / 2, None, 0.34, 14, name="ICHIP")
    label(g.shapes, x + 0.25 + chip_w(kind) + 0.25, y, w - chip_w(kind) - 0.8, h, text, size, TEXT, align="l")
    return g
