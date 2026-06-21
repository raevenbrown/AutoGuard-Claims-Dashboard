import pandas as pd

# --- Step 1: Build the mock dataframe ---
# A Python dictionary maps column names to lists of values.
# Each list position represents one row (record) in the table.
claims_data = {
    "claim_id": [101, 102, 103, 104, 105, 106, 107],
    "vehicle_id": [1, 2, 3, 4, 1, 3, 2],
    "repair_cost": [1200.00, 850.00, 3400.00, 500.00, 2100.00, 975.00, 4800.00],
    "claim_status": ["Approved", "Pending", "Approved", "Denied", "Pending", "Denied", "Approved"]
}

# pd.DataFrame() converts the dictionary into a structured table
df = pd.DataFrame(claims_data)

print("=== Full Dataset ===")
print(df.to_string(index=False))
print()

# --- Step 2: Filter rows where repair_cost > 1000 ---
# Create boolean mask (True/False indicator per row)
mask = df["repair_cost"] > 1000

print("=== Boolean Mask (True = passes filter) ===")
print(mask.to_string())
print()

# Apply the mask back to the dataframe
filtered_df = df[mask]

print("=== Filtered Claims (repair_cost > $1,000) ===")
print(filtered_df.to_string(index=False))
print()

# --- Step 3: KPI Summary & Analytics ---
total_exposure = filtered_df["repair_cost"].sum()
avg_cost = filtered_df["repair_cost"].mean()
claim_count = len(filtered_df)
approval_rate = (df["claim_status"] == "Approved").mean() * 100

print("=== KPI Summary ===")
print(f"High-cost claims flagged : {claim_count}")
print(f"Total financial exposure : ${total_exposure:,.2f}")
print(f"Average cost per claim   : ${avg_cost:,.2f}")
print(f"Approval rate (all data) : {approval_rate:.1f}%")
