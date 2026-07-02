import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Main Page Canvas Configuration
st.set_page_config(page_title="AutoGuard Core Enterprise OS", layout="wide")

# 2. Ingest the Robust Data Core
reporting_data = {
    "claim_id": [101, 102, 103, 104, 105, 106, 107],
    "reporting_quarter": ["Q1 2026", "Q1 2026", "Q2 2026", "Q2 2026", "Q2 2026", "Q2 2026", "Q2 2026"],
    "reporting_month": ["January", "February", "March", "April", "May", "June", "June"],
    "customer_name": ["Alice Smith", "Bob Jones", "Charlie Brown", "Diana Prince", "Evan Wright", "Fiona Gallagher", "George Clark"],
    "account_type": ["Private", "Commercial", "Private", "Private", "Commercial", "Private", "Commercial"],
    "car_model": ["Kia Optima", "Ford F-150", "Kia Optima", "Honda Civic", "Ford F-150", "Honda Civic", "Kia Optima"],
    "part_needed": ["Alternator", "Torque Converter", "Wiring Harness", "Brake Pads", "Clutch Pack", "Air Filter", "Gearbox Set"],
    "claim_type": ["Electrical", "Transmission", "Electrical", "Routine", "Transmission", "Routine", "Transmission"],
    "mechanic_shop": ["Pep Boys", "Precision Auto", "Pep Boys", "Local Shop B", "Precision Auto", "Local Shop B", "Pep Boys"],
    "insurance_provider": ["State Farm", "Geico", "Progressive", "Allstate", "State Farm", "Geico", "Progressive"],
    "days_in_shop": [14, 11, 9, 7, 5, 4, 3],
    "rental_car_allocated": ["Yes", "Yes", "No", "No", "Yes", "No", "Yes"],
    "rental_car_type": ["Midsize Sedan", "Fullsize SUV", "None", "None", "Compact Sedan", "None", "Fullsize SUV"],
    "rental_duration_days": [10, 14, 0, 0, 7, 0, 5],
    "daily_rental_allowance": [45.00, 50.00, 0.00, 0.00, 45.00, 0.00, 50.00],
    "parts_cost": [800.00, 500.00, 2400.00, 200.00, 1500.00, 475.00, 3300.00],
    "labor_cost": [400.00, 350.00, 1000.00, 300.00, 600.00, 500.00, 1500.00],
    "repair_cost": [1200.00, 850.00, 3400.00, 500.00, 2100.00, 975.00, 4800.00],
    "claim_status": ["Approved", "Pending", "Approved", "Denied", "Pending", "Denied", "Approved"],
    "funnel_stage": ["Closed Authorized", "Engineering Audit", "Closed Authorized", "Denied Static", "Parts Valuation", "Denied Static", "Closed Authorized"],
    "suggested_csr_script": [
        "Your electrical claim at Pep Boys was approved. Alternator parts covered. Midsize Sedan active for 10 days ($45/day).",
        "Transmission review pending at Precision Auto. Torque converter on backlog. Fullsize SUV rental approved for 14 days ($50/day).",
        "Electrical claim authorized at Pep Boys. Wiring harness allocation cleared. No rental requested.",
        "Claim Denied: Routine maintenance for brake pads is excluded from this powertrain baseline coverage.",
        "Transmission claim pending review at Precision Auto for clutch pack authorization. Compact Sedan active for 7 days ($45/day).",
        "Claim Denied: Air filter swap is categorized as non-covered standard user preventative maintenance.",
        "High-priority transmission claim authorized at Pep Boys. Gearbox set fully covered. Fullsize SUV rental active for 5 days ($50/day)."
    ]
}
df = pd.DataFrame(reporting_data)

# 3. Sidebar: Left-Hand Navigation Dashboard Core (Gemini / Creative Metrics Style)
st.sidebar.title("🛡️ AutoGuard OS")
st.sidebar.markdown("**Network Mesh:** `● Sync Active`")
st.sidebar.write("---")

# Left Sidebar Navigation Toggles
st.sidebar.subheader("🏁 Main Navigator")
app_mode = st.sidebar.radio(
    "Select Interface View:",
    ["👥 Customer Overview", "🏪 Shop & Cost Overview", "💰 Sales & Quarter Overview"]
)

st.sidebar.write("---")
st.sidebar.subheader("🎛️ Dynamic Target Filters")
status_filter = st.sidebar.multiselect("Claim Status Filter:", options=df["claim_status"].unique(), default=df["claim_status"].unique())
account_filter = st.sidebar.multiselect("Account Profile Slicer:", options=df["account_type"].unique(), default=df["account_type"].unique())

filtered_df = df[(df["claim_status"].isin(status_filter)) & (df["account_type"].isin(account_filter))]

# File Ingestion Tooling placed neatly at the bottom of left sidebar controls
st.sidebar.write("---")
uploaded_file = st.sidebar.file_uploader("Upload Payload Ingestion Batch (.csv)", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)


