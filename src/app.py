import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# 1. Page Configuration Setup
st.set_page_config(page_title="AutoGuard Enterprise Ecosystem", layout="wide")
st.title("🛡️ AutoGuard Enterprise Operations Platform")
st.markdown("Centralized Core System: Cross-Department Intelligence Platform.")
st.write("---")

# 2. Ingest the Data (The Mega Enterprise Dataset)
enterprise_claims_data = {
    "claim_id": [101, 102, 103, 104, 105, 106, 107],
    "submission_date": ["2026-06-15", "2026-06-18", "2026-06-20", "2026-06-22", "2026-06-24", "2026-06-25", "2026-06-26"],
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
df = pd.DataFrame(enterprise_claims_data)

# 3. Sidebar Configuration (The Control Room)
st.sidebar.header("📁 System Controls")
st.sidebar.markdown("**Database Mesh Status:** `● Sync Active` ")
uploaded_file = st.sidebar.file_uploader("Ingest Batch Processing Payload (.csv)", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

st.sidebar.write("---")

# Global System Filters (Putting your requested filters back at the very top)
st.sidebar.header("🎛️ Master Status Controls")
status_filter = st.sidebar.multiselect(
    "Filter System State:",
    options=df["claim_status"].unique(),
    default=df["claim_status"].unique()
)
filtered_df = df[df["claim_status"].isin(status_filter)]

# 4. 👥 ROW 1: THE FRONT-LINE CUSTOMER SUPPORT HUB (Moved Up)
st.header("👥 Customer Support Hub & Smart CSR Scripting")
st.markdown("*Agents leverage this upper portal for instantaneous phone support, rental tracking, and policy transparency.*")

display_cols = [
    "claim_id", "submission_date", "customer_name", "insurance_provider", 
    "car_model", "part_needed", "days_in_shop", "rental_car_allocated", 
    "rental_vendor", "daily_rental_allowance", "repair_cost", "claim_status", "suggested_csr_script"
]
st.dataframe(filtered_df[display_cols], use_container_width=True)
st.write("---")

# 5. 🎯 ROW 2: THE STRATEGIC STRATIFICATION CHARTS (Marketing / Product / Finance)
st.header("🎯 Multi-Department Operational Matrix")

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("📈 Product Marketing & Actuarial Risk Layer")
    # Interactive distribution chart checking demographics, account types, and car lines
    fig_demog = px.sunburst(
        filtered_df, 
        path=["account_type", "car_model", "gender"], 
        values="repair_cost",
        title="Claim Volume Mix by Account Type, Car Model, and Gender"
    )
    st.plotly_chart(fig_demog, use_container_width=True)

with chart_col2:
    st.subheader("💰 Finance & Operations Claims Matrix")
    # Matching your reference dashboard concept: Claim amount vs Status tracking
    fig_status = px.pie(
        filtered_df, 
        values="repair_cost", 
        names="claim_status", 
        hole=0.4,
        title="Financial Allocation Breakdown by Active Claim Status",
        color_discrete_map={"Approved": "#2E7D32", "Pending": "#1565C0", "Denied": "#C62828"}
    )
    st.plotly_chart(fig_status, use_container_width=True)

st.write("---")

# 6. 💼 ROW 3: REVENUE PROTECTION & PIPELINE EFFICIENCY (Finance & Network Operations)
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
    st.metric(label="Active Rental Fleet Allocations", value=f"{total_active_rentals} Contracts")
