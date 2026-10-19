#!/bin/sh
# usage: RENDER_DIR=/some/dir ./render.sh [first] [last]
# Renders the deck with LibreOffice, then to PNG at 80 dpi (LibreOffice swaps Arial for the
# metric-compatible Liberation Sans, so overflow checks stay valid).
HERE="$(cd "$(dirname "$0")" && pwd)"
DECK="$HERE/../After_Launch_Late_Steam_Driving_and_Prestige_Explained.pptx"
OUT="${RENDER_DIR:-$HERE/render}"
mkdir -p "$OUT"
rm -f "$OUT"/*.png "$OUT"/*.pdf
soffice --headless --convert-to pdf --outdir "$OUT" "$DECK" >/dev/null 2>&1
PDF="$OUT/After_Launch_Late_Steam_Driving_and_Prestige_Explained.pdf"
if [ -n "$1" ]; then
  pdftoppm -r 80 -png -f "$1" -l "${2:-$1}" "$PDF" "$OUT/s"
else
  pdftoppm -r 80 -png "$PDF" "$OUT/s"
fi
ls "$OUT"
