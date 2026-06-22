/* ============================================================
   AI-Powered Retail Shelf Intelligence Platform
   Business Analytics Queries
   ============================================================ */


/* ============================================================
   QUERY 1: TOTAL REVENUE
   Purpose:
   Calculate total revenue generated from all sales.
   Dashboard KPI:
   Total Revenue
   ============================================================ */



/* ============================================================
   QUERY 2: TOP 10 STORES BY REVENUE
   Purpose:
   Identify the highest-performing stores.
   Dashboard KPI:
   Top Revenue Stores
   ============================================================ */

SELECT
    s.store_name,
    ROUND(SUM(sa.sales_amount), 2) AS revenue
FROM sales sa
JOIN stores s
    ON sa.store_id = s.store_id
GROUP BY s.store_name
ORDER BY revenue DESC
LIMIT 10;


/* ============================================================
   QUERY 3: REVENUE BY CATEGORY
   Purpose:
   Analyze revenue contribution by product category.
   Dashboard KPI:
   Category Performance
   ============================================================ */

SELECT
    p.category,
    ROUND(SUM(s.sales_amount), 2) AS revenue
FROM sales s
JOIN products p
    ON s.sku_id = p.sku_id
GROUP BY p.category
ORDER BY revenue DESC;


/* ============================================================
   QUERY 4: STOCK-OUT ANALYSIS
   Purpose:
   Analyze inventory stock status distribution.
   Dashboard KPI:
   Stock-Out Frequency
   ============================================================ */

SELECT
    stock_status,
    COUNT(*) AS total_records
FROM inventory
GROUP BY stock_status;


/* ============================================================
   QUERY 5: SHELF COMPLIANCE PERCENTAGE
   Purpose:
   Measure shelf compliance performance.
   Dashboard KPI:
   Shelf Compliance %
   ============================================================ */

SELECT
    ROUND(
        100.0 *
        SUM(
            CASE
                WHEN shelf_compliance = 'Compliant'
                THEN 1
                ELSE 0
            END
        )
        / COUNT(*),
        2
    ) AS shelf_compliance_percentage
FROM shelf_audit;


/* ============================================================
   QUERY 6: PRICING ACCURACY PERCENTAGE
   Purpose:
   Measure pricing correctness across stores.
   Dashboard KPI:
   Pricing Accuracy %
   ============================================================ */

SELECT
    ROUND(
        100.0 *
        SUM(
            CASE
                WHEN price_status = 'Correct'
                THEN 1
                ELSE 0
            END
        )
        / COUNT(*),
        2
    ) AS pricing_accuracy
FROM pricing;


/* ============================================================
   QUERY 7: ESTIMATED REVENUE LEAKAGE
   Purpose:
   Estimate revenue loss due to missing inventory.
   Dashboard KPI:
   Revenue Leakage
   ============================================================ */

SELECT
    ROUND(
        SUM(
            (expected_stock - actual_stock)
            * p.unit_price
        ),
        2
    ) AS estimated_revenue_leakage
FROM inventory i
JOIN products p
    ON i.sku_id = p.sku_id
WHERE expected_stock > actual_stock;


/* ============================================================
   QUERY 8: TOP 10 PROBLEMATIC PRODUCTS
   Purpose:
   Identify products with the highest shelf issues.
   Dashboard KPI:
   Most Problematic Products
   ============================================================ */

SELECT
    p.product_name,
    COUNT(*) AS issue_count
FROM shelf_audit s
JOIN products p
    ON s.sku_id = p.sku_id
WHERE audit_issue <> 'None'
GROUP BY p.product_name
ORDER BY issue_count DESC
LIMIT 10;


/* ============================================================
   END OF BUSINESS ANALYTICS QUERIES
   ============================================================ */