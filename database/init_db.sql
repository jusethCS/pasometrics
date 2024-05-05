\set ON_ERROR_STOP on

\echo
\echo
\echo

\c postgres

DROP DATABASE pasometricsdb;
CREATE DATABASE pasometricsdb;

\c pasometricsdb


CREATE TABLE horse (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE test (
    id SERIAL PRIMARY KEY,
    horse INTEGER NOT NULL 
        REFERENCES horse
		ON UPDATE cascade 
		ON DELETE set null,
    date TIMESTAMP NOT NULL,
    description TEXT
);
