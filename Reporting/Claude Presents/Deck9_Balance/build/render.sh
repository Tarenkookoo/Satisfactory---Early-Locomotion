#!/bin/bash
# usage: render.sh deck.pptx outdir  -> PNGs at 80 dpi (LibreOffice then pdftoppm)
set -e
in="$1"; out="$2"; mkdir -p "$out"
soffice --headless --convert-to pdf --outdir "$out" "$in" >/dev/null 2>&1
pdf="$out/$(basename "${in%.pptx}").pdf"
rm -f "$out"/s-*.png
pdftoppm -r 80 -png "$pdf" "$out/s"
ls "$out"/s-*.png | wc -l
