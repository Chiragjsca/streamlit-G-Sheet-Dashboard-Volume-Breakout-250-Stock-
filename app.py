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
st.markdown(, unsafe_allow_html=True)
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
return st.radio("🤖 AI Model:", options, index=0,
horizontal=True, key=f"ai_model_sel_{key_suffix}")
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
PINE_CUSTOM_RULES =
TRADING_RULES_LIBRARY =
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
import streamlit as st
hide_streamlit_ui =
st.markdown(hide_streamlit_ui, unsafe_allow_html=True)
import streamlit as st
hide_github_icon =
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
"❌ अरे भाईसा! Password इल्ले! 😅 खम्मा घणी, सॉरी। तुम चाहो तो सिस्टम हिला सकते हो, तुमसे सब कुछ हो पाएगा! पर यहाँ ज़्यादा 🤪 दिमाग मत लगाओ। इस निर्दोष वेबसाइट को नहीं, 😂 इस भूतिया गलत पासवर्ड को छोड़ दो!"
]
st.error(random.choice(password_errors))
dynamic_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
st.markdown(f"<p style='text-align: center; color: gray; font-size: 14px; margin-top: 20px;'>Data refreshed: {dynamic_time}</p>", unsafe_allow_html=True)
st.stop()
st.markdown(, unsafe_allow_html=True)
import yfinance as yf
import streamlit as st
from datetime import datetime
st.markdown("<p style='font-size:0.85rem; font-weight:bold; margin:0; padding:0;'>📊 Top 250 NSE Stock-Volume Breakout Dashboard</p>", unsafe_allow_html=True)
st.caption(f"Data refreshed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
@st.cache_data(ttl=60)
def get_live_index_data():
symbols = {
"NIFTY 50": "^NSEI",
"NIFTY NEXT 50": "^NN50",
"NIFTY MIDCAP 50": "^NSEMDCP50",
"NIFTY MIDCAP 100": "^CRSLMID",
"NIFTY MIDCAP 150": "UNSUPPORTED",
"NIFTY SMLCAP 50": "UNSUPPORTED",
"NIFTY SMLCAP 100": "UNSUPPORTED",
"NIFTY SMLCAP 250": "UNSUPPORTED",
"NIFTY MIDSML 400": "UNSUPPORTED",
"NIFTY 100": "^CNX100",
"NIFTY 200": "^CNX200",
"NIFTY500 MULTI...": "UNSUPPORTED",
"NIFTY LARGEMID...": "UNSUPPORTED",
"NIFTY MID SELE...": "UNSUPPORTED",
"NIFTY TOTAL MK...": "UNSUPPORTED",
"NIFTY MICROCAP...": "UNSUPPORTED",
"NIFTY 500": "^CRSLDX",
"NIFTY FPI 150": "UNSUPPORTED",
"NIFTY500 LMS E...": "UNSUPPORTED",
"NIFTY MIDSMALL...": "UNSUPPORTED",
"NIFTY SMALLCAP...": "UNSUPPORTED"
}
data_grid = {}
for name, ticker_code in symbols.items():
if ticker_code == "UNSUPPORTED":
data_grid[name] = {"price": "No Data", "change": 0.0}
continue
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
bg_color = ""
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
if not color_dict: return "
r, g, b = int(color_dict.get('red', 0) * 255), int(color_dict.get('green', 0) * 255), int(color_dict.get('blue', 0) * 255)
return f"
@st.cache_data(ttl=300, show_spinner=False)
def fetch_stock_ohlc_history(nse_symbol, period="1y"):
try:
raw_sym = str(nse_symbol).strip().upper()
if not raw_sym:
return pd.DataFrame()
ticker_code = raw_sym if raw_sym.endswith(".NS") else f"{raw_sym}.NS"
hist = yf.download(ticker_code, period=period, interval="1d",
progress=False, auto_adjust=True)
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
if 'error' in data: return pd.DataFrame()
if 'sheets' not in data or not data['sheets']: return pd.DataFrame()
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
else: seen[h] = 0
clean_headers.append(h)
df = pd.DataFrame(values_list[1:], columns=clean_headers)
for i, col in enumerate(clean_headers):
df[f"_bg_{col}"] = [row[i] if i < len(row) else "
df[f"_txt_{col}"] = [row[i] if i < len(row) else "
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
if url: df_proc.at[idx, col] = f'<a href="{url}" target="_blank" style="text-decoration:none; color:
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
import streamlit.components.v1 as components
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
return f
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
@st.cache_data(ttl=300)
def get_sheet_stocks_data():
df = load_sheet_data_with_colors("Top 250 Stocks")
data_grid = {}
if df.empty:
return data_grid
actual_cols = [c for c in df.columns if not c.startswith("_bg_") and not c.startswith("_txt_")]
sym_col = next((c for c in actual_cols if c.lower() in ["nse code", "symbol", "ticker", "stock symbol", "id", "stock"]), None)
cmp_col = next((c for c in actual_cols if "cmp" in c.lower()), None)
pct_col = next((c for c in actual_cols if "price %" in c.lower() or "change" in c.lower()), None)
if not sym_col or not cmp_col:
return data_grid
for _, row in df.iterrows():
sym = str(row.get(sym_col, "")).strip()
if not sym or sym == "nan":
continue
raw_cmp = str(row.get(cmp_col, "")).replace(",", "").strip()
raw_pct = str(row.get(pct_col, "0")).replace("%", "").replace(",", "").strip() if pct_col else "0"
try:
price_val = float(raw_cmp)
price_str = f"{price_val:,.2f}"
except ValueError:
price_str = "No Data"
try:
pct_val = float(raw_pct)
except ValueError:
pct_val = 0.0
data_grid[sym] = {"price": price_str, "change": pct_val}
return data_grid
sheet_live_data = get_sheet_stocks_data()
sheet_cards_html = "<div style='display: flex; flex-wrap: wrap; gap: 10px; margin-top: 10px; font-family: system-ui, -apple-system, sans-serif;'>"
sheet_valid_cards_count = 0
for name, info in sheet_live_data.items():
if info["price"] in ["No Data", "Loading...", "Error"]:
continue
sheet_valid_cards_count += 1
bg_color = "
change_sign = "+" if info["change"] >= 0 else ""
nse_url = f"https://www.nseindia.com/get-quotes/equity?symbol={name}"
sheet_cards_html += f"<a href='{nse_url}' target='_blank' style='text-decoration:none;'>"
sheet_cards_html += f"<div style='background-color: {bg_color}; color: white; padding: 12px 16px; border-radius: 8px; flex: 1 1 calc(16.66% - 10px); min-width: 140px; box-shadow: 0 2px 5px rgba(0,0,0,0.05);'>"
sheet_cards_html += f"<div style='font-size: 11px; font-weight: 700; letter-spacing: 0.5px; opacity: 0.95; margin-bottom: 6px; text-transform: uppercase;'>{name}</div>"
sheet_cards_html += f"<div style='display: flex; justify-content: space-between; align-items: baseline;'>"
sheet_cards_html += f"<span style='font-size: 15px; font-weight: 700;'>{info['price']}</span>"
sheet_cards_html += f"<span style='font-size: 11px; font-weight: 600; background: rgba(255,255,255,0.2); padding: 1px 6px; border-radius: 4px;'>{change_sign}{info['change']:.2f}%</span>"
sheet_cards_html += f"</div></div></a>"
sheet_cards_html += "</div>"
with st.expander("📈 Click to view Top 250 Stocks Matrix", expanded=False):
if sheet_valid_cards_count == 0:
st.info("Stock matrix data is currently unavailable. Please check the 'Top 250 Stocks' sheet.")
else:
st.markdown(sheet_cards_html, unsafe_allow_html=True)
st.write("---")
@st.cache_data(ttl=300)
def get_ranked_sheet_data():
df = load_sheet_data_with_colors("Top 250 Stocks")
if df.empty:
return pd.DataFrame()
actual_cols = [c for c in df.columns if not c.startswith("_bg_") and not c.startswith("_txt_")]
sym_col = next((c for c in actual_cols if c.lower() in ["nse code", "symbol", "ticker", "stock symbol", "id", "stock"]), None)
cmp_col = next((c for c in actual_cols if "cmp" in c.lower()), None)
pct_col = next((c for c in actual_cols if "price %" in c.lower() or "change" in c.lower()), None)
vol_col = next((c for c in actual_cols if "volume" in c.lower()), None)
value_col = next((c for c in actual_cols if "value" in c.lower() and "face" not in c.lower() and "enterprise" not in c.lower()), None)
turnover_col = next((c for c in actual_cols if "turnover" in c.lower()), None)
if not sym_col:
return pd.DataFrame()
rank_df = pd.DataFrame()
rank_df['Symbol'] = df[sym_col].astype(str).str.strip()
rank_df['CMP'] = pd.to_numeric(df[cmp_col].astype(str).str.replace(r'[%,]', '', regex=True), errors='coerce') if cmp_col else 0.0
rank_df['Pct_Change'] = pd.to_numeric(df[pct_col].astype(str).str.replace(r'[%,]', '', regex=True), errors='coerce') if pct_col else 0.0
rank_df['Volume'] = pd.to_numeric(df[vol_col].astype(str).str.replace(r'[%,]', '', regex=True), errors='coerce') if vol_col else 0.0
fallback_calc = rank_df['CMP'] * rank_df['Volume']
if value_col:
rank_df['Value'] = pd.to_numeric(df[value_col].astype(str).str.replace(r'[a-zA-Z%, ]', '', regex=True), errors='coerce')
else:
rank_df['Value'] = fallback_calc
if turnover_col:
rank_df['Turnover'] = pd.to_numeric(df[turnover_col].astype(str).str.replace(r'[a-zA-Z%, ]', '', regex=True), errors='coerce')
else:
rank_df['Turnover'] = fallback_calc
rank_df = rank_df.dropna(subset=['Symbol', 'CMP']).reset_index(drop=True)
rank_df = rank_df[(rank_df['Symbol'] != 'nan') & (rank_df['Symbol'] != '')]
return rank_df
def build_ranking_cards_html(dataframe, metric_label="change"):
cards_html = "<div style='display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 20px; font-family: system-ui, -apple-system, sans-serif;'>"
if dataframe.empty:
return "<p style='color: gray; font-size: 14px;'>No data available for this ranking.</p>"
for _, row in dataframe.iterrows():
sym = row['Symbol']
price = row['CMP']
pct = row['Pct_Change']
bg_color = "
change_sign = "+" if pct >= 0 else ""
if metric_label == "volume":
vol = row.get('Volume', 0)
pill_text = f"Vol: {vol/1000000:.1f}M" if vol >= 1000000 else f"Vol: {vol:,.0f}"
elif metric_label == "value":
val = row.get('Value', 0)
pill_text = f"Val: ₹{val/10000000:,.1f}Cr" if val >= 10000000 else f"Val: ₹{val:,.0f}"
elif metric_label == "turnover":
to = row.get('Turnover', 0)
pill_text = f"T.O: ₹{to/10000000:,.1f}Cr" if to >= 10000000 else f"T.O: ₹{to:,.0f}"
elif metric_label == "vol_val":
vol = row.get('Volume', 0)
val = row.get('Value', 0)
v_str = f"{vol/1000000:.1f}M" if vol >= 1000000 else f"{vol/1000:.1f}k"
val_str = f"₹{val/10000000:,.1f}Cr" if val >= 10000000 else f"₹{val:,.0f}"
pill_text = f"📦 {v_str} | 💰 {val_str}"
else:
pill_text = f"{change_sign}{pct:.2f}%"
nse_url = f"https://www.nseindia.com/get-quotes/equity?symbol={sym}"
cards_html += f"<a href='{nse_url}' target='_blank' style='text-decoration:none;'>"
cards_html += f"<div style='background-color: {bg_color}; color: white; padding: 12px 16px; border-radius: 8px; flex: 1 1 calc(16.66% - 10px); min-width: 140px; box-shadow: 0 2px 5px rgba(0,0,0,0.05);'>"
cards_html += f"<div style='font-size: 11px; font-weight: 700; letter-spacing: 0.5px; opacity: 0.95; margin-bottom: 6px; text-transform: uppercase;'>{sym}</div>"
cards_html += f"<div style='display: flex; justify-content: space-between; align-items: baseline;'>"
cards_html += f"<span style='font-size: 15px; font-weight: 700;'>{price:,.2f}</span>"
cards_html += f"<span style='font-size: 11px; font-weight: 600; background: rgba(255,255,255,0.2); padding: 1px 6px; border-radius: 4px; white-space: nowrap;'>{pill_text}</span>"
cards_html += f"</div></div></a>"
cards_html += "</div>"
return cards_html
rank_data = get_ranked_sheet_data()
with st.expander("🏆 Click to view Advanced Ranking Dashboards (Top 250 Stocks)", expanded=False):
if rank_data.empty:
st.info("Ranking data is currently unavailable. Please check the 'Top 250 Stocks' sheet.")
else:
df_gainers = rank_data.nlargest(20, 'Pct_Change')
df_losers = rank_data.nsmallest(20, 'Pct_Change')
df_vol_gainers = rank_data.nlargest(20, 'Volume')
df_vol_losers = rank_data[rank_data['Volume'] > 0].nsmallest(20, 'Volume')
df_active_vol_val = rank_data.nlargest(20, 'Volume')
df_top_value = rank_data.nlargest(20, 'Value')
df_top_turnover = rank_data.nlargest(20, 'Turnover')
df_most_active = rank_data.nlargest(20, 'Value')
rank_tab1, rank_tab2, rank_tab3, rank_tab4, rank_tab5, rank_tab6 = st.tabs([
"📈 Gainers/Losers",
"📦 Volume Leaders",
"🔥 Active (Vol & Val)",
"💰 Top by Value",
"💎 Top by Turnover",
"💰 Most Active"
])
with rank_tab1:
st.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>🚀 Top 20 Gainers</p>", unsafe_allow_html=True)
st.markdown(build_ranking_cards_html(df_gainers, "change"), unsafe_allow_html=True)
st.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>🔻 Top 20 Losers</p>", unsafe_allow_html=True)
st.markdown(build_ranking_cards_html(df_losers, "change"), unsafe_allow_html=True)
with rank_tab2:
st.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>📦 Top 20 by Volume</p>", unsafe_allow_html=True)
st.markdown(build_ranking_cards_html(df_vol_gainers, "volume"), unsafe_allow_html=True)
st.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>💤 Bottom 20 by Volume</p>", unsafe_allow_html=True)
st.markdown(build_ranking_cards_html(df_vol_losers, "volume"), unsafe_allow_html=True)
with rank_tab3:
st.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>🔥 Most Active Stocks (Volume & Traded Value)</p>", unsafe_allow_html=True)
st.markdown(build_ranking_cards_html(df_active_vol_val, "vol_val"), unsafe_allow_html=True)
with rank_tab4:
st.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>💰 Most Active by Traded Value</p>", unsafe_allow_html=True)
st.markdown(build_ranking_cards_html(df_top_value, "value"), unsafe_allow_html=True)
with rank_tab5:
st.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>💎 Highest Market Turnover</p>", unsafe_allow_html=True)
st.markdown(build_ranking_cards_html(df_top_turnover, "turnover"), unsafe_allow_html=True)
with rank_tab6:
st.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>💰 Most Active (Highest Traded Value)</p>", unsafe_allow_html=True)
st.markdown(build_ranking_cards_html(df_most_active, "value"), unsafe_allow_html=True)
st.write("---")
def compute_bottom_fishing_score(row, actual_cols):
score = 0
reasons = []
def get_num(col_keywords, negate=False):
for kw in col_keywords:
col = next((c for c in actual_cols if kw.lower() in c.lower()), None)
if col and col in row:
try:
val = float(str(row[col]).replace('%','').replace(',','').strip())
return -val if negate else val
except: pass
return None
cmp = get_num(["cmp"])
low_52 = get_num(["52w low", "52 week low", "52wlow"])
if cmp and low_52 and low_52 > 0:
pct_from_low = ((cmp - low_52) / low_52) * 100
if 8 <= pct_from_low <= 15:
score += 30
reasons.append(f"✅ CMP +{pct_from_low:.1f}% from 52W Low (sweet zone)")
elif pct_from_low < 8:
score += 15
reasons.append(f"⚠️ CMP +{pct_from_low:.1f}% from 52W Low (still bottoming)")
elif pct_from_low <= 25:
score += 10
reasons.append(f"🟡 CMP +{pct_from_low:.1f}% from 52W Low (extended)")
else:
reasons.append(f"❌ CMP +{pct_from_low:.1f}% from 52W Low (too far)")
dma200 = get_num(["200 dma"])
if cmp and dma200 and dma200 > 0:
if cmp > dma200:
score += 15
reasons.append("✅ CMP above 200 DMA (uptrend confirmed)")
else:
diff_pct = ((cmp - dma200) / dma200) * 100
if diff_pct > -10:
score += 7
reasons.append(f"🟡 CMP {diff_pct:.1f}% below 200 DMA (near support)")
else:
reasons.append(f"❌ CMP {diff_pct:.1f}% below 200 DMA (downtrend)")
vol = get_num(["volume"])
if vol and vol > 0:
if vol >= 10_000_000:
score += 10
reasons.append(f"✅ High volume: {vol:,.0f}")
elif vol >= 1_000_000:
score += 6
reasons.append(f"🟡 Moderate volume: {vol:,.0f}")
else:
score += 2
reasons.append(f"⚠️ Low volume: {vol:,.0f}")
de = get_num(["d/e ratio", "debt", "d/e"])
if de is not None:
if de <= 0.1:
score += 10
reasons.append(f"✅ Debt-Free / Zero Debt (D/E={de:.2f})")
elif de <= 0.5:
score += 7
reasons.append(f"✅ Very Low Debt (D/E={de:.2f})")
elif de <= 1.0:
score += 4
reasons.append(f"🟡 Manageable Debt (D/E={de:.2f})")
else:
reasons.append(f"❌ High Debt (D/E={de:.2f})")
np_val = get_num(["net profit"])
if np_val is not None:
if np_val > 0:
score += 10
reasons.append(f"✅ Profitable: Net Profit ₹{np_val:.1f} Cr")
else:
reasons.append(f"❌ Loss Making: Net Profit ₹{np_val:.1f} Cr")
ronw = get_num(["ronw"])
if ronw is not None:
if ronw >= 15:
score += 10
reasons.append(f"✅ Strong RONW: {ronw:.1f}%")
elif ronw >= 8:
score += 6
reasons.append(f"🟡 Moderate RONW: {ronw:.1f}%")
elif ronw > 0:
score += 2
reasons.append(f"⚠️ Low RONW: {ronw:.1f}%")
else:
reasons.append(f"❌ Negative RONW: {ronw:.1f}%")
promo = get_num(["promoters %", "promoter"])
if promo is not None:
if promo >= 50:
score += 8
reasons.append(f"✅ Promoter Holding: {promo:.1f}%")
elif promo >= 35:
score += 5
reasons.append(f"🟡 Promoter Holding: {promo:.1f}%")
else:
reasons.append(f"⚠️ Low Promoter: {promo:.1f}%")
pledge = get_num(["pledged %", "pledged"])
if pledge is not None:
if pledge == 0:
score += 7
reasons.append("✅ Zero Pledged Shares")
elif pledge <= 5:
score += 4
reasons.append(f"🟡 Low Pledge: {pledge:.1f}%")
else:
reasons.append(f"❌ High Pledge: {pledge:.1f}%")
sales = get_num(["net sales", "net sale"])
if sales and sales > 0:
reasons.append(f"📊 Net Sales: ₹{sales:.1f} Cr")
delivery_pct = get_num(["delivery"])
if delivery_pct is not None:
reasons.append(f"📦 % Delivery: {delivery_pct:.1f}%")
if score >= 75:
grade = "🟢 STRONG BUY"
elif score >= 55:
grade = "🟡 WATCHLIST"
elif score >= 35:
grade = "🟠 CAUTION"
else:
grade = "🔴 AVOID"
return score, grade, reasons
WATCHLIST_SHEET_NAME = "Watchlist"
def get_gspread_client():
if "gcp_service_account" not in st.secrets:
return None
info = st.secrets["gcp_service_account"]
if isinstance(info, str):
info = json.loads(info)
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_info(info, scopes=scope)
return gspread.authorize(creds)
SPREADSHEET_ID = "1SFhuZbLLlwwFsNo1k2RRx_Zp6bAkRR20W0F_zTwgdwU"
def ensure_watchlist_sheet(client):
try:
ss = client.open_by_key(SPREADSHEET_ID)
try:
return ss.worksheet(WATCHLIST_SHEET_NAME)
except gspread.WorksheetNotFound:
ws = ss.add_worksheet(title=WATCHLIST_SHEET_NAME, rows=500, cols=6)
ws.append_row(["Symbol", "CMP", "Note", "BF Score", "BF Grade", "Added On"])
return ws
except Exception:
return None
def load_watchlist_from_sheet():
client = get_gspread_client()
if not client:
return
ws = ensure_watchlist_sheet(client)
if not ws:
return
try:
records = ws.get_all_records()
loaded = {}
for r in records:
sym = str(r.get("Symbol", "")).strip()
if sym:
loaded[sym] = {
"note":  str(r.get("Note", "")),
"cmp":   str(r.get("CMP", "")),
"bf_score": str(r.get("BF Score", "")),
"bf_grade": str(r.get("BF Grade", "")),
"added": str(r.get("Added On", "")),
}
st.session_state.watchlist = loaded
except Exception:
pass
def save_watchlist_to_sheet():
client = get_gspread_client()
if not client:
st.warning("⚠️ Google Sheet write failed — check secrets.")
return False
ws = ensure_watchlist_sheet(client)
if not ws:
return False
try:
ws.clear()
ws.append_row(["Symbol", "CMP", "Note", "BF Score", "BF Grade", "Added On"])
for sym, info in st.session_state.watchlist.items():
ws.append_row([
sym,
info.get("cmp", ""),
info.get("note", ""),
info.get("bf_score", ""),
info.get("bf_grade", ""),
info.get("added", ""),
])
return True
except Exception as e:
st.warning(f"⚠️ Sheet write error: {e}")
return False
def watchlist_add(sym, cmp="", note="", bf_score="", bf_grade=""):
st.session_state.watchlist[sym] = {
"cmp": cmp, "note": note,
"bf_score": bf_score, "bf_grade": bf_grade,
"added": datetime.now().strftime("%Y-%m-%d %H:%M"),
}
def watchlist_remove(sym):
st.session_state.watchlist.pop(sym, None)
if "watchlist_loaded" not in st.session_state:
load_watchlist_from_sheet()
st.session_state.watchlist_loaded = True
def compute_gtt(row_data: dict, cols: list) -> dict:
def _num(keys):
for k in keys:
for c in cols:
if k in c.lower():
try:
v = str(row_data.get(c, "")).replace(",", "").replace("%", "").strip()
return float(v)
except (ValueError, TypeError):
pass
return None
cmp   = _num(["cmp"])
high  = _num(["52w high", "52 week high", "52wk high"])
low   = _num(["52w low",  "52 week low",  "52wk low"])
dma50 = _num(["50 dma", "50dma"])
dma200= _num(["200 dma","200dma"])
result = {"cmp": cmp, "52w_high": high, "52w_low": low, "dma50": dma50, "dma200": dma200}
if cmp and high and low:
atr_approx = (high - low) / 52
result["atr_approx"] = round(atr_approx, 2)
result["sl_tight"]    = round(cmp - 1.0 * atr_approx, 2)
result["sl_standard"] = round(cmp - 1.5 * atr_approx, 2)
result["sl_wide"]     = round(cmp - 2.0 * atr_approx, 2)
rr = 2.0
sl_gap = cmp - result["sl_standard"]
result["target_1r"]  = round(cmp + sl_gap * 1.0, 2)
result["target_2r"]  = round(cmp + sl_gap * rr,  2)
result["target_3r"]  = round(cmp + sl_gap * 3.0, 2)
result["trail_sl_50dma"]  = round(dma50,  2) if dma50  else None
result["trail_sl_200dma"] = round(dma200, 2) if dma200 else None
result["risk_pct"] = round((sl_gap / cmp) * 100, 2) if cmp else None
return result
def ai_results_to_excel(history: list) -> bytes:
if not history:
return b""
df = pd.DataFrame(history, columns=["Symbol", "Model", "Query", "AI Result", "Timestamp"])
buf = io.BytesIO()
with pd.ExcelWriter(buf, engine="openpyxl") as writer:
df.to_excel(writer, index=False, sheet_name="AI Analysis")
ws = writer.sheets["AI Analysis"]
ws.column_dimensions["A"].width = 12
ws.column_dimensions["B"].width = 14
ws.column_dimensions["C"].width = 40
ws.column_dimensions["D"].width = 80
ws.column_dimensions["E"].width = 20
return buf.getvalue()
if st.sidebar.button("🧹 Clear All Filters", use_container_width=True):
for key in list(st.session_state.keys()):
if key.startswith("filter_") or key in ("search_query", "main_matrix_search", "perf_matrix_search", "bf_search"):
del st.session_state[key]
st.session_state.grid_reset_token += 1
st.rerun()
st.sidebar.markdown("---")
st.sidebar.header("🔍 Global Search")
search_query = st.sidebar.text_input("Search by Symbol, Name, etc...", key="search_query")
st.sidebar.markdown("---")
st.sidebar.header("📑 Select a Tab")
sheet_names = ["Top 250 Stocks", "NSE Fundamentals", "Final List", "Final List 2", "Diff @ 200 DMA", "+%", "-%"]
selected_sheet = st.sidebar.selectbox("Choose sheet", sheet_names, key="filter_sheet")
st.markdown(f"<p style='font-size:0.85rem; font-weight:bold; margin:0; padding:0;'>📄 {selected_sheet}</p>", unsafe_allow_html=True)
with st.spinner("Downloading data from Google API..."):
raw_df = load_sheet_data_with_colors(selected_sheet)
if not raw_df.empty:
guess_idx = 0
actual_cols = [c for c in raw_df.columns if not c.startswith("_bg_") and not c.startswith("_txt_")]
hidden_cols_for_sheet = get_hidden_columns(selected_sheet, actual_cols)
locked_symbol_override = LOCKED_SYMBOL_COLUMN.get(selected_sheet)
if locked_symbol_override and locked_symbol_override in actual_cols:
guess_idx = actual_cols.index(locked_symbol_override)
else:
for i, col_name in enumerate(actual_cols):
if col_name.lower() in ["nse code", "symbol", "ticker", "stock symbol", "id", "stock"]:
guess_idx = i
break
st.sidebar.markdown("---")
st.sidebar.header("⚙️ Settings")
selected_symbol_col = st.sidebar.selectbox(
"Symbol Column (locked):", actual_cols, index=guess_idx, key="filter_symbol_col",
disabled=True, help="Locked for consistency across sheets. To change it, edit "
"LOCKED_SYMBOL_COLUMN near the top of the .py file."
)
final_df = process_hyperlinks(raw_df, selected_symbol_col)
filtered_df = final_df.copy()
if search_query:
mask = filtered_df[actual_cols].astype(str).apply(lambda x: x.str.contains(search_query, case=False, na=False)).any(axis=1)
filtered_df = filtered_df[mask]
st.sidebar.markdown("---")
st.sidebar.header("🎨 Color Filters")
color_filter_col = st.sidebar.selectbox("Select Column to Filter by Color:", ["None"] + actual_cols, key="filter_color_col")
if color_filter_col != "None":
bg_col_reference = f"_bg_{color_filter_col}"
if bg_col_reference in filtered_df.columns:
unique_hexes = filtered_df[bg_col_reference].unique()
color_dictionary = {
"
"
"
"
"
"
"
"
"
}
ui_color_options = []
for hx in unique_hexes:
hx_lower = str(hx).lower()
if hx_lower in color_dictionary:
ui_color_options.append(color_dictionary[hx_lower])
else:
ui_color_options.append(f"🎨 Custom Hex: {hx_lower}")
selected_ui_colors = st.sidebar.multiselect(f"Select Colors in '{color_filter_col}':", sorted(ui_color_options), key="filter_color_selections")
if selected_ui_colors:
valid_hexes_to_keep = []
for ui_choice in selected_ui_colors:
for hex_key, name in color_dictionary.items():
if name == ui_choice:
valid_hexes_to_keep.append(hex_key)
if ui_choice.startswith("🎨 Custom Hex: "):
valid_hexes_to_keep.append(ui_choice.replace("🎨 Custom Hex: ", ""))
filtered_df = filtered_df[filtered_df[bg_col_reference].str.lower().isin(valid_hexes_to_keep)]
st.sidebar.markdown("---")
st.sidebar.header("🎯 Categorical Filters")
active_filters = [c for c in actual_cols if any(key in c.lower() for key in [
"cumulative average", "industry", "sector", "output", "start gtt order",
"volume trend", "breakout signal", "trend", "macd crossover", "buy signal"
])]
for col_to_filter in active_filters:
unique_options = sorted([val for val in final_df[col_to_filter].unique() if str(val).strip() != ""])
selected_options = st.sidebar.multiselect(f"Filter by {col_to_filter}:", options=unique_options, key=f"filter_cat_{col_to_filter}")
if selected_options:
filtered_df = filtered_df[filtered_df[col_to_filter].isin(selected_options)]
st.sidebar.markdown("---")
st.sidebar.header("📈 DMA Trend Filter")
dma_choice = st.sidebar.selectbox("Select DMA Condition:", [
"All (No Filter)", "50 DMA < 100 DMA < 200 DMA", "50 DMA > 100 DMA > 200 DMA",
"50 DMA > 200 DMA", "50 DMA < 200 DMA"], key="filter_dma_trend")
if dma_choice != "All (No Filter)":
dma50_col = next((c for c in actual_cols if "50 dma" in c.lower()), None)
dma100_col = next((c for c in actual_cols if "100 dma" in c.lower()), None)
dma200_col = next((c for c in actual_cols if "200 dma" in c.lower()), None)
if dma50_col and dma200_col:
s50 = pd.to_numeric(filtered_df[dma50_col].astype(str).str.replace(r'[%,]', '', regex=True), errors='coerce')
s200 = pd.to_numeric(filtered_df[dma200_col].astype(str).str.replace(r'[%,]', '', regex=True), errors='coerce')
if dma_choice == "50 DMA > 200 DMA": filtered_df = filtered_df[s50 > s200]
elif dma_choice == "50 DMA < 200 DMA": filtered_df = filtered_df[s50 < s200]
elif dma100_col:
s100 = pd.to_numeric(filtered_df[dma100_col].astype(str).str.replace(r'[%,]', '', regex=True), errors='coerce')
if dma_choice == "50 DMA < 100 DMA < 200 DMA": filtered_df = filtered_df[(s50 < s100) & (s100 < s200)]
elif dma_choice == "50 DMA > 100 DMA > 200 DMA": filtered_df = filtered_df[(s50 > s100) & (s100 > s200)]
st.sidebar.markdown("---")
st.sidebar.header("📊 Numeric Range Filters")
diff_200_col = next((c for c in actual_cols if "diff" in c.lower() and "200" in c.lower()), None)
if diff_200_col: filtered_df = apply_numeric_slider(filtered_df, diff_200_col, st.sidebar, "Diff. from 200 DMA Range:")
low_pct_col = next((c for c in actual_cols if "52" in c.lower() and "low" in c.lower() and ("%" in c.lower() or "per" in c.lower())), None)
if low_pct_col: filtered_df = apply_numeric_slider(filtered_df, low_pct_col, st.sidebar, "From 52W Low Range:")
high_pct_col = next((c for c in actual_cols if "52" in c.lower() and "high" in c.lower() and ("%" in c.lower() or "per" in c.lower())), None)
if high_pct_col: filtered_df = apply_numeric_slider(filtered_df, high_pct_col, st.sidebar, "From 52W High Range:")
numeric_targets = ["Volume", "CMP", "Price %", "Promoters %", "Institutional %", "Face Value", "Net Profit", "EPS", "RONW %", "Market Cap", "Enterprise Value", "RSI", "Delivery"]
processed_cols = {diff_200_col, low_pct_col, high_pct_col}
for target in numeric_targets:
col_match = next((c for c in actual_cols if target.lower() in c.lower() and c not in processed_cols), None)
if col_match:
filtered_df = apply_numeric_slider(filtered_df, col_match, st.sidebar)
processed_cols.add(col_match)
st.sidebar.markdown("---")
st.sidebar.header("📅 Date Filters")
high_date_col = next((c for c in actual_cols if "52w high date" in c.lower()), None)
low_date_col = next((c for c in actual_cols if "52w low date" in c.lower()), None)
if high_date_col: filtered_df = apply_date_filter(filtered_df, high_date_col, st.sidebar)
if low_date_col: filtered_df = apply_date_filter(filtered_df, low_date_col, st.sidebar)
st.sidebar.markdown("---")
st.sidebar.header("📊 My Watchlist")
if st.session_state.watchlist:
wl_count = len(st.session_state.watchlist)
st.sidebar.caption(f"🔖 {wl_count} stock{'s' if wl_count > 1 else ''} saved")
for _ws, _wi in list(st.session_state.watchlist.items()):
_col1, _col2 = st.sidebar.columns([3, 1])
_col1.markdown(
f"**{_ws}** {'`' + _wi['cmp'] + '`' if _wi['cmp'] else ''}<br>"
f"<small style='color:gray'>{_wi.get('note','')[:35]}</small>",
unsafe_allow_html=True,
)
if _col2.button("❌", key=f"wl_rm_{_ws}", help=f"Remove {_ws}"):
watchlist_remove(_ws)
save_watchlist_to_sheet()
st.rerun()
st.sidebar.markdown("")
_wl_df = pd.DataFrame([
{"Symbol": s, "CMP": d["cmp"], "Note": d["note"],
"BF Score": d.get("bf_score",""), "BF Grade": d.get("bf_grade",""),
"Added On": d["added"]}
for s, d in st.session_state.watchlist.items()
])
_wl_buf = io.BytesIO()
with pd.ExcelWriter(_wl_buf, engine="openpyxl") as _w:
_wl_df.to_excel(_w, index=False, sheet_name="Watchlist")
st.sidebar.download_button(
"📥 Download Watchlist Excel",
data=_wl_buf.getvalue(),
file_name=f"Watchlist_{datetime.now().strftime('%Y%m%d')}.xlsx",
mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
use_container_width=True,
)
else:
st.sidebar.info("No stocks in watchlist yet.\nAdd from the workspace panel below.")
if st.session_state.ai_history:
st.sidebar.markdown("---")
st.sidebar.header("🤖 AI History Export")
st.sidebar.caption(f"{len(st.session_state.ai_history)} analyses saved this session")
_ai_xl = ai_results_to_excel(st.session_state.ai_history)
st.sidebar.download_button(
"📥 Download All AI Results (Excel)",
data=_ai_xl,
file_name=f"AI_Analysis_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx",
mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
use_container_width=True,
)
if st.sidebar.button("🗑️ Clear AI History", use_container_width=True):
st.session_state.ai_history = []
st.rerun()
core_sequence = []
if selected_symbol_col in filtered_df.columns:
core_sequence.append(selected_symbol_col)
vol_target = next((c for c in actual_cols if "volume" in c.lower()), None)
close_target = next((c for c in actual_cols if "close price" in c.lower() or "prev" in c.lower()), None)
cmp_target = next((c for c in actual_cols if "cmp" in c.lower()), None)
pct_target = next((c for c in actual_cols if "price %" in c.lower()), None)
high_target = next((c for c in actual_cols if "52" in c.lower() and "high" in c.lower() and "date" not in c.lower() and "%" not in c.lower()), None)
low_target = next((c for c in actual_cols if "52" in c.lower() and "low" in c.lower() and "date" not in c.lower() and "%" not in c.lower()), None)
deliv_target = next((c for c in actual_cols if "delivery" in c.lower()), None)
rsi_target = next((c for c in actual_cols if "rsi" in c.lower()), None)
volume_trend_target = next((c for c in actual_cols if "volume trend" in c.lower()), None)
breakout_signal_target = next((c for c in actual_cols if "breakout signal" in c.lower()), None)
trend_target = next((c for c in actual_cols if "trend" in c.lower() and c != volume_trend_target and "dma" not in c.lower()), None)
macd_crossover_target = next((c for c in actual_cols if "macd" in c.lower()), None)
buy_signal_target = next((c for c in actual_cols if "buy signal" in c.lower()), None)
diff_200_target = next((c for c in actual_cols if "diff" in c.lower() and "200" in c.lower()), None)
configured_priority = get_priority_columns(selected_sheet, actual_cols)
if configured_priority:
for col in configured_priority:
if col not in core_sequence:
core_sequence.append(col)
else:
for target in (vol_target, close_target, cmp_target, pct_target, high_target, low_target):
if target and target not in core_sequence:
core_sequence.append(target)
all_other_fields = [c for c in filtered_df.columns if c not in core_sequence and not c.startswith("_bg_") and not c.startswith("_txt_") and c != "_raw_symbol_"]
hidden_meta_attributes = [c for c in filtered_df.columns if c.startswith("_bg_") or c.startswith("_txt_") or c == "_raw_symbol_"]
enforced_column_layout = core_sequence + all_other_fields + hidden_meta_attributes
filtered_df = filtered_df[enforced_column_layout]
st.markdown("---")
st.subheader(f"🚀 Executive Dashboard — {selected_sheet}")
st.caption("Live snapshot of the currently filtered stock universe. Adjust sidebar filters to update instantly.")
def _dash_numify(series):
if series is None:
return pd.Series(dtype=float)
return pd.to_numeric(
series.astype(str).str.replace(r'[%,₹\s]', '', regex=True),
errors='coerce'
)
dash_df = filtered_df
total_stocks = len(dash_df)
pct_series = _dash_numify(dash_df[pct_target]) if pct_target and pct_target in dash_df.columns else pd.Series(dtype=float)
vol_series = _dash_numify(dash_df[vol_target]) if vol_target and vol_target in dash_df.columns else pd.Series(dtype=float)
cmp_series = _dash_numify(dash_df[cmp_target]) if cmp_target and cmp_target in dash_df.columns else pd.Series(dtype=float)
high_series = _dash_numify(dash_df[high_target]) if high_target and high_target in dash_df.columns else pd.Series(dtype=float)
low_series = _dash_numify(dash_df[low_target]) if low_target and low_target in dash_df.columns else pd.Series(dtype=float)
rsi_series = _dash_numify(dash_df[rsi_target]) if rsi_target and rsi_target in dash_df.columns else pd.Series(dtype=float)
deliv_series = _dash_numify(dash_df[deliv_target]) if deliv_target and deliv_target in dash_df.columns else pd.Series(dtype=float)
mcap_target = next((c for c in actual_cols if "market cap" in c.lower()), None)
mcap_series = _dash_numify(dash_df[mcap_target]) if mcap_target and mcap_target in dash_df.columns else pd.Series(dtype=float)
diff200_series = _dash_numify(dash_df[diff_200_target]) if diff_200_target and diff_200_target in dash_df.columns else pd.Series(dtype=float)
turnover_target = next((c for c in actual_cols if "turnover" in c.lower()), None)
turnover_series = _dash_numify(dash_df[turnover_target]) if turnover_target and turnover_target in dash_df.columns else pd.Series(dtype=float)
advances = int((pct_series > 0).sum()) if not pct_series.empty else 0
declines = int((pct_series < 0).sum()) if not pct_series.empty else 0
unchanged = int((pct_series == 0).sum()) if not pct_series.empty else 0
avg_change = float(pct_series.mean()) if pct_series.notna().any() else 0.0
adv_decline_ratio = (advances / declines) if declines > 0 else None
median_change = float(pct_series.median()) if pct_series.notna().any() else None
total_volume = float(vol_series.sum()) if vol_series.notna().any() else 0.0
total_mcap = float(mcap_series.sum()) if mcap_series.notna().any() else 0.0
total_turnover = float(turnover_series.sum()) if turnover_series.notna().any() else 0.0
avg_rsi = float(rsi_series.mean()) if rsi_series.notna().any() else None
avg_deliv = float(deliv_series.mean()) if deliv_series.notna().any() else None
above_200dma_count = int((diff200_series > 0).sum()) if diff200_series.notna().any() else 0
below_200dma_count = int((diff200_series < 0).sum()) if diff200_series.notna().any() else 0
breakout_count = 0
if breakout_signal_target and breakout_signal_target in dash_df.columns:
breakout_count = int(dash_df[breakout_signal_target].astype(str).str.contains("breakout|buy|bullish", case=False, na=False).sum())
buy_signal_count = 0
if buy_signal_target and buy_signal_target in dash_df.columns:
buy_signal_count = int(dash_df[buy_signal_target].astype(str).str.contains("buy", case=False, na=False).sum())
near_high_count, near_low_count = 0, 0
near_low_15_count = 0
if cmp_series.notna().any() and high_series.notna().any():
prox_high = (cmp_series / high_series.replace(0, np.nan)) * 100
near_high_count = int((prox_high >= 95).sum())
if cmp_series.notna().any() and low_series.notna().any():
prox_low = (cmp_series / low_series.replace(0, np.nan)) * 100
near_low_count = int((prox_low <= 105).sum())
near_low_15_count = int((prox_low <= 115).sum())
def _dash_kpi(container, label, value, bg="
container.markdown(
f"<div style='background:{bg}; border-radius:10px; padding:12px 8px; text-align:center; border:1px solid rgba(0,0,0,0.06);'>"
f"<div style='font-size:0.70em; color:
f"<div style='font-size:1.30em; font-weight:800; color:{fg}; margin-top:2px;'>{value}</div>"
f"</div>",
unsafe_allow_html=True
)
kpi_row1 = st.columns(7)
_dash_kpi(kpi_row1[0], "📦 TOTAL STOCKS", f"{total_stocks:,}")
_dash_kpi(kpi_row1[1], "🟢 ADVANCES", f"{advances:,}", bg="
_dash_kpi(kpi_row1[2], "🔴 DECLINES", f"{declines:,}", bg="
_dash_kpi(kpi_row1[3], "⚪ UNCHANGED", f"{unchanged:,}")
_dash_kpi(
kpi_row1[4], "🕳️ NEAR 52W LOW (≤15%)",
f"{near_low_15_count:,}" if (cmp_series.notna().any() and low_series.notna().any()) else "N/A",
bg="
)
_dash_kpi(kpi_row1[5], "🚀 BREAKOUTS", f"{breakout_count:,}", bg="
_dash_kpi(kpi_row1[6], "✅ BUY SIGNALS", f"{buy_signal_count:,}", bg="
st.markdown("<div style='margin-top:8px;'></div>", unsafe_allow_html=True)
kpi_row2 = st.columns(4)
_dash_kpi(kpi_row2[0], "🏔️ NEAR 52W HIGH (≥95%)", f"{near_high_count:,}", bg="
_dash_kpi(kpi_row2[1], "🕳️ NEAR 52W LOW (≤5%)", f"{near_low_count:,}", bg="
_dash_kpi(kpi_row2[2], "📉 BELOW 200 DMA", f"{below_200dma_count:,}" if diff200_series.notna().any() else "N/A", bg="
_dash_kpi(kpi_row2[3], "🎯 ABOVE 200 DMA", f"{above_200dma_count:,}" if diff200_series.notna().any() else "N/A", bg="
st.markdown("<br>", unsafe_allow_html=True)
DASH_CHART_CONFIG = {"displaylogo": False, "modeBarButtons": [["toImage"]]}
def _gradient_color(frac):
frac = max(0.0, min(1.0, frac))
stops = [(0.0, (234, 67, 53)), (0.5, (249, 168, 37)), (1.0, (15, 157, 88))]
for i in range(len(stops) - 1):
f0, c0 = stops[i]
f1, c1 = stops[i + 1]
if f0 <= frac <= f1:
t = (frac - f0) / (f1 - f0) if f1 > f0 else 0.0
r = int(c0[0] + (c1[0] - c0[0]) * t)
g = int(c0[1] + (c1[1] - c0[1]) * t)
b = int(c0[2] + (c1[2] - c0[2]) * t)
return f"
return "
def _render_dot_scatter_html(title_text, points, y_min, y_max, y_label, height=340):
if not points:
st.info("No data available for this chart.")
return
n = len(points)
span = (y_max - y_min) or 1.0
dots_html = ""
for i, (sym, val, url) in enumerate(points):
frac = (val - y_min) / span
frac_c = max(0.0, min(1.0, frac))
color = _gradient_color(frac_c)
left_pct = (i / max(n - 1, 1)) * 100
top_pct = (1 - frac_c) * 100
dots_html += (
f'<a href="{url}" target="_blank" title="{sym}: {val:.2f}{y_label}" '
f'style="position:absolute; left:{left_pct:.3f}%; top:{top_pct:.3f}%; '
f'width:11px; height:11px; margin:-6px 0 0 -6px; border-radius:50%; '
f'background:{color}; display:block; border:1px solid rgba(255,255,255,0.75); '
f'box-shadow:0 0 1px rgba(0,0,0,0.35); cursor:pointer;"></a>'
)
gridlines = ""
for gp, gv in [(0, y_max), (25, None), (50, (y_min + y_max) / 2), (75, None), (100, y_min)]:
label = f"{gv:.0f}" if gv is not None else ""
gridlines += (
f'<div style="position:absolute; left:0; right:0; top:{gp}%; border-top:1px dashed rgba(0,0,0,0.08); height:0;">'
f'<span style="position:absolute; left:-2px; top:-8px; font-size:10px; color:
)
html = (
f'<div style="font-family:\'Source Sans Pro\',sans-serif;">'
f'<div style="font-weight:700; font-size:14px; margin-bottom:2px;">{title_text}</div>'
f'<div style="font-size:11px; color:
f'<div style="position:relative; width:calc(100% - 26px); height:{height}px; margin-left:26px; '
f'background:
f'{gridlines}'
f'{dots_html}'
f'</div>'
f'<div style="display:flex; justify-content:space-between; margin-left:26px; margin-top:4px;">'
f'<span style="font-size:10px; color:
f'<span style="font-size:10px; color:
f'<span style="font-size:10px; color:
f'</div>'
f'</div>'
)
components.html(html, height=height + 90, scrolling=False)
dash_c1, dash_c2, dash_c3 = st.columns([1, 1.3, 1.3])
with dash_c1:
if advances or declines or unchanged:
fig_breadth = go.Figure(data=[go.Pie(
labels=["Advances", "Declines", "Unchanged"],
values=[advances, declines, unchanged],
hole=0.55,
marker=dict(colors=["
)])
fig_breadth.update_layout(title="Market Breadth", template="plotly_white", height=300,
margin=dict(t=40, b=10, l=10, r=10), showlegend=True)
st.plotly_chart(fig_breadth, use_container_width=True, key=f"dash_breadth_{selected_sheet}", config=DASH_CHART_CONFIG)
else:
st.info("No % change column detected for breadth chart.")
with dash_c2:
if pct_series.notna().any():
fig_pcthist = go.Figure(data=[go.Histogram(x=pct_series.dropna(), nbinsx=30, marker_color="
fig_pcthist.update_layout(title="% Change Distribution", template="plotly_white", height=300,
margin=dict(t=40, b=10, l=10, r=10), xaxis_title="% Change", yaxis_title="Stocks")
st.plotly_chart(fig_pcthist, use_container_width=True, key=f"dash_pcthist_{selected_sheet}", config=DASH_CHART_CONFIG)
else:
st.info("No % change column detected.")
with dash_c3:
if rsi_series.notna().any():
fig_rsihist = go.Figure(data=[go.Histogram(x=rsi_series.dropna(), nbinsx=25, marker_color="
fig_rsihist.add_vrect(x0=0, x1=30, fillcolor="
fig_rsihist.add_vrect(x0=70, x1=100, fillcolor="
fig_rsihist.update_layout(title="RSI(14) Distribution", template="plotly_white", height=300,
margin=dict(t=40, b=10, l=10, r=10), xaxis_title="RSI")
st.plotly_chart(fig_rsihist, use_container_width=True, key=f"dash_rsihist_{selected_sheet}", config=DASH_CHART_CONFIG)
else:
st.info("No RSI column detected for this sheet.")
dash_c4, dash_c5, dash_c6 = st.columns(3)
if selected_symbol_col in dash_df.columns:
symbol_series = dash_df[selected_symbol_col].astype(str)
elif "_raw_symbol_" in dash_df.columns:
symbol_series = dash_df["_raw_symbol_"].astype(str)
else:
symbol_series = dash_df.index.astype(str).to_series(index=dash_df.index)
if "_raw_symbol_" in dash_df.columns:
clean_symbol_series = dash_df["_raw_symbol_"].astype(str).str.strip()
else:
clean_symbol_series = symbol_series.astype(str).str.replace(r"<[^>]+>", "", regex=True).str.strip()
def _render_clickable_dot_scatter(fig, chart_key):
fig.update_layout(clickmode="event+select")
try:
event = st.plotly_chart(fig, use_container_width=True, key=chart_key, on_select="rerun")
except TypeError:
st.plotly_chart(fig, use_container_width=True, key=chart_key)
st.caption("⚠️ Click-to-open needs Streamlit ≥ 1.35 — update `streamlit` in requirements.txt to enable it.")
return
clicked_symbol = None
sel = event.get("selection") if isinstance(event, dict) else getattr(event, "selection", None)
if sel:
pts = sel.get("points") if isinstance(sel, dict) else getattr(sel, "points", None)
if pts:
last_pt = pts[-1]
cd = last_pt.get("customdata") if isinstance(last_pt, dict) else getattr(last_pt, "customdata", None)
if cd:
clicked_symbol = cd[0] if isinstance(cd, (list, tuple)) else cd
if clicked_symbol:
nse_chart_url = f"https://charting.nseindia.com/?symbol={clicked_symbol}-EQ"
cl1, cl2 = st.columns([3, 1])
with cl1:
st.success(f"Selected: **{clicked_symbol}**")
with cl2:
st.link_button("📈 Open on NSE", nse_chart_url, use_container_width=True)
st.markdown(
f"🔗 **More links for {clicked_symbol}:** "
f"[Trading View (🔗)](https://www.tradingview.com/symbols/{clicked_symbol}/) &nbsp;|&nbsp; "
f"[History Data (🔗)](https://www.equitypandit.com/historical-data/{clicked_symbol}) &nbsp;|&nbsp; "
f"[Screener (🔗)](https://www.screener.in/company/{clicked_symbol}) &nbsp;|&nbsp; "
f"[Zerodha (🔗)](https://zerodha.com/markets/stocks/NSE/{clicked_symbol}) &nbsp;|&nbsp; "
f"[Chartlink (🔗)](https://chartink.com/stocks-new?load-snapshot=exponential-moving-average-simple-moving-average-simple-moving-average-moving-average-convergence-divergence-chart-snapshot-175&symbol={clicked_symbol}) &nbsp;|&nbsp; "
f"[Market Smith (🔗)](https://marketsmithindia.com/mstool/eval/{clicked_symbol}/evaluation.jsp) &nbsp;|&nbsp; "
f"[NSE URL (🔗)](https://www.nseindia.com/get-quotes/equity?symbol={clicked_symbol})"
)
else:
st.caption("Click any dot above to select a stock — its NSE chart button and quick-links will appear here.")
with dash_c4:
if pct_series.notna().any():
top_gain_idx = pct_series.dropna().sort_values(ascending=False).head(10).index
top_g = pd.DataFrame({
"Symbol": symbol_series.loc[top_gain_idx].values,
"Change %": pct_series.loc[top_gain_idx].values
}).iloc[::-1]
fig_g = go.Figure(go.Bar(x=top_g["Change %"], y=top_g["Symbol"], orientation='h', marker_color="
fig_g.update_layout(title="🏆 Top 10 Gainers", template="plotly_white", height=340, margin=dict(t=40, b=10, l=10, r=10))
st.plotly_chart(fig_g, use_container_width=True, key=f"dash_topgain_{selected_sheet}", config=DASH_CHART_CONFIG)
else:
st.info("No % change column detected.")
with dash_c5:
if pct_series.notna().any():
top_lose_idx = pct_series.dropna().sort_values(ascending=True).head(10).index
top_l = pd.DataFrame({
"Symbol": symbol_series.loc[top_lose_idx].values,
"Change %": pct_series.loc[top_lose_idx].values
}).iloc[::-1]
fig_l = go.Figure(go.Bar(x=top_l["Change %"], y=top_l["Symbol"], orientation='h', marker_color="
fig_l.update_layout(title="📉 Top 10 Losers", template="plotly_white", height=340, margin=dict(t=40, b=10, l=10, r=10))
st.plotly_chart(fig_l, use_container_width=True, key=f"dash_toplose_{selected_sheet}", config=DASH_CHART_CONFIG)
else:
st.info("No % change column detected.")
with dash_c6:
if vol_series.notna().any():
top_vol_idx = vol_series.dropna().sort_values(ascending=False).head(10).index
top_v = pd.DataFrame({
"Symbol": symbol_series.loc[top_vol_idx].values,
"Volume": vol_series.loc[top_vol_idx].values
}).iloc[::-1]
fig_v = go.Figure(go.Bar(x=top_v["Volume"], y=top_v["Symbol"], orientation='h', marker_color="
fig_v.update_layout(title="🔥 Top 10 by Volume", template="plotly_white", height=340, margin=dict(t=40, b=10, l=10, r=10))
st.plotly_chart(fig_v, use_container_width=True, key=f"dash_topvol_{selected_sheet}", config=DASH_CHART_CONFIG)
else:
st.info("No Volume column detected for this sheet.")
dash_n1, dash_n2, dash_n3 = st.columns(3)
with dash_n1:
if cmp_series.notna().any() and high_series.notna().any():
pct_from_high = ((high_series - cmp_series) / high_series.replace(0, np.nan) * 100)
near_high_idx = pct_from_high.dropna().sort_values(ascending=True).head(10).index
near_h = pd.DataFrame({
"Symbol": symbol_series.loc[near_high_idx].values,
"% Below 52W High": pct_from_high.loc[near_high_idx].values
}).iloc[::-1]
fig_nh = go.Figure(go.Bar(x=near_h["% Below 52W High"], y=near_h["Symbol"], orientation='h', marker_color="
fig_nh.update_layout(title="🏔️ Top 10 Nearest 52W High", template="plotly_white", height=340, margin=dict(t=40, b=10, l=10, r=10))
st.plotly_chart(fig_nh, use_container_width=True, key=f"dash_nearhigh_{selected_sheet}", config=DASH_CHART_CONFIG)
else:
st.info("52-Week High column not detected for this sheet.")
with dash_n2:
if cmp_series.notna().any() and low_series.notna().any():
pct_from_low = ((cmp_series - low_series) / low_series.replace(0, np.nan) * 100)
near_low_idx = pct_from_low.dropna().sort_values(ascending=True).head(10).index
near_l = pd.DataFrame({
"Symbol": symbol_series.loc[near_low_idx].values,
"% Above 52W Low": pct_from_low.loc[near_low_idx].values
}).iloc[::-1]
fig_nl = go.Figure(go.Bar(x=near_l["% Above 52W Low"], y=near_l["Symbol"], orientation='h', marker_color="
fig_nl.update_layout(title="🕳️ Top 10 Nearest 52W Low", template="plotly_white", height=340, margin=dict(t=40, b=10, l=10, r=10))
st.plotly_chart(fig_nl, use_container_width=True, key=f"dash_nearlow_{selected_sheet}", config=DASH_CHART_CONFIG)
else:
st.info("52-Week Low column not detected for this sheet.")
with dash_n3:
if deliv_series.notna().any():
top_deliv_idx = deliv_series.dropna().sort_values(ascending=False).head(10).index
top_d = pd.DataFrame({
"Symbol": symbol_series.loc[top_deliv_idx].values,
"% Delivery": deliv_series.loc[top_deliv_idx].values
}).iloc[::-1]
fig_d = go.Figure(go.Bar(x=top_d["% Delivery"], y=top_d["Symbol"], orientation='h', marker_color="
fig_d.update_layout(title="🚚 Top 10 by Delivery %", template="plotly_white", height=340, margin=dict(t=40, b=10, l=10, r=10))
st.plotly_chart(fig_d, use_container_width=True, key=f"dash_topdeliv_{selected_sheet}", config=DASH_CHART_CONFIG)
else:
st.info("No Delivery % column detected for this sheet.")
dash_c7, dash_c8 = st.columns(2)
with dash_c7:
if cmp_series.notna().any() and high_series.notna().any() and low_series.notna().any():
span = (high_series - low_series).replace(0, np.nan)
pos_in_range = ((cmp_series - low_series) / span * 100).clip(0, 100)
valid_mask = pos_in_range.notna() & clean_symbol_series.notna()
syms_v = clean_symbol_series[valid_mask].str.strip().values
vals_v = pos_in_range[valid_mask].values
fig_range = go.Figure(go.Scatter(
x=syms_v, y=vals_v, mode="markers",
marker=dict(
size=9, color=vals_v,
colorscale=[[0, "
cmin=0, cmax=100,
showscale=True, colorbar=dict(title="% of Range")
),
customdata=syms_v,
hovertemplate="%{customdata}: %{y:.2f}%<extra></extra>",
))
fig_range.update_layout(
title="📍 Position within 52-Week Range (0% = Low, 100% = High)",
template="plotly_white", height=340, margin=dict(t=40, b=10, l=10, r=10),
xaxis=dict(showticklabels=False, title="Stocks"), yaxis_title="% of 52W Range"
)
_render_clickable_dot_scatter(fig_range, f"dash_range_{selected_sheet}")
else:
st.info("52-Week High/Low columns not detected for this sheet.")
with dash_c8:
if diff200_series.notna().any() and clean_symbol_series is not None:
valid_mask2 = diff200_series.notna() & clean_symbol_series.notna()
syms_v2 = clean_symbol_series[valid_mask2].str.strip().values
diff_vals = diff200_series[valid_mask2].values
d_absmax = max(abs(float(np.nanmin(diff_vals))), abs(float(np.nanmax(diff_vals))), 1e-9)
fig_diff200 = go.Figure(go.Scatter(
x=syms_v2, y=diff_vals, mode="markers",
marker=dict(
size=9, color=diff_vals,
colorscale=[[0, "
cmin=-d_absmax, cmax=d_absmax,
showscale=True, colorbar=dict(title="% Diff")
),
customdata=syms_v2,
hovertemplate="%{customdata}: %{y:.2f}%<extra></extra>",
))
fig_diff200.update_layout(
title="📐 Difference from 200 DMA (0% = at 200 DMA)",
template="plotly_white", height=340, margin=dict(t=40, b=10, l=10, r=10),
xaxis=dict(showticklabels=False, title="Stocks"), yaxis_title="% Diff from 200 DMA"
)
_render_clickable_dot_scatter(fig_diff200, f"dash_diff200_{selected_sheet}")
else:
st.info("Difference from 200 DMA column not detected for this sheet.")
dash_c9, _dash_c10_spacer = st.columns([1, 1.4])
with dash_c9:
signal_col = trend_target or buy_signal_target or breakout_signal_target
if signal_col and signal_col in dash_df.columns:
sig_counts = dash_df[signal_col].astype(str).str.strip()
sig_counts = sig_counts[(sig_counts != "") & (sig_counts.str.lower() != "nan")]
if not sig_counts.empty:
vc = sig_counts.value_counts().head(8)
fig_sig = go.Figure(go.Bar(x=vc.values, y=vc.index.astype(str), orientation='h', marker_color="
fig_sig.update_layout(title=f"📶 {signal_col} Breakdown", template="plotly_white", height=340, margin=dict(t=40, b=10, l=10, r=10))
st.plotly_chart(fig_sig, use_container_width=True, key=f"dash_signal_{selected_sheet}", config=DASH_CHART_CONFIG)
else:
st.info("No signal data available.")
else:
st.info("No Trend/Signal column detected for this sheet.")
st.markdown("---")
top_col1, top_col2, top_col3 = st.columns([3, 1, 2.2])
with top_col1:
sizing_mode = st.radio(
"📏 Column Width Adjustment:",
["Default", "✅ Fit to Row 1", "✅✅ Fit to Row 2"],
horizontal=True,
help="Automatically adjust the column widths based on the text length of the selected row."
)
with top_col3:
st.markdown("<div style='margin-top: 2px; font-size:0.9rem;'>🔍 Filter stocks inside this matrix...</div>", unsafe_allow_html=True)
matrix_search_query = st.text_input(
"Search symbol:", placeholder="Type symbol name...",
key="main_matrix_search", label_visibility="collapsed"
)
if matrix_search_query:
filtered_df = filtered_df[filtered_df['_raw_symbol_'].astype(str).str.contains(matrix_search_query, case=False, na=False)]
export_df = clean_for_export(filtered_df)
buffer = io.BytesIO()
with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
safe_sheet_name = selected_sheet[:31].replace(":", "").replace("/", "")
export_df.to_excel(writer, index=False, sheet_name=safe_sheet_name)
with top_col2:
st.markdown("<div style='margin-top: 28px;'></div>", unsafe_allow_html=True)
st.download_button(
label="📥 Download as Excel",
data=buffer.getvalue(),
file_name=f"{selected_sheet}_Export_{datetime.now().strftime('%Y%m%d')}.xlsx",
mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
use_container_width=False
)
bot_col1, bot_col2 = st.columns([1, 4])
with bot_col1:
st.write(f"**Rows:** {filtered_df.shape[0]} | **Columns:** {len(actual_cols)}")
with bot_col2:
url_placeholder = st.empty()
html_renderer = JsCode()
exact_mirror_style = JsCode()
gb = GridOptionsBuilder.from_dataframe(filtered_df)
gb.configure_selection(selection_mode="single", use_checkbox=True)
gb.configure_side_bar(filters_panel=False, columns_panel=True)
priority_columns_lower = ["nse code", "id", "company name", "stock name", "symbol", "industry", "sector"]
is_first_visible_column = True
for col in filtered_df.columns:
if col.startswith("_bg_") or col.startswith("_txt_") or col == "_raw_symbol_":
gb.configure_column(col, hide=True)
continue
if col in hidden_cols_for_sheet:
gb.configure_column(col, hide=True)
continue
if sizing_mode == "✅ Fit to Row 1" and len(filtered_df) > 0:
char_count = get_clean_text_length(filtered_df.iloc[0][col])
header_count = len(str(col))
base_calc = int(max(char_count, header_count) * 7 + 22)
if is_first_visible_column: base_calc += 30
width, min_width = (base_calc, 40)
elif sizing_mode == "✅✅ Fit to Row 2" and len(filtered_df) > 1:
char_count = get_clean_text_length(filtered_df.iloc[1][col])
header_count = len(str(col))
base_calc = int(max(char_count, header_count) * 7 + 22)
if is_first_visible_column: base_calc += 30
width, min_width = (base_calc, 40)
else:
width, min_width = (220, 150) if col.lower() in priority_columns_lower else (120, 80)
pinned_value = "left" if is_first_visible_column else None
if is_first_visible_column: is_first_visible_column = False
c_low = col.lower()
if col == selected_symbol_col or any(k in c_low for k in ["trading view", "history data", "screener", "zerodha", "chartlink", "market smith", "official nse", "nse"]):
gb.configure_column(col, width=width, minWidth=min_width, sortable=True, filter=True, resizable=True,
editable=False, pinned=pinned_value, cellRenderer=html_renderer, cellStyle=exact_mirror_style)
else:
gb.configure_column(col, width=width, minWidth=min_width, sortable=True, filter=True, resizable=True,
editable=False, pinned=pinned_value, cellStyle=exact_mirror_style)
gb.configure_grid_options(domLayout="normal", rowHeight=35, headerHeight=45, enableCellTextSelection=True, ensureDomOrder=True, alwaysShowHorizontalScroll=True)
grid_options = gb.build()
grid_response = AgGrid(
filtered_df, gridOptions=grid_options, theme="streamlit", update_mode=GridUpdateMode.SELECTION_CHANGED,
allow_unsafe_jscode=True, fit_columns_on_grid_load=False, enable_enterprise_modules=False, height=400, width='100%',
key=f"primary_stock_table_grid_{st.session_state.grid_reset_token}"
)
selected_rows = grid_response.get("selected_rows", [])
if (selected_rows is not None and len(selected_rows) > 0) or len(filtered_df) > 0:
if selected_rows is not None and len(selected_rows) > 0:
sel_row = selected_rows.iloc[0] if isinstance(selected_rows, pd.DataFrame) else selected_rows[0]
else:
sel_row = filtered_df.iloc[0]
sym = str(sel_row.get("_raw_symbol_", "")).strip()
if sym:
with url_placeholder.container():
st.markdown(
f"**⚡ {sym} Links:** "
f"[Trading View (🔗)](https://www.tradingview.com/symbols/{sym}/) &nbsp;|&nbsp; "
f"[History Data (🔗)](https://www.equitypandit.com/historical-data/{sym}) &nbsp;|&nbsp; "
f"[Screener (🔗)](https://www.screener.in/company/{sym}) &nbsp;|&nbsp; "
f"[Zerodha (🔗)](https://zerodha.com/markets/stocks/NSE/{sym}) &nbsp;|&nbsp; "
f"[Chartlink (🔗)](https://chartink.com/stocks-new?load-snapshot=exponential-moving-average-simple-moving-average-simple-moving-average-moving-average-convergence-divergence-chart-snapshot-175&symbol={sym}) &nbsp;|&nbsp; "
f"[Market Smith (🔗)](https://marketsmithindia.com/mstool/eval/{sym}/evaluation.jsp) &nbsp;|&nbsp; "
f"[NSE URL (🔗)](https://www.nseindia.com/get-quotes/equity?symbol={sym})"
)
st.markdown(f"---")
st.subheader(f"🛠️ Live Workspace Panel: {sym}")
box_height = st.slider("📏 Adjust Panel Box Height (px):", min_value=300, max_value=1000, value=500, step=50, key="panel_height_slider")
ws_tabs = st.tabs([
"🕯️ Price Chart (EMA + RSI)",
"📈 Chart & Trade Info (NSE Component)", "📋 History Data (EquityPandit)",
"🎯 Bullish/Bearish Zone", "📁 Screener Documents",
"🪁 Zerodha Portal", "📊 MarketSmith India", "📉 TradingView Symbol Profile",
"🤖 AI Stock Analysis", "💻 AI Pine Script Builder",
"🔬 Bottom Fishing Score",
"🎯 GTT Order Calculator", "📊 Watchlist Manager", "📰 News Feed"
])
with ws_tabs[1]:
_url0 = f"https://charting.nseindia.com/?symbol={sym}-EQ"
st.markdown(f"**NSE Interactive Chart Frame** &nbsp;|&nbsp; [🌐 Open in Browser]({_url0})", unsafe_allow_html=False)
st.caption("📱 If frame is blank on mobile, tap the link above to open directly.")
components.html(f'<iframe src="{_url0}" width="100%" height="{box_height}" style="border:none; border-radius:5px;"></iframe>', height=box_height+20)
with ws_tabs[2]:
_url1 = f"https://www.equitypandit.com/historical-data/{sym.lower()}"
st.markdown(f"**EquityPandit Historical Matrix Data** &nbsp;|&nbsp; [🌐 Open in Browser]({_url1})")
st.caption("📱 If frame is blank on mobile, tap the link above to open directly.")
components.html(f'<iframe src="{_url1}" width="100%" height="{box_height}" style="border:none; border-radius:5px; background-color:white;"></iframe>', height=box_height+20)
with ws_tabs[3]:
_url2 = f"https://www.equitypandit.com/share-price/{sym.lower()}
st.markdown(f"**Bullish / Bearish Zone Indicator** &nbsp;|&nbsp; [🌐 Open in Browser]({_url2})")
st.caption("📱 If frame is blank on mobile, tap the link above to open directly.")
components.html(f'<iframe src="{_url2}" width="100%" height="{box_height}" style="border:none; border-radius:5px; background-color:white;"></iframe>', height=box_height+20)
with ws_tabs[4]:
_url3 = f"https://www.screener.in/company/{sym}/consolidated/"
st.markdown(f"**Screener Corporate Filings** &nbsp;|&nbsp; [🌐 Open in Browser]({_url3})")
st.caption("📱 If frame is blank on mobile, tap the link above to open directly.")
components.html(f'<iframe src="{_url3}" width="100%" height="{box_height}" style="border:none; border-radius:5px; background-color:white;"></iframe>', height=box_height+20)
with ws_tabs[5]:
_url4 = f"https://zerodha.com/markets/stocks/NSE/{sym}/"
st.markdown(f"**Zerodha Markets Financial Performance Metrics** &nbsp;|&nbsp; [🌐 Open in Browser]({_url4})")
st.caption("📱 If frame is blank on mobile, tap the link above to open directly.")
components.html(f'<iframe src="{_url4}" width="100%" height="{box_height}" style="border:none; border-radius:5px; background-color:white;"></iframe>', height=box_height+20)
with ws_tabs[6]:
_url5 = f"https://marketsmithindia.com/mstool/eval/{sym.lower()}/evaluation.jsp"
st.markdown(f"**MarketSmith India Institutional Trading Evaluation Engine** &nbsp;|&nbsp; [🌐 Open in Browser]({_url5})")
st.caption("📱 If frame is blank on mobile, tap the link above to open directly.")
components.html(f'<iframe src="{_url5}" width="100%" height="{box_height}" style="border:none; border-radius:5px; background-color:white;"></iframe>', height=box_height+20)
with ws_tabs[7]:
_url6 = f"https://www.tradingview.com/symbols/{sym}/"
st.markdown(f"**TradingView Comprehensive Asset Market Registry Summary Profile** &nbsp;|&nbsp; [🌐 Open in Browser]({_url6})")
st.caption("📱 If frame is blank on mobile, tap the link above to open directly.")
components.html(f'<iframe src="{_url6}" width="100%" height="{box_height}" style="border:none; border-radius:5px; background-color:white;"></iframe>', height=box_height+20)
with ws_tabs[8]:
st.markdown(f"
if not ai_enabled:
st.warning("⚠️ No AI configured. Add `GEMINI_API_KEY` or `GROQ_API_KEY` to Streamlit secrets.")
else:
chosen_model = ai_model_selector("analysis")
st.caption(
"⚡ Groq = llama-3.3-70b (free, fast) &nbsp;|&nbsp; 🧠 Gemini = gemini-2.5-flash"
if groq_enabled and gemini_enabled
else ("⚡ Groq connected" if groq_enabled else "🧠 Gemini connected")
)
st.write("Using the live data pulled from your dashboard, the AI can analyze technicals, ranges, and context.")
ai_query = st.text_area(
"Your Query:",
value=f"Based on the current data provided, give me a quick summary of the technical performance and trend for {sym}.",
height=80,
key="ai_query_analysis"
)
if st.button("✨ Generate AI Analysis", use_container_width=True, key="btn_ai_analysis"):
with st.spinner(f"Analyzing {sym} with {chosen_model}..."):
try:
clean_row_context = {k: v for k, v in sel_row.items() if not str(k).startswith('_')}
prompt = f
ai_result = call_ai(prompt, chosen_model)
st.session_state["last_ai_result"] = {"sym": sym, "model": chosen_model, "query": ai_query, "result": ai_result}
st.session_state.ai_history.append([
sym, chosen_model, ai_query, ai_result,
datetime.now().strftime("%Y-%m-%d %H:%M:%S")
])
st.info(ai_result)
except Exception as e:
st.error(f"AI error: {e}")
if st.session_state.get("last_ai_result", {}).get("sym") == sym:
_last = st.session_state["last_ai_result"]
_res_text = _last["result"]
st.markdown("---")
_ec1, _ec2, _ec3 = st.columns(3)
with _ec1:
_single_xl = ai_results_to_excel([[
sym, _last["model"], _last["query"], _res_text,
datetime.now().strftime("%Y-%m-%d %H:%M:%S")
]])
st.download_button(
"📥 Save as Excel",
data=_single_xl,
file_name=f"AI_{sym}_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx",
mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
use_container_width=True,
key="dl_ai_excel_analysis"
)
with _ec2:
_wa_text = urllib.parse.quote(
f"📊 *{sym} AI Analysis* ({_last['model']})\n\n{_res_text[:800]}"
+ ("\n\n_(truncated)_" if len(_res_text) > 800 else "")
)
st.markdown(
f"<a href='https://wa.me/?text={_wa_text}' target='_blank'>"
f"<button style='width:100%;padding:8px;background:
f"border:none;border-radius:6px;cursor:pointer;font-size:14px;font-weight:bold;'>"
f"📱 Share on WhatsApp</button></a>",
unsafe_allow_html=True
)
with _ec3:
_tg_text = urllib.parse.quote(
f"📊 {sym} AI Analysis ({_last['model']})\n\n{_res_text[:800]}"
)
st.markdown(
f"<a href='https://t.me/share/url?url=NSEDashboard&text={_tg_text}' target='_blank'>"
f"<button style='width:100%;padding:8px;background:
f"border:none;border-radius:6px;cursor:pointer;font-size:14px;font-weight:bold;'>"
f"✈️ Share on Telegram</button></a>",
unsafe_allow_html=True
)
st.markdown("---")
st.markdown("**💡 Suggested Prompts** — copy any prompt below and paste it into the query box above:")
prompt_lines = "\n".join(
[f"{i+1}. {p.replace('{sym}', sym)}" for i, p in enumerate(SUGGESTED_AI_PROMPTS)]
)
st.text(prompt_lines)
with ws_tabs[9]:
st.markdown(f"
if not ai_enabled:
st.warning("⚠️ No AI configured. Add `GEMINI_API_KEY` or `GROQ_API_KEY` to Streamlit secrets.")
else:
chosen_model_pine = ai_model_selector("pine")
st.write("Generate a custom TradingView Pine Script v5 strategy tailored to this stock's current metrics.")
strategy_focus = st.selectbox("Select Strategy Focus:", [
"Volume Breakout with Dynamic Stop Loss",
"Moving Average Crossover (50/100/200 DMA)",
"Trend Following with Trailing Stop",
"Mean Reversion from 52W High/Low"
], key="pine_strategy_focus")
pine_query = st.text_area("Additional Custom Rules (Optional):", value=f"Include risk management parameters and plot signals on the chart.", height=60, key="pine_query")
if st.button("⚙️ Generate TradingView Pine Script", use_container_width=True, key="btn_pine"):
with st.spinner(f"Writing Pine Script v5 code for {sym}..."):
try:
clean_row_context = {k: v for k, v in sel_row.items() if not str(k).startswith('_')}
prompt = f
pine_result = call_ai(prompt, chosen_model_pine)
st.session_state["last_pine_result"] = {"sym": sym, "result": pine_result}
st.markdown("
st.write("Copy the code below and paste it into the TradingView Pine Editor.")
st.markdown(pine_result)
except Exception as e:
st.error(f"AI error: {e}")
if st.session_state.get("last_pine_result", {}).get("sym") == sym:
_pine_res = st.session_state["last_pine_result"]["result"]
_pine_xl = ai_results_to_excel([[
sym, "Pine Script", strategy_focus, _pine_res,
datetime.now().strftime("%Y-%m-%d %H:%M:%S")
]])
st.download_button(
"📥 Save Pine Script as Excel",
data=_pine_xl,
file_name=f"PineScript_{sym}_{datetime.now().strftime('%Y%m%d')}.xlsx",
mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
key="dl_pine_excel"
)
st.markdown("---")
st.markdown("**📋 Custom Rules Reference** — copy any rule and paste it into the Additional Custom Rules box above:")
st.text(PINE_CUSTOM_RULES)
with ws_tabs[10]:
st.markdown(f"
st.caption("Scores this stock on 8 key criteria for buying from the bottom. Based entirely on your live sheet data.")
clean_sel = {k: v for k, v in sel_row.items() if not str(k).startswith('_')}
bf_score, bf_grade, bf_reasons = compute_bottom_fishing_score(clean_sel, actual_cols)
score_color = "
st.markdown(f, unsafe_allow_html=True)
st.markdown("
for reason in bf_reasons:
st.markdown(f"- {reason}")
st.markdown("---")
st.markdown("
criteria_md =
st.markdown(criteria_md)
st.info("💡 **Buy Strategy:** Look for scores ≥ 55 (Watchlist) or ≥ 75 (Strong Buy). "
"The sweet zone is CMP at 8–15% above 52W Low with uptrend confirmed (CMP > 200 DMA), "
"backed by positive profits, low debt, and high promoter holding. "
"This combination maximizes probability of a bull run from the bottom.")
if ai_enabled:
st.markdown("---")
chosen_model_bf = ai_model_selector("bf")
if st.button("🤖 Get AI Deep Analysis for Bottom Buy", use_container_width=True, key="bf_ai_btn"):
with st.spinner(f"Running deep bottom-fishing analysis for {sym} with {chosen_model_bf}..."):
try:
prompt = f
bf_ai_result = call_ai(prompt, chosen_model_bf)
st.session_state["last_bf_ai_result"] = {"sym": sym, "result": bf_ai_result}
st.session_state.ai_history.append([
sym, chosen_model_bf, "Bottom Fishing Deep Analysis", bf_ai_result,
datetime.now().strftime("%Y-%m-%d %H:%M:%S")
])
st.success("✅ AI Analysis Complete")
st.markdown(bf_ai_result)
except Exception as e:
st.error(f"AI error: {e}")
st.markdown("---")
st.markdown("
_bf_card_text = (
f"🔬 *Bottom Fishing Score: {sym}*\n\n"
f"📊 Score: *{bf_score}/100*\n"
f"📈 Grade: {bf_grade}\n\n"
+ "\n".join(bf_reasons[:5])
+ f"\n\n🕒 {datetime.now().strftime('%d %b %Y %H:%M')}\n📌 NSE Stock Dashboard"
)
_bf_wa  = urllib.parse.quote(_bf_card_text)
_bf_tg  = urllib.parse.quote(_bf_card_text)
_sh1, _sh2 = st.columns(2)
with _sh1:
st.markdown(
f"<a href='https://wa.me/?text={_bf_wa}' target='_blank'>"
f"<button style='width:100%;padding:8px;background:
f"border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>"
f"📱 Share on WhatsApp</button></a>",
unsafe_allow_html=True
)
with _sh2:
st.markdown(
f"<a href='https://t.me/share/url?url=Dashboard&text={_bf_tg}' target='_blank'>"
f"<button style='width:100%;padding:8px;background:
f"border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>"
f"✈️ Share on Telegram</button></a>",
unsafe_allow_html=True
)
with ws_tabs[11]:
st.markdown(f"
st.caption("Auto-suggest Stop-Loss, Targets & ATR-based GTT levels from your live sheet data.")
clean_sel_gtt = {k: v for k, v in sel_row.items() if not str(k).startswith('_')}
gtt = compute_gtt(clean_sel_gtt, actual_cols)
if not gtt.get("cmp"):
st.warning("⚠️ CMP column not found in sheet data. Cannot compute GTT levels.")
else:
cmp_v = gtt["cmp"]
gc1, gc2, gc3, gc4 = st.columns(4)
gc1.metric("📍 CMP", f"₹{cmp_v:,.2f}")
if gtt.get("52w_high"): gc2.metric("⬆️ 52W High", f"₹{gtt['52w_high']:,.2f}")
if gtt.get("52w_low"):  gc3.metric("⬇️ 52W Low",  f"₹{gtt['52w_low']:,.2f}")
if gtt.get("atr_approx"): gc4.metric("📊 ATR (approx)", f"₹{gtt['atr_approx']:,.2f}")
st.markdown("---")
st.markdown("
col_atr1, col_atr2 = st.columns(2)
manual_atr = col_atr1.number_input(
"Manual ATR Override (₹) — leave 0 to use auto",
min_value=0.0, value=0.0, step=0.5, key="gtt_manual_atr"
)
rr_ratio = col_atr2.selectbox(
"Risk-Reward Ratio:", ["1:1", "1:1.5", "1:2", "1:2.5", "1:3"],
index=2, key="gtt_rr_ratio"
)
rr_val = float(rr_ratio.split(":")[1])
effective_atr = manual_atr if manual_atr > 0 else gtt.get("atr_approx", 0)
if effective_atr and effective_atr > 0:
sl_tight    = round(cmp_v - 1.0 * effective_atr, 2)
sl_standard = round(cmp_v - 1.5 * effective_atr, 2)
sl_wide     = round(cmp_v - 2.0 * effective_atr, 2)
sl_gap      = cmp_v - sl_standard
t1 = round(cmp_v + sl_gap * 1.0,   2)
t2 = round(cmp_v + sl_gap * rr_val, 2)
t3 = round(cmp_v + sl_gap * 3.0,   2)
risk_pct = round((sl_gap / cmp_v) * 100, 2)
st.markdown("
sl_df = pd.DataFrame([
{"Type": "Tight SL (1× ATR)",    "Price (₹)": sl_tight,    "% Risk": round((cmp_v-sl_tight)/cmp_v*100,2),    "Use Case": "Intraday / Scalp"},
{"Type": "Standard SL (1.5× ATR)","Price (₹)": sl_standard,"% Risk": round((cmp_v-sl_standard)/cmp_v*100,2),"Use Case": "Swing / BTST"},
{"Type": "Wide SL (2× ATR)",     "Price (₹)": sl_wide,     "% Risk": round((cmp_v-sl_wide)/cmp_v*100,2),     "Use Case": "Positional"},
])
if gtt.get("trail_sl_50dma"):
sl_df = pd.concat([sl_df, pd.DataFrame([{
"Type": "Trail SL @ 50 DMA", "Price (₹)": gtt["trail_sl_50dma"],
"% Risk": round((cmp_v-gtt["trail_sl_50dma"])/cmp_v*100,2) if gtt["trail_sl_50dma"] < cmp_v else 0,
"Use Case": "Trailing Stop"
}])], ignore_index=True)
st.dataframe(sl_df, use_container_width=True, hide_index=True)
st.markdown(f"
tgt_df = pd.DataFrame([
{"Target": "T1 (1R)",            "Price (₹)": t1, "% Gain": round((t1-cmp_v)/cmp_v*100,2), "Strategy": "Book 30–40%"},
{"Target": f"T2 ({rr_ratio} R:R)","Price (₹)": t2, "% Gain": round((t2-cmp_v)/cmp_v*100,2), "Strategy": "Book 40–50%"},
{"Target": "T3 (3R — runner)",   "Price (₹)": t3, "% Gain": round((t3-cmp_v)/cmp_v*100,2), "Strategy": "Hold remainder"},
])
st.dataframe(tgt_df, use_container_width=True, hide_index=True)
st.markdown("
ps_col1, ps_col2 = st.columns(2)
capital = ps_col1.number_input("Capital (₹):", min_value=1000, value=100000, step=5000, key="gtt_capital")
risk_pct_inp = ps_col2.number_input("Max Risk % of Capital:", min_value=0.5, max_value=10.0, value=2.0, step=0.5, key="gtt_risk_pct")
max_loss_rs = capital * risk_pct_inp / 100
qty = int(max_loss_rs / (cmp_v - sl_standard)) if (cmp_v - sl_standard) > 0 else 0
invest_val = qty * cmp_v
st.success(
f"📦 Suggested Qty: **{qty} shares** &nbsp;|&nbsp; "
f"Investment: **₹{invest_val:,.0f}** &nbsp;|&nbsp; "
f"Max Loss: **₹{max_loss_rs:,.0f}** ({risk_pct_inp}%)"
)
st.markdown("---")
st.markdown("
gtt_summary = (
f"🎯 *GTT Order: {sym}*\n\n"
f"📍 Entry CMP: ₹{cmp_v:,.2f}\n"
f"🛡️ Stop-Loss: ₹{sl_standard:,.2f} ({risk_pct:.1f}% risk)\n"
f"🎯 Target 1:  ₹{t1:,.2f} (+{round((t1-cmp_v)/cmp_v*100,1)}%)\n"
f"🎯 Target 2:  ₹{t2:,.2f} (+{round((t2-cmp_v)/cmp_v*100,1)}%)\n"
f"🎯 Target 3:  ₹{t3:,.2f} (+{round((t3-cmp_v)/cmp_v*100,1)}%)\n"
f"📦 Qty: {qty} shares | ₹{invest_val:,.0f}\n"
f"📊 ATR: ₹{effective_atr:.2f} | R:R {rr_ratio}\n"
f"🕒 {datetime.now().strftime('%d %b %Y %H:%M')}"
)
st.code(gtt_summary, language="")
_gtt_wa = urllib.parse.quote(gtt_summary)
_gtt_tg = urllib.parse.quote(gtt_summary)
_gc1, _gc2 = st.columns(2)
with _gc1:
st.markdown(
f"<a href='https://wa.me/?text={_gtt_wa}' target='_blank'>"
f"<button style='width:100%;padding:8px;background:
f"border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>"
f"📱 Share GTT on WhatsApp</button></a>",
unsafe_allow_html=True
)
with _gc2:
st.markdown(
f"<a href='https://t.me/share/url?url=Dashboard&text={_gtt_tg}' target='_blank'>"
f"<button style='width:100%;padding:8px;background:
f"border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>"
f"✈️ Share GTT on Telegram</button></a>",
unsafe_allow_html=True
)
else:
st.warning("⚠️ Could not compute ATR — 52W High/Low columns not found in sheet. Please enter ATR manually above.")
with ws_tabs[12]:
st.markdown(f"
clean_sel_wl = {k: v for k, v in sel_row.items() if not str(k).startswith('_')}
bf_score_wl, bf_grade_wl, _ = compute_bottom_fishing_score(clean_sel_wl, actual_cols)
cmp_wl = str(clean_sel_wl.get(cmp_target, "")) if cmp_target else ""
already_in = sym in st.session_state.watchlist
st.markdown(f"**Current Stock: {sym}** {'✅ Already in Watchlist' if already_in else ''}")
wl_note = st.text_input(
"📝 Note (optional):",
value=st.session_state.watchlist.get(sym, {}).get("note", ""),
placeholder="e.g. Near 52W low, watching for breakout",
key=f"wl_note_{sym}"
)
wl_col1, wl_col2 = st.columns(2)
with wl_col1:
if st.button(
f"{'🔄 Update' if already_in else '➕ Add'} {sym} to Watchlist",
use_container_width=True, key="wl_add_btn"
):
watchlist_add(sym, cmp=cmp_wl, note=wl_note,
bf_score=str(bf_score_wl), bf_grade=bf_grade_wl)
saved = save_watchlist_to_sheet()
if saved:
st.success(f"✅ {sym} saved to Watchlist (Google Sheet updated!)")
else:
st.info(f"✅ {sym} added to session Watchlist (Sheet write failed — check secrets).")
st.rerun()
with wl_col2:
if already_in:
if st.button(f"❌ Remove {sym} from Watchlist", use_container_width=True, key="wl_rm_btn"):
watchlist_remove(sym)
save_watchlist_to_sheet()
st.rerun()
st.markdown("---")
st.markdown("
if st.session_state.watchlist:
wl_data = [
{
"Symbol":   s,
"CMP (₹)":  d["cmp"],
"BF Score": d.get("bf_score",""),
"Grade":    d.get("bf_grade",""),
"Note":     d.get("note",""),
"Added":    d.get("added",""),
}
for s, d in st.session_state.watchlist.items()
]
wl_df = pd.DataFrame(wl_data)
st.dataframe(wl_df, use_container_width=True, hide_index=True)
_wl2_buf = io.BytesIO()
with pd.ExcelWriter(_wl2_buf, engine="openpyxl") as _w2:
wl_df.to_excel(_w2, index=False, sheet_name="Watchlist")
st.download_button(
"📥 Download Watchlist as Excel",
data=_wl2_buf.getvalue(),
file_name=f"Watchlist_{datetime.now().strftime('%Y%m%d')}.xlsx",
mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
use_container_width=True,
key="dl_wl_excel_tab"
)
_wl_share_lines = "\n".join(
[f"• {s} — Score:{d.get('bf_score','')} {d.get('bf_grade','').split()[0] if d.get('bf_grade') else ''} — {d.get('note','')[:30]}"
for s, d in list(st.session_state.watchlist.items())[:15]]
)
_wl_share_text = f"📊 *My NSE Watchlist*\n\n{_wl_share_lines}\n\n🕒 {datetime.now().strftime('%d %b %Y')}"
_wl_wa = urllib.parse.quote(_wl_share_text)
_wl_tg = urllib.parse.quote(_wl_share_text)
st.markdown("")
_ws1, _ws2 = st.columns(2)
with _ws1:
st.markdown(
f"<a href='https://wa.me/?text={_wl_wa}' target='_blank'>"
f"<button style='width:100%;padding:8px;background:
f"border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>"
f"📱 Share Watchlist on WhatsApp</button></a>",
unsafe_allow_html=True
)
with _ws2:
st.markdown(
f"<a href='https://t.me/share/url?url=Dashboard&text={_wl_tg}' target='_blank'>"
f"<button style='width:100%;padding:8px;background:
f"border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>"
f"✈️ Share Watchlist on Telegram</button></a>",
unsafe_allow_html=True
)
else:
st.info("Your watchlist is empty. Add stocks using the button above!")
with ws_tabs[13]:
st.markdown(f"
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import datetime
import email.utils
def get_time_ago_tab(pubdate_str):
try:
dt = email.utils.parsedate_to_datetime(pubdate_str)
now = datetime.datetime.now(datetime.timezone.utc)
diff = now - dt
seconds = diff.total_seconds()
if seconds < 0: return "Just now"
if seconds < 60: return f"{int(seconds)} secs ago"
if seconds < 3600:
mins = int(seconds / 60)
return f"{mins} min{'s' if mins != 1 else ''} ago"
if seconds < 86400:
hours = int(seconds / 3600)
return f"{hours} hour{'s' if hours != 1 else ''} ago"
if seconds < 172800: return "Yesterday"
days = int(seconds / 86400)
return f"{days} days ago"
except Exception:
return "Recent"
@st.cache_data(ttl=600)
def fetch_single_stock_news(target_symbol, limit=10):
try:
query = urllib.parse.quote(f'"{target_symbol}" stock share news NSE India')
url = f"https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
xml_data = response.read()
root = ET.fromstring(xml_data)
alert_keywords = ["52 week high", "52-week high", "52 week low", "52-week low", "upper circuit", "lower circuit", "hits circuit", "locked in circuit"]
n_list = []
for item in root.findall('.//item'):
title = item.find('title').text
link = item.find('link').text
pub_date = item.find('pubDate').text if item.find('pubDate') is not None else ""
is_alert = any(k in title.lower() for k in alert_keywords)
icon = "🚨 **[ALERT]** " if is_alert else ""
try:
dt = email.utils.parsedate_to_datetime(pub_date)
except Exception:
dt = datetime.datetime.min.replace(tzinfo=datetime.timezone.utc)
n_list.append({
"display_title": f"{icon}{title}",
"link": link,
"time_ago": get_time_ago_tab(pub_date),
"timestamp": dt
})
n_list.sort(key=lambda x: x["timestamp"], reverse=True)
return n_list[:limit]
except Exception:
return []
with st.spinner(f"Fetching today's latest news for {sym}..."):
stock_news = fetch_single_stock_news(sym, limit=10)
if stock_news:
for news in stock_news:
is_today = "min" in news['time_ago'] or "hour" in news['time_ago'] or "sec" in news['time_ago'] or "Just now" in news['time_ago']
time_color = "
time_weight = "bold" if is_today else "normal"
st.markdown(f"- <a href='{news['link']}' target='_blank' style='text-decoration: none; color: inherit;'>{news['display_title']}</a> <span style='color: {time_color}; font-weight: {time_weight}; font-size: 0.85em;'>— 🕒 {news['time_ago']}</span>", unsafe_allow_html=True)
st.markdown("<hr style='margin: 0.5em 0; opacity: 0.2;'>", unsafe_allow_html=True)
else:
st.info(f"No recent news found for {sym}.")
with ws_tabs[0]:
st.markdown(f"
hist_period = st.select_slider(
"History range:", options=["3mo", "6mo", "1y", "2y", "5y"],
value="1y", key=f"chart_period_{sym}"
)
with st.spinner(f"Loading price history for {sym}..."):
chart_df = fetch_stock_ohlc_history(sym, period=hist_period)
if chart_df.empty or "Close" not in chart_df.columns:
st.warning(f"⚠️ No historical price data available for **{sym}** via Yahoo Finance "
f"(tried `{sym}.NS`). The symbol may be delisted, renamed, or not tracked by Yahoo.")
else:
close_s = chart_df["Close"].squeeze().dropna()
last_close = float(close_s.iloc[-1])
prev_close = float(close_s.iloc[-2]) if len(close_s) > 1 else last_close
day_chg = ((last_close - prev_close) / prev_close * 100) if prev_close else 0.0
_delta14 = close_s.diff()
_gain14 = _delta14.clip(lower=0).rolling(14).mean()
_loss14 = (-_delta14.clip(upper=0)).rolling(14).mean()
_rsi14_s = 100 - (100 / (1 + _gain14 / _loss14.replace(0, float("nan"))))
last_rsi14 = _rsi14_s.dropna().iloc[-1] if not _rsi14_s.dropna().empty else None
price_tab, rsi_tab = st.tabs(["Price + EMAs", "RSI"])
with price_tab:
chart_type = st.radio(
"Chart type", ["Candle", "Line"], horizontal=True, key=f"chart_type_{sym}"
)
delta9 = close_s.diff()
gain9  = delta9.clip(lower=0).rolling(9).mean()
loss9  = (-delta9.clip(upper=0)).rolling(9).mean()
rsi9   = 100 - (100 / (1 + gain9 / loss9.replace(0, float("nan"))))
ema3   = rsi9.ewm(span=3, adjust=False).mean()
_w21   = np.arange(1, 22, dtype=float)
wma21  = rsi9.rolling(21).apply(
lambda x: float(np.dot(x, _w21) / _w21.sum()), raw=True
)
idx = list(chart_df.index)
rsi9_arr = rsi9.values
nk_sig_x, nk_sig_y_price = [], []
nk_sig_x2, nk_sig_y_rsi = [], []
for i in range(22, len(rsi9)):
r, r_prev = rsi9_arr[i], rsi9_arr[i - 1]
if np.isnan(r) or np.isnan(r_prev):
continue
if r >= 50 and r_prev < 50:
d = rsi9.index[i]
if d in close_s.index:
nk_sig_x.append(d); nk_sig_y_price.append(float(close_s.loc[d]) * 0.993)
nk_sig_x2.append(d); nk_sig_y_rsi.append(float(r))
if not ema3.dropna().empty and not wma21.dropna().empty:
last_e = ema3.dropna().iloc[-1]; last_w = wma21.dropna().iloc[-1]
sig_color = "
sig_text  = "🟢 H-M: POSITIVE (Bullish)" if last_e > last_w else "🔴 H-M: NEGATIVE (Bearish)"
st.markdown(
f"<div style='background:{sig_color}22;border-left:4px solid {sig_color};"
f"padding:6px 12px;border-radius:4px;margin-bottom:6px;font-size:13px;"
f"font-weight:700;color:{sig_color}'>{sig_text} — EMA3: {last_e:.1f} | WMA21: {last_w:.1f}</div>",
unsafe_allow_html=True,
)
fig = make_subplots(
rows=3, cols=1, shared_xaxes=True,
row_heights=[0.55, 0.25, 0.20], vertical_spacing=0.03,
specs=[[{"type": "xy"}], [{"type": "xy"}], [{"type": "xy"}]],
)
if chart_type == "Candle":
try:
fig.add_trace(go.Candlestick(
x=idx,
open=chart_df["Open"].squeeze(), high=chart_df["High"].squeeze(),
low=chart_df["Low"].squeeze(), close=chart_df["Close"].squeeze(),
name="OHLC",
increasing_line_color="
increasing_fillcolor="
line=dict(width=1.6),
whiskerwidth=0.9,
), row=1, col=1)
except Exception:
fig.add_trace(go.Scatter(x=idx, y=close_s, name="Close",
line=dict(color="
else:
fig.add_trace(go.Scatter(x=idx, y=close_s, name="Close",
line=dict(color="
for period_n, color, lbl in [(20, "
ema_line = close_s.ewm(span=period_n, adjust=False).mean()
fig.add_trace(go.Scatter(x=idx, y=ema_line, name=lbl,
line=dict(color=color, width=1.8)), row=1, col=1)
wk52_high = float(chart_df["High"].max())
wk52_low  = float(chart_df["Low"].min())
fig.add_hline(
y=wk52_high, line_dash="dash", line_color="
opacity=0.85, row=1, col=1,
annotation_text=f"52W High ₹{wk52_high:,.2f}", annotation_position="top right",
annotation_font=dict(color="
)
fig.add_hline(
y=wk52_low, line_dash="dash", line_color="
opacity=0.85, row=1, col=1,
annotation_text=f"52W Low ₹{wk52_low:,.2f}", annotation_position="bottom right",
annotation_font=dict(color="
)
if nk_sig_x:
fig.add_trace(go.Scatter(
x=nk_sig_x, y=nk_sig_y_price, mode="markers",
name="H-M Entry (RSI>50)",
marker=dict(color="lime", size=12, symbol="circle",
line=dict(color="white", width=1.5)),
), row=1, col=1)
try:
vol_s = chart_df["Volume"].squeeze()
open_s_v = chart_df["Open"].squeeze()
close_s_v = chart_df["Close"].squeeze()
vol_colors = [
"
for o, c in zip(open_s_v.tolist(), close_s_v.tolist())
]
fig.add_trace(go.Bar(
x=idx, y=vol_s.tolist(), name="Volume",
marker=dict(color=vol_colors, line=dict(width=0)),
opacity=0.85, showlegend=False,
), row=3, col=1)
vol_avg20 = vol_s.rolling(20).mean()
fig.add_trace(go.Scatter(
x=idx, y=vol_avg20.tolist(), name="Vol Avg(20)",
line=dict(color="
), row=3, col=1)
except Exception:
pass
_rsi_s = rsi9.reindex(rsi9.index)
_mid   = pd.Series(50.0, index=rsi9.index)
_above = _rsi_s.where(_rsi_s >= 50, 50.0)
fig.add_trace(go.Scatter(x=idx, y=_mid.tolist(), line=dict(width=0), mode="lines",
showlegend=False, hoverinfo="skip"), row=2, col=1)
fig.add_trace(go.Scatter(x=idx, y=_above.tolist(), fill="tonexty",
fillcolor="rgba(38,166,154,0.35)", line=dict(width=0), mode="lines",
showlegend=False, hoverinfo="skip"), row=2, col=1)
_below = _rsi_s.where(_rsi_s <= 50, 50.0)
fig.add_trace(go.Scatter(x=idx, y=_mid.tolist(), line=dict(width=0), mode="lines",
showlegend=False, hoverinfo="skip"), row=2, col=1)
fig.add_trace(go.Scatter(x=idx, y=_below.tolist(), fill="tonexty",
fillcolor="rgba(239,83,80,0.35)", line=dict(width=0), mode="lines",
showlegend=False, hoverinfo="skip"), row=2, col=1)
fig.add_trace(go.Scatter(x=idx, y=rsi9.tolist(), name="RSI(9)",
line=dict(color="
fig.add_trace(go.Scatter(x=idx, y=ema3.tolist(), name="EMA3",
line=dict(color="
fig.add_trace(go.Scatter(x=idx, y=wma21.tolist(), name="WMA21",
line=dict(color="
if nk_sig_x2:
fig.add_trace(go.Scatter(
x=nk_sig_x2, y=nk_sig_y_rsi, mode="markers",
name="Entry (RSI panel)", showlegend=False,
marker=dict(color="lime", size=6, symbol="circle",
line=dict(color="white", width=1)),
), row=2, col=1)
fig.add_hline(y=70, line_dash="dot", line_color="
fig.add_hline(y=50, line_dash="dash", line_color="
annotation_text="50", annotation_position="right")
fig.add_hline(y=30, line_dash="dot", line_color="
annotation_text="30", annotation_position="right")
fig.update_layout(
template="plotly_white",
height=950,
title=dict(
text=f"{sym} — Ultra HD Chart (Price, EMAs, H-M, Volume)",
font=dict(size=12, color="
),
margin=dict(t=60, b=80, l=20, r=20),
xaxis_rangeslider_visible=False, xaxis2_rangeslider_visible=False,
xaxis3_rangeslider_visible=False,
legend=dict(
orientation="h",
y=-0.15, x=0.5, xanchor="center", yanchor="top",
font=dict(size=13, color="
),
hovermode="x unified",
font=dict(size=13, color="
hoverlabel=dict(
font_size=14,
font_family="system-ui, -apple-system, sans-serif",
bgcolor="rgba(255,255,255,0.95)"
),
plot_bgcolor="
)
fig.update_xaxes(
showspikes=True, spikemode="across+toaxis",
spikesnap="cursor", spikethickness=1.5,
spikedash="solid", spikecolor="
gridcolor="rgba(0,0,0,0.06)", linecolor="rgba(0,0,0,0.3)",
tickfont=dict(size=12, family="system-ui, sans-serif")
)
fig.update_yaxes(
gridcolor="rgba(0,0,0,0.06)", zeroline=False,
linecolor="rgba(0,0,0,0.3)",
tickfont=dict(size=12, family="system-ui, sans-serif")
)
fig.update_yaxes(range=[0, 100], row=2, col=1)
fig.update_yaxes(title_text="Price (₹)", title_font=dict(size=14, weight="bold"), row=1, col=1)
fig.update_yaxes(title_text="RSI / H-M", title_font=dict(size=14, weight="bold"), row=2, col=1)
fig.update_yaxes(title_text="Volume", title_font=dict(size=14, weight="bold"), row=3, col=1)
hd_config = {
"displaylogo": False,
"responsive": True,
"toImageButtonOptions": {
"format": "png",
"filename": f"{sym}_Ultra_HD_Analysis",
"height": 1080,
"width": 1920,
"scale": 6,
},
"modeBarButtonsToAdd": [
"drawline", "drawopenpath", "drawrect", "eraseshape"
]
}
st.plotly_chart(fig, use_container_width=True, key=f"price_ema_chart_{sym}", config=hd_config)
if nk_sig_x:
st.caption(
f"🟢 {len(nk_sig_x)} H-M entry signal(s) — RSI(9) crossed above 50 (bottom-catch). "
"**H-M panel:** Green fill = RSI above 50 (momentum). Red fill = RSI below 50 (pullback). "
"For informational purposes only."
)
else:
st.caption(
"**H-M panel:** Green fill = RSI above 50. Red fill = RSI below 50 (pullback zone). "
"🟢 circles = RSI(9) cross above 50 (entry). For informational purposes only."
)
fund_primary_row = {}
if selected_sheet != "NSE Fundamentals":
fund_df = load_sheet_data_with_colors("NSE Fundamentals")
if not fund_df.empty:
fund_cols = [c for c in fund_df.columns if not c.startswith("_bg_") and not c.startswith("_txt_")]
sym_col_fund = next((c for c in fund_cols if c.lower() in ["nse code", "symbol", "ticker", "stock symbol", "id", "stock"]), None)
if sym_col_fund:
fund_match = fund_df[fund_df[sym_col_fund].astype(str).str.strip() == sym]
if not fund_match.empty:
_raw_fund_row = fund_match.iloc[0].to_dict()
fund_primary_row = {
k: v for k, v in _raw_fund_row.items()
if not str(k).startswith("_bg_") and not str(k).startswith("_txt_") and str(k) != "_raw_symbol_"
}
def _sheet_val(row, primary_dict, *keys):
def _search_row(r_data):
if r_data is None or len(r_data) == 0: return "-"
try:
r_idx = list(r_data.keys()) if isinstance(r_data, dict) else list(r_data.index)
except Exception:
return "-"
r_idx = [c for c in r_idx if not str(c).startswith("_bg_") and not str(c).startswith("_txt_") and str(c) != "_raw_symbol_"]
for key in keys:
k_low = key.lower().strip()
for c in r_idx:
if str(c).strip().lower() == k_low:
v = r_data.get(c, "")
v = "" if v is None else str(v).strip()
if v not in ("", "nan", "None", "N/A", "n/a", "-"): return v
for c in r_idx:
if k_low in str(c).strip().lower():
v = r_data.get(c, "")
v = "" if v is None else str(v).strip()
if v not in ("", "nan", "None", "N/A", "n/a", "-"): return v
return "-"
val = _search_row(primary_dict)
if val == "-":
val = _search_row(row)
return val
def _info_card_html(label, value):
return (
"<div style='background:var(--secondary-background-color,
"border:1px solid rgba(128,128,128,0.35);"
"border-radius:6px;padding:8px 10px;min-width:150px;flex:1 1 150px;'>"
f"<div style='font-size:11px;color:var(--text-color,
f"<div style='font-size:14px;font-weight:700;color:var(--text-color,
"</div>"
)
def _render_group(title, fields):
cards = "".join(
_info_card_html(lbl, _sheet_val(sel_row, fund_primary_row, *keys)) for lbl, keys in fields
)
st.markdown(
f"<div style='font-size:13px;font-weight:700;color:
f"<div style='display:flex;flex-wrap:wrap;gap:8px;'>{cards}</div>",
unsafe_allow_html=True,
)
st.markdown("<hr style='margin:16px 0 4px 0;opacity:0.25;'>", unsafe_allow_html=True)
st.markdown(
f"<div style='font-size:15px;font-weight:800;color:var(--text-color,
unsafe_allow_html=True,
)
def _render_group_direct(title, items):
cards = "".join(_info_card_html(lbl, val) for lbl, val in items)
st.markdown(
f"<div style='font-size:13px;font-weight:700;color:
f"<div style='display:flex;flex-wrap:wrap;gap:8px;'>{cards}</div>",
unsafe_allow_html=True,
)
_chg_arrow = "▲" if day_chg >= 0 else "▼"
_chg_color = "
_render_group_direct("📊 Price Snapshot", [
("Last Close", f"₹{last_close:,.2f} "
f"<span style='color:{_chg_color};font-size:12px;'>{_chg_arrow} {day_chg:+.2f}%</span>"),
("52W High", f"₹{float(chart_df['High'].max()):,.2f}"),
("52W Low", f"₹{float(chart_df['Low'].min()):,.2f}"),
("RSI(14)", f"{last_rsi14:.1f}" if last_rsi14 is not None else "–"),
])
_render_group("🏢 Company Info", [
("Company Name", ["company name", "stock name"]),
("Sector", ["sector", "industry"]),
("% Delivery", ["% delivery", "delivery %", "delivery"]),
("52W High Date", ["52w high date", "52 week high date"]),
("52W Low Date", ["52w low date", "52 week low date"]),
("Volume", ["volume"]),
("Turnover", ["turnover"]),
])
_render_group("📡 Signals & System Output", [
("Output", ["output"]),
("Difference from 200 DMA", ["difference from 200 dma", "differance from 200 dma"]),
("CAR Rating", ["cumulative average rule (car) rating", "car rating"]),
("Start GTT Order", ["start gtt order", "gtt order"]),
("Volume Trend", ["volume trend"]),
("Breakout Signal", ["breakout signal"]),
("Trend", ["trend"]),
("MACD Crossover", ["macd crossover"]),
("Buy Signal", ["buy signal"]),
])
_render_group("💰 Fundamentals", [
("Face Value", ["face value"]),
("Total Equity Capital", ["total equity capital"]),
("Market Cap", ["market cap"]),
("EPS", ["eps"]),
("RONW %", ["ronw"]),
("Promoters %", ["promoters %", "promoter"]),
("Institutional %", ["institutional %", "institutional"]),
("Pledged %", ["pledged %", "pledged"]),
("D/E Ratio", ["d/e ratio", "de ratio"]),
("Net Sales (Cr)", ["net sales"]),
("Net Profit (Cr.)", ["net profit"]),
("Reserves (Cr)", ["reserves"]),
("Total Debt (Cr)", ["total debt"]),
("Inventory (Cr)", ["inventory"]),
("Cash & Equiv (Cr)", ["cash & equiv", "cash and equiv", "cash equivalent"]),
("Operating Cash Flow (Cr)", ["operating cash flow"]),
("Trade Receivables (Cr)", ["trade receivables"]),
("Trade Payables (Cr)", ["trade payables"]),
("Fixed Assets/Net PPE (Cr)", ["fixed assets", "net ppe"]),
("Total Assets (Cr)", ["total assets"]),
("Open (₹)", ["open price", "open (", "open"]),
("High (₹)", ["day high", "high price", "high ("]),
("Low (₹)", ["day low", "low price", "low ("]),
("Prev Close (₹)", ["prev close", "previous close", "close price"]),
("Price Change (₹)", ["price change", "change (", "change in price"]),
("% Change", ["% change", "price %", "change %"]),
("Shares Outstanding (Cr)", ["shares outstanding"]),
("Book Value (₹/share)", ["book value"]),
("Public %", ["public %", "public holding"]),
("FII %", ["fii %", "fii holding", "fii"]),
("DII %", ["dii %", "dii holding", "dii"]),
])
with rsi_tab:
idx_rsi = list(chart_df.index)
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=idx_rsi, y=_rsi14_s, name="RSI(14)",
line=dict(color="
fig2.add_hline(y=70, line_dash="dot", line_color="
fig2.add_hline(y=30, line_dash="dot", line_color="
fig2.add_hrect(y0=45, y1=65, fillcolor="
annotation_text="Ideal entry 45-65", annotation_position="top right")
fig2.update_layout(template="plotly_white", height=280, yaxis=dict(range=[0, 100]),
margin=dict(t=30, b=20), plot_bgcolor="
font=dict(color="
fig2.update_xaxes(gridcolor="rgba(0,0,0,0.08)")
fig2.update_yaxes(gridcolor="rgba(0,0,0,0.08)")
st.plotly_chart(fig2, use_container_width=True, key=f"rsi14_chart_{sym}")
st.markdown("---")
st.subheader("📊 National Live Market Analytics Portal Framework")
mkt_tabs = st.tabs([
"🔥 Most Active", "🚀 Volume Gainers", "🏆 Top Gainers/Losers", "⭐ 52W Boundaries", "📦 Stocks Traded", "⚖️ Advances/Declines",
"🕒 Pre-Open Market", "⚡ Price Band Hitters", "🗺️ Index Ticker Heatmap", "🎫 IPO Tracker", "⚠️ Volume Shockers",
"📂 Document Reports", "🖋️ TV Script Engine", "🔮 MunafaSutra Tickers", "🎯 Dhan Asset Registry", "💎 Weekly Activity Metrics",
"🔧 ScanX Core Screener", "🚦 ScanX Live Engine", "🎨 Screener Exploration", "📈 IPO Chittorgarh", "🏷️ IPO Watch Panel", "💓 NSE Pulse",
"📊 Chartink Screeners", "📋 Chartink Dashboard", "🗾 Chartink Atlas", "📚 Mahesh Kaushik", "💰 EFTI Wealth",
"✅ Securities Available", "🏛️ Corporate Filings", "📉 52W Low Market"
])
def _portal_btn(url, label="Open in Browser"):
return (
f"<div style='margin-bottom:8px;'>"
f"<a href='{url}' target='_blank' style='"
f"display:inline-block; background:
f"padding:8px 18px; border-radius:6px; text-decoration:none;'>"
f"🌐 {label}</a>"
f"<span style='font-size:12px; color:
f"</div>"
)
with mkt_tabs[0]:
_u = "https://www.nseindia.com/market-data/most-active-equities"
st.markdown(_portal_btn(_u), unsafe_allow_html=True)
components.html(f'<iframe src="{_u}" width="100%" height="500" style="border:none;"></iframe>', height=520)
with mkt_tabs[1]:
_u = "https://www.nseindia.com/market-data/volume-gainers-spurts"
st.markdown(_portal_btn(_u), unsafe_allow_html=True)
components.html(f'<iframe src="{_u}" width="100%" height="500" style="border:none;"></iframe>', height=520)
with mkt_tabs[2]:
_u = "https://www.nseindia.com/market-data/top-gainers-losers"
st.markdown(_portal_btn(_u), unsafe_allow_html=True)
components.html(f'<iframe src="{_u}" width="100%" height="500" style="border:none;"></iframe>', height=520)
with mkt_tabs[3]:
_u = "https://www.nseindia.com/market-data/52-week-high-equity-market"
st.markdown(_portal_btn(_u), unsafe_allow_html=True)
components.html(f'<iframe src="{_u}" width="100%" height="500" style="border:none;"></iframe>', height=520)
with mkt_tabs[4]:
_u = "https://www.nseindia.com/market-data/stocks-traded"
st.markdown(_portal_btn(_u), unsafe_allow_html=True)
components.html(f'<iframe src="{_u}" width="100%" height="500" style="border:none;"></iframe>', height=520)
with mkt_tabs[5]:
_u = "https://www.nseindia.com/market-data/advance"
st.markdown(_portal_btn(_u), unsafe_allow_html=True)
components.html(f'<iframe src="{_u}" width="100%" height="500" style="border:none;"></iframe>', height=520)
with mkt_tabs[6]:
_u = "https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market"
st.markdown(_portal_btn(_u), unsafe_allow_html=True)
components.html(f'<iframe src="{_u}" width="100%" height="500" style="border:none;"></iframe>', height=520)
with mkt_tabs[7]:
_u = "https://www.nseindia.com/market-data/upper-band-hitters"
st.markdown(_portal_btn(_u), unsafe_allow_html=True)
components.html(f'<iframe src="{_u}" width="100%" height="500" style="border:none;"></iframe>', height=520)
with mkt_tabs[8]:
_u = "https://www.nseindia.com/index-tracker/NIFTY%2050"
st.markdown(_portal_btn(_u), unsafe_allow_html=True)
components.html(f'<iframe src="{_u}" width="100%" height="500" style="border:none;"></iframe>', height=520)
with mkt_tabs[9]:
_u = "https://www.nseindia.com/market-data/all-upcoming-issues-ipo"
st.markdown(_portal_btn(_u), unsafe_allow_html=True)
components.html(f'<iframe src="{_u}" width="100%" height="500" style="border:none;"></iframe>', height=520)
with mkt_tabs[10]:
_u = "https://www.moneycontrol.com/stocks/market-stats/volume-shockers-nse/"
st.markdown(_portal_btn(_u), unsafe_allow_html=True)
components.html(f'<iframe src="{_u}" width="100%" height="500" style="border:none; background-color:white;"></iframe>', height=520)
with mkt_tabs[11]:
_u = "https://www.nseindia.com/all-reports/"
st.markdown(_portal_btn(_u), unsafe_allow_html=True)
components.html(f'<iframe src="{_u}" width="100%" height="500" style="border:none;"></iframe>', height=520)
with mkt_tabs[12]:
_u = "https://www.tradingview.com/scripts/"
st.markdown(_portal_btn(_u), unsafe_allow_html=True)
components.html(f'<iframe src="{_u}" width="100%" height="500" style="border:none;"></iframe>', height=520)
with mkt_tabs[13]:
_u = "https://munafasutra.com/nse/"
st.markdown(_portal_btn(_u), unsafe_allow_html=True)
components.html(f'<iframe src="{_u}" width="100%" height="500" style="border:none; background-color:white;"></iframe>', height=520)
with mkt_tabs[14]:
_u = "https://dhan.co/all-stocks-list/"
st.markdown(_portal_btn(_u), unsafe_allow_html=True)
components.html(f'<iframe src="{_u}" width="100%" height="500" style="border:none; background-color:white;"></iframe>', height=520)
with mkt_tabs[15]:
_u = "https://dhan.co/stocks/market/most-active-stocks-this-week/"
st.markdown(_portal_btn(_u), unsafe_allow_html=True)
components.html(f'<iframe src="{_u}" width="100%" height="500" style="border:none; background-color:white;"></iframe>', height=520)
with mkt_tabs[16]:
_u = "https://scanx.trade/create-custom-screener"
st.markdown(_portal_btn(_u), unsafe_allow_html=True)
components.html(f'<iframe src="{_u}" width="100%" height="500" style="border:none; background-color:white;"></iframe>', height=520)
with mkt_tabs[17]:
_u = "https://scanx.trade/stock-screener/live-market-screener"
st.markdown(_portal_btn(_u), unsafe_allow_html=True)
components.html(f'<iframe src="{_u}" width="100%" height="500" style="border:none; background-color:white;"></iframe>', height=520)
with mkt_tabs[18]:
_u = "https://www.screener.in/explore/"
st.markdown(_portal_btn(_u), unsafe_allow_html=True)
components.html(f'<iframe src="{_u}" width="100%" height="500" style="border:none; background-color:white;"></iframe>', height=520)
with mkt_tabs[19]:
_u = "https://www.chittorgarh.com/"
st.markdown(_portal_btn(_u), unsafe_allow_html=True)
components.html(f'<iframe src="{_u}" width="100%" height="500" style="border:none; background-color:white;"></iframe>', height=520)
with mkt_tabs[20]:
_u = "https://ipowatch.in/"
st.markdown(_portal_btn(_u), unsafe_allow_html=True)
components.html(f'<iframe src="{_u}" width="100%" height="500" style="border:none; background-color:white;"></iframe>', height=520)
with mkt_tabs[21]:
_u = "https://nsepulse.streamlit.app/"
st.markdown(_portal_btn(_u), unsafe_allow_html=True)
components.html(f'<iframe src="{_u}" width="100%" height="500" style="border:none; background-color:white;"></iframe>', height=520)
with mkt_tabs[22]:
_u = "https://chartink.com/screeners"
st.markdown(_portal_btn(_u), unsafe_allow_html=True)
components.html(f'<iframe src="{_u}" width="100%" height="500" style="border:none; background-color:white;"></iframe>', height=520)
with mkt_tabs[23]:
_u = "https://chartink.com/scan_dashboard"
st.markdown(_portal_btn(_u), unsafe_allow_html=True)
components.html(f'<iframe src="{_u}" width="100%" height="500" style="border:none; background-color:white;"></iframe>', height=520)
with mkt_tabs[24]:
_u = "https://chartink.com/atlas"
st.markdown(_portal_btn(_u), unsafe_allow_html=True)
components.html(f'<iframe src="{_u}" width="100%" height="500" style="border:none; background-color:white;"></iframe>', height=520)
with mkt_tabs[25]:
_u = "https://www.maheshkaushik.com/"
st.markdown(_portal_btn(_u), unsafe_allow_html=True)
components.html(f'<iframe src="{_u}" width="100%" height="500" style="border:none; background-color:white;"></iframe>', height=520)
with mkt_tabs[26]:
_u = "https://eftiwealth.com/"
st.markdown(_portal_btn(_u), unsafe_allow_html=True)
components.html(f'<iframe src="{_u}" width="100%" height="500" style="border:none; background-color:white;"></iframe>', height=520)
with mkt_tabs[27]:
_u = "https://www.nseindia.com/static/market-data/securities-available-for-trading"
st.markdown(_portal_btn(_u), unsafe_allow_html=True)
components.html(f'<iframe src="{_u}" width="100%" height="500" style="border:none;"></iframe>', height=520)
with mkt_tabs[28]:
_u = "https://www.nseindia.com/companies-listing/corporate-filings-announcements"
st.markdown(_portal_btn(_u), unsafe_allow_html=True)
components.html(f'<iframe src="{_u}" width="100%" height="500" style="border:none;"></iframe>', height=520)
with mkt_tabs[29]:
_u = "https://www.nseindia.com/market-data/52-week-low-equity-market"
st.markdown(_portal_btn(_u), unsafe_allow_html=True)
components.html(f'<iframe src="{_u}" width="100%" height="500" style="border:none;"></iframe>', height=520)
@st_fragment
def render_performance_matrix():
st.markdown("---")
st.markdown("
perf_width_col1, perf_width_col2 = st.columns([4, 1])
with perf_width_col1:
perf_sizing_mode = st.radio(
"📏 Column Width Adjustment:",
["Default", "✅ Fit to Row 1", "✅✅ Fit to Row 2"],
horizontal=True,
help="Automatically adjust column widths based on text length of the selected row.",
key="perf_matrix_sizing_mode"
)
horizons = [
"1 Day", "2 Day", "3 Day", "5 Day", "7 Day", "10 Day", "12 Day", "15 Days", "20 Days", "25 Days", "30 Days",
"2 Months", "3 Months", "4 Months", "5 Months", "6 Months", "7 Months", "8 Months", "9 Months", "10 Months", "11 Months",
"1 Year", "18 Months", "1.5 Years", "2 Years", "2.5 Years", "3 Years", "Volume"
]
col_tools1, col_tools2, col_tools3 = st.columns([2, 2, 3])
with col_tools1:
sort_basis = st.selectbox("🎯 Base Horizon for Performance Ranking:", horizons, index=0)
with col_tools2:
sort_direction = st.radio("排序 Sorting Order Type:", ["Best -> Worst", "Worst -> Best"], index=0, horizontal=True)
with col_tools3:
summary_search = st.text_input("🔍 Filter stocks inside this matrix...", placeholder="Type symbol name...", key="perf_matrix_search")
detected_metric_map = {}
for h in horizons:
if h == "Volume":
if vol_target: detected_metric_map[h] = vol_target
continue
keywords = [h.lower(), h.lower().replace(" ", ""), h.lower().replace("s", "")]
if h == "1 Day": keywords.append("price %")
for c in actual_cols:
if any(k in c.lower() for k in keywords) and "%" in c.lower():
detected_metric_map[h] = c
break
if detected_metric_map:
reporting_data = []
for idx, row in filtered_df.iterrows():
clean_ticker = str(row.get('_raw_symbol_', '')).strip()
price_val = row.get(cmp_target, "") if cmp_target else ""
url = f"https://charting.nseindia.com/?symbol={clean_ticker}-EQ"
hyperlinked_name = f'<a href="{url}" target="_blank" style="text-decoration:none; color:
entry = {
"STOCK NAME": hyperlinked_name,
"CURRENT PRICE": price_val
}
for h, actual_col in detected_metric_map.items():
raw_val = str(row.get(actual_col, "0")).replace("%", "").replace(",", "").strip()
try:
entry[h] = float(raw_val) if raw_val not in ["", "nan", "None"] else 0.0
except ValueError:
entry[h] = 0.0
if deliv_target:
raw_dval = str(row.get(deliv_target, "0")).replace("%", "").replace(",", "").strip()
try:
entry["% Delivery"] = float(raw_dval) if raw_dval not in ["", "nan", "None"] else 0.0
except ValueError:
entry["% Delivery"] = 0.0
if rsi_target:
raw_rsi = str(row.get(rsi_target, "")).replace("%", "").replace(",", "").strip()
try:
entry["RSI (14)"] = float(raw_rsi) if raw_rsi not in ["", "nan", "None"] else None
except ValueError:
entry["RSI (14)"] = None
if diff_200_target:
raw_diff200 = str(row.get(diff_200_target, "")).replace("%", "").replace(",", "").strip()
try:
entry["Diff. from 200 DMA"] = float(raw_diff200) if raw_diff200 not in ["", "nan", "None"] else None
except ValueError:
entry["Diff. from 200 DMA"] = None
if high_target:
raw_52h = str(row.get(high_target, "")).replace(",", "").strip()
try:
entry["52W High"] = float(raw_52h) if raw_52h not in ["", "nan", "None"] else None
except ValueError:
entry["52W High"] = None
if low_target:
raw_52l = str(row.get(low_target, "")).replace(",", "").strip()
try:
entry["52W Low"] = float(raw_52l) if raw_52l not in ["", "nan", "None"] else None
except ValueError:
entry["52W Low"] = None
if volume_trend_target:
entry["Volume Trend"] = str(row.get(volume_trend_target, "")).strip()
if breakout_signal_target:
entry["Breakout Signal"] = str(row.get(breakout_signal_target, "")).strip()
if trend_target:
entry["Trend"] = str(row.get(trend_target, "")).strip()
if macd_crossover_target:
entry["MACD Crossover"] = str(row.get(macd_crossover_target, "")).strip()
if buy_signal_target:
entry["Buy Signal"] = str(row.get(buy_signal_target, "")).strip()
clean_r = {k: v for k, v in row.items() if not str(k).startswith('_')}
bf_s, bf_g, _ = compute_bottom_fishing_score(clean_r, actual_cols)
entry["🔬 BF Score"] = bf_s
entry["📊 BF Grade"] = bf_g
reporting_data.append(entry)
perf_df = pd.DataFrame(reporting_data)
if summary_search:
perf_df = perf_df[perf_df["STOCK NAME"].str.replace(r'<[^>]*>', '', regex=True).str.contains(summary_search, case=False, na=False)]
target_sort_col = sort_basis if sort_basis in perf_df.columns else perf_df.columns[2]
ascending_flag = (sort_direction == "Worst -> Best")
perf_df = perf_df.sort_values(by=target_sort_col, ascending=ascending_flag).reset_index(drop=True)
perf_df.insert(0, "RANK", perf_df.index + 1)
display_perf_df = perf_df.copy()
for h in detected_metric_map.keys():
if h in display_perf_df.columns:
if h == "Volume":
display_perf_df[h] = display_perf_df[h].apply(lambda x: f"{int(x):,}" if pd.notnull(x) else "-")
else:
display_perf_df[h] = display_perf_df[h].apply(lambda x: f"+{x:.2f}%" if x > 0 else (f"{x:.2f}%" if x < 0 else "0.00%"))
if "% Delivery" in display_perf_df.columns:
display_perf_df["% Delivery"] = display_perf_df["% Delivery"].apply(lambda x: f"{x:.2f}%" if pd.notnull(x) else "-")
if "RSI (14)" in display_perf_df.columns:
display_perf_df["RSI (14)"] = display_perf_df["RSI (14)"].apply(lambda x: f"{x:.2f}" if pd.notnull(x) else "-")
if "Diff. from 200 DMA" in display_perf_df.columns:
display_perf_df["Diff. from 200 DMA"] = display_perf_df["Diff. from 200 DMA"].apply(
lambda x: (f"+{x:.2f}%" if x > 0 else (f"{x:.2f}%" if x < 0 else "0.00%")) if pd.notnull(x) else "-"
)
if "52W High" in display_perf_df.columns:
display_perf_df["52W High"] = display_perf_df["52W High"].apply(lambda x: f"{x:,.2f}" if pd.notnull(x) else "-")
if "52W Low" in display_perf_df.columns:
display_perf_df["52W Low"] = display_perf_df["52W Low"].apply(lambda x: f"{x:,.2f}" if pd.notnull(x) else "-")
perf_gb = GridOptionsBuilder.from_dataframe(display_perf_df)
perf_gb.configure_default_column(filter=True, sortable=True, resizable=True, floatingFilter=False, flex=0)
perf_gb.configure_column("RANK", width=70, pinned="left")
perf_gb.configure_column("STOCK NAME", width=140, pinned="left", cellRenderer=html_renderer)
color_code_js = JsCode()
bf_score_js = JsCode()
bf_grade_js = JsCode()
trend_style_js = JsCode()
for col in display_perf_df.columns:
if col in ("RANK",):
continue
if perf_sizing_mode == "✅ Fit to Row 1" and len(display_perf_df) > 0:
char_count = get_clean_text_length(display_perf_df.iloc[0][col])
header_count = len(str(col))
dyn_width = int(max(char_count, header_count) * 7 + 22)
elif perf_sizing_mode == "✅✅ Fit to Row 2" and len(display_perf_df) > 1:
char_count = get_clean_text_length(display_perf_df.iloc[1][col])
header_count = len(str(col))
dyn_width = int(max(char_count, header_count) * 7 + 22)
else:
default_widths = {
"STOCK NAME": 140, "CURRENT PRICE": 130, "% Delivery": 110, "🔬 BF Score": 110, "📊 BF Grade": 160,
"RSI (14)": 100, "Diff. from 200 DMA": 140, "52W High": 110, "52W Low": 110,
"Volume Trend": 120, "Breakout Signal": 130, "Trend": 130, "MACD Crossover": 130, "Buy Signal": 130,
}
dyn_width = default_widths.get(col, 130)
min_w = max(70, min(dyn_width, 90))
if col == "STOCK NAME":
perf_gb.configure_column(col, width=dyn_width, minWidth=min_w, pinned="left", cellRenderer=html_renderer)
elif col == "CURRENT PRICE":
perf_gb.configure_column(col, width=dyn_width, minWidth=min_w)
elif col == "🔬 BF Score":
perf_gb.configure_column(col, width=dyn_width, minWidth=min_w, cellStyle=bf_score_js)
elif col == "📊 BF Grade":
perf_gb.configure_column(col, width=dyn_width, minWidth=min_w, cellStyle=bf_grade_js)
elif col in ("Volume Trend", "Breakout Signal", "Trend", "MACD Crossover", "Buy Signal"):
perf_gb.configure_column(col, width=dyn_width, minWidth=min_w, cellStyle=trend_style_js)
elif col in detected_metric_map or col == "Diff. from 200 DMA":
perf_gb.configure_column(col, width=dyn_width, minWidth=min_w, cellStyle=color_code_js)
else:
perf_gb.configure_column(col, width=dyn_width, minWidth=min_w)
perf_gb.configure_grid_options(domLayout="normal", rowHeight=38, headerHeight=45, enableCellTextSelection=True, alwaysShowHorizontalScroll=True, suppressColumnVirtualisation=True)
perf_grid_ops = perf_gb.build()
AgGrid(display_perf_df, gridOptions=perf_grid_ops, theme="streamlit", allow_unsafe_jscode=True, fit_columns_on_grid_load=False, height=450, width='100%', key="horizon_perf_grid")
render_performance_matrix()
@st_fragment
def render_bottom_fishing_scanner():
st.markdown("---")
st.markdown("
st.caption("Stocks that are 8–15% above 52W Low, in uptrend, with high volume + strong fundamentals")
bf_width_col1, bf_width_col2 = st.columns([4, 1])
with bf_width_col1:
bf_sizing_mode = st.radio(
"📏 Column Width Adjustment:",
["Default", "✅ Fit to Row 1", "✅✅ Fit to Row 2"],
horizontal=True,
help="Automatically adjust column widths based on text length of the selected row.",
key="bf_scanner_sizing_mode"
)
bf_col1, bf_col2, bf_col3 = st.columns([2, 2, 2])
with bf_col1:
min_bf_score = st.slider("Minimum BF Score:", min_value=0, max_value=100, value=55, step=5, key="bf_min_score")
with bf_col2:
bf_sort = st.radio("Sort by:", ["Score (High→Low)", "Score (Low→High)"], horizontal=True, key="bf_sort")
with bf_col3:
bf_search = st.text_input("Search symbol:", placeholder="e.g. WIPRO", key="bf_search")
bf_results = []
for idx, row in filtered_df.iterrows():
clean_r = {k: v for k, v in row.items() if not str(k).startswith('_')}
bf_s, bf_g, bf_rsns = compute_bottom_fishing_score(clean_r, actual_cols)
if bf_s >= min_bf_score:
ticker = str(row.get('_raw_symbol_', '')).strip()
cmp_v = clean_r.get(cmp_target, "") if cmp_target else ""
sector_col = next((c for c in actual_cols if "sector" in c.lower()), None)
sector_v = clean_r.get(sector_col, "") if sector_col else ""
nse_chart_url = f"https://charting.nseindia.com/?symbol={ticker}-EQ"
symbol_link = f'<a href="{nse_chart_url}" target="_blank" style="text-decoration:none; color:
deliv_v = None
if deliv_target:
raw_dv = str(clean_r.get(deliv_target, "")).replace("%", "").replace(",", "").strip()
try:
deliv_v = float(raw_dv) if raw_dv not in ["", "nan", "None"] else None
except ValueError:
deliv_v = None
rsi_v = str(clean_r.get(rsi_target, "")).strip() if rsi_target else "-"
diff200_v = str(clean_r.get(diff_200_target, "")).strip() if diff_200_target else "-"
high52_v = str(clean_r.get(high_target, "")).strip() if high_target else "-"
low52_v = str(clean_r.get(low_target, "")).strip() if low_target else "-"
vol_trend_v = str(clean_r.get(volume_trend_target, "")).strip() if volume_trend_target else "-"
breakout_v = str(clean_r.get(breakout_signal_target, "")).strip() if breakout_signal_target else "-"
trend_v = str(clean_r.get(trend_target, "")).strip() if trend_target else "-"
macd_v = str(clean_r.get(macd_crossover_target, "")).strip() if macd_crossover_target else "-"
buy_sig_v = str(clean_r.get(buy_signal_target, "")).strip() if buy_signal_target else "-"
bf_results.append({
"Symbol": symbol_link,
"Score": bf_s,
"Grade": bf_g,
"CMP": cmp_v,
"RSI (14)": rsi_v,
"% Delivery": f"{deliv_v:.2f}%" if deliv_v is not None else "-",
"Diff. from 200 DMA": diff200_v,
"52W High": high52_v,
"52W Low": low52_v,
"Volume Trend": vol_trend_v,
"Breakout Signal": breakout_v,
"Trend": trend_v,
"MACD Crossover": macd_v,
"Buy Signal": buy_sig_v,
"Sector": str(sector_v)[:30],
"Key Reasons": " | ".join(bf_rsns[:3])
})
if bf_search:
bf_results = [r for r in bf_results if bf_search.upper() in re.sub(r'<[^>]*>', '', r["Symbol"]).upper()]
bf_results.sort(key=lambda x: x["Score"], reverse=(bf_sort == "Score (High→Low)"))
if bf_results:
st.success(f"✅ Found **{len(bf_results)}** stocks matching your bottom-fishing criteria (score ≥ {min_bf_score})")
bf_scan_df = pd.DataFrame(bf_results)
bf_gb = GridOptionsBuilder.from_dataframe(bf_scan_df)
bf_gb.configure_default_column(filter=True, sortable=True, resizable=True, floatingFilter=False, flex=0)
bf_score_style = JsCode()
trend_style_js = JsCode()
bf_default_widths = {
"Symbol": 120, "Score": 90, "Grade": 160, "CMP": 100, "% Delivery": 110, "Sector": 200, "Key Reasons": 400,
"RSI (14)": 100, "Diff. from 200 DMA": 140, "52W High": 110, "52W Low": 110,
"Volume Trend": 120, "Breakout Signal": 130, "Trend": 130, "MACD Crossover": 130, "Buy Signal": 130,
}
for col in bf_scan_df.columns:
if bf_sizing_mode == "✅ Fit to Row 1" and len(bf_scan_df) > 0:
char_count = get_clean_text_length(bf_scan_df.iloc[0][col])
header_count = len(str(col))
dyn_w = int(max(char_count, header_count) * 7 + 22)
elif bf_sizing_mode == "✅✅ Fit to Row 2" and len(bf_scan_df) > 1:
char_count = get_clean_text_length(bf_scan_df.iloc[1][col])
header_count = len(str(col))
dyn_w = int(max(char_count, header_count) * 7 + 22)
else:
dyn_w = bf_default_widths.get(col, 120)
pinned = "left" if col == "Symbol" else None
min_w = max(70, min(dyn_w, 90))
if col == "Score":
bf_gb.configure_column(col, width=dyn_w, minWidth=min_w, pinned=pinned, cellStyle=bf_score_style)
elif col == "Symbol":
bf_gb.configure_column(col, width=dyn_w, minWidth=min_w, pinned=pinned, cellRenderer=html_renderer)
elif col in ("Volume Trend", "Breakout Signal", "Trend", "MACD Crossover", "Buy Signal"):
bf_gb.configure_column(col, width=dyn_w, minWidth=min_w, pinned=pinned, cellStyle=trend_style_js)
else:
bf_gb.configure_column(col, width=dyn_w, minWidth=min_w, pinned=pinned)
bf_gb.configure_grid_options(domLayout="normal", rowHeight=40, headerHeight=45, alwaysShowHorizontalScroll=True, suppressColumnVirtualisation=True)
bf_grid_ops = bf_gb.build()
AgGrid(bf_scan_df, gridOptions=bf_grid_ops, theme="streamlit", allow_unsafe_jscode=True, fit_columns_on_grid_load=False, height=400, width='100%', key="bf_scanner_grid")
bf_buffer = io.BytesIO()
with pd.ExcelWriter(bf_buffer, engine='openpyxl') as writer:
clean_for_export(bf_scan_df).to_excel(writer, index=False, sheet_name="Bottom Fishing")
st.download_button("📥 Download BF Scanner Results", data=bf_buffer.getvalue(),
file_name=f"BottomFishing_{pd.Timestamp.now().strftime('%Y%m%d')}.xlsx",
mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
else:
st.info(f"No stocks found with BF Score ≥ {min_bf_score}. Try lowering the minimum score.")
render_bottom_fishing_scanner()
if pct_target:
st.markdown("---")
st.markdown("
temp_df = filtered_df.copy()
temp_df[pct_target] = pd.to_numeric(temp_df[pct_target].astype(str).str.replace(r'[%,]', '', regex=True), errors='coerce')
temp_df = temp_df.dropna(subset=[pct_target])
top_10 = temp_df.nlargest(10, pct_target)
bottom_10 = temp_df.nsmallest(10, pct_target)
colA, colB = st.columns(2)
with colA:
top_html = "<h4 style='margin-top:0px; margin-bottom:8px;'>⬆️ Top 10 (Daily)</h4>"
for _, row in top_10.iterrows():
clean_s = str(row.get('_raw_symbol_', '')).strip()
v = row[pct_target]
cmp_val = row.get(cmp_target, "") if cmp_target else ""
try:
price_float = float(str(cmp_val).replace(',', '').strip())
pct_float = float(v)
prev_price = price_float / (1 + (pct_float / 100))
abs_change = price_float - prev_price
change_str = f"<span style='font-size: 0.85em; opacity: 0.75; margin-right: 6px;'>+{abs_change:,.2f}</span>"
price_str = f"₹{price_float:,.2f}"
except:
price_str = f"₹{cmp_val}"
change_str = ""
url = f"https://charting.nseindia.com/?symbol={clean_s}-EQ"
top_html += f"<a href='{url}' target='_blank' style='text-decoration:none;'><div style='background-color:
st.markdown(top_html, unsafe_allow_html=True)
with colB:
bot_html = "<h4 style='margin-top:0px; margin-bottom:8px;'>⬇️ Bottom 10 (Daily)</h4>"
for _, row in bottom_10.iterrows():
clean_s = str(row.get('_raw_symbol_', '')).strip()
v = row[pct_target]
cmp_val = row.get(cmp_target, "") if cmp_target else ""
try:
price_float = float(str(cmp_val).replace(',', '').strip())
pct_float = float(v)
prev_price = price_float / (1 + (pct_float / 100))
abs_change = price_float - prev_price
change_str = f"<span style='font-size: 0.85em; opacity: 0.75; margin-right: 6px;'>{abs_change:,.2f}</span>"
price_str = f"₹{price_float:,.2f}"
except:
price_str = f"₹{cmp_val}"
change_str = ""
url = f"https://charting.nseindia.com/?symbol={clean_s}-EQ"
bot_html += f"<a href='{url}' target='_blank' style='text-decoration:none;'><div style='background-color:
st.markdown(bot_html, unsafe_allow_html=True)
st.markdown("---")
st.markdown("
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import pandas as pd
def get_time_ago_global(pubdate_str):
try:
dt = pd.to_datetime(pubdate_str, utc=True)
now = pd.Timestamp.now(tz='UTC')
seconds = (now - dt).total_seconds()
if seconds < 0: return "Just now"
if seconds < 60: return f"{int(seconds)} secs ago"
if seconds < 3600:
mins = int(seconds / 60)
return f"{mins} min{'s' if mins != 1 else ''} ago"
if seconds < 86400:
hours = int(seconds / 3600)
return f"{hours} hour{'s' if hours != 1 else ''} ago"
if seconds < 172800:
return f"Yesterday ({dt.strftime('%d %b %Y')})"
days = int(seconds / 86400)
return f"{days} days ago ({dt.strftime('%d %b %Y')})"
except Exception:
return "Recent"
@st.cache_data(ttl=600)
def fetch_strict_alerts(symbol, limit=10):
try:
search_terms = f'"{symbol}" NSE AND ("52 week high" OR "52 week low" OR "upper circuit" OR "lower circuit")'
query = urllib.parse.quote(search_terms)
url = f"https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
xml_data = response.read()
root = ET.fromstring(xml_data)
alert_keywords = ["52 week high", "52-week high", "52 week low", "52-week low", "upper circuit", "lower circuit", "hits circuit", "locked in circuit"]
news_list = []
for item in root.findall('.//item'):
title = item.find('title').text
if not any(keyword in title.lower() for keyword in alert_keywords):
continue
link = item.find('link').text
pub_date = item.find('pubDate').text if item.find('pubDate') is not None else ""
try:
dt = pd.to_datetime(pub_date, utc=True)
except Exception:
dt = pd.Timestamp.now(tz='UTC') - pd.Timedelta(days=100)
now = pd.Timestamp.now(tz='UTC')
diff_days = (now - dt).total_seconds() / 86400
if diff_days <= 15.0:
time_ago_str = get_time_ago_global(pub_date)
news_list.append({
"display_title": f"🚨 **[ALERT]** {title}",
"link": link,
"time_ago": time_ago_str,
"timestamp": dt,
"title_raw": title
})
news_list.sort(key=lambda x: x["timestamp"], reverse=True)
return news_list[:limit]
except Exception:
return []
@st.cache_data(ttl=600)
def fetch_all_stock_news_tab3(symbol, limit=5):
try:
query = urllib.parse.quote(f'"{symbol}" stock share news NSE India')
url = f"https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
xml_data = response.read()
root = ET.fromstring(xml_data)
news_list = []
alert_keywords = ["52 week high", "52-week high", "52 week low", "52-week low", "upper circuit", "lower circuit", "hits circuit", "locked in circuit", "upper limit", "lower limit"]
for item in root.findall('.//item'):
title = item.find('title').text
link = item.find('link').text
pub_date = item.find('pubDate').text if item.find('pubDate') is not None else ""
is_alert = any(keyword in title.lower() for keyword in alert_keywords)
icon = "🚨 **[ALERT]** " if is_alert else ""
display_title = f"{icon}{title}"
try:
dt = pd.to_datetime(pub_date, utc=True)
except Exception:
dt = pd.Timestamp.now(tz='UTC') - pd.Timedelta(days=100)
now = pd.Timestamp.now(tz='UTC')
diff_days = (now - dt).total_seconds() / 86400
if diff_days <= 1.0:
time_ago_str = get_time_ago_global(pub_date)
news_list.append({
"display_title": display_title,
"link": link,
"time_ago": time_ago_str,
"timestamp": dt
})
news_list.sort(key=lambda x: x["timestamp"], reverse=True)
return news_list[:limit]
except Exception:
return []
@st.cache_data(ttl=600)
def fetch_all_stock_news_tab4(symbol, limit=5):
try:
query = urllib.parse.quote(f'"{symbol}" stock share news NSE India')
url = f"https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
xml_data = response.read()
root = ET.fromstring(xml_data)
news_list = []
alert_keywords = ["52 week high", "52-week high", "52 week low", "52-week low", "upper circuit", "lower circuit", "hits circuit", "locked in circuit", "upper limit", "lower limit"]
for item in root.findall('.//item'):
title = item.find('title').text
link = item.find('link').text
pub_date = item.find('pubDate').text if item.find('pubDate') is not None else ""
is_alert = any(keyword in title.lower() for keyword in alert_keywords)
icon = "🚨 **[ALERT]** " if is_alert else ""
display_title = f"{icon}{title}"
try:
dt = pd.to_datetime(pub_date, utc=True)
except Exception:
dt = pd.Timestamp.now(tz='UTC') - pd.Timedelta(days=100)
time_ago_str = get_time_ago_global(pub_date)
news_list.append({
"display_title": display_title,
"link": link,
"time_ago": time_ago_str,
"timestamp": dt
})
news_list.sort(key=lambda x: x["timestamp"], reverse=True)
return news_list[:limit]
except Exception:
return []
@st.cache_data(ttl=600)
def fetch_corporate_announcements(symbol, limit=6):
try:
search_terms = f'"{symbol}" AND ("Regulation 30" OR "LODR" OR "Board Meeting" OR "AGM" OR "Analyst Meet" OR "Financial Results" OR "Corporate Action" OR "Dividend")'
query = urllib.parse.quote(search_terms)
url = f"https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
xml_data = response.read()
root = ET.fromstring(xml_data)
news_list = []
for item in root.findall('.//item'):
title = item.find('title').text
link = item.find('link').text
pub_date = item.find('pubDate').text if item.find('pubDate') is not None else ""
try:
dt = pd.to_datetime(pub_date, utc=True)
except Exception:
dt = pd.Timestamp.now(tz='UTC') - pd.Timedelta(days=100)
time_ago_str = get_time_ago_global(pub_date)
news_list.append({
"display_title": f"📢 {title}",
"link": link,
"time_ago": time_ago_str,
"timestamp": dt
})
news_list.sort(key=lambda x: x["timestamp"], reverse=True)
return news_list[:limit]
except Exception:
return []
BSE_CODE_MAP = {
"RELIANCE": "500325", "TCS": "532540", "HDFCBANK": "500180",
"INFY": "500209", "ICICIBANK": "532174", "HINDUNILVR": "500696",
"SBIN": "500112", "BHARTIARTL": "532454", "BAJFINANCE": "500034",
"KOTAKBANK": "500247", "LT": "500510", "HCLTECH": "532281",
"AXISBANK": "532215", "ASIANPAINT": "500820", "MARUTI": "532500",
"SUNPHARMA": "524715", "TITAN": "500114", "ULTRACEMCO": "532538",
"ONGC": "500312", "NTPC": "532555", "POWERGRID": "532898",
"WIPRO": "507685", "NESTLEIND": "500790", "JSWSTEEL": "500228",
"TATASTEEL": "500470", "TATAMOTORS": "500570", "TECHM": "532755",
"GRASIM": "500300", "ADANIENT": "512599", "ADANIPORTS": "532921",
"COALINDIA": "533278", "DIVISLAB": "532488", "DRREDDY": "500124",
"EICHERMOT": "505200", "BAJAJFINSV": "532978", "BAJAJ-AUTO": "532977",
"CIPLA": "500087", "BRITANNIA": "500825", "HEROMOTOCO": "500182",
"APOLLOHOSP": "508869", "HINDALCO": "500440", "UPL": "512070",
"TATACONSUM": "500800", "SBILIFE": "540719", "HDFCLIFE": "540777",
"INDUSINDBK": "532187", "BPCL": "500547", "IOC": "530965",
"M&M": "500520", "PIDILITIND": "500331", "SIEMENS": "500550",
"HAVELLS": "517354", "VOLTAS": "500575", "AMBUJACEM": "500425",
"ACC": "500410", "SHREECEM": "500387", "RAMCOCEM": "500260",
"DALMIA": "502525", "JKCEMENT": "532644", "STAR": "540175",
"TVSMOTOR": "532343", "BOSCHLTD": "500530", "MUTHOOTFIN": "533398",
"CHOLAFIN": "500443", "BAJAJHLDNG": "500490", "TORNTPHARM": "500420",
"AUROPHARMA": "524208", "LUPIN": "500257", "BIOCON": "532523",
"ALKEM": "539523", "IPCALAB": "530827", "GLAXO": "500660",
"ABBOTINDIA": "500488", "PFIZER": "500680", "SANOFI": "500674",
"MCDOWELL-N": "532432", "ITC": "500875", "GODFRYPHLP": "500163",
"COLPAL": "500830", "DABUR": "500096", "MARICO": "531642",
"GODREJCP": "532424", "HINDPETRO": "500104", "CASTROLIND": "500870",
"INDIGO": "521737", "INTERGLOBE": "539448", "SPICEJET": "500285",
"IRCTC": "542830", "CONCOR": "531344", "ADANIGREEN": "541450",
"ADANITRANS": "539254", "TATAPOWER": "500400", "TORNTPOWER": "532779",
"CESC": "500084", "NHPC": "533098", "SJVN": "533206",
"PFC": "532810", "RECLTD": "532955", "IRFC": "543257",
"ZOMATO": "543320", "NYKAA": "543384", "PAYTM": "543396",
"POLICYBZR": "543390", "DELHIVERY": "543529", "CARTRADE": "543202",
"RVNL": "542649", "IRCON": "541956", "NBCC": "534309",
"HUDCO": "540530", "MMTC": "513377", "MTNL": "500108",
"BEL": "500049", "HAL": "541154", "COCHINSHIP": "526235",
"MAZAGON": "543237", "GRSE": "542351", "MIDHANI": "541195",
"BEML": "500048", "BHEL": "500103", "SAIL": "500113",
"NMDC": "526371", "MOIL": "533286", "NATIONALUM": "532234",
"HINDZINC": "500188", "VEDL": "500295", "GMRINFRA": "532754",
"NHAI": "500253", "IRB": "532947", "ASHOKLEY": "500477",
"ESCORTS": "500495", "FORCE": "517168", "SML": "513275",
"MOTHERSON": "517334", "MINDAIND": "532539", "ENDURANCE": "540350",
"BALKRISIND": "502355", "APOLLOTYRE": "500877", "MRF": "500290",
"CEATLTD": "500878", "JK TYRE": "530007", "INOXWIND": "539083",
"SUZLON": "532667", "RPOWER": "500390", "JPPOWER": "532627",
"FEDERALBNK": "500469", "IDFCFIRSTB": "539437", "BANDHANBNK": "541153",
"RBLBANK": "540065", "DCBBANK": "532772", "KTKBANK": "532209",
"SOUTHBANK": "532218", "CANBK": "532483", "BANKBARODA": "532134",
"UNIONBANK": "532477", "INDIANB": "532814", "UCOBANK": "532505",
"CENTRALBK": "532885", "MAHABANK": "532525", "J&KBANK": "532209",
"PNB": "532461", "IOB": "532388", "BANKINDIA": "532149",
"DENABANK": "532121", "SYNDIBANK": "532276", "VIJAYABANK": "532245",
"ORIENTBANK": "500315", "CORPBANK": "532179", "ANDHRABANK": "532418",
"ALLAHABAD": "532480", "ALBK": "532480", "MFSL": "542299",
"HDFCAMC": "541530", "NIPPONLIFE": "543171", "UTIAMC": "543238",
"ABCAPITAL": "540691", "ANGELONE": "543235", "ICICIGI": "540716",
"GICRE": "540755", "NIACL": "540769", "STAR": "540175",
"CROMPTON": "539876", "ORIENTELEC": "531637", "BLUESTAR": "500067",
"WHIRLPOOL": "500238", "VGUARD": "532953", "BAJAJEL": "500031",
"CERA": "532443", "HINDWARE": "509820", "HSIL": "509675",
"KAJARIACER": "500233", "SOMANYCER": "532622", "GRINDWELL": "506076",
"CARBORUNIV": "513375", "ASTRAL": "532830", "FINOLEX": "500940",
"SUPREMEIND": "509930", "BERGER": "509480", "KANSAINER": "500165",
"AKZOINDIA": "500710", "INDIACEM": "530005", "RAMCOIND": "500260",
"DALMIA": "502525", "HEIDELBERG": "500292", "PRISM": "500338",
"BIRLACORPN": "500335", "ORIENTCEM": "502420", "SAGCEM": "502090",
"STARCEMENT": "540575", "JKLAKSHMI": "500380", "NUVOCO": "543334",
"ZYDUSLIFE": "532321", "TORNTPHAR": "500420", "NATCOPHAR": "524816",
"GRANULES": "532482", "LAURUS": "540222", "STRIDES": "532531",
"AJANTPHAR": "532331", "CAPLIPOINT": "539266", "DIVI": "532488",
"SUNPHARMA": "524715", "GLAND": "543245", "SEQUENT": "543225",
"METROPOLIS": "542650", "DRLAL": "532259", "THYROCARE": "539871",
"KRSNAA": "543328", "VIJAYA": "532542", "MAXHEALTH": "543220",
"KIMS": "543308", "ASTER": "540975", "FORTIS": "532843",
"NHOSPIT": "532526", "APOLLOHOSP": "508869", "NARAYANA": "539551",
"YATHARTH": "544120", "RAINBOW": "543524", "SUVENPHAR": "530239",
"LAURUSLABS": "540222", "SOLARA": "541540", "SHILPAMED": "530879",
"PERSISTENT": "533179", "MINDTREE": "532819", "MPHASIS": "526299",
"HEXAWARE": "532861", "NIIT": "500304", "KPIT": "542651",
"LTTS": "540115", "COFORGE": "532541", "ZENSAR": "504067",
"RAMSYSTEMS": "532370", "MASTEK": "523704", "SASKEN": "532663",
"TATAELXSI": "500408", "CYIENT": "532175", "SONATSOFTW": "532221",
"TANLA": "532790", "LTIM": "540005", "INFY": "500209",
"ROUTE": "543228", "BSOFT": "526301", "NEWGEN": "540900",
"INTELLECT": "538835", "NUCLEUS": "531209", "NELCO": "504112",
"DELTACORP": "532840", "WONDERLA": "538268", "MAHINDCIE": "532756",
"STARHLTH": "543412", "NAUKRI": "532777", "JUSTDIAL": "535648",
"MATRIMONY": "539846", "MAKEMYTRIP": "513377", "IXIGO": "544229",
"RATEGAIN": "543417", "TEAMLEASE": "539658", "QUESS": "539978",
"SIS": "540673", "SECURKLOUD": "539963", "HAPPYFORGE": "543532",
"KALYANKJIL": "543278", "SENCO": "543456", "THANGAMAYL": "531509",
"TRIBHOVAND": "512415", "PC JEWELLER": "534809", "RAJESHEXPO": "531500",
}
@st.cache_data(ttl=600)
def fetch_bse_all_documents(bse_code, days_back=90):
result = {"announcements": [], "annual_reports": [], "credit_ratings": [], "concalls": [], "ppt": []}
try:
import datetime
to_date   = datetime.date.today()
from_date = to_date - datetime.timedelta(days=days_back)
str_from  = from_date.strftime("%Y%m%d")
str_to    = to_date.strftime("%Y%m%d")
ann_url = (
f"https://api.bseindia.com/BseIndiaAPI/api/AnnSubCategoryGetData/w"
f"?pageno=1&strCat=-1&strPrevDate={str_from}&strScrip={bse_code}"
f"&strSearch=P&strToDate={str_to}&strType=C&subcategory=-1"
)
headers = {
"User-Agent": "Mozilla/5.0",
"Referer": "https://www.bseindia.com/",
"Accept": "application/json",
}
req = urllib.request.Request(ann_url, headers=headers)
with urllib.request.urlopen(req, timeout=8) as r:
data = json.loads(r.read())
for row in (data.get("Table") or [])[:30]:
title = row.get("HEADLINE", "") or row.get("SUBCATNAME", "")
dt_str = row.get("NEWS_DT", "") or row.get("DT_TM", "")
newsid = row.get("NEWSID", "")
link = f"https://www.bseindia.com/xml-data/corpfiling/AttachLive/{newsid}.pdf" if newsid else ""
try:
dt_disp = pd.to_datetime(dt_str).strftime("%d %b %Y")
except Exception:
dt_disp = dt_str[:10]
subcat = (row.get("SUBCATNAME") or "").lower()
entry = {"title": title, "link": link, "date": dt_disp}
if any(k in subcat for k in ["annual report", "annual rep"]):
result["annual_reports"].append(entry)
elif any(k in subcat for k in ["credit rat", "rating"]):
result["credit_ratings"].append(entry)
elif any(k in subcat for k in ["concall", "con call", "earnings call", "analyst"]):
result["concalls"].append(entry)
elif any(k in subcat for k in ["investor presentation", "presentation", "ppt"]):
result["ppt"].append(entry)
else:
result["announcements"].append(entry)
except Exception:
pass
return result
try:
filtered_symbols_full = filtered_df['_raw_symbol_'].dropna().unique()
if len(filtered_symbols_full) > 0:
news_tab1, news_tab2, news_tab3, news_tab4, news_tab5, news_tab6, news_tab7 = st.tabs([
"🚨 Latest Alerts Timeline",
"🏢 Alerts by Stock",
"📰 Smart News Engine (1 Day)",
"📰 Smart News Engine (All News)",
"📢 Corporate Announcements",
"📢 DOCUMENTS HUB",
"📜 Rules"
])
master_alerts_list = []
filtered_symbols_alerts = filtered_symbols_full[:30]
with st.spinner("Scanning Top 30 stocks for Circuit & 52-Week Breakouts (15 Days)..."):
for sym in filtered_symbols_alerts:
clean_symbol = str(sym).strip()
news_items = fetch_strict_alerts(clean_symbol, limit=15)
for n in news_items:
n["symbol"] = clean_symbol
master_alerts_list.append(n)
alerted_symbols     = {n["symbol"] for n in master_alerts_list}
fresh_alerted_syms  = {
n["symbol"] for n in master_alerts_list
if "min"  in n["time_ago"] or "hour" in n["time_ago"]
or "sec"  in n["time_ago"] or "Just now" in n["time_ago"]
}
def symbol_badge(sym):
if sym in fresh_alerted_syms:
bg, fg, border = "
elif sym in alerted_symbols:
bg, fg, border = "
else:
bg, fg, border = "
return (
f"<span style='background:{bg}; color:{fg}; padding:2px 9px; "
f"border-radius:5px; font-weight:700; font-size:0.82em; "
f"border:1px solid {border}; white-space:nowrap;'>"
f"⚡ {sym}</span>"
)
with news_tab1:
col_s1, col_s2, col_s3 = st.columns([2, 1, 1])
search_news = col_s1.text_input("🔍 Search Alerts:", placeholder="e.g. ICICIBANK, circuit...", key="global_news_search")
time_filter = col_s2.selectbox("⏳ Time Filter:", ["All (Up to 15 Days)", "Past 7 Days", "Today Only"], key="global_news_time")
sort_order = col_s3.radio("↕️ Sort By Time:", ["Newest First", "Oldest First"], horizontal=True, key="global_news_sort")
display_news = master_alerts_list.copy()
if search_news:
sq = search_news.lower()
display_news = [n for n in display_news if sq in n['symbol'].lower() or sq in n['title_raw'].lower()]
if time_filter == "Today Only":
display_news = [n for n in display_news if "min" in n['time_ago'] or "hour" in n['time_ago'] or "sec" in n['time_ago'] or "Just now" in n['time_ago']]
elif time_filter == "Past 7 Days":
now_utc = pd.Timestamp.now(tz='UTC')
display_news = [n for n in display_news if (now_utc - n['timestamp']).total_seconds() / 86400 <= 7.0]
display_news.sort(key=lambda x: x["timestamp"], reverse=(sort_order == "Newest First"))
st.markdown("<br>", unsafe_allow_html=True)
if display_news:
for news in display_news:
is_today = "min" in news['time_ago'] or "hour" in news['time_ago'] or "sec" in news['time_ago'] or "Just now" in news['time_ago']
time_color  = "
time_weight = "bold"    if is_today else "normal"
badge = symbol_badge(news['symbol'])
st.markdown(
f"- {badge}&nbsp; <a href='{news['link']}' target='_blank' "
f"style='text-decoration: none; color: inherit;'>{news['display_title']}</a> "
f"<span style='color: {time_color}; font-weight: {time_weight}; font-size: 0.85em;'>"
f"— 🕒 {news['time_ago']}</span>",
unsafe_allow_html=True
)
st.markdown("<hr style='margin: 0.4em 0; opacity: 0.15;'>", unsafe_allow_html=True)
else:
st.info("No circuit or 52-week alerts match your search or filter criteria.")
with news_tab2:
news_cols = st.columns(2)
idx_counter = 0
for clean_symbol in [str(s).strip() for s in filtered_symbols_alerts]:
sym_news = [n for n in master_alerts_list if n['symbol'] == clean_symbol]
sym_news.sort(key=lambda x: x["timestamp"], reverse=True)
if sym_news:
with news_cols[idx_counter % 2]:
exp_icon = "🟢" if clean_symbol in fresh_alerted_syms else "🟡"
with st.expander(f"{exp_icon} {clean_symbol} Action Alerts (0 Sec to 15 Days)", expanded=True):
top_3_news = sym_news[:3]
remaining_news = sym_news[3:]
for news in top_3_news:
is_today = "min" in news['time_ago'] or "hour" in news['time_ago'] or "sec" in news['time_ago'] or "Just now" in news['time_ago']
time_color = "
time_weight = "bold" if is_today else "normal"
st.markdown(f"- <a href='{news['link']}' target='_blank' style='text-decoration: none; color: inherit;'>{news['display_title']}</a> <span style='color: {time_color}; font-weight: {time_weight}; font-size: 0.85em;'>— 🕒 {news['time_ago']}</span>", unsafe_allow_html=True)
if remaining_news:
with st.expander(f"🔽 Show {len(remaining_news)} more older alerts", expanded=False):
for news in remaining_news:
is_today = "min" in news['time_ago'] or "hour" in news['time_ago'] or "sec" in news['time_ago'] or "Just now" in news['time_ago']
time_color = "
time_weight = "bold" if is_today else "normal"
st.markdown(f"- <a href='{news['link']}' target='_blank' style='text-decoration: none; color: inherit;'>{news['display_title']}</a> <span style='color: {time_color}; font-weight: {time_weight}; font-size: 0.85em;'>— 🕒 {news['time_ago']}</span>", unsafe_allow_html=True)
idx_counter += 1
if idx_counter == 0:
st.info("No circuit breakouts or 52-week boundary alerts for the currently filtered stocks in the last 15 days.")
with news_tab3:
st.markdown("
news_cols_3 = st.columns(2)
idx_counter_3 = 0
for symbol in filtered_symbols_full[:10]:
clean_symbol = str(symbol).strip()
news_items = fetch_all_stock_news_tab3(clean_symbol, limit=5)
if news_items:
with news_cols_3[idx_counter_3 % 2]:
with st.expander(f"📰 {clean_symbol} News Feed (0 Sec to 1 Day)", expanded=True):
for news in news_items:
is_today = "min" in news['time_ago'] or "hour" in news['time_ago'] or "sec" in news['time_ago'] or "Just now" in news['time_ago']
time_color = "
time_weight = "bold" if is_today else "normal"
st.markdown(f"- <a href='{news['link']}' target='_blank' style='text-decoration: none; color: inherit;'>{news['display_title']}</a> <span style='color: {time_color}; font-weight: {time_weight}; font-size: 0.85em;'>— 🕒 {news['time_ago']}</span>", unsafe_allow_html=True)
idx_counter_3 += 1
if idx_counter_3 == 0:
st.info("No general news found for the currently filtered stocks in the last 24 hours.")
with news_tab4:
st.markdown("
news_cols_4 = st.columns(2)
idx_counter_4 = 0
for symbol in filtered_symbols_full[:10]:
clean_symbol = str(symbol).strip()
news_items = fetch_all_stock_news_tab4(clean_symbol, limit=6)
if news_items:
with news_cols_4[idx_counter_4 % 2]:
with st.expander(f"📰 {clean_symbol} News Feed (All News)", expanded=True):
top_3_news4     = news_items[:3]
remaining_news4 = news_items[3:]
for news in top_3_news4:
is_today = "min" in news['time_ago'] or "hour" in news['time_ago'] or "sec" in news['time_ago'] or "Just now" in news['time_ago']
time_color = "
time_weight = "bold" if is_today else "normal"
st.markdown(f"- <a href='{news['link']}' target='_blank' style='text-decoration: none; color: inherit;'>{news['display_title']}</a> <span style='color: {time_color}; font-weight: {time_weight}; font-size: 0.85em;'>— 🕒 {news['time_ago']}</span>", unsafe_allow_html=True)
if remaining_news4:
with st.expander(f"🔽 Show {len(remaining_news4)} more articles", expanded=False):
for news in remaining_news4:
is_today = "min" in news['time_ago'] or "hour" in news['time_ago'] or "sec" in news['time_ago'] or "Just now" in news['time_ago']
time_color = "
time_weight = "bold" if is_today else "normal"
st.markdown(f"- <a href='{news['link']}' target='_blank' style='text-decoration: none; color: inherit;'>{news['display_title']}</a> <span style='color: {time_color}; font-weight: {time_weight}; font-size: 0.85em;'>— 🕒 {news['time_ago']}</span>", unsafe_allow_html=True)
idx_counter_4 += 1
if idx_counter_4 == 0:
st.info("No general news found for the currently filtered stocks.")
with news_tab5:
st.markdown("
st.markdown("<span style='font-size: 0.9em; color: gray;'>Tracks Regulation 30, LODR, Board Meetings, AGMs, and Analyst Meets.</span>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
news_cols_5 = st.columns(2)
idx_counter_5 = 0
for symbol in filtered_symbols_full[:15]:
clean_symbol = str(symbol).strip()
announcement_items = fetch_corporate_announcements(clean_symbol, limit=7)
if announcement_items:
with news_cols_5[idx_counter_5 % 2]:
with st.expander(f"📢 {clean_symbol} Filings & Announcements", expanded=True):
top_3_ann     = announcement_items[:3]
remaining_ann = announcement_items[3:]
for announcement in top_3_ann:
is_today = "min" in announcement['time_ago'] or "hour" in announcement['time_ago'] or "sec" in announcement['time_ago'] or "Just now" in announcement['time_ago']
time_color = "
time_weight = "bold" if is_today else "normal"
st.markdown(f"- <a href='{announcement['link']}' target='_blank' style='text-decoration: none; color: inherit;'>{announcement['display_title']}</a> <span style='color: {time_color}; font-weight: {time_weight}; font-size: 0.85em;'>— 🕒 {announcement['time_ago']}</span>", unsafe_allow_html=True)
if remaining_ann:
with st.expander(f"🔽 Show {len(remaining_ann)} more filings", expanded=False):
for announcement in remaining_ann:
is_today = "min" in announcement['time_ago'] or "hour" in announcement['time_ago'] or "sec" in announcement['time_ago'] or "Just now" in announcement['time_ago']
time_color = "
time_weight = "bold" if is_today else "normal"
st.markdown(f"- <a href='{announcement['link']}' target='_blank' style='text-decoration: none; color: inherit;'>{announcement['display_title']}</a> <span style='color: {time_color}; font-weight: {time_weight}; font-size: 0.85em;'>— 🕒 {announcement['time_ago']}</span>", unsafe_allow_html=True)
idx_counter_5 += 1
if idx_counter_5 == 0:
st.info("No recent corporate filings or official announcements found for the filtered stocks.")
with news_tab6:
st.markdown("
st.markdown("<span style='font-size:0.88em; color:
st.markdown("<br>", unsafe_allow_html=True)
ctrl1, ctrl2, ctrl3 = st.columns([3, 1.2, 1.2])
with ctrl1:
all_doc_syms = [str(s).strip() for s in filtered_symbols_full[:60]]
selected_doc_stocks = st.multiselect("🔍 Stocks to view:", options=all_doc_syms, default=all_doc_syms[:4], key="doc_hub_stocks_v2")
with ctrl2:
doc_days_label = st.selectbox("📅 Date range:", ["30 Days", "90 Days", "180 Days", "1 Year"], index=1, key="doc_days_v2")
with ctrl3:
doc_ann_limit = st.selectbox("📋 Rows per section:", [3, 5, 8, 12], index=1, key="doc_limit_v2")
days_map = {"30 Days": 30, "90 Days": 90, "180 Days": 180, "1 Year": 365}
doc_days_back = days_map[doc_days_label]
if not selected_doc_stocks:
st.info("Select at least one stock above to view its documents.")
else:
for doc_sym in selected_doc_stocks:
bse_code = BSE_CODE_MAP.get(doc_sym.upper(), "")
with st.expander(f"📁  {doc_sym}   {'· BSE ' + bse_code if bse_code else '· BSE code not mapped — Screener links shown'}", expanded=True):
btn_html = "<div style='display:flex; flex-wrap:wrap; gap:8px; margin-bottom:14px;'>"
btn_links = [
("📢 BSE Announcements",
f"https://www.bseindia.com/corporates/Corp_Annoucement.html?expandable=0&scripcd={bse_code}" if bse_code else f"https://www.nseindia.com/companies-listing/corporate-filings-announcements?symbol={doc_sym}",
"
("📑 Annual Reports",   f"https://www.screener.in/company/{doc_sym}/", "
("⭐ Credit Ratings",   f"https://www.screener.in/company/{doc_sym}/", "
("🎙️ Concalls",         f"https://www.screener.in/company/{doc_sym}/", "
("📊 Investor PPT",
f"https://www.bseindia.com/corporates/Inv_Rel.aspx?scripcd={bse_code}" if bse_code else f"https://www.screener.in/company/{doc_sym}/",
"
("🏛️ NSE Filings",      f"https://www.nseindia.com/companies-listing/corporate-filings-announcements?symbol={doc_sym}", "
("📈 Screener",         f"https://www.screener.in/company/{doc_sym}/", "
]
for label, href, bg, fg in btn_links:
btn_html += f"<a href='{href}' target='_blank' style='background:{bg}; color:{fg}; padding:5px 12px; border-radius:6px; font-size:0.78em; font-weight:600; text-decoration:none; white-space:nowrap;'>{label}</a>"
btn_html += "</div>"
st.markdown(btn_html, unsafe_allow_html=True)
docs_data = {}
if bse_code:
with st.spinner(f"Fetching BSE filings for {doc_sym}…"):
docs_data = fetch_bse_all_documents(bse_code, days_back=doc_days_back)
c_ann, c_ar, c_cr, c_cc = st.columns([3, 2, 2, 3])
with c_ann:
st.markdown("<p style='font-weight:700; font-size:0.9em; border-bottom:2px solid
ann_items = docs_data.get("announcements", [])
if ann_items:
subtab_recent, subtab_all = st.tabs(["Recent", "All ↗"])
with subtab_recent:
for a in ann_items[:doc_ann_limit]:
title_short = (a["title"][:85] + "…") if len(a["title"]) > 85 else a["title"]
link_part = (f"<a href='{a['link']}' target='_blank' style='color:
st.markdown(f"<div style='font-size:0.82em; margin-bottom:6px; border-left:3px solid
with subtab_all:
full_url = (f"https://www.bseindia.com/corporates/Corp_Annoucement.html?expandable=0&scripcd={bse_code}" if bse_code else f"https://www.nseindia.com/companies-listing/corporate-filings-announcements?symbol={doc_sym}")
st.markdown(f"<a href='{full_url}' target='_blank' style='color:
else:
bse_url = (f"https://www.bseindia.com/corporates/Corp_Annoucement.html?expandable=0&scripcd={bse_code}" if bse_code else f"https://www.nseindia.com/companies-listing/corporate-filings-announcements?symbol={doc_sym}")
st.markdown(f"<a href='{bse_url}' target='_blank' style='color:
st.caption("No announcements in selected date range.")
with c_ar:
st.markdown("<p style='font-weight:700; font-size:0.9em; border-bottom:2px solid
ar_items = docs_data.get("annual_reports", [])
if ar_items:
for ar in ar_items[:6]:
yr = ar["date"][:4] if ar["date"] else "Report"
link_part = (f"<a href='{ar['link']}' target='_blank' style='color:
st.markdown(f"<div style='font-size:0.82em; margin-bottom:5px;'>{link_part}</div>", unsafe_allow_html=True)
else:
if bse_code:
st.markdown(f"<a href='https://www.bseindia.com/AnnualReports.html?scripcd={bse_code}' target='_blank' style='color:
st.markdown(f"<a href='https://www.screener.in/company/{doc_sym}/' target='_blank' style='color:
st.caption("Not found in selected range — try 1 Year.")
with c_cr:
st.markdown("<p style='font-weight:700; font-size:0.9em; border-bottom:2px solid
cr_items = docs_data.get("credit_ratings", [])
if cr_items:
for cr in cr_items[:4]:
title_short = (cr["title"][:70] + "…") if len(cr["title"]) > 70 else cr["title"]
link_part = (f"<a href='{cr['link']}' target='_blank' style='color:
st.markdown(f"<div style='font-size:0.82em; margin-bottom:5px; border-left:3px solid
else:
st.markdown(f"<a href='https://www.screener.in/company/{doc_sym}/' target='_blank' style='color:
st.markdown("<div style='font-size:0.78em; margin-top:8px; color:
st.caption("Not found via BSE — check links above.")
with c_cc:
st.markdown("<p style='font-weight:700; font-size:0.9em; border-bottom:2px solid
concall_items = docs_data.get("concalls", [])
ppt_items = docs_data.get("ppt", [])
combined = ppt_items + concall_items
if combined:
for item in combined[:doc_ann_limit]:
is_ppt = item in ppt_items
icon = "📊" if is_ppt else "🎙️"
title_short = (item["title"][:70] + "…") if len(item["title"]) > 70 else item["title"]
link_part = (f"<a href='{item['link']}' target='_blank' style='color:
st.markdown(f"<div style='font-size:0.82em; margin-bottom:5px; border-left:3px solid
else:
st.markdown(f"<a href='https://www.screener.in/company/{doc_sym}/' target='_blank' style='color:
st.caption("No concalls/PPT in selected date range.")
st.markdown("<br>", unsafe_allow_html=True)
badges_html = "<div style='display:flex; gap:6px; flex-wrap:wrap;'>"
badges = [
("📝 Transcript", f"https://www.screener.in/company/{doc_sym}/", "
("🤖 AI Summary",  f"https://www.screener.in/company/{doc_sym}/", "
("📊 PPT",         f"https://www.bseindia.com/corporates/Inv_Rel.aspx?scripcd={bse_code}" if bse_code else f"https://www.screener.in/company/{doc_sym}/", "
("▶️ REC",          f"https://www.youtube.com/results?search_query={doc_sym}+concall+earnings", "
]
for label, href, bg, fg in badges:
badges_html += f"<a href='{href}' target='_blank' style='background:{bg}; color:{fg}; padding:3px 10px; border-radius:4px; font-size:0.76em; font-weight:600; text-decoration:none;'>{label}</a>"
badges_html += "</div>"
st.markdown(badges_html, unsafe_allow_html=True)
with news_tab7:
st.markdown("
st.markdown(
"<span style='font-size:0.88em; color:
"constant near the top of the .py file to change anything shown below — same pattern as the "
"AI Prompt Library &amp; Pine Script Custom Rules Library.</span>",
unsafe_allow_html=True
)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(TRADING_RULES_LIBRARY)
else:
st.info("No stocks currently filtered to check.")
except Exception as e:
st.error(f"⚠️ Could not load the News Engine. Error details: {e}")
else:
st.warning("No data loaded. Check sheet sharing and secrets.")
