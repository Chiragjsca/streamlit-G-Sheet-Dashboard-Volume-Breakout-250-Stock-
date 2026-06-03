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
# 🔐 ADMIN LOGIN
# ==========================================
ADMIN_PASSWORD = "dada"
if "logged_in" not in st.session_state: st.session_state.logged_in = False
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align: center; margin-top: 100px;'>🔐 Admin Login</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        with st.form("login_form"):
            pwd = st.text_input("Enter Password", type="password")
            if st.form_submit_button("Login", use_container_width=True):
                if pwd == ADMIN_PASSWORD:
                    st.session_state.logged_in = True
                    st.rerun()
    st.stop() 

# ==========================================
# 🌍 MARKET TICKER
# ==========================================
st.title("📊 Top 250 NSE Stock-Volume Breakout Dashboard")
st.caption(f"Data refreshed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# ==========================================
# 🛠️ HELPER FUNCTIONS
# ==========================================
def rgb_to_hex(color_dict):
    if not color_dict: return "#ffffff"
    return f"#{int(color_dict.get('red', 0) * 255):02x}{int(color_dict.get('green', 0) * 255):02x}{int(color_dict.get('blue', 0) * 255):02x}"

@st.cache_data(ttl=300)
def load_sheet_data_with_colors(sheet_name):
    try:
        # FIXED: AttrDict conversion logic
        secret = st.secrets["gcp_service_account"]
        service_account_info = dict(secret) if isinstance(secret, dict) else json.loads(secret)
        
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_info(service_account_info, scopes=scope)
        
        spreadsheet_id = "1SFhuZbLLlwwFsNo1k2RRx_Zp6bAkRR20W0F_zTwgdwU"
        authed_session = AuthorizedSession(creds)
        url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}?includeGridData=true&ranges={urllib.parse.quote(sheet_name)}"
        response = authed_session.get(url)
        data = response.json()

        sheet_data = data['sheets'][0]['data'][0]
        row_data = sheet_data.get('rowData', [])
        
        values_list = []
        for row in row_data:
            cells = row.get('values', [])
            values_list.append([cell.get('formattedValue', '') for cell in cells])
            
        return pd.DataFrame(values_list[1:], columns=values_list[0])
    except Exception as e:
        st.error(f"Sheet Load Error: {e}")
        return pd.DataFrame()

def clean_for_export(df):
    return df.applymap(lambda x: re.sub(r'<[^>]*>', '', str(x)) if pd.notnull(x) else x)

# ==========================================
# 📑 APP UI
# ==========================================
sheet_names = ["Top 250 Stocks", "Final List", "Final List 2", "Diff @ 200 DMA", "+%", "-%"]
selected_sheet = st.sidebar.selectbox("Choose sheet", sheet_names)
raw_df = load_sheet_data_with_colors(selected_sheet)

if not raw_df.empty:
    # 📌 TOP LAYOUT: Button on right
    top1, top2 = st.columns([4, 1])
    with top1:
        st.write(f"**Total Rows:** {len(raw_df)}")
    with top2:
        # Pushing button slightly down to align with text
        st.markdown("<div style='margin-top: -15px;'></div>", unsafe_allow_html=True)
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            clean_for_export(raw_df).to_excel(writer, index=False)
        st.download_button("📥 Download Excel", data=buffer.getvalue(), file_name=f"{selected_sheet}.xlsx", use_container_width=True)

    # 🎨 AG GRID
    gb = GridOptionsBuilder.from_dataframe(raw_df)
    gb.configure_selection(selection_mode="single", use_checkbox=True)
    grid_response = AgGrid(raw_df, gridOptions=gb.build(), allow_unsafe_jscode=True, height=400)

    # 🛠️ WORKSPACE
    selected_rows = grid_response.get("selected_rows", [])
    if selected_rows is not None and len(selected_rows) > 0:
        sel_row = selected_rows.iloc[0] if isinstance(selected_rows, pd.DataFrame) else selected_rows[0]
        sym = str(sel_row.get(next((c for c in raw_df.columns if "symbol" in c.lower()), raw_df.columns[0]), "")).strip()
        
        st.subheader(f"Workspace: {sym}")
        tab1, tab2, tab3 = st.tabs(["📈 Chart", "🤖 AI Analysis", "💻 Pine Script Builder"])
        
        with tab1:
            components.html(f'<iframe src="https://www.tradingview.com/chart/?symbol=NSE:{sym}" width="100%" height="500"></iframe>', height=520)
            
        with tab2:
            if st.button("✨ Generate AI Analysis"):
                model = genai.GenerativeModel('gemini-2.0-flash')
                resp = model.generate_content(f"Analyze {sym} data: {sel_row.to_dict()}")
                st.info(resp.text)
                
        with tab3:
            focus = st.selectbox("Select Strategy", ["Volume Breakout", "52W Low Reversal"])
            if st.button("⚙️ Generate Script"):
                model = genai.GenerativeModel('gemini-2.0-flash')
                resp = model.generate_content(f"Write a V5 Pine Script for {sym} focusing on {focus}. Include commission setup.")
                st.code(resp.text, language='pinescript')

else:
    st.warning("No data found. Please check Google Sheet connection.")
