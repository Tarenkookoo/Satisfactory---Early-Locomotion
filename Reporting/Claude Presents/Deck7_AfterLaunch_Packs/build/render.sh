#!/bin/bash
# usage: render.sh file.pptx outdir [dpi]
f="$1"; out="$2"; dpi="${3:-80}"
mkdir -p "$out"; rm -f "$out"/*.png "$out"/*.pdf
soffice --headless --convert-to pdf --outdir "$out" "$f" >/dev/null 2>&1
pdf="$out/$(basename "${f%.pptx}").pdf"
pdftoppm -r "$dpi" -png "$pdf" "$out/s"
ls "$out" | head -40
