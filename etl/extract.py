from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

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


def extract_data():

    sales = pd.read_csv(sales_path)

    inventory = pd.read_csv(
        inventory_path
    )

    print("Extraction Completed")

    return sales, inventory