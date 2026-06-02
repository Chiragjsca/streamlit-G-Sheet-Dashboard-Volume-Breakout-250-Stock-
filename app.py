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

# ---------- Helper: extract URL and label from HYPERLINK formula (supports CONCATENATE and &) ----------
def extract_hyperlink_info(cell_value, symbol):
    """Return (url, label) from a HYPERLINK formula, using the provided symbol for dynamic parts."""
    if not isinstance(cell_value, str) or not cell_value.startswith("=HYPERLINK("):
        return None, cell_value

    # Pattern to capture the entire arguments inside HYPERLINK(...)
    # It matches: HYPERLINK( something , something )
    match = re.search(r'=HYPERLINK\((.*),\s*(.*)\)', cell_value, re.DOTALL)
    if not match:
        return None, cell_value

    url_part = match.group(1).strip()
    label_part = match.group(2).strip()

    # Function to evaluate a string that may contain CONCATENATE() or & concatenation
    def evaluate_concat(expr, symbol):
        # Remove surrounding quotes if present (literal string)
        if expr.startswith('"') and expr.endswith('"'):
            return expr[1:-1]
        # Handle CONCATENATE(...)
        concat_match = re.search(r'CONCATENATE\((.*)\)', expr, re.IGNORECASE)
        if concat_match:
            inner = concat_match.group(1)
            # Split by commas, but careful with nested quotes
            parts = []
            current = ''
            in_quotes = False
            for ch in inner:
                if ch == '"':
                    in_quotes = not in_quotes
                if ch == ',' and not in_quotes:
                    parts.append(current.strip())
                    current = ''
                else:
                    current += ch
            parts.append(current.strip())
            # Evaluate each part (which can be string literal or & concatenation)
            evaluated_parts = []
            for p in parts:
                evaluated_parts.append(evaluate_concat(p, symbol))
            return ''.join(evaluated_parts)
        # Handle & concatenation
        if '&' in expr:
            subparts = expr.split('&')
            result = ''
            for sp in subparts:
                sp = sp.strip()
                if sp.startswith('"') and sp.endswith('"'):
                    result += sp[1:-1]
                elif sp.upper() == 'A2':  # Assuming A2 is the symbol cell reference
                    result += str(symbol)
                else:
                    # Could be a cell reference like A2, but we'll assume it's the symbol
                    result += str(symbol)
            return result
        # If it's a plain cell reference like A2
        if expr.upper() == 'A2':
            return str(symbol)
        # If it's a string literal
        if expr.startswith('"') and expr.endswith('"'):
            return expr[1:-1]
        return expr

    # Extract URL and label using the symbol
    try:
        url = evaluate_concat(url_part, symbol)
        label = evaluate_concat(label_part, symbol)
        return url, label
    except Exception:
        return None, cell_value

# ---------- Convert Excel serial numbers to date (for 52W High Date and 52W Low Date) ----------
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

        # Identify the column that contains stock symbols (used for HYPERLINK evaluation)
        symbol_col = None
        for col in ["Symbol", "Stock Name", "Company Name", "Ticker"]:
            if col in df.columns:
                symbol_col = col
                break
        if symbol_col is None and len(df.columns) > 0:
            symbol_col = df.columns[0]  # fallback to first column

        # Columns with HYPERLINK formulas
        link_columns = [
            "Trading View", "History Data", "Screener", "Zerodha", "Chartlink",
            "Market smith india", "NSE Chart", "Official NSE URL",
            "NSE 1", "Trading View 1", "History Data 1", "Screener 1",
            "Zerodha 1", "Chartlink 1", "Market smith india 1", "Official NSE URL 1"
        ]

        # Process each row and column to convert HYPERLINK formulas to HTML links
        for col in link_columns:
            if col not in df.columns:
                continue
            new_values = []
            for idx, val in enumerate(df[col]):
                if pd.isna(val) or val == "":
                    new_values.append("")
                    continue
                # Get the symbol for this row
                symbol = df.iloc[idx][symbol_col] if symbol_col else ""
                url, label = extract_hyperlink_info(val, symbol)
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

        # Convert only the two date columns
        for col in ["52W High Date", "52W Low Date"]:
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

    # Custom cell renderer that forces HTML rendering
    html_renderer = JsCode("""
    function(params) {
        if (params.value && typeof params.value === 'string' && params.value.indexOf('<a') !== -1) {
            return params.value;
        }
        return params.value;
    }
    """)

    gb = GridOptionsBuilder.from_dataframe(df)

    priority_columns = ["ID", "Company Name", "Stock Name", "Symbol", "Industry", "Sector"]

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
st.caption("Powered by Google Sheets & Streamlit | Columns are resizable, reorderable, horizontally scrollable | Hyperlinks clickable | Dates formatted")
