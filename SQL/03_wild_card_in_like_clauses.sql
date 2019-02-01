-- What ways can we use wildcard characters in LIKE clauses?
-- LIKE lets you use two wildcard characters, "%" and "_".
-- "%" matches any amount of characters (including zero characters).
-- So if we want all our customers whose last name starts with "Al", we could query:

SELECT * FROM customers c WHERE last_name LIKE 'al%'; -- Case insensitive

-- If you need it to match case, you can use the BINARY keywords
SELECT * FROM customers c WHERE last_name LIKE BINARY 'Al%';


-- "_" matches exactly one character.
-- If we want all our customers who live on the 200 block of Flatley Avenue in Dover, we could query

SELECT first_name, street_address FROM customers
WHERE street_address LIKE '2__ Flatley Avenue' AND city = 'Dover';


-- And some databases (like SQL Server, but not MySQL or PostgreSQL) support sets or ranges of characters.
-- So we could get every customer whose city starts with either "m" or "d":

SELECT customer_id FROM customers WHERE city LIKE '[md]%';

-- Or whose last name starts with any character in the range “a” through “m” (“a”, “b”, “c”...“k”, “l”, “m”):

SELECT customer_id FROM customers WHERE last_name LIKE '[a-m]%';


# TASK: Get all customers named Sam, or like Sam, who live in Dover.
SELECT * FROM customers c
WHERE c.first_name LIKE '%sam%' AND city = 'Dover';
-- 1072 rows in set (0.47 sec)

-- This is pretty slow. How to speed it up?
-- Indexing?

ALTER TABLE customers ADD INDEX (first_name);
-- 1072 rows in set (0.53 sec) (Like nothing ever happened. Even got worse.
-- It's because of the Function in the WHERE clause, which has to be evaluated for every record

-- First, we already know the city is Dover and the zip code is 33220, so we don't need to return all that along
-- with every result

SELECT c.first_name, c.last_name, c.street_address
FROM customers c
WHERE c.first_name LIKE '%sam%' AND c.city = 'Dover';
-- 1072 rows in set (0.41 sec)

-- A little better. But we can do much much better
-- We don't really need the wild card % before sam. We don't need people whose names don't begin with sam to be in the
-- query result. So..

SELECT c.first_name, c.last_name, c.street_address
FROM customers c
WHERE c.first_name LIKE 'sam%' AND c.city = 'Dover'
-- 1065 rows in set (0.02 sec)

-- That made a lot of difference. But also due to the indexing

