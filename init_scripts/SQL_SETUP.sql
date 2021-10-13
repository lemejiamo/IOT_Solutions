CREATE DATABASE IF NOT EXISTS IOT_Solutions_dev;
CREATE USER IF NOT EXISTS 'IOT_DEV'@'localhost' IDENTIFIED BY 'IOTDEV';
GRANT ALL PRIVILEGES ON `IOT_Solutions_dev`.* TO 'IOT_DEV'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'IOT_DEV'@'localhost';
FLUSH PRIVILEGES;