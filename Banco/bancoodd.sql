CREATE DATABASE  IF NOT EXISTS `dadosodds` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `dadosodds`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: dadosodds
-- ------------------------------------------------------
-- Server version	8.0.37

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `jogos`
--

DROP TABLE IF EXISTS `jogos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jogos` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `casa` varchar(255) NOT NULL,
  `resultado` varchar(50) DEFAULT NULL,
  `fora` varchar(255) NOT NULL,
  `time_favorito` varchar(255) DEFAULT NULL,
  `pais_favorito` varchar(255) DEFAULT NULL,
  `odd_favorito` decimal(5,2) DEFAULT NULL,
  `time_normal` varchar(255) DEFAULT NULL,
  `pais_normal` varchar(255) DEFAULT NULL,
  `odd_normal` decimal(5,2) DEFAULT NULL,
  `diferenca_odd` decimal(5,2) DEFAULT NULL,
  `vitoria` varchar(50) DEFAULT NULL,
  `url_resultado` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jogos`
--

LOCK TABLES `jogos` WRITE;
/*!40000 ALTER TABLE `jogos` DISABLE KEYS */;
INSERT INTO `jogos` VALUES (3,'Sportivo Ameliano',NULL,'Tacuary Assunção','Sportivo Ameliano',NULL,1.87,'Tacuary Assunção',NULL,3.50,1.63,NULL,'https://www.sofascore.com/sportivo-ameliano-tacuary/ZucskvEc#id:11903801'),(5,'Coquimbo Unido',NULL,'CD Palestino','Coquimbo Unido',NULL,2.15,'CD Palestino',NULL,3.10,0.95,NULL,'https://www.sofascore.com/coquimbo-unido-palestino/hnbspnb#id:11987243'),(6,'Talleres',NULL,'Colón','Talleres',NULL,1.78,'Colón',NULL,3.90,2.12,NULL,'https://www.sofascore.com/talleres-colon/hobskob#id:10341636'),(7,'SSD Citta Di Campobasso',NULL,'Cavese 1919','SSD Citta Di Campobasso',NULL,2.10,'Cavese 1919',NULL,2.87,0.77,NULL,'https://www.sofascore.com/talleres-colon/hobskob#id:10981412'),(8,'Trapani',NULL,'Calcio Caldiero Terme','Trapani',NULL,1.39,'Calcio Caldiero Terme',NULL,5.25,3.86,NULL,'https://www.sofascore.com/caldiero-terme-trapani/LyrsMQFc#id:12357035'),(9,'Sportivo Dock Sud Reservas',NULL,'CA Ferrocarril Midland Reserves','CA Ferrocarril Midland Reserves',NULL,1.82,'Sportivo Dock Sud Reservas',NULL,3.50,1.68,NULL,'https://www.sofascore.com/talleres-colon/hobskob#id:10981412'),(11,'Canuelas FC Reservas',NULL,'UAI Urquiza Reservas','Canuelas FC Reservas',NULL,1.66,'UAI Urquiza Reservas',NULL,3.90,2.24,NULL,'https://www.sofascore.com/talleres-colon/hobskob#id:10981412'),(12,'Central Ballester Reservas',NULL,'Centro Espanol Reservas','Centro Espanol Reservas',NULL,2.25,'Central Ballester Reservas',NULL,2.37,0.12,NULL,'https://www.sofascore.com/centro-espanyol-reserves-central-ballester-reserves/TrgestUhe#id:12397820'),(13,'General Lamadrid Reservas',NULL,'Juventud Unida San Miguel Reservas','General Lamadrid Reservas',NULL,2.25,'Juventud Unida San Miguel Reservas',NULL,2.65,0.40,NULL,'https://www.sofascore.com/juventud-unida-san-miguel-reserves-general-lamadrid-reserve/vagdsKTge#id:12397826'),(14,'Real Pilar FC Reservas',NULL,'CA Lugano Reservas','Real Pilar FC Reservas',NULL,1.60,'CA Lugano Reservas',NULL,4.40,2.80,NULL,'https://www.sofascore.com/talleres-colon/hobskob#id:10981412'),(15,'Victoriano Arenas Reservas',NULL,'Club Defensores De Cambaceres Reservas','Victoriano Arenas Reservas',NULL,2.40,'Club Defensores De Cambaceres Reservas',NULL,2.75,0.35,NULL,'https://www.sofascore.com/talleres-colon/hobskob#id:10981412'),(16,'Argentino De Rosario Reservas',NULL,'Justo Jose de Urquiza Reserves','Argentino De Rosario Reservas',NULL,1.57,'Justo Jose de Urquiza Reserves',NULL,4.80,3.23,NULL,'https://www.sofascore.com/argentino-de-rosario-reserves-justo-jose-de-urquiza-reserve/rYtcsuTge#id:12397983'),(17,'Deportivo Espanol Reserves',NULL,'CA Claypole Reservas','Deportivo Espanol Reserves',NULL,2.10,'CA Claypole Reservas',NULL,2.85,0.75,NULL,'https://www.sofascore.com/ca-claypole-reserves-deportivo-espanol-reserve/DYgcsziFd#id:12397984'),(19,'CA San Miguel Reservas',NULL,'Ferro Carril Oeste Reserves','CA San Miguel Reservas',NULL,2.10,'Ferro Carril Oeste Reserves',NULL,2.85,0.75,NULL,'https://www.sofascore.com/talleres-colon/hobskob#id:10981412'),(21,'CSD Tristan Suarez Reservas',NULL,'Deportivo Moron Reservas','CSD Tristan Suarez Reservas',NULL,2.20,'Deportivo Moron Reservas',NULL,2.95,0.75,NULL,'https://www.sofascore.com/talleres-colon/hobskob#id:10981412'),(22,'Finlândia Sub-21',NULL,'Estônia Sub-21','Estônia Sub-21',NULL,1.47,'Finlândia Sub-21',NULL,5.25,3.78,NULL,'https://www.sofascore.com/talleres-colon/hobskob#id:10981412'),(23,'Letônia Sub-21',NULL,'Lituânia Sub-21','Letônia Sub-21',NULL,1.98,'Lituânia Sub-21',NULL,2.95,0.97,NULL,'https://www.sofascore.com/talleres-colon/hobskob#id:10981412'),(24,'Geórgia Sub-21',NULL,'Cazaquistão Sub-21','Geórgia Sub-21',NULL,1.52,'Cazaquistão Sub-21',NULL,5.00,3.48,NULL,'https://www.sofascore.com/talleres-colon/hobskob#id:10981412'),(25,'Dinamarca Sub-21',NULL,'Noruega Sub-21','Dinamarca Sub-21',NULL,2.20,'Noruega Sub-21',NULL,2.55,0.35,NULL,'https://www.sofascore.com/talleres-colon/hobskob#id:10981412'),(26,'Itália Base',NULL,'Ucrânia Base','Ucrânia Base',NULL,2.10,'Itália Base',NULL,2.85,0.75,NULL,NULL),(27,'Sola FK',NULL,'Madla IL','Sola FK',NULL,1.40,'Madla IL',NULL,5.25,3.85,NULL,'https://www.sofascore.com/madla-sola/FZcsuGCb#id:12012945'),(28,'IF Brommapojkarna',NULL,'KIF Orebro DFF','KIF Orebro DFF',NULL,1.88,'IF Brommapojkarna',NULL,3.50,1.62,NULL,'https://www.sofascore.com/if-brommapojkarna-kif-orebro-dff/PXcsXdV#id:11921999'),(29,'Torslanda IK',NULL,'Ljungskile SK','Torslanda IK',NULL,2.05,'Ljungskile SK',NULL,2.95,0.90,NULL,'https://www.sofascore.com/ljungskile-sk-torslanda-ik/PKszL#id:11988783'),(30,'Motala AIF FK',NULL,'IFK Kumla','Motala AIF FK',NULL,2.10,'IFK Kumla',NULL,2.55,0.45,NULL,'https://www.sofascore.com/ifk-kumla-fk-motala-aif-fk/JKsMVi#id:12048138'),(31,'Bergnasets AIK',NULL,'IFK Ostersund','IFK Ostersund',NULL,2.30,'Bergnasets AIK',NULL,2.45,0.15,NULL,'https://www.sofascore.com/bergnasets-aik-ifk-ostersund/RViswtAb#id:12021154'),(32,'Hassleholms IF',NULL,'Osterlen FF','Hassleholms IF',NULL,1.32,'Osterlen FF',NULL,7.25,5.93,NULL,'https://www.sofascore.com/osterlen-ff-hassleholms-if/zVisLjBb#id:12023664'),(33,'Malaui',NULL,'São Tomé e Príncipe','Malaui',NULL,1.16,'São Tomé e Príncipe',NULL,17.00,15.84,NULL,'https://www.sofascore.com/sao-tome-and-principe-malawi/TkdsnBn#id:12183338'),(34,'Guiné-Bissau',NULL,'Etiópia','Guiné-Bissau',NULL,1.57,'Etiópia',NULL,6.75,5.18,NULL,'https://www.sofascore.com/guinea-bissau-ethiopia/LkdsDuj#id:12183526'),(35,'Líbia',NULL,'Maurícias','Líbia',NULL,1.25,'Maurícias',NULL,11.00,9.75,NULL,'https://www.sofascore.com/mauritius-libya/AVbsFVb#id:12183446'),(36,'Mauritânia',NULL,'Sudão','Mauritânia',NULL,1.75,'Sudão',NULL,4.75,3.00,NULL,'https://www.sofascore.com/mauritania-sudan/JUbsEVb#id:12183491'),(37,'República do Congo',NULL,'Níger','República do Congo',NULL,1.75,'Níger',NULL,5.25,3.50,NULL,'https://www.sofascore.com/congo-republic-niger/GkdsPkd#id:12183392'),(38,'Egito',NULL,'Burkina Faso','Egito',NULL,1.46,'Burkina Faso',NULL,6.75,5.29,NULL,'https://www.sofascore.com/egypt-burkina-faso/ZUbsiVb#id:12183516'),(39,'Senegal',NULL,'RD Congo','Senegal',NULL,1.47,'RD Congo',NULL,6.75,5.28,NULL,'https://www.sofascore.com/dr-congo-senegal/OUbsyWb#id:12183493'),(40,'Benin',NULL,'Ruanda','Benin',NULL,2.05,'Ruanda',NULL,3.75,1.70,NULL,'https://www.sofascore.com/rwanda-benin/UUbsMkd#id:12183457'),(41,'Mali',NULL,'Gana','Mali',NULL,1.98,'Gana',NULL,3.80,1.82,NULL,'https://www.sofascore.com/mali-ghana/oVbsGWb#id:12183326'),(42,'Argélia',NULL,'Guiné','Argélia',NULL,1.55,'Guiné',NULL,5.75,4.20,NULL,'https://www.sofascore.com/guinea-algeria/QTbsBWb#id:12183353'),(43,'Iraque',NULL,'Indonésia','Indonésia',NULL,2.20,'Iraque',NULL,3.30,1.10,NULL,'https://www.sofascore.com/indonesia-iraq/rVbsEWb#id:11763625'),(44,'Austrália',NULL,'Bangladesh','Bangladesh',NULL,1.02,'Austrália',NULL,71.00,69.99,NULL,'https://www.sofascore.com/bangladesh-australia/QUbsFwc#id:11763586'),(45,'Omã',NULL,'Taiwan','Taiwan',NULL,1.09,'Omã',NULL,23.00,21.91,NULL,'https://www.sofascore.com/chinese-taipei-oman/MVbsMtc#id:11763643'),(46,'Vietnã',NULL,'Ilhas Filipinas','Vietnã',NULL,1.37,'Ilhas Filipinas',NULL,8.00,6.63,NULL,'https://www.sofascore.com/vietnam-philippines/QVbsaQc#id:11740247'),(47,'China',NULL,'Tailândia','China',NULL,1.88,'Tailândia',NULL,4.00,2.12,NULL,'https://www.sofascore.com/china-thailand/FUbsfVb#id:11740244'),(48,'Irã',NULL,'Hong Kong','Hong Kong',NULL,1.07,'Irã',NULL,31.00,29.93,NULL,'https://www.sofascore.com/iran-hong-kong/pVbsqVb#id:11763640'),(49,'Coreia do Sul',NULL,'Singapura','Singapura',NULL,1.02,'Coreia do Sul',NULL,81.00,79.99,NULL,NULL),(50,'Japão',NULL,'Myanmar','Myanmar',NULL,1.00,'Japão',NULL,101.00,100.00,NULL,'https://www.sofascore.com/myanmar-japan/vVbsJuj#id:11761478'),(51,'Síria',NULL,'Coreia do Norte','Coreia do Norte',NULL,2.15,'Síria',NULL,3.40,1.25,NULL,'https://www.sofascore.com/north-korea-syria/GUbsuhc#id:11740243'),(52,'Kuwait',NULL,'Índia','Índia',NULL,2.37,'Kuwait',NULL,3.00,0.63,NULL,NULL),(53,'Uzbequistão',NULL,'Turquemenistão','Uzbequistão',NULL,1.12,'Turquemenistão',NULL,17.50,16.38,NULL,NULL),(54,'Quirguistão',NULL,'Malásia','Quirguistão',NULL,1.87,'Malásia',NULL,4.00,2.13,NULL,NULL),(55,'Arábia Saudita',NULL,'Paquistão','Paquistão',NULL,1.03,'Arábia Saudita',NULL,61.00,59.98,NULL,NULL),(57,'Emirados Árabes Unidos',NULL,'Nepal','Nepal',NULL,1.01,'Emirados Árabes Unidos',NULL,81.00,79.99,NULL,NULL),(58,'Catar',NULL,'Afeganistão','Afeganistão',NULL,1.12,'Catar',NULL,18.00,16.88,NULL,NULL),(59,'Jordânia',NULL,'Tajiquistão','Jordânia',NULL,1.52,'Tajiquistão',NULL,5.75,4.23,NULL,NULL),(60,'Bahrain',NULL,'Iémen','Bahrain',NULL,1.13,'Iémen',NULL,23.00,21.87,NULL,NULL),(61,'MKS Swit Nowy Dwor Mazowiecki',NULL,'Victoria Sulejowek','Victoria Sulejowek',NULL,2.05,'MKS Swit Nowy Dwor Mazowiecki',NULL,2.87,0.82,NULL,NULL),(62,'MP Mikkelin II',NULL,'Kultsu FC','Kultsu FC',NULL,2.10,'MP Mikkelin II',NULL,2.60,0.50,NULL,NULL),(63,'San Antonio FC ECU',NULL,'Chacaritas','San Antonio FC ECU',NULL,2.00,'Chacaritas',NULL,3.40,1.40,NULL,NULL),(64,'MC Alger Sub-21',NULL,'CR Belouizdad Sub-21','MC Alger Sub-21',NULL,1.75,'CR Belouizdad Sub-21',NULL,3.60,1.85,NULL,NULL),(65,'Atlético Huila',NULL,'Orsomarso SC','Orsomarso SC',NULL,2.40,'Atlético Huila',NULL,2.75,0.35,NULL,NULL),(66,'CD Real Cartagena FC',NULL,'Tigres FC','Tigres FC',NULL,2.15,'CD Real Cartagena FC',NULL,2.95,0.80,NULL,NULL),(67,'CS Cerrito',NULL,'Sud America','CS Cerrito',NULL,2.05,'Sud America',NULL,3.10,1.05,NULL,NULL);
/*!40000 ALTER TABLE `jogos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-06 19:21:11
