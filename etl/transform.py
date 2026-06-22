import pandas as pd


def transform_data(sales, inventory):

    # Convert dates
    sales["transaction_date"] = pd.to_datetime(
        sales["transaction_date"],
        errors="coerce"
    )

    inventory["inventory_date"] = pd.to_datetime(
        inventory["inventory_date"],
        errors="coerce"
    )

    # Remove duplicates
    sales = sales.drop_duplicates()

    inventory = inventory.drop_duplicates()

    # Merge datasets
    df = inventory.merge(
        sales,
        on=["store_id", "sku_id"],
        how="left"
    )

    # Feature Engineering
    df["stock_gap"] = (
        df["expected_stock"]
        - df["actual_stock"]
    )

    df["shelf_compliance_pct"] = (
        df["actual_stock"]
        / df["expected_stock"]
    ) * 100

    df["stock_out_flag"] = (
        df["actual_stock"] == 0
    ).astype(int)

    print("Transformation Completed")

    return df