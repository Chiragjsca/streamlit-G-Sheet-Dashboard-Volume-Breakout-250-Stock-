import streamlit as st
import pandas as pd
import numpy as np
import gspread
from google.oauth2.service_account import Credentials
from google.auth.transport.requests import AuthorizedSession
import json
import urllib.parse
from datetime import datetime
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode
from st_aggrid.shared import GridUpdateMode
import streamlit.components.v1 as components
import re
import io
import google.generativeai as genai
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title="Top 250 NSE Stock-Volume Breakout Dashboard", layout="wide", page_icon="📊")

# FIXED: Added proper block indentation
if hasattr(st, "fragment"):
    st_fragment = st.fragment
elif hasattr(st, "experimental_fragment"):
    st_fragment = st.experimental_fragment
else:
    def st_fragment(func=None, **kwargs):
        if func is not None:
            return func
        def _wrap(f):
            return f
        return _wrap

# FIXED: Removed the invalid syntax empty comma
st.markdown("", unsafe_allow_html=True)

gemini_enabled = False
groq_enabled   = False

if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    gemini_enabled = True

if "GROQ_API_KEY" in st.secrets:
    try:
        from groq import Groq as GroqClient
        _groq_client = GroqClient(api_key=st.secrets["GROQ_API_KEY"])
        groq_enabled = True
    except ImportError:
        groq_enabled = False

ai_enabled = gemini_enabled or groq_enabled

def call_ai(prompt: str, model_choice: str) -> str:
    if model_choice == "⚡ Groq (Fast)" and groq_enabled:
        resp = _groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2048,
        )
        return resp.choices[0].message.content
    elif gemini_enabled:
        mdl = genai.GenerativeModel("gemini-2.5-flash")
        return mdl.generate_content(prompt).text
    else:
        raise RuntimeError("No AI model is configured. Add GEMINI_API_KEY or GROQ_API_KEY to secrets.")

def ai_model_selector(key_suffix: str = "") -> str:
    options, default = [], 0
    if groq_enabled:   options.append("⚡ Groq (Fast)")
    if gemini_enabled: options.append("🧠 Gemini")
    if not options:    options = ["⚡ Groq (Fast)", "🧠 Gemini"]
    return st.radio("🤖 AI Model:", options, index=0, horizontal=True, key=f"ai_model_sel_{key_suffix}")

SUGGESTED_AI_PROMPTS = [
    "Based on the current data provided, give me a quick summary of the technical performance and trend for {sym}. Also give me all other details and calculate if this company is profitable or not.",
    "Analyze the 52-week high and low data for {sym}. Is the stock closer to its peak or bottom? What does this imply for entry or exit timing? Identify the ideal buy zone.",
    "Examine the 50 DMA, 100 DMA, and 200 DMA data for {sym}. Is the stock in a bullish crossover, bearish zone, or consolidation phase? Explain the trend strength and momentum.",
    "Using the volume data for {sym}, identify if there is unusual volume activity. Does the current volume indicate institutional buying, selling, or accumulation? What does it signal?",
    "Evaluate the full fundamentals of {sym} — EPS, RONW%, D/E ratio, Net Profit (Cr.), Book Value, and Market Cap. Is this company financially healthy and worth long-term investment?",
    "What is the risk profile of {sym} based on its Pledged %, Promoters Holding %, Institutional Holding %, and Debt-to-Equity ratio? Should a retail investor be cautious right now?",
    "Compare {sym}'s current CMP vs its 200 DMA. Is the stock overbought, oversold, or fairly valued based on the Difference from 200 DMA metric? What is the ideal risk-reward entry zone?",
    "Give a complete Buy / Hold / Sell recommendation for {sym} using all available technical and fundamental data. Include specific price targets, support levels, and a stop-loss level.",
    "Based on the CAR Rating and Output signal for {sym}, what is the system suggesting? Does the historical price action and current data support this signal? How reliable is it?",
    "Summarize {sym}'s sector positioning, market cap, enterprise value, book value, and promoter holding. How does this stock compare to typical benchmarks in its sector in the Indian market?",
]

PINE_CUSTOM_RULES = ""
TRADING_RULES_LIBRARY = ""

