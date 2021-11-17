-- Database setup script should go here

-- TESTING
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema dbproject
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema dbproject
-- -----------------------------------------------------
-- CREATE SCHEMA IF NOT EXISTS `dbproject` DEFAULT CHARACTER SET utf8 ;
-- USE `dbproject` ;

-- -----------------------------------------------------
-- Table `dbproject`.`LISTING`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbproject`.`LISTING` (
  `listing_mls_number` INT NOT NULL AUTO_INCREMENT,
  `listing_type` VARCHAR(45) NOT NULL,
  `listing_status` VARCHAR(45) NOT NULL,
  `listing_description` VARCHAR(3000) NOT NULL,
  `listing_sale_yn` TINYINT NOT NULL,
  `listing_rent_yn` TINYINT NOT NULL,
  `listing_price` BIGINT NOT NULL,
  `listing_original_price` BIGINT NOT NULL,
  `listing_address_number` INT NOT NULL,
  `listing_address_street` VARCHAR(45) NOT NULL,
  `listing_address_city` VARCHAR(45) NOT NULL,
  `listing_address_state` VARCHAR(45) NOT NULL,
  `listing_address_zip` MEDIUMINT NOT NULL,
  `listing_structure_style` VARCHAR(45) NOT NULL,
  `listing_bedroom_count` SMALLINT NOT NULL,
  `listing_full_bath_count` SMALLINT NOT NULL,
  `listing_half_bath_count` SMALLINT NOT NULL,
  `listing_basement_yn` TINYINT NOT NULL,
  `listing_waterfront_yn` TINYINT NOT NULL,
  `listing_fireplace_yn` TINYINT NOT NULL,
  `listing_garage_yn` TINYINT NOT NULL,
  `listing_pool_yn` TINYINT NOT NULL,
  `listing_ownership` VARCHAR(45) NOT NULL,
  `listing_school_district` VARCHAR(45) NOT NULL,
  `listing_garage_car_count` SMALLINT NOT NULL,
  `listing_above_grade_sqft` MEDIUMINT NOT NULL,
  `listing_acreage` DECIMAL NOT NULL,
  `listing_year_built` MEDIUMINT NOT NULL,
  `listing_date` DATE NOT NULL,
  `listing_agent_license_number` INT NOT NULL,
  `listing_colisting_agent_license_number` INT,
  `listing_image_links` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`listing_mls_number`))
ENGINE = InnoDB;

/*
insert into
`dbproject`.`LISTING`( `listing_mls_number`,`listing_type`,`listing_status`, `listing_description`,
`listing_sale_yn`,`listing_rent_yn`,`listing_price`,`listing_original_price`,`listing_address_number`,
`listing_address_street`, `listing_address_city`, `listing_address_state`,
`listing_address_zip`,`listing_structure_style`,`listing_bedroom_count`, `listing_full_bath_count`,
`listing_half_bath_count`,`listing_basement_yn`,`listing_waterfront_yn`,`listing_fireplace_yn`, `listing_garage_yn`,
`listing_pool_yn`, `listing_ownership`,`listing_school_district`,`listing_garage_car_count`,
`listing_above_grade_sqft`,`listing_acreage`,`listing_year_built`,`listing_date`,`listing_agent_license_number`,
`listing_colisting_agent_license_number`, `listing_image_links`) values

(12345, 'Family', 'Sale', 'Insert random description', 1, 0, 323425, 45246, 4726, 'Fruit Street',
'Las Vegas', 'Nevada', '45361', 'Style', 3, 2, 1, 0, 1, 0, 1, 1, 'owernship', 'Fun Elementary School',
2, 234, 345, 1956, '2018-04-23', '345', '435', 'www.image');


 UPDATE:
update LISTING set listing_status = 'Not for sale' where listing_mls_number = 12345; */

/* DELETE:
DELETE FROM LISTING WHERE listing_mls_number='12325';

select * from LISTING; 

 /*SEARCH: select * from LISTING WHERE listing_address_zip LIKE */

-- ----------
-------------------------------------------
-- Table `dbproject`.`CLIENT`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbproject`.`CLIENT` (
  `client_id` INT NOT NULL,
  `client_first_name` VARCHAR(45) NOT NULL,
  `client_middle_initial` VARCHAR(45) NULL,
  `client_last_name` VARCHAR(45) NOT NULL,
  `client_area_code` MEDIUMINT NOT NULL,
  `client_phone_number` INT NOT NULL,
  `client_email_address` VARCHAR(45) NOT NULL,
  `client_agent_license_number` INT NOT NULL,
  `LISTING_mls_number` INT NULL,
  PRIMARY KEY (`client_id`),
  INDEX `fk_CLIENT_LISTING1_idx` (`LISTING_mls_number` ASC) VISIBLE,
  CONSTRAINT `fk_CLIENT_LISTING1`
    FOREIGN KEY (`LISTING_mls_number`)
    REFERENCES `dbproject`.`LISTING` (`listing_mls_number`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


/*
insert into
`dbproject`.`CLIENT`(`client_id`, `client_first_name`, `client_middle_initial`, 
`client_last_name`,`client_area_code`, `client_phone_number`, `client_email_address`,
`client_agent_license_number`) values

(003,'Lisa','','Zhang','123','4567890', 'email@gmail.com','123'),
(004,'John','','Doe','123','4567899', 'email1@gmail.com','010');


select * from CLIENT;


DELETE FROM CLIENT WHERE client_id='002';*/

-- -----------------------------------------------------
-- Table `dbproject`.`AGENT`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbproject`.`AGENT` (
  `agent_license_number` INT NOT NULL,
  `agent_first_name` VARCHAR(45) NOT NULL,
  `agent_middle_initial` VARCHAR(45) NULL,
  `agent_last_name` VARCHAR(45) NOT NULL,
  `agent_office_area_code` MEDIUMINT NOT NULL,
  `agent_office_phone_number` INT NOT NULL,
  `agent_mobile_area_code` MEDIUMINT NOT NULL,
  `agent_mobile_phone_number` INT NOT NULL,
  `agent_email_address` VARCHAR(45) NOT NULL,
  `agent_office_street` VARCHAR(45) NOT NULL,
  `agent_office_city` VARCHAR(45) NOT NULL,
  `agent_office_state` VARCHAR(45) NOT NULL,
  `agent_office_zip` MEDIUMINT NOT NULL,
  `agent_company_id` INT NOT NULL,
  `CLIENT_id` INT NULL,
  `LISTING_mls_number` INT NULL,
  PRIMARY KEY (`agent_license_number`),
  INDEX `fk_AGENT_CLIENT1_idx` (`CLIENT_id` ASC) VISIBLE,
  INDEX `fk_AGENT_LISTING1_idx` (`LISTING_mls_number` ASC) VISIBLE,
  CONSTRAINT `fk_AGENT_CLIENT1`
    FOREIGN KEY (`CLIENT_id`)
    REFERENCES `dbproject`.`CLIENT` (`client_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_AGENT_LISTING1`
    FOREIGN KEY (`LISTING_mls_number`)
    REFERENCES `dbproject`.`LISTING` (`listing_mls_number`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

/*
insert into 
`dbproject`.`AGENT`(`agent_license_number`, `agent_first_name`, `agent_middle_initial`,
`agent_last_name`, `agent_office_area_code`, `agent_office_phone_number`, `agent_mobile_area_code`,
`agent_mobile_phone_number`, `agent_email_address`, `agent_office_street`, `agent_office_city`,
`agent_office_state`, `agent_office_zip`, `agent_company_id`, `CLIENT_id`, `LISTING_mls_number`) values

(999, 'Sarah', 'S', 'Smith', '485', '6527446', '584', '5869385', 'sarah@gmail.com', 'Water Street', 'Rochester Hills', 'Michigan', '48309', '785', '395', '38049'),
(998, 'Sam', 'W', 'Smith', '485', '6527446', '584', '5869385', 'sarah@gmail.com', 'Water Street', 'Rochester Hills', 'Michigan', '48309', '785', '395', '38049');

select * from AGENT WHERE agent_license_number;
DELETE FROM AGENT WHERE agent_license_number=999;*/


-- -----------------------------------------------------
-- Table `dbproject`.`COMPANY`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbproject`.`COMPANY` (
  `company_id` INT NOT NULL,
  `company_hq_street` VARCHAR(45) NOT NULL,
  `company_hq_city` VARCHAR(45) NOT NULL,
  `company_hq_state` VARCHAR(45) NOT NULL,
  `company_hq_zip` MEDIUMINT NOT NULL,
  `company_hq_phone_area` MEDIUMINT NOT NULL,
  `company_hq_phone_number` INT NOT NULL,
  `company_hq_fax_area` MEDIUMINT NOT NULL,
  `company_hq_fax_number` INT NOT NULL,
  `company_license_number` INT NOT NULL,
  `AGENT_license_number` INT NULL,
  PRIMARY KEY (`company_id`),
  INDEX `fk_COMPANY_AGENT_idx` (`AGENT_license_number` ASC) VISIBLE,
  CONSTRAINT `fk_COMPANY_AGENT`
    FOREIGN KEY (`AGENT_license_number`)
    REFERENCES `dbproject`.`AGENT` (`agent_license_number`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

/*
insert into
`dbproject`.`COMPANY`(`company_id`, `company_hq_street`, `company_hq_city`,`company_hq_state`,
`company_hq_zip`, `company_hq_phone_area`, `company_hq_phone_number`,`company_hq_fax_area`,
`company_hq_fax_number`,`company_license_number`,`AGENT_license_number`) values
(123, 'Tree Street', 'Detroit', 'Michigan', 48309, 123, 4567891, 123, 1234123, 451, 001);


DELETE FROM COMPANY WHERE company_id=123;*/

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;