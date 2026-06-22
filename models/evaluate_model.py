from pathlib import Path
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    accuracy_score,
    classification_report
)

from sklearn.ensemble import (
    RandomForestRegressor,
    RandomForestClassifier
)

# =====================================
# Project Root
# =====================================
BASE_DIR = Path(__file__).resolve().parent.parent

# =====================================
# Dataset Path
# =====================================
data_path = (
    BASE_DIR
    / "datasets"
    / "processed datasets"
    / "etl_output.csv"
)

# =====================================
# Load Dataset
# =====================================
df = pd.read_csv(data_path)

print("Original Shape:", df.shape)

# =====================================
# Keep only required columns
# =====================================
required_columns = [
    "expected_stock",
    "actual_stock",
    "sales_amount",
    "quantity_sold"
]

df = df[required_columns]

# Remove rows containing NaN
df = df.dropna()

print("Shape After Removing Missing Values:", df.shape)

# =====================================
# REGRESSION MODEL
# =====================================
X_reg = df[
    [
        "expected_stock",
        "actual_stock",
        "sales_amount"
    ]
]

y_reg = df["quantity_sold"]

X_train, X_test, y_train, y_test = train_test_split(
    X_reg,
    y_reg,
    test_size=0.2,
    random_state=42
)

reg_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

reg_model.fit(X_train, y_train)

reg_pred = reg_model.predict(X_test)

mae = mean_absolute_error(
    y_test,
    reg_pred
)

rmse = mean_squared_error(
    y_test,
    reg_pred
) ** 0.5

print("\n========================")
print("Demand Forecast Model")
print("========================")

print("MAE :", round(mae, 2))
print("RMSE:", round(rmse, 2))

# =====================================
# CLASSIFICATION MODEL
# =====================================
df["stock_label"] = df["actual_stock"].apply(
    lambda x:
    "Out Of Stock"
    if x == 0
    else "Low Stock"
    if x < 20
    else "In Stock"
)

X_clf = df[
    [
        "expected_stock",
        "quantity_sold",
        "sales_amount"
    ]
]

y_clf = df["stock_label"]

X_train, X_test, y_train, y_test = train_test_split(
    X_clf,
    y_clf,
    test_size=0.2,
    random_state=42
)

clf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

clf_model.fit(X_train, y_train)

clf_pred = clf_model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    clf_pred
)

print("\n========================")
print("Inventory Classifier")
print("========================")

print("Accuracy:", round(accuracy, 4))

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        clf_pred
    )
)