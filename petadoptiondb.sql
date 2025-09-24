 create database petadoption;
 use petadoption;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20)
);

INSERT INTO users (username, password, role,email)
VALUES ('sneha', 'scrypt:32768:8:1$2XnVq8iKYyIkXQrG$e5b0cc5b2dfbd3175e34fdb1d0344e967f76184fe53ea912591a1a207f89d006a1828156cdfe0f5869ef301aad7f3b461912d871f7ea7aaf7f94a3536cebf4ee', 'admin','snehasingh.connect@gmail.com');

INSERT INTO users (username, password, role,email)
VALUES ('bhagyashree', 'scrypt:32768:8:1$ODyqZktqoC60aLWG$c32a2c8575ea499f3cacdbdf2e34aaaa2978ce21266acba638cc2a93161d1053184c8ee3a05b5191850780241e006da184335e1158716b4766efb8bea8bfc762', 'user','bhagyashrisangve@gmail.com');

select * from users;

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

SELECT username, password FROM users;

