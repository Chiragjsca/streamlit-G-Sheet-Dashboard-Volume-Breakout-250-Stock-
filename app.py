import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import json
import re
from datetime import datetime
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode
from st_aggrid.shared import GridUpdateMode

# ---------- Page config ----------
st.set_page_config(page_title="NSE Stock Dashboard", layout="wide")
st.title("📊 NSE Stock Market Dashboard")
st.caption(f"Data refreshed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# ---------- Helper: extract URL and label from HYPERLINK formula ----------
def extract_hyperlink_info(cell_value):
    if isinstance(cell_value, str) and cell_value.startswith("=HYPERLINK("):
        pattern = r'=HYPERLINK\("([^"]+)",\s*"([^"]*)"\)'
        match = re.search(pattern, cell_value)
        if match:
            return match.group(1), match.group(2)
    return None, cell_value

# ---------- Convert Excel serial numbers to dates ----------
def convert_excel_serial_to_date(val):
    if not isinstance(val, str):
        return val
    # Remove any whitespace
    val = val.strip()
    # Handle #N/A or other error strings
    if val.startswith("#N/A") or val.startswith("#"):
        return ""
    # Check if it's a numeric string (integer or float)
    try:
        num = float(val)
        # Excel serial date: days since 1899-12-30 (Excel for Windows)
        # Pandas conversion: pd.to_datetime(num, unit='D', origin='1899-12-30')
        date = pd.to_datetime(num, unit='D', origin='1899-12-30')
        # Format as YYYY-MM-DD (you can change the format)
        return date.strftime('%Y-%m-%d')
    except (ValueError, OverflowError):
        return val

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

        # Fetch using FORMULA to capture HYPERLINK formulas
        all_values = worksheet.get_all_values(value_render_option='FORMULA')
        if not all_values:
            return pd.DataFrame()

        # Clean headers (deduplicate)
        raw_headers = all_values[0]
        clean_headers = []
        seen = {}
        for h in raw_headers:
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

        # ---------- Process HYPERLINK columns (convert to HTML <a> tags) ----------
        link_columns = [
            "Trading View", "History Data", "Screener", "Zerodha", "Chartlink",
            "Market smith india", "NSE Chart", "Official NSE URL",
            "NSE 1", "Trading View 1", "History Data 1", "Screener 1",
            "Zerodha 1", "Chartlink 1", "Market smith india 1", "Official NSE URL 1"
        ]

        for col in link_columns:
            if col in df.columns:
                new_values = []
                for val in df[col]:
                    if pd.isna(val) or val == "":
                        new_values.append("")
                        continue

                    url, label = extract_hyperlink_info(val)
                    if url and label:
                        if col.endswith("1"):
                            new_values.append(f'<a href="{url}" target="_blank" style="color:#1f77b4; text-decoration:none;">🔗 Link</a>')
                        else:
                            new_values.append(f'<a href="{url}" target="_blank" style="color:#1f77b4; text-decoration:none;">{label}</a>')
                    elif isinstance(val, str) and (val.startswith("http://") or val.startswith("https://")):
                        if col.endswith("1"):
                            new_values.append(f'<a href="{val}" target="_blank" style="color:#1f77b4; text-decoration:none;">🔗 Link</a>')
                        else:
                            new_values.append(f'<a href="{val}" target="_blank" style="color:#1f77b4; text-decoration:none;">{val}</a>')
                    else:
                        new_values.append(val)
                df[col] = new_values

        # ---------- Convert date columns (e.g., 52W High Date, 52W Low Date) ----------
        # Identify columns that contain "Date" in name (case insensitive)
        date_columns = [col for col in df.columns if "date" in col.lower()]
        for col in date_columns:
            df[col] = df[col].apply(convert_excel_serial_to_date)

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

    # Custom cell renderer to display HTML links properly
    html_renderer = JsCode("""
    function(params) {
        if (params.value && typeof params.value === 'string' && params.value.includes('<a')) {
            return params.value;
        }
        return params.value;
    }
    """)

    # Build grid options
    gb = GridOptionsBuilder.from_dataframe(df)

    # Priority columns (wider)
    priority_columns = [
        "ID", "Company Name", "Stock Name", "Symbol", "Industry", "Sector"
    ]

    for col in df.columns:
        if col in priority_columns:
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
st.caption("Powered by Google Sheets & Streamlit | Columns are resizable, reorderable, horizontally scrollable | Hyperlinks clickable | Dates correctly formatted")