# 4. Main Right Canvas Header Logic
st.title("AutoGuard Corporate Reporting Platform")
st.markdown(f"Currently viewing: **{app_mode}**")
st.write("---")


# ==========================================
# VIEW 1: CUSTOMER OVERVIEW (THE RETENTION STORY)
# ==========================================
if app_mode == "👥 Customer Overview":
    st.header("👥 Front-Line Customer Experience Registry")
    st.markdown("##### *Eliminating customer churn and drop-off anxiety through total communication clarity.*")
    st.write("")
    
    # Quick Summary Cards specialized just for Customer Ops
    c_m1, c_m2 = st.columns(2)
    with c_m1:
        st.metric("Total Active Claims Tracked", value=len(filtered_df))
    with c_m2:
        st.metric("Active Vehicle Fleet Rentals Out", value=len(filtered_df[filtered_df["rental_car_allocated"] == "Yes"]))
    st.write("")
    
    customer_cols = [
        "claim_id", "customer_name", "insurance_provider", "car_model", 
        "rental_car_allocated", "rental_car_type", "rental_duration_days", 
        "daily_rental_allowance", "claim_status", "suggested_csr_script"
    ]
    st.dataframe(filtered_df[customer_cols], use_container_width=True)


# ==========================================
# VIEW 2: SHOP & COST OVERVIEW (THE OPERATIONS STORY)
# ==========================================
elif app_mode == "🏪 Shop & Cost Overview":
    st.header("🏪 Repair Network Costs & Integrity Matrix")
    st.markdown("##### *Monitoring network repair cycle times and component resource distribution splits.*")
    st.write("")
    
    # Metric scorecards tailored for Finance/Ops
    total_parts = filtered_df["parts_cost"].sum()
    total_labor = filtered_df["labor_cost"].sum()
    st.subheader(f"Total Operational Outflow: ${(total_parts + total_labor):,.2f}")
    st.write("")
    
    s_col1, s_col2 = st.columns(2)
    with s_col1:
        cost_mix = pd.DataFrame({"Component": ["Parts Matrix", "Labor Allocation"], "Expense Amount": [total_parts, total_labor]})
        fig_donut = px.pie(cost_mix, values="Expense Amount", names="Component", hole=0.5,
                           title="Material Parts vs. Internal Labor Expense Mix",
                           color_discrete_sequence=["#9C27B0", "#E040FB"])
        st.plotly_chart(fig_donut, use_container_width=True)
        
    with s_col2:
        fig_bay = px.bar(filtered_df, x="mechanic_shop", y="days_in_shop", color="car_model", barmode="group",
                         title="Average Machine Cycle Days by Location Partner",
                         labels={"mechanic_shop": "Repair Network Facility", "days_in_shop": "Days Elapsed in Shop"})
        st.plotly_chart(fig_bay, use_container_width=True)


# ==========================================
# VIEW 3: SALES & QUARTER OVERVIEW (THE REVENUE STORY)
# ==========================================
elif app_mode == "💰 Sales & Quarter Overview":
    st.header("💰 Booking Volume Pipeline & Conversion Funnel")
    st.markdown("##### *Evaluating processing lifecycle velocities and fiscal performance curves.*")
    st.write("")
    
    # High executive metrics pinned right at the gates of revenue
    total_payout = filtered_df[filtered_df["claim_status"] == "Approved"]["repair_cost"].sum()
    sa_m1, sa_m2 = st.columns(2)
    with sa_m1:
        st.metric("Total Net Authorized Payouts", value=f"${total_payout:,.2f}")
    with sa_m2:
        st.metric("Current Backlog Queue Count", value=len(filtered_df[filtered_df["claim_status"] == "Pending"]))
    st.write("")
    
    sa_col1, sa_col2 = st.columns(2)
    with sa_col1:
        fig_sales_q = px.bar(filtered_df, x="reporting_quarter", y="repair_cost", color="claim_status",
                             title="Gross Booking Volume Distributions",
                             labels={"reporting_quarter": "Fiscal Period Mark", "repair_cost": "Booking Volume Valuation ($)"},
                             color_discrete_map={"Approved": "#2E7D32", "Pending": "#1565C0", "Denied": "#C62828"})
        st.plotly_chart(fig_sales_q, use_container_width=True)
        
    with sa_col2:
        sales_funnel = filtered_df.groupby("funnel_stage")["repair_cost"].sum().reset_index().sort_values(by="repair_cost", ascending=False)
        fig_sales_funnel = px.funnel(sales_funnel, x="repair_cost", y="funnel_stage",
                                     title="Financial Pipeline Velocity Stages",
                                     labels={"repair_cost": "Total Value in Stage ($)", "funnel_stage": "System Stage"})
        st.plotly_chart(fig_sales_funnel, use_container_width=True)
