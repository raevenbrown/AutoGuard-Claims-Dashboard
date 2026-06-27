import streamlit as st
import pandas as pd

# 1. Page Configuration Setup
st.set_page_config(page_title="AutoGuard Claims Dashboard", layout="wide")
st.title("🛡️ AutoGuard Executive Claims Dashboard")
st.markdown("Real-time interactive analytics pipeline for automotive warranty claim lifecycle evaluation.")
st.write("---")

# 2. Ingest the Data (Your existing logic)
claims_data = {
    "claim_id": [101, 102, 103, 104, 105, 106, 107],
    "vehicle_id": [1, 2, 3, 4, 1, 3, 2],
    "repair_cost": [1200.00, 850.00, 3400.00, 500.00, 2100.00, 975.00, 4800.00],
    "claim_status": ["Approved", "Pending", "Approved", "Denied", "Pending", "Denied", "Approved"]
}
df = pd.DataFrame(claims_data)

# 3. Sidebar Filtering Logic for Interactivity
st.sidebar.header("Dashboard Filters")
status_filter = st.sidebar.multiselect(
    "Filter by Claim Status:",
    options=df["claim_status"].unique(),
    default=df["claim_status"].unique()
)

# Apply Filter
filtered_df = df[df["claim_status"].isin(status_filter)]

# 4. Interactive KPI Cards (Phase 3 Visual Layer)
total_exposure = filtered_df["repair_cost"].sum()
avg_cost = filtered_df["repair_cost"].mean() if len(filtered_df) > 0 else 0
claim_count = len(filtered_df)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Financial Exposure", value=f"${total_exposure:,.2f}")
with col2:
    st.metric(label="Average Cost Per Claim", value=f"${avg_cost:,.2f}")
with col3:
    st.metric(label="Total Claims Tracked", value=str(claim_count))

st.write("---")

# 5. Data Table Presentation
st.subheader("📋 Filtered Claims Record Log")
st.dataframe(filtered_df, use_container_width=True)
