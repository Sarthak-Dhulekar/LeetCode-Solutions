SELECT
	customer_id
FROM (SELECT
      customer_id,
	COUNT(DISTINCT product_key) AS product_key
FROM Customer
     GROUP BY customer_id) AS counting
WHERE product_key IN
(SELECT
	COUNT(*) AS product_key
FROM Product);