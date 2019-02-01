-- INNER JOIN is the same as JOIN, and LEFT OUTER JOIN is the same as LEFT JOIN
-- Inner joins give only the rows where all the joined tables have related data.


SELECT first_name, phone, orders.cake_id, pickup_date
FROM customers INNER JOIN orders
ON customers.customer_id = orders.customer_id;
-- We won't get any customers without orders or any orders without customers.

-- Left outer joins give all the rows from the first table, but only related rows in the next table.


SELECT cake_id, pickup_date, customers.customer_id, first_name
FROM customers LEFT OUTER JOIN orders
ON orders.customer_id = customers.customer_id
ORDER BY pickup_date;
-- We'll get all the customers, and their orders if they have any


-- Right outer joins include any related rows in the first table, and all the rows in the next table.
SELECT customers.customer_id, first_name, pickup_date
FROM customers RIGHT OUTER JOIN orders
ON customers.customer_id = orders.customer_id
ORDER BY pickup_date;
-- We'll get the customer if there is one, and then every order.


-- Full outer joins take all the records from every table.
-- But MySQL doesn't support full outer joins! No problem, we can get the same result with a
-- UNION of left and right outer joins:
SELECT order_id, pickup_date, customers.customer_id, first_name
FROM orders LEFT OUTER JOIN customers
ON orders.customer_id = customers.customer_id

UNION

SELECT order_id, pickup_date, customers.customer_id, first_name
FROM orders RIGHT OUTER JOIN customers
ON orders.customer_id = customers.customer_id;


-- Cross joins give every row from the first table paired with every row in the next table,
-- ignoring any relationship. With customers and orders, we'd get every customer paired with every order.
-- Cross joins are sometimes called Cartesian joins because they return the cartesian product of data
-- sets—every combination of elements in every set.
--
-- This isn't used often because the results aren't usually useful.
-- But sometimes you might actually need every combination of the rows in your tables,
-- or you might need a large table for performance testing.
-- If you cross join 2 tables with 10,000 rows each, you get a table with 100,000,000 rows!


# Self joins refer to any join that joins data in the same table.
# For example, some of our customers were referred to our bakery by other customers.
# We could do a left outer join to get every customer and their referrer if they have one:
SELECT customer.first_name, referrer.first_name
FROM customers AS customer LEFT OUTER JOIN customers AS referrer
ON customer.referrer_id = referrer.customer_id;

