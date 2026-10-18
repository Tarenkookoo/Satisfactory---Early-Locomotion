"""Build "Early Locomotion, Explained" (42 slides) from OUTLINE.md.

Usage:
  python3 build_deck.py                 # build the deck
  python3 build_deck.py --render 1 10   # build, then render slides 1-10 to PNG
Renders go to $RENDER_DIR (default: ./build/render, which is not committed).
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'build'))

import lib  # noqa: E402
import slides_a  # noqa: E402

CHUNKS = [slides_a]
for mod in ('slides_b', 'slides_c', 'slides_d'):
    try:
        CHUNKS.append(__import__(mod))
    except ModuleNotFoundError:
        pass

OUT = os.path.join(HERE, 'Early_Locomotion_Explained.pptx')


def build():
    prs = lib.new_deck()
    n = 0
    for mod in CHUNKS:
        for fn in mod.SLIDES:
            n += 1
            fn(prs, n)
    lib.finalize(prs)
    prs.save(OUT)
    print('saved', OUT, n, 'slides')
    return OUT


def render(first, last):
    out = os.environ.get('RENDER_DIR', os.path.join(HERE, 'build', 'render'))
    os.makedirs(out, exist_ok=True)
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', out, OUT],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    pdf = os.path.join(out, 'Early_Locomotion_Explained.pdf')
    dpi = os.environ.get('RENDER_DPI', '80')
    subprocess.run(['pdftoppm', '-r', dpi, '-png', '-f', str(first), '-l', str(last), pdf,
                    os.path.join(out, 's')], check=True)
    print('rendered to', out)


if __name__ == '__main__':
    build()
    if '--render' in sys.argv:
        i = sys.argv.index('--render')
        render(int(sys.argv[i + 1]), int(sys.argv[i + 2]))
