import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import json
import re
from datetime import datetime

# ---------- Page config ----------
st.set_page_config(page_title="NSE Stock Dashboard", layout="wide")
st.title("📊 NSE Stock Market Dashboard")
st.caption(f"Data refreshed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# ---------- Helper: extract URL from Google Sheets HYPERLINK formula ----------
def extract_hyperlink(url_or_formula):
    """
    If the cell contains =HYPERLINK("url","label") -> return the url.
    Otherwise return the original value.
    """
    if isinstance(url_or_formula, str) and url_or_formula.startswith("=HYPERLINK("):
        # extract the first quoted string after the opening parenthesis
        match = re.search(r'=HYPERLINK\("([^"]+)"', url_or_formula)
        if match:
            return match.group(1)
    return url_or_formula

# ---------- Load Google Sheet (handles duplicate headers & hyperlinks) ----------
@st.cache_data(ttl=300)
def load_sheet_data(sheet_name):
    try:
        # 1. Authenticate
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

        # 2. Get all values (including formulas)
        all_values = worksheet.get_all_values()
        if not all_values:
            return pd.DataFrame()

        # 3. Clean headers – first row
        raw_headers = all_values[0]
        # Remove empty strings, make unique by appending "_dupX" if duplicates
        seen = {}
        clean_headers = []
        for h in raw_headers:
            if h == "":
                h = "empty_column"
            if h in seen:
                seen[h] += 1
                h = f"{h}_{seen[h]}"
            else:
                seen[h] = 0
            clean_headers.append(h)

        # 4. Build DataFrame from remaining rows
        data_rows = all_values[1:]
        df = pd.DataFrame(data_rows, columns=clean_headers)

        # 5. Convert HYPERLINK formulas in specific columns to clickable HTML
        hyperlink_columns = [
            "Trading View", "History Data", "Screener", "Zerodha", "Chartlink",
            "Market smith india", "NSE Chart", "Official NSE URL", "NSE 1",
            "Trading View 1", "History Data 1", "Screener 1", "Zerodha 1",
            "Chartlink 1", "Market smith india 1", "Official NSE URL 1"
        ]

        for col in hyperlink_columns:
            if col in df.columns:
                # Extract URL from formula and create HTML link
                df[col] = df[col].apply(extract_hyperlink)
                df[col] = df[col].apply(
                    lambda x: f'<a href="{x}" target="_blank">🔗 Link</a>' if pd.notna(x) and str(x).startswith("http") else x
                )

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

# ---------- Main area ----------
st.header(f"📄 {selected_sheet}")

with st.spinner("Loading data..."):
    df = load_sheet_data(selected_sheet)

if not df.empty:
    st.write(f"**Rows:** {df.shape[0]} | **Columns:** {df.shape[1]}")

    # Display with HTML rendering enabled for clickable links
    st.markdown(
        df.to_html(escape=False, index=False),
        unsafe_allow_html=True
    )

    # Optional: Download CSV (original data, without HTML tags)
    csv = df.replace(r'<a href="([^"]+)".*', r'\1', regex=True).to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download as CSV", csv, f"{selected_sheet.replace(' ', '_')}.csv", "text/csv")

else:
    st.warning("No data loaded. Check sheet sharing and secrets.")

st.markdown("---")
st.caption("Powered by Google Sheets & Streamlit")
