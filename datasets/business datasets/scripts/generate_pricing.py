import pandas as pd
import numpy as np
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

# Update paths according to your folder structure
stores = pd.read_csv(
    r"C:\Users\vic\Desktop\shhhh\dataanalyticsproject\AI-Powered Retail Shelf Intelligence Platform\datasets\business datasets\data\stores.csv"
)

products = pd.read_csv(
    r"C:\Users\vic\Desktop\shhhh\dataanalyticsproject\AI-Powered Retail Shelf Intelligence Platform\datasets\business datasets\data\products.csv"
)

pricing = []

price_id = 1

for _, store in stores.iterrows():

    for _, product in products.iterrows():

        expected_price = product["unit_price"]

        # 90% correct pricing
        if np.random.random() < 0.9:
            displayed_price = expected_price
            price_status = "Correct"

        else:
            displayed_price = round(
                expected_price + np.random.randint(-20, 21),
                2
            )

            if displayed_price <= 0:
                displayed_price = expected_price

            price_status = "Mismatch"

        pricing.append([
            f"PR{price_id:06}",
            store["store_id"],
            product["sku_id"],
            "2026-06-01",
            expected_price,
            displayed_price,
            price_status
        ])

        price_id += 1

pricing_df = pd.DataFrame(
    pricing,
    columns=[
        "price_id",
        "store_id",
        "sku_id",
        "audit_date",
        "expected_price",
        "displayed_price",
        "price_status"
    ]
)

pricing_df.to_csv(
    os.path.join(current_dir, "pricing.csv"),
    index=False
)

print("pricing.csv generated successfully!")