#!/bin/bash
# Render the deck to PNGs (80 dpi) in the scratchpad: render.sh [first last]
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
OUTDIR="${RENDER_DIR:-/tmp/claude-0/-home-user-Satisfactory---Early-Locomotion/006e117b-f170-5b30-9a89-e1172c1aa238/scratchpad/render}"
mkdir -p "$OUTDIR"
rm -f "$OUTDIR"/*.png "$OUTDIR"/*.pdf
soffice --headless --convert-to pdf --outdir "$OUTDIR" "$HERE/../Coal_Water_and_Servicing_Explained.pptx" >/dev/null 2>&1
if [ -n "$1" ]; then
  pdftoppm -r 80 -png -f "$1" -l "$2" "$OUTDIR/Coal_Water_and_Servicing_Explained.pdf" "$OUTDIR/s"
else
  pdftoppm -r 80 -png "$OUTDIR/Coal_Water_and_Servicing_Explained.pdf" "$OUTDIR/s"
fi
ls "$OUTDIR"
