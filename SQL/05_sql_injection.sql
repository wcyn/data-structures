-- SQL injection is when a hacker gains access to our database because
-- we used their malicious user input to build a dynamic SQL query.
-- Example Python code
-- sql_text = "SELECT * FROM customers WHERE phone = '%s'" % phone_input

-- We’re expecting something like "8015550198" which would give us:
-- SELECT * FROM customers WHERE phone = '8015550198';

-- But what if a user enters "1' OR 1=1;-- "?

-- Then we’d have:

SELECT * FROM customers WHERE phone = '1' OR 1=1;-- ';
-- This will return the data for every customer because the WHERE clause will always evaluate to true

-- Five ways to prevent SQL injection

-- 1. Use stored procedures or prepared SQL statements. Do not build dynamic SQL

-- 2. Validate the type and pattern of input.

-- 3. Escape special characters like quotes. This approach is a quick and easy way to reduce the chances of
-- SQL injection, but it's not fully effective.
-- When we escape our input, now our query will be:
  SELECT * FROM customers WHERE phone = '1\' OR 1=1;-- '; -- Not a valid query

-- 4. Limit database privileges.
-- Application accounts that connect to the database should have as few privileges as possible.
-- It's unlikely, for example, that your application will ever have to delete a table.
-- So don't allow it.
