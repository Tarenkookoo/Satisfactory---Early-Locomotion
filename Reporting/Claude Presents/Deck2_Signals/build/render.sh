#!/bin/sh
# Usage: render.sh <deck.pptx> <outdir>   (LibreOffice -> PDF -> PNG at 80 dpi)
set -e
mkdir -p "$2"
rm -f "$2"/*.png "$2"/*.pdf
soffice --headless --convert-to pdf --outdir "$2" "$1" >/dev/null 2>&1
pdftoppm -r 80 -png "$2"/*.pdf "$2/s"
ls "$2" | head -50
