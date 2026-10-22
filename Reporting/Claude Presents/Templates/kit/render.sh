#!/bin/bash
# Render a deck to PNGs with LibreOffice (80 dpi): render.sh FILE.pptx [OUTDIR] [DPI]
# LibreOffice is NOT PowerPoint: use this to catch overflow, overlap and missing shapes, then open the file in
# PowerPoint for the real check. Needs soffice and pdftoppm on the PATH.
set -e
F="${1:?usage: render.sh FILE.pptx [OUTDIR] [DPI]}"
OUT="${2:-${TMPDIR:-/tmp}/el_render}"
DPI="${3:-80}"
mkdir -p "$OUT"
rm -f "$OUT"/*.png "$OUT"/*.pdf
soffice --headless --convert-to pdf --outdir "$OUT" "$F" >/dev/null 2>&1
B="$(basename "${F%.*}")"
pdftoppm -r "$DPI" -png "$OUT/$B.pdf" "$OUT/s"
ls "$OUT"
