# 📊 Top 250 NSE Stock-Volume Breakout Dashboard

A professional, all‑in‑one dashboard for Indian stock market analysis.
It combines live data from Google Sheets, AI (Gemini/Groq), advanced filtering, watchlists, a **bottom‑fishing** score, a GTT order calculator, a global market news & alerts engine, dozens of embedded market portals, and much more.

---

## 🆕 Latest Update

- **🔗 NSE URL hyperlink fixed** — now works no matter what the identifier column is named (`Symbol`, `NSE Code`, `Ticker`, etc.), and the link label no longer shows a redundant `nse ` prefix.
- **🌍 3 new portal tabs** — Securities Available for Trading, Corporate Filings & Announcements, 52‑Week Low Equity Market (Portal Framework is now 30 tabs).
- **🧹 "Clear All Filters" actually clears everything** — including the data grid's own in‑grid column filters, not just the sidebar widgets.
- **🔍 New "Search symbol" box** above the main Top 250 Stocks grid.
- **📜 New "Rules" tab** under Global Market News, with your personal trading rules, fully editable from one constant in the code.

Full write‑up in the [Changelog](#-changelog--latest-fixes) section at the bottom.

---

## ✨ Key Features

- **📈 Live Market Indices** – NIFTY 50, NIFTY Next 50, NIFTY Midcap 50, etc. (Yahoo Finance, refreshes every 60s).
- **🏢 Top 250 Stocks Matrix** – CMP & daily % change cards, fully linked to NSE, with a quick symbol search box.
- **🏆 Advanced Ranking Dashboards** – Gainers/Losers, Volume Leaders, Most Active (Volume & Value), Top by Turnover.
- **🌍 National Exchange Scanner** – Embedded TradingView screeners for **all NSE/BSE** stocks (Gainers, Losers, 52W High/Low, Reversals, Top 100 Traded).
- **📄 Google Sheets Integration** – 6 different sheets (`Top 250 Stocks`, `Final List`, `Diff @ 200 DMA`, etc.) with full colour preservation.
- **🎨 Powerful Filtering** – Global search, colour filters, numeric sliders, DMA trend filters (e.g. 50 DMA > 200 DMA), date filters — and a one‑click "Clear All Filters" that now resets the data grid too.
- **🔗 NSE Chart Hyperlinks** – Work on the identifier column regardless of whether it's named *Symbol* or *NSE Code*; labels show the clean stock name only.
- **🤖 AI Analysis** – Gemini or Groq (Llama 3.3) analyses any selected stock using live sheet data. Pre‑defined prompts, exportable history.
- **💻 Pine Script Generator** – AI writes TradingView Pine Script v5 strategies (Volume Breakout, Moving Average Crossover, Trend Following, Mean Reversion).
- **🔬 Bottom Fishing Score** – 0–100 score based on 8 criteria (proximity to 52W low, uptrend, volume, debt, profit, RONW, promoter holding, pledge). Grades: Strong Buy / Watchlist / Caution / Avoid.
- **🎯 GTT Order Calculator** – Auto‑suggest Stop‑Loss (1×, 1.5×, 2× ATR), multiple targets (1R, 2R, 3R), position sizing, copy‑ready order summary.
- **📝 Watchlist Manager** – Persistent watchlist stored in a Google Sheet. Add notes, download Excel, share via WhatsApp/Telegram.
- **📅 Multi‑Horizon Performance Matrix** – Returns for 24 time horizons (1 day … 3 years) plus volume, coloured by performance.
- **🧭 National Analytics Portal** – 30 embedded iframes (NSE official pages, Moneycontrol, Chartink, Screener, ScanX, IPO Watch, etc.) with "Open in Browser" fallback.
- **📰 Global Market News, Alerts & Corporate Announcements** – Circuit/52‑week breakout alerts, per‑stock alert feeds, a smart news engine, official corporate filings, a BSE Documents Hub, and an editable **Rules** tab.
- **📥 Full Excel Export** – Export filtered grids, watchlist, AI history, bottom‑fishing results.
- **🖼️ Responsive Design** – Works on desktop and mobile (with external links for embedded iframes).

---

## 📖 User Guide

This dashboard is a complete technical & fundamental analysis platform for the top 250 NSE stocks, plus a full-market scanner for all NSE/BSE equities. It combines live data from Google Sheets, AI analysis (Gemini/Groq), advanced filtering, a watchlist manager, a bottom‑fishing score, a GTT order calculator, a market news & alerts engine, and dozens of embedded market portals.

### 1. Login
A simple admin login gate protects the dashboard before any data loads.

### 2. Live Market Indices (Top Section)
- Displays NIFTY 50, NIFTY NEXT 50, NIFTY MIDCAP 50 and other key indices.
- Data is fetched from Yahoo Finance (refreshed every 60 seconds).
- Each card shows: index name, current price, daily % change (green/red).
- Click on any card → opens the official NSE live‑indices page.

💡 If no cards appear, Yahoo Finance data may be temporarily unavailable.

### 3. Top 250 Stocks Matrix & Ranking Dashboards

**3.1 Stock Ticker Cards**
- Shows CMP and daily % change for each stock in the "Top 250 Stocks" sheet.
- Click a card → opens NSE quote page.

**3.2 Advanced Ranking Dashboards (6 tabs)**

| Tab | What it shows |
|---|---|
| Gainers/Losers | Top 20 gainers & top 20 losers by % change |
| Volume Leaders | Highest & lowest 20 by volume |
| Active (Vol & Val) | Top 20 by volume, displaying both volume & traded value |
| Top by Value | Top 20 by traded value (₹) |
| Top by Turnover | Top 20 by turnover (₹) |
| Most Active | Top 20 by traded value (repeated, for convenience) |

Each card includes: symbol, price, and a metric pill (e.g. `+2.5%` or `Vol: 1.2M`).

### 4. National Exchange Scanner (All NSE/BSE Stocks)
Embedded TradingView screeners inside 5 tabs:

| Tab | Content |
|---|---|
| Gainers & Losers | Top gainers / top losers |
| Volume & Active | Volume leaders & most active (turnover) |
| 52W High / Low | New 52‑week highs / lows |
| 52W Reversals | Outperforming 52W high / underperforming 52W low |
| Top 100 Traded | General screener – sort by any metric |

📱 If an iframe is blank on mobile, use the "Open in Browser" button above it.

### 5. Main Data Grid (Google Sheets)

**5.1 Sheet selection (sidebar)**
Choose from: `Top 250 Stocks` | `Final List` | `Final List 2` | `Diff @ 200 DMA` | `+%` | `-%`

**5.2 Powerful filtering (sidebar)**
- Global search – any column.
- Color filters – filter cells by background colour (e.g. all green cells in a column).
- Categorical filters – Industry, Sector, Output, Start GTT Order, etc.
- DMA trend filter – e.g. `50 DMA > 200 DMA`.
- Numeric range sliders – Volume, CMP, Promoters %, Net Profit, EPS, RONW %, Market Cap, Diff from 200 DMA, From 52W Low %, From 52W High %.
- Date filters – 52W high / low dates (Past 5 days … Past 1 year).

**5.3 "Search symbol" box (above the grid)** 🆕
A dedicated quick filter sits right above the main grid — type any part of a symbol to instantly narrow the rows shown, without touching the sidebar. It also drives what gets exported to Excel and what the Rows/Columns counter reports.

**5.4 Interactive table (AgGrid)**
- Click on any row → opens the Workspace Panel (see section 6).
- Columns are dynamically coloured to match Google Sheets' background/text colours.
- Links (NSE chart, TradingView, Screener, Zerodha, etc.) are clickable directly in the grid — the identifier column links correctly whether it's named *Symbol* or *NSE Code*.
- Column width can be set to auto‑fit row 1 or row 2.
- The grid's own in‑grid column filters are fully reset by the sidebar's "Clear All Filters" button.

**5.5 Export**
Download the currently filtered table as Excel (all colours removed).

### 6. Workspace Panel (after selecting a stock)
When you click a row in the main grid, a detailed panel appears with 11 tabs:

| Tab | Description |
|---|---|
| Chart & Trade Info | NSE interactive chart (if the iframe is blocked, tap the "Open in Browser" link) |
| History Data | EquityPandit historical data iframe |
| Bullish/Bearish Zone | EquityPandit zone indicator |
| Screener Documents | Screener.in consolidated financials |
| Zerodha Portal | Zerodha markets page |
| MarketSmith India | Institutional evaluation |
| TradingView Profile | Asset profile from TradingView |
| 🤖 AI Stock Analysis | Ask AI (Gemini or Groq) about the stock using live sheet data. Includes suggested prompts, WhatsApp/Telegram share, and Excel export of AI history. |
| 💻 AI Pine Script Builder | Generate a complete TradingView Pine Script v5 strategy based on the stock's data. Choose from 4 strategy templates + add custom rules. |
| 🔬 Bottom Fishing Score | Scores the stock (0–100) for buying near the 52W low. Shows grade (Strong Buy / Watchlist / Caution / Avoid) and detailed reasoning (proximity to low, uptrend, volume, debt, profit, RONW, promoter holding, pledge). |
| 🎯 GTT Order Calculator | Automatically suggests stop‑loss (tight/standard/wide), targets (1R, 2R, 3R), ATR, position sizing, and a copy‑ready GTT summary. Share via WhatsApp/Telegram. |

(Watchlist Manager is also reachable from this panel and from the sidebar — see section 8.)

### 7. AI Features (Gemini & Groq)

**Requirements**
- Add `GEMINI_API_KEY` and/or `GROQ_API_KEY` to Streamlit secrets.
- If both are present, you can choose between ⚡ Groq (Llama 3.3 70B) and 🧠 Gemini 2.5 Flash.

**AI Stock Analysis**
- Select a stock from the grid, go to the AI tab.
- Type your own question or pick from 10 suggested prompts (technical summary, entry zone, volume analysis, fundamentals, risk profile, buy/hold/sell recommendation, etc.).
- The AI receives the full live row data (CMP, volumes, DMAs, fundamentals, etc.) and answers contextually.
- Results are saved in `st.session_state.ai_history` and can be exported as a combined Excel file.

**AI Pine Script Builder**
- Choose a strategy focus (volume breakout, moving average crossover, trend following, mean reversion).
- Add custom rules (e.g., "use ATR trailing stop").
- AI generates ready‑to‑paste Pine Script v5 code.
- Code can be saved as Excel.

**Bottom Fishing AI Deep Analysis**
- Inside the Bottom Fishing Score tab, click "Get AI Deep Analysis".
- AI analyses the BF score, scoring breakdown, and gives specific entry/exit advice.

### 8. Watchlist Manager
- Stored in Google Sheet (tab name `Watchlist`) – persistent across sessions.
- Columns: `Symbol`, `CMP`, `Note`, `BF Score`, `BF Grade`, `Added On`.
- Add stocks from the Watchlist Manager tab of the workspace panel.
- View, download, or share your watchlist directly from the sidebar or the workspace tab.

⚠️ If sheet write fails, check your `gcp_service_account` secrets.

### 9. Bottom Fishing Scanner (Standalone)
- Located after the main grid.
- Scores every stock from 0–100 based on 8 criteria (see table below).
- Slider to set minimum BF score (default 55 = Watchlist grade).
- Sort by score high→low or low→high.
- Search a specific symbol.
- Results show Symbol, Score, Grade, CMP, Sector, and the top 3 reasons.
- Export results as Excel.

| Criteria | Max Points |
|---|---|
| CMP within 8–15% of 52W low | 30 |
| CMP > 200 DMA (uptrend) | 15 |
| High volume (≥ 10M) | 10 |
| Low / zero debt (D/E ≤ 0.1) | 10 |
| Positive net profit | 10 |
| RONW ≥ 15% | 10 |
| Promoter holding ≥ 50% | 8 |
| Zero pledged shares | 7 |

**Grades:** 🟢 STRONG BUY (≥75) | 🟡 WATCHLIST (55–74) | 🟠 CAUTION (35–54) | 🔴 AVOID (<35)

### 10. Multi‑Horizon Performance Summary Matrix
- Displays percentage returns over 24 time horizons (1 day, 2 days, … 3 years) plus Volume.
- Ranks stocks based on any chosen horizon.
- Includes BF Score & Grade columns.
- Colours: green background for positive returns, red for negative.
- Click the STOCK NAME cell → opens NSE chart.
- Filter by symbol, adjust column widths, and export is available via the main Excel download.

### 11. Daily Top / Bottom Performers
- Shows 10 best and 10 worst daily performers (based on the Price % column).
- Each badge is a clickable link to the NSE chart.

### 12. National Analytics Portal (30 tabs)
A huge collection of embedded financial portals:

**NSE official:** Most Active, Volume Gainers, Top Gainers/Losers, 52‑Week High/Low, Stocks Traded, Advances/Declines, Pre‑Open Market, Price Band Hitters, Index Heatmap, IPO Tracker, Document Reports, Securities Available for Trading 🆕, Corporate Filings & Announcements 🆕, 52‑Week Low Equity Market 🆕

**Third‑party:** Volume Shockers (Moneycontrol), TradingView Scripts, MunafaSutra, Dhan stock lists, ScanX (custom & live screener), Screener.in explore, Chittorgarh IPO, IPO Watch, NSE Pulse, Chartink (screeners, dashboard, atlas), Mahesh Kaushik, EFTI Wealth

Each tab has an "Open in Browser" button – use it if the iframe does not load on mobile.

### 13. Global Market News, Alerts & Corporate Announcements 🆕
A dedicated section that scans the currently filtered stocks for news and filings, with 7 tabs:

| Tab | What it does |
|---|---|
| 🚨 Latest Alerts Timeline | Consolidated feed of circuit‑breakout & 52‑week boundary alerts across the top 30 filtered stocks, with search, time filter (Today / Past 7 Days / All), and sort order. |
| 🏢 Alerts by Stock | The same alerts grouped per stock, in expandable cards (top 3 shown, rest collapsible). |
| 📰 Smart News Engine (1 Day) | General news headlines from the last 24 hours for the top 10 filtered stocks. |
| 📰 Smart News Engine (All News) | All‑time general news headlines for the top 10 filtered stocks. |
| 📢 Corporate Announcements | Official Regulation 30 / LODR filings — board meetings, AGMs, analyst meets — for the top 15 filtered stocks. |
| 📢 DOCUMENTS HUB | Pick specific stocks and pull live BSE filings: Announcements, Annual Reports, Credit Ratings, Concalls/PPT, with quick‑access buttons to BSE, NSE, and Screener.in. |
| 📜 Rules | Your personal trading rules — 52W High/Low highlight logic, the Diff @ 200 DMA strategy (with mind map), risk‑management rules, and quick reference links. Fully editable — see [Editable Constants](#-editable-constants-reference). |

### 14. Sidebar Controls – Summary
- **Clear All Filters** – reset every sidebar filter/search **and** the data grid's own in‑grid filters/sort.
- **Global Search** – case‑insensitive search across all visible columns.
- **Sheet selector** – change the active Google Sheet.
- **Symbol Column** – choose which column contains the stock symbol (works whether it's named *Symbol* or *NSE Code*).
- **Color Filters** – pick a column and select background colours to show.
- **Categorical Filters** – Industry, Sector, Output, etc.
- **DMA Trend Filter** – e.g. `50 DMA < 100 DMA < 200 DMA`.
- **Numeric sliders** – Volume, CMP, Promoters %, Net Profit, EPS, RONW, etc.
- **Date filters** – 52W high / low date.
- **Watchlist manager** – view / remove stocks, download watchlist Excel.
- **AI History Export** – download all AI queries and answers.

### 15. Data Freshness & Caching
- Google Sheets data: cached for 300 seconds (5 minutes).
- Live indices (Yahoo Finance): cached for 60 seconds.
- Use the browser refresh or the "Clear All Filters" button to force a reload.

---

## 📊 Comprehensive Details

### 🎯 Core Purpose
A comprehensive technical & fundamental analysis platform for the top 250 NSE (National Stock Exchange) stocks, combined with a full-market scanner for all NSE/BSE equities and a news/alerts engine. It integrates real-time data, AI analysis, and advanced trading tools.

### 📈 Major Features Explained

**1. Live Market Indices (Real-time Updates)**
- Displays **NIFTY 50, NIFTY Next 50, NIFTY Midcap 50**, and other indices.
- **Data Source:** Yahoo Finance (refreshes every 60 seconds).
- **Display:** Index name, current price, daily % change (color-coded green/red).
- **Interaction:** Clicking a card opens the NSE live indices page.

**2. Top 250 Stocks Matrix**
- Shows **Current Market Price (CMP)** and **daily % change** for each stock.
- All cards are **linked to NSE quote pages**.
- A **"Search symbol" box** above the main grid lets you instantly narrow the rows shown.
- Advanced ranking tabs: Gainers/Losers, Volume Leaders, Active (Vol & Val), Top by Value, Top by Turnover, Most Active.

**3. National Exchange Scanner (All NSE/BSE Stocks)**
- **5 TradingView screener tabs:** Gainers & Losers, Volume & Active traders, 52‑Week High/Low, 52‑Week Reversals, Top 100 Traded stocks.
- Mobile-friendly with "Open in Browser" fallback for blocked iframes.

**4. Google Sheets Integration**
- **6 different sheets available:** Top 250 Stocks, Final List, Final List 2, Diff @ 200 DMA, +% (positive % performers), -% (negative % performers).
- **Full color preservation** from Google Sheets.

**5. Powerful Filtering System (Sidebar)**
- **Global search** – case-insensitive across all columns.
- **Color filters** – filter by background color (e.g., all green cells).
- **Categorical filters** – Industry, Sector, Output, Start GTT Order, etc.
- **DMA trend filters** – Example: `50 DMA > 200 DMA` (uptrend detection).
- **Numeric sliders** for: Volume, Current Market Price (CMP), Promoters %, Net Profit, EPS, RONW %, Market Cap, Diff from 200 DMA, From 52W Low %, From 52W High %.
- **Date filters** – 52W high/low dates (Past 5 days to Past 1 year).

**6. Interactive Data Grid (AgGrid)**
- **Dynamic color coding** – matches Google Sheets' background/text colors.
- **Clickable links** – NSE chart, TradingView, Screener, Zerodha, and other portals; the identifier column always renders as a clickable NSE chart link regardless of its header text.
- **Row selection** – opens the **Workspace Panel** (see below).
- **Export** – download filtered data as Excel (colors removed).
- **Clear All Filters** fully resets both the sidebar filters and the grid's own column filters.

### 🛠️ Workspace Panel (11 Detailed Tabs)
When you select a stock from the grid:

1. **Chart & Trade Info** – NSE interactive chart with trading information
2. **History Data** – EquityPandit historical data
3. **Bullish/Bearish Zone** – EquityPandit zone indicator
4. **Screener Documents** – Screener.in consolidated financials
5. **Zerodha Portal** – Zerodha markets page
6. **MarketSmith India** – Institutional evaluation metrics
7. **TradingView Profile** – Asset profile and technical analysis
8. **🤖 AI Stock Analysis** – Ask AI (Gemini or Groq) contextual questions
9. **💻 AI Pine Script Builder** – Auto-generate TradingView Pine Script v5 strategies
10. **🔬 Bottom Fishing Score** – 0–100 score for value investing
11. **🎯 GTT Order Calculator** – Auto-suggest stop-loss & targets

### 🤖 AI Features (Gemini & Groq)

**Requirements:**
- Add `GEMINI_API_KEY` and/or `GROQ_API_KEY` to Streamlit secrets.
- Choose between **Groq (Llama 3.3 70B)** or **Gemini 2.5 Flash**.

**AI Stock Analysis:**
- 10 suggested prompts: technical summary, entry zone analysis, volume analysis, fundamental review, risk profile, buy/hold/sell recommendation, etc.
- AI receives **full live row data** (CMP, volumes, DMAs, fundamentals).
- Results stored in session state and **exportable as Excel**.

**AI Pine Script Builder:**
- Choose strategy focus: Volume Breakout, Moving Average Crossover, Trend Following, Mean Reversion.
- Add custom rules (e.g., "use ATR trailing stop").
- Generates **ready-to-paste Pine Script v5 code**.
- Can be saved as Excel.

### 🔬 Bottom Fishing Score (Value Investing Tool)

**What it does:** Identifies stocks trading near 52-week lows with upside potential.

**Scoring Criteria (0–100 points):**

| Criteria | Max Points |
|---|---|
| CMP within 8–15% of 52W low | 30 |
| CMP > 200 DMA (uptrend) | 15 |
| High volume (≥ 10M) | 10 |
| Low/zero debt (D/E ≤ 0.1) | 10 |
| Positive net profit | 10 |
| RONW ≥ 15% | 10 |
| Promoter holding ≥ 50% | 8 |
| Zero pledged shares | 7 |

**Grades:**
- 🟢 **STRONG BUY** (≥75)
- 🟡 **WATCHLIST** (55–74)
- 🟠 **CAUTION** (35–54)
- 🔴 **AVOID** (<35)

**Features:**
- Slider to set minimum BF score (default 55).
- Sort by score (high→low or low→high).
- Symbol search.
- Results show Score, Grade, CMP, Sector, and top 3 reasons.
- Export results as Excel.
- AI Deep Analysis available inside the tab.

### 🎯 GTT Order Calculator

**Auto-suggests:**
- **Stop-Loss Options:** Tight (1× ATR), Standard (1.5× ATR), Wide (2× ATR).
- **Multiple Targets:** 1R, 2R, 3R (risk-reward ratios).
- **Position Sizing** – calculates based on your account size.
- **Copy-ready GTT Summary** – shareable via WhatsApp/Telegram.

### 📝 Watchlist Manager

**Storage:** Persistent Google Sheet named "Watchlist".

**Columns:** Symbol, CMP, Note, BF Score, BF Grade, Added On.

**Features:**
- Add/remove stocks from any workspace panel.
- View, download, share via WhatsApp/Telegram.
- Accessible from sidebar or workspace tab.

### 📅 Multi-Horizon Performance Matrix
- **24 time horizons:** 1 day, 2 days, 3 days... 3 years.
- **Color coding:** Green = positive returns, Red = negative.
- **Includes:** BF Score & Grade columns.
- **Sortable** by any horizon.
- **Clickable stock names** → opens NSE chart.

### 🧭 National Analytics Portal (30 Tabs)

**NSE Official Pages:** Most Active, Volume Gainers, Top Gainers/Losers, 52-Week High/Low, Stocks Traded, Advances/Declines, Pre-Open Market, Price Band Hitters, Index Heatmap, IPO Tracker, Document Reports, Securities Available for Trading 🆕, Corporate Filings & Announcements 🆕, 52‑Week Low Equity Market 🆕

**Third-Party Portals:** Volume Shockers (Moneycontrol), TradingView Scripts, MunafaSutra, Dhan stock lists, ScanX (custom & live screener), Screener.in explore, Chittorgarh IPO, IPO Watch, NSE Pulse, Chartink (screeners, dashboard, atlas), Mahesh Kaushik, EFTI Wealth

### 📰 Global Market News, Alerts & Corporate Announcements

| Tab | Description |
|---|---|
| Latest Alerts Timeline | Circuit/52W alerts across top 30 filtered stocks, searchable & sortable |
| Alerts by Stock | Same alerts, grouped per stock |
| Smart News Engine (1 Day) | News from last 24 hours, top 10 stocks |
| Smart News Engine (All News) | All-time news, top 10 stocks |
| Corporate Announcements | Regulation 30 / LODR filings, top 15 stocks |
| Documents Hub | Live BSE filings: announcements, annual reports, credit ratings, concalls/PPT |
| Rules 🆕 | Personal trading rules — editable via `TRADING_RULES_LIBRARY` in the code |

### 📥 Data Freshness & Caching

| Data Source | Cache Duration |
|---|---|
| Google Sheets | 300 seconds (5 minutes) |
| Live indices (Yahoo Finance) | 60 seconds |

**Force Refresh:** Use browser refresh or "Clear All Filters" button.

### 🔧 Editable Constants Reference

| Constant | Purpose | Location |
|---|---|---|
| `SUGGESTED_AI_PROMPTS` | Pre-built prompts for the AI Stock Analysis tab | Top of `app.py` |
| `PINE_CUSTOM_RULES` | Pine Script strategy templates for the AI Pine Script Builder | Top of `app.py` |
| `TRADING_RULES_LIBRARY` 🆕 | Content shown in the Global Market News → Rules tab | Top of `app.py` |

### 🏆 Key Advantages

✅ **All-in-one solution** – No need to jump between multiple platforms
✅ **AI-powered insights** – Contextual analysis with Gemini or Groq
✅ **Value investing focus** – Bottom fishing score identifies bargains
✅ **Trading-ready tools** – GTT calculator, Pine Script generator
✅ **Comprehensive data** – 250 stocks + full NSE/BSE scanner + market news engine
✅ **Responsive design** – Works on desktop and mobile
✅ **Persistent storage** – Watchlists and AI history saved
✅ **Export capabilities** – Download all data as Excel
✅ **Reliable filtering** – "Clear All Filters" now resets everything, including the grid

---

## 🆕 Changelog — Latest Fixes

### 1. NSE URL Hyperlink — Now Works for Both "Symbol" & "NSE Code"
**Before:** If the Google Sheet's identifier column header was `Symbol`, clicking the cell did nothing — the link only worked when the header was `NSE Code`.
**Now:** Whichever column you pick under sidebar → **⚙️ Settings → Symbol Column**, that column always becomes a clickable NSE chart link (`https://charting.nseindia.com/?symbol=...-EQ`), regardless of its header text.
**Bonus cleanup:** Cell text used to read `nse IDEA`, `nse NYKAA`. It now just shows `IDEA`, `NYKAA` — saving column width.

> 💡 Root cause: two separate places in the code checked "is this an NSE column?" — one that built the link's HTML, and a second one in the grid setup that decided whether to actually *render* that HTML as a clickable link or show it as plain text. Both now also check "is this the chosen Symbol column?" in addition to checking the header text.

### 2. National Analytics Portal — 3 New Tabs

| New Tab | URL |
|---|---|
| ✅ Securities Available | nseindia.com/static/market-data/securities-available-for-trading |
| 🏛️ Corporate Filings | nseindia.com/companies-listing/corporate-filings-announcements |
| 📉 52W Low Market | nseindia.com/market-data/52-week-low-equity-market |

### 3. Clear All Filters — Real Fix
**Before:** Pressing it reset sidebar widgets but the **data grid's own column filter icons** stayed stuck — the grid component keeps its own internal state tied to a fixed identifier, separate from the sidebar.
**Now:** Pressing the button forces the grid to fully remount, wiping its internal filter/sort state. It also clears the new matrix search boxes and the Bottom Fishing Scanner's search box.

### 4. Search Symbol Box — Top 250 Stocks Matrix
Sits directly above the main grid, next to "Column Width Adjustment". Type any part of a symbol to instantly filter visible rows — affects the grid, the Rows/Columns counter, and the Excel export together.

### 5. Rules Tab — Global Market News Section
New **📜 Rules** tab (after "DOCUMENTS HUB") shows:
- Core sheet/trading conventions and the "no compromise" philosophy.
- 🟢/🟠 Rule 1 & 2 — what the Green/Orange CMP highlight near 52W High/Low means.
- 52W Low/High Date color meaning table (18 days / 30 days / 1 year ago).
- 🔵 Rule 3 — the full "Diff @ 200 DMA" strategy and mind map (`−40% → −30% → −20% → −10%`).
- Quick links to NSE All Reports, Securities Available, and 52‑Week Low pages.
- 🛑 Risk-management rules (stop-loss %, risk-reward ratio, profit booking, priority order: IPO → F&O → 52W Low).

**To edit these rules:** open `app.py` and find the `TRADING_RULES_LIBRARY` constant near the top of the file (next to `SUGGESTED_AI_PROMPTS` and `PINE_CUSTOM_RULES`). It's plain Markdown text — edit it directly and the Rules tab updates automatically.

### ✅ Quick Test Checklist
- [ ] Set Symbol Column to a header that does **not** contain "nse" (e.g. `Symbol`) → confirm the cell is a clickable link with no `nse ` prefix.
- [ ] Open the 3 new Portal tabs → confirm each iframe loads (or use "Open in Browser" on mobile).
- [ ] Apply a filter using the grid's own column filter icon, then click "Clear All Filters" → confirm it actually clears.
- [ ] Type a symbol into the new "Search symbol" box above the main grid → confirm rows filter live.
- [ ] Open the new **📜 Rules** tab under Global Market News → confirm your rules render correctly.
