import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import json
from datetime import datetime

# ---------- Page Configuration ----------
st.set_page_config(
    page_title="NSE Stock Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📊 NSE Stock Market Dashboard")
st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# ---------- Load Google Sheet Data ----------
@st.cache_data(ttl=300)  # cache for 5 minutes
def load_sheet_data(sheet_name):
    """
    Load a specific worksheet from the Google Sheet using service account.
    Returns a pandas DataFrame.
    """
    try:
        # Get credentials from Streamlit secrets
        # The secrets should contain a key "gcp_service_account" with the full JSON content
        if "gcp_service_account" not in st.secrets:
            st.error("Missing 'gcp_service_account' in secrets. Please check your secrets.toml file.")
            return pd.DataFrame()

        # Load the service account JSON
        service_account_info = st.secrets["gcp_service_account"]

        # If it's stored as a string, parse it
        if isinstance(service_account_info, str):
            service_account_info = json.loads(service_account_info)

        # Define the scope
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]

        # Create credentials
        creds = Credentials.from_service_account_info(service_account_info, scopes=scope)

        # Authorize and open the spreadsheet
        client = gspread.authorize(creds)
        spreadsheet_id = "1SFhuZbLLlwwFsNo1k2RRx_Zp6bAkRR20W0F_zTwgdwU"  # your sheet ID
        sh = client.open_by_key(spreadsheet_id)

        # Select worksheet by name
        worksheet = sh.worksheet(sheet_name)

        # Get all records as a list of dicts
        data = worksheet.get_all_records()
        df = pd.DataFrame(data)

        return df

    except Exception as e:
        st.error(f"Error loading sheet '{sheet_name}': {str(e)}")
        return pd.DataFrame()

# ---------- Sidebar: Sheet Selection ----------
sheet_names = [
    "Top 250 Stocks",
    "Final List",
    "Final List 2",
    "Diff @ 200 DMA",
    "+%",
    "-%"
]

st.sidebar.header("📑 Select a Sheet")
selected_sheet = st.sidebar.selectbox("Choose Tab", sheet_names)

st.sidebar.markdown("---")
st.sidebar.info(
    "Data is pulled directly from your Google Sheet.\n"
    "Make sure the spreadsheet is shared with the service account email:\n"
    "`streamlit-g-sheet-dashboard-vo@axiomatic-idiom-496012-p8.iam.gserviceaccount.com`"
)

# ---------- Main Content ----------
st.header(f"📄 {selected_sheet}")

with st.spinner(f"Loading {selected_sheet} ..."):
    df = load_sheet_data(selected_sheet)

if not df.empty:
    st.write(f"**Rows:** {df.shape[0]} | **Columns:** {df.shape[1]}")
    st.dataframe(df, use_container_width=True)

    # Optional: download as CSV
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download as CSV",
        data=csv,
        file_name=f"{selected_sheet.replace(' ', '_')}.csv",
        mime="text/csv",
    )
else:
    st.warning("No data could be loaded. Check your secrets and sheet permissions.")

# ---------- Footer ----------
st.markdown("---")
st.caption("Powered by Google Sheets & Streamlit")