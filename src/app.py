import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration Setup
st.set_page_config(page_title="AutoGuard Intelligence Platform", layout="wide")
st.title("🛡️ AutoGuard Corporate Reporting & Narrative Hub")
st.markdown("### Strategic Analytics Engine: Transforming Underwriting Risk into Operational Capital")
st.write("---")

# 2. Ingest the Enhanced Structural Reporting Data
narrative_data = {
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
df = pd.DataFrame(narrative_data)

# 3. Sidebar Filter Operations (The Strategic Control Panel)
st.sidebar.header("📁 Control Panel")
uploaded_file = st.sidebar.file_uploader("Upload Claims Matrix (.csv)", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

st.sidebar.write("---")
st.sidebar.header("🎯 Master Cohort Slicers")

status_filter = st.sidebar.multiselect("Claim Lifecycle Status:", options=df["claim_status"].unique(), default=df["claim_status"].unique())
account_filter = st.sidebar.multiselect("Policy Account Profile:", options=df["account_type"].unique(), default=df["account_type"].unique())
shop_filter = st.sidebar.multiselect("Mechanic Shop Network:", options=df["mechanic_shop"].unique(), default=df["mechanic_shop"].unique())

# Apply Master Slicers
filtered_df = df[
    (df["claim_status"].isin(status_filter)) & 
    (df["account_type"].isin(account_filter)) &
    (df["mechanic_shop"].isin(shop_filter))
]

# 4. ACT 1: THE EXECUTIVE FINANCIAL OVERVIEW (Top Strategic Summary)
st.header("📊 Act 1: Executive Capital Allocation & Financial Health")
col1, col2, col3, col4 = st.columns(4)

total_exposure = filtered_df["repair_cost"].sum()
pending_liquidity = filtered_df[filtered_df["claim_status"] == "Pending"]["repair_cost"].sum()
avg_cycle_time = filtered_df["days_in_shop"].mean() if len(filtered_df) > 0 else 0
total_active_rentals = len(filtered_df[filtered_df["rental_car_allocated"] == "Yes"])

with col1:
    st.metric(label="Gross Financial Exposure", value=f"${total_exposure:,.2f}", delta="Underwriting Target")
with col2:
    st.metric(label="Pending Liquidity Reserve (Risk)", value=f"${pending_liquidity:,.2f}", delta="Requires Verification", delta_color="inverse")
with col3:
    st.metric(label="Mean Cycle Time (Friction)", value=f"{avg_cycle_time:.1f} Days", delta="Target <= 7 Days")
with col4:
    st.metric(label="Active Rental Fleet Leases", value=f"{total_active_rentals} Contracts", delta="Vendor Exposure")

st.write("---")

# 5. ACT 2: CHRONOLOGICAL FINANCIAL LOSS RATIOS (Historical Outflow Trend)
st.subheader("📉 Chronicle Timeline: Liabilities over Time")
month_order = ["January", "February", "March", "April", "May", "June"]
monthly_summary = filtered_df.groupby(["reporting_month", "claim_status"])["repair_cost"].sum().reset_index()

fig_trend = px.area(
    monthly_summary, 
    x="reporting_month", 
    y="repair_cost", 
    color="claim_status",
    title="Chronological Outflow Trends: Net Liquidity Allocations",
    labels={"reporting_month": "Fiscal Month", "repair_cost": "Aggregated Outflow ($)"},
    category_orders={"reporting_month": month_order},
    color_discrete_map={"Approved": "#2E7D32", "Pending": "#1565C0", "Denied": "#C62828"}
)
st.plotly_chart(fig_trend, use_container_width=True)

st.write("---")

# 6. ACT 3: SEGMENTATION & MARKET UNDERWRITING TRAPS (The Refactored Multi-Department Matrix)
st.header("🎯 Act 2: Multi-Department Segment Analysis")
st.markdown("#### Discovering Profitability Bottlenecks Across Product, Marketing, and Operations Layers")

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("🏎️ Underwriting Matrix: Vehicle Loss Volatility")
    st.markdown("*Used by **Product Marketing** to instantly flag vehicle lines leaking capital due to structural/component trends.*")
    
    fig_car_bar = px.bar(
        filtered_df,
        x="repair_cost",
        y="car_model",
        color="claim_type",
        barmode="group",
        title="Gross Claims Exposure Across Vehicular Profiles",
        labels={"repair_cost": "Total Financial Leakage ($)", "car_model": "Vehicle Classification"}
    )
    st.plotly_chart(fig_car_bar, use_container_width=True)

with chart_col2:
    st.subheader("🏪 Vendor Network Integrity Portal")
    st.markdown("*Used by **Operations & Partnership Teams** to audit mechanic behavior and vendor compliance guidelines.*")
    
    fig_vendor_stack = px.bar(
        filtered_df,
        x="mechanic_shop",
        y="repair_cost",
        color="claim_status",
        title="Network Vendor Approval/Denial Ratios & Financial Footprint",
        labels={"mechanic_shop": "Repair Network Facility Location", "repair_cost": "Total Billed Assets ($)"},
        color_discrete_map={"Approved": "#2E7D32", "Pending": "#1565C0", "Denied": "#C62828"}
    )
    st.plotly_chart(fig_vendor_stack, use_container_width=True)

st.write("---")

# 7. ACT 4: TRANSLATING COMPLIANCE INTO TRUST (Customer Support Hub)
st.header("👥 Act 3: Front-Line Policy Communication Portal")
st.markdown("#### Instantly Empowering Front-Line Reps to Explain Complex Backend Database Logic Clear as Day")

display_cols = [
    "claim_id", "submission_date", "customer_name", "insurance_provider", 
    "car_model", "part_needed", "days_in_shop", "rental_car_allocated", 
    "rental_vendor", "daily_rental_allowance", "repair_cost", "claim_status", "suggested_csr_script"
]
st.dataframe(filtered_df[display_cols], use_container_width=True)
