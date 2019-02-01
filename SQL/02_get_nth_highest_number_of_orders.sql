--  TASK: How can we get the nth highest number of orders a single customer has?

CREATE VIEW customer_order_counts AS
SELECT customers.customer_id, first_name, count(orders.customer_id) AS order_count
FROM customers LEFT OUTER JOIN orders
ON (customers.customer_id = orders.customer_id)
GROUP BY customers.customer_id;

SELECT * FROM customer_order_counts
ORDER BY order_count DESC LIMIT 4;

-- +-------------+------------+-------------+
-- | customer_id | first_name | order_count |
-- +-------------+------------+-------------+
-- |      694556 | Lee        |           5 |
-- |      123727 | Rosie      |           4 |
-- |      742247 | Heike      |           4 |
-- |      216445 | Deborah    |           4 |
-- +-------------+------------+-------------+

-- This gets the third item in the list. If LIMIT is given two arguments, the second argument becomes the number of
-- rows to return, and the first argument is the offset
SELECT * FROM customer_order_counts
ORDER BY order_count DESC LIMIT 2, 1;

-- As a bonus, how would you do this with pure SQL, not relying on MySQLs handy LIMIT clause? It’s tricky!
