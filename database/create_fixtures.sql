CREATE USER postgres;
CREATE DATABASE docker;
GRANT ALL PRIVILEGES ON DATABASE docker TO postgres;

CREATE TABLE IF NOT EXISTS accounts (
    firstname VARCHAR,
    lastname VARCHAR,
    username VARCHAR
);