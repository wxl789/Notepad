-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: db_cement_bill
-- ------------------------------------------------------
-- Server version	5.7.23-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(80) NOT NULL,
  `email` varchar(120) DEFAULT NULL,
  `password` varchar(32) NOT NULL,
  `avatar_hash` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'jfxu',NULL,'jfxu',NULL),(2,'tom',NULL,'tom',NULL);
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('665eaeea5bb3');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bill`
--

DROP TABLE IF EXISTS `bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bill` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `destination` varchar(45) NOT NULL,
  `si_ji` varchar(45) NOT NULL,
  `kai_piao_ren` varchar(45) NOT NULL,
  `t` int(11) NOT NULL,
  `price` int(11) DEFAULT NULL,
  `notes` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill`
--

LOCK TABLES `bill` WRITE;
/*!40000 ALTER TABLE `bill` DISABLE KEYS */;
INSERT INTO `bill` VALUES (1,'2018-08-04','兴宇','许家勇','徐苗英',6,500,''),(2,'2018-08-06','丁山河','许家勇','徐苗英',10,25,''),(3,'2018-08-06','仁和绿化\n','许家军','徐苗英',10,30,''),(4,'2018-10-01','下沙\n','王彬\n','冯美亚',13,0,''),(5,'2018-10-22','下沙de','许家军','冯美亚',100,1000,''),(6,'2018-12-01','下沙','许俊峰','李文明',100,230,'呵呵哒'),(7,'2019-03-04','北京','许家勇','金主',10000,100000,'厉害了'),(8,'2018-12-02','下沙','许俊峰','李文明',100,230,'呵呵哒'),(9,'2016-09-03','九堡','许家军','李文娥',200,500,'还可以'),(10,'2018-04-05','临平','许俊峰','自己',299,300,''),(11,'2010-12-01','下沙','许家平','李斌',100,500,'来了'),(12,'2016-09-30','九堡','许家军','自己',200,500,'还可以'),(13,'2014-02-01','黄山','自己','自己',2000,10000,''),(14,'2018-12-22','黄山','自己','自己',19,300,''),(15,'2014-05-08','滨江','啊九','桦翼',100,399,''),(16,'2018-12-04','黄山','阿斌','桦翼',200,345,''),(18,'2019-12-01','黄山','小明','金峰',199,200,'呵呵'),(21,'2018-10-27','合肥','小明','金峰',29,499,''),(22,'2019-11-11','基金风','爱里','积极',199,2333,'啊地方'),(23,'2019-11-11','基金风','爱里','积极',199,2333,'啊地方'),(25,'2012-12-01','目的地','阿兰','小麦',100,222,'呵呵打'),(29,'2010-12-12','金沙和','敖东','矜持',200,1212,'撒地方'),(30,'2019-12-11','金华','晓东','李刘',10,900,'已付'),(32,'2019-12-11','全球',' 全球','全球全球',100,12,'qq');
/*!40000 ALTER TABLE `bill` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-31  2:01:22
