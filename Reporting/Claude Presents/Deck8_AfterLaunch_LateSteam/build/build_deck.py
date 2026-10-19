"""Build Deck 8. usage: python3 build_deck.py  (writes the .pptx one folder up)."""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib

OUT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..',
                      'After_Launch_Late_Steam_Driving_and_Prestige_Explained.pptx'))


def main():
    prs = lib.new_deck()
    for modname in ('slides_a', 'slides_b', 'slides_c'):
        try:
            mod = __import__(modname)
        except ModuleNotFoundError:
            continue
        mod.build(prs)
    lib.save(prs, OUT)
    print('wrote', OUT, os.path.getsize(OUT), 'bytes,', len(prs.slides), 'slides')


if __name__ == '__main__':
    main()
