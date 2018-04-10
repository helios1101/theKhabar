-- MySQL dump 10.13  Distrib 5.7.21, for Linux (x86_64)
--
-- Host: localhost    Database: myapp
-- ------------------------------------------------------
-- Server version	5.7.21-0ubuntu0.16.04.1

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
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(80) DEFAULT NULL,
  `password` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userInfo`
--

DROP TABLE IF EXISTS `userInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userInfo` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(300) DEFAULT NULL,
  `username` varchar(300) DEFAULT NULL,
  `email` varchar(300) DEFAULT NULL,
  `password` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userInfo`
--

LOCK TABLES `userInfo` WRITE;
/*!40000 ALTER TABLE `userInfo` DISABLE KEYS */;
INSERT INTO `userInfo` VALUES (32,'aaaa','aaaa','aaaa','$5$rounds=535000$w1nHptZrHmrnyuM9$fzXEWrGtStanW5o5M05.z/VC9xesQdTWiEODLdOm8rA'),(33,'manan','manan','manan','$5$rounds=535000$4wru7yfYoADjE5H0$JoEzGLUVIA5pFEsJFkBrgqi184So60ndOT2W2rIqBq4'),(34,'pulkit','pulkit','pulkit','$5$rounds=535000$Z5WR2SpB/mPJKKlE$9jkZJ59ewWDjq1Ku8BsCNu9Jc0wh3ogZAu4JPDIajZ/'),(35,'preet','preet123','preet','$5$rounds=535000$a35A4ENrxNlIyHI3$rYkdDCrD2lWRrxPIVORQtvf.Mky7PAm/9VCied0T.vB'),(36,'paya','paya123','paya','$5$rounds=535000$KcGvp9BdDvXUXGI.$4VE3huFvAp3rW/SThAyrveI12umd3lhzeUdWJnWQJWB'),(37,'riaa','ria123','riaa','$5$rounds=535000$l/l8g0kSJfu6AHmM$Xd83aseddDECoBw88/GEjno5WP5oBRFK5wEICmcNVM0'),(39,'manav','manav','manav','$5$rounds=535000$uw1m7chPBrjB8zwX$SsVrCH8LgJk9/ee.DTlG0Iydvpw1uN04bhDUHR8r.S6'),(40,'dhwani','dhwani','dhwani','$5$rounds=535000$wbJC7T22r8.6iZV.$Q/SoLJ/jlp0g.j/xO8BwvgZNyZSMSxh6nmTbo3WKOGC'),(41,'dddd','dddd','dddd','$5$rounds=535000$0Bp1QUwN2lJTC1J0$oMKKgJgrnH/G7Qn6/JbY5JWnkIpNzefEdsoIVqn0yv2'),(42,'xxxx','xxxx','xxxx','$5$rounds=535000$ALl6cqL1vgFIpYnB$/BvLJqzpf6KrwXyLvz3Lyfpdwit8mxS.l9t9K32NMP8'),(43,'yyyy','yyyy','yyyy','$5$rounds=535000$VS0OsOtp1jlbxkTM$ORGzTSzsqRP30B7iBTwEOZE4RX2qG94hC8hk7EZ4dy/'),(44,'zzzz','zzzz','zzzz','$5$rounds=535000$KUqDErO67wGcsbu1$uKQ2DU431CSxBh.CxjBsPPx93D2KRoj1L5UpqPyUZJ.'),(45,'wwww','wwww','wwww','$5$rounds=535000$hsTVQLsUmrYXZmr7$RKLJz1dVXjyTwJF8NeIMSwX1ruDv6dOczqemCgeHkQD'),(46,'llll','llll','llll','$5$rounds=535000$/bs.V1A8YOtWZtMn$rvBELvZPnjbEXVJf.L0LhtOZ7PLZLIe0v5PNed/8vrD'),(47,'rrrr','rrrr','rrrr','$5$rounds=535000$fOKMdUntp13zzq7M$6s8.SQI0IgWzuBIparAmS9Hz0er2YBTRyYOYJVx48KA'),(48,'kkkk','kkkk','kkkk','$5$rounds=535000$WYKxFg/KpztPtdmM$..bGTQP3lKb7SCy4D1JNpZgchHorjVwNaWmaQLHYz2/'),(49,'uuuu','uuuu','uuuu','$5$rounds=535000$HWWbzxc9JqgMKuQs$SARV56FPneglYz9YvGMQRgR6UcVUUD25sW.nw/zQAS7'),(50,'tttt','tttt','tttt','$5$rounds=535000$2X5TJ4Ug56zIqDma$XaWlKw210po2kbNocrOy9KYC7YMdvfTrfdXanwt0GG6'),(51,'eeee','eeee','eeee','$5$rounds=535000$cQ.6kPZYgxAtFabh$AnaaAYZLsOBdCvx5cKmGwnp5cp2GTCTFz9gvNwae6v1'),(52,'ffff','ffff','ffff','$5$rounds=535000$QJhJTXMHE/2BrQJN$lKFBX.manC4gxZe9LMq3mOt/VbcBpneKGDmEFF3p937'),(53,'hhhh','hhhh','hhhh','$5$rounds=535000$ycLip3yohz8HWAEU$AL6U8Jv54LzHyO0jlOfvyZ8SonTzA7tCvqpLOps66ZC'),(54,'-1','-1','-1','-1'),(55,'gggg','gggg','gggg','$5$rounds=535000$o5ZlCh.rHYdZR5Jl$AgkF.wGASJA/5/QI.Zl93iH0855q0zmQyXdRLxw2zsC'),(56,'-1','-1','-1','-1'),(57,'iiii','iiii','iiii','$5$rounds=535000$izNDMFoTVNmtELIh$3OPnm.ij8atZyMTfQ0A913RWQYHVvif9oZCZC2.KAq1'),(58,'-1','-1','-1','-1'),(59,'xyxy','xyxy','xyxy','$5$rounds=535000$Dmg9YeVGshP7AhMZ$Yo56vwGfUu7F2Abis1FDN23yguaJKlv.XioNH3.Xq.8'),(60,'pqpq','ppqq','pqpq','$5$rounds=535000$WiP/u.xV2XQeOEUa$gGsfB1lCvOXoh5hoZb5m4zkgRBV9JE65qqr.Dauw/a1'),(61,'bhavna','bhavna123','bhavna','$5$rounds=535000$wIV5UepFj4aim63x$6qSwoVD.cRos2YsvVJ6aCFPOXi8zl1oe7XDhnhkE2D5');
/*!40000 ALTER TABLE `userInfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `username` varchar(30) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `register_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `pref1` varchar(50) DEFAULT NULL,
  `pref2` varchar(50) DEFAULT NULL,
  `pref3` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'pulkit','pulkit@fff','pulkit123','$5$rounds=535000$U.leTOvgWWmis9YS$8KAaZhn2RhQdsxX652Ua0bgUphhhK1.Q7I4.qKuCW98','2018-04-05 13:36:20',NULL,NULL,NULL),(2,'neel123','nnnn','neel1998','$5$rounds=535000$W6kVzGvfnPK9HFKd$AfPDgkNkRWGVuECgWx9cbxfE6G57VLiLbJ1.V4.8DF1','2018-04-05 13:37:57',NULL,NULL,NULL),(3,'neel123','nnnn','neel98','$5$rounds=535000$HdRZKheBHegpxMaF$VcF9Y.nbSFA6r1qU3Bk17f9biChWKVHtic/5uGI7393','2018-04-05 13:39:23',NULL,NULL,NULL),(4,'manan','manan','mannnnnaannn','$5$rounds=535000$rujqgbLNwYrMPS81$tOfdaAkM0hSixlWyZClh7CxZMwrSEqQsJmQHMAomZV/','2018-04-05 14:16:12',NULL,NULL,NULL),(5,'neel_1998','nnnnnn','anant99','$5$rounds=535000$.45jt7Y1WJq8Icbz$93B.pheJyCVQj7DVYLa4Q0G6tCky/b0p547XGRm6ne0','2018-04-05 14:25:48',NULL,NULL,NULL),(6,'darth','nnnnn','darth_vader','$5$rounds=535000$jsTyPS67nXv.FZCN$sp9vwjTRSTco/Rehfja559EwBPi2KOI92.6HY6fiF50','2018-04-05 15:42:14',NULL,NULL,NULL),(7,'neel_1998','nnnnn','nnn111','$5$rounds=535000$RX5ZfXoEYy8vHcgX$PhlOTnhjEPZGZo1TY2K.RurGcVQKmljnGJwUMe4eLiD','2018-04-05 16:15:20',NULL,NULL,NULL),(8,'piiii','puipui','pui123','$5$rounds=535000$tel83oxYDgEtqNvt$mgSa/pJbqmHTuOMUUIdnaBEjRfCuG1BVEIZLW09j24.','2018-04-05 16:16:45',NULL,NULL,NULL),(9,'neel_1998','1111','11111','$5$rounds=535000$aVY48HEMADkpQ8JJ$XZ2gS.kBYhcUJryy6CUdmIfosFIUMeIzGEcVFnjJty0','2018-04-05 16:19:59',NULL,NULL,NULL),(10,'jay','jay@','jay11','$5$rounds=535000$HY3I1mJnh.kCqUMx$pTI41MNeM6Vvdsfi0tGqigWo1wbC.82uyh05xyFfwt5','2018-04-05 16:26:04',NULL,NULL,NULL),(11,'neel_1998','11111','neelll','$5$rounds=535000$F7DXQERZz2d0hkgD$.KbC35nEFVB5gyrm3nAgtZVEbrBZVJ0SPlJjicEfAU8','2018-04-05 16:44:01',NULL,NULL,NULL),(12,'abcd','abcd','abcd','$5$rounds=535000$q9qz8AWmDRkjGK8H$IUFBVGMCD2SdEVGcpkQiyuZQLNrSidOJdMaKKev3Yg9','2018-04-05 16:51:02',NULL,NULL,NULL),(13,'aaa','aaaa','aaaa','$5$rounds=535000$DUyIW9vrYbDqg1JE$g8Wi9eTFhN4RCKb9S/Y2czLa//FzgQg23yfXn8ym7p.','2018-04-05 16:51:59',NULL,NULL,NULL),(14,'bbbbb','bbbbb','bbbb','$5$rounds=535000$/WFSPgE4Dru12Pam$B6JVOPxdOn6sqEwAZ75cFJkoHmooat0.ka0q4Vc7t0/','2018-04-05 16:55:24',NULL,NULL,NULL),(15,'bbbbb','bbbbb','bbbb11','$5$rounds=535000$L/SPwQkiXYmGROcN$UWTCB7XlADcagnS4FMGAt9DA2Dony4zyzTFxwriBVs5','2018-04-05 16:56:56',NULL,NULL,NULL),(16,'11111','11111','puipui','$5$rounds=535000$xoVwSuU4/fzhWmVP$kONPngy7K/jwqNLbN1jJTV3ipRwnufOKNGraUjWeN4D','2018-04-05 17:02:05',NULL,NULL,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-04-10 14:44:04
