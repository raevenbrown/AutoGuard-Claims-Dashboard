import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Main Page Canvas Configuration
st.set_page_config(page_title="AutoGuard Core Enterprise OS", layout="wide")

# 2. Ingest the Robust Cross-Vehicle Data Core (Complete 10-Row Enterprise Dataset)
reporting_data = {
    "claim_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "reporting_quarter": ["Q1 2026", "Q1 2026", "Q2 2026", "Q2 2026", "Q2 2026", "Q2 2026", "Q2 2026", "Q2 2026", "Q2 2026", "Q2 2026"],
    "reporting_month": ["January", "February", "March", "April", "May", "June", "June", "June", "June", "June"],
    "customer_name": ["Alice Smith", "Bob Jones", "Charlie Brown", "Diana Prince", "Evan Wright", "Fiona Gallagher", "George Clark", "Henry Cavill", "Iris West", "Jack Reacher"],
    "account_type": ["Private", "Commercial", "Private", "Private", "Commercial", "Private", "Commercial", "Private", "Commercial", "Private"],
    "car_model": ["Kia Optima", "Ford F-150", "BMW 3-Series", "Honda Civic", "Audi A4", "Toyota Camry", "Nissan Altima", "BMW 3-Series", "Toyota Camry", "Audi A4"],
    "part_needed": ["Alternator", "Torque Converter", "Mechatronic Unit", "Brake Pads", "Turbocharger", "Air Filter", "Gearbox Set", "Steering Rack", "Water Pump", "Fuel Injectors"],
    "claim_type": ["Electrical", "Transmission", "Transmission", "Routine", "Engine", "Routine", "Transmission", "Electrical", "Engine", "Engine"],
    "mechanic_shop": ["Pep Boys", "Precision Auto", "Pep Boys", "Local Shop B", "Precision Auto", "Local Shop B", "Pep Boys", "Precision Auto", "Pep Boys", "Precision Auto"],
    "insurance_provider": ["State Farm", "Geico", "Progressive", "Allstate", "State Farm", "Geico", "Progressive", "Allstate", "State Farm", "Geico"],
    "days_in_shop": [14, 11, 22, 7, 19, 4, 3, 25, 5, 16],
    "rental_car_allocated": ["Yes", "Yes", "Yes", "No", "Yes", "No", "Yes", "Yes", "No", "Yes"],
    "rental_car_type": ["Midsize Sedan", "Fullsize SUV", "Luxury Sedan", "None", "Luxury Sedan", "None", "Fullsize SUV", "Luxury Sedan", "None", "Luxury Sedan"],
    "rental_duration_days": [10, 14, 21, 0, 14, 0, 5, 21, 0, 14],
    "daily_rental_allowance": [45.00, 50.00, 75.00, 0.00, 75.00, 0.00, 50.00, 75.00, 0.00, 75.00],
    "parts_cost": [800.00, 500.00, 4200.00, 200.00, 3100.00, 475.00, 3300.00, 2900.00, 350.00, 1800.00],
    "labor_cost": [400.00, 350.00, 1000.00, 300.00, 1200.00, 500.00, 1500.00, 1100.00, 250.00, 900.00],
    "repair_cost": [1200.00, 850.00, 3400.00, 500.00, 2100.00, 975.00, 4800.00, 4000.00, 600.00, 2700.00],
    "claim_status": ["Approved", "Pending", "Approved", "Denied", "Pending", "Denied", "Approved", "Approved", "Approved", "Approved"],
    "funnel_stage": ["Closed Authorized", "Engineering Audit", "Closed Authorized", "Denied Static", "Parts Valuation", "Denied Static", "Closed Authorized", "Closed Authorized", "Closed Authorized", "Closed Authorized"],
    "rental_vendor": ["Hertz", "Enterprise", "Hertz", "None", "Hertz", "None", "Enterprise", "Enterprise", "None", "Hertz"],
    "suggested_csr_script": [
        "Your electrical claim at Pep Boys was approved. Alternator parts covered. Midsize Sedan active for 10 days with Hertz ($45/day).",
        "Transmission review pending at Precision Auto. Torque converter on backlog. Fullsize SUV rental approved for 14 days with Enterprise ($50/day).",
        "BMW claim approved at Pep Boys. Luxury component allocation cleared. Hertz luxury rental active ($75/day).",
        "Claim Denied: Routine maintenance for brake pads is excluded from this powertrain baseline coverage.",
        "Audi engine claim pending at Precision Auto for turbocharger verification. Hertz luxury rental active ($75/day).",
        "Claim Denied: Air filter swap is categorized as non-covered standard user preventative maintenance.",
        "High-priority transmission claim authorized at Pep Boys. Gearbox set fully covered. Enterprise rental active ($50/day).",
        "BMW electrical claim authorized at Precision Auto. Steering rack verified. Enterprise active for 21 days.",
        "Toyota engine claim approved at Pep Boys. Water pump covered under standard baseline limits. No rental.",
        "Audi fuel injector claim authorized at Precision Auto. Parts cleared from European distribution node."
    ]
}
df = pd.DataFrame(reporting_data)

