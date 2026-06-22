# API Documentation

## Base URL

http://127.0.0.1:8000

---

# Demand Prediction API

## Endpoint

POST /predict-demand

### Request

{
    "expected_stock": 100,
    "actual_stock": 80,
    "sales_amount": 15000
}

### Response

{
    "predicted_demand": 125
}

---

# Stock Prediction API

## Endpoint

POST /predict-stock

### Request

{
    "expected_stock": 100,
    "quantity_sold": 30,
    "sales_amount": 15000
}

### Response

{
    "predicted_stock_status": "In Stock"
}

---

## Swagger Documentation

Run:

python -m uvicorn api.main:app --reload

Open:

http://127.0.0.1:8000/docs

Interactive API testing is available through Swagger UI.