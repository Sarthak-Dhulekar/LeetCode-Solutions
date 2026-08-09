SELECT
    customer_number
FROM Orders
GROUP BY customer_number
order by COUNT(order_number) DESC
LIMIT 1;