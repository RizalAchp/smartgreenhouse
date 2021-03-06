CREATE DATABASE IF NOT EXISTS `python_mysql`;

USE `python_mysql`;

DROP TABLE IF EXISTS `dht_sensor`;
CREATE TABLE IF NOT EXISTS `dht_sensor`(
    `id_dht` INT(11) AUTO_INCREMENT PRIMARY KEY,
    `humidity` DECIMAL(10,2) NOT NULL,
    `temp` DECIMAL(10,2) NOT NULL,
    `waktu_dht` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=INNODB;

DROP TABLE IF EXISTS `soil_sensor`;
CREATE TABLE IF NOT EXISTS `soil_sensor`(
    `id_soil` INT(11) AUTO_INCREMENT PRIMARY KEY,
    `moisture` DECIMAL(10,2) NOT NULL,
    `waktu_soil` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=INNODB;

DROP TABLE IF EXISTS `sensor_etc`;
CREATE TABLE IF NOT EXISTS `sensor_etc`(
    `id_dht` INT(11) AUTO_INCREMENT PRIMARY KEY,
    `jarak` DECIMAL(10,2) NOT NULL,
    `cahaya` DECIMAL(10,2) NOT NULL,
    `waktu_etc` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=INNODB;