HIDDEN_COLUMNS_BY_NAME = {
    "Top 250 Stocks": [
        "50 DMA",
        "100 DMA",
        "200 DMA",
        "NSE 1",
        "Trading View 1",
        "History Data 1",
        "Screener 1",
        "Zerodha 1",
        "Chartlink 1",
        "Market smith india 1",
        "Official NSE URL 1",
    ],
    "NSE Fundamentals": [],
    "Final List": [],
    "Final List 2": [],
    "Diff @ 200 DMA": [],
    "+%": [],
    "-%": [],
}

HIDDEN_COLUMNS_BY_LETTER = {
    "Top 250 Stocks": [
        "E", "F", "G",
        "AA", "AB", "AC", "AD", "AE", "AF", "AG", "AH",
    ],
    "NSE Fundamentals": [],
    "Final List": [],
    "Final List 2": [],
    "Diff @ 200 DMA": [],
    "+%": [],
    "-%": [],
}

def _col_letter_to_index(letter: str) -> int:
    letter = str(letter).strip().upper()
    if not letter or not letter.isalpha():
        return -1
    idx = 0
    for ch in letter:
        idx = idx * 26 + (ord(ch) - ord('A') + 1)
    return idx - 1

def get_hidden_columns(sheet_name: str, ordered_columns) -> set:
    ordered_columns = list(ordered_columns)
    hidden = set()
    for col_name in HIDDEN_COLUMNS_BY_NAME.get(sheet_name, []):
        if col_name in ordered_columns:
            hidden.add(col_name)
    for letter in HIDDEN_COLUMNS_BY_LETTER.get(sheet_name, []):
        idx = _col_letter_to_index(letter)
        if 0 <= idx < len(ordered_columns):
            hidden.add(ordered_columns[idx])
    return hidden

LOCKED_SYMBOL_COLUMN = {
    "Top 250 Stocks": None,
    "NSE Fundamentals": None,
    "Final List": None,
    "Final List 2": None,
    "Diff @ 200 DMA": None,
    "+%": None,
    "-%": None,
}

COLUMN_ORDER_BY_NAME = {
    "Top 250 Stocks": [
        "Volume",
        "% Delivery",
        "Close Price",
        "CMP",
        "Price %",
        "52W High",
        "52W Low",
        "Output",
        "Differance from 200 DMA",
        "Cumulative Average Rule (CAR) Rating",
    ],
    "NSE Fundamentals": [],
    "Final List": [],
    "Final List 2": [],
    "Diff @ 200 DMA": [],
    "+%": [],
    "-%": [],
}

COLUMN_ORDER_BY_LETTER = {
    "Top 250 Stocks": ["B", "C", "D", "L"],
    "NSE Fundamentals": [],
    "Final List": [],
    "Final List 2": [],
    "Diff @ 200 DMA": [],
    "+%": [],
    "-%": [],
}

def get_priority_columns(sheet_name: str, ordered_columns) -> list:
    ordered_columns = list(ordered_columns)
    priority = []
    for letter in COLUMN_ORDER_BY_LETTER.get(sheet_name, []):
        idx = _col_letter_to_index(letter)
        if 0 <= idx < len(ordered_columns):
            col = ordered_columns[idx]
            if col not in priority:
                priority.append(col)
    for col_name in COLUMN_ORDER_BY_NAME.get(sheet_name, []):
        if col_name in ordered_columns and col_name not in priority:
            priority.append(col_name)
    return priority

hide_streamlit_ui = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_ui, unsafe_allow_html=True)

