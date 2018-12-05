# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: localhost (MySQL 5.5.5-10.1.21-MariaDB)
# Database: foodhygiene
# Generation Time: 2018-12-05 10:53:19 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table fhr_business_type
# ------------------------------------------------------------

DROP TABLE IF EXISTS `fhr_business_type`;

CREATE TABLE `fhr_business_type` (
  `business_type_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `business_type_name` varchar(50) DEFAULT '',
  PRIMARY KEY (`business_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `fhr_business_type` WRITE;
/*!40000 ALTER TABLE `fhr_business_type` DISABLE KEYS */;

INSERT INTO `fhr_business_type` (`business_type_id`, `business_type_name`)
VALUES
	(1,'Restaurant'),
	(5,'Hospitals and Child Care'),
	(7,'Distributors/Transporters'),
	(14,'Importers/Exporters'),
	(4613,'Retailer'),
	(7838,'Farmers'),
	(7839,'Manufacturer'),
	(7840,'Supermarket'),
	(7841,'Catering'),
	(7842,'Hotel'),
	(7843,'Bar'),
	(7844,'Takeaway'),
	(7845,'Place of Education'),
	(7846,'Mobile Caterer');

/*!40000 ALTER TABLE `fhr_business_type` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
