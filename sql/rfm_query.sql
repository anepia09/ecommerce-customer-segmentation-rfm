WITH customer_rfm AS (
    SELECT
        "Customer ID" AS customer_id,
        JULIANDAY((SELECT MAX(InvoiceDate) FROM transactions)) 
            - JULIANDAY(MAX(InvoiceDate)) AS recency,
        COUNT(DISTINCT Invoice) AS frequency,
        SUM(Quantity * Price) AS monetary
    FROM transactions
    GROUP BY "Customer ID"
)
SELECT *
FROM customer_rfm
ORDER BY monetary DESC
LIMIT 10;
