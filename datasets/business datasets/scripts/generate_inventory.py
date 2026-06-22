import pandas as pd
import numpy as np
import os

# Load existing files
# Get current script location
current_dir = os.path.dirname(os.path.abspath(__file__))

# Build full paths
stores_path = os.path.join(current_dir, "..", "data", "stores.csv")
products_path = os.path.join(current_dir, "..", "data", "products.csv")

# Read files
stores = pd.read_csv(
    "C:\\Users\\vic\\Desktop\\shhhh\\dataanalyticsproject\\AI-Powered Retail Shelf Intelligence Platform\\datasets\\business datasets\\data\\stores.csv"
)

products = pd.read_csv(
    "C:\\Users\\vic\\Desktop\\shhhh\\dataanalyticsproject\\AI-Powered Retail Shelf Intelligence Platform\\datasets\\business datasets\\data\\products.csv"
)

print("Stores Shape:", stores.shape)
print("Products Shape:", products.shape)


inventory = []

inventory_id = 1

for _, store in stores.iterrows():

    for _, product in products.iterrows():

        expected_stock = np.random.randint(20, 100)

        actual_stock = max(
            0,
            expected_stock - np.random.randint(0, 40)
        )

        if actual_stock == 0:
            stock_status = "Out of Stock"

        elif actual_stock <= expected_stock * 0.2:
            stock_status = "Low Stock"

        else:
            stock_status = "In Stock"

        inventory.append([
            f"INV{inventory_id:06}",
            store["store_id"],
            product["sku_id"],
            "2026-06-01",
            expected_stock,
            actual_stock,
            stock_status
        ])

        inventory_id += 1

inventory_df = pd.DataFrame(
    inventory,
    columns=[
        "inventory_id",
        "store_id",
        "sku_id",
        "inventory_date",
        "expected_stock",
        "actual_stock",
        "stock_status"
    ]
)

inventory_path = os.path.join(current_dir, "inventory.csv")

inventory_df.to_csv(
    inventory_path,
    index=False
)

print("inventory.csv generated successfully!")