# 3. Sidebar Configuration Controls (Account Data Sync Panel Layout)
st.sidebar.title("👤 Agent Profile: Active Session")
st.sidebar.markdown("**Logged In Rep:** `CSR_ID_9052` ")
st.sidebar.markdown("**Network Mesh:** `● Sync Secure`")

uploaded_file = st.sidebar.file_uploader("🔄 Sync Profile / Ingest Local CSV Batch Data", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

st.sidebar.write("---")

# Left Sidebar Navigation Console
st.sidebar.subheader("🏁 Navigation Console")
app_mode = st.sidebar.radio(
    "Select System Panel View:",
    ["👥 Customer Overview", "🏪 Shop & Cost Overview", "💰 Sales & Quarter Overview"]
)

st.sidebar.write("---")
st.sidebar.header("🎛️ Dynamic Data Filters")
status_filter = st.sidebar.multiselect("Claim Status:", options=df["claim_status"].unique(), default=df["claim_status"].unique())
account_filter = st.sidebar.multiselect("Policy Account Profile:", options=df["account_type"].unique(), default=df["account_type"].unique())
shop_filter = st.sidebar.multiselect("Filter Partner Shop Network:", options=df["mechanic_shop"].unique(), default=df["mechanic_shop"].unique())
rental_filter = st.sidebar.multiselect("Filter Rental Car Vendors:", options=df["rental_vendor"].unique(), default=df["rental_vendor"].unique())

# Apply Full Dimensional Filtering Logic
filtered_df = df[
    (df["claim_status"].isin(status_filter)) & 
    (df["account_type"].isin(account_filter)) &
    (df["mechanic_shop"].isin(shop_filter)) &
    (df["rental_vendor"].isin(rental_filter))
]

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
        "rental_car_allocated", "rental_vendor", "rental_car_type", "rental_duration_days", 
        "daily_rental_allowance", "claim_status", "suggested_csr_script"
    ]
    st.dataframe(filtered_df[customer_cols], use_container_width=True)
    
    st.write("---")
    st.subheader("📝 Live CRM Case Logger Notes")
    st.markdown("*Select a Case/Customer record from the table above to log a real-time manual update interaction below.*")
    
    if len(filtered_df) > 0:
        target_id = st.selectbox("Select Target Claim ID to Append:", options=filtered_df["claim_id"].unique())
        user_notes = st.text_input(label="Type Caller Interaction / Status Verification Update Log Note:")
        if user_notes:
            st.success(f"Successfully pinned case log entry update for Claim #{target_id}: '{user_notes}'")
    else:
        st.warning("No records match your active sidebar filters to log updates.")


