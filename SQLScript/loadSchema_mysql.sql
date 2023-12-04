-- MySQL dump 10.13  Distrib 8.1.0, for macos13 (arm64)
--
-- Host: localhost    Database: MeetMinder
-- ------------------------------------------------------
-- Server version	8.1.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `MeetMinder`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `MeetMinder` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `MeetMinder`;

--
-- Table structure for table `agenda`
--

DROP TABLE IF EXISTS `agenda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `agenda` (
  `agendaid` int NOT NULL AUTO_INCREMENT,
  `topic` text NOT NULL,
  `duration` int DEFAULT NULL,
  `meetingid` int NOT NULL,
  PRIMARY KEY (`agendaid`),
  KEY `meetingid` (`meetingid`),
  CONSTRAINT `agenda_ibfk_1` FOREIGN KEY (`meetingid`) REFERENCES `meeting` (`meetingid`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `agenda`
--

LOCK TABLES `agenda` WRITE;
/*!40000 ALTER TABLE `agenda` DISABLE KEYS */;
INSERT INTO `agenda` VALUES (1,'Introduction',30,7),(2,'Discussion on Project A',45,14),(3,'Coffee Break',15,2),(4,'Team Building Activity',60,18),(5,'Report on Sales Performance',20,11),(6,'Lunch Break',45,5),(7,'Review of Marketing Strategy',40,16),(8,'Q&A Session',30,20),(9,'Technical Workshop',50,13),(10,'Networking Break',15,8),(11,'Update on Research and Development',25,4),(12,'Project B Presentation',35,10),(13,'Customer Feedback Analysis',30,1),(14,'Team Collaboration Exercise',55,19),(15,'Closing Remarks',15,12),(16,'New Product Launch Discussion',40,6),(17,'Employee Recognition Ceremony',30,9),(18,'Financial Report Presentation',25,17),(19,'Breakout Sessions',50,3),(20,'Future Plans and Goals',35,15);
/*!40000 ALTER TABLE `agenda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `attendee`
--

