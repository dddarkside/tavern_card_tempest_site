-- Удаление всех таблиц
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS auth;

-- Создание таблицы users
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mail VARCHAR(255) UNIQUE,
    name VARCHAR(255)
);

-- Создание таблицы events
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) UNIQUE,
    date DATE,
    participants INT[]
);

-- Создание таблицы auth
CREATE TABLE IF NOT EXISTS auth (
    id INT,
    password VARCHAR(255),
    FOREIGN KEY (id) REFERENCES users(id)
);