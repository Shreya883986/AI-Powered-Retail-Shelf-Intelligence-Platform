CREATE TABLE dw_dim_store AS
SELECT DISTINCT
    store_id,
    store_name,
    city,
    state,
    region,
    store_size
FROM stores;

CREATE TABLE dw_dim_product AS
SELECT DISTINCT
    sku_id,
    product_name,
    brand,
    category,
    unit_price
FROM products;

CREATE TABLE dw_dim_date AS
SELECT DISTINCT
    transaction_date AS date_key
FROM sales;

CREATE TABLE dw_fact_sales AS
SELECT
    transaction_id,
    transaction_date,
    store_id,
    sku_id,
    quantity_sold,
    sales_amount
FROM sales;

CREATE TABLE dw_fact_shelf_audit AS
SELECT
    audit_id,
    audit_date,
    store_id,
    sku_id,
    visibility_score,
    shelf_compliance,
    audit_issue
FROM shelf_audit;

SELECT COUNT(*) FROM dw_dim_store;
SELECT COUNT(*) FROM dw_dim_product;
SELECT COUNT(*) FROM dw_dim_date;
SELECT COUNT(*) FROM dw_fact_sales;
SELECT COUNT(*) FROM dw_fact_shelf_audit;

SELECT * FROM dw_dim_store;
SELECT * FROM dw_dim_product;
SELECT * FROM dw_dim_date;
SELECT * FROM dw_fact_sales;
SELECT * FROM dw_fact_shelf_audit;