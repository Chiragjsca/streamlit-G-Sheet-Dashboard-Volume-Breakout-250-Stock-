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

# ---------- Page config ----------
st.set_page_config(page_title="NSE Stock Dashboard", layout="wide")
st.title("📊 NSE Stock Market Dashboard")
st.caption(f"Data refreshed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# ---------- Helper: Convert Google RGB to HEX ----------
def rgb_to_hex(color_dict):
    if not color_dict:
        return "#ffffff"
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
    
    # Save a completely pure, hidden copy of the symbol column before adding HTML
    df_proc['_raw_symbol_'] = df_proc[symbol_col]
    
    for idx, row in df_proc.iterrows():
        sym = str(row['_raw_symbol_']).strip()
        if not sym or sym == "nan":
            continue
            
        for col in df_proc.columns:
            if col.startswith("_bg_") or col.startswith("_txt_") or col == "_raw_symbol_":
                continue
                
            c_lower = col.lower()
            url = None
            label = "🔗 Link"
            
            if "trading view" in c_lower: url, label = f"https://www.tradingview.com/symbols/{sym}", f"Tre {sym}" if not c_lower.endswith("1") else "🔗 Link"
            elif "history data" in c_lower: url, label = f"https://www.equitypandit.com/historical-data/{sym}", f"History {sym}" if not c_lower.endswith("1") else "🔗 Link"
            elif "screener" in c_lower: url, label = f"https://www.screener.in/company/{sym}", f"Scr {sym}" if not c_lower.endswith("1") else "🔗 Link"
            elif "zerodha" in c_lower: url, label = f"https://zerodha.com/markets/stocks/NSE/{sym}", f"🪁 {sym}" if not c_lower.endswith("1") else "🔗 Link"
            elif "chartlink" in c_lower: url, label = f"https://chartink.com/stocks-new?load-snapshot=exponential-moving-average-simple-moving-average-simple-moving-average-moving-average-convergence-divergence-chart-snapshot-175&symbol={sym}", f"CL {sym}" if not c_lower.endswith("1") else "🔗 Link"
            elif "market smith" in c_lower: url, label = f"https://marketsmithindia.com/mstool/eval/{sym}/evaluation.jsp", f"ms {sym}" if not c_lower.endswith("1") else "🔗 Link"
            elif "official nse" in c_lower: url, label = f"https://www.nseindia.com/get-quotes/equity?symbol={sym}", f"nse📰 {sym}" if not c_lower.endswith("1") else "🔗 Link"
            elif "nse" in c_lower: url, label = f"https://charting.nseindia.com/?symbol={sym}-EQ", f"nse {sym}" if not c_lower.endswith("1") else "🔗 Link"
                
            if url:
                df_proc.at[idx, col] = f'<a href="{url}" target="_blank" style="text-decoration:none; color:inherit;">{label}</a>'
                
    return df_proc

# ---------- Helper: Numeric and Date Filters ----------
def apply_numeric_slider(df, col_name, st_container, display_label=None):
    if col_name in df.columns:
        num_series = df[col_name].astype(str).str.replace(r'[%,]', '', regex=True)
        num_series = pd.to_numeric(num_series, errors='coerce')
        
        # CRITICAL FIX: Replace Infinity with NaN to prevent Streamlit crashes
        num_series = num_series.replace([np.inf, -np.inf], np.nan)
        
        valid_nums = num_series.dropna()
        if not valid_nums.empty:
            # Round the min and max to prevent floating point precision crashes
            min_val = round(float(valid_nums.min()), 2)
            max_val = round(float(valid_nums.max()), 2)
            
            if min_val < max_val:
                label = display_label if display_label else f"{col_name} Range:"
                selected_range = st_container.slider(
                    label, 
                    min_value=min_val, 
                    max_value=max_val, 
                    value=(min_val, max_val),
                    key=f"filter_num_{col_name}"
                )
                return df[(num_series >= selected_range[0]) & (num_series <= selected_range[1])]
    return df

def apply_date_filter(df, col_name, st_container):
    if col_name in df.columns:
        options = ["All Time", "Past 5 Days", "Past 10 Days", "Past 15 Days", "Past 20 Days", 
                   "Past 25 Days", "Past 30 Days", "Past 1 Month", "Past 2 Months", 
                   "Past 6 Months", "Past 1 Year"]
        
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
        if key.startswith("filter_") or key == "search_query":
            del st.session_state[key]
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

with st.spinner("Downloading data and exact colors from Google API..."):
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

    # ==========================================
    # 🔍 1. APPLY SEARCH BAR FILTER
    # ==========================================
    if search_query:
        mask = filtered_df[actual_cols].astype(str).apply(lambda x: x.str.contains(search_query, case=False, na=False)).any(axis=1)
        filtered_df = filtered_df[mask]

    # ==========================================
    # 🎯 2. APPLY CATEGORY DROP DOWN FILTERS
    # ==========================================
    st.sidebar.markdown("---")
    st.sidebar.header("🎯 Categorical Filters")
    
    active_filters = [c for c in actual_cols if any(key in c.lower() for key in ["cumulative average", "industry", "sector", "output", "start gtt order"])]
    
    for col_to_filter in active_filters:
        unique_options = sorted([val for val in final_df[col_to_filter].unique() if str(val).strip() != ""])
        selected_options = st.sidebar.multiselect(f"Filter by {col_to_filter}:", options=unique_options, key=f"filter_cat_{col_to_filter}")
        if selected_options:
            filtered_df = filtered_df[filtered_df[col_to_filter].isin(selected_options)]

    # ==========================================
    # 📈 3. SPECIAL DMA TREND FILTER
    # ==========================================
    st.sidebar.markdown("---")
    st.sidebar.header("📈 Special DMA Trend Filter")
    dma_options = [
        "All (No Filter)",
        "50 DMA < 100 DMA < 200 DMA",
        "50 DMA > 100 DMA > 200 DMA",
        "50 DMA > 200 DMA",
        "50 DMA < 200 DMA"
    ]
    dma_choice = st.sidebar.selectbox("Select DMA Condition:", dma_options, key="filter_dma_trend")

    if dma_choice != "All (No Filter)":
        dma50_col = next((c for c in actual_cols if "50 dma" in c.lower()), None)
        dma100_col = next((c for c in actual_cols if "100 dma" in c.lower()), None)
        dma200_col = next((c for c in actual_cols if "200 dma" in c.lower()), None)
        
        if dma50_col and dma200_col:
            s50 = pd.to_numeric(filtered_df[dma50_col].astype(str).str.replace(r'[%,]', '', regex=True), errors='coerce')
            s200 = pd.to_numeric(filtered_df[dma200_col].astype(str).str.replace(r'[%,]', '', regex=True), errors='coerce')
            
            if dma_choice == "50 DMA > 200 DMA":
                filtered_df = filtered_df[s50 > s200]
            elif dma_choice == "50 DMA < 200 DMA":
                filtered_df = filtered_df[s50 < s200]
            elif dma100_col:
                s100 = pd.to_numeric(filtered_df[dma100_col].astype(str).str.replace(r'[%,]', '', regex=True), errors='coerce')
                if dma_choice == "50 DMA < 100 DMA < 200 DMA":
                    filtered_df = filtered_df[(s50 < s100) & (s100 < s200)]
                elif dma_choice == "50 DMA > 100 DMA > 200 DMA":
                    filtered_df = filtered_df[(s50 > s100) & (s100 > s200)]

    # ==========================================
    # 📊 4. APPLY ALL NUMERIC RANGE SLIDERS
    # ==========================================
    st.sidebar.markdown("---")
    st.sidebar.header("📊 Numeric Range Filters")
    
    cmp_col = next((c for c in actual_cols if c.lower() in ["cmp", "close price"]), None)

    # A) Diff from 200 DMA Filter
    diff_200_col = next((c for c in actual_cols if "diff" in c.lower() and "200" in c.lower()), None)
    if diff_200_col:
        filtered_df = apply_numeric_slider(filtered_df, diff_200_col, st.sidebar, "Diff. from 200 DMA (%) Range:")

    # B) 52W Low % (Find it, or compute it dynamically safely)
    low_pct_col = next((c for c in actual_cols if "52" in c.lower() and "low" in c.lower() and ("%" in c.lower() or "per" in c.lower() or "away" in c.lower())), None)
    if not low_pct_col and cmp_col:
        low_col = next((c for c in actual_cols if "52" in c.lower() and "low" in c.lower() and "date" not in c.lower() and "%" not in c.lower()), None)
        if low_col:
            cmp_s = pd.to_numeric(filtered_df[cmp_col].astype(str).str.replace(r'[%,]', '', regex=True), errors='coerce')
            low_s = pd.to_numeric(filtered_df[low_col].astype(str).str.replace(r'[%,]', '', regex=True), errors='coerce')
            
            # CRITICAL FIX: Prevent divide by zero making infinity
            low_s = low_s.replace(0, np.nan)
            
            filtered_df["% from 52W Low (Calc)"] = ((cmp_s - low_s) / low_s) * 100
            filtered_df["% from 52W Low (Calc)"] = filtered_df["% from 52W Low (Calc)"].round(2)
            low_pct_col = "% from 52W Low (Calc)"
            
    if low_pct_col:
        filtered_df = apply_numeric_slider(filtered_df, low_pct_col, st.sidebar, "% from 52W Low Range:")

    # C) 52W High % (Find it, or compute it dynamically safely)
    high_pct_col = next((c for c in actual_cols if "52" in c.lower() and "high" in c.lower() and ("%" in c.lower() or "per" in c.lower() or "away" in c.lower())), None)
    if not high_pct_col and cmp_col:
        high_col = next((c for c in actual_cols if "52" in c.lower() and "high" in c.lower() and "date" not in c.lower() and "%" not in c.lower()), None)
        if high_col:
            cmp_s = pd.to_numeric(filtered_df[cmp_col].astype(str).str.replace(r'[%,]', '', regex=True), errors='coerce')
            high_s = pd.to_numeric(filtered_df[high_col].astype(str).str.replace(r'[%,]', '', regex=True), errors='coerce')
            
            # CRITICAL FIX: Prevent divide by zero making infinity
            high_s = high_s.replace(0, np.nan)
            
            filtered_df["% from 52W High (Calc)"] = ((cmp_s - high_s) / high_s) * 100
            filtered_df["% from 52W High (Calc)"] = filtered_df["% from 52W High (Calc)"].round(2)
            high_pct_col = "% from 52W High (Calc)"
            
    if high_pct_col:
        filtered_df = apply_numeric_slider(filtered_df, high_pct_col, st.sidebar, "% from 52W High Range:")

    # D) Remaining Numeric Targets
    numeric_targets = [
        "Volume", "CMP", "Price %", 
        "Promoters %", "Institutional %", "Face Value", 
        "Net Profit", "EPS", "RONW %", "Market Cap", "Enterprise Value"
    ]
    
    processed_cols = {diff_200_col, low_pct_col, high_pct_col}
    for target in numeric_targets:
        col_match = next((c for c in actual_cols if target.lower() in c.lower() and c not in processed_cols), None)
        if col_match:
            filtered_df = apply_numeric_slider(filtered_df, col_match, st.sidebar)
            processed_cols.add(col_match)

    # ==========================================
    # 📅 5. APPLY DATE FILTERS
    # ==========================================
    st.sidebar.markdown("---")
    st.sidebar.header("📅 Date Filters")
    
    high_date_col = next((c for c in actual_cols if "52w high date" in c.lower()), None)
    low_date_col = next((c for c in actual_cols if "52w low date" in c.lower()), None)

    if high_date_col: filtered_df = apply_date_filter(filtered_df, high_date_col, st.sidebar)
    if low_date_col: filtered_df = apply_date_filter(filtered_df, low_date_col, st.sidebar)

    # ==========================================
    # 📌 TOP UI: ROWS COUNT & DYNAMIC QUICK LINKS
    # ==========================================
    col1, col2 = st.columns([1, 3])
    with col1:
        st.write(f"**Rows:** {filtered_df.shape[0]} | **Columns:** {len(filtered_df.columns) - 1}") # subtract hidden raw_symbol
    
    # Placeholder for the top right dynamic links
    url_placeholder = col2.empty()

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
        
        if (!bgColor || bgColor.toLowerCase() === '#ffffff') return null;
        
        return {
            'backgroundColor': bgColor,
            'color': txtColor || '#000000',
            'fontWeight': (txtColor === '#ffffff' || bgColor === '#0f9d58') ? 'bold' : 'normal'
        };
    }
    """)

    gb = GridOptionsBuilder.from_dataframe(filtered_df)
    
    # Enable Row Selection
    gb.configure_selection(selection_mode="single", use_checkbox=True)

    priority_columns_lower = ["nse code", "id", "company name", "stock name", "symbol", "industry", "sector"]
    is_first_visible_column = True

    for col in filtered_df.columns:
        if col.startswith("_bg_") or col.startswith("_txt_") or col == "_raw_symbol_":
            gb.configure_column(col, hide=True)
            continue

        width, min_width = (220, 150) if col.lower() in priority_columns_lower else (120, 80)
        
        pinned_value = None
        if is_first_visible_column:
            pinned_value = "left"
            is_first_visible_column = False 

        gb.configure_column(
            col,
            width=width,
            minWidth=min_width,
            sortable=True,
            filter=True,
            resizable=True,
            editable=False,
            pinned=pinned_value,
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

    grid_response = AgGrid(
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

    # ==========================================
    # 🎯 POPULATE TOP-RIGHT URLS ON ROW SELECTION
    # ==========================================
    selected_rows = grid_response.get("selected_rows", [])
    if selected_rows is not None and len(selected_rows) > 0:
        sel_row = selected_rows.iloc[0] if isinstance(selected_rows, pd.DataFrame) else selected_rows[0]
        sym = str(sel_row.get("_raw_symbol_", "")).strip() 
        
        if sym:
            with url_placeholder.container():
                with st.expander(f"⚡ **{sym} Quick Links:**", expanded=True):
                    st.markdown(
                        f"[Trading View (🔗)](https://www.tradingview.com/symbols/{sym}) &nbsp; | &nbsp; "
                        f"[History Data (🔗)](https://www.equitypandit.com/historical-data/{sym}) &nbsp; | &nbsp; "
                        f"[Screener (🔗)](https://www.screener.in/company/{sym}) &nbsp; | &nbsp; "
                        f"[Zerodha (🔗)](https://zerodha.com/markets/stocks/NSE/{sym}) &nbsp; | &nbsp; "
                        f"[Chartlink (🔗)](https://chartink.com/stocks-new?load-snapshot=exponential-moving-average-simple-moving-average-simple-moving-average-moving-average-convergence-divergence-chart-snapshot-175&symbol={sym}) &nbsp; | &nbsp; "
                        f"[Market smith india (🔗)](https://marketsmithindia.com/mstool/eval/{sym}/evaluation.jsp) &nbsp; | &nbsp; "
                        f"[Official NSE URL (🔗)](https://www.nseindia.com/get-quotes/equity?symbol={sym})"
                    )

else:
    st.warning("No data loaded. Check sheet sharing and secrets.")
