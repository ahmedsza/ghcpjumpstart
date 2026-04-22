IF EXISTS (SELECT 1 FROM sys.objects WHERE object_id = OBJECT_ID(N'[retail].[usp_GetCustomerSalesSummary]') AND type in (N'P', N'PC'))
DROP PROCEDURE [retail].[usp_GetCustomerSalesSummary]
GO


SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE   PROCEDURE [retail].[usp_GetCustomerSalesSummary]
    @NameFilter NVARCHAR(100) = NULL
AS
BEGIN
    SET NOCOUNT ON;

    SELECT *
    FROM (
        SELECT DISTINCT
            c.customer_id,
            c.first_name + ' ' + c.last_name AS full_name,
            c.email,

            (SELECT COUNT(*) FROM retail.orders o2 WHERE o2.customer_id = c.customer_id) AS total_orders,

            (SELECT SUM(oi2.total_amount) 
             FROM retail.order_items oi2 
             INNER JOIN retail.orders o3 ON o3.order_id = oi2.order_id 
             WHERE o3.customer_id = c.customer_id) AS lifetime_spend,

            (SELECT TOP 1 o4.order_date 
             FROM retail.orders o4 
             WHERE o4.customer_id = c.customer_id 
             ORDER BY o4.order_date DESC) AS last_order_date,

            (SELECT store_name FROM retail.stores WHERE store_id = c.primary_store_id) AS store_name,

            p.product_name,
            cat.category_name,

            CASE 
                WHEN (SELECT SUM(oi5.total_amount) 
                      FROM retail.order_items oi5 
                      INNER JOIN retail.orders o5 ON o5.order_id = oi5.order_id 
                      WHERE o5.customer_id = c.customer_id) > 1000 THEN 'VIP'
                WHEN (SELECT SUM(oi5.total_amount) 
                      FROM retail.order_items oi5 
                      INNER JOIN retail.orders o5 ON o5.order_id = oi5.order_id 
                      WHERE o5.customer_id = c.customer_id) > 500 THEN 'Gold'
                ELSE 'Standard'
            END AS customer_tier,

            -- Quadratic: for each row, re-aggregate ALL customers then count how many beat this one
            (SELECT COUNT(*) FROM (
                SELECT o7.customer_id
                FROM retail.orders o7
                INNER JOIN retail.order_items oi7 ON oi7.order_id = o7.order_id
                WHERE o7.customer_id <> c.customer_id
                GROUP BY o7.customer_id
                HAVING SUM(oi7.total_amount) > 
                    (SELECT ISNULL(SUM(oi8.total_amount), 0)
                     FROM retail.order_items oi8 
                     INNER JOIN retail.orders o8 ON o8.order_id = oi8.order_id
                     WHERE o8.customer_id = c.customer_id)
            ) AS ranked) AS customers_who_spent_more,

            -- Triangle join: overlapping product purchases in same store
            (SELECT COUNT(*)
             FROM retail.order_items oi9
             INNER JOIN retail.orders o9 ON o9.order_id = oi9.order_id
             WHERE o9.store_id = o.store_id
               AND o9.customer_id <> c.customer_id
               AND oi9.product_id IN (
                   SELECT oi10.product_id 
                   FROM retail.order_items oi10 
                   INNER JOIN retail.orders o10 ON o10.order_id = oi10.order_id
                   WHERE o10.customer_id = c.customer_id
               )
            ) AS shared_product_purchases,

            -- Re-aggregates all orders every row with non-sargable date filter
            (SELECT AVG(CAST(CONVERT(VARCHAR(20), sub.total) AS DECIMAL(18,2)))
             FROM (
                 SELECT o11.customer_id, SUM(oi11.total_amount) AS total
                 FROM retail.orders o11
                 INNER JOIN retail.order_items oi11 ON oi11.order_id = o11.order_id
                 WHERE CONVERT(VARCHAR, o11.order_date, 101) LIKE '%2024%'
                 GROUP BY o11.customer_id
             ) sub
            ) AS avg_customer_spend_2024

        FROM retail.customers c, retail.orders o, retail.order_items oi, 
             retail.products p, retail.categories cat
        WHERE c.customer_id = o.customer_id
            AND o.order_id = oi.order_id
            AND oi.product_id = p.product_id
            AND p.category_id = cat.category_id
            AND CONVERT(VARCHAR, o.order_date, 101) LIKE '%2024%'
            AND ISNULL(c.phone, '') <> ''
            AND c.first_name LIKE '%' + ISNULL(@NameFilter, 'a') + '%'
            AND oi.total_amount > 0
    ) AS results
    ORDER BY lifetime_spend DESC;
END;

GO