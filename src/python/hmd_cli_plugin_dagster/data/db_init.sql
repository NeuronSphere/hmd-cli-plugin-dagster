CREATE USER dagster_user WITH PASSWORD 'dagster_password';

CREATE DATABASE dagster;

GRANT ALL PRIVILEGES ON DATABASE dagster TO dagster_user;