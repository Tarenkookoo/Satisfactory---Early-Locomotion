"""check_template: structural and house-style checks for the template, the patterns deck and decks built from them.

usage: python3 check_template.py FILE.pptx [FILE2.pptx ...] [--polished] [--words] [--quiet]

  --polished  the file went through tools/polish.py: transitions and animations are expected on slides
              (layouts and master must still be clean)
  --words     print the per-slide word table even when nothing is wrong
  --quiet     print only problems and the final verdict

Exit status 0 when every file passes, 1 when any error is found. Warnings never fail a file.

Checks (E = error, W = warning)
  package    E zip integrity; every XML part parses; every relationship target exists; [Content_Types] covers
             every part; no notes parts; no thumbnail or printer-settings leftovers (W)
  theme      E Arial theme fonts; E light hyperlink colours; E master background #1E2126
  layouts    E no stale default layouts; E title placeholder, prompt text in every placeholder; E slide-number
             placeholder (all but Cover and Closing); E no transitions, animations or notes; E type floor
  slides     E smallest font >= 14 pt (credit lines 10 pt, credits tables 11 pt); E alt text on pictures, groups
             and tables; E language en-GB everywhere; E no notes; E no transitions or animations (unless
             --polished); E reading order (title, chip, visual, caption, number); E no empty placeholders;
             E text overflow estimate; W word budget (25 aim, 45 cap; Status legend and Credits exempt);
             W loose diagram shapes outside groups
  xml        E child order of the common containers (what PowerPoint enforces and LibreOffice does not);
             E unique shape ids per part
"""
import os
import re
import sys
import zipfile

from lxml import etree

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pptx import Presentation  # noqa: E402
from pptx.util import Emu  # noqa: E402

import el_kit as k  # noqa: E402

A = "http://schemas.openxmlformats.org/drawingml/2006/main"
P = "http://schemas.openxmlformats.org/presentationml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
MC = "http://schemas.openxmlformats.org/markup-compatibility/2006"
NS = {"a": A, "p": P, "r": R}

DEFAULT_LAYOUT_NAMES = {"Title Slide", "Title and Content", "Section Header", "Two Content", "Comparison",
                        "Title Only", "Blank", "Content with Caption", "Picture with Caption",
                        "Title and Vertical Text", "Vertical Title and Text"}
NO_NUMBER_LAYOUTS = {"Cover", "Closing / what next"}
WORD_EXEMPT_LAYOUTS = {"Status legend", "Credits / sources table", "Cover", "Closing / what next",
                       "Chapter divider"}
CREDITS_LAYOUT = "Credits / sources table"

