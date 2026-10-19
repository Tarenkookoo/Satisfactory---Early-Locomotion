"""Build Deck 4. usage: python3 build_deck.py [max_slide]   (default: every slide that exists)

Output: ../The_Monorail_Transition_Explained.pptx
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib import new_deck  # noqa: E402

OUT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                   "The_Monorail_Transition_Explained.pptx"))


def collect():
    fns = []
    for mod in ("slides_a", "slides_b", "slides_c"):
        try:
            m = __import__(mod)
        except ModuleNotFoundError as e:
            if e.name == mod:
                continue
            raise
        fns.extend(m.SLIDES)
    return fns


def main():
    fns = collect()
    n = int(sys.argv[1]) if len(sys.argv) > 1 else len(fns)
    prs = new_deck("The Monorail Transition, Explained", "Explainer deck 4 of the Early Locomotion series")
    for fn in fns[:n]:
        fn(prs)
    prs.save(OUT)
    print("saved %s: %d slides, %.0f KB" % (OUT, len(prs.slides), os.path.getsize(OUT) / 1024))


if __name__ == "__main__":
    main()
