# 📊 Top 250 NSE Stock-Volume Breakout Dashboard

A professional, all‑in‑one dashboard for Indian stock market analysis.  
It combines live data from Google Sheets, AI (Gemini/Groq), advanced filtering, watchlists, a **bottom‑fishing** score, a GTT order calculator, dozens of embedded market portals, and much more.

---

## ✨ Key Features

- **📈 Live Market Indices** – NIFTY 50, NIFTY Next 50, NIFTY Midcap 50, etc. (Yahoo Finance, refreshes every 60s).
- **🏢 Top 250 Stocks Matrix** – CMP & daily % change cards, fully linked to NSE.
- **🏆 Advanced Ranking Dashboards** – Gainers/Losers, Volume Leaders, Most Active (Volume & Value), Top by Turnover.
- **🌍 National Exchange Scanner** – Embedded TradingView screeners for **all NSE/BSE** stocks (Gainers, Losers, 52W High/Low, Reversals, Top 100 Traded).
- **📄 Google Sheets Integration** – 6 different sheets (`Top 250 Stocks`, `Final List`, `Diff @ 200 DMA`, etc.) with full colour preservation.
- **🎨 Powerful Filtering** – Global search, colour filters, numeric sliders, DMA trend filters (e.g. 50 DMA > 200 DMA), date filters.
- **🤖 AI Analysis** – Gemini or Groq (Llama 3.3) analyses any selected stock using live sheet data. Pre‑defined prompts, exportable history.
- **💻 Pine Script Generator** – AI writes TradingView Pine Script v5 strategies (Volume Breakout, Moving Average Crossover, Trend Following, Mean Reversion).
- **🔬 Bottom Fishing Score** – 0–100 score based on 8 criteria (proximity to 52W low, uptrend, volume, debt, profit, RONW, promoter holding, pledge). Grades: Strong Buy / Watchlist / Caution / [...]
- **🎯 GTT Order Calculator** – Auto‑suggest Stop‑Loss (1×, 1.5×, 2× ATR), multiple targets (1R, 2R, 3R), position sizing, copy‑ready order summary.
- **📝 Watchlist Manager** – Persistent watchlist stored in a Google Sheet. Add notes, download Excel, share via WhatsApp/Telegram.
- **📅 Multi‑Horizon Performance Matrix** – Returns for 24 time horizons (1 day … 3 years) plus volume, coloured by performance.
- **🧭 National Analytics Portal** – 27 embedded iframes (NSE official pages, Moneycontrol, Chartink, Screener, ScanX, IPO Watch, etc.) with "Open in Browser" fallback.
- **📥 Full Excel Export** – Export filtered grids, watchlist, AI history, bottom‑fishing results.
- **🖼️ Responsive Design** – Works on desktop and mobile (with external links for embedded iframes).

--------------------------------------------------------------------------------------------------

📊 Top 250 NSE Stock-Volume Breakout Dashboard – User Guide
This dashboard is a complete technical & fundamental analysis platform for the top 250 NSE stocks, plus a full-market scanner for all NSE/BSE equities. It combines live data from Google Sheets, AI ana[...]

📈 2. Live Market Indices (Top Section)
Displays NIFTY 50, NIFTY NEXT 50, NIFTY MIDCAP 50 and other key indices.

Data is fetched from Yahoo Finance (refreshed every 60 seconds).

Each card shows: index name, current price, daily % change (green/red).

Click on any card → opens the official NSE live‑indices page.

💡 If no cards appear, Yahoo Finance data may be temporarily unavailable.

📊 3. Top 250 Stocks Matrix & Ranking Dashboards
3.1 Stock Ticker Cards
Shows CMP and daily % change for each stock in the "Top 250 Stocks" sheet.

Click a card → opens NSE quote page.