# ---------------------------------------------------------------- XML child order (ranks share a tuple)
ORDER = {
    "a:ln": [("noFill", "solidFill", "gradFill", "pattFill"), ("prstDash", "custDash"),
             ("round", "bevel", "miter"), ("headEnd",), ("tailEnd",), ("extLst",)],
    "a:spPr": None, "p:spPr": [("xfrm",), ("custGeom", "prstGeom"), ("noFill", "solidFill", "gradFill", "blipFill",
                                                                  "pattFill", "grpFill"), ("ln",),
                               ("effectLst", "effectDag"), ("scene3d",), ("sp3d",), ("extLst",)],
    "a:pPr": [("lnSpc",), ("spcBef",), ("spcAft",), ("buClrTx", "buClr"), ("buSzTx", "buSzPct", "buSzPts"),
              ("buFontTx", "buFont"), ("buNone", "buAutoNum", "buChar", "buBlip"), ("tabLst",), ("defRPr",),
              ("extLst",)],
    "a:rPr": [("ln",), ("noFill", "solidFill", "gradFill", "blipFill", "pattFill", "grpFill"),
              ("effectLst", "effectDag"), ("highlight",), ("uLnTx", "uLn"), ("uFillTx", "uFill"), ("latin",),
              ("ea",), ("cs",), ("sym",), ("hlinkClick",), ("hlinkMouseOver",), ("rtl",), ("extLst",)],
    "a:bodyPr": [("prstTxWarp",), ("noAutofit", "normAutofit", "spAutoFit"), ("scene3d",), ("sp3d",),
                 ("flatTx",), ("extLst",)],
    "a:tcPr": [("lnL",), ("lnR",), ("lnT",), ("lnB",), ("lnTlToBr",), ("lnBlToTr",), ("cell3D",),
               ("noFill", "solidFill", "gradFill", "blipFill", "pattFill", "grpFill"), ("headers",), ("extLst",)],
    "p:sp": [("nvSpPr",), ("spPr",), ("style",), ("txBody",), ("extLst",)],
    "p:pic": [("nvPicPr",), ("blipFill",), ("spPr",), ("style",), ("extLst",)],
    "p:cSld": [("bg",), ("spTree",), ("custDataLst",), ("controls",), ("extLst",)],
    "p:sld": [("cSld",), ("clrMapOvr",), ("transition", "AlternateContent"), ("timing",), ("extLst",)],
    "p:sldLayout": [("cSld",), ("clrMapOvr",), ("transition", "AlternateContent"), ("timing",), ("hf",),
                    ("extLst",)],
    "p:sldMaster": [("cSld",), ("clrMap",), ("sldLayoutIdLst",), ("transition", "AlternateContent"), ("timing",),
                    ("hf",), ("txStyles",), ("extLst",)],
    "p:presentation": [("sldMasterIdLst",), ("notesMasterIdLst",), ("handoutMasterIdLst",), ("sldIdLst",),
                       ("sldSz",), ("notesSz",), ("smartTags",), ("embeddedFontLst",), ("custShowLst",),
                       ("photoAlbum",), ("custDataLst",), ("kinsoku",), ("defaultTextStyle",),
                       ("modifyVerifier",), ("extLst",)],
    "a:tbl": [("tblPr",), ("tblGrid",), ("tr",)],
    "a:txBody": [("bodyPr",), ("lstStyle",), ("p",)],
    "p:txBody": [("bodyPr",), ("lstStyle",), ("p",)],
    "a:p": [("pPr",), ("r", "br", "fld"), ("endParaRPr",)],
    "p:grpSpPr": [("xfrm",), ("noFill", "solidFill", "gradFill", "blipFill", "pattFill", "grpFill"),
                  ("effectLst", "effectDag"), ("scene3d",), ("extLst",)],
    "a:xfrm": [("off",), ("ext",), ("chOff",), ("chExt",)],
}
ORDER["a:spPr"] = ORDER["p:spPr"]
for _n in range(1, 10):
    ORDER["a:lvl%dpPr" % _n] = ORDER["a:pPr"]
ORDER["a:defRPr"] = ORDER["a:rPr"]
ORDER["a:endParaRPr"] = ORDER["a:rPr"]
ORDER["a:defPPr"] = ORDER["a:pPr"]
ORDER["a:fld"] = [("rPr",), ("pPr",), ("t",)]


def _qn(tag):
    pre, name = tag.split(":")
    return "{%s}%s" % ({"a": A, "p": P, "r": R}[pre], name)


class Report:
    def __init__(self, path, quiet=False):
        self.path = path
        self.errors = []
        self.warnings = []
        self.quiet = quiet

    def err(self, where, msg):
        self.errors.append("%s: %s" % (where, msg))

    def warn(self, where, msg):
        self.warnings.append("%s: %s" % (where, msg))


# ---------------------------------------------------------------- package level
def check_package(z, rep):
    bad = z.testzip()
    if bad:
        rep.err("zip", "corrupt member " + bad)
    names = set(z.namelist())
    roots = {}
    for n in sorted(names):
        if n.endswith((".xml", ".rels")):
            try:
                roots[n] = etree.fromstring(z.read(n))
            except Exception as exc:  # noqa: BLE001
                rep.err(n, "XML parse error: %s" % exc)
    ct = roots.get("[Content_Types].xml")
    if ct is not None:
        defaults = {e.get("Extension").lower() for e in ct if e.tag.endswith("Default")}
        overrides = {e.get("PartName") for e in ct if e.tag.endswith("Override")}
        for n in names:
            if n == "[Content_Types].xml" or n.endswith("/"):
                continue
            ext = n.rsplit(".", 1)[-1].lower()
            if "/" + n not in overrides and ext not in defaults:
                rep.err("content types", "no content type for " + n)
        for o in overrides:
            if o.lstrip("/") not in names:
                rep.err("content types", "override for missing part " + o)
    for n, root in roots.items():
        if not n.endswith(".rels"):
            continue
        base = os.path.dirname(os.path.dirname(n))
        for rel in root:
            if rel.get("TargetMode") == "External":
                continue
            tgt = rel.get("Target")
            full = tgt.lstrip("/") if tgt.startswith("/") else os.path.normpath(os.path.join(base, tgt))
            full = full.replace("\\", "/")
            if full not in names:
                rep.err(n, "relationship %s targets missing part %s" % (rel.get("Id"), full))
    for n in names:
        if "notesSlide" in n or "notesMaster" in n:
            rep.err("package", "notes part present: " + n)
        if "printerSettings" in n or n.endswith("thumbnail.jpeg"):
            rep.warn("package", "stale part present: " + n)
    # r:id references inside parts resolve
    for n, root in roots.items():
        if n.endswith(".rels") or not n.startswith("ppt/"):
            continue
        relname = os.path.join(os.path.dirname(n), "_rels", os.path.basename(n) + ".rels").replace("\\", "/")
        ids = set()
        if relname in roots:
            ids = {r.get("Id") for r in roots[relname]}
        for el in root.iter():
            for attr in ("embed", "id", "link"):
                v = el.get("{%s}%s" % (R, attr))
                if v and v not in ids:
                    rep.err(n, "unresolved relationship id %s" % v)
    return roots


