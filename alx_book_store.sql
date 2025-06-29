-- 1. Create the database and switch to it
CREATE DATABASE IF NOT EXISTS alx_book_store
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
USE alx_book_store;

-- 2. Authors table
CREATE TABLE Authors (
  author_id INT AUTO_INCREMENT PRIMARY KEY,
  author_name VARCHAR(215) NOT NULL
) ENGINE=InnoDB;

-- 3. Books table
CREATE TABLE Books (
  book_id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(130) NOT NULL,
  author_id INT NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  publication_date DATE,
  FOREIGN KEY (author_id)
    REFERENCES Authors(author_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB;

-- 4. Customers table
CREATE TABLE Customers (
  customer_id INT AUTO_INCREMENT PRIMARY KEY,
  customer_name VARCHAR(215) NOT NULL,
  email VARCHAR(215) NOT NULL UNIQUE,
  address TEXT
) ENGINE=InnoDB;

-- 5. Orders table
CREATE TABLE Orders (
  order_id INT AUTO_INCREMENT PRIMARY KEY,
  customer_id INT NOT NULL,
  order_date DATE NOT NULL DEFAULT (CURRENT_DATE),
  FOREIGN KEY (customer_id)
    REFERENCES Customers(customer_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
) ENGINE=InnoDB;

-- 6. Order_Details table
CREATE TABLE Order_Details (
  orderdetailid INT AUTO_INCREMENT PRIMARY KEY,
  order_id INT NOT NULL,
  book_id INT NOT NULL,
  quantity DOUBLE NOT NULL CHECK (quantity > 0),
  FOREIGN KEY (order_id)
    REFERENCES Orders(order_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  FOREIGN KEY (book_id)
    REFERENCES Books(book_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB;
