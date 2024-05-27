\set ON_ERROR_STOP on

\echo
\echo
\echo

\c postgres

DROP DATABASE pasometricsdb;
CREATE DATABASE pasometricsdb;

\c pasometricsdb

CREATE TABLE users (
    username TEXT NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    lastname TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE horse (
    id TEXT NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    birthday DATE,
    gait TEXT,
    gender TEXT
);

CREATE TABLE view (
    username TEXT NOT NULL 
        REFERENCES users
		ON UPDATE cascade 
		ON DELETE set null,
    horse TEXT NOT NULL 
        REFERENCES horse
		ON UPDATE cascade 
		ON DELETE set null,
    class TEXT
);

CREATE TABLE test (
    id SERIAL PRIMARY KEY,
    horse TEXT NOT NULL 
        REFERENCES horse
		ON UPDATE cascade 
		ON DELETE set null,
    date TIMESTAMP NOT NULL,
    testtype TEXT NOT NULL
);
