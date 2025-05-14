DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS mahasiswa;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE mahasiswa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT NOT NULL,
    nim TEXT UNIQUE NOT NULL
);

INSERT INTO users (username, password) VALUES ('admin', 'password123');