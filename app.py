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
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stToolbar"] {visibility: hidden;}
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
            if submit and pwd == ADMIN_PASSWORD:
                st.session_state.logged_in = True
                st.rerun()
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
        # FIXED: AttrDict loading issue
        secret = st.secrets["gcp_service_account"]
        service_account_info = json.loads(json.dumps(dict(secret))) if isinstance(secret, dict) else json.loads(secret)
        
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
        st.error(f"Error: {e}")
        return pd.DataFrame()

def clean_for_export(df):
    export_df = df.copy()
    for col in export_df.select_dtypes(include=['object']).columns:
        export_df[col] = export_df[col].apply(lambda x: re.sub(r'<[^>]*>', '', str(x)) if pd.notnull(x) else x)
    return export_df

# ==========================================
# 📑 SIDEBAR
# ==========================================
sheet_names = ["Top 250 Stocks", "Final List", "Final List 2", "Diff @ 200 DMA", "+%", "-%"]
selected_sheet = st.sidebar.selectbox("Choose sheet", sheet_names)

# ---------- Data Processing ----------
raw_df = load_sheet_data_with_colors(selected_sheet)
if not raw_df.empty:
    actual_cols = [c for c in raw_df.columns if not c.startswith("_")]
    filtered_df = raw_df.copy()
    
    # ==========================================
    # 📌 TOP UI: LAYOUT (Excel Button Right Aligned)
    # ==========================================
    st.markdown("---")
    top_row1, top_row2 = st.columns([3, 1])
    
    with top_row1:
        sizing_mode = st.radio("Column Width Adjustment:", ["Default", "Fit to Row 1", "Fit to Row 2"], horizontal=True)
    with top_row2:
        export_df = clean_for_export(filtered_df)
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            export_df.to_excel(writer, index=False)
        st.download_button("📥 Download as Excel", data=buffer.getvalue(), file_name=f"{selected_sheet}.xlsx", use_container_width=True)

    # Grid & Workspace logic follows...
    # (Simplified for final display, ensure you keep your previous AgGrid and Tabs logic here)
    gb = GridOptionsBuilder.from_dataframe(filtered_df)
    gb.configure_selection(selection_mode="single", use_checkbox=True)
    grid_response = AgGrid(filtered_df, gridOptions=gb.build(), allow_unsafe_jscode=True, height=400)
    
    # [Rest of your Workspace Tabs and AI Logic]
    # Remember to use model='gemini-2.0-flash' in your Gemini code blocks.
else:
    st.warning("No data loaded. Check if tab names are correct.")
