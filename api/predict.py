from pathlib import Path
import joblib
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

DEMAND_MODEL_PATH = (
    BASE_DIR / "models" / "saved_models" / "demand_forecast_model.pkl"
)

STOCK_MODEL_PATH = (
    BASE_DIR / "models" / "saved_models" / "inventory_classifier.pkl"
)

demand_model = joblib.load(DEMAND_MODEL_PATH)
stock_model = joblib.load(STOCK_MODEL_PATH)


def predict_demand(expected_stock, actual_stock, sales_amount):
    input_data = pd.DataFrame([{
        "expected_stock": expected_stock,
        "actual_stock": actual_stock,
        "sales_amount": sales_amount
    }])

    prediction = demand_model.predict(input_data)[0]

    return round(float(prediction), 2)


def predict_stock(expected_stock, quantity_sold, sales_amount):
    input_data = pd.DataFrame([{
        "expected_stock": expected_stock,
        "quantity_sold": quantity_sold,
        "sales_amount": sales_amount
    }])

    prediction = stock_model.predict(input_data)[0]

    return str(prediction)