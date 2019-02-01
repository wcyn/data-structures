# TASK: Get the order ID of every order in January and February, 2017.

# Non Indexed Query
SELECT order_id FROM orders WHERE DATEDIFF(orders.pickup_date, '2017-03-01') < 0;
# -- 161314 rows in set (0.25 sec)

# Add an index on pickup_date
ALTER TABLE orders ADD INDEX (pickup_date);

# Running the first query still gives us about the same performance.
# That's because Functions evaluate for every row in a table without using the index
# Instead, we can compare the dates directly

SELECT order_id FROM orders WHERE pickup_date >= '2017-01-01' AND pickup_date < '2017-03-01';
# -- 161314 rows in set (0.08 sec)