3.2 Advanced Ranking Dashboards (6 tabs)
Tab	What it shows
Gainers/Losers	Top 20 gainers & top 20 losers by % change
Volume Leaders	Highest & lowest 20 by volume
Active (Vol & Val)	Top 20 by volume, displaying both volume & traded value
Top by Value	Top 20 by traded value (₹)
Top by Turnover	Top 20 by turnover (₹)
Most Active	Top 20 by traded value (repeated, for convenience)
Each card includes: symbol, price, and a metric pill (e.g. +2.5% or Vol: 1.2M).

🌍 4. National Exchange Scanner (All NSE/BSE Stocks)
Embedded TradingView screeners inside 5 tabs:

Tab	Content
Gainers & Losers	Top gainers / top losers
Volume & Active	Volume leaders & most active (turnover)
52W High / Low	New 52‑week highs / lows
52W Reversals	Outperforming 52W high / underperforming 52W low
Top 100 Traded	General screener – sort by any metric
📱 If an iframe is blank on mobile, use the "Open in Browser" button above it.

🧩 5. Main Data Grid (Google Sheets)
5.1 Sheet selection (sidebar)
Choose from:
Top 250 Stocks | Final List | Final List 2 | Diff @ 200 DMA | +% | -%

5.2 Powerful filtering (sidebar)
Global search – any column.

Color filters – filter cells by background colour (e.g. all green cells in a column).

Categorical filters – Industry, Sector, Output, Start GTT Order, etc.

DMA trend filter – e.g. 50 DMA > 200 DMA.

Numeric range sliders – Volume, CMP, Promoters %, Net Profit, EPS, RONW %, Market Cap, and also Diff from 200 DMA, From 52W Low %, From 52W High %.

Date filters – 52W high / low dates (Past 5 days … Past 1 year).

5.3 Interactive table (AgGrid)
Click on any row → opens the Workspace Panel (see section 6).

Columns are dynamically coloured to match Google Sheets' background/text colours.

Links (TradingView, Screener, Zerodha, etc.) are clickable directly in the grid.

Column width can be set to auto-fit row 1 or row 2.

5.4 Export
Download the currently filtered table as Excel (all colours removed).

🛠️ 6. Workspace Panel (after selecting a stock)
When you click a row in the main grid, a detailed panel appears with 11 tabs:

