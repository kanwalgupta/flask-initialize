CREATE TABLE IF NOT EXISTS passengers (
    id serial PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    gender VARCHAR(255),
    age INTEGER
);
