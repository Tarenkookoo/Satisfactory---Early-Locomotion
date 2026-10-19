"""Shape library for Deck 5 ("Regions, Running Numbers and Fleet Identity, Explained").

Modelled on the accepted Deck 3 library (same style tokens from OUTLINE.md). All helpers take `sh`,
a shapes collection (slide.shapes or group.shapes), so the same call works on a slide or inside a
group. Sizes are in inches. Locomotive and wagon drawings are generic silhouettes, not the mod's models.
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
ORANGE_DK = "#C96F1B"
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
DARKMETAL = "#3A3F47"
DARK = "#101418"  # text on bright fills
WAGON = "#6C7480"
# Example style colours for "regional look" illustrations (not chip colours, not a launch list)
STYLE_A = "#2BB5B0"   # teal   - "British" example
STYLE_B = "#D6619B"   # rose   - "North American" example
STYLE_C = "#D9B26F"   # sand   - "Continental European" example / world style example

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


def rgb(h):
    h = h.lstrip("#")
    return RGBColor(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


def I(v):
    return Inches(v)


def shade(h, f):
    """Lighten (f>0) or darken (f<0) a hex colour."""
    h = h.lstrip("#")
    c = [int(h[i:i + 2], 16) for i in (0, 2, 4)]
    if f >= 0:
        c = [int(v + (255 - v) * f) for v in c]
    else:
        c = [int(v * (1 + f)) for v in c]
    return "#%02X%02X%02X" % tuple(c)


# --- text measuring (Liberation Sans has Arial metrics) --------------------
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


def wrap_lines(s, size, width, bold=False):
    out = []
    for para in s.split("\n"):
        cur = ""
        for w in para.split(" "):
            t = (cur + " " + w).strip()
            if text_w(t, size, bold) <= width or not cur:
                cur = t
            else:
                out.append(cur)
                cur = w
        out.append(cur)
    return out


def balanced_width(text, size, max_w, bold=False, min_w=6.0):
    """Widest box (<= max_w) that wraps `text` into two lines whose second line is not an orphan."""
    first = wrap_lines(text, size, max_w, bold)
    if len(first) != 2 or text_w(first[1], size, bold) >= 0.45 * text_w(first[0], size, bold):
        return max_w
    w = max_w
    while w > min_w:
        w = round(w - 0.1, 2)
        ls = wrap_lines(text, size, w, bold)
        if len(ls) != 2:
            break
        if text_w(ls[1], size, bold) >= 0.45 * text_w(ls[0], size, bold):
            return min(max_w, w + 0.3)
    return max_w


# --- deck ------------------------------------------------------------------
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
    cp.keywords = "Satisfactory; Early Locomotion; regions; running numbers; fleet identity"
    master = prs.slide_masters[0]
    theme_part = master.part.part_related_by(RT.THEME)
    xml = theme_part.blob.decode("utf8")
    xml = re.sub(r'(<a:(?:major|minor)Font>\s*<a:latin typeface=")[^"]*(")', r"\1Arial\2", xml)
    xml = re.sub(r'(<a:hlink>\s*<a:srgbClr val=")[0-9A-Fa-f]{6}(")', r"\g<1>8FC7FF\2", xml)
    xml = re.sub(r'(<a:folHlink>\s*<a:srgbClr val=")[0-9A-Fa-f]{6}(")', r"\g<1>C9B2F5\2", xml)
    theme_part._blob = xml.encode("utf8")
    return prs


def new_slide(prs, title, chip_kind=None, title_size=36, title_w=10.2, title_box=None, chip_note=None):
    """Title Only layout: real title placeholder (good for navigation), then the status chip."""
    layout = prs.slide_layouts[5]
    s = prs.slides.add_slide(layout)
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = rgb(BG)
    t = s.shapes.title
    bx = title_box or (0.6, 0.4, title_w, 0.8)
    t.left, t.top, t.width, t.height = I(bx[0]), I(bx[1]), I(bx[2]), I(bx[3])
    t.name = "TITLE"
    tf = t.text_frame
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.NONE
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = tf.margin_right = 0
    tf.margin_top = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.LEFT
    r = p.add_run()
    r.text = title
    _font(r, title_size, TEXT, True)
    if chip_kind:
        chip(s.shapes, chip_kind, 13.333 - 0.6 - 1.7, 0.58, name="CHIP")
        if chip_note:
            label(s.shapes, 13.333 - 0.6 - 2.4, 1.02, 2.4, 0.3, chip_note, 14, MUTED, align="r", name="CHIP NOTE")
    return s


def finish(slide, caption, n):
    """Caption bar (20 pt) and slide number, added last (reading order)."""
    sh = slide.shapes
    bar_y, bar_h = 6.3, 0.8
    rect(sh, 0.6, bar_y, 12.13, bar_h, PANEL, None, radius=0.08, name="CAPTION BAR")
    rect(sh, 0.6, bar_y + 0.06, 0.08, bar_h - 0.12, ORANGE, None, name="CAPTION RULE")
    cw = balanced_width(caption, 20, 11.4)
    tb = label(sh, 0.9, bar_y, cw, bar_h, caption, 20, TEXT, align="l", anchor="m", name="CAPTION")
    if n is not None:
        label(sh, 11.73, 7.14, 1.0, 0.3, str(n), 14, MUTED, align="r", name="NUM")
    return tb


# --- low-level styling ------------------------------------------------------
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
            t, o = rn if isinstance(rn, tuple) else (rn, {})
            r = p.add_run()
            r.text = t
            _font(r, o.get("size", size), o.get("color", color), o.get("bold", bold), o.get("italic", False))
            if o.get("link"):
                r.hyperlink.address = o["link"]


# --- primitives --------------------------------------------------------------
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


def path(sh, pts, color=ORANGE, w=2.25, head=True, dash=None, name=None):
    """Open polyline (elbow arrows)."""
    shp = poly(sh, pts, None, color, w, closed=False, name=name, dash=dash)
    if head:
        _ends(shp, False, True)
    return shp


def curve(sh, p0, p1, p2, color=ORANGE, w=2.25, n=28, head=True, dash=None, name=None):
    """Quadratic Bezier polyline p0 -> p2 bending towards p1, optional arrow head at the end."""
    pts = []
    for i in range(n + 1):
        t = i / n
        pts.append(((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0],
                    (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]))
    return path(sh, pts, color, w, head, dash, name)


def group(sh, name, alt):
    g = sh.add_group_shape()
    g.name = name
    set_alt(g, alt, name)
    return g


# --- chips --------------------------------------------------------------------
def chip(sh, kind, x, y, w=1.7, h=0.4, size=14, text=None, name="CHIP", align="c"):
    fill, tcol, outline = CHIPS[kind]
    t = text if text is not None else kind.upper()
    return rect(sh, x, y, w, h, fill, outline, 2.0, radius=min(0.12, h / 2), name=name, text=t, size=size,
                color=tcol, bold=True, align=align, margins=(0.06, 0.0, 0.06, 0.0))


def ichip(sh, kind, x, y, text, w=None, h=0.34, align="c"):
    """Inline chip carrying its own words (14 pt, per MULTI_DECK_RULES: nothing below 14 pt)."""
    if w is None:
        w = text_w(text, 14, True) + 0.34
    return chip(sh, kind, x, y, w, h, 14, text, name="ICHIP", align=align)


# --- pictures ---------------------------------------------------------------
def add_picture_fit(sh, fname, x, y, w, h, alt, focus=(0.5, 0.5), radius=0.08, name=None):
    """Cover-fit: crops (never stretches) the picture to the box."""
    path_ = os.path.join(IMG_DIR, fname)
    with Image.open(path_) as im:
        iw, ih = im.size
    ar_box, ar_img = w / h, iw / ih
    pic = sh.add_picture(path_, I(x), I(y), I(w), I(h))
    if ar_img > ar_box:
        vis = ar_box / ar_img
        left = (1 - vis) * focus[0]
        pic.crop_left, pic.crop_right = left, 1 - vis - left
    else:
        vis = ar_img / ar_box
        top = (1 - vis) * focus[1]
        pic.crop_top, pic.crop_bottom = top, 1 - vis - top
    if radius:
        geom = pic._element.spPr.find(qn("a:prstGeom"))
        geom.set("prst", "roundRect")
        av = geom.find(qn("a:avLst"))
        if av is None:
            av = etree.SubElement(geom, qn("a:avLst"))
        for g in list(av):
            av.remove(g)
        gd = etree.SubElement(av, qn("a:gd"))
        gd.set("name", "adj")
        gd.set("fmla", "val %d" % int(min(0.5, radius / min(w, h)) * 100000))
    set_alt(pic, alt, name or os.path.splitext(fname)[0])
    return pic


def credit(sh, x, y, w, text, align="l", h=0.24, color=MUTED):
    return label(sh, x, y, w, h, text, 10, color, align=align, anchor="t", name="CREDIT", margins=(0, 0, 0, 0))


# --- tables ----------------------------------------------------------------------
def cell_border(cell, color, w_pt=0.75):
    tcPr = cell._tc.get_or_add_tcPr()
    for tag in ("a:lnL", "a:lnR", "a:lnT", "a:lnB"):
        for old in tcPr.findall(qn(tag)):
            tcPr.remove(old)
    first = tcPr[0] if len(tcPr) else None
    for tag in ("a:lnL", "a:lnR", "a:lnT", "a:lnB"):
        ln = etree.Element(qn(tag))
        ln.set("w", str(int(w_pt * 12700)))
        ln.set("cap", "flat")
        ln.set("cmpd", "sng")
        sf = etree.SubElement(ln, qn("a:solidFill"))
        c = etree.SubElement(sf, qn("a:srgbClr"))
        c.set("val", color.lstrip("#"))
        etree.SubElement(ln, qn("a:prstDash")).set("val", "solid")
        if first is not None:
            first.addprevious(ln)
        else:
            tcPr.append(ln)


def set_cell(cell, text, size, color=TEXT, bold=False, fill=None, align="l", border=LINE,
             margins=(0.08, 0.04, 0.08, 0.04)):
    cell.margin_left, cell.margin_top, cell.margin_right, cell.margin_bottom = [I(m) for m in margins]
    cell.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf = cell.text_frame
    tf.word_wrap = True
    paras = text if isinstance(text, list) else [text]
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = {"l": PP_ALIGN.LEFT, "c": PP_ALIGN.CENTER, "r": PP_ALIGN.RIGHT}[align]
        runs = para if isinstance(para, list) else [para]
        for rn in runs:
            t, o = (rn if isinstance(rn, tuple) else (rn, {}))
            r = p.add_run()
            r.text = t
            _font(r, o.get("size", size), o.get("color", color), o.get("bold", bold))
            if o.get("link"):
                r.hyperlink.address = o["link"]
    if fill:
        cell.fill.solid()
        cell.fill.fore_color.rgb = rgb(fill)
    else:
        cell.fill.background()
    if border:
        cell_border(cell, border)


def add_table(sh, x, y, w, h, rows, cols, col_w, alt, name="TABLE"):
    gf = sh.add_table(rows, cols, I(x), I(y), I(w), I(h))
    tbl = gf.table
    tblPr = tbl._tbl.tblPr
    tblPr.set("firstRow", "1")
    tblPr.set("bandRow", "0")
    for i, cw in enumerate(col_w):
        tbl.columns[i].width = I(cw)
    for r in tbl.rows:
        r.height = I(h / rows)
    set_alt(gf, alt, name)
    return gf, tbl


# --- small icons ---------------------------------------------------------------------
def wheel(sh, cx, cy, d, fill=COAL, rim=STEEL, lw=1.5):
    oval(sh, cx - d / 2, cy - d / 2, d, d, fill, rim, lw, name="wheel")
    oval(sh, cx - d * 0.13, cy - d * 0.13, d * 0.26, d * 0.26, rim, None, name="hub")


def padlock(sh, x, y, s, color=AMBER, body_text_color=DARK, name="padlock"):
    """Padlock whose body is s wide and 0.8 s tall; the shackle rises above (total height 1.35 s)."""
    sw = s * 0.62
    sx = x + (s - sw) / 2
    pts = []
    n = 14
    r = sw / 2
    cx, cy = sx + r, y + 0.55 * s
    pts.append((sx, y + 0.6 * s))
    for i in range(n + 1):
        a = math.pi - math.pi * i / n
        pts.append((cx + r * math.cos(a), cy - r * math.sin(a)))
    pts.append((sx + sw, y + 0.6 * s))
    poly(sh, pts, None, color, max(2.5, s * 5), closed=False, name=name + " shackle")
    rect(sh, x, y + 0.55 * s, s, 0.8 * s, color, None, radius=0.05 * s, name=name + " body")
    oval(sh, x + s * 0.43, y + 0.8 * s, s * 0.14, s * 0.14, body_text_color, None, name=name + " keyhole")
    rect(sh, x + s * 0.47, y + 0.9 * s, s * 0.06, s * 0.2, body_text_color, None, name=name + " keyhole slot")


def magnifier(sh, x, y, s, color=TEXT, lw=3.5, name="magnifier"):
    """Magnifying glass, lens top-left; s = overall size."""
    d = s * 0.66
    oval(sh, x, y, d, d, None, color, lw, name=name + " lens")
    line(sh, x + d * 0.85, y + d * 0.85, x + s, y + s, color, lw * 1.5, name=name + " handle")


def pencil(sh, x, y, s, color=AMBER):
    """Pencil pointing down-left; s = bounding square."""
    u = s
    body = [(x + 0.74 * u, y + 0.0), (x + 1.0 * u, y + 0.26 * u), (x + 0.3 * u, y + 0.96 * u),
            (x + 0.04 * u, y + 0.7 * u)]
    poly(sh, body, color, None, name="pencil body")
    tip = [(x + 0.04 * u, y + 0.7 * u), (x + 0.3 * u, y + 0.96 * u), (x + 0.0, y + 1.0 * u)]
    poly(sh, tip, "#F2F2F2", None, name="pencil tip")


def globe(sh, cx, cy, r, fill="#2D5F8B", rim=STEEL):
    oval(sh, cx - r, cy - r, 2 * r, 2 * r, fill, rim, 2.0, name="globe")
    oval(sh, cx - r * 0.45, cy - r, r * 0.9, 2 * r, None, shade(rim, 0.2), 1.25, name="meridian")
    line(sh, cx, cy - r, cx, cy + r, shade(rim, 0.2), 1.25, name="axis")
    line(sh, cx - r, cy, cx + r, cy, shade(rim, 0.2), 1.25, name="equator")
    # two simple land patches
    poly(sh, [(cx - r * 0.55, cy - r * 0.35), (cx - r * 0.2, cy - r * 0.6), (cx + r * 0.1, cy - r * 0.35),
              (cx - r * 0.1, cy - r * 0.05), (cx - r * 0.5, cy - r * 0.05)], "#4F8F5B", None, name="land")
    poly(sh, [(cx + r * 0.2, cy + r * 0.1), (cx + r * 0.6, cy + r * 0.2), (cx + r * 0.45, cy + r * 0.6),
              (cx + r * 0.15, cy + r * 0.45)], "#4F8F5B", None, name="land")


def monitor(sh, x, y, w, h, bezel=STEEL, screen=BG):
    """Screen with stand. Returns the inner screen rect (x, y, w, h)."""
    rect(sh, x, y, w, h, PANEL_ALT, bezel, 2.5, radius=0.1, name="monitor frame")
    pad = 0.12
    rect(sh, x + pad, y + pad, w - 2 * pad, h - 2 * pad - 0.0, screen, None, radius=0.04, name="screen")
    poly(sh, [(x + w / 2 - 0.3, y + h), (x + w / 2 + 0.3, y + h), (x + w / 2 + 0.45, y + h + 0.28),
              (x + w / 2 - 0.45, y + h + 0.28)], PANEL_ALT, bezel, 2.0, name="monitor stand")
    rect(sh, x + w / 2 - 0.7, y + h + 0.26, 1.4, 0.07, PANEL_ALT, bezel, 1.5, name="monitor base")
    return (x + pad, y + pad, w - 2 * pad, h - 2 * pad)


def cross(sh, cx, cy, d, color=RED, lw=7):
    h = d / 2
    line(sh, cx - h, cy - h, cx + h, cy + h, color, lw, name="cross")
    line(sh, cx - h, cy + h, cx + h, cy - h, color, lw, name="cross")


def tick(sh, cx, cy, d, color=GREEN, lw=6):
    pts = [(cx - d * 0.5, cy), (cx - d * 0.12, cy + d * 0.38), (cx + d * 0.5, cy - d * 0.4)]
    poly(sh, pts, None, color, lw, closed=False, name="tick")


def plate(sh, x, y, w, h, text, size=18, fill=COAL, border=ORANGE, color=TEXT, name="number plate", lw=2.25):
    """Painted number plate. Every invented number shown on one must be labelled 'Example only'."""
    return rect(sh, x, y, w, h, fill, border, lw, radius=min(0.08, h / 3), name=name, text=text, size=size,
                color=color, bold=True, margins=(0.03, 0.0, 0.03, 0.0))


def plate_blank(sh, x, y, w, h, border=ORANGE):
    """Plate outline with three short bars for digits (no invented number)."""
    rect(sh, x, y, w, h, COAL, border, 2.0, radius=min(0.08, h / 3), name="number plate (blank)")
    for k in range(3):
        rect(sh, x + w * (0.2 + k * 0.22), y + h * 0.3, w * 0.14, h * 0.4, MUTED, None, name="digit bar")


def skel(sh, x, y, w, h=0.12, color=LINE, name="skeleton line"):
    return rect(sh, x, y, w, h, color, None, radius=h / 2, name=name)


def pool_box(sh, x, y, w, h, cols, rows, filled, name="pool", empty_hl=None, accent=STEEL):
    """A box of small plate slots. `filled` = number of slots filled (row-major). `empty_hl` = slot index to
    highlight (the empty slot that receives a returning number)."""
    rect(sh, x, y, w, h, PANEL, STEEL, 2.0, radius=0.1, name=name)
    pad = 0.18
    gw = (w - 2 * pad) / cols
    gh = (h - 2 * pad) / rows
    k = 0
    for r in range(rows):
        for c in range(cols):
            sx, sy = x + pad + c * gw + 0.05, y + pad + r * gh + 0.05
            if k < filled:
                rect(sh, sx, sy, gw - 0.1, gh - 0.1, ORANGE_DK, None, radius=0.04, name="slot full")
            elif empty_hl is not None and k == empty_hl:
                rect(sh, sx, sy, gw - 0.1, gh - 0.1, None, AMBER, 2.0, radius=0.04, dash=MSO_LINE.DASH,
                     name="slot free")
            else:
                rect(sh, sx, sy, gw - 0.1, gh - 0.1, None, LINE, 1.25, radius=0.04, name="slot free")
            k += 1


def scale(sh, cx, top, beam_w, color=STEEL, post_h=2.0, ph=1.4, pan_half=1.0):
    """Balance scale, beam level. Returns the top-centre point of each pan: ((lx, y), (rx, y))."""
    by = top + 0.2
    rect(sh, cx - 0.08, by, 0.16, post_h, color, None, name="scale post")
    poly(sh, [(cx - 0.8, by + post_h), (cx + 0.8, by + post_h), (cx + 0.5, by + post_h - 0.28),
              (cx - 0.5, by + post_h - 0.28)], shade(color, -0.25), color, 1.5, name="scale base")
    rect(sh, cx - beam_w / 2, by - 0.06, beam_w, 0.12, color, None, radius=0.05, name="scale beam")
    oval(sh, cx - 0.14, by - 0.14, 0.28, 0.28, AMBER, None, name="scale pivot")
    anchors = []
    for sgn in (-1, 1):
        ex = cx + sgn * (beam_w / 2 - 0.1)
        py = by + ph
        line(sh, ex, by, ex - pan_half * 0.9, py, color, 1.5, name="scale string")
        line(sh, ex, by, ex + pan_half * 0.9, py, color, 1.5, name="scale string")
        poly(sh, [(ex - pan_half, py), (ex + pan_half, py), (ex + pan_half * 0.8, py + 0.16),
                  (ex - pan_half * 0.8, py + 0.16)], shade(color, -0.1), color, 1.5, name="scale pan")
        anchors.append((ex, py))
    return anchors


# --- locomotive and wagon silhouettes ---------------------------------------------
def _R(sh, x, gy, u):
    """Return helpers for ground-up coordinates: a(offset) -> x, hh(height) -> y."""
    return (lambda a: x + a * u), (lambda h: gy - h * u)


def engine(sh, x, gy, u, style="tender", size=2, color=ORANGE, with_tender=True, variant=None):
    """Generic side-view steam locomotive silhouette facing right. (x, gy) = left edge and rail-top line.
    style: 'tank' (British-type tank engine), 'tender' (long boiler with tender), 'american' (tall engine with pilot
    and headlamp), 'euro' (slim chimney, smoke deflectors). size: 1 small, 2 medium, 3 large.
    Returns dict(W, H, plate=(x,y,w,h), left=(x,y), right=(x,y), top)."""
    X, Y = _R(sh, x, gy, u)

    def rc(a, h0, w, h1, fill, line_=None, lw=1.0, radius=None, name="part"):
        return rect(sh, X(a), Y(h1), w * u, (h1 - h0) * u, fill, line_, lw, radius=radius, name=name)

    def wl(a, d, h=None):
        cy = Y(d / 2 if h is None else h)
        wheel(sh, X(a), cy, d * u, COAL, STEEL, 1.5)

    dark = shade(color, -0.28)
    coalc = COAL
    n = {1: 3, 2: 4, 3: 5}[size]
    info = {}
    if style == "tank":
        sp = 2.0
        B = (n - 1) * sp + 2.4
        bunker, cab = 1.7, 2.0
        W = bunker + cab + B + 1.0 + 0.3
        rc(0, 1.0, W - 0.3, 1.45, DARKMETAL, STEEL, 0.75, name="frame")
        rc(0, 1.45, bunker, 3.4, color, None, radius=0.05 * u, name="bunker")
        poly(sh, [(X(0.1), Y(3.4)), (X(0.5), Y(3.85)), (X(1.1), Y(3.9)), (X(1.6), Y(3.4))], coalc, COAL_LINE, 1.0,
             name="bunker coal")
        rc(bunker, 1.45, cab, 4.2, color, None, radius=0.05 * u, name="cab")
        rc(bunker - 0.1, 4.2, cab + 0.2, 4.45, DARKMETAL, STEEL, 0.75, name="cab roof")
        rc(bunker + 0.5, 2.9, 0.9, 3.8, coalc, None, name="cab window")
        bx = bunker + cab
        rc(bx, 1.95, B, 3.95, color, None, radius=0.5 * u, name="boiler")
        rc(bx, 1.5, B - 0.5, 3.25, dark, None, radius=0.25 * u, name="side tank")
        rc(bx + B, 1.95, 1.0, 3.95, "#4A515B", None, radius=0.12 * u, name="smokebox")
        rc(bx + B + 0.2, 3.95, 0.6, 5.0, DARKMETAL, STEEL, 0.75, name="chimney")
        rc(bx + B + 0.05, 4.9, 0.9, 5.15, DARKMETAL, STEEL, 0.75, name="chimney lip")
        rc(bx + B * 0.42, 3.95, 0.9, 4.5, color, None, radius=0.2 * u, name="dome")
        if variant == "euro":
            rc(bx + B + 0.3, 4.9, 0.4, 5.5, DARKMETAL, STEEL, 0.75, name="slim chimney")
            poly(sh, [(X(bx + B - 1.3), Y(3.6)), (X(bx + B - 0.1), Y(3.6)), (X(bx + B - 0.1), Y(5.3)),
                      (X(bx + B - 1.1), Y(5.0))], DARKMETAL, STEEL, 1.0, name="smoke deflector")
            oval(sh, X(W - 0.55), Y(2.2), 0.5 * u, 0.5 * u, AMBER, None, name="lamp")
        info.update(plate=(X(bx + 0.4), Y(3.25), 1.6 * u, 0.7 * u), W=W + 0.0, top=Y(5.5))
        cx0 = W / 2 - (n - 1) * sp / 2
        for i in range(n):
            wl(cx0 + i * sp, 1.8)
        pin = 0.9 + 0.45
        rc(cx0, pin - 0.07, (n - 1) * sp, pin + 0.07, "#D0D4D8", None, name="coupling rod")
        rc(W - 0.3, 1.0, 0.3, 1.9, STEEL, None, name="buffer beam")
    elif style in ("tender", "euro"):
        sp = 2.25
        euro = style == "euro"
        tender_w = 4.1 if with_tender else 0.0
        cab = 2.0
        B = (n - 1) * sp + 3.4
        lead = size >= 2
        W = tender_w + (0.35 if with_tender else 0) + cab + B + 1.0 + 0.3
        e0 = tender_w + (0.35 if with_tender else 0)
        if with_tender:
            rc(0, 1.0, tender_w, 1.45, DARKMETAL, STEEL, 0.75, name="tender frame")
            rc(0, 1.45, tender_w, 3.25 if euro else 3.1, color, None, radius=0.05 * u, name="tender body")
            poly(sh, [(X(0.15), Y(3.1)), (X(0.9), Y(3.75)), (X(2.4), Y(3.8)), (X(tender_w - 0.15), Y(3.1))], coalc,
                 COAL_LINE, 1.0, name="tender coal")
            rc(tender_w, 1.9, 0.35, 2.05, STEEL, None, name="coupling")
            for a in ((0.9, 2.1, 3.3) if euro else (1.0, 3.1)):
                wl(a, 1.4)
        rc(e0, 1.0, W - e0 - 0.3, 1.45, DARKMETAL, STEEL, 0.75, name="frame")
        rc(e0, 1.45, cab, 4.2, color, None, radius=0.05 * u, name="cab")
        if euro:
            rc(e0 - 0.15, 4.2, cab + 0.3, 4.6, DARKMETAL, STEEL, 0.75, radius=0.15 * u, name="cab roof")
        else:
            rc(e0 - 0.1, 4.2, cab + 0.2, 4.45, DARKMETAL, STEEL, 0.75, name="cab roof")
        rc(e0 + 0.5, 2.9, 0.9, 3.8, coalc, None, name="cab window")
        bx = e0 + cab
        rc(bx, 1.95, B, 3.95, color, None, radius=0.5 * u, name="boiler")
        for k in (0.3, 0.55, 0.8):
            rc(bx + B * k, 1.95, 0.07, 3.95, dark, None, name="boiler band")
        rc(bx + B, 1.95, 1.0, 3.95, "#4A515B", None, radius=0.12 * u, name="smokebox")
        if euro:
            rc(bx + B + 0.3, 3.95, 0.4, 5.3, DARKMETAL, STEEL, 0.75, name="chimney")
            poly(sh, [(X(bx + B - 1.3), Y(3.5)), (X(bx + B - 0.1), Y(3.5)), (X(bx + B - 0.1), Y(5.2)),
                      (X(bx + B - 1.1), Y(4.9))], DARKMETAL, STEEL, 1.0, name="smoke deflector")
            oval(sh, X(W - 0.55), Y(2.2), 0.5 * u, 0.5 * u, AMBER, None, name="lamp")
        else:
            rc(bx + B + 0.2, 3.95, 0.6, 5.0, DARKMETAL, STEEL, 0.75, name="chimney")
            rc(bx + B + 0.05, 4.9, 0.9, 5.15, DARKMETAL, STEEL, 0.75, name="chimney lip")
        rc(bx + B * 0.4, 3.95, 0.9, 4.5, color, None, radius=0.2 * u, name="dome")
        cx0 = e0 + 1.15
        for i in range(n):
            wl(cx0 + i * sp, 2.0)
        if lead:
            wl(cx0 + (n - 1) * sp + 2.3, 1.1)
        pin = 1.0 + 0.5
        rc(cx0, pin - 0.07, (n - 1) * sp, pin + 0.07, "#D0D4D8", None, name="coupling rod")
        rc(W - 0.3, 1.0, 0.3, 1.9, STEEL, None, name="buffer beam")
        info.update(plate=(X(bx + 0.3), Y(3.3), 1.6 * u, 0.7 * u), W=W, top=Y(5.3))
        info["tender_plate"] = (X(0.9), Y(2.95), 1.7 * u, 0.7 * u) if with_tender else None
        info["cab_plate"] = (X(e0 + 0.2), Y(4.05), 1.6 * u, 0.7 * u)
    elif style == "american":
        d = {1: 1.7, 2: 1.9, 3: 2.1}[size]
        n = {1: 2, 2: 3, 3: 4}[size]
        sp = d * 1.12
        tender_w = 4.6 if with_tender else 0.0
        cab = 2.3
        B = (n - 1) * sp + 3.2
        W = tender_w + (0.4 if with_tender else 0) + cab + B + 1.2 + 1.5
        e0 = tender_w + (0.4 if with_tender else 0)
        if with_tender:
            rc(0, 1.15, tender_w, 1.6, DARKMETAL, STEEL, 0.75, name="tender frame")
            rc(0, 1.6, tender_w, 3.6, color, None, radius=0.05 * u, name="tender body")
            poly(sh, [(X(0.15), Y(3.6)), (X(0.9), Y(4.2)), (X(2.6), Y(4.25)), (X(tender_w - 0.15), Y(3.6))], coalc,
                 COAL_LINE, 1.0, name="tender coal")
            rc(tender_w, 2.2, 0.4, 2.35, STEEL, None, name="coupling")
            for a in (0.9, 1.9, 2.7, 3.7):
                wl(a, 1.2)
        rc(e0, 1.15, W - e0 - 1.0, 1.6, DARKMETAL, STEEL, 0.75, name="frame")
        rc(e0, 1.6, cab, 5.0, color, None, radius=0.05 * u, name="cab")
        rc(e0 - 0.2, 5.0, cab + 0.4, 5.3, DARKMETAL, STEEL, 0.75, name="cab roof")
        rc(e0 + 0.55, 3.4, 1.0, 4.5, coalc, None, name="cab window")
        bx = e0 + cab
        rc(bx, 2.2, B, 4.7, color, None, radius=0.55 * u, name="boiler")
        rc(bx + B, 2.2, 1.2, 4.7, "#4A515B", None, radius=0.12 * u, name="smokebox")
        poly(sh, [(X(bx + B + 0.35), Y(4.7)), (X(bx + B + 0.35), Y(5.2)), (X(bx + B - 0.05), Y(6.4)),
                  (X(bx + B + 1.15), Y(6.4)), (X(bx + B + 0.75), Y(5.2)), (X(bx + B + 0.75), Y(4.7))],
             DARKMETAL, STEEL, 0.75, name="funnel stack")
        oval(sh, X(bx + B + 0.9), Y(5.5), 0.75 * u, 0.75 * u, AMBER, "#F2F2F2", 1.0, name="headlamp")
        rc(bx + B * 0.28, 4.7, 0.9, 5.3, color, None, radius=0.2 * u, name="sand dome")
        rc(bx + B * 0.62, 4.7, 1.0, 5.4, color, None, radius=0.2 * u, name="steam dome")
        poly(sh, [(X(W - 1.5), Y(1.55)), (X(W), Y(0.45)), (X(W - 1.5), Y(0.45))], DARKMETAL, STEEL, 1.0,
             name="pilot")
        rc(bx + B * 0.5 - 0.3, 5.3, 0.3, 5.9, STEEL, None, name="bell")
        cx0 = e0 + 1.3
        for i in range(n):
            wl(cx0 + i * sp, d)
        wl(W - 3.0, 1.0)
        wl(W - 1.9, 1.0)
        pin = d / 2 + 0.5
        rc(cx0, pin - 0.07, (n - 1) * sp, pin + 0.07, "#D0D4D8", None, name="coupling rod")
        info.update(plate=(X(bx + 0.3), Y(4.45), 1.6 * u, 0.7 * u), W=W, top=Y(6.4))
        info["tender_plate"] = (X(0.8), Y(3.2), 1.9 * u, 0.7 * u) if with_tender else None
        info["cab_plate"] = (X(e0 + 0.3), Y(4.6), 1.6 * u, 0.7 * u)
    info["W"] = info.get("W")
    info["x"] = x
    info["gy"] = gy
    info["u"] = u
    return info


def wagon(sh, x, gy, u, style="box", color=WAGON, length=4.4):
    """Freight wagon silhouette on the same unit scale as engine(). Styles: box, hopper, flat."""
    X, Y = _R(sh, x, gy, u)

    def rc(a, h0, w, h1, fill, line_=None, lw=1.0, radius=None, name="part"):
        return rect(sh, X(a), Y(h1), w * u, (h1 - h0) * u, fill, line_, lw, radius=radius, name=name)

    rc(0, 1.0, length, 1.4, DARKMETAL, STEEL, 0.75, name="wagon frame")
    if style == "box":
        rc(0, 1.4, length, 3.5, color, None, radius=0.05 * u, name="wagon body")
        rc(-0.1, 3.5, length + 0.2, 3.75, shade(color, -0.3), None, name="wagon roof")
        rc(length * 0.38, 1.5, 0.12, 3.4, shade(color, -0.4), None, name="door line")
        rc(length * 0.62, 1.5, 0.12, 3.4, shade(color, -0.4), None, name="door line")
    elif style == "hopper":
        poly(sh, [(X(0), Y(3.9)), (X(length), Y(3.9)), (X(length - 0.7), Y(1.4)), (X(0.7), Y(1.4))], color, None,
             name="hopper body")
        rc(0, 3.7, length, 3.95, shade(color, 0.25), None, name="hopper rim")
        poly(sh, [(X(length * 0.3), Y(1.4)), (X(length * 0.4), Y(1.1)), (X(length * 0.5), Y(1.4))], DARKMETAL,
             None, name="hopper hatch")
        poly(sh, [(X(length * 0.55), Y(1.4)), (X(length * 0.65), Y(1.1)), (X(length * 0.75), Y(1.4))], DARKMETAL,
             None, name="hopper hatch")
    else:  # flat
        rc(0, 1.4, length, 1.8, color, None, name="flat bed")
        rc(length * 0.2, 1.8, length * 0.28, 3.0, shade(color, -0.25), None, radius=0.04 * u, name="crate")
        rc(length * 0.56, 1.8, length * 0.24, 2.6, shade(color, -0.25), None, radius=0.04 * u, name="crate")
    for a in (0.9, length - 0.9):
        wheel(sh, X(a), Y(0.6), 1.2 * u, COAL, STEEL, 1.25)
    return {"W": length, "u": u, "x": x, "gy": gy}


def station_building(sh, x, gy, u, style="gable", color=STYLE_A):
    """Small station: platform plus building. 'gable' = pitched roof; 'depot' = flat roof with a sign board."""
    X, Y = _R(sh, x, gy, u)
    L = 8.0
    rect(sh, X(0), Y(0.6), L * u, 0.6 * u, "#5A606A", STEEL, 1.0, name="platform")
    if style == "gable":
        rect(sh, X(0.8), Y(3.6), 5.2 * u, 3.0 * u, color, None, name="building")
        poly(sh, [(X(0.5), Y(3.6)), (X(3.4), Y(5.6)), (X(6.3), Y(3.6))], shade(color, -0.35), None, name="gable roof")
        rect(sh, X(4.8), Y(5.4), 0.55 * u, 1.3 * u, DARKMETAL, None, name="chimney")
        rect(sh, X(1.3), Y(2.8), 1.0 * u, 1.0 * u, COAL, None, name="window")
        rect(sh, X(4.4), Y(2.8), 1.0 * u, 1.0 * u, COAL, None, name="window")
        rect(sh, X(2.9), Y(3.0), 0.9 * u, 2.4 * u, shade(color, -0.45), None, name="door")
    else:
        rect(sh, X(0.8), Y(3.1), 5.4 * u, 2.5 * u, color, None, name="building")
        rect(sh, X(0.8), Y(4.3), 5.4 * u, 1.2 * u, shade(color, 0.2), None, name="false front")
        rect(sh, X(0.6), Y(3.2), 5.8 * u, 0.3 * u, shade(color, -0.4), None, name="roof")
        rect(sh, X(1.4), Y(2.3), 1.0 * u, 1.0 * u, COAL, None, name="window")
        rect(sh, X(4.4), Y(2.3), 1.0 * u, 1.0 * u, COAL, None, name="window")
        rect(sh, X(2.9), Y(2.5), 1.0 * u, 2.2 * u, shade(color, -0.45), None, name="door")
        # water tank on legs
        rect(sh, X(6.6), Y(6.2), 1.4 * u, 1.3 * u, WATER, None, radius=0.1 * u, name="tank")
        for lx in (6.7, 7.8):
            rect(sh, X(lx), Y(4.9), 0.1 * u, 4.3 * u, STEEL, None, name="tank leg")
    return {"W": L, "u": u}


def rails_strip(sh, x, y, length, sleepers=True):
    """Side-on rail line (a thin steel bar), y = top of rail."""
    rect(sh, x, y, length, 0.07, STEEL, None, name="rail")
    if sleepers:
        k = 0
        while k * 0.4 < length:
            rect(sh, x + k * 0.4, y + 0.07, 0.14, 0.09, SLEEPER, None, name="sleeper")
            k += 1
