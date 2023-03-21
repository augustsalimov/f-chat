CREATE SCHEMA IF NOT EXISTS content; 

CREATE TABLE IF NOT EXISTS content.users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(25) UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE UNIQUE INDEX user_pass_idx ON content.users (username, password);