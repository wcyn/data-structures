CREATE TABLE cakes (
    cake_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    flavor VARCHAR(100) NOT NULL
);

CREATE TABLE customers (
    customer_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    phone VARCHAR(15),
    street_address VARCHAR(255),
    city VARCHAR(255),
    zip_code VARCHAR(5),
    referrer_id INT,
    FOREIGN KEY (referrer_id) REFERENCES customers (customer_id)
);

CREATE TABLE orders (
    order_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    cake_id INT NOT NULL,
    customer_id INT,
    pickup_date DATE NOT NULL,
    FOREIGN KEY (cake_id) REFERENCES cakes (cake_id),
    FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
);
