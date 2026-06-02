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
def apply_numeric_slider(df, col_name, st_container):
    """Parses formatted strings to numbers and applies a slider filter."""
    if col_name in df.columns:
        num_series = df[col_name].astype(str).str.replace(r'[%,]', '', regex=True)
        num_series = pd.to_numeric(num_series, errors='coerce')
        
        valid_nums = num_series.dropna()
        if not valid_nums.empty:
            min_val = float(valid_nums.min())
            max_val = float(valid_nums.max())
            
            if min_val < max_val:
                selected_range = st_container.slider(
                    f"{col_name} Range:", 
                    min_value=min_val, 
                    max_value=max_val, 
                    value=(min_val, max_val),
                    key=f"filter_num_{col_name}" # ADDED KEY
                )
                return df[(num_series >= selected_range[0]) & (num_series <= selected_range[1])]
    return df

def apply_date_filter(df, col_name, st_container):
    """Parses dates and filters based on selected timeframe."""
    if col_name in df.columns:
        options = ["All Time", "Past 5 Days", "Past 10 Days", "Past 15 Days", "Past 20 Days", 
                   "Past 25 Days", "Past 30 Days", "Past 1 Month", "Past 2 Months", 
                   "Past 6 Months", "Past 1 Year"]
        
        selection = st_container.selectbox(f"{col_name}:", options, key=f"filter_date_{col_name}") # ADDED KEY
        
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

# 1. CLEAR FILTERS BUTTON LOGIC
if st.sidebar.button("🧹 Clear All Filters", use_container_width=True):
    for key in list(st.session_state.keys()):
        if key.startswith("filter_") or key == "search_query":
            del st.session_state[key]
    st.rerun() # Forces the app to refresh immediately

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
    
    # Auto-detect Symbol column
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
    # 📊 3. APPLY NUMERIC RANGE SLIDERS
    # ==========================================
    st.sidebar.markdown("---")
    st.sidebar.header("📊 Numeric Range Filters")
    
    cmp_col = next((c for c in actual_cols if "cmp" in c.lower()), None)
    price_pct_col = next((c for c in actual_cols if "price %" in c.lower()), None)
    diff_dma_col = next((c for c in actual_cols if "diff" in c.lower() and "200" in c.lower()), None)

    if cmp_col: filtered_df = apply_numeric_slider(filtered_df, cmp_col, st.sidebar)
    if price_pct_col: filtered_df = apply_numeric_slider(filtered_df, price_pct_col, st.sidebar)
    if diff_dma_col: filtered_df = apply_numeric_slider(filtered_df, diff_dma_col, st.sidebar)

    # ==========================================
    # 📅 4. APPLY DATE FILTERS
    # ==========================================
    st.sidebar.markdown("---")
    st.sidebar.header("📅 Date Filters")
    
    high_date_col = next((c for c in actual_cols if "52w high date" in c.lower()), None)
    low_date_col = next((c for c in actual_cols if "52w low date" in c.lower()), None)

    if high_date_col: filtered_df = apply_date_filter(filtered_df, high_date_col, st.sidebar)
    if low_date_col: filtered_df = apply_date_filter(filtered_df, low_date_col, st.sidebar)

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
        
        if (!bgColor || bgColor.toLowerCase() === '#ffffff') return null;
        
        return {
            'backgroundColor': bgColor,
            'color': txtColor || '#000000',
            'fontWeight': (txtColor === '#ffffff' || bgColor === '#0f9d58') ? 'bold' : 'normal'
        };
    }
    """)

    gb = GridOptionsBuilder.from_dataframe(filtered_df)
    priority_columns_lower = ["nse code", "id", "company name", "stock name", "symbol", "industry", "sector"]

    is_first_visible_column = True

    for col in filtered_df.columns:
        if col.startswith("_bg_") or col.startswith("_txt_"):
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
