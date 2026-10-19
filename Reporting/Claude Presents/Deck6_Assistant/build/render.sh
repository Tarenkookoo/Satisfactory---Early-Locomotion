#!/bin/bash
# Render the deck to PNGs (80 dpi): render.sh [first last]
# Output goes to $RENDER_DIR (default: $TMPDIR/deck6_render, or /tmp/deck6_render).
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
OUTDIR="${RENDER_DIR:-${TMPDIR:-/tmp}/deck6_render}"
NAME="Railway_Guide_Lessons_and_Build_Menu_Explained"
mkdir -p "$OUTDIR"
rm -f "$OUTDIR"/*.png "$OUTDIR"/*.pdf
soffice --headless --convert-to pdf --outdir "$OUTDIR" "$HERE/../$NAME.pptx" >/dev/null 2>&1
if [ -n "$1" ]; then
  pdftoppm -r 80 -png -f "$1" -l "$2" "$OUTDIR/$NAME.pdf" "$OUTDIR/s"
else
  pdftoppm -r 80 -png "$OUTDIR/$NAME.pdf" "$OUTDIR/s"
fi
ls "$OUTDIR"