hide_github_icon = """
<style>
.viewerBadge_link__1S137 {display: none !important;}
</style>
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)

ADMIN_PASSWORD = "romo"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "watchlist" not in st.session_state:
    st.session_state.watchlist = {}
if "ai_history" not in st.session_state:
    st.session_state.ai_history = []
if "grid_reset_token" not in st.session_state:
    st.session_state.grid_reset_token = 0

if not st.session_state.logged_in:
    st.markdown("<p style='text-align: center; margin-top: 100px; color: Green; font-size: 18px;'>250-V Dashboard</p>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; margin-top: 0px; font-size: 20px;'>🔐 Admin Login</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        with st.form("login_form"):
            pwd = st.text_input("Enter Password", type="password")
            submit = st.form_submit_button("Login", use_container_width=True)
            if submit:
                if pwd == ADMIN_PASSWORD:
                    st.session_state.logged_in = True
                    st.rerun()
                else:
                    import random
                    password_errors = [
                        "Password इल्ले! 😅 इल्ले!, खम्मा घणी भाईसा, सॉरी। तुमसे सब कुछ हो पाएगा! यहां बहुत 🤪 दिमाग मत लगाओ, इस वेबसाइट को नहीं, 😂 इस गलत पासवर्ड को छोड़ दो!",
                        "❌ Password इल्ले भाईसा! 😅 इल्ले! खम्मा घणी, सॉरी। तुम बाहुबली हो, तुमसे सब कुछ हो पाएगा! पर यहाँ फालतू 🤪 दिमाग मत लगाओ। अपनी सुंदर वेबसाइट को नहीं, 😂 इस सड़े हुए गलत पासवर्ड को छोड़ दो!",
                        "❌ खम्मा घणी भाईसा, Password इल्ले! 😅 sorry! तुम तो मंगल ग्रह पर पानी खोज सकते हो, तुमसे सब कुछ हो पाएगा! पर यहाँ ज़्यादा 🤪 दिमाग मत लगाओ। इस सीधे-सादे वेबसाइट को नहीं, 😂 इस जाली पासवर्ड को छोड़ दो!",
                        "❌ Password इल्ले! 😅 इल्ले! खम्मा घणी भाईसा, सॉरी। लोड मत लो, तुमसे सब कुछ हो पाएगा! पर यहाँ फालतू 🤪 दिमाग मत लगाओ। दुनिया छोड़ दो, मोक्ष पकड़ लो, पर पहले 😂 इस गलत पासवर्ड को छोड़ दो!",
                        "❌ अरे भाईसा! Password इल्ले! 😅 खम्मा घणी, sorry। तुम चाहो तो सिस्टम हिला सकते हो, तुमसे सब कुछ हो पाएगा! पर यहाँ ज़्यादा 🤪 दिमाग मत लगाओ। इस निर्दोष वेबसाइट को नहीं, 😂 इस भूतिया गलत पासवर्ड को छोड़ दो!"
                    ]
                    st.error(random.choice(password_errors))
    dynamic_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    st.markdown(f"<p style='text-align: center; color: gray; font-size: 14px; margin-top: 20px;'>Data refreshed: {dynamic_time}</p>", unsafe_allow_html=True)
    st.stop()

import yfinance as yf

st.markdown("<p style='font-size:0.85rem; font-weight:bold; margin:0; padding:0;'>📊 Top 250 NSE Stock-Volume Breakout Dashboard</p>", unsafe_allow_html=True)
st.caption(f"Data refreshed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

@st.cache_data(ttl=60)
def get_live_index_data():
    symbols = {
        "NIFTY 50": "^NSEI",
        "NIFTY NEXT 50": "^NN50",
        "NIFTY MIDCAP 50": "^NSEMDCP50",
        "NIFTY MIDCAP 100": "^CRSLMID",
        "NIFTY 100": "^CNX100",
        "NIFTY 200": "^CNX200",
        "NIFTY 500": "^CRSLDX",
    }
    data_grid = {}
    for name, ticker_code in symbols.items():
        try:
            ticker = yf.Ticker(ticker_code)
            hist = ticker.history(period="5d")
            if not hist.empty and len(hist) >= 2:
                live_price = float(hist['Close'].iloc[-1])
                prev_close = float(hist['Close'].iloc[-2])
                pct_change = ((live_price - prev_close) / prev_close) * 100
                data_grid[name] = {"price": f"{live_price:,.2f}", "change": pct_change}
            else:
                data_grid[name] = {"price": "Loading...", "change": 0.0}
        except Exception:
            data_grid[name] = {"price": "Error", "change": 0.0}
    return data_grid

live_data = get_live_index_data()
cards_html = "<div style='display: flex; flex-wrap: wrap; gap: 10px; margin-top: 10px; font-family: system-ui, -apple-system, sans-serif;'>"
valid_cards_count = 0
for name, info in live_data.items():
    if info["price"] in ["No Data", "Loading...", "Error"]:
        continue
    valid_cards_count += 1
    bg_color = "#1f2937"
    change_sign = "+" if info["change"] >= 0 else ""
    index_nse_url = "https://www.nseindia.com/market-data/live-market-indices"
    cards_html += f"<a href='{index_nse_url}' target='_blank' style='text-decoration:none;'>"
    cards_html += f"<div style='background-color: {bg_color}; color: white; padding: 12px 16px; border-radius: 8px; flex: 1 1 calc(16.66% - 10px); min-width: 140px; box-shadow: 0 2px 5px rgba(0,0,0,0.05);'>"
    cards_html += f"<div style='font-size: 11px; font-weight: 700; letter-spacing: 0.5px; opacity: 0.95; margin-bottom: 6px; text-transform: uppercase;'>{name}</div>"
    cards_html += f"<div style='display: flex; justify-content: space-between; align-items: baseline;'>"
    cards_html += f"<span style='font-size: 15px; font-weight: 700;'>{info['price']}</span>"
    cards_html += f"<span style='font-size: 11px; font-weight: 600; background: rgba(255,255,255,0.2); padding: 1px 6px; border-radius: 4px;'>{change_sign}{info['change']:.2f}%</span>"
    cards_html += f"</div></div></a>"
cards_html += "</div>"

with st.expander("📈 Click to view Live Market Indices", expanded=False):
    if valid_cards_count == 0:
        st.info("Market data is currently unavailable. Please check back later.")
    else:
        st.markdown(cards_html, unsafe_allow_html=True)
st.write("---")

def rgb_to_hex(color_dict):
    if not color_dict: return ""
    r = int(color_dict.get('red', 0) * 255)
    g = int(color_dict.get('green', 0) * 255)
    b = int(color_dict.get('blue', 0) * 255)
    return f"#{r:02x}{g:02x}{b:02x}"

@st.cache_data(ttl=300, show_spinner=False)
def fetch_stock_ohlc_history(nse_symbol, period="1y"):
    try:
        raw_sym = str(nse_symbol).strip().upper()
        if not raw_sym:
            return pd.DataFrame()
        ticker_code = raw_sym if raw_sym.endswith(".NS") else f"{raw_sym}.NS"
        hist = yf.download(ticker_code, period=period, interval="1d", progress=False, auto_adjust=True)
        if hist is None or hist.empty:
            return pd.DataFrame()
        if isinstance(hist.columns, pd.MultiIndex):
            hist.columns = hist.columns.get_level_values(0)
        hist.index = pd.to_datetime(hist.index)
        return hist
    except Exception:
        return pd.DataFrame()

@st.cache_data(ttl=300)
def load_sheet_data_with_colors(sheet_name):
    try:
        if "gcp_service_account" not in st.secrets:
            st.error("Missing 'gcp_service_account' in secrets.")
            return pd.DataFrame()
        service_account_info = st.secrets["gcp_service_account"]
        if isinstance(service_account_info, str):
            service_account_info = json.loads(service_account_info)
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_info(service_account_info, scopes=scope)
        client = gspread.authorize(creds)
        spreadsheet_id = "1SFhuZbLLlwwFsNo1k2RRx_Zp6bAkRR20W0F_zTwgdwU"
        
        encoded_sheet = urllib.parse.quote(sheet_name)
        authed_session = AuthorizedSession(creds)
        url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}?includeGridData=true&ranges={encoded_sheet}"
        response = authed_session.get(url)
        data = response.json()
        
        if 'error' in data or 'sheets' not in data or not data['sheets']: 
            return pd.DataFrame()
        
        sheet_data = data['sheets'][0]['data'][0]
        row_data = sheet_data.get('rowData', [])
        if not row_data: return pd.DataFrame()
        
        values_list, bg_colors_list, txt_colors_list = [], [], []
        for row in row_data:
            cells = row.get('values', [])
            row_vals, row_bgs, row_txts = [], [], []
            for cell in cells:
                row_vals.append(cell.get('formattedValue', ''))
                fmt = cell.get('effectiveFormat', {})
                row_bgs.append(rgb_to_hex(fmt.get('backgroundColor', {})))
                row_txts.append(rgb_to_hex(fmt.get('textFormat', {}).get('foregroundColor', {})))
            values_list.append(row_vals)
            bg_colors_list.append(row_bgs)
            txt_colors_list.append(row_txts)
            
        raw_headers = values_list[0]
        clean_headers = []
        seen = {}
        for h in raw_headers:
            h = str(h).strip()
            if h == "": h = "empty_column"
            if h in seen:
                seen[h] += 1
                h = f"{h}_{seen[h]}"
            else: 
                seen[h] = 0
            clean_headers.append(h)
            
        df = pd.DataFrame(values_list[1:], columns=clean_headers)
        for i, col in enumerate(clean_headers):
            df[f"_bg_{col}"] = [row[i] if i < len(row) else "#ffffff" for row in bg_colors_list[1:]]
            df[f"_txt_{col}"] = [row[i] if i < len(row) else "#000000" for row in txt_colors_list[1:]]
        return df
    except Exception as e:
        return pd.DataFrame()

def process_hyperlinks(df, symbol_col):
    df_proc = df.copy()
    df_proc['_raw_symbol_'] = df_proc[symbol_col]
    for idx, row in df_proc.iterrows():
        sym = str(row['_raw_symbol_']).strip()
        if not sym or sym == "nan": continue
        for col in df_proc.columns:
            if col.startswith("_bg_") or col.startswith("_txt_") or col == "_raw_symbol_": continue
            c_lower = col.lower()
            url, label = None, "🔗 Link"
            if "trading view" in c_lower: url, label = f"https://www.tradingview.com/symbols/{sym}/", f"Tre {sym}" if not c_lower.endswith("1") else "🔗 Link"
            elif "history data" in c_lower: url, label = f"https://www.equitypandit.com/historical-data/{sym}", f"History {sym}" if not c_lower.endswith("1") else "🔗 Link"
            elif "screener" in c_lower: url, label = f"https://www.screener.in/company/{sym}", f"Scr {sym}" if not c_lower.endswith("1") else "🔗 Link"
            elif "zerodha" in c_lower: url, label = f"https://zerodha.com/markets/stocks/NSE/{sym}", f"🪁 {sym}" if not c_lower.endswith("1") else "🔗 Link"
            elif "chartlink" in c_lower: url, label = f"https://chartink.com/stocks-new?load-snapshot=exponential-moving-average-simple-moving-average-simple-moving-average-moving-average-convergence-divergence-chart-snapshot-175&symbol={sym}", f"CL {sym}" if not c_lower.endswith("1") else "🔗 Link"
            elif "market smith" in c_lower: url, label = f"https://marketsmithindia.com/mstool/eval/{sym}/evaluation.jsp", f"ms {sym}" if not c_lower.endswith("1") else "🔗 Link"
            elif "official nse" in c_lower: url, label = f"https://www.nseindia.com/get-quotes/equity?symbol={sym}", f"nse📰 {sym}" if not c_lower.endswith("1") else "🔗 Link"
            elif "nse" in c_lower or col == symbol_col:
                url, label = f"https://charting.nseindia.com/?symbol={sym}-EQ", (sym if not c_lower.endswith("1") else "🔗 Link")
            if url: 
                df_proc.at[idx, col] = f'<a href="{url}" target="_blank" style="text-decoration:none;">{label}</a>'
    return df_proc

def apply_numeric_slider(df, col_name, st_container, display_label=None):
    if col_name in df.columns:
        num_series = df[col_name].astype(str).str.replace(r'[%,]', '', regex=True)
        num_series = pd.to_numeric(num_series, errors='coerce').replace([np.inf, -np.inf], np.nan)
        valid_nums = num_series.dropna()
        if not valid_nums.empty:
            min_val, max_val = round(float(valid_nums.min()), 2), round(float(valid_nums.max()), 2)
            if min_val < max_val:
                label = display_label if display_label else f"{col_name} Range:"
                selected_range = st_container.slider(label, min_value=min_val, max_value=max_val, value=(min_val, max_val), key=f"filter_num_{col_name}")
                return df[(num_series >= selected_range[0]) & (num_series <= selected_range[1])]
    return df

def apply_date_filter(df, col_name, st_container):
    if col_name in df.columns:
        options = ["All Time", "Past 5 Days", "Past 10 Days", "Past 15 Days", "Past 20 Days",
                   "Past 25 Days", "Past 30 Days", "Past 1 Month", "Past 2 Months", "Past 6 Months", "Past 1 Year"]
        selection = st_container.selectbox(f"{col_name}:", options, key=f"filter_date_{col_name}")
        if selection != "All Time":
            date_series = pd.to_datetime(df[col_name], errors='coerce', dayfirst=True)
            today = pd.Timestamp.now()
            if selection == "Past 5 Days": threshold = today - pd.Timedelta(days=5)
            elif selection == "Past 10 Days": threshold = today - pd.Timedelta(days=10)
            elif selection == "Past 15 Days": threshold = today - pd.Timedelta(days=15)
            elif selection == "Past 20 Days": threshold = today - pd.Timedelta(days=20)
            elif selection == "Past 25 Days": threshold = today - pd.Timedelta(days=25)
            elif selection == "Past 30 Days": threshold = today - pd.Timedelta(days=30)
            elif selection == "Past 1 Month": threshold = today - pd.DateOffset(months=1)
            elif selection == "Past 2 Months": threshold = today - pd.DateOffset(months=2)
            elif selection == "Past 6 Months": threshold = today - pd.DateOffset(months=6)
            elif selection == "Past 1 Year": threshold = today - pd.DateOffset(years=1)
            return df[date_series >= threshold]
    return df

def get_clean_text_length(val):
    if pd.isna(val): return 0
    clean_text = re.sub(r'<[^>]*>', '', str(val))
    return len(clean_text)

def clean_for_export(df):
    export_df = df.copy()
    cols_to_drop = [c for c in export_df.columns if c.startswith("_bg_") or c.startswith("_txt_") or c == "_raw_symbol_"]
    export_df = export_df.drop(columns=cols_to_drop, errors='ignore')
    for col in export_df.select_dtypes(include=['object']).columns:
        export_df[col] = export_df[col].apply(lambda x: re.sub(r'<[^>]*>', '', str(x)) if pd.notnull(x) else x)
    return export_df

st.markdown("<p style='font-size:0.85rem; font-weight:bold; margin:0; padding:0;'>🌍 National Exchange Scanner (All NSE/BSE Stocks)</p>", unsafe_allow_html=True)
st.caption("Live market data covering 2,000+ equities. Powered by TradingView.")

with st.expander("🏆 Click to view Full-Market India Rankings", expanded=False):
    nse_tab1, nse_tab2, nse_tab3, nse_tab4, nse_tab5 = st.tabs([
        "🚀 Gainers & Losers",
        "📦 Volume & Active",
        "⭐ 52W High / Low",
        "🔄 52W Reversals",
        "📊 Top 100 Traded"
    ])
    
    def render_tv_widget(screen_type):
        return f"""
        <div class="tradingview-widget-container">
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-screener.js" async>
          {{
          "width": "100%",
          "height": 490,
          "defaultColumn": "overview",
          "defaultScreen": "{screen_type}",
          "market": "india",
          "showToolbar": true,
          "colorTheme": "light",
          "locale": "en"
        }}
          </script>
        </div>
        """
        
    with nse_tab1:
        colA, colB = st.columns(2)
        with colA:
            st.markdown("<p style='font-size:14px; font-weight:bold;'>🚀 Top Gainers</p>", unsafe_allow_html=True)
            components.html(render_tv_widget("top_gainers"), height=520)
        with colB:
            st.markdown("<p style='font-size:14px; font-weight:bold;'>🔻 Top Losers</p>", unsafe_allow_html=True)
            components.html(render_tv_widget("top_losers"), height=520)
    with nse_tab2:
        colA, colB = st.columns(2)
        with colA:
            st.markdown("<p style='font-size:14px; font-weight:bold;'>📦 Volume Leaders</p>", unsafe_allow_html=True)
            components.html(render_tv_widget("volume_leaders"), height=520)
        with colB:
            st.markdown("<p style='font-size:14px; font-weight:bold;'>🔥 Most Active (Volume & Value)</p>", unsafe_allow_html=True)
            components.html(render_tv_widget("most_active"), height=520)
    with nse_tab3:
        colA, colB = st.columns(2)
        with colA:
            st.markdown("<p style='font-size:14px; font-weight:bold;'>⭐ New 52-Week Highs</p>", unsafe_allow_html=True)
            components.html(render_tv_widget("new_52wk_high"), height=520)
        with colB:
            st.markdown("<p style='font-size:14px; font-weight:bold;'>⭐ New 52-Week Lows</p>", unsafe_allow_html=True)
            components.html(render_tv_widget("new_52wk_low"), height=520)
    with nse_tab4:
        colA, colB = st.columns(2)
        with colA:
            st.markdown("<p style='font-size:14px; font-weight:bold;'>📈 Outperforming 52W High (Reversal Up)</p>", unsafe_allow_html=True)
            components.html(render_tv_widget("outperforming_52wk_high"), height=520)
        with colB:
            st.markdown("<p style='font-size:14px; font-weight:bold;'>📉 Underperforming 52W Low (Reversal Down)</p>", unsafe_allow_html=True)
            components.html(render_tv_widget("underperforming_52wk_low"), height=520)
    with nse_tab5:
        st.markdown("<p style='font-size:14px; font-weight:bold;'>📊 Top 100+ Stocks Traded (Full India Screener)</p>", unsafe_allow_html=True)
        components.html(render_tv_widget("general"), height=520)

st.write("---")