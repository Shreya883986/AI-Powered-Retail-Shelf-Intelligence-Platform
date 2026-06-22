from pathlib import Path
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_absolute_error, mean_squared_error, accuracy_score

# ====================================
# Project Root
# ====================================
BASE_DIR = Path(__file__).resolve().parent.parent

# ====================================
# Paths
# ====================================
data_path = (
    BASE_DIR
    / "datasets"
    / "processed datasets"
    / "etl_output.csv"
)

save_folder = (
    BASE_DIR
    / "models"
    / "saved_models"
)

save_folder.mkdir(exist_ok=True)

# ====================================
# Load Data
# ====================================
df = pd.read_csv(data_path)

print("Original Shape:", df.shape)

# ====================================
# Keep required columns only
# ====================================
required_columns = [
    "expected_stock",
    "actual_stock",
    "sales_amount",
    "quantity_sold"
]

df = df[required_columns]

# Remove rows with missing values
df = df.dropna()

print("Shape After Removing Missing Values:", df.shape)

# ====================================
# Demand Forecasting Model
# Predict quantity_sold
# ====================================
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

reg_predictions = reg_model.predict(X_test)

mae = mean_absolute_error(y_test, reg_predictions)
rmse = mean_squared_error(y_test, reg_predictions) ** 0.5

print("\nDemand Forecasting Model")
print("------------------------")
print("MAE:", round(mae, 2))
print("RMSE:", round(rmse, 2))

joblib.dump(
    reg_model,
    save_folder / "demand_forecast_model.pkl"
)

print("Demand Forecast Model Saved")

# ====================================
# Inventory Classification Model
# Predict stock status
# ====================================
df["stock_label"] = df["actual_stock"].apply(
    lambda x:
    "Out Of Stock" if x == 0
    else "Low Stock" if x < 20
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

clf_predictions = clf_model.predict(X_test)

accuracy = accuracy_score(y_test, clf_predictions)

print("\nInventory Classification Model")
print("-------------------------------")
print("Accuracy:", round(accuracy, 2))

joblib.dump(
    clf_model,
    save_folder / "inventory_classifier.pkl"
)

print("Inventory Classifier Model Saved")

print("\nAll Models Trained and Saved Successfully")