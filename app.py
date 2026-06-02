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

# ==========================================
# ⚙️ PAGE CONFIGURATION
# ==========================================
st.set_page_config(page_title="NSE Stock Dashboard", layout="wide", page_icon="📊")

# ==========================================
# 🔐 ADMIN LOGIN SYSTEM
# ==========================================
ADMIN_PASSWORD = "admin"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align: center; margin-top: 100px;'>🔐 Admin Login</h1>", unsafe_allow_html=True)
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
                    st.error("❌ Incorrect Password. Please try again.")
    st.stop() 

# ==========================================
# 🌍 GLOBAL MARKET TICKER (TRADINGVIEW)
# ==========================================
st.title("📊 NSE Stock Market Dashboard")
st.caption(f"Data refreshed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

components.html("""
<div class="tradingview-widget-container">
  <div class="tradingview-widget-container__widget"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>
  {
  "symbols": [
    {"proName": "NSE:NIFTY", "title": "Nifty 50"},
    {"proName": "NSE:BANKNIFTY", "title": "Bank Nifty"},
    {"proName": "BSE:SENSEX", "title": "Sensex"},
    {"proName": "NSE:CNXIT", "title": "Nifty IT"},
    {"proName": "NSE:CNXAUTO", "title": "Nifty Auto"}
  ],
  "showSymbolLogo": true,
  "isTransparent": true,
  "displayMode": "adaptive",
  "colorTheme": "dark",
  "locale": "en"
}
  </script>
</div>
""", height=70)

# ==========================================
# 🛠️ HELPER FUNCTIONS
# ==========================================
def rgb_to_hex(color_dict):
    if not color_dict: return "#ffffff"
    r, g, b = int(color_dict.get('red', 0) * 255), int(color_dict.get('green', 0) * 255), int(color_dict.get('blue', 0) * 255)
    return f"#{r:02x}{g:02x}{b:02x}"

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
            
            if "trading view" in c_lower: url, label = f"https://www.tradingview.com/symbols/{sym}", f"Tre {sym}" if not c_lower.endswith("1") else "🔗 Link"
            elif "history data" in c_lower: url, label = f"https://www.equitypandit.com/historical-data/{sym}", f"History {sym}" if not c_lower.endswith("1") else "🔗 Link"
            elif "screener" in c_lower: url, label = f"https://www.screener.in/company/{sym}", f"Scr {sym}" if not c_lower.endswith("1") else "🔗 Link"
            elif "zerodha" in c_lower: url, label = f"https://zerodha.com/markets/stocks/NSE/{sym}", f"🪁 {sym}" if not c_lower.endswith("1") else "🔗 Link"
            elif "chartlink" in c_lower: url, label = f"https://chartink.com/stocks-new?load-snapshot=exponential-moving-average-simple-moving-average-simple-moving-average-moving-average-convergence-divergence-chart-snapshot-175&symbol={sym}", f"CL {sym}" if not c_lower.endswith("1") else "🔗 Link"
            elif "market smith" in c_lower: url, label = f"https://marketsmithindia.com/mstool/eval/{sym}/evaluation.jsp", f"ms {sym}" if not c_lower.endswith("1") else "🔗 Link"
            elif "official nse" in c_lower: url, label = f"https://www.nseindia.com/get-quotes/equity?symbol={sym}", f"nse📰 {sym}" if not c_lower.endswith("1") else "🔗 Link"
            elif "nse" in c_lower: url, label = f"https://charting.nseindia.com/?symbol={sym}-EQ", f"nse {sym}" if not c_lower.endswith("1") else "🔗 Link"
                
            if url: df_proc.at[idx, col] = f'<a href="{url}" target="_blank" style="text-decoration:none; color:inherit;">{label}</a>'
                
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

# ==========================================
# 📑 SIDEBAR CONTROLS 
# ==========================================
if st.sidebar.button("🧹 Clear All Filters", use_container_width=True):
    for key in list(st.session_state.keys()):
        if key.startswith("filter_") or key == "search_query": del st.session_state[key]
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.header("🔍 Global Search")
search_query = st.sidebar.text_input("Search by Symbol, Name, etc...", key="search_query")

st.sidebar.markdown("---")
st.sidebar.header("📑 Select a Tab")
sheet_names = ["Top 250 Stocks", "Final List", "Final List 2", "Diff @ 200 DMA", "+%", "-%"]
selected_sheet = st.sidebar.selectbox("Choose sheet", sheet_names, key="filter_sheet")

# ---------- Main Execution ----------
st.header(f"📄 {selected_sheet}")

with st.spinner("Downloading data from Google API..."):
    raw_df = load_sheet_data_with_colors(selected_sheet)

if not raw_df.empty:
    
    guess_idx = 0
    actual_cols = [c for c in raw_df.columns if not c.startswith("_bg_") and not c.startswith("_txt_")]
    
    for i, col_name in enumerate(actual_cols):
        if col_name.lower() in ["nse code", "symbol", "ticker", "stock symbol", "id", "stock"]:
            guess_idx = i
            break
            
    st.sidebar.markdown("---")
    st.sidebar.header("⚙️ Settings")
    selected_symbol_col = st.sidebar.selectbox("Symbol Column:", actual_cols, index=guess_idx, key="filter_symbol_col")
    
    final_df = process_hyperlinks(raw_df, selected_symbol_col)
    filtered_df = final_df.copy()

    # 1. Search Bar Filter
    if search_query:
        mask = filtered_df[actual_cols].astype(str).apply(lambda x: x.str.contains(search_query, case=False, na=False)).any(axis=1)
        filtered_df = filtered_df[mask]

    # 2. Categorical Filters
    st.sidebar.markdown("---")
    st.sidebar.header("🎯 Categorical Filters")
    active_filters = [c for c in actual_cols if any(key in c.lower() for key in ["cumulative average", "industry", "sector", "output", "start gtt order"])]
    for col_to_filter in active_filters:
        unique_options = sorted([val for val in final_df[col_to
