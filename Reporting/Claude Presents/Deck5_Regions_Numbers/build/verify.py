"""Whole-deck verification for Deck 5: tag counts against the brief, contrast, alt text, reading order,
language, picture aspect, notes/transitions/animations, document properties, forbidden words."""
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pptx import Presentation  # noqa: E402
from pptx.util import Emu  # noqa: E402
from check import walk, PATH  # noqa: E402

EXPECT = {"AGREED": 18, "UNDECIDED": 3, "PROPOSED": 1, "PROVISIONAL": 1, "(none)": 3}
FORBIDDEN = ["superseded", "£", "$", "price", "cost "]  # 'cost' is allowed only inside the briefed chip text
BRIEF_OK = ("Cost and screens", "Renumber cost and screens")


def lum(h):
    h = h.lstrip("#")
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def contrast(a, b):
    la, lb = lum(a), lum(b)
    if la < lb:
        la, lb = lb, la
    return (la + 0.05) / (lb + 0.05)


def fill_of(shape):
    try:
        if shape.fill.type == 1:
            return str(shape.fill.fore_color.rgb)
    except Exception:
        pass
    return None


prs = Presentation(PATH)
tags = Counter()
bad, warn = [], []
pics = links = 0
langs = Counter()
for i, sl in enumerate(prs.slides, 1):
    chip = None
    order = [s.name for s in sl.shapes]
    # reading order: title first, then chip (if any), caption last (before slide number)
    if order[0] != "TITLE":
        bad.append((i, "title is not first in reading order"))
    cap_idx = [k for k, n in enumerate(order) if n == "CAPTION"]
    if cap_idx and cap_idx[-1] < len(order) - 3:
        bad.append((i, "caption is not near the end of the reading order"))
    for s in walk(sl.shapes):
        if s.name == "CHIP" and chip is None:
            chip = s.text_frame.text
        if s.shape_type == 13:
            pics += 1
            if not s._element.xpath("./p:nvPicPr/p:cNvPr")[0].get("descr"):
                bad.append((i, "picture without alt"))
            # aspect: displayed ratio must equal the cropped-image ratio
            iw, ih = s.image.size
            vis_w = iw * (1 - s.crop_left - s.crop_right)
            vis_h = ih * (1 - s.crop_top - s.crop_bottom)
            if abs((vis_w / vis_h) / (s.width / s.height) - 1) > 0.01:
                bad.append((i, "picture stretched"))
        if s.shape_type == 6 and not s._element.xpath("./p:nvGrpSpPr/p:cNvPr")[0].get("descr"):
            bad.append((i, "group without alt: " + s.name))
        if s.has_text_frame:
            f = fill_of(s)
            backs = [f] if f else ["1E2126", "2B2F36", "343A43"]
            for p in s.text_frame.paragraphs:
                for r in p.runs:
                    langs[r.font.language_id] += 1
                    if r.font.color and r.font.color.type is not None and r.text.strip():
                        col = str(r.font.color.rgb)
                        worst = min(contrast(col, b) for b in backs)
                        if worst < 4.5:
                            warn.append((i, "contrast %.2f %s on %s: %s" % (worst, col, backs, r.text[:30])))
                    if r.hyperlink.address:
                        links += 1
            low = s.text_frame.text.lower()
            for w in ("superseded", "£", "$"):
                if w in low:
                    bad.append((i, "forbidden text '%s': %s" % (w, s.text_frame.text[:30])))
        if getattr(s, "has_table", False) and s.has_table:
            for row in s.table.rows:
                for c in row.cells:
                    f = None
                    try:
                        f = str(c.fill.fore_color.rgb) if c.fill.type == 1 else None
                    except Exception:
                        pass
                    for p in c.text_frame.paragraphs:
                        for r in p.runs:
                            langs[r.font.language_id] += 1
                            if r.font.color and r.font.color.type is not None and f:
                                w = contrast(str(r.font.color.rgb), f)
                                if w < 4.5:
                                    bad.append((i, "table contrast %.2f" % w))
    tags[(chip or "(none)")] += 1
    if sl.has_notes_slide:
        bad.append((i, "has notes"))
    if sl._element.xpath(".//p:transition") or sl._element.xpath(".//p:timing") or \
            sl._element.xpath(".//*[local-name()='AlternateContent']"):
        bad.append((i, "transition/animation present"))

print("tag counts:", dict(tags))
print("expected  :", EXPECT)
if dict(tags) != EXPECT:
    bad.append((0, "tag counts differ from the brief"))
print("slides:", len(prs.slides), "| pictures:", pics, "| hyperlinks:", links)
print("run languages:", {str(k): v for k, v in langs.items()})
print("problems:", bad if bad else "none")
print("contrast warnings (text on a shape the check cannot see; review by hand):", len(warn))
for w in warn[:12]:
    print("   ", w)
cp = prs.core_properties
print("title:", cp.title, "| author:", cp.author, "| language:", cp.language)
print("slide size in:", Emu(prs.slide_width).inches, Emu(prs.slide_height).inches)
print("file KB:", os.path.getsize(PATH) // 1024)
sys.exit(1 if bad else 0)
