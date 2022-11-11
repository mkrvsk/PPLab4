-- MySQL Script generated by MySQL Workbench
-- Wed Oct 20 13:54:09 2021
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema art
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema art
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `art` DEFAULT CHARACTER SET utf8 ;
USE `art` ;

-- -----------------------------------------------------
-- Table `art`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `art`.`user` (
  `user_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(255) NOT NULL,
  `firstname` VARCHAR(255) NULL,
  `lastname` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`user_id`));


-- -----------------------------------------------------
-- Table `art`.`moderator`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `art`.`moderator` (
  `moderator_id` INT NOT NULL AUTO_INCREMENT,
  `moderatorname` VARCHAR(255) NOT NULL,
  `fristname` VARCHAR(255) NULL,
  `lastname` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NOT NULL,
  `moderatorkey` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`moderator_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `art`.`article`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `art`.`article` (
  `article_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `body` TEXT(8000) NOT NULL,
  `version` VARCHAR(32) NOT NULL,
  PRIMARY KEY (`article_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `art`.`state`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `art`.`state` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `art`.`updated_article`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `art`.`updated_article` (
  `article_id` INT NOT NULL,
  `state_id` INT NOT NULL,
  `moderator_id` INT NOT NULL,
  `user_id` INT UNSIGNED NOT NULL,
  `article_body` TEXT(8000) NULL,
  `date` VARCHAR(45) NULL DEFAULT 'CURRENT_TIMESTAMP',
  INDEX `fk_updated_article_state1_idx` (`state_id` ASC) VISIBLE,
  INDEX `fk_updated_article_article1_idx` (`article_id` ASC) VISIBLE,
  INDEX `fk_updated_article_moderator1_idx` (`moderator_id` ASC) VISIBLE,
  INDEX `fk_updated_article_user1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_updated_article_state1`
    FOREIGN KEY (`state_id`)
    REFERENCES `art`.`state` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_updated_article_article1`
    FOREIGN KEY (`article_id`)
    REFERENCES `art`.`article` (`article_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_updated_article_moderator1`
    FOREIGN KEY (`moderator_id`)
    REFERENCES `art`.`moderator` (`moderator_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_updated_article_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `art`.`user` (`user_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
