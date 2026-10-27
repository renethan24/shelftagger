# Shelf Tag Printer — project context

Context for continuing this work in a new conversation.

## Goal
Print retail shelf tags for Maine Spirits items at Pine State Beverage, from an iPad, on a Brother QL-810W over Wi-Fi.

## Hard constraints
- **Fully local.** No hosting: anything hosted needs too many approval layers at work. The tool is a single self-contained HTML file with libraries inlined.
- **iPad.** Safari won't run JS in local files, so the file is opened in Microsoft Edge (Files → Share → Edge) or a local HTML runner app like HTML Serve. Not yet confirmed on the actual iPad.
- **Printing via AirPrint.** Page size is set with CSS `@page`, injected by JS based on the label-size toggle.

## Decisions so far
- Input: .xlsx preferred, .csv also supported (SheetJS reads both). First sheet only.
- Column headers come from the export exactly as listed in README.md. The period in `Item .` is intentional; the date headers include literal single quotes. Header matching is normalised (case, spaces, periods, quotes).
- Barcode encodes the **6-digit item number**, not the UPC. Code 128 default, Code 39 toggle. Item numbers are left-padded to 6 digits because Excel strips the leading zero.
- Size line format: `Size UOI/Units` (e.g. `700ML BTL/1`), matching the sample tag.
- Price default: Retail Price. Options for Sales Price, or Sales-if-set-else-Retail.
- Header text default "Maine Spirits", editable.
- Label sizes:
  - **Small:** 1.1" x 2.4" (DK-1209, 62 x 29 mm). The primary design, modelled on the sample tag. Not yet test-printed (no labels on hand).
  - **Large:** 2.4" x 3.9" (DK-1202, 62 x 100 mm), portrait, one tag per label, same fields scaled up. Being used for test prints now.
- Print area is kept filled on every selection change, so the browser's own Print menu works if `window.print()` doesn't fire in the viewer app.

- Barcode scanning: **Scan barcode** opens the camera through a file input (`capture="environment"`), then ZXing decodes the photo in the page. Chosen over a live camera feed because `getUserMedia` needs a secure origin, which a local file or data: URL may not be. Matches the product UPC column (leading zeros ignored, since Excel drops them) or a 6-digit item number from one of our own tags. One match is ticked; several matches are shown via the search box.

## Status / next steps
- Push to a new (empty) GitHub repository.
- Test print on 62 x 100 mm labels from the iPad; check alignment and the open-in-Edge flow.
- Possible: offset nudges if print alignment is off; 3-up small tags on a large label for testing the small size.

## Working preferences
Targeted, minimal changes over rewrites; one step at a time when debugging. Edit `src/template.html`, then run `build.py`.
