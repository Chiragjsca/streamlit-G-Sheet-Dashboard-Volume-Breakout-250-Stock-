# 🛠️ Update Notes — Top 250 NSE Stock-Volume Breakout Dashboard

This update fixes 3 reported bugs and adds 2 requested features to the dashboard. Everything else in the app is unchanged.

---

## ✨ What's Fixed & Added

- **🔗 NSE URL Hyperlink — Now Works for Both "Symbol" & "NSE Code"** – Previously the chart link only rendered when the identifier column was literally named *NSE Code*. It now works no matter what that column is called (Symbol, NSE Code, Ticker, etc.), and the link label no longer shows a redundant `nse ` prefix — just the clean stock name.
- **🌍 3 New URLs in National Live Market Analytics Portal Framework** – Added *Securities Available for Trading*, *Corporate Filings & Announcements*, and *52-Week Low Equity Market* as new embedded tabs.
- **🧹 "Clear All Filters" Button — Actually Clears Everything Now** – Previously it reset the sidebar filters but left the data grid's own in-grid column filters/sort stuck. It now force-resets the grid too.
- **🔍 "Search Symbol" Box Added to Top 250 Stocks Matrix** – A quick filter box now sits directly above the main grid, matching the style already used in the Performance Matrix section.
- **📜 New "Rules" Tab Added to Global Market News, Alerts & Corporate Announcements** – A dedicated tab now displays your personal trading rules (52W High/Low logic, the Diff @ 200 DMA strategy, risk-management rules), editable from one place in the code.

---

## 📖 User Guide — What Changed, Section by Section

### 1. NSE URL Hyperlink Fix
**Where:** Main "Top 250 Stocks" data grid (and any other sheet tab).
**Before:** If the Google Sheet's identifier column header was `Symbol`, clicking the cell did nothing — the link only worked when the header was `NSE Code`.
**Now:** Whichever column you pick under sidebar → **⚙️ Settings → Symbol Column**, that column always becomes a clickable NSE chart link (`https://charting.nseindia.com/?symbol=...-EQ`), regardless of its header text.
**Bonus cleanup:** The cell text used to read `nse IDEA`, `nse NYKAA`, etc. It now just shows `IDEA`, `NYKAA` — saving column width.

> 💡 Root cause (for reference): there were *two* separate places in the code checking "is this an NSE column?" — one that built the link's HTML, and a second one in the grid setup that decided whether to actually *render* that HTML as a clickable link or show it as plain text. Both now also check "is this the chosen Symbol column?" in addition to checking the header text.

### 2. National Analytics Portal — New Tabs
**Where:** 🌍 National Live Market Analytics Portal Framework section.
**Added 3 new tabs** at the end of the existing 27:

| New Tab | URL |
|---|---|
| ✅ Securities Available | nseindia.com/static/market-data/securities-available-for-trading |
| 🏛️ Corporate Filings | nseindia.com/companies-listing/corporate-filings-announcements |
| 📉 52W Low Market | nseindia.com/market-data/52-week-low-equity-market |

Each opens the same way as every other portal tab — an embedded iframe plus an "🌐 Open in Browser" button for mobile.

### 3. Clear All Filters — Real Fix
**Where:** Sidebar → 🧹 Clear All Filters button.
**Before:** Pressing it reset sidebar widgets (sliders, dropdowns, search boxes) but the **data grid's own column filter icons** (the ones you click directly inside the table header) stayed stuck — because the grid component keeps its own internal state tied to a fixed identifier, separate from the sidebar.
**Now:** Pressing the button also forces the grid to fully remount, wiping its internal filter/sort state. It also now clears the new matrix search boxes (see #4) and the Bottom Fishing Scanner's search box.

### 4. Search Symbol Box — Top 250 Stocks Matrix
**Where:** Directly above the main grid, next to the "Column Width Adjustment" control.
**What it does:** Type any part of a symbol name to instantly filter the visible rows — same behavior as the existing search box in the Multi-Horizon Performance Matrix section. Filtering also affects the Excel export and the Rows/Columns counter, so what you see is what you download.

### 5. Rules Tab — Global Market News Section
**Where:** 📰 Global Market News, Alerts & Corporate Announcements → new **📜 Rules** tab (after "DOCUMENTS HUB").
**What it shows:**
- Core sheet/trading conventions (always use NSE Code, never compromise on rules, timing edge).
- 🟢/🟠 Rule 1 & 2 — what the Green/Orange CMP highlight near 52W High/Low means.
- 52W Low/High Date color meaning table (18 days / 30 days / 1 year ago).
- 🔵 Rule 3 — the full "Diff @ 200 DMA" strategy, including the mind-map flow (`−40% → −30% → −20% → −10%`).
- Quick links to the NSE All Reports, Securities Available, and 52-Week Low pages.
- 🛑 Risk-management rules (stop-loss %, risk-reward ratio, profit booking, priority order: IPO → F&O → 52W Low).

**To edit these rules later:** open `app.py` and find the `TRADING_RULES_LIBRARY` constant near the top of the file (right next to `SUGGESTED_AI_PROMPTS` and `PINE_CUSTOM_RULES`). It's plain Markdown text — edit it directly and the Rules tab updates automatically.

---

## 🔧 Reference: Editable Constants in `app.py`

| Constant | Purpose | Location |
|---|---|---|
| `SUGGESTED_AI_PROMPTS` | Pre-built prompts for the AI Stock Analysis tab | Top of file |
| `PINE_CUSTOM_RULES` | Pine Script strategy templates for the AI Pine Script Builder | Top of file |
| `TRADING_RULES_LIBRARY` | **(New)** Content shown in the Rules tab | Top of file |

---

## ✅ Quick Test Checklist

- [ ] Set Symbol Column to a header that does **not** contain "nse" (e.g. `Symbol`) → confirm the cell is a clickable link with no `nse ` prefix.
- [ ] Open the 3 new Portal tabs → confirm each iframe loads (or use "Open in Browser" on mobile).
- [ ] Apply a filter using the grid's own column filter icon, then click "Clear All Filters" → confirm it actually clears.
- [ ] Type a symbol into the new "Search symbol" box above the main grid → confirm rows filter live.
- [ ] Open the new **📜 Rules** tab under Global Market News → confirm your rules render correctly.
