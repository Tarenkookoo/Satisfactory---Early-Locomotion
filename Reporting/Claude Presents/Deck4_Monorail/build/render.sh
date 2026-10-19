#!/bin/sh
# Render the deck to PNGs (LibreOffice then pdftoppm at 80 dpi) into $1 (default: ../../scratch render dir).
# usage: render.sh <out_dir> [first] [last]
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
PPTX="$HERE/../The_Monorail_Transition_Explained.pptx"
OUT="${1:?output dir}"
mkdir -p "$OUT"
rm -f "$OUT"/*.png "$OUT"/*.pdf
soffice --headless --convert-to pdf --outdir "$OUT" "$PPTX" >/dev/null 2>&1
PDF="$OUT/The_Monorail_Transition_Explained.pdf"
if [ -n "$2" ]; then
  pdftoppm -r 80 -png -f "$2" -l "${3:-$2}" "$PDF" "$OUT/s"
else
  pdftoppm -r 80 -png "$PDF" "$OUT/s"
fi
ls "$OUT"
