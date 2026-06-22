from fastapi import FastAPI
from api.schema import DemandInput, StockInput
from api.predict import predict_demand, predict_stock

app = FastAPI(
    title="AI-Powered Retail Shelf Intelligence API",
    description="API for demand prediction and inventory stock classification.",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Retail Shelf Intelligence API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/predict-demand")
def demand_prediction(data: DemandInput):
    prediction = predict_demand(
        data.expected_stock,
        data.actual_stock,
        data.sales_amount
    )
    return {"predicted_quantity_sold": prediction}

@app.post("/predict-stock")
def stock_prediction(data: StockInput):
    prediction = predict_stock(
        data.expected_stock,
        data.quantity_sold,
        data.sales_amount
    )
    return {"predicted_stock_status": prediction}