def check_order(roots, rep):
    for n, root in roots.items():
        if not n.startswith("ppt/") or n.endswith(".rels") or "theme" in n:
            continue
        for el in root.iter():
            if not isinstance(el.tag, str):
                continue
            qn_ = etree.QName(el)
            pre = {A: "a", P: "p"}.get(qn_.namespace)
            if not pre:
                continue
            key = "%s:%s" % (pre, qn_.localname)
            order = ORDER.get(key)
            if not order:
                continue
            rank = {}
            for i, grp in enumerate(order):
                for g in grp:
                    rank[g] = i
            seq = []
            for c in el:
                if not isinstance(c.tag, str):
                    continue
                ln = etree.QName(c).localname
                if ln in rank:
                    seq.append(rank[ln])
                elif key not in ("a:p",) and etree.QName(c).namespace in (A, P, MC):
                    rep.err(n, "unexpected <%s> inside <%s>" % (ln, key))
            if seq != sorted(seq):
                rep.err(n, "child order inside <%s>: %s" % (key, [etree.QName(c).localname for c in el]))
        ids = [e.get("id") for e in root.iter("{%s}cNvPr" % P)]
        if len(ids) != len(set(ids)):
            rep.err(n, "duplicate shape ids")


def check_transitions(roots, rep, polished):
    for n, root in roots.items():
        if not n.startswith("ppt/") or n.endswith(".rels"):
            continue
        is_slide = n.startswith("ppt/slides/slide")
        if is_slide and polished:
            continue
        for tag in ("transition", "timing"):
            if list(root.iter("{%s}%s" % (P, tag))):
                rep.err(n, "contains <p:%s> (no transitions or animations in layouts, master or unpolished slides)"
                        % tag)


def check_language(roots, z, rep):
    core = roots.get("docProps/core.xml")
    if core is not None:
        langs = [e.text for e in core.iter() if isinstance(e.tag, str) and e.tag.endswith("}language")]
        if langs != ["en-GB"]:
            rep.err("core.xml", "dc:language is %s, want en-GB" % langs)
    else:
        rep.err("core.xml", "missing")
    for n, root in roots.items():
        if not n.startswith("ppt/") or n.endswith(".rels") or "theme" in n:
            continue
        for tag in ("rPr", "defRPr", "endParaRPr"):
            for e in root.iter("{%s}%s" % (A, tag)):
                lg = e.get("lang")
                if lg not in (None, "en-GB"):
                    rep.err(n, "language %s on <a:%s>" % (lg, tag))
                    break


