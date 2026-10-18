"""Whole-deck verification: tag counts, contrast, links, notes, alt text, pictures, fonts."""
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pptx import Presentation  # noqa: E402
from pptx.util import Emu  # noqa: E402
from check import walk  # noqa: E402

PATH = os.path.abspath(os.path.join(HERE, "..", "Coal_Water_and_Servicing_Explained.pptx"))


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
bad = []
links = 0
pics = 0
for i, sl in enumerate(prs.slides, 1):
    chip = None
    for s in walk(sl.shapes):
        if s.name == "CHIP" and chip is None:
            chip = s.text_frame.text
        if s.shape_type == 13:
            pics += 1
            if not s._element.xpath("./p:nvPicPr/p:cNvPr")[0].get("descr"):
                bad.append((i, "picture without alt"))
        if s.has_text_frame:
            f = fill_of(s)
            backs = [f] if f else ["1E2126", "2B2F36", "343A43"]
            for p in s.text_frame.paragraphs:
                for r in p.runs:
                    if r.font.color and r.font.color.type is not None and r.text.strip():
                        col = str(r.font.color.rgb)
                        # chips with outline only sit on the dark panel
                        worst = min(contrast(col, b) for b in backs)
                        if worst < 4.5:
                            bad.append((i, "contrast %.2f %s on %s: %s" % (worst, col, backs, r.text[:30])))
                    if r.hyperlink.address:
                        links += 1
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
                            if r.hyperlink.address:
                                links += 1
                            if r.font.color and r.font.color.type is not None and f:
                                w = contrast(str(r.font.color.rgb), f)
                                if w < 4.5:
                                    bad.append((i, "table contrast %.2f %s: %s" % (w, r.font.color.rgb, r.text[:20])))
    tags[chip or "(none)"] += 1
    if sl.has_notes_slide:
        bad.append((i, "has notes"))
    if sl._element.xpath(".//p:transition") or sl._element.xpath(".//p:timing"):
        bad.append((i, "transition/animation"))
print("tag counts:", dict(tags))
print("pictures:", pics, " hyperlinks:", links)
print("problems:", bad if bad else "none")
cp = prs.core_properties
print("title:", cp.title, "| author:", cp.author, "| language:", cp.language)
print("slide size in:", Emu(prs.slide_width).inches, Emu(prs.slide_height).inches)
