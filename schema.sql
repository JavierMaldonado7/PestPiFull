-- create table if not exists users(user_id serial primary key, user_name varchar(15), user_email varchar(30), user_password varchar(20));
-- create table if not exists alerts(alert_id serial primary key, user_id integer references users(user_id), pi_id integer references pestpis(pi_id), alert_type varchar(20), alert_date DATETIME, alert_isActive BOOLEAN);
-- create table if not exists pestpis(pi_id serial primary key, user_id integer references users(user_id), pi_ipmain varchar(20) references mainpests(main_ip), pi_location varchar(20), pi_ip varchar(20), pi_status varchar(10));
-- create table if not exists mainpests(main_id serial primary key, user_id integer references users(user_id), main_ip varchar(20), pi_ip varchar(20) references pestpis(pi_ip));


-- new schema
-- Users table
CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    user_name VARCHAR(15),
    user_email VARCHAR(30),
    user_password VARCHAR(20)
);

-- pestpis table, modified with unique constraint on pi_ip
CREATE TABLE IF NOT EXISTS pestpis (
    pi_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    pi_ipmain VARCHAR(20), -- Assuming no foreign key here unless absolutely necessary
    pi_location VARCHAR(20),
    pi_ip VARCHAR(20) UNIQUE,  -- Now with UNIQUE constraint
    pi_status VARCHAR(10)
);

-- mainpests table, assuming pi_ip is now uniquely constrained
CREATE TABLE IF NOT EXISTS mainpests (
    main_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    main_ip VARCHAR(20),
    pi_ip VARCHAR(20) REFERENCES pestpis(pi_ip)  -- Reference is valid with unique constraint
);

-- Alerts table
CREATE TABLE IF NOT EXISTS alerts (
    alert_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    pi_id INTEGER REFERENCES pestpis(pi_id),
    alert_type VARCHAR(20),
    alert_date TIMESTAMP, -- Using timestamp instead of DATETIME
    alert_isActive BOOLEAN
);
