 create database petadoption;
 use petadoption;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
ALTER TABLE users ADD COLUMN role VARCHAR(20) DEFAULT 'user';

INSERT INTO users (username, password)
VALUES ('sneha_admin', 'singhsneha25');
Select * from users;

INSERT INTO users (username, password)
VALUES ('bhagyashree', 'sangvebhagya13');

INSERT INTO users (username, password, role)
VALUES ('soumya', 'sinhasoumya71', 'user');

CREATE TABLE pets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    breed VARCHAR(100),
    category ENUM('cat', 'dog'),
    status VARCHAR(50),
    image_url TEXT
);

CREATE TABLE adoption_requests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    pet_id INT,
    status VARCHAR(50),
    request_date DATETIME
);

CREATE TABLE donations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    amount DECIMAL(10,2),
    message TEXT,
    donation_date DATETIME
);

CREATE TABLE messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    subject VARCHAR(100),
    content TEXT,
    sent_at DATETIME
);

ALTER TABLE adoption_requests
ADD CONSTRAINT fk_user
FOREIGN KEY (user_id) REFERENCES users(id)
ON DELETE CASCADE;

ALTER TABLE adoption_requests
ADD CONSTRAINT fk_pet
FOREIGN KEY (pet_id) REFERENCES pets(id)
ON DELETE CASCADE;

ALTER TABLE donations
ADD FOREIGN KEY (user_id) REFERENCES users(id);

ALTER TABLE messages
ADD FOREIGN KEY (user_id) REFERENCES users(id);
