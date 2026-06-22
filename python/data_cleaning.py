from pathlib import Path
import pandas as pd

# Base directory of project
BASE_DIR = Path(__file__).resolve().parent.parent

# Input file
sales_path = (
    BASE_DIR
    / "datasets"
    / "data warehouse"
    / "dw_fact_sales.csv"
)

# Output file
output_path = (
    BASE_DIR
    / "datasets"
    / "processed datasets"
    / "clean_sales.csv"
)

# Load data
df = pd.read_csv(sales_path)

print("Original Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Convert transaction date to datetime
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# Fill missing values
df = df.ffill()

# Save cleaned dataset
df.to_csv(output_path, index=False)

print("Cleaning completed successfully.")
print("Cleaned Shape:", df.shape)
print(f"Saved file to:\n{output_path}")