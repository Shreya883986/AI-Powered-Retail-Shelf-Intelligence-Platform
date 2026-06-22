import pandas as pd
import numpy as np
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

# Update these paths if needed
stores = pd.read_csv(
    r"C:\Users\vic\Desktop\shhhh\dataanalyticsproject\AI-Powered Retail Shelf Intelligence Platform\datasets\business datasets\data\stores.csv"
)

products = pd.read_csv(
    r"C:\Users\vic\Desktop\shhhh\dataanalyticsproject\AI-Powered Retail Shelf Intelligence Platform\datasets\business datasets\data\products.csv"
)

sales = []

num_transactions = 100000

for i in range(1, num_transactions + 1):

    store = stores.sample(1).iloc[0]

    product = products.sample(1).iloc[0]

    quantity_sold = np.random.randint(1, 11)

    unit_price = product["unit_price"]

    sales_amount = round(
        quantity_sold * unit_price,
        2
    )

    random_date = pd.Timestamp(
        np.random.choice(
            pd.date_range(
                "2025-01-01",
                "2025-12-31"
            )
        )
    )

    sales.append([
        f"T{i:07}",
        random_date.date(),
        store["store_id"],
        product["sku_id"],
        quantity_sold,
        unit_price,
        sales_amount
    ])

sales_df = pd.DataFrame(
    sales,
    columns=[
        "transaction_id",
        "transaction_date",
        "store_id",
        "sku_id",
        "quantity_sold",
        "unit_price",
        "sales_amount"
    ]
)

sales_df.to_csv(
    os.path.join(current_dir, "sales.csv"),
    index=False
)

print("sales.csv generated successfully!")
print("Rows:", len(sales_df))