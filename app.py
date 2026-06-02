import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import json
import re
from datetime import datetime
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="NSE Stock Dashboard",
    layout="wide"
)

st.title("📊 NSE Stock Market Dashboard")
st.caption(f"Data refreshed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# =====================================================
# HELPER FUNCTION
# =====================================================

def extract_hyperlink_info(cell_value):
    if isinstance(cell_value, str) and cell_value.startswith("=HYPERLINK("):
        pattern = r'=HYPERLINK\("([^"]+)",\s*"([^"]*)"\)'
        match = re.search(pattern, cell_value)

        if match:
            return match.group(1), match.group(2)

    return None, cell_value

# =====================================================
# LOAD SHEET
# =====================================================

@st.cache_data(ttl=300)
def load_sheet_data(sheet_name):

    try:

        if "gcp_service_account" not in st.secrets:
            st.error("Missing gcp_service_account in secrets.")
            return pd.DataFrame()

        service_account_info = st.secrets["gcp_service_account"]

        if isinstance(service_account_info, str):
            service_account_info = json.loads(service_account_info)

        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]

        creds = Credentials.from_service_account_info(
            service_account_info,
            scopes=scope
        )

        client = gspread.authorize(creds)

        spreadsheet_id = "1SFhuZbLLlwwFsNo1k2RRx_Zp6bAkRR20W0F_zTwgdwU"

        sh = client.open_by_key(spreadsheet_id)

        worksheet = sh.worksheet(sheet_name)

        all_values = worksheet.get_all_values(
            value_render_option='FORMULA'
        )

        if not all_values:
            return pd.DataFrame()

        # -----------------------------------------
        # HEADERS CLEANING
        # -----------------------------------------

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

        df = pd.DataFrame(
            data_rows,
            columns=clean_headers
        )

        # -----------------------------------------
        # HYPERLINK COLUMNS
        # -----------------------------------------

        link_columns = [
            "Trading View",
            "History Data",
            "Screener",
            "Zerodha",
            "Chartlink",
            "Market smith india",
            "NSE Chart",
            "Official NSE URL",
            "NSE 1",
            "Trading View 1",
            "History Data 1",
            "Screener 1",
            "Zerodha 1",
            "Chartlink 1",
            "Market smith india 1",
            "Official NSE URL 1"
        ]

        for col in link_columns:

            if col not in df.columns:
                continue

            new_values = []

            for val in df[col]:

                if pd.isna(val) or val == "":
                    new_values.append("")
                    continue

                url, label = extract_hyperlink_info(val)

                if url and label:

                    if col.endswith("1"):
                        new_values.append(
                            f'<a href="{url}" target="_blank">🔗 Link</a>'
                        )
                    else:
                        new_values.append(
                            f'<a href="{url}" target="_blank">{label}</a>'
                        )

                elif isinstance(val, str) and (
                    val.startswith("http://")
                    or val.startswith("https://")
                ):

                    if col.endswith("1"):
                        new_values.append(
                            f'<a href="{val}" target="_blank">🔗 Link</a>'
                        )
                    else:
                        new_values.append(
                            f'<a href="{val}" target="_blank">{val}</a>'
                        )

                else:
                    new_values.append(val)

            df[col] = new_values

        return df

    except Exception as e:

        st.error(
            f"Error loading sheet '{sheet_name}': {str(e)}"
        )

        return pd.DataFrame()

# =====================================================
# SIDEBAR
# =====================================================

sheet_names = [
    "Top 250 Stocks",
    "Final List",
    "Final List 2",
    "Diff @ 200 DMA",
    "+%",
    "-%"
]

st.sidebar.header("📑 Select a Tab")

selected_sheet = st.sidebar.selectbox(
    "Choose sheet",
    sheet_names
)

st.sidebar.markdown("---")

st.sidebar.info(
    "🔐 Permissions required\n\n"
    "Share your Google Sheet with:\n\n"
    "streamlit-g-sheet-dashboard-vo@axiomatic-idiom-496012-p8.iam.gserviceaccount.com"
)

# =====================================================
# MAIN DISPLAY
# =====================================================

st.header(f"📄 {selected_sheet}")

with st.spinner("Loading data..."):
    df = load_sheet_data(selected_sheet)

if not df.empty:

    st.write(
        f"**Rows:** {df.shape[0]} | **Columns:** {df.shape[1]}"
    )

    # =================================================
    # AG GRID
    # =================================================

    gb = GridOptionsBuilder.from_dataframe(df)

    gb.configure_default_column(
        sortable=True,
        filter=True,
        resizable=True,
        editable=False
    )

    priority_columns = [
    "ID",
    "Company Name",
    "Stock Name",
    "Symbol",
    "Industry",
    "Sector"
]

for col in df.columns:

    if col in priority_columns:
        gb.configure_column(
            col,
            width=220,
            minWidth=150,
            menuTabs=[
                "generalMenuTab",
                "filterMenuTab",
                "columnsMenuTab"
            ]
        )

    else:
        gb.configure_column(
            col,
            width=120,
            minWidth=80,
            menuTabs=[
                "generalMenuTab",
                "filterMenuTab",
                "columnsMenuTab"
            ]
        )

    gb.configure_default_column(
    sortable=True,
    filter=True,
    resizable=True,
    editable=False,
    enableRowGroup=True,
    enablePivot=True,
    enableValue=True
)

# Sidebar for Show / Hide Columns
gb.configure_side_bar()

gb.configure_grid_options(
    domLayout="normal",
    rowHeight=35,
    headerHeight=45,
    enableCellTextSelection=True,
    ensureDomOrder=True,
    suppressMovableColumns=False,
    suppressColumnVirtualisation=False,
    alwaysShowHorizontalScroll=True,
    animateRows=True,
    sideBar=True
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
    height=700,
    reload_data=False,
    key="stock_grid"
)

    # =================================================
    # DOWNLOAD CSV
    # =================================================

    csv_df = df.replace(
        r'<a href="([^"]+)">([^<]+)</a>',
        r'\2 (\1)',
        regex=True
    )

    csv = csv_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📥 Download CSV",
        csv,
        f"{selected_sheet.replace(' ', '_')}.csv",
        "text/csv"
    )

else:

    st.warning(
        "No data loaded. Check Sheet permissions and Secrets."
    )

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.caption(
    "Powered by Google Sheets & Streamlit | "
    "50px columns | Resizable | Horizontal Scroll Enabled"
)
