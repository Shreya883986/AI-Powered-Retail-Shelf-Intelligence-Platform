-- STORES TABLE

CREATE TABLE stores (
    store_id VARCHAR(10) PRIMARY KEY,
    store_name VARCHAR(100),
    city VARCHAR(50),
    state VARCHAR(50),
    region VARCHAR(20),
    store_size VARCHAR(20),
    opening_year INT
);

-- PRODUCTS TABLE

CREATE TABLE products (
    sku_id VARCHAR(20) PRIMARY KEY,
    product_name VARCHAR(100),
    brand VARCHAR(50),
    category VARCHAR(50),
    unit_price NUMERIC(10,2),
    shelf_section VARCHAR(50)
);

-- INVENTORY TABLE

CREATE TABLE inventory (
    inventory_id VARCHAR(20) PRIMARY KEY,
    store_id VARCHAR(10),
    sku_id VARCHAR(20),
    inventory_date DATE,
    expected_stock INT,
    actual_stock INT,
    stock_status VARCHAR(30),

    FOREIGN KEY (store_id) REFERENCES stores(store_id),
    FOREIGN KEY (sku_id) REFERENCES products(sku_id)
);

-- PRICING TABLE

CREATE TABLE pricing (
    price_id VARCHAR(20) PRIMARY KEY,
    store_id VARCHAR(10),
    sku_id VARCHAR(20),
    audit_date DATE,
    expected_price NUMERIC(10,2),
    displayed_price NUMERIC(10,2),
    price_status VARCHAR(30),

    FOREIGN KEY (store_id) REFERENCES stores(store_id),
    FOREIGN KEY (sku_id) REFERENCES products(sku_id)
);

-- SALES TABLE

CREATE TABLE sales (
    transaction_id VARCHAR(20) PRIMARY KEY,
    transaction_date DATE,
    store_id VARCHAR(10),
    sku_id VARCHAR(20),
    quantity_sold INT,
    unit_price NUMERIC(10,2),
    sales_amount NUMERIC(12,2),

    FOREIGN KEY (store_id) REFERENCES stores(store_id),
    FOREIGN KEY (sku_id) REFERENCES products(sku_id)
);

-- SHELF AUDIT TABLE

CREATE TABLE shelf_audit (
    audit_id VARCHAR(20) PRIMARY KEY,
    audit_date DATE,
    store_id VARCHAR(10),
    sku_id VARCHAR(20),
    expected_qty INT,
    detected_qty INT,
    visibility_score NUMERIC(5,2),
    shelf_compliance VARCHAR(30),
    audit_issue VARCHAR(50),

    FOREIGN KEY (store_id) REFERENCES stores(store_id),
    FOREIGN KEY (sku_id) REFERENCES products(sku_id)
);