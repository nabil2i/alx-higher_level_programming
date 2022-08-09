-- creates a table called first_table in the current database in the MySQL server
-- no failure even if the table exists already
CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
