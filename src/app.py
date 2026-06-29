import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration Setup
st.set_page_config(page_title="AutoGuard Operations Platform", layout="wide")
st.title("🛡️ AutoGuard Enterprise Operations Platform")
st.markdown("Centralized Full-Stack Intelligence Engine for Finance, Marketing, and Customer Service Analytics.")
st.write("---")

# 2. Ingest the Data (The Advanced Analyst Dataset)
advanced_claims_data = {
    "claim_id": [101, 102, 103, 104, 105, 106, 107],
    "customer_name": ["Alice Smith", "Bob Jones", "Charlie Brown", "Diana Prince", "Evan Wright", "Fiona Gallagher", "George Clark"],
    "car_model": ["Kia Optima", "Ford F-150", "Kia Optima", "Honda Civic", "Ford F-150", "Honda Civic", "Kia Optima"],
    "claim_type": ["Electrical", "Transmission", "Electrical", "Routine", "Transmission", "Routine", "Transmission"],
    "mechanic_shop": ["Pep Boys", "Precision Auto", "Pep Boys", "Local Shop B", "Precision Auto", "Local Shop B", "Pep Boys"],
    "repair_cost": [1200.00, 850.00, 3400.00, 500.00, 2100.00, 975.00, 4800.00],
    "claim_status": ["Approved", "Pending", "Approved", "Denied", "Pending", "Denied", "Approved"],
    "suggested_csr_script": [
        "Your electrical claim at Pep Boys was approved. Total coverage applied: $1,200.00.",
        "Your transmission claim at Precision Auto is currently under engineering review because it is matching historical baseline risk patterns.",
        "Your electrical claim at Pep Boys was approved. Total coverage applied: $3,400.00.",
        "Claim Denied: Routine maintenance is excluded from your powertrain policy framework.",
        "Your transmission claim at Precision Auto is currently pending approval while we verify parts allocation thresholds.",
        "Claim Denied: Routine filter swaps are classified as standard user maintenance.",
        "Your high-priority transmission claim at Pep Boys has been fully authorized at $4,800.00."
    ]
}
df = pd.DataFrame(advanced_claims_data)

# 3. Sidebar Configuration (Data Engineering & Control Layer)
st.sidebar.header("📁 System Controls")
st.sidebar.markdown("**Database Status:** `● Connected to Live Mesh` ")

# File Uploader for Future Scalability
uploaded_file = st.sidebar.file_uploader("Upload New Claims Ingestion Batch (.csv)", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

st.sidebar.write("---")
st.sidebar.header("🎯 Department View Filters")
selected_shop = st.sidebar.multiselect("Filter by Partner Mechanic Shop:", options=df["mechanic_shop"].unique(), default=df["mechanic_shop"].unique())
filtered_df = df[df["mechanic_shop"].isin(selected_shop)]

# 4. Row 1: Executive Trust & Retention Metrics (Finance / Support Layer)
total_exposure = filtered_df["repair_cost"].sum()
pending_risk = filtered_df[filtered_df["claim_status"] == "Pending"]["repair_cost"].sum()
denied_claims = filtered_df[filtered_df["claim_status"] == "Denied"]
denial_rate = (len(denied_claims) / len(filtered_df) * 100) if len(filtered_df) > 0 else 0

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Financial Exposure (Finance)", value=f"${total_exposure:,.2f}")
with col2:
    st.metric(label="Pending Liquidity Risk (Finance)", value=f"${pending_risk:,.2f}")
with col3:
    st.metric(label="System Denial Rate (Marketing/Ops)", value=f"{denial_rate:.1f}%")

st.write("---")

# 5. Row 2: Strategic Charts (Marketing & Product Risk Layer)
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("📊 Risk Matrix: Cost by Vehicle Model")
    # Horizontal bar chart for Product Marketing premium pricing evaluations
    fig_car = px.bar(filtered_df, x="repair_cost", y="car_model", color="claim_type", 
                     orientation='h', title="Claim Financial Density per Vehicle Class",
                     labels={"repair_cost": "Total Cost ($)", "car_model": "Vehicle Model"})
    st.plotly_chart(fig_car, use_container_width=True)

with chart_col2:
    st.subheader("🏪 Network Integrity: Shop Performance")
    # Grouped bar chart for Partner Operations network validation
    fig_shop = px.histogram(filtered_df, x="mechanic_shop", color="claim_status", 
                            barmode="group", title="Approval vs. Denial Distributions by Location",
                            labels={"mechanic_shop": "Mechanic Shop Location"})
    st.plotly_chart(fig_shop, use_container_width=True)

st.write("---")

# 6. Row 3: Customer Transparency Portal (Customer Support Layer)
st.subheader("👥 Live Customer Record Log & Smart CSR Scripting")
st.markdown("Agents read the *Suggested CSR Script* column directly to customers to explain backend automated threshold decisions seamlessly.")

# Display customized columns for cleaner readability
display_cols = ["claim_id", "customer_name", "car_model", "mechanic_shop", "repair_cost", "claim_status", "suggested_csr_script"]
st.dataframe(filtered_df[display_cols], use_container_width=True)
