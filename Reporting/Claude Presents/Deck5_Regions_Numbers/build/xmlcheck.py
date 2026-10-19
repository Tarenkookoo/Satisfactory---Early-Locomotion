"""Structural checks that LibreOffice does not enforce but PowerPoint does:
child order inside a:ln, unique shape ids per slide, every part parses, zip integrity."""
import os
import sys
import zipfile
from lxml import etree

HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.abspath(os.path.join(HERE, "..", "Regions_Numbers_and_Fleet_Identity_Explained.pptx"))
A = "http://schemas.openxmlformats.org/drawingml/2006/main"
P = "http://schemas.openxmlformats.org/presentationml/2006/main"
LN_ORDER = ["noFill", "solidFill", "gradFill", "pattFill", "prstDash", "custDash", "round", "bevel", "miter",
            "headEnd", "tailEnd", "extLst"]
SPPR_ORDER = ["xfrm", "custGeom", "prstGeom", "noFill", "solidFill", "gradFill", "blipFill", "pattFill", "grpFill",
              "ln", "effectLst", "effectDag", "scene3d", "sp3d", "extLst"]

problems = []
with zipfile.ZipFile(PATH) as z:
    bad = z.testzip()
    if bad:
        problems.append("zip member corrupt: " + bad)
    names = z.namelist()
    for n in names:
        if n.endswith(".xml") or n.endswith(".rels"):
            try:
                etree.fromstring(z.read(n))
            except Exception as e:  # noqa: BLE001
                problems.append("XML parse error in %s: %s" % (n, e))
    for n in sorted(x for x in names if x.startswith("ppt/slides/slide") and x.endswith(".xml")):
        root = etree.fromstring(z.read(n))
        ids = [e.get("id") for e in root.iter("{%s}cNvPr" % P)]
        if len(ids) != len(set(ids)):
            problems.append("%s: duplicate shape ids" % n)
        for ln in root.iter("{%s}ln" % A):
            seq = [etree.QName(c).localname for c in ln]
            idx = [LN_ORDER.index(t) for t in seq if t in LN_ORDER]
            if idx != sorted(idx):
                problems.append("%s: a:ln child order %s" % (n, seq))
        for sp in root.iter("{%s}spPr" % P):
            seq = [etree.QName(c).localname for c in sp]
            idx = [SPPR_ORDER.index(t) for t in seq if t in SPPR_ORDER]
            if idx != sorted(idx):
                problems.append("%s: spPr child order %s" % (n, seq))
        for r in root.iter("{%s}rPr" % A):
            if r.get("lang") not in (None, "en-GB"):
                problems.append("%s: lang %s" % (n, r.get("lang")))
    notes = [x for x in names if "notesSlide" in x]
    if notes:
        problems.append("notes parts present: %s" % notes[:3])
print("parts:", len(names), "| problems:", problems if problems else "none")
sys.exit(1 if problems else 0)
