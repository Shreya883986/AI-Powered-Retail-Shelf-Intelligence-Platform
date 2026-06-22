# System Architecture

## Architecture Overview

The platform follows a complete Data Analytics lifecycle.

Raw Data
    ↓
Data Cleaning
    ↓
ETL Pipeline
    ↓
Data Warehouse
    ↓
Business Analysis
    ↓
Machine Learning
    ↓
FastAPI Service
    ↓
Power BI Dashboard

---

## Data Sources

### Sales Data

Contains:

- Transaction ID
- Product Information
- Quantity Sold
- Sales Amount

### Inventory Data

Contains:

- Expected Stock
- Actual Stock
- Stock Status

### Product Data

Contains:

- Product Name
- Brand
- Category

### Store Data

Contains:

- Store Information
- Region
- State
- Store Size

---

## Data Warehouse Layer

Fact Table:

- dw_fact_sales

Dimension Data:

- Product Information
- Store Information
- Inventory Information

---

## ETL Layer

The ETL pipeline performs:

### Extract

Loads CSV files

### Transform

- Data cleaning
- Missing value handling
- Feature generation

### Load

Loads transformed data into warehouse-ready datasets

---

## Analytics Layer

Business analysis performed:

- Revenue Analysis
- Store Performance Analysis
- Inventory Analysis
- Shelf Compliance Analysis

---

## Machine Learning Layer

Models implemented:

### Demand Forecasting

Predict future sales demand

### Inventory Classification

Predict stock status

---

## API Layer

FastAPI endpoints:

POST /predict-demand

POST /predict-stock

---

## Visualization Layer

Power BI dashboards provide:

- Revenue Monitoring
- Inventory Tracking
- Product Performance
- Store Performance
- Shelf Intelligence Monitoring