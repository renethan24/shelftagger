# Shelf Tag Printer

Offline shelf tag generator for a Brother QL-810W, run from an iPad. Load an item file (.xlsx or .csv), pick items, print tags over AirPrint. Everything runs in the page; no server, no internet.

## Files

| File | Purpose |
|---|---|
| `shelf-tags.html` | Ready-to-use build. This is the file that goes on the iPad. |
| `src/template.html` | Editable source (UI, tag layout, logic). Edit this, not the build. |
| `build.py` | Pastes the libraries into the template to produce `shelf-tags.html`. |

## Build

```
npm install
python3 build.py
```

Libraries: [SheetJS](https://sheetjs.com) 0.18.5 (reads .xlsx/.csv), [JsBarcode](https://github.com/lindell/JsBarcode) (draws barcodes) and [ZXing](https://github.com/zxing-js/library) 0.21.3 (reads barcodes from photos).

## Using it on the iPad

Safari won't run JavaScript in a local file, so open it in an app that will:

1. Copy `shelf-tags.html` to the iPad's Files app.
2. Long-press it → Share → **Microsoft Edge** (or open it in an app like HTML Serve).
3. Open your item file, tick items (or tap **Scan barcode** and photograph a product UPC or an existing shelf tag), set copies, tap **Print**. If the button does nothing, use the app's own Share → Print.

## Print settings

| Label | Brother roll | Paper size in iOS print dialog |
|---|---|---|
| 1.1" x 2.4" | DK-1209 | 29 x 62 mm |
| 2.4" x 3.9" | DK-1202 | 62 x 100 mm |

Choose the matching **Label size** in the app first; it sets the print page size.

## Input file

Reads the first sheet. Expected headers (matching ignores case, spaces, periods and quotes):

`Item .`, `Description`, `Size`, `UOI`, `Units`, `Proof`, `Product Category`, `UPC`, `Agency Cost`, `Agency Sale Cost`, `Agent Savings`, `Retail Price`, `Sales Price`, `Retail Savings`, `'Effective Start Date'`, `'Effective End Date'`

Required: `Item .`, `Description`, `Size`, `Retail Price`.

## Tag contents

- Header text (default "Maine Spirits", editable in the app)
- Size line: `Size UOI/Units`, e.g. `700ML BTL/1`
- Price: Retail, Sales, or Sales-if-set-else-Retail (selectable)
- Description
- Barcode of the item number (Code 128 default, Code 39 optional); item numbers are left-padded to 6 digits, or the UPC from the file (UPC-A / EAN-13)
- Item number
