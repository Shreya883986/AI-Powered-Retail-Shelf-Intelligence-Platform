import pandas as pd
import numpy as np
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

stores = pd.read_csv(
    r"C:\Users\vic\Desktop\shhhh\dataanalyticsproject\AI-Powered Retail Shelf Intelligence Platform\datasets\business datasets\data\stores.csv"
)

products = pd.read_csv(
    r"C:\Users\vic\Desktop\shhhh\dataanalyticsproject\AI-Powered Retail Shelf Intelligence Platform\datasets\business datasets\data\products.csv"
)

audit_data = []

audit_id = 1

for _, store in stores.iterrows():

    for _, product in products.iterrows():

        expected_qty = np.random.randint(10, 40)

        detected_qty = max(
            0,
            expected_qty - np.random.randint(0, 20)
        )

        visibility_score = round(
            (detected_qty / expected_qty) * 100,
            2
        )

        if detected_qty == 0:
            issue = "Stock Out"

        elif visibility_score < 50:
            issue = "Low Visibility"

        elif np.random.random() < 0.05:
            issue = "Misplaced Product"

        else:
            issue = "None"

        compliance = (
            "Compliant"
            if issue == "None"
            else "Non-Compliant"
        )

        audit_data.append([
            f"AUD{audit_id:06}",
            "2026-06-01",
            store["store_id"],
            product["sku_id"],
            expected_qty,
            detected_qty,
            visibility_score,
            compliance,
            issue
        ])

        audit_id += 1

audit_df = pd.DataFrame(
    audit_data,
    columns=[
        "audit_id",
        "audit_date",
        "store_id",
        "sku_id",
        "expected_qty",
        "detected_qty",
        "visibility_score",
        "shelf_compliance",
        "audit_issue"
    ]
)

audit_df.to_csv(
    os.path.join(current_dir, "shelf_audit.csv"),
    index=False
)

print("shelf_audit.csv generated successfully!")
print("Rows:", len(audit_df))