-- Data Loading Script
-- Retail Shelf Intelligence Platform

-- Stores
COPY stores
FROM 'path/to/stores.csv'
DELIMITER ','
CSV HEADER;

-- Products
COPY products
FROM 'path/to/products.csv'
DELIMITER ','
CSV HEADER;

-- Inventory
COPY inventory
FROM 'path/to/inventory.csv'
DELIMITER ','
CSV HEADER;

-- Pricing
COPY pricing
FROM 'path/to/pricing.csv'
DELIMITER ','
CSV HEADER;

-- Sales
COPY sales
FROM 'path/to/sales.csv'
DELIMITER ','
CSV HEADER;

-- Shelf Audit
COPY shelf_audit
FROM 'path/to/shelf_audit.csv'
DELIMITER ','
CSV HEADER;