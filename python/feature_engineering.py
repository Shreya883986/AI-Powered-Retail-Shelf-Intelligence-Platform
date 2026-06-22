from pathlib import Path
import pandas as pd

# ============================
# Project Base Directory
# ============================
BASE_DIR = Path(__file__).resolve().parent.parent

# ============================
# Input File
# ============================
sales_path = (
    BASE_DIR
    / "datasets"
    / "data warehouse"
    / "dw_fact_sales.csv"
)

# ============================
# Output File
# ============================
output_path = (
    BASE_DIR
    / "datasets"
    / "processed datasets"
    / "feature_engineered_data.csv"
)

# ============================
# Load Data
# ============================
df = pd.read_csv(sales_path)

print("Original Shape:", df.shape)

# ============================
# Convert Date
# ============================
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# ============================
# Revenue Per Unit
# ============================
df["revenue_per_unit"] = (
    df["sales_amount"] /
    df["quantity_sold"]
)

# ============================
# Month
# ============================
df["month"] = df["transaction_date"].dt.month_name()

# ============================
# Year
# ============================
df["year"] = df["transaction_date"].dt.year

# ============================
# Quarter
# ============================
df["quarter"] = df["transaction_date"].dt.quarter

# ============================
# Day Name
# ============================
df["day_name"] = df["transaction_date"].dt.day_name()

# ============================
# Weekend Flag
# ============================
df["is_weekend"] = (
    df["day_name"]
    .isin(["Saturday", "Sunday"])
)

# ============================
# High Revenue Transaction
# ============================
median_sales = df["sales_amount"].median()

df["high_revenue_product"] = (
    df["sales_amount"] > median_sales
).astype(int)

# ============================
# Revenue Category
# ============================
df["revenue_category"] = pd.qcut(
    df["sales_amount"],
    q=3,
    labels=["Low", "Medium", "High"]
)

# ============================
# Revenue Contribution %
# ============================
total_sales = df["sales_amount"].sum()

df["revenue_contribution_pct"] = (
    df["sales_amount"] / total_sales
) * 100

# ============================
# Average Quantity Sold per SKU
# ============================
avg_qty = (
    df.groupby("sku_id")["quantity_sold"]
      .mean()
      .reset_index()
)

avg_qty.rename(
    columns={
        "quantity_sold": "avg_quantity_sold"
    },
    inplace=True
)

df = df.merge(
    avg_qty,
    on="sku_id",
    how="left"
)

# ============================
# Save Dataset
# ============================
df.to_csv(
    output_path,
    index=False
)

print("\nFeature Engineering Completed Successfully.")
print("Final Shape:", df.shape)
print(f"\nSaved to:\n{output_path}")