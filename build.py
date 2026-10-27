#!/usr/bin/env python3
"""Build shelf-tags.html: paste the JS libraries into src/template.html.

Usage:
    npm install          # once, fetches xlsx + jsbarcode into node_modules/
    python3 build.py     # writes shelf-tags.html
"""
from pathlib import Path

ROOT = Path(__file__).parent
LIBS = {
    "/*XLSX_LIB*/": ROOT / "node_modules/xlsx/dist/xlsx.full.min.js",
    "/*JSBARCODE_LIB*/": ROOT / "node_modules/jsbarcode/dist/JsBarcode.all.min.js",
    "/*ZXING_LIB*/": ROOT / "node_modules/@zxing/library/umd/index.min.js",
}

html = (ROOT / "src/template.html").read_text(encoding="utf-8")
for marker, path in LIBS.items():
    if marker not in html:
        raise SystemExit(f"Marker {marker} not found in template")
    if not path.exists():
        raise SystemExit(f"Missing {path} - run `npm install` first")
    # Escape any closing script tags inside the library so the page doesn't break.
    lib = path.read_text(encoding="utf-8").replace("</script", "<\\/script")
    html = html.replace(marker, lib)

out = ROOT / "shelf-tags.html"
out.write_text(html, encoding="utf-8")
print(f"Wrote {out} ({out.stat().st_size:,} bytes)")