Tab	Description
Chart & Trade Info	NSE interactive chart (if the iframe is blocked, tap the "Open in Browser" link)
History Data	EquityPandit historical data iframe
Bullish/Bearish Zone	EquityPandit zone indicator
Screener Documents	Screener.in consolidated financials
Zerodha Portal	Zerodha markets page
MarketSmith India	Institutional evaluation
TradingView Profile	Asset profile from TradingView
🤖 AI Stock Analysis	Ask AI (Gemini or Groq) about the stock using live sheet data. Also includes suggested prompts, WhatsApp/Telegram share, and Excel export of AI history.
💻 AI Pine Script Builder	Generate a complete TradingView Pine Script v5 strategy based on the stock's data. Choose from 4 strategy templates + add custom rules.
🔬 Bottom Fishing Score	Scores the stock (0–100) for buying near the 52W low. Shows grade (Strong Buy / Watchlist / Caution / Avoid) and detailed reasoning (proximity to low, uptrend, volume, debt[...]
🎯 GTT Order Calculator	Automatically suggests stop‑loss (tight/standard/wide), targets (1R, 2R, 3R), ATR, position sizing, and a copy‑ready GTT summary. Share via WhatsApp/Telegram.
📊 Watchlist Manager	Add/remove the current stock to your personal watchlist (stored in a Google Sheet called Watchlist). Add a note, then view/manage the full watchlist, download as Excel, or [...]
🤖 7. AI Features (Gemini & Groq)
Requirements
Add GEMINI_API_KEY and/or GROQ_API_KEY to Streamlit secrets.

If both are present, you can choose between ⚡ Groq (llama 3.3 70B) and 🧠 Gemini 2.5 Flash.

AI Stock Analysis
Select a stock from the grid, go to the AI tab.

Type your own question or pick from 10 suggested prompts (technical summary, entry zone, volume analysis, fundamentals, risk profile, buy/hold/sell recommendation, etc.).

The AI receives the full live row data (CMP, volumes, DMAs, fundamentals, etc.) and answers contextually.

Results are saved in st.session_state.ai_history and can be exported as a combined Excel file.

AI Pine Script Builder
Choose a strategy focus (volume breakout, moving average crossover, trend following, mean reversion).

Add custom rules (e.g., "use ATR trailing stop").

AI generates ready‑to‑paste Pine Script v5 code.

Code can be saved as Excel.

Bottom Fishing AI Deep Analysis
Inside the Bottom Fishing Score tab, click "Get AI Deep Analysis".

AI analyses the BF score, scoring breakdown, and gives specific entry/exit advice.

📝 8. Watchlist Manager
Stored in Google Sheet (tab name Watchlist) – persistent across sessions.

Columns: Symbol, CMP, Note, BF Score, BF Grade, Added On.

Add stocks from the Watchlist Manager tab of the workspace panel.

View, download, or share your watchlist directly from the sidebar or the workspace tab.

⚠️ If sheet write fails, check your gcp_service_account secrets.

🔬 9. Bottom Fishing Scanner (Standalone)
Located after the main grid.

Scores every stock from 0–100 based on 8 criteria (see table below).

Slider to set minimum BF score (default 55 = Watchlist grade).

Sort by score high→low or low→high.

Search a specific symbol.

Results show Symbol, Score, Grade, CMP, Sector, and the top 3 reasons.

Export results as Excel.

Criteria	Max Points
CMP within 8–15% of 52W low	30
CMP > 200 DMA (uptrend)	15
High volume (≥ 10M)	10
Low / zero debt (D/E ≤ 0.1)	10
Positive net profit	10
RONW ≥ 15%	10
Promoter holding ≥ 50%	8
Zero pledged shares	7
Grades:
🟢 STRONG BUY (≥75) | 🟡 WATCHLIST (55–74) | 🟠 CAUTION (35–54) | 🔴 AVOID (<35)

📅 10. Multi‑Horizon Performance Summary Matrix
Displays percentage returns over 24 time horizons (1 day, 2 days, … 3 years) plus Volume.

Ranks stocks based on any chosen horizon.

Includes BF Score & Grade columns.

Colours: green background for positive returns, red for negative.

Click the STOCK NAME cell → opens NSE chart.

Filter by symbol, adjust column widths, and export is available via the main Excel download.

🏆 11. Daily Top / Bottom Performers
Shows 10 best and 10 worst daily performers (based on the Price % column).

Each badge is a clickable link to the NSE chart.

🧭 12. National Analytics Portal (27 additional tabs)
A huge collection of embedded financial portals:

NSE official:

Most Active, Volume Gainers, Top Gainers/Losers, 52‑Week High/Low, Stocks Traded, Advances/Declines, Pre‑Open Market, Price Band Hitters, Index Heatmap, IPO Tracker, Document Reports

Third‑party:

Volume Shockers (Moneycontrol), TradingView Scripts, MunafaSutra, Dhan stock lists, ScanX (custom & live screener), Screener.in explore, Chittorgarh IPO, IPO Watch, NSE Pulse, Chartink (screeners, das[...]

Each tab has an "Open in Browser" button – use it if the iframe does not load on mobile.

⚙️ 13. Sidebar Controls – Summary
Clear All Filters – reset every filter and search.

Global Search – case‑insensitive search across all visible columns.

Sheet selector – change the active Google Sheet.

Symbol Column – choose which column contains the stock symbol.

Color Filters – pick a column and select background colours to show.

Categorical Filters – Industry, Sector, Output, etc.

DMA Trend Filter – e.g. 50 DMA < 100 DMA < 200 DMA.

Numeric sliders – Volume, CMP, Promoters %, Net Profit, EPS, RONW, etc.

Date filters – 52W high / low date.

Watchlist manager – view / remove stocks, download watchlist Excel.

AI History Export – download all AI queries and answers.

📥 14. Data Freshness & Caching
Google Sheets data: cached for 300 seconds (5 minutes).

Live indices (Yahoo Finance): cached for 60 seconds.

Use the browser refresh or the "Clear All Filters" button to force a reload.

---

## 📊 Comprehensive Details: Top 250 NSE Stock-Volume Breakout Dashboard

This is a **professional-grade Streamlit dashboard** for Indian stock market analysis.

---

### **🎯 Core Purpose**
A comprehensive technical & fundamental analysis platform for the top 250 NSE (National Stock Exchange) stocks, combined with a full-market scanner for all NSE/BSE equities. It integrates real-time data, AI analysis, and advanced trading tools.

---

### **📈 Major Features Explained**

#### **1. Live Market Indices (Real-time Updates)**
- Displays **NIFTY 50, NIFTY Next 50, NIFTY Midcap 50**, and other indices
- **Data Source:** Yahoo Finance (refreshes every 60 seconds)
- **Display:** Index name, current price, daily % change (color-coded green/red)
- **Interaction:** Clicking a card opens the NSE live indices page

#### **2. Top 250 Stocks Matrix**
- Shows **Current Market Price (CMP)** and **daily % change** for each stock
- All cards are **linked to NSE quote pages**
- Advanced ranking tabs:
  - **Gainers/Losers:** Top 20 gainers & losers by % change
  - **Volume Leaders:** Highest & lowest 20 by volume
  - **Active (Vol & Val):** Top 20 by volume with traded value
  - **Top by Value:** Top 20 by traded value (₹)
  - **Top by Turnover:** Top 20 by turnover (₹)
  - **Most Active:** Top 20 by traded value (convenience tab)

#### **3. National Exchange Scanner (All NSE/BSE Stocks)**
- **5 TradingView screener tabs:**
  - Gainers & Losers
  - Volume & Active traders
  - 52-Week High/Low
  - 52-Week Reversals (outperforming/underperforming)
  - Top 100 Traded stocks
- Mobile-friendly with "Open in Browser" fallback for blocked iframes

#### **4. Google Sheets Integration**
- **6 different sheets available:**
  - Top 250 Stocks
  - Final List
  - Final List 2
  - Diff @ 200 DMA
  - +% (positive % performers)
  - -% (negative % performers)
- **Full color preservation** from Google Sheets

#### **5. Powerful Filtering System (Sidebar)**
- **Global search** – case-insensitive across all columns
- **Color filters** – filter by background color (e.g., all green cells)
- **Categorical filters** – Industry, Sector, Output, Start GTT Order, etc.
- **DMA trend filters** – Example: 50 DMA > 200 DMA (uptrend detection)
- **Numeric sliders** for:
  - Volume
  - Current Market Price (CMP)
  - Promoters %
  - Net Profit
  - EPS
  - RONW %
  - Market Cap
  - Diff from 200 DMA
  - From 52W Low %
  - From 52W High %
- **Date filters** – 52W high/low dates (Past 5 days to Past 1 year)

#### **6. Interactive Data Grid (AgGrid)**
- **Dynamic color coding** – matches Google Sheets' background/text colors
- **Clickable links** – TradingView, Screener, Zerodha, and other portals
- **Row selection** – opens the **Workspace Panel** (see below)
- **Export** – download filtered data as Excel (colors removed)

---

### **🛠️ Workspace Panel (11 Detailed Tabs)**
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

---

### **🤖 AI Features (Gemini & Groq)**

**Requirements:**
- Add `GEMINI_API_KEY` and/or `GROQ_API_KEY` to Streamlit secrets
- Choose between **Groq (Llama 3.3 70B)** or **Gemini 2.5 Flash**

**AI Stock Analysis:**
- 10 suggested prompts:
  - Technical summary
  - Entry zone analysis
  - Volume analysis
  - Fundamental review
  - Risk profile
  - Buy/Hold/Sell recommendation
  - Etc.
- AI receives **full live row data** (CMP, volumes, DMAs, fundamentals)
- Results stored in session state and **exportable as Excel**

**AI Pine Script Builder:**
- Choose strategy focus: Volume Breakout, Moving Average Crossover, Trend Following, Mean Reversion
- Add custom rules (e.g., "use ATR trailing stop")
- Generates **ready-to-paste Pine Script v5 code**
- Can be saved as Excel

---

### **🔬 Bottom Fishing Score (Value Investing Tool)**

**What it does:** Identifies stocks trading near 52-week lows with upside potential.

**Scoring Criteria (0–100 points):**
| Criteria | Max Points |
|----------|-----------|
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
- Slider to set minimum BF score (default 55)
- Sort by score (high→low or low→high)
- Symbol search
- Results show Score, Grade, CMP, Sector, and top 3 reasons
- Export results as Excel
- AI Deep Analysis available inside the tab

---

### **🎯 GTT Order Calculator**

**Auto-suggests:**
- **Stop-Loss Options:**
  - Tight (1× ATR)
  - Standard (1.5× ATR)
  - Wide (2× ATR)
- **Multiple Targets:** 1R, 2R, 3R (risk-reward ratios)
- **Position Sizing** – calculates based on your account size
- **Copy-ready GTT Summary** – shareable via WhatsApp/Telegram

---

### **📝 Watchlist Manager**

**Storage:** Persistent Google Sheet named "Watchlist"

**Columns:**
- Symbol
- CMP
- Note
- BF Score
- BF Grade
- Added On

**Features:**
- Add/remove stocks from any workspace panel
- View, download, share via WhatsApp/Telegram
- Accessible from sidebar or workspace tab

---

### **📅 Multi-Horizon Performance Matrix**

- **24 time horizons:** 1 day, 2 days, 3 days... 3 years
- **Color coding:** Green = positive returns, Red = negative
- **Includes:** BF Score & Grade columns
- **Sortable** by any horizon
- **Clickable stock names** → opens NSE chart

---

### **🧭 National Analytics Portal (27+ Tabs)**

**NSE Official Pages:**
- Most Active
- Volume Gainers
- Top Gainers/Losers
- 52-Week High/Low
- Stocks Traded
- Advances/Declines
- Pre-Open Market
- Price Band Hitters
- Index Heatmap
- IPO Tracker
- Document Reports

**Third-Party Portals:**
- Volume Shockers (Moneycontrol)
- TradingView Scripts
- MunafaSutra
- Dhan stock lists
- ScanX (custom & live screener)
- Screener.in explore
- Chittorgarh IPO
- IPO Watch
- NSE Pulse
- Chartink (screeners, dashboard)
- And more...

---

### **📥 Data Freshness & Caching**

| Data Source | Cache Duration |
|------------|----------------|
| Google Sheets | 300 seconds (5 minutes) |
| Live indices (Yahoo Finance) | 60 seconds |

**Force Refresh:** Use browser refresh or "Clear All Filters" button

---

### **🏆 Key Advantages**

✅ **All-in-one solution** – No need to jump between multiple platforms  
✅ **AI-powered insights** – Contextual analysis with Gemini or Groq  
✅ **Value investing focus** – Bottom fishing score identifies bargains  
✅ **Trading-ready tools** – GTT calculator, Pine Script generator  
✅ **Comprehensive data** – 250 stocks + full NSE/BSE scanner  
✅ **Responsive design** – Works on desktop and mobile  
✅ **Persistent storage** – Watchlists and AI history saved  
✅ **Export capabilities** – Download all data as Excel