DROP TABLE IF EXISTS `attendee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attendee` (
  `attendeeid` int NOT NULL AUTO_INCREMENT,
  `userid` int NOT NULL,
  `meetingid` int NOT NULL,
  `status` text NOT NULL,
  PRIMARY KEY (`attendeeid`),
  KEY `userid` (`userid`),
  KEY `meetingid` (`meetingid`),
  CONSTRAINT `attendee_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `user` (`userid`),
  CONSTRAINT `attendee_ibfk_2` FOREIGN KEY (`meetingid`) REFERENCES `meeting` (`meetingid`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attendee`
--

LOCK TABLES `attendee` WRITE;
/*!40000 ALTER TABLE `attendee` DISABLE KEYS */;
INSERT INTO `attendee` VALUES (1,4,10,'Attending'),(2,7,5,'Not Attending'),(3,12,18,'Maybe Attending'),(4,3,1,'Attending'),(5,19,14,'Not Attending'),(6,6,8,'Maybe Attending'),(7,14,3,'Attending'),(8,2,17,'Not Attending'),(9,8,11,'Maybe Attending'),(10,11,6,'Attending'),(11,1,15,'Not Attending'),(12,16,2,'Maybe Attending'),(13,13,7,'Attending'),(14,20,12,'Not Attending'),(15,5,9,'Maybe Attending'),(16,10,16,'Attending'),(17,9,4,'Not Attending'),(18,17,20,'Maybe Attending'),(19,18,13,'Attending'),(20,15,19,'Not Attending');
/*!40000 ALTER TABLE `attendee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `meeting`
--

DROP TABLE IF EXISTS `meeting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `meeting` (
  `meetingid` int NOT NULL AUTO_INCREMENT,
  `title` text NOT NULL,
  `description` text,
  `time` date NOT NULL,
  `location` text NOT NULL,
  `organizerid` int NOT NULL,
  PRIMARY KEY (`meetingid`),
  KEY `organizerid` (`organizerid`),
  CONSTRAINT `meeting_ibfk_1` FOREIGN KEY (`organizerid`) REFERENCES `user` (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meeting`
--

LOCK TABLES `meeting` WRITE;
/*!40000 ALTER TABLE `meeting` DISABLE KEYS */;
INSERT INTO `meeting` VALUES (1,'Team Sync','Discussing upcoming projects','2023-11-08','Aurora Tower',15),(2,'Project Kickoff','Introduction to new project','2023-11-09','Sapphire Plaza',8),(3,'Innovation Workshop','Brainstorming new ideas','2023-11-10','Emerald Heights',3),(4,'Status Update','Reviewing current progress','2023-11-11','Ruby Mansion',17),(5,'Planning Session','Strategizing for the future','2023-11-12','Topaz Tower',10),(6,'Creative Meeting','Exploring creative solutions','2023-11-13','Diamond Plaza',4),(7,'Collaboration Summit','Fostering team collaboration','2023-11-14','Opal House',20),(8,'Executive Briefing','Updates from the executive team','2023-11-15','Amethyst Hall',11),(9,'Product Launch','Introducing a new product','2023-11-16','Sapphire Tower',7),(10,'Strategic Planning','Long-term planning discussion','2023-11-17','Crystal Mansion',19),(11,'Tech Innovation','Exploring new technologies','2023-11-18','Emerald Tower',12),(12,'Marketing Campaign','Planning upcoming marketing campaigns','2023-11-19','Topaz Mansion',2),(13,'Customer Feedback','Gathering feedback from customers','2023-11-20','Diamond Heights',16),(14,'Team Building','Building a stronger team','2023-11-21','Ruby Tower',9),(15,'Product Demo','Demo of a new product','2023-11-22','Opal Tower',1),(16,'Agile Sprint Review','Reviewing progress in the agile sprint','2023-11-23','Amber Plaza',18),(17,'Investor Meeting','Meeting with potential investors','2023-11-24','Crystal Tower',14),(18,'Training Session','Employee training on new tools','2023-11-25','Sapphire Heights',6),(19,'Team Retrospective','Reflecting on team performance','2023-11-26','Emerald Mansion',13),(20,'Closing Ceremony','Celebrating project completion','2023-11-27','Topaz Heights',5);
/*!40000 ALTER TABLE `meeting` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `meetingresource`
--

DROP TABLE IF EXISTS `meetingresource`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `meetingresource` (
  `meetingresourceid` int NOT NULL AUTO_INCREMENT,
  `meetingid` int DEFAULT NULL,
  `resourceid` int DEFAULT NULL,
  PRIMARY KEY (`meetingresourceid`),
  KEY `meetingid` (`meetingid`),
  KEY `resourceid` (`resourceid`),
  CONSTRAINT `meetingresource_ibfk_1` FOREIGN KEY (`meetingid`) REFERENCES `meeting` (`meetingid`),
  CONSTRAINT `meetingresource_ibfk_2` FOREIGN KEY (`resourceid`) REFERENCES `resource` (`resourceid`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meetingresource`
--

LOCK TABLES `meetingresource` WRITE;
/*!40000 ALTER TABLE `meetingresource` DISABLE KEYS */;
INSERT INTO `meetingresource` VALUES (1,1,1),(2,2,5),(3,3,10),(4,4,15),(5,5,2),(6,6,8),(7,7,12),(8,8,18),(9,9,3),(10,10,20),(11,11,6),(12,12,14),(13,13,7),(14,14,9),(15,15,16),(16,16,11),(17,17,13),(18,18,4),(19,19,19),(20,20,17);
/*!40000 ALTER TABLE `meetingresource` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notification`
--

DROP TABLE IF EXISTS `notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notification` (
  `notificationid` int NOT NULL AUTO_INCREMENT,
  `userid` int NOT NULL,
  `message` text,
  `timestamp` date NOT NULL,
  PRIMARY KEY (`notificationid`),
  KEY `userid` (`userid`),
  CONSTRAINT `notification_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `user` (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notification`
--

LOCK TABLES `notification` WRITE;
/*!40000 ALTER TABLE `notification` DISABLE KEYS */;
INSERT INTO `notification` VALUES (1,5,'You have a new message.','2023-11-08'),(2,12,'Reminder: Team Meeting tomorrow.','2023-11-09'),(3,3,'Congratulations! You reached a milestone.','2023-11-10'),(4,18,'Important update: Policy changes.','2023-11-11'),(5,8,'New task assigned to you.','2023-11-12'),(6,16,'Upcoming deadline: Project submission.','2023-11-13'),(7,7,'Feedback requested for recent project.','2023-11-14'),(8,1,'Announcement: Company-wide Town Hall.','2023-11-15'),(9,10,'Happy Birthday! 🎉','2023-11-16'),(10,14,'Training session scheduled for next week.','2023-11-17'),(11,20,'Emergency meeting called, please attend.','2023-11-18'),(12,9,'New job opportunity available.','2023-11-19'),(13,6,'Reminder: Complete your annual review.','2023-11-20'),(14,11,'Update on IT system maintenance.','2023-11-21'),(15,2,'Welcome to the team!','2023-11-22'),(16,19,'Survey: Share your feedback on company culture.','2023-11-23'),(17,4,'Holiday schedule for next month.','2023-11-24'),(18,15,'Training program registration open.','2023-11-25'),(19,17,'Notice: Office will be closed on Friday.','2023-11-26'),(20,13,'Reminder: Complete cybersecurity training.','2023-11-27');
/*!40000 ALTER TABLE `notification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resource`
--

DROP TABLE IF EXISTS `resource`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `resource` (
  `resourceid` int NOT NULL AUTO_INCREMENT,
  `resourcename` text NOT NULL,
  `description` text,
  PRIMARY KEY (`resourceid`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resource`
--

LOCK TABLES `resource` WRITE;
/*!40000 ALTER TABLE `resource` DISABLE KEYS */;
INSERT INTO `resource` VALUES (1,'resource1','Description for resource 1'),(2,'resource2','Description for resource 2'),(3,'resource3','Description for resource 3'),(4,'resource4','Description for resource 4'),(5,'resource5','Description for resource 5'),(6,'resource6','Description for resource 6'),(7,'resource7','Description for resource 7'),(8,'resource8','Description for resource 8'),(9,'resource9','Description for resource 9'),(10,'resource10','Description for resource 10'),(11,'resource11','Description for resource 11'),(12,'resource12','Description for resource 12'),(13,'resource13','Description for resource 13'),(14,'resource14','Description for resource 14'),(15,'resource15','Description for resource 15'),(16,'resource16','Description for resource 16'),(17,'resource17','Description for resource 17'),(18,'resource18','Description for resource 18'),(19,'resource19','Description for resource 19'),(20,'resource20','Description for resource 20');
/*!40000 ALTER TABLE `resource` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `room`
--

DROP TABLE IF EXISTS `room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `room` (
  `roomid` int NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `capacity` int NOT NULL,
  `resourceid` int NOT NULL,
  PRIMARY KEY (`roomid`),
  KEY `resourceid` (`resourceid`),
  CONSTRAINT `room_ibfk_1` FOREIGN KEY (`resourceid`) REFERENCES `resource` (`resourceid`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `room`
--

LOCK TABLES `room` WRITE;
/*!40000 ALTER TABLE `room` DISABLE KEYS */;
INSERT INTO `room` VALUES (1,'Room1',10,5),(2,'Room2',15,12),(3,'Room3',20,8),(4,'Room4',25,3),(5,'Room5',30,17),(6,'Room6',12,10),(7,'Room7',18,6),(8,'Room8',22,1),(9,'Room9',28,14),(10,'Room10',35,19),(11,'Room11',14,4),(12,'Room12',19,11),(13,'Room13',24,7),(14,'Room14',29,15),(15,'Room15',16,2),(16,'Room16',21,18),(17,'Room17',26,9),(18,'Room18',31,13),(19,'Room19',23,16),(20,'Room20',27,20);
/*!40000 ALTER TABLE `room` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `userid` int NOT NULL AUTO_INCREMENT,
  `username` text NOT NULL,
  `email` text NOT NULL,
  `password` text NOT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'user1','user1@example.com','password1'),(2,'user2','user2@example.com','password2'),(3,'user3','user3@example.com','password3'),(4,'user4','user4@example.com','password4'),(5,'user5','user5@example.com','password5'),(6,'user6','user6@example.com','password6'),(7,'user7','user7@example.com','password7'),(8,'user8','user8@example.com','password8'),(9,'user9','user9@example.com','password9'),(10,'user10','user10@example.com','password10'),(11,'user11','user11@example.com','password11'),(12,'user12','user12@example.com','password12'),(13,'user13','user13@example.com','password13'),(14,'user14','user14@example.com','password14'),(15,'user15','user15@example.com','password15'),(16,'user16','user16@example.com','password16'),(17,'user17','user17@example.com','password17'),(18,'user18','user18@example.com','password18'),(19,'user19','user19@example.com','password19'),(20,'user20','user20@example.com','password20');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-08 22:52:14
