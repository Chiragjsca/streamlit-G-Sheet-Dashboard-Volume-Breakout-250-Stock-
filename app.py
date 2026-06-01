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

        # Get formulas (not rendered values)
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

        # Columns with HYPERLINK formulas or raw URLs
        link_columns = [
            "Trading View", "History Data", "Screener", "Zerodha", "Chartlink",
            "Market smith india", "NSE Chart", "Official NSE URL",
            "NSE 1", "Trading View 1", "History Data 1", "Screener 1",
            "Zerodha 1", "Chartlink 1", "Market smith india 1", "Official NSE URL 1"
        ]

        # Process each column
        for col in link_columns:
            if col in df.columns:
                new_values = []
                for val in df[col]:
                    if pd.isna(val) or val == "":
                        new_values.append("")
                        continue

                    url, label = extract_hyperlink_info(val)
                    if url and label:
                        # For normal columns: keep original label; for "1" columns: show 🔗 Link
                        if col.endswith("1"):
                            new_values.append(f'<a href="{url}" target="_blank">🔗 Link</a>')
                        else:
                            new_values.append(f'<a href="{url}" target="_blank">{label}</a>')
                    elif isinstance(val, str) and (val.startswith("http://") or val.startswith("https://")):
                        # Raw URL – for "1" columns show 🔗 Link, otherwise show full URL
                        if col.endswith("1"):
                            new_values.append(f'<a href="{val}" target="_blank">🔗 Link</a>')
                        else:
                            new_values.append(f'<a href="{val}" target="_blank">{val}</a>')
                    else:
                        new_values.append(val)
                df[col] = new_values

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

    # Prepare grid options for AG Grid
    gb = GridOptionsBuilder.from_dataframe(df)

    # Enable column resizing, reordering, and filtering
    gb.configure_column(enableRowGroup=False, enablePivot=False, enableValue=False)
    gb.configure_default_column(
        resizable=True,
        sortable=True,
        filter=True,
        editable=False,
        width=150
    )
    gb.configure_grid_options(
        domLayout='autoHeight',
        rowHeight=35,
        headerHeight=45,
        enableCellTextSelection=True,
        ensureDomOrder=True
    )

    # Allow column reordering (drag & drop)
    gb.configure_grid_options(suppressMovableColumns=False)

    # Build grid options
    grid_options = gb.build()

    # Display AG Grid
    grid_response = AgGrid(
        df,
        gridOptions=grid_options,
        update_mode=GridUpdateMode.SELECTION_CHANGED,
        allow_unsafe_jscode=True,
        theme='streamlit',  # or 'balham', 'alpine'
        fit_columns_on_grid_load=False,
        enable_enterprise_modules=False,
        height=600,
        width='100%',
        reload_data=False
    )

    # Download button (strip HTML tags for CSV)
    csv_df = df.replace(r'<a href="([^"]+)">([^<]+)</a>', r'\2 (\1)', regex=True)
    csv = csv_df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download as CSV", csv, f"{selected_sheet.replace(' ', '_')}.csv", "text/csv")

else:
    st.warning("No data loaded. Check sheet sharing and secrets.")

st.markdown("---")
st.caption("Powered by Google Sheets & Streamlit | Columns are resizable & reorderable")
