from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

BASE_DIR = Path(__file__).resolve().parent.parent

data_path = (
    BASE_DIR
    / "datasets"
    / "processed datasets"
    / "etl_output.csv"
)

df = pd.read_csv(data_path)

# Create target
df["stock_label"] = df["actual_stock"].apply(
    lambda x:
    "Out Of Stock" if x == 0
    else "Low Stock" if x < 20
    else "In Stock"
)

X = df[
    [
        "expected_stock",
        "quantity_sold",
        "sales_amount"
    ]
]

y = df["stock_label"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

clf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

clf.fit(X_train, y_train)

print("Inventory Classifier Trained")