"""Build the template kit deliverables.

    python3 build_template.py            builds all three files into Templates/
    python3 build_template.py template   builds only EL_Claude_Template_v001.pptx (+ .potx)
    python3 build_template.py patterns   builds only EL_Claude_Template_Patterns_v001.pptx

A  EL_Claude_Template_v001.pptx          template: theme, master, 13 layouts, no slides
B  EL_Claude_Template_v001.potx          the same file saved as a PowerPoint template
C  EL_Claude_Template_Patterns_v001.pptx one filled example slide per layout (neutral dummy text)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import el_kit as k  # noqa: E402
import layouts  # noqa: E402

OUT_DIR = os.path.abspath(os.path.join(HERE, ".."))
TEMPLATE = os.path.join(OUT_DIR, "EL_Claude_Template_v001.pptx")
TEMPLATE_POTX = os.path.join(OUT_DIR, "EL_Claude_Template_v001.potx")
PATTERNS = os.path.join(OUT_DIR, "EL_Claude_Template_Patterns_v001.pptx")


def build_template():
    prs = layouts.new_template_presentation()
    k.set_core_properties(prs, "Early Locomotion house style: Claude template (v001)",
                          "PowerPoint template: charcoal-and-orange theme, Arial, 13 custom layouts",
                          "template; layouts; Early Locomotion; Claude Presents")
    prs.save(TEMPLATE)
    try:
        k.write_potx(TEMPLATE, TEMPLATE_POTX)
    except Exception as exc:  # noqa: BLE001
        print("potx skipped:", exc)
    return TEMPLATE


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    if what in ("all", "template"):
        print("built", build_template())
    if what in ("all", "patterns"):
        import patterns  # noqa: E402  (added in chunk 2)
        print("built", patterns.build_patterns(PATTERNS))
