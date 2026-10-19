"""Build the Deck 9 .pptx. usage: build_deck.py [last_slide] [out.pptx]"""
import os
import sys
from lib import setup_presentation, finish
import slides_a
try:
    import slides_b
    FUNCS = slides_a.ALL + slides_b.ALL
except ImportError:
    FUNCS = slides_a.ALL

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "How_the_Mod_Is_Balanced_Explained.pptx")

if __name__ == "__main__":
    last = int(sys.argv[1]) if len(sys.argv) > 1 else len(FUNCS)
    out = sys.argv[2] if len(sys.argv) > 2 else OUT
    prs = setup_presentation()
    for f in FUNCS[:last]:
        f(prs)
    finish(prs, out)
    print("saved", out, len(prs.slides), "slides")
