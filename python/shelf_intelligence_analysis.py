from pathlib import Path
import pandas as pd

# =========================================
# Project Base Directory
# =========================================
BASE_DIR = Path(__file__).resolve().parent.parent

# =========================================
# Input Files
# =========================================
sales_path = (
    BASE_DIR
    / "datasets"
    / "data warehouse"
    / "dw_fact_sales.csv"
)

inventory_path = (
    BASE_DIR
    / "datasets"
    / "business datasets"
    / "data"
    / "inventory.csv"
)

# =========================================
# Output File
# =========================================
output_path = (
    BASE_DIR
    / "datasets"
    / "processed datasets"
    / "shelf_intelligence_analysis.csv"
)

# =========================================
# Load Data
# =========================================
sales = pd.read_csv(sales_path)
inventory = pd.read_csv(inventory_path)

print("Sales Shape:", sales.shape)
print("Inventory Shape:", inventory.shape)

# =========================================
# Merge Data
# =========================================
df = inventory.merge(
    sales,
    on=["store_id", "sku_id"],
    how="left"
)

print("Merged Shape:", df.shape)

# =========================================
# Convert Dates
# =========================================
df["inventory_date"] = pd.to_datetime(
    df["inventory_date"],
    errors="coerce"
)

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# =========================================
# Stock Gap
# =========================================
df["stock_gap"] = (
    df["expected_stock"]
    - df["actual_stock"]
)

# =========================================
# Shelf Compliance %
# =========================================
df["shelf_compliance_pct"] = (
    df["actual_stock"]
    / df["expected_stock"]
) * 100

# =========================================
# Stock Out Flag
# =========================================
df["stock_out_flag"] = (
    df["actual_stock"] == 0
).astype(int)

# =========================================
# Potential Revenue Loss
# =========================================
df["potential_revenue_loss"] = (
    df["stock_gap"]
    * (
        df["sales_amount"]
        / df["quantity_sold"]
    )
)

# Replace inf values
df["potential_revenue_loss"] = (
    df["potential_revenue_loss"]
    .replace([float("inf"), -float("inf")], 0)
    .fillna(0)
)

# =========================================
# Critical Products
# =========================================
critical_products = df[
    (df["stock_gap"] > 0)
]

print("\nCritical Products:")
print(
    critical_products[
        [
            "store_id",
            "sku_id",
            "stock_gap"
        ]
    ].head()
)

# =========================================
# KPI Summary
# =========================================
print("\n========== KPI SUMMARY ==========")

print(
    "Average Shelf Compliance:",
    round(df["shelf_compliance_pct"].mean(), 2)
)

print(
    "Total Stock Gap:",
    df["stock_gap"].sum()
)

print(
    "Out Of Stock Count:",
    df["stock_out_flag"].sum()
)

print(
    "Potential Revenue Loss:",
    round(
        df["potential_revenue_loss"].sum(),
        2
    )
)

# =========================================
# Save Dataset
# =========================================
df.to_csv(
    output_path,
    index=False
)

print("\nShelf Intelligence Analysis Completed.")
print(f"\nSaved to:\n{output_path}")