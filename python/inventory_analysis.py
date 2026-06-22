from pathlib import Path
import pandas as pd

# =====================================
# Project Base Directory
# =====================================
BASE_DIR = Path(__file__).resolve().parent.parent

# =====================================
# Input File
# =====================================
inventory_path = (
    BASE_DIR
    / "datasets"
    / "business datasets"
    / "data"
    / "inventory.csv"
)

# =====================================
# Output File
# =====================================
output_path = (
    BASE_DIR
    / "datasets"
    / "processed datasets"
    / "inventory_analysis.csv"
)

# =====================================
# Load Inventory Data
# =====================================
inventory = pd.read_csv(inventory_path)

print("Original Shape:", inventory.shape)

# =====================================
# Convert Date Column
# =====================================
inventory["inventory_date"] = pd.to_datetime(
    inventory["inventory_date"],
    errors="coerce"
)

# =====================================
# Remove Duplicates
# =====================================
inventory = inventory.drop_duplicates()

# =====================================
# Stock Gap
# =====================================
inventory["stock_gap"] = (
    inventory["expected_stock"]
    - inventory["actual_stock"]
)

# =====================================
# Stock Loss Percentage
# =====================================
inventory["stock_loss_percent"] = (
    inventory["stock_gap"]
    / inventory["expected_stock"]
) * 100

# =====================================
# Inventory Health
# =====================================
inventory["inventory_health"] = (
    inventory["actual_stock"]
    >= inventory["expected_stock"]
)

inventory["inventory_health"] = (
    inventory["inventory_health"]
    .map({
        True: "Healthy",
        False: "Shortage"
    })
)

# =====================================
# Stock-Out Flag
# =====================================
inventory["stock_out_flag"] = (
    inventory["actual_stock"] == 0
).astype(int)

# =====================================
# Total Inventory Leakage
# =====================================
inventory["inventory_leakage"] = (
    inventory["expected_stock"]
    - inventory["actual_stock"]
)

# =====================================
# Critical Inventory
# =====================================
critical_inventory = inventory[
    inventory["stock_gap"] > 0
]

print("\nCritical Inventory Records:")
print(critical_inventory.head())

# =====================================
# Summary Statistics
# =====================================
print("\nInventory Summary")

print("Average Expected Stock:",
      round(inventory["expected_stock"].mean(),2))

print("Average Actual Stock:",
      round(inventory["actual_stock"].mean(),2))

print("Total Inventory Leakage:",
      inventory["inventory_leakage"].sum())

print("Stock Out Count:",
      inventory["stock_out_flag"].sum())

# =====================================
# Save Dataset
# =====================================
inventory.to_csv(
    output_path,
    index=False
)

print("\nInventory Analysis Completed Successfully.")
print(f"\nSaved to:\n{output_path}")