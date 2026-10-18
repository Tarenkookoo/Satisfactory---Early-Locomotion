"""Build Deck 3. Usage: python3 build_deck.py [last_slide_number]"""
import importlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib import new_deck  # noqa: E402

OUT = os.path.abspath(os.path.join(HERE, "..", "Coal_Water_and_Servicing_Explained.pptx"))


def main(upto=24):
    prs = new_deck("Coal, Water and Servicing, Explained",
                   "Read-alone explainer deck 3 for the Early Locomotion mod for Satisfactory")
    fns = []
    for mod in ("slides_a", "slides_b", "slides_c"):
        try:
            fns += importlib.import_module(mod).SLIDES
        except ModuleNotFoundError:
            pass
    for f in fns[:upto]:
        f(prs)
    prs.save(OUT)
    print("saved", OUT, len(prs.slides), "slides")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 24)
