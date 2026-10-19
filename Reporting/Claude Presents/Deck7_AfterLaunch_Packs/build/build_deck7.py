"""Build Deck 7. usage: python3 build_deck7.py [last_slide] [out.pptx]
Builds slides 1..last_slide (default: all 24). The deliverable is built with no arguments."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import el_lib as L

ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))   # Reporting/Claude Presents
L.IMG_DIR = os.path.join(ROOT, 'images')
OUT_DEFAULT = os.path.join(HERE, '..', 'After_Launch_Packs_Locomotives_and_History_Explained.pptx')


def main():
    last = int(sys.argv[1]) if len(sys.argv) > 1 else 24
    out = sys.argv[2] if len(sys.argv) > 2 else OUT_DEFAULT
    builders = []
    import slides_1_8
    builders += slides_1_8.BUILDERS
    try:
        import slides_9_16
        builders += slides_9_16.BUILDERS
    except ImportError:
        pass
    try:
        import slides_17_24
        builders += slides_17_24.BUILDERS
    except ImportError:
        pass
    prs = L.new_deck()
    for b in builders[:last]:
        b(prs)
    prs.save(out)
    print('saved', out, len(prs.slides._sldIdLst), 'slides')


if __name__ == '__main__':
    main()
