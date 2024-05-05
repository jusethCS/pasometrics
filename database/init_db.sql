\set ON_ERROR_STOP on

\echo
\echo
\echo

\c postgres

DROP DATABASE pasometricsdb;
CREATE DATABASE pasometricsdb;

\c pasometricsdb


CREATE TABLE horse (
    _id SERIAL PRIMARY KEY,
    _name TEXT NOT NULL
);

CREATE TABLE test (
    _id SERIAL PRIMARY KEY,
    _horse INTEGER NOT NULL 
        REFERENCES horse
		ON UPDATE cascade 
		ON DELETE set null,
    _date TIMESTAMP NOT NULL,
    _description TEXT
);

CREATE TABLE mt (
    _test_id INTEGER NOT NULL
        REFERENCES test
        ON UPDATE cascade 
        ON DELETE set null,
    _index INTEGER,
    _date DATE,
    _time TIME,
    _recording_time TIMESTAMP,
    _heart_rate INTEGER,
    _step_count INTEGER,
    _acceleration_x FLOAT,
    _acceleration_y FLOAT,
    _acceleration_z FLOAT,
    _attitude_pitch FLOAT,
    _attitude_roll FLOAT,
    _attitude_yaw FLOAT,
    _rotation_x FLOAT,
    _rotation_y FLOAT,
    _rotation_z FLOAT,
    _gravity_x FLOAT,
    _gravity_y FLOAT,
    _gravity_z FLOAT
);

CREATE TABLE m8 (
    _test_id INTEGER NOT NULL
        REFERENCES test
        ON UPDATE cascade 
        ON DELETE set null,
    _index INTEGER,
    _date DATE,
    _time TIME,
    _recording_time TIMESTAMP,
    _heart_rate INTEGER,
    _step_count INTEGER,
    _acceleration_x FLOAT,
    _acceleration_y FLOAT,
    _acceleration_z FLOAT,
    _attitude_pitch FLOAT,
    _attitude_roll FLOAT,
    _attitude_yaw FLOAT,
    _rotation_x FLOAT,
    _rotation_y FLOAT,
    _rotation_z FLOAT,
    _gravity_x FLOAT,
    _gravity_y FLOAT,
    _gravity_z FLOAT
);

CREATE TABLE ddt (
    _test_id INTEGER NOT NULL
        REFERENCES test
        ON UPDATE cascade 
        ON DELETE set null,
    _index INTEGER,
    _date DATE,
    _time TIME,
    _recording_time TIMESTAMP,
    _heart_rate INTEGER,
    _step_count INTEGER,
    _acceleration_x FLOAT,
    _acceleration_y FLOAT,
    _acceleration_z FLOAT,
    _attitude_pitch FLOAT,
    _attitude_roll FLOAT,
    _attitude_yaw FLOAT,
    _rotation_x FLOAT,
    _rotation_y FLOAT,
    _rotation_z FLOAT,
    _gravity_x FLOAT,
    _gravity_y FLOAT,
    _gravity_z FLOAT
);

CREATE TABLE dit (
    _test_id INTEGER NOT NULL
        REFERENCES test
        ON UPDATE cascade 
        ON DELETE set null,
    _index INTEGER,
    _date DATE,
    _time TIME,
    _recording_time TIMESTAMP,
    _heart_rate INTEGER,
    _step_count INTEGER,
    _acceleration_x FLOAT,
    _acceleration_y FLOAT,
    _acceleration_z FLOAT,
    _attitude_pitch FLOAT,
    _attitude_roll FLOAT,
    _attitude_yaw FLOAT,
    _rotation_x FLOAT,
    _rotation_y FLOAT,
    _rotation_z FLOAT,
    _gravity_x FLOAT,
    _gravity_y FLOAT,
    _gravity_z FLOAT
);

CREATE TABLE pdt (
    _test_id INTEGER NOT NULL
        REFERENCES test
        ON UPDATE cascade 
        ON DELETE set null,
    _index INTEGER,
    _date DATE,
    _time TIME,
    _recording_time TIMESTAMP,
    _heart_rate INTEGER,
    _step_count INTEGER,
    _acceleration_x FLOAT,
    _acceleration_y FLOAT,
    _acceleration_z FLOAT,
    _attitude_pitch FLOAT,
    _attitude_roll FLOAT,
    _attitude_yaw FLOAT,
    _rotation_x FLOAT,
    _rotation_y FLOAT,
    _rotation_z FLOAT,
    _gravity_x FLOAT,
    _gravity_y FLOAT,
    _gravity_z FLOAT
);

CREATE TABLE pit (
    _test_id INTEGER NOT NULL
        REFERENCES test
        ON UPDATE cascade 
        ON DELETE set null,
    _index INTEGER,
    _date DATE,
    _time TIME,
    _recording_time TIMESTAMP,
    _heart_rate INTEGER,
    _step_count INTEGER,
    _acceleration_x FLOAT,
    _acceleration_y FLOAT,
    _acceleration_z FLOAT,
    _attitude_pitch FLOAT,
    _attitude_roll FLOAT,
    _attitude_yaw FLOAT,
    _rotation_x FLOAT,
    _rotation_y FLOAT,
    _rotation_z FLOAT,
    _gravity_x FLOAT,
    _gravity_y FLOAT,
    _gravity_z FLOAT
);

