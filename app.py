import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import json
from datetime import datetime
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode
from st_aggrid.shared import GridUpdateMode

# ---------- Page config ----------
st.set_page_config(page_title="NSE Stock Dashboard", layout="wide")
st.title("📊 NSE Stock Market Dashboard")
st.caption(f"Data refreshed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# ---------- Convert Excel serial number to date ----------
def excel_serial_to_date(val):
    if pd.isna(val) or val == "" or val == "#N/A":
        return ""
    try:
        num = float(val)
        date = pd.to_datetime(num, unit='D', origin='1899-12-30')
        return date.strftime('%Y-%m-%d')
    except (ValueError, TypeError, OverflowError):
        return str(val)

# ---------- Load Google Sheet ----------
@st.cache_data(ttl=300)
def load_sheet_data(sheet_name):
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
        sh = client.open_by_key(spreadsheet_id)
        worksheet = sh.worksheet(sheet_name)

        all_values = worksheet.get_all_values(value_render_option='FORMULA')
        if not all_values:
            return pd.DataFrame()

        # ---------- Clean headers (strip spaces and deduplicate) ----------
        raw_headers = all_values[0]
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

        data_rows = all_values[1:]
        df = pd.DataFrame(data_rows, columns=clean_headers)

        # ---------- Find the Symbol column robustly ----------
        symbol_col = None
        for c in df.columns:
            if c.lower() in ["symbol", "ticker", "stock symbol"]:
                symbol_col = c
                break

        # ---------- Generate Clickable HTML Links (Super Robust) ----------
        if symbol_col:
            for idx, row in df.iterrows():
                sym = str(row[symbol_col]).strip()
                if not sym or sym == "nan":
                    continue
                
                # Iterate over every column to check if it's a link column
                for col in df.columns:
                    c_lower = col.lower()
                    url = None
                    label = "🔗 Link" # Default for columns ending in '1'
                    
                    # 1. Match the column to the correct URL
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
                            
                    elif "nse" in c_lower: # Catches "NSE Chart" and "NSE 1"
                        url = f"https://charting.nseindia.com/?symbol={sym}-EQ"
                        if not c_lower.endswith("1"): label = f"nse {sym}"
                        
                    # 2. If a URL was matched, inject the HTML format
                    if url:
                        df.at[idx, col] = f'<a href="{url}" target="_blank" style="color:#1f77b4; text-decoration:none;">{label}</a>'

        # ---------- Date Column Fixes ----------
        date_columns_to_fix = ["52W High Date", "52W Low Date"]
        for col in date_columns_to_fix:
            if col in df.columns:
                df[col] = df[col].apply(excel_serial_to_date)

        return df

    except Exception as e:
        st.error(f"Error loading sheet '{sheet_name}': {str(e)}")
        return pd.DataFrame()

# ---------- Sidebar ----------
sheet_names = [
    "Top 250 Stocks",
    "Final List",
    "Final List 2",
    "Diff @ 200 DMA",
    "+%",
    "-%"
]

st.sidebar.header("📑 Select a Tab")
selected_sheet = st.sidebar.selectbox("Choose sheet", sheet_names)

st.sidebar.markdown("---")
st.sidebar.info(
    "🔐 **Permissions required**\n\n"
    "Share your Google Sheet with this email:\n"
    "`streamlit-g-sheet-dashboard-vo@axiomatic-idiom-496012-p8.iam.gserviceaccount.com`"
)

# ---------- Main display with AG Grid ----------
st.header(f"📄 {selected_sheet}")

with st.spinner("Loading data..."):
    df = load_sheet_data(selected_sheet)

if not df.empty:
    st.write(f"**Rows:** {df.shape[0]} | **Columns:** {df.shape[1]}")

    # Custom cell renderer for HTML links
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

    gb = GridOptionsBuilder.from_dataframe(df)

    # Priority columns (wider)
    priority_columns_lower = ["id", "company name", "stock name", "symbol", "industry", "sector"]

    for col in df.columns:
        if col.lower() in priority_columns_lower:
            width, min_width = 220, 150
        else:
            width, min_width = 120, 80

        gb.configure_column(
            col,
            width=width,
            minWidth=min_width,
            sortable=True,
            filter=True,
            resizable=True,
            editable=False,
            cellRenderer=html_renderer
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
        df,
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

    # Download button (strip HTML tags for CSV)
    csv_df = df.replace(r'<a[^>]*>([^<]*)</a>', r'\1', regex=True)
    csv = csv_df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download as CSV", csv, f"{selected_sheet.replace(' ', '_')}.csv", "text/csv")

else:
    st.warning("No data loaded. Check sheet sharing and secrets.")

st.markdown("---")
st.caption("Powered by Google Sheets & Streamlit | Columns are resizable, reorderable, horizontally scrollable | Hyperlinks clickable | 52W High/Low Dates converted from Excel serials")
