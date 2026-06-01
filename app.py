import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from st_aggrid import AgGrid, GridOptionsBuilder
import datetime

# ------------------------------
# Page config
st.set_page_config(page_title="NSE Stock Dashboard", layout="wide")

# ------------------------------
# Google Sheets connection (cached to avoid repeated calls)
@st.cache_resource
def load_google_sheet(sheet_name="Top 250 Stocks"):
    # Use Streamlit secrets for security (recommended)
    # Create a section in .streamlit/secrets.toml like:
    # [gcp_service_account]
    # type = "service_account"
    # project_id = "..."
    # private_key_id = "..."
    # private_key = "... (with quotes and newlines)"
    # client_email = "..."
    # client_id = "..."
    # auth_uri = "https://accounts.google.com/o/oauth2/auth"
    # token_uri = "https://oauth2.googleapis.com/token"
    creds_dict = st.secrets["gcp_service_account"]
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)
    # Replace with your actual Google Sheet name
    sheet = client.open("NSE_Stock_Dashboard").worksheet(sheet_name)
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    return df

# ------------------------------
# Main app
st.title("📊 NSE Stock Market Dashboard")
st.caption(f"Data refreshed: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Tab selection
tab1, tab2 = st.tabs(["Top 250 Stocks", "Info"])

with tab1:
    st.subheader("Top 250 Stocks")

    # Load data - adjust sheet name as needed
    try:
        df = load_google_sheet("Top 250 Stocks")
        st.success(f"Loaded {len(df)} rows, {len(df.columns)} columns")
    except Exception as e:
        st.error(f"Failed to load data: {e}")
        st.stop()

    # Configure ag-Grid
    gb = GridOptionsBuilder.from_dataframe(df)

    # FIX: use configure_default_column (not configure_columns)
    gb.configure_default_column(
        enableRowGroup=False,
        enablePivot=False,
        enableValue=False,
        resizable=True,
        filterable=True,
        sortable=True
    )

    # Optional: pin or hide specific columns
    # gb.configure_column("Symbol", width=100, pinned="left")
    # gb.configure_column("S.No", hide=True)

    grid_options = gb.build()

    # Display interactive grid
    grid_response = AgGrid(
        df,
        gridOptions=grid_options,
        height=600,
        width="100%",
        theme="streamlit",
        enable_enterprise_modules=False,
        update_mode="NO_UPDATE"
    )

    st.caption(f"Rows: {len(df)} | Columns: {len(df.columns)}")

with tab2:
    st.markdown("""
    **Permissions required**  
    Share your Google Sheet with this service account email:  
    `streamlit-g-sheet-dashboard-vo@axiomatic-idom-496012-p8.iam.gserviceaccount.com`

    **Error resolved**  
    The previous `TypeError` was caused by using `gb.configure_columns(...)`, which does not exist.  
    It has been replaced with the correct method `gb.configure_default_column(...)`.

    **How to use**  
    1. Replace `"NSE_Stock_Dashboard"` with your actual Google Sheet name.  
    2. Store your service account JSON credentials in Streamlit secrets (as shown in the code comments).  
    3. Run with `streamlit run app.py`.

    **Dependencies**  