# ==========================================
# VIEW 2: SHOP & COST OVERVIEW (THE OPERATIONS STORY)
# ==========================================
elif app_mode == "🏪 Shop & Cost Overview":
    st.header("🏪 Repair Network Costs & Integrity Matrix")
    st.markdown("##### *Monitoring network repair cycle times, components, and facility affordability indexes.*")
    st.write("")
    
    total_parts = filtered_df["parts_cost"].sum()
    total_labor = filtered_df["labor_cost"].sum()
    st.subheader(f"Gross Fleet Operational Outflow Volume: ${(total_parts + total_labor):,.2f}")
    st.write("")
    
    if len(filtered_df) > 0:
        s_col1, s_col2 = st.columns(2)
        with s_col1:
            cost_mix = pd.DataFrame({
                "Cost Metric Classification": ["Raw Mechanical Replacement Parts Cost", "Mechanic Technical Labor Billing"], 
                "Aggregated Outflow": [total_parts, total_labor]
            })
            
            fig_donut = px.pie(cost_mix, values="Aggregated Outflow", names="Cost Metric Classification", hole=0.5,
                               title="Financial Split: Capital Disbursed to Parts vs. Labor Hours",
                               color_discrete_sequence=["#9C27B0", "#E040FB"])
            
            # FIXED: Hardcoded currency text templates to render native dollar amounts ($#,##0.00 format) alongside percentages
            fig_donut.update_traces(
                texttemplate='$%{value:,.2f}<br>(%{percent})', 
                textinfo='value+percent', 
                hovertemplate='<b>%{label}</b><br>Total: $%{value:,.2f}<br>Percentage: %{percent}'
            )
            st.plotly_chart(fig_donut, use_container_width=True)
            st.caption("**Analytical Cost Explanation:** This donut distribution breaks down macro expenses across the selected filter footprint, showing exactly how physical parts acquisition overhead stacks up directly against standard garage mechanical labor billable hours.")
            
        with s_col2:
            fig_bay = px.bar(filtered_df, x="mechanic_shop", y="days_in_shop", color="car_model", barmode="group",
                             title="Average Machine Cycle Days by Location Partner",
                             labels={"mechanic_shop": "Repair Network Facility", "days_in_shop": "Days Elapsed in Shop"})
            st.plotly_chart(fig_bay, use_container_width=True)
            st.caption("**Analytical Cycle Explanation:** This time-series graph isolates internal repair facility operational velocities (Cycle Time). It charts the total consecutive calendar days vehicles sit physically inside the service bays before processing completion.")

        # Shop Affordability Matrix and Preferred Router Intelligence
        st.write("---")
        st.header("📊 Act 2: Network Vendor Affordability & Procurement Router Matrix")
        st.markdown("##### *Granular financial overview identifying real-time average itemized parts cost per facility to guide optimal policyholder routing.*")
        
        shop_insights = filtered_df.groupby("mechanic_shop").agg(
            avg_parts_spent=("parts_cost", "mean"),
            avg_labor_spent=("labor_cost", "mean"),
            avg_days_delayed=("days_in_shop", "mean"),
            volume_processed=("claim_id", "count")
        ).reset_index()
        
        shop_insights.columns = [
            "Network Shop Facility", "Avg Replacement Parts Bill ($)", 
            "Avg Facility Labor Invoice ($)", "Avg Cycle Time (Days in Shop)", "Total Claim Volume Logged"
        ]
        st.dataframe(shop_insights.style.format({
            "Avg Replacement Parts Bill ($)": "${:,.2f}",
            "Avg Facility Labor Invoice ($)": "${:,.2f}",
            "Avg Cycle Time (Days in Shop)": "{:.1f} Days"
        }), use_container_width=True)
        
        # Brand Breakdown Matrix explaining cost/time variances explicitly
        st.write("")
        st.subheader("💡 AutoGuard Brand Specific Routing Matrix (BMW & Audi vs. Nissan & Toyota)")
        st.markdown("Vehicle parts costs and bay hold durations vary massively based on manufacturer class. Use this reference lookup to set accurate caller expectations:")
        
        col_brand1, col_brand2 = st.columns(2)
        with col_brand1:
            st.info("🇪🇺 **Import Luxury Tier (BMW & Audi):**\n"
                    "* **Parts Variance:** High-end engineering components (e.g., Mechatronic transmission blocks or turbo assemblies) command a severe premium, averaging **$1,800 to $4,200** per claim instance.\n"
                    "* **Cycle Time Impact:** Expect a baseline shop hold of **16 to 25 Days**. Complex proprietary system diagnostic sequences and overseas supply chain distribution lines add significant downtime friction.")
        with col_brand2:
            st.success("🇯🇵 **Domestic & Import Mainstream Tier (Toyota & Nissan):**\n"
                    "* **Parts Variance:** Hardware units (e.g., water pumps, alternators, standard gearboxes) are highly standardized, lowering average parts bills down to **$350 to $800**.\n"
                    "* **Cycle Time Impact:** Repair fulfillment drops drastically to **3 to 5 Days** at locations like Pep Boys due to instantaneous local parts distribution coverage.")
            
        st.write("")
        st.markdown("#### 🎯 Smart Shop Optimization Routing Logic")
        st.success("🏆 **Precision Auto — Best for BMW & Audi Logistics:** Precision Auto maintains specialized master technicians for imports. While their baseline labor rate is standard, their supply chain relationships lower complex European component procurement margins by **15%**.")
        st.warning("⚡ **Pep Boys — Best for Toyota & Nissan Volume:** Pep Boys operates with localized inventory hubs. For mainstream passenger vehicle lines, they can hot-swap components out instantly, hitting an optimized turnaround SLA under **4 days**.")
    else:
        st.warning("No active data records match your current sidebar filter combination combinations.")


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
    
    if len(filtered_df) > 0:
        # Month-by-month historical line trend pinned right at the top
        st.subheader("📈 Month-over-Month Growth Velocity")
        month_order = ["January", "February", "March", "April", "May", "June"]
        monthly_summary = filtered_df.groupby("reporting_month")["repair_cost"].sum().reindex(month_order).reset_index().fillna(0)
        
        fig_trend = px.line(
            monthly_summary, x="reporting_month", y="repair_cost", text="repair_cost",
            title="Chronological Gross Capital Intake Velocity (Monthly Delta)",
            labels={"reporting_month": "Fiscal Month", "repair_cost": "Total Booked Claims ($)"},
            markers=True
        )
        fig_trend.update_traces(textposition="top center", line_color="#1565C0")
        st.plotly_chart(fig_trend, use_container_width=True)
        
        # Chronological Performance Variance Analysis context right under line chart
        st.markdown("📋 **Fiscal Month Variance Analysis (Executive Story Context):**")
        st.caption("📉 **Q1 Volumetric Softness (January - February):** Financial liability intake shows lower aggregate values during this opening window. This is a normal seasonal trend driven by low winter vehicle usage, resulting in lower active component failures and extended policy baseline holds.")
        st.caption("📈 **Q2 Hyper-Expansion Acceleration (May - June):** Booking numbers spike sharply as summer temperatures rise. Extreme thermal stress triggers an increase in heavy electrical and high-friction transmission claims across the fleet portfolio.")
        st.write("---")
        
        # Quarter-over-Quarter and Funnel breakdown charts side-by-side underneath
        sa_col1, sa_col2 = st.columns(2)
        with sa_col1:
            st.subheader("📊 Macro Quarterly Distribution")
            fig_sales_q = px.bar(filtered_df, x="reporting_quarter", y="repair_cost", color="claim_status",
                                 title="Gross Booking Volume Distributions by Quarter",
                                 labels={"reporting_quarter": "Fiscal Period Mark", "repair_cost": "Booking Volume Valuation ($)"},
                                 color_discrete_map={"Approved": "#2E7D32", "Pending": "#1565C0", "Denied": "#C62828"})
            st.plotly_chart(fig_sales_q, use_container_width=True)
            
        with sa_col2:
            st.subheader("⏳ Lifecycle Stage History Funnel")
            sales_funnel = filtered_df.groupby("funnel_stage")["repair_cost"].sum().reset_index().sort_values(by="repair_cost", ascending=False)
            fig_sales_funnel = px.funnel(sales_funnel, x="repair_cost", y="funnel_stage",
                                         title="Financial Pipeline Velocity Stages",
                                         labels={"repair_cost": "Total Value in Stage ($)", "funnel_stage": "System Stage"})
            st.plotly_chart(fig_sales_funnel, use_container_width=True)
        
        st.write("---")
        st.subheader("🕵️‍♂️ Risk Mitigation Audit Log: System Denial Reasons")
        st.markdown("Executive context mapping exactly why specific data values were filtered out or denied during systemic pipeline checks:")
        st.info("💡 **Policy Exclusion Code 401 (Routine Braking Systems):** Component requested was classified as routine friction wear-and-tear pads. Powertrain policies strictly cover mechanical engine and internal gearing component failures, preventing systemic margin bleeding on standard wear items.")
        st.info("💡 **Policy Exclusion Code 402 (Air Filtration Units):** Filter intake element replacements fall under basic preventative owner maintenance guidelines and do not meet the structural threshold requirements for mechanical claim insurance allocation.")
    else:
        st.warning("No active data records match your current sidebar filter selections.")