def check_theme(z, roots, rep):
    th = [n for n in roots if n.startswith("ppt/theme/theme")]
    if not th:
        rep.err("theme", "no theme part")
        return
    root = roots[th[0]]
    for which in ("majorFont", "minorFont"):
        lat = root.find(".//{%s}%s/{%s}latin" % (A, which, A))
        if lat is None or lat.get("typeface") != "Arial":
            rep.err("theme", "%s is not Arial" % which)
    def lum(h):
        r, g, b = [int(h[i:i + 2], 16) for i in (0, 2, 4)]
        return (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255
    for tag in ("hlink", "folHlink"):
        c = root.find(".//{%s}%s/{%s}srgbClr" % (A, tag, A))
        if c is None or lum(c.get("val")) < 0.5:
            rep.err("theme", "%s colour is missing or too dark for a charcoal background" % tag)
    m = [n for n in roots if n.startswith("ppt/slideMasters/slideMaster")]
    if m:
        bg = roots[m[0]].find(".//{%s}bg//{%s}srgbClr" % (P, A))
        if bg is None or bg.get("val").upper() != "1E2126":
            rep.err("master", "background is not #1E2126")


# ---------------------------------------------------------------- inherited text properties
def _lst_levels(lst, lvl):
    if lst is None:
        return None
    return lst.find("{%s}lvl%dpPr" % (A, lvl + 1))


class Resolver:
    """Resolves font size, bold, left margin and insets through shape, layout, master and defaults."""

    def __init__(self, prs):
        self.prs = prs
        self.master = prs.slide_master
        self.mel = self.master._element
        self.tx = self.mel.find("{%s}txStyles" % P)
        self.default = prs.part._element.find("{%s}defaultTextStyle" % P)

    @staticmethod
    def _ph(el):
        return el.find(".//{%s}ph" % P)

    def _find_by_ph(self, container_el, ph):
        if ph is None:
            return None
        idx, typ = ph.get("idx"), ph.get("type")
        found = None
        for sp in container_el.iter("{%s}sp" % P):
            q = self._ph(sp)
            if q is None:
                continue
            if idx is not None and q.get("idx") == idx and (typ is None or q.get("type") == typ or True):
                return sp
            if idx is None and q.get("idx") is None and (q.get("type") or "obj") == (typ or "obj"):
                found = sp
        return found

    def _master_ph(self, ph):
        typ = (ph.get("type") if ph is not None else None) or "body"
        want = "title" if typ in ("title", "ctrTitle") else ("sldNum" if typ == "sldNum" else "body")
        for sp in self.mel.iter("{%s}sp" % P):
            q = self._ph(sp)
            if q is not None and (q.get("type") or "body") == want:
                return sp
        return None

    def chain(self, sp_el, owner_el):
        """List of (lstStyle element, bodyPr element) in priority order, plus the tx style kind."""
        sp_chain = [sp_el]
        ph = self._ph(sp_el)
        kind = "other"
        if ph is not None:
            typ = ph.get("type") or "body"
            kind = "title" if typ in ("title", "ctrTitle") else ("other" if typ in ("sldNum", "dt", "ftr")
                                                                 else "body")
            if owner_el.tag == "{%s}sld" % P:
                rel_layout = getattr(self, "_slide_layout", None)
                if rel_layout is not None:
                    lay_sp = self._find_by_ph(rel_layout, ph)
                    if lay_sp is not None:
                        sp_chain.append(lay_sp)
            m = self._master_ph(ph)
            if m is not None:
                sp_chain.append(m)
        lsts = [s.find(".//{%s}lstStyle" % A) for s in sp_chain]
        bodies = [s.find(".//{%s}bodyPr" % A) for s in sp_chain]
        return lsts, bodies, kind

    def size_bold_marl(self, lsts, kind, lvl, run_rpr):
        sz = run_rpr.get("sz") if run_rpr is not None else None
        b = run_rpr.get("b") if run_rpr is not None else None
        marl = None
        for lst in lsts:
            e = _lst_levels(lst, lvl)
            if e is None:
                continue
            if marl is None and e.get("marL") is not None:
                marl = int(e.get("marL"))
            d = e.find("{%s}defRPr" % A)
            if d is not None:
                if sz is None and d.get("sz"):
                    sz = d.get("sz")
                if b is None and d.get("b") is not None:
                    b = d.get("b")
        style_el = {"title": "titleStyle", "body": "bodyStyle", "other": "otherStyle"}[kind]
        for src in (self.tx.find("{%s}%s" % (P, style_el)) if self.tx is not None else None, self.default):
            e = _lst_levels(src, lvl)
            if e is None:
                continue
            if marl is None and e.get("marL") is not None:
                marl = int(e.get("marL"))
            d = e.find("{%s}defRPr" % A)
            if d is not None:
                if sz is None and d.get("sz"):
                    sz = d.get("sz")
                if b is None and d.get("b") is not None:
                    b = d.get("b")
        return (int(sz) / 100.0 if sz else 18.0), b in ("1", "true"), (marl or 0) / 914400.0

    @staticmethod
    def insets(bodies):
        vals = {"lIns": 91440, "tIns": 45720, "rIns": 91440, "bIns": 45720}
        for key in vals:
            for b in bodies:
                if b is not None and b.get(key) is not None:
                    vals[key] = int(b.get(key))
                    break
        return [vals[x] / 914400.0 for x in ("lIns", "tIns", "rIns", "bIns")]

    @staticmethod
    def anchor(bodies):
        for b in bodies:
            if b is not None and b.get("anchor"):
                return b.get("anchor")
        return "t"


def walk(shapes):
    for s in shapes:
        yield s
        if s.shape_type == 6:
            yield from walk(s.shapes)


def inches(v):
    return Emu(v).inches


def paragraph_runs(p_el):
    return [r for r in p_el if r.tag in ("{%s}r" % A, "{%s}fld" % A)]


def shape_text_metrics(res, shape, owner_el, floor_exceptions, rep, where, layout_name):
    """Yields problems about font size and overflow for one text-bearing shape. Returns (min_pt, text)."""
    sp_el = shape._element
    if sp_el.tag != "{%s}sp" % P:
        return None, ""
    tx = sp_el.find("{%s}txBody" % P)
    if tx is None:
        return None, ""
    lsts, bodies, kind = res.chain(sp_el, owner_el)
    ins = res.insets(bodies)
    w = inches(shape.width) - ins[0] - ins[2]
    h = inches(shape.height) - ins[1] - ins[3]
    total_h = 0.0
    min_pt = None
    text_all = []
    for p_el in tx.findall("{%s}p" % A):
        ppr = p_el.find("{%s}pPr" % A)
        lvl = int(ppr.get("lvl", "0")) if ppr is not None else 0
        runs = paragraph_runs(p_el)
        text = "".join((r.findtext("{%s}t" % A) or "") for r in runs)
        text_all.append(text)
        sizes, bold = [], False
        marl = 0
        for r in runs:
            rpr = r.find("{%s}rPr" % A)
            sz, b, marl = res.size_bold_marl(lsts, kind, lvl, rpr)
            sizes.append(sz)
            bold = bold or b
        if not runs:
            end = p_el.find("{%s}endParaRPr" % A)
            sz, b, marl = res.size_bold_marl(lsts, kind, lvl, end)
            sizes.append(sz)
        size = max(sizes)
        if runs and text.strip():
            min_pt = min(sizes) if min_pt is None else min(min_pt, min(sizes))
        lines = len(k.wrap_lines(text if text else " ", size, max(0.2, w - marl), bold))
        total_h += lines * size * 1.2 / 72.0
    return min_pt, "\n".join(text_all), total_h, h, w


# ---------------------------------------------------------------- slide checks
ROLE_CHIP = "status chip"


def role(shape):
    n = (shape.name or "").lower()
    if shape.is_placeholder:
        t = str(shape.placeholder_format.type)
        if "TITLE" in t and "SUB" not in t:
            return 0
        if "SLIDE_NUMBER" in t:
            return 4
        if n == ROLE_CHIP:
            return 1
        if n == "caption":
            return 3
        return 2
    if n.startswith(ROLE_CHIP):
        return 1
    if n == "slide number":
        return 4
    if n == "caption":
        return 3
    return 2


def floor_for(shape, layout_name):
    n = (shape.name or "").lower()
    if n.startswith("credit line"):
        return 10
    return 14


def check_slide(prs, res, slide, idx, rep, words_rows):
    where = "slide %d" % idx
    layout_name = slide.slide_layout.name
    sld_el = slide._element
    res._slide_layout = slide.slide_layout._element
    if slide.has_notes_slide:
        rep.err(where, "has speaker notes")
    # title
    t = slide.shapes.title
    title_text = t.text_frame.text.strip() if t is not None and t.has_text_frame else ""
    if t is None:
        rep.err(where, "no title placeholder")
    elif not title_text:
        rep.err(where, "empty title")
    # reading order
    top = list(slide.shapes)
    roles = [role(s) for s in top]
    if roles != sorted(roles):
        rep.err(where, "reading order: roles %s in shape order %s (want title, chip, visuals, caption, number)"
                % (roles, [s.name for s in top]))
    if roles and roles[0] != 0:
        rep.err(where, "first shape in reading order is not the title")
    if layout_name not in NO_NUMBER_LAYOUTS and 4 not in roles:
        rep.err(where, "no slide number placeholder")
    # empty placeholders
    for s in top:
        if s.is_placeholder:
            if s._element.tag == "{%s}sp" % P and s.has_text_frame:
                if "SLIDE_NUMBER" in str(s.placeholder_format.type):
                    continue
                if not s.text_frame.text.strip():
                    rep.err(where, "empty placeholder '%s'" % s.name)
            elif s._element.tag == "{%s}sp" % P:
                rep.err(where, "empty placeholder '%s'" % s.name)
    # alt text
    for s in walk(slide.shapes):
        el = s._element
        c = el.xpath("./p:nvPicPr/p:cNvPr | ./p:nvGrpSpPr/p:cNvPr | ./p:nvGraphicFramePr/p:cNvPr")
        if c and not (c[0].get("descr") or "").strip():
            rep.err(where, "no alt text on '%s'" % s.name)
    loose = [s for s in top if not s.is_placeholder and s.shape_type == 1 and
             role(s) == 2 and not (s.name or "").lower().startswith(("chip", "inline chip", "icon", "legend"))]
    if len(loose) > 8:
        rep.warn(where, "%d loose autoshapes outside groups; group diagrams and give each group alt text"
                 % len(loose))
    # fonts, overflow, words
    min_pt = None
    body_words = 0
    for s in walk(slide.shapes):
        nm = s.name or ""
        floor = floor_for(s, layout_name)
        if getattr(s, "has_table", False) and s.has_table:
            tfloor = 11 if layout_name == CREDITS_LAYOUT else 14
            for row in s.table.rows:
                for cell in row.cells:
                    for p in cell.text_frame.paragraphs:
                        for r in p.runs:
                            sz = r.font.size.pt if r.font.size else 14.0
                            min_pt = sz if min_pt is None else min(min_pt, sz)
                            if sz < tfloor:
                                rep.err(where, "table text %.0f pt is below %d pt" % (sz, tfloor))
                    if layout_name not in WORD_EXEMPT_LAYOUTS:
                        body_words += k.word_count(cell.text_frame.text)
            continue
        if s._element.tag != "{%s}sp" % P and s._element.tag != "{%s}cxnSp" % P:
            continue
        got = shape_text_metrics(res, s, sld_el, None, rep, where, layout_name)
        if got[0] is None and not got[1]:
            continue
        mn, text, need, have, w = got
        if mn is not None:
            min_pt = mn if min_pt is None else min(min_pt, mn)
            if mn < floor - 0.01:
                rep.err(where, "font %.0f pt in '%s' is below the %d pt floor" % (mn, nm, floor))
        if text.strip():
            if need > have + 0.03:
                rep.err(where, "text may overflow '%s': needs %.2f in, box has %.2f in" % (nm, need, have))
            longest = max((k.text_w(wd, mn or 14, False) for wd in text.split()), default=0)
            if longest > w + 0.01:
                rep.err(where, "a word is wider than the box in '%s'" % nm)
            x, y, bw, bh = [inches(v) for v in (s.left, s.top, s.width, s.height)]
            if x < -0.01 or y < -0.01 or x + bw > 13.34 or y + bh > 7.51:
                rep.err(where, "'%s' extends off the slide" % nm)
            r_ = role(s)
            lname = nm.lower()
            if (not (s.is_placeholder and ("TITLE" in str(s.placeholder_format.type) or
                                           "SLIDE_NUMBER" in str(s.placeholder_format.type)))
                    and r_ != 1 and lname not in ("slide number",) and not lname.startswith(("credit line", "chip",
                                                                                           "status chip"))):
                if layout_name not in WORD_EXEMPT_LAYOUTS:
                    body_words += k.word_count(text)
    words_rows.append((idx, layout_name, title_text[:34], body_words, min_pt))
    if layout_name not in WORD_EXEMPT_LAYOUTS:
        if body_words > 45:
            rep.err(where, "%d words (cap is 45)" % body_words)
        elif body_words > 25:
            rep.warn(where, "%d words (aim for 25 or fewer)" % body_words)
    # picture checks: no stretching (crop only) is by construction; check aspect when a blip is present
    for s in top:
        if s._element.tag == "{%s}pic" % P:
            try:
                iw, ih = s.image.size
                cl, cr, ct, cb = s.crop_left, s.crop_right, s.crop_top, s.crop_bottom
                vis_ar = (iw * (1 - cl - cr)) / (ih * (1 - ct - cb))
                box_ar = s.width / s.height
                if abs(vis_ar / box_ar - 1) > 0.02:
                    rep.err(where, "picture '%s' is stretched (visible aspect %.3f vs box %.3f)"
                            % (s.name, vis_ar, box_ar))
            except Exception as exc:  # noqa: BLE001
                rep.warn(where, "could not check picture aspect: %s" % exc)


# ---------------------------------------------------------------- layout checks
def check_layouts(prs, rep):
    names = [l.name for l in prs.slide_layouts]
    for n in names:
        if n in DEFAULT_LAYOUT_NAMES:
            rep.err("layouts", "stale default layout '%s' is still in the template" % n)
    if len(set(names)) != len(names):
        rep.err("layouts", "duplicate layout names")
    for lay in prs.slide_layouts:
        w = "layout '%s'" % lay.name
        phs = list(lay.placeholders)
        types = [str(p.placeholder_format.type) for p in phs]
        if not any("TITLE" in t and "SUB" not in t for t in types):
            rep.err(w, "no title placeholder")
        if lay.name not in NO_NUMBER_LAYOUTS and not any("SLIDE_NUMBER" in t for t in types):
            rep.err(w, "no slide-number placeholder")
        for p in phs:
            if "SLIDE_NUMBER" in str(p.placeholder_format.type):
                continue
            txt = p.text_frame.text.strip() if p.has_text_frame else ""
            if not txt:
                rep.err(w, "placeholder '%s' has no prompt text" % p.name)
        if lay._element.find("{%s}transition" % P) is not None or lay._element.find("{%s}timing" % P) is not None:
            rep.err(w, "transition or timing present")
        idxs = [p.placeholder_format.idx for p in phs]
        if len(idxs) != len(set(idxs)):
            rep.err(w, "duplicate placeholder idx")
    # type floor over master and layouts (credit line placeholders may be 10 pt)
    parts = [prs.slide_master._element] + [l._element for l in prs.slide_layouts]
    for el in parts:
        for tag in ("defRPr", "rPr", "endParaRPr"):
            for e in el.iter("{%s}%s" % (A, tag)):
                sz = e.get("sz")
                if sz and int(sz) < 1400:
                    sp = next((a for a in e.iterancestors("{%s}sp" % P)), None)
                    nm = sp.find(".//{%s}cNvPr" % P).get("name") if sp is not None else ""
                    if not nm.startswith("Credit line"):
                        rep.err("layouts", "font %s pt below the 14 pt floor (in '%s')" % (int(sz) / 100, nm))


# ---------------------------------------------------------------- driver
def check_file(path, polished=False, show_words=False, quiet=False):
    rep = Report(path, quiet)
    with zipfile.ZipFile(path) as z:
        roots = check_package(z, rep)
        check_order(roots, rep)
        check_transitions(roots, rep, polished)
        check_language(roots, z, rep)
        check_theme(z, roots, rep)
        names = z.namelist()
    ext = os.path.splitext(path)[1].lower()
    rows = []
    n_slides = 0
    if ext == ".potx":
        rep.warn("file", ".potx is not opened by python-pptx; only package-level checks ran on it")
    else:
        prs = Presentation(path)
        n_slides = len(prs.slides)
        check_layouts(prs, rep)
        res = Resolver(prs)
        for i, s in enumerate(prs.slides, 1):
            check_slide(prs, res, s, i, rep, rows)
        cp = prs.core_properties
        if not cp.title:
            rep.err("core", "no document title")
        if not cp.author:
            rep.err("core", "no author")
    print("== %s  (%d slides, %d KB)" % (os.path.basename(path), n_slides, os.path.getsize(path) // 1024))
    if rows and (show_words or rep.warnings or rep.errors) and not quiet:
        print("%3s %-32s %-34s %5s %6s" % ("#", "layout", "title", "words", "min pt"))
        for r in rows:
            print("%3d %-32s %-34s %5d %6s" % (r[0], r[1][:32], r[2], r[3], ("%g" % r[4]) if r[4] else "-"))
    for w in rep.warnings:
        print("  warning:", w)
    for e in rep.errors:
        print("  ERROR:", e)
    print("  result:", "PASS" if not rep.errors else "FAIL (%d errors)" % len(rep.errors),
          "| %d warnings" % len(rep.warnings))
    return not rep.errors


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    if not args:
        print(__doc__)
        sys.exit(2)
    ok = True
    for f in args:
        ok = check_file(f, "--polished" in flags, "--words" in flags, "--quiet" in flags) and ok
    sys.exit(0 if ok else 1)
