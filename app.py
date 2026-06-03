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

# ==========================================
# ⚙️ PAGE CONFIGURATION
# ==========================================
st.set_page_config(page_title="Top 250 NSE Stock-Volume Breakout Dashboard", layout="wide", page_icon="📊")

# ==========================================
# 🤖 CONFIGURE AI (GEMINI)
# ==========================================
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    ai_enabled = True
else:
    ai_enabled = False

# ==========================================
# 🛡️ HIDE STREAMLIT MENU & GITHUB ICON
# ==========================================
hide_streamlit_ui = """
<style>
    /* Hides the top-right menu (hamburger menu) */
    #MainMenu {visibility: hidden;}
    /* Hides the header containing the GitHub icon and Deploy button */
    header {visibility: hidden;}
    /* Hides the toolbar specifically */
    [data-testid="stToolbar"] {visibility: hidden;}
    /* Hides the footer (optional, removes 'Made with Streamlit') */
    footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_ui, unsafe_allow_html=True)

# ==========================================
# 🔐 ADMIN LOGIN SYSTEM
# ==========================================
ADMIN_PASSWORD = "dada"

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
st.title("📊 Top 250 NSE Stock-Volume Breakout Dashboard")
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
        service_account_info = json.loads(st.secrets["gcp_service_account"])
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_info(service_account_info, scopes=scope)
        client = gspread.authorize(creds)

        spreadsheet_id = "1SFhuZbLLlwwFsNo1k2RRx_Zp6bAkRR20W0F_zTwgdwU"
        encoded_sheet = urllib.parse.quote(sheet_name)

        authed_session = AuthorizedSession(creds)
        url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}?includeGridData=true&ranges={encoded_sheet}"
        response = authed_session.get(url)
        data = response.json()

        if 'error' in data or 'sheets' not in data: return pd.DataFrame()

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
        df = pd.DataFrame(values_list[1:], columns=raw_headers)
        return df
    except Exception as e:
        st.error(f"DEBUG ERROR: {e}") # This will show the real problem on your page
        return pd.DataFrame()

def process_hyperlinks(df, symbol_col):
    df_proc = df.copy()
    df_proc['_raw_symbol_'] = df_proc[symbol_col]
    for idx, row in df_proc.iterrows():
        sym = str(row['_raw_symbol_']).strip()
        if not sym or sym == "nan": continue
        for col in df_proc.columns:
            if col in ["_raw_symbol_"]: continue
            c_lower = col.lower()
            url = None
            if "trading view" in c_lower: url = f"https://www.tradingview.com/symbols/{sym}/"
            elif "screener" in c_lower: url = f"https://www.screener.in/company/{sym}"
            elif "zerodha" in c_lower: url = f"https://zerodha.com/markets/stocks/NSE/{sym}"
            elif "nse" in c_lower: url = f"https://charting.nseindia.com/?symbol={sym}-EQ"
            
            if url: df_proc.at[idx, col] = f'<a href="{url}" target="_blank">{row[col]}</a>'
    return df_proc

def apply_numeric_slider(df, col_name, st_container):
    if col_name in df.columns:
        num_series = pd.to_numeric(df[col_name].astype(str).str.replace(r'[%,]', '', regex=True), errors='coerce')
        valid = num_series.dropna()
        if not valid.empty:
            s_range = st_container.slider(f"{col_name} Range:", float(valid.min()), float(valid.max()), (float(valid.min()), float(valid.max())))
            return df[(num_series >= s_range[0]) & (num_series <= s_range[1])]
    return df

def clean_for_export(df):
    export_df = df.copy()
    cols_to_drop = [c for c in export_df.columns if c.startswith("_bg_") or c.startswith("_txt_") or c == "_raw_symbol_"]
    export_df = export_df.drop(columns=cols_to_drop, errors='ignore')
    for col in export_df.select_dtypes(include=['object']).columns:
        export_df[col] = export_df[col].apply(lambda x: re.sub(r'<[^>]*>', '', str(x)) if pd.notnull(x) else x)
    return export_df

# ==========================================
# 📑 SIDEBAR
# ==========================================
sheet_names = ["Top 250 Stocks", "Final List", "Final List 2", "Diff @ 200 DMA", "+%", "-%"]
selected_sheet = st.sidebar.selectbox("Choose sheet", sheet_names)
search_query = st.sidebar.text_input("Global Search")

# ---------- Data Processing ----------
raw_df = load_sheet_data_with_colors(selected_sheet)
if not raw_df.empty:
    actual_cols = [c for c in raw_df.columns if not c.startswith("_")]
    filtered_df = raw_df.copy()
    
    # Simple Filters
    if search_query:
        filtered_df = filtered_df[filtered_df.apply(lambda row: row.astype(str).str.contains(search_query, case=False).any(), axis=1)]

    # ==========================================
    # 📌 TOP UI: LAYOUT FIXES
    # ==========================================
    st.markdown("---")
    top_col1, top_col2 = st.columns([4, 1])
    
    with top_col1:
        st.write(f"**Rows:** {filtered_df.shape[0]} | **Columns:** {len(actual_cols)}") 
        
    with top_col2:
        st.markdown("<div style='margin-top: -20px;'></div>", unsafe_allow_html=True) # Adjust alignment
        export_df = clean_for_export(filtered_df)
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            export_df.to_excel(writer, index=False)
        st.download_button("📥 Download as Excel", data=buffer.getvalue(), file_name=f"{selected_sheet}.xlsx", use_container_width=False)

    url_placeholder = st.empty()

    # ==========================================
    # 🎨 AG GRID
    # ==========================================
    gb = GridOptionsBuilder.from_dataframe(filtered_df)
    gb.configure_selection(selection_mode="single", use_checkbox=True)
    grid_options = gb.build()
    
    grid_response = AgGrid(filtered_df, gridOptions=grid_options, allow_unsafe_jscode=True, height=400)

    # ==========================================
    # 🛠️ WORKSPACE TABS
    # ==========================================
    selected_rows = grid_response.get("selected_rows", [])
    if selected_rows is not None and len(selected_rows) > 0:
        sel_row = selected_rows.iloc[0] if isinstance(selected_rows, pd.DataFrame) else selected_rows[0]
        sym = str(sel_row.get(next((c for c in actual_cols if "symbol" in c.lower()), actual_cols[0]), "")).strip()

        if sym:
            ws_tabs = st.tabs(["📈 Chart", "🤖 AI Analysis", "💻 AI Pine Script Builder"])
            
            with ws_tabs[0]:
                components.html(f'<iframe src="https://www.tradingview.com/chart/?symbol=NSE:{sym}" width="100%" height="500"></iframe>', height=520)

            with ws_tabs[1]:
                st.markdown(f"### 🤖 Ask Gemini About **{sym}**")
                ai_query = st.text_area("Your Query:", value=f"Analyze {sym} technicals.", height=80)
                if st.button("✨ Generate AI Analysis"):
                    model = genai.GenerativeModel('gemini-2.5-flash')
                    response = model.generate_content(f"Analyze {sym} using this data: {sel_row.to_dict()}. {ai_query}")
                    st.info(response.text)

            with ws_tabs[2]:
                st.markdown(f"### 💻 AI Pine Script Generator")
                strategy_focus = st.selectbox("Select Strategy:", ["Volume Breakout", "Reversal from 52-Week Low", "EMA Cross"])
                if st.button("⚙️ Generate Pine Script V5"):
                    model = genai.GenerativeModel('gemini-2.5-flash')
                    prompt = f"""
                    Write a Pine Script V5 strategy for {sym}. 
                    Focus: {strategy_focus}.
                    Rules: 
                    1. Use strategy("Name", overlay=true, commission_type=strategy.commission.percent, commission_value=0.01).
                    2. Include Volume, EMA Cross, RSI(14), SuperTrend, and PVT.
                    3. No conversational text, just code.
                    """
                    response = model.generate_content(prompt)
                    st.markdown(response.text)

else:
    st.warning("No data loaded.")