CREATE TABLE dd8 (
    _test_id INTEGER NOT NULL
        REFERENCES test
        ON UPDATE cascade 
        ON DELETE set null,
    _index INTEGER,
    _date DATE,
    _time TIME,
    _recording_time TIMESTAMP,
    _heart_rate INTEGER,
    _step_count INTEGER,
    _acceleration_x FLOAT,
    _acceleration_y FLOAT,
    _acceleration_z FLOAT,
    _attitude_pitch FLOAT,
    _attitude_roll FLOAT,
    _attitude_yaw FLOAT,
    _rotation_x FLOAT,
    _rotation_y FLOAT,
    _rotation_z FLOAT,
    _gravity_x FLOAT,
    _gravity_y FLOAT,
    _gravity_z FLOAT
);

CREATE TABLE di8 (
    _test_id INTEGER NOT NULL
        REFERENCES test
        ON UPDATE cascade 
        ON DELETE set null,
    _index INTEGER,
    _date DATE,
    _time TIME,
    _recording_time TIMESTAMP,
    _heart_rate INTEGER,
    _step_count INTEGER,
    _acceleration_x FLOAT,
    _acceleration_y FLOAT,
    _acceleration_z FLOAT,
    _attitude_pitch FLOAT,
    _attitude_roll FLOAT,
    _attitude_yaw FLOAT,
    _rotation_x FLOAT,
    _rotation_y FLOAT,
    _rotation_z FLOAT,
    _gravity_x FLOAT,
    _gravity_y FLOAT,
    _gravity_z FLOAT
);

CREATE TABLE pd8 (
    _test_id INTEGER NOT NULL
        REFERENCES test
        ON UPDATE cascade 
        ON DELETE set null,
    _index INTEGER,
    _date DATE,
    _time TIME,
    _recording_time TIMESTAMP,
    _heart_rate INTEGER,
    _step_count INTEGER,
    _acceleration_x FLOAT,
    _acceleration_y FLOAT,
    _acceleration_z FLOAT,
    _attitude_pitch FLOAT,
    _attitude_roll FLOAT,
    _attitude_yaw FLOAT,
    _rotation_x FLOAT,
    _rotation_y FLOAT,
    _rotation_z FLOAT,
    _gravity_x FLOAT,
    _gravity_y FLOAT,
    _gravity_z FLOAT
);

CREATE TABLE pi8 (
    _test_id INTEGER NOT NULL
        REFERENCES test
        ON UPDATE cascade 
        ON DELETE set null,
    _index INTEGER,
    _date DATE,
    _time TIME,
    _recording_time TIMESTAMP,
    _heart_rate INTEGER,
    _step_count INTEGER,
    _acceleration_x FLOAT,
    _acceleration_y FLOAT,
    _acceleration_z FLOAT,
    _attitude_pitch FLOAT,
    _attitude_roll FLOAT,
    _attitude_yaw FLOAT,
    _rotation_x FLOAT,
    _rotation_y FLOAT,
    _rotation_z FLOAT,
    _gravity_x FLOAT,
    _gravity_y FLOAT,
    _gravity_z FLOAT
);

CREATE TABLE board (
    _test_id INTEGER NOT NULL
        REFERENCES test
        ON UPDATE cascade 
        ON DELETE set null,
    _softness_mean FLOAT,
    _softness_max FLOAT,
    _deviation FLOAT,
    _force_mean_front_right_leg FLOAT,
    _force_mean_front_left_leg FLOAT,
    _force_mean_hind_right_leg FLOAT,
    _force_mean_hind_left_leg FLOAT,
    _force_max_front_right_leg FLOAT,
    _force_max_front_left_leg FLOAT,
    _force_max_hind_right_leg FLOAT,
    _force_max_hind_left_leg FLOAT,
    _vel_mean_front_right_leg FLOAT,
    _vel_mean_front_left_leg FLOAT,
    _vel_mean_hind_right_leg FLOAT,
    _vel_mean_hind_left_leg FLOAT,
    _vel_max_front_right_leg FLOAT,
    _vel_max_front_left_leg FLOAT,
    _vel_max_hind_right_leg FLOAT,
    _vel_max_hind_left_leg FLOAT,
    _heart_rate_mean FLOAT,
    _heart_rate_max FLOAT
);

CREATE TABLE eight (
    _test_id INTEGER NOT NULL
        REFERENCES test
        ON UPDATE cascade 
        ON DELETE set null,
    _softness_mean FLOAT,
    _softness_max FLOAT,
    _left_turn_mean FLOAT,
    _left_turn_max FLOAT,
    _right_turn_mean FLOAT,
    _right_turn_max FLOAT,
    _force_mean_front_right_leg FLOAT,
    _force_mean_front_left_leg FLOAT,
    _force_mean_hind_right_leg FLOAT,
    _force_mean_hind_left_leg FLOAT,
    _force_max_front_right_leg FLOAT,
    _force_max_front_left_leg FLOAT,
    _force_max_hind_right_leg FLOAT,
    _force_max_hind_left_leg FLOAT,
    _vel_mean_front_right_leg FLOAT,
    _vel_mean_front_left_leg FLOAT,
    _vel_mean_hind_right_leg FLOAT,
    _vel_mean_hind_left_leg FLOAT,
    _vel_max_front_right_leg FLOAT,
    _vel_max_front_left_leg FLOAT,
    _vel_max_hind_right_leg FLOAT,
    _vel_max_hind_left_leg FLOAT,
    _heart_rate_mean FLOAT,
    _heart_rate_max FLOAT
);