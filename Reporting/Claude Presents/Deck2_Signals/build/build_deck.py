"""Build the Deck 2 .pptx from whichever chunk modules exist. Usage: python3 build_deck.py [out.pptx]"""
import importlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib import Deck  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    HERE, "..", "Signals_and_Signal_Boxes_Explained.pptx")


def main():
    d = Deck()
    n = 0
    for mod in ("chunk1", "chunk2", "chunk3"):
        if not os.path.exists(os.path.join(HERE, mod + ".py")):
            continue
        m = importlib.import_module(mod)
        for fn in m.SLIDES:
            fn(d)
            n += 1
    d.finalize(OUT)
    print(f"built {n} slides -> {os.path.normpath(OUT)}")


if __name__ == "__main__":
    main()
