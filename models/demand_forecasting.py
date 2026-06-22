from pathlib import Path
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, root_mean_squared_error

# ====================================
# Project Root
# ====================================
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset
data_path = (
    BASE_DIR
    / "datasets"
    / "processed datasets"
    / "etl_output.csv"
)

# Model Save Path
model_path = (
    BASE_DIR
    / "models"
    / "saved_models"
    / "demand_forecast_model.pkl"
)

# ====================================
# Load Data
# ====================================
df = pd.read_csv(data_path)

print("Original Shape:", df.shape)

# ====================================
# Select Features and Target
# ====================================
columns_needed = [
    "expected_stock",
    "actual_stock",
    "sales_amount",
    "quantity_sold"
]

df = df[columns_needed]

# Remove rows containing NaN
df = df.dropna()

print("Shape After Removing NaN:", df.shape)

# ====================================
# Features and Target
# ====================================
X = df[
    [
        "expected_stock",
        "actual_stock",
        "sales_amount"
    ]
]

y = df["quantity_sold"]

# ====================================
# Train-Test Split
# ====================================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ====================================
# Train Model
# ====================================
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# ====================================
# Prediction
# ====================================
pred = model.predict(X_test)

# ====================================
# Metrics
# ====================================
mae = mean_absolute_error(y_test, pred)
rmse = root_mean_squared_error(y_test, pred)

print("\nModel Performance")
print("-------------------")
print("MAE :", round(mae,2))
print("RMSE:", round(rmse,2))

# ====================================
# Save Model
# ====================================
joblib.dump(
    model,
    model_path
)

print("\nDemand Forecast Model Saved Successfully")
print(model_path)