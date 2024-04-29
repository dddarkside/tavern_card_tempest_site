-- Удаление всех таблиц
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS auth;

-- Создание таблицы users
CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY,
    mail VARCHAR(255),
    name VARCHAR(255)
);

-- Создание таблицы events
CREATE TABLE IF NOT EXISTS events (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    date DATE,
    participants INT[]
);

-- Создание таблицы auth
CREATE TABLE IF NOT EXISTS auth (
    id INT,
    password VARCHAR(255),
    FOREIGN KEY (id) REFERENCES users(id)
);