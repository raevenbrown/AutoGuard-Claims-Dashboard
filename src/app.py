import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration Setup
st.set_page_config(page_title="AutoGuard Corporate Intelligence", layout="wide")
st.title("🛡️ AutoGuard Corporate Reporting & Analytics Hub")
st.markdown("Enterprise Operational Intelligence Platform | Multi-Department Auditing & Trend Analysis.")
st.write("---")

# 2. Ingest the Data (Expanded with Historical Months for Financial Trend Charting)
reporting_data = {
    "claim_id": [101, 102, 103, 104, 105, 106, 107],
    "reporting_month": ["January", "February", "March", "April", "May", "June", "June"],
    "submission_date": ["2026-01-15", "2026-02-18", "2026-03-20", "2026-04-22", "2026-05-24", "2026-06-25", "2026-06-26"],
    "customer_name": ["Alice Smith", "Bob Jones", "Charlie Brown", "Diana Prince", "Evan Wright", "Fiona Gallagher", "George Clark"],
    "age": [28, 45, 62, 31, 51, 22, 39],
    "gender": ["Female", "Male", "Male", "Female", "Male", "Female", "Male"],
    "account_type": ["Private", "Commercial", "Private", "Private", "Commercial", "Private", "Commercial"],
    "car_model": ["Kia Optima", "Ford F-150", "Kia Optima", "Honda Civic", "Ford F-150", "Honda Civic", "Kia Optima"],
    "part_needed": ["Alternator", "Torque Converter", "Wiring Harness", "Brake Pads", "Clutch Pack", "Air Filter", "Gearbox Set"],
    "claim_type": ["Electrical", "Transmission", "Electrical", "Routine", "Transmission", "Routine", "Transmission"],
    "mechanic_shop": ["Pep Boys", "Precision Auto", "Pep Boys", "Local Shop B", "Precision Auto", "Local Shop B", "Pep Boys"],
    "insurance_provider": ["State Farm", "Geico", "Progressive", "Allstate", "State Farm", "Geico", "Progressive"],
    "days_in_shop": [14, 11, 9, 7, 5, 4, 3],
    "rental_car_allocated": ["Yes", "Yes", "No", "No", "Yes", "No", "Yes"],
    "rental_vendor": ["Hertz", "Enterprise", "None", "None", "Hertz", "None", "Enterprise"],
    "daily_rental_allowance": [45.00, 50.00, 0.00, 0.00, 45.00, 0.00, 50.00],
    "repair_cost": [1200.00, 850.00, 3400.00, 500.00, 2100.00, 975.00, 4800.00],
    "claim_status": ["Approved", "Pending", "Approved", "Denied", "Pending", "Denied", "Approved"],
    "suggested_csr_script": [
        "Your electrical claim at Pep Boys was approved. Alternator parts covered. Hertz rental active ($45/day).",
        "Transmission review pending at Precision Auto. Torque converter on backlog. Enterprise rental covered ($50/day).",
        "Electrical claim authorized at Pep Boys. Wiring harness allocation cleared. No rental requested.",
        "Claim Denied: Routine maintenance for brake pads is excluded from this powertrain baseline coverage.",
        "Transmission claim pending review at Precision Auto for clutch pack authorization. Hertz rental active ($45/day).",
        "Claim Denied: Air filter swap is categorized as non-covered standard user preventative maintenance.",
        "High-priority transmission claim authorized at Pep Boys. Gearbox set fully covered. Enterprise rental active ($50/day)."
    ]
}
df = pd.DataFrame(reporting_data)

