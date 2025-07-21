-- init.sql

CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    content TEXT,
    author_id INTEGER REFERENCES authors(id),
    published_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO authors (name, email) VALUES
('Alice Johnson', 'alice@example.com'),
('Bob Smith', 'bob@example.com');

INSERT INTO posts (title, content, author_id) VALUES
('First Post', 'Hello, this is my first post! I am here to create a aesthetic porfolio of mine', 1),
('Second Post', 'Another day, another post. The climate is so cool today', 2);
