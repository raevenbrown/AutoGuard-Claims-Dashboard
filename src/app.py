import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Main Page Canvas Configuration
st.set_page_config(page_title="AutoGuard Core Enterprise OS", layout="wide")

# 2. Ingest the Detailed Structural Data Core
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

# 3. Sidebar Configuration Controls (Moved up and re-styled as an Account Profile Sync)
st.sidebar.title("👤 Agent Profile: Active Session")
st.sidebar.markdown("**Logged In Rep:** `CSR_ID_9052` ")
st.sidebar.markdown("**Network Mesh:** `● Sync Secure`")

# Upload Button Moved High up to act like an Account Sync action
uploaded_file = st.sidebar.file_uploader("🔄 Sync Profile / Ingest Local CSV Batch Data", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

st.sidebar.write("---")

# Left Sidebar Navigation Toggles
st.sidebar.subheader("🏁 Navigation Console")
app_mode = st.sidebar.radio(
    "Select System Panel View:",
    ["👥 Customer Overview", "🏪 Shop & Cost Overview", "💰 Sales & Quarter Overview"]
)

st.sidebar.write("---")
st.sidebar.subheader("🎛️ Dynamic Data Filters")
status_filter = st.sidebar.multiselect("Claim Status:", options=df["claim_status"].unique(), default=df["claim_status"].unique())
account_filter = st.sidebar.multiselect("Policy Account Profile:", options=df["account_type"].unique(), default=df["account_type"].unique())

filtered_df = df[(df["claim_status"].isin(status_filter)) & (df["account_type"].isin(account_filter))]


# 4. Main Right Canvas Header
st.title("🛡️ AutoGuard Corporate Reporting Platform")
st.markdown(f"Current Dashboard Console Profile: **{app_mode}**")
st.write("---")


# ==========================================
# VIEW 1: CUSTOMER OVERVIEW (THE RETENTION STORY)
# ==========================================
if app_mode == "👥 Customer Overview":
    st.header("👥 Front-Line Customer Experience Registry")
    st.markdown("##### *Eliminating customer churn and drop-off anxiety through total communication clarity.*")
    st.write("")
    
    c_m1, c_m2 = st.columns(2)
    with c_m1:
        st.metric("Total Active Customer Records Evaluated", value=len(filtered_df))
    with c_m2:
        st.metric("Active Managed Rental Contracts Dispatched", value=len(filtered_df[filtered_df["rental_car_allocated"] == "Yes"]))
    st.write("")
    
    customer_cols = [
        "claim_id", "customer_name", "insurance_provider", "car_model", 
        "rental_car_allocated", "rental_car_type", "rental_duration_days", 
        "daily_rental_allowance", "claim_status", "suggested_csr_script"
    ]
    st.dataframe(filtered_df[customer_cols], use_container_width=True)
    
    st.write("---")
    st.subheader("📝 Live CRM Case Logger Notes")
    st.markdown("*Select a Case/Customer record from the table above to log a real-time manual update interaction below.*")
    
    # NEW REQUEST: Case note logging entry mechanism
    target_id = st.selectbox("Select Target Claim ID to Append:", options=filtered_df["claim_id"].unique())
    user_notes = st.text_input(label="Type Caller Interaction / Status Verification Update Log Note:")
    if user_notes:
        st.success(f"Successfully pinned case log entry update for Claim #{target_id}: '{user_notes}'")


# ==========================================
# VIEW 2: SHOP & COST OVERVIEW (THE OPERATIONS STORY)
# ==========================================
elif app_mode == "🏪 Shop & Cost Overview":
    st.header("🏪 Repair Network Costs & Integrity Matrix")
    st.markdown("##### *Monitoring network repair cycle times and component resource distribution splits.*")
    st.write("")
    
    total_parts = filtered_df["parts_cost"].sum()
    total_labor = filtered_df["labor_cost"].sum()
    st.subheader(f"Gross Fleet Operational Outflow Volume: ${(total_parts + total_labor):,.2f}")
    st.write("")
    
    s_col1, s_col2 = st.columns(2)
    with s_col1:
        # NEW REQUEST: Highly descriptive cost component re-mapping
        cost_mix = pd.DataFrame({
            "Cost Metric Classification": ["Raw Mechanical Replacement Parts Cost", "Mechanic Technical Labor Billing"], 
            "Aggregated Outflow": [total_parts, total_labor]
        })
        fig_donut = px.pie(cost_mix, values="Aggregated Outflow", names="Cost Metric Classification", hole=0.5,
                           title="Financial Split: Capital Disbursed to Parts vs. Labor Hours",
                           color_discrete_sequence=["#9C27B0", "#E040FB"])
        st.plotly_chart(fig_donut, use_container_width=True)
        st.caption("**Analytical Breakdown Explanation:** This donut distribution splits the total capital layout. It shows how much money was strictly allocated to purchasing mechanical replacement hardware items versus how much was spent paying out the garage technician's hourly labor invoice fees.")
        
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
    
    # NEW REQUEST: Detailed Policy Denial audit context logic
    st.write("---")
    st.subheader("🕵️‍♂️ Risk Mitigation Audit Log: System Denial Reasons")
    st.markdown("Executive context mapping exactly why specific data values were filtered out or denied during systemic pipeline checks:")
    st.info("💡 **Policy Exclusion Code 401 (Routine Braking Systems):** Component requested was classified as routine friction wear-and-tear pads. Powertrain policies strictly cover mechanical engine and internal gearing component failures, preventing systemic margin bleeding on standard wear items.")
    st.info("💡 **Policy Exclusion Code 402 (Air Filtration Units):** Filter intake element replacements fall under basic preventative owner maintenance guidelines and do not meet the structural threshold requirements for mechanical claim insurance allocation.")