# 3. Sidebar Filter Operations (The Control Room)
st.sidebar.header("📁 Data Ingestion Controls")
uploaded_file = st.sidebar.file_uploader("Upload Processing Payload (.csv)", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

st.sidebar.write("---")
st.sidebar.header("🎛️ Master Analytical Filters")

# Status State Filter
status_filter = st.sidebar.multiselect(
    "Filter System State:",
    options=df["claim_status"].unique(),
    default=df["claim_status"].unique()
)

# NEW REQUEST: Account Type Filter (Private vs Commercial)
account_filter = st.sidebar.multiselect(
    "Filter Policy Classification:",
    options=df["account_type"].unique(),
    default=df["account_type"].unique()
)

# Apply Combined Filtering Logic
filtered_df = df[(df["claim_status"].isin(status_filter)) & (df["account_type"].isin(account_filter))]


# 4. 💼 ROW 1: EXECUTIVE OPERATIONAL SUMMARY (MOVED TO THE TOP)
st.header("💼 Executive Operational Summary")
col1, col2, col3, col4 = st.columns(4)

total_exposure = filtered_df["repair_cost"].sum()
pending_liquidity = filtered_df[filtered_df["claim_status"] == "Pending"]["repair_cost"].sum()
avg_cycle_time = filtered_df["days_in_shop"].mean() if len(filtered_df) > 0 else 0
total_active_rentals = len(filtered_df[filtered_df["rental_car_allocated"] == "Yes"])

with col1:
    st.metric(label="Total Financial Exposure", value=f"${total_exposure:,.2f}")
with col2:
    st.metric(label="Pending Liquidity Reserve", value=f"${pending_liquidity:,.2f}")
with col3:
    st.metric(label="Avg Shop Cycle Time", value=f"{avg_cycle_time:.1f} Days")
with col4:
    st.metric(label="Active Rental Allocations", value=f"{total_active_rentals} Contracts")

st.write("---")


# 5. 📉 NEW REQUEST: MONTH-BY-MONTH FINANCIAL OUTFLOW TRENDS
st.header("📉 Financial Outflow Trends (Finance Department Reporting)")
st.markdown("*Chronological progression tracking net claim liabilities across fiscal periods.*")

# Sort data sequentially by month order for proper visualization flow
month_order = ["January", "February", "March", "April", "May", "June"]
monthly_summary = filtered_df.groupby("reporting_month")["repair_cost"].sum().reindex(month_order).reset_index().fillna(0)

fig_trend = px.line(
    monthly_summary, 
    x="reporting_month", 
    y="repair_cost", 
    text="repair_cost",
    title="Month-over-Month Gross Claim Liabilities ($)",
    labels={"reporting_month": "Fiscal Month", "repair_cost": "Total Claims Paid ($)"},
    markers=True
)
fig_trend.update_traces(textposition="top center", line_color="#1565C0")
st.plotly_chart(fig_trend, use_container_width=True)

st.write("---")


# 6. 🎯 ROW 3: TARGETED STRATEGY CHARTS
st.header("🎯 Multi-Department Operational Matrix")
chart_col1, chart_col2 = px_cols = st.columns(2)

with chart_col1:
    st.subheader("📈 Product Marketing Risk Matrix")
    fig_demog = px.sunburst(
        filtered_df, 
        path=["account_type", "car_model", "gender"], 
        values="repair_cost",
        title="Claim Cost Volatility by Segment"
    )
    st.plotly_chart(fig_demog, use_container_width=True)

with chart_col2:
    st.subheader("📊 Liquidity Allocation Structure")
    fig_status = px.pie(
        filtered_df, 
        values="repair_cost", 
        names="claim_status", 
        hole=0.4,
        title="Asset Allocation by Lifecycle Status",
        color_discrete_map={"Approved": "#2E7D32", "Pending": "#1565C0", "Denied": "#C62828"}
    )
    st.plotly_chart(fig_status, use_container_width=True)

st.write("---")


# 7. 👥 ROW 4: CUSTOMER SUPPORT PORTAL
st.header("👥 Front-Line Customer Support Portal")
display_cols = [
    "claim_id", "submission_date", "customer_name", "insurance_provider", 
    "car_model", "part_needed", "days_in_shop", "rental_car_allocated", 
    "rental_vendor", "daily_rental_allowance", "repair_cost", "claim_status", "suggested_csr_script"
]
st.dataframe(filtered_df[display_cols], use_container_width=True)
