-- creates the table id_not_null on your MySQL server
-- doesn't fail
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
