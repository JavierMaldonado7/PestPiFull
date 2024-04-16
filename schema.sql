create table if not exists users(user_id serial primary key, user_name varchar(15), user_email varchar(30), user_password varchar(20));
create table if not exists alerts(alert_id serial primary key, user_id integer references users(user_id), pi_id integer references pestpis(pi_id), alert_type varchar(20), alert_date DATETIME, alert_isActive BOOLEAN);
create table if not exists pestpis(pi_id serial primary key, user_id integer references users(user_id), pi_ipmain varchar(20) references mainpests(main_ip), pi_location varchar(20), pi_ip varchar(20), pi_status varchar(10));
create table if not exists mainpests(main_id serial primary key, user_id integer references users(user_id), main_ip varchar(20), pi_ip varchar(20) references pestpis(pi_ip));
