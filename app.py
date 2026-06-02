import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from google.auth.transport.requests import AuthorizedSession
import json
import urllib.parse
from datetime import datetime
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode
from st_aggrid.shared import GridUpdateMode

# ---------- Page config ----------
st.set_page_config(page_title="NSE Stock Dashboard", layout="wide")
st.title("📊 NSE Stock Market Dashboard")
st.caption(f"Data refreshed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# ---------- Helper: Convert Google RGB to HEX ----------
def rgb_to_hex(color_dict):
    if not color_dict:
        return "#ffffff" # Default white
    r = int(color_dict.get('red', 0) * 255)
    g = int(color_dict.get('green', 0) * 255)
    b = int(color_dict.get('blue', 0) * 255)
    return f"#{r:02x}{g:02x}{b:02x}"

# ---------- Load Google Sheet (Values + Colors via API) ----------
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

        if 'error' in data:
            st.error(f"Google API Error: {data['error'].get('message', 'Unknown Error')}")
            return pd.DataFrame()

        if 'sheets' not in data or not data['sheets']:
            return pd.DataFrame()

        sheet_data = data['sheets'][0]['data'][0]
        row_data = sheet_data.get('rowData', [])

        if not row_data:
            return pd.DataFrame()

        values_list = []
        bg_colors_list = []
        txt_colors_list = []

        for row in row_data:
            cells = row.get('values', [])
            row_vals = []
            row_bgs = []
            row_txts = []
            
            for cell in cells:
                val = cell.get('formattedValue', '')
                row_vals.append(val)
                
                fmt = cell.get('effectiveFormat', {})
                bg = fmt.get('backgroundColor', {})
                txt = fmt.get('textFormat', {}).get('foregroundColor', {})
                
                row_bgs.append(rgb_to_hex(bg))
                row_txts.append(rgb_to_hex(txt))
                
            values_list.append(row_vals)
            bg_colors_list.append(row_bgs)
            txt_colors_list.append(row_txts)

        raw_headers = values_list[0]
        clean_headers = []
        seen = {}
        for h in raw_headers:
            h = str(h).strip()
            if h == "":
                h = "empty_column"
            if h in seen:
                seen[h] += 1
                h = f"{h}_{seen[h]}"
            else:
                seen[h] = 0
            clean_headers.append(h)

        df = pd.DataFrame(values_list[1:], columns=clean_headers)

        for i, col in enumerate(clean_headers):
            bg_col_name = f"_bg_{col}"
            txt_col_name = f"_txt_{col}"
            
            df[bg_col_name] = [row[i] if i < len(row) else "#ffffff" for row in bg_colors_list[1:]]
            df[txt_col_name] = [row[i] if i < len(row) else "#000000" for row in txt_colors_list[1:]]

        return df

    except Exception as e:
        st.error(f"Error loading sheet '{sheet_name}': {str(e)}")
        return pd.DataFrame()

# ---------- Process Hyperlinks Dynamically ----------
def process_hyperlinks(df, symbol_col):
    df_proc = df.copy()
    
    for idx, row in df_proc.iterrows():
        sym = str(row[symbol_col]).strip()
        if not sym or sym == "nan":
            continue
            
        for col in df_proc.columns:
            if col.startswith("_bg_") or col.startswith("_txt_"):
                continue
                
            c_lower = col.lower()
            url = None
            label = "🔗 Link"
            
            if "trading view" in c_lower:
                url = f"https://www.tradingview.com/symbols/{sym}"
                if not c_lower.endswith("1"): label = f"Tre {sym}"
            elif "history data" in c_lower:
                url = f"https://www.equitypandit.com/historical-data/{sym}"
                if not c_lower.endswith("1"): label = f"History {sym}"
            elif "screener" in c_lower:
                url = f"https://www.screener.in/company/{sym}"
                if not c_lower.endswith("1"): label = f"Scr {sym}"
            elif "zerodha" in c_lower:
                url = f"https://zerodha.com/markets/stocks/NSE/{sym}"
                if not c_lower.endswith("1"): label = f"🪁 {sym}"
            elif "chartlink" in c_lower:
                url = f"https://chartink.com/stocks-new?load-snapshot=exponential-moving-average-simple-moving-average-simple-moving-average-moving-average-convergence-divergence-chart-snapshot-175&symbol={sym}"
                if not c_lower.endswith("1"): label = f"CL {sym}"
            elif "market smith" in c_lower:
                url = f"https://marketsmithindia.com/mstool/eval/{sym}/evaluation.jsp"
                if not c_lower.endswith("1"): label = f"ms {sym}"
            elif "official nse" in c_lower:
                url = f"https://www.nseindia.com/get-quotes/equity?symbol={sym}"
                if not c_lower.endswith("1"): label = f"nse📰 {sym}"
            elif "nse" in c_lower:
                url = f"https://charting.nseindia.com/?symbol={sym}-EQ"
                if not c_lower.endswith("1"): label = f"nse {sym}"
                
            if url:
                df_proc.at[idx, col] = f'<a href="{url}" target="_blank" style="text-decoration:none; color:inherit;">{label}</a>'

    return df_proc

# ==========================================
# 📑 SIDEBAR CONTROLS (Top Left)
# ==========================================
st.sidebar.header("🔍 Global Search")
search_query = st.sidebar.text_input("Search by Symbol, Name, etc...")

st.sidebar.markdown("---")
st.sidebar.header("📑 Select a Tab")
sheet_names = ["Top 250 Stocks", "Final List", "Final List 2", "Diff @ 200 DMA", "+%", "-%"]
selected_sheet = st.sidebar.selectbox("Choose sheet", sheet_names)

# ---------- Main Execution ----------
st.header(f"📄 {selected_sheet}")

with st.spinner("Downloading data and exact colors from Google API..."):
    raw_df = load_sheet_data_with_colors(selected_sheet)

if not raw_df.empty:
    
    # Auto-detect Symbol column for hyperlinks
    guess_idx = 0
    actual_cols = [c for c in raw_df.columns if not c.startswith("_bg_") and not c.startswith("_txt_")]
    
    for i, col_name in enumerate(actual_cols):
        if col_name.lower() in ["nse code", "symbol", "ticker", "stock symbol", "id", "stock"]:
            guess_idx = i
            break
            
    st.sidebar.markdown("---")
    st.sidebar.header("⚙️ Settings")
    selected_symbol_col = st.sidebar.selectbox("Symbol Column:", actual_cols, index=guess_idx)
    
    final_df = process_hyperlinks(raw_df, selected_symbol_col)

    # ==========================================
    # 🔍 APPLY SEARCH & DROP DOWN FILTERS
    # ==========================================
    filtered_df = final_df.copy()

    # 1. Apply Top-Left Search Bar Filter
    if search_query:
        # Search across all visible columns (ignore hidden color columns)
        mask = filtered_df[actual_cols].astype(str).apply(lambda x: x.str.contains(search_query, case=False, na=False)).any(axis=1)
        filtered_df = filtered_df[mask]

    st.sidebar.markdown("---")
    st.sidebar.header("🎯 Drop Down Filters")
    
    # Identify specific columns you want to filter (Case-insensitive matching to find your specific columns)
    active_filters = []
    for c in actual_cols:
        c_lower = c.lower()
        if "cumulative average" in c_lower or "industry" in c_lower or "sector" in c_lower or "output" in c_lower or "start gtt order" in c_lower:
            active_filters.append(c)
    
    # 2. Apply Dropdown Filters
    for col_to_filter in active_filters:
        # Get unique values, ignoring empty strings
        unique_options = sorted([val for val in final_df[col_to_filter].unique() if str(val).strip() != ""])
        
        selected_options = st.sidebar.multiselect(f"Filter by {col_to_filter}:", options=unique_options)
        
        if selected_options:
            filtered_df = filtered_df[filtered_df[col_to_filter].isin(selected_options)]

    st.write(f"**Rows:** {filtered_df.shape[0]} | **Columns:** {len(actual_cols)}")

    # ==========================================
    # 🎨 EXACT COLOR REFLECTION & HTML LOGIC
    # ==========================================

    html_renderer = JsCode("""
    class HtmlRenderer {
        init(params) {
            this.eGui = document.createElement('span');
            this.eGui.innerHTML = params.value ? params.value : '';
        }
        getGui() {
            return this.eGui;
        }
    }
    """)

    exact_mirror_style = JsCode("""
    function(params) {
        let colName = params.colDef.field;
        let bgCol = "_bg_" + colName;
        let txtCol = "_txt_" + colName;
        
        let bgColor = params.data[bgCol];
        let txtColor = params.data[txtCol];
        
        if (!bgColor || bgColor.toLowerCase() === '#ffffff') {
            return null;
        }
        
        return {
            'backgroundColor': bgColor,
            'color': txtColor || '#000000',
            'fontWeight': (txtColor === '#ffffff' || bgColor === '#0f9d58') ? 'bold' : 'normal'
        };
    }
    """)

    gb = GridOptionsBuilder.from_dataframe(filtered_df)
    priority_columns_lower = ["nse code", "id", "company name", "stock name", "symbol", "industry", "sector"]

    # Tracking variable to freeze only the absolute first visible data column
    is_first_visible_column = True

    for col in filtered_df.columns:
        if col.startswith("_bg_") or col.startswith("_txt_"):
            gb.configure_column(col, hide=True)
            continue

        if col.lower() in priority_columns_lower:
            width, min_width = 220, 150
        else:
            width, min_width = 120, 80

        # Determine if this column should be pinned (frozen)
        pinned_value = None
        if is_first_visible_column:
            pinned_value = "left"
            is_first_visible_column = False # Turn off so subsequent columns don't freeze

        gb.configure_column(
            col,
            width=width,
            minWidth=min_width,
            sortable=True,
            filter=True,
            resizable=True,
            editable=False,
            pinned=pinned_value, # <--- THIS FREEZES THE FIRST COLUMN
            cellRenderer=html_renderer,
            cellStyle=exact_mirror_style
        )

    gb.configure_grid_options(
        domLayout="normal",
        rowHeight=35,
        headerHeight=45,
        enableCellTextSelection=True,
        ensureDomOrder=True,
        suppressMovableColumns=False,
        suppressColumnVirtualisation=False,
        alwaysShowHorizontalScroll=True,
        animateRows=True
    )

    grid_options = gb.build()

    AgGrid(
        filtered_df,
        gridOptions=grid_options,
        theme="streamlit",
        update_mode=GridUpdateMode.SELECTION_CHANGED,
        allow_unsafe_jscode=True,
        fit_columns_on_grid_load=False,
        enable_enterprise_modules=False,
        height=600,
        width='100%',
        reload_data=False,
        key="stock_grid"
    )

else:
    st.warning("No data loaded. Check sheet sharing and secrets.")
