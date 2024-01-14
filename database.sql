/*
SQLyog Community v13.2.0 (64 bit)
MySQL - 8.2.0 : Database - lode_com
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add Token',7,'add_token'),
(26,'Can change Token',7,'change_token'),
(27,'Can delete Token',7,'delete_token'),
(28,'Can view Token',7,'view_token'),
(29,'Can add token',8,'add_tokenproxy'),
(30,'Can change token',8,'change_tokenproxy'),
(31,'Can delete token',8,'delete_tokenproxy'),
(32,'Can view token',8,'view_tokenproxy'),
(33,'Can add blacklisted token',9,'add_blacklistedtoken'),
(34,'Can change blacklisted token',9,'change_blacklistedtoken'),
(35,'Can delete blacklisted token',9,'delete_blacklistedtoken'),
(36,'Can view blacklisted token',9,'view_blacklistedtoken'),
(37,'Can add outstanding token',10,'add_outstandingtoken'),
(38,'Can change outstanding token',10,'change_outstandingtoken'),
(39,'Can delete outstanding token',10,'delete_outstandingtoken'),
(40,'Can view outstanding token',10,'view_outstandingtoken'),
(41,'Can add city',11,'add_city'),
(42,'Can change city',11,'change_city'),
(43,'Can delete city',11,'delete_city'),
(44,'Can view city',11,'view_city'),
(45,'Can add game',12,'add_game'),
(46,'Can change game',12,'change_game'),
(47,'Can delete game',12,'delete_game'),
(48,'Can view game',12,'view_game'),
(49,'Can add subgame',13,'add_subgame'),
(50,'Can change subgame',13,'change_subgame'),
(51,'Can delete subgame',13,'delete_subgame'),
(52,'Can view subgame',13,'view_subgame'),
(53,'Can add rate',14,'add_rate'),
(54,'Can change rate',14,'change_rate'),
(55,'Can delete rate',14,'delete_rate'),
(56,'Can view rate',14,'view_rate');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values 
(1,'pbkdf2_sha256$720000$PmOTyNsl4EpyLnlnYAIOUf$AIYOgVuLu2/ivdcFuLytd/kNVbf9NTm85mN33BrZT/Q=','2024-01-14 15:31:03.981969',0,'n31997','Nam','Ngo Ngoc','chris.nn2522@gmail.com',0,1,'2024-01-10 17:47:37.805285'),
(2,'pbkdf2_sha256$720000$idrHORiZvuXpaWG721EIq5$XPlnrhF3Sp89pksQALABb9Qp8+bX+dw4UixxYlgx3/E=',NULL,1,'namngocngo22','','','namngocngo22@gmail.com',1,1,'2024-01-10 17:48:55.022455');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `authtoken_token` */

DROP TABLE IF EXISTS `authtoken_token`;

CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `authtoken_token` */

insert  into `authtoken_token`(`key`,`created`,`user_id`) values 
('c4fddc5b31fe5d0c12825d50a05a3c8494ad6ca9','2024-01-10 17:47:38.296093',1);

/*Table structure for table `cities` */

DROP TABLE IF EXISTS `cities`;

CREATE TABLE `cities` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL,
  `region` varchar(50) NOT NULL,
  `feature` int NOT NULL,
  `time_release` varchar(8) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `cities` */

insert  into `cities`(`id`,`name`,`date`,`region`,`feature`,`time_release`,`status`,`created_at`,`updated_at`) values 
(1,'Miền Bắc','','bac',0,'18:15:00',1,'2019-08-16 09:14:40.000000','2019-08-16 23:00:36.000000'),
(6,'Gia Lai','5','trung',0,'17:15:00',1,'2019-08-16 09:14:40.000000','2019-08-16 09:14:40.000000'),
(9,'Ninh Thuận','5','trung',0,'17:15:00',1,'2019-08-16 09:14:40.000000','2019-08-16 09:14:40.000000'),
(19,'Bình Dương','5','nam',0,'16:15:00',1,'2019-08-16 09:14:40.000000','2019-08-16 09:14:40.000000'),
(33,'Trà Vinh','5','nam',0,'16:15:00',1,'2019-08-16 09:14:40.000000','2019-08-16 09:14:40.000000'),
(34,'Vĩnh Long','5','nam',0,'16:15:00',1,'2019-08-16 09:14:40.000000','2019-08-16 09:14:40.000000');

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(7,'authtoken','token'),
(8,'authtoken','tokenproxy'),
(5,'contenttypes','contenttype'),
(11,'server','city'),
(12,'server','game'),
(14,'server','rate'),
(13,'server','subgame'),
(6,'sessions','session'),
(9,'token_blacklist','blacklistedtoken'),
(10,'token_blacklist','outstandingtoken');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2024-01-10 17:34:44.023915'),
(2,'auth','0001_initial','2024-01-10 17:34:44.485801'),
(3,'admin','0001_initial','2024-01-10 17:34:44.604806'),
(4,'admin','0002_logentry_remove_auto_add','2024-01-10 17:34:44.613781'),
(5,'admin','0003_logentry_add_action_flag_choices','2024-01-10 17:34:44.623755'),
(6,'contenttypes','0002_remove_content_type_name','2024-01-10 17:34:44.741133'),
(7,'auth','0002_alter_permission_name_max_length','2024-01-10 17:34:44.823490'),
(8,'auth','0003_alter_user_email_max_length','2024-01-10 17:34:44.844433'),
(9,'auth','0004_alter_user_username_opts','2024-01-10 17:34:44.850447'),
(10,'auth','0005_alter_user_last_login_null','2024-01-10 17:34:44.906784'),
(11,'auth','0006_require_contenttypes_0002','2024-01-10 17:34:44.909776'),
(12,'auth','0007_alter_validators_add_error_messages','2024-01-10 17:34:44.916757'),
(13,'auth','0008_alter_user_username_max_length','2024-01-10 17:34:44.978109'),
(14,'auth','0009_alter_user_last_name_max_length','2024-01-10 17:34:45.029972'),
(15,'auth','0010_alter_group_name_max_length','2024-01-10 17:34:45.047923'),
(16,'auth','0011_update_proxy_permissions','2024-01-10 17:34:45.057897'),
(17,'auth','0012_alter_user_first_name_max_length','2024-01-10 17:34:45.133213'),
(18,'authtoken','0001_initial','2024-01-10 17:34:45.209527'),
(19,'authtoken','0002_auto_20160226_1747','2024-01-10 17:34:45.232466'),
(20,'authtoken','0003_tokenproxy','2024-01-10 17:34:45.234461'),
(21,'sessions','0001_initial','2024-01-10 17:34:45.264426'),
(22,'server','0001_initial','2024-01-10 18:27:23.445124'),
(23,'token_blacklist','0001_initial','2024-01-10 18:27:23.630911'),
(24,'token_blacklist','0002_outstandingtoken_jti_hex','2024-01-10 18:27:23.650858'),
(25,'token_blacklist','0003_auto_20171017_2007','2024-01-10 18:27:23.661830'),
(26,'token_blacklist','0004_auto_20171017_2013','2024-01-10 18:27:23.717229'),
(27,'token_blacklist','0005_remove_outstandingtoken_jti','2024-01-10 18:27:23.770134'),
(28,'token_blacklist','0006_auto_20171017_2113','2024-01-10 18:27:23.788115'),
(29,'token_blacklist','0007_auto_20171017_2214','2024-01-10 18:27:24.003254'),
(30,'token_blacklist','0008_migrate_to_bigautofield','2024-01-10 18:27:24.191395'),
(31,'token_blacklist','0010_fix_migrate_to_bigautofield','2024-01-10 18:27:24.202395'),
(32,'token_blacklist','0011_linearizes_history','2024-01-10 18:27:24.204361'),
(33,'token_blacklist','0012_alter_outstandingtoken_user','2024-01-10 18:27:24.214569'),
(34,'server','0002_alter_city_created_at_alter_city_time_release_and_more','2024-01-11 16:19:53.137164'),
(35,'server','0003_game_subgame','2024-01-11 16:37:28.129518'),
(36,'server','0004_alter_subgame_multi','2024-01-11 16:38:49.896459'),
(37,'server','0005_game_region','2024-01-11 16:41:55.648484'),
(38,'server','0006_rate_alter_game_table_alter_subgame_table','2024-01-11 16:46:44.397843');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('0qs5kv8efz4tvidmduzwmoq3axwom9e5','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rOigL:MNzv3OtTo3o4nQWzDgaNEBJRC2ztL7TXeZ8VaBanXQI','2024-01-27 18:24:33.375164'),
('1qhugldt91m3294wllbsperzjogqdjso','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rOhn0:OXKd603v_PQSnAXOz67VlDcAXWgiUcO45Ag5jcmyjug','2024-01-27 17:27:22.009785'),
('3a3bh6lsvtnjkh5puvm5h58wl6n1n4zt','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rOill:wNfFhf7dUBI64knwyRWmwCjt6Ndppn4TyXSh6g9Osrk','2024-01-27 18:30:09.254700'),
('3ssj3g4z3whgd44olkiftj206mrmtihn','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rNz7f:fGejARpZdWb_7VP4H7AGgSA68WxvLLZH6xqpcNMHWyY','2024-01-25 17:45:43.738545'),
('49f8ydnxcrw65sxicyr5wad7djmddrsx','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rOict:wp5WV5rXHu2l8hOGmOPDUT9fyPLMy3WCkgWfd6F1TXw','2024-01-27 18:20:59.015259'),
('4xgpd93saabgeftfypn99fwki8f5vn8n','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rOixC:Q2LY6SJHnd55gy37ZNnEmS4wTbu_nUjXsF8zPlJ0UBY','2024-01-27 18:41:58.096331'),
('5qcvecgf9c2wjkw6li3w4ko3r45jre6u','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rOivs:N3qSgzTUAQxIqY4SPbid9JmiX0iMXNIar2iE4Nojs84','2024-01-27 18:40:36.071621'),
('9pn4rdzafvhlkj1s0vlzt9j40zvr134x','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rOaec:udUXX7DYjep54DBKHTk1nVxdsQyKJ1J9Zp_ytZGTMZ4','2024-01-27 09:50:14.184425'),
('9sbiohygy78rcou0u95wtk0kfd3fg2o8','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rOidm:RF-NhilxemqHq06FepGkoQAa2QU6EAWnz6HLUMxjFBM','2024-01-27 18:21:54.037869'),
('a6xq0o2ne5abmzwldovw8oz3dyitzoqe','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rOivc:VJKSFjuTJ6p1MNJ1zEWn1hVSIUjx47-Te-oNT24nrS0','2024-01-27 18:40:20.581922'),
('avlrr36lm1e9y6zznbqgt57hxz6aok1h','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rOivf:Ajezmmlh42jN4bNqw1zzsJhoHVzDpMRot_cq6V-MVJs','2024-01-27 18:40:23.491647'),
('bpc4t973g36sm4f14bjvak0lq9qeysu0','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rOicY:ABZhpleuX2XEV9KS8PvjbVchfrFU0AfVXG0abUmagVs','2024-01-27 18:20:38.648884'),
('byo4fgmgb8ptp9gldcrzc67w3jn3re0p','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rOirW:J0tQPXHGjHnGkRfN5eAVfq7Glizvro44jHNvAaULrbU','2024-01-27 18:36:06.012161'),
('d65a1dh4ur0rk2m6uanz7lb7mkwy9add','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rOis9:3BaIjqmTYgt6QdrPoLGGz9JF1LqkKH_owq57Sd7x7Y0','2024-01-27 18:36:45.576406'),
('d77ltpcwrys0x45006mt8t78mmpw9thj','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rOioT:LTJni4SlufEIJ0qPbAXHn1JgC_5L-gLlJtJupKjRD7M','2024-01-27 18:32:57.286451'),
('emy1atjmdq5mrko1jphkp5dqvijmskbz','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rP2S0:JrEr65l-WZ1OhVP2bFcaD2Vz-Gldz9Btni8mPMkDgBY','2024-01-28 15:31:04.285396'),
('exwfjbno6oppzhocel1h9f9bqczog21d','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rOigl:9N4if8uv86NUR1U-upE_UFIxbCDZugVSkNxRvNtZbGY','2024-01-27 18:24:59.208659'),
('h5ep9w6oc9wk8iwdj3uv2qfsnh4o7k9n','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rOixX:-1K1FFfx06PGUCvsIQW469yOE0pp2YIXz1A3z43DAEQ','2024-01-27 18:42:19.735297'),
('ka6k83pe260zq4rak5xj3g1w682xmolm','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rOicN:AQQ7GBRd0bhwYEggFzolh5Cfi05DjDgtLkmghrNOnhs','2024-01-27 18:20:27.135529'),
('lbjupf367a8qxtw7uvmhzvoe6e37spkc','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rOaJn:-jIhd8y0LitVROAucKQVr7G6fQCHrKvDsG-0JjLqPZQ','2024-01-27 09:28:43.252547'),
('meqec3m427tibhp3b0iy8pgvbb0zkqu3','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rOaVm:X4cuAJCXg8T_m4R4TodNBJ5wSfS1ngGObsGuurdIKi0','2024-01-27 09:41:06.435844'),
('npvz7hz0ke0l6n2nh6ak1foq841razr2','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rOaGw:2bGbPXE_IEQKh4MWOu_iu_QreujlCS8zkhU-5AB2EoY','2024-01-27 09:25:46.449825'),
('ps36sttxt37bcw4nws1du1s3vx1whjoo','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rOiqQ:K3iaS3rjqlyo2v55dr84jcm9GWqGCQyDsSjjlGo0Oq8','2024-01-27 18:34:58.820708'),
('pu5xh0yrt4ky70fc0griu7qz111uutzi','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rOir5:LUVSzm4YVRBcR8V-yJLpQAyn2JWR6wbkDe5pH_4oCKg','2024-01-27 18:35:39.932425'),
('s1nsys0sheukxg4c13v4tp36xxami8it','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rOfm6:BxXV-2rtN9EsZnqhUk8QkZ3qhPey2blbxlydE3hAeMU','2024-01-27 15:18:18.883850'),
('ugdtjh2kaqmhz42iyh2whox77482s95x','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rOiwu:uzlNuPHsr-pX8mHMcIqYowNX_WkXEvL8nG5hnhTtkhM','2024-01-27 18:41:40.401713'),
('ve0whw3kztria0f3ctvc8g674htawzw6','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rOixe:tjeB_AREI0Ex1xD_x-_H84TvP0w06CmKp8NWkQ7BFP0','2024-01-27 18:42:26.266313'),
('wwst9zyyzw66puz6dagrg2nr2fvliwa6','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rOitw:_BWBgK-GeqpmnRpHzT95rfZxYZwrUVfUbs68YFYXwHg','2024-01-27 18:38:36.275056'),
('x9wdqiemyook8i13uvli2sggizop44fs','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rOipO:mDnYJ91CJpH0TtpJnyNkmkExy7OUMRVccG6OnKd5lUY','2024-01-27 18:33:54.793972'),
('y0vbl16ufmf9uqcqn6cowe2rwdtwa2sy','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rOiy1:R4-DXUOuGZus57-C02K8xlqgCdkZFQzyADHKFM66xgw','2024-01-27 18:42:49.712681'),
('z2ore5a0f5jwygwj7y506o448vyjlkr6','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rOikz:7gSqlcLQe4_mviavCvMBjaoShe4TmvYTmEU1cO6H6jc','2024-01-27 18:29:21.873367'),
('zhzsw337aug1txk0hahemcxa422ua3na','.eJxVjMEOwiAQRP-FsyFdSunGo3e_gSzsIlUDSWlPjf9um_Sgt8m8N7MpT-uS_dpk9hOrqwJ1-e0CxZeUA_CTyqPqWMsyT0Efij5p0_fK8r6d7t9Bppb3dS9gLA_OdSmkGCNaBOyspD3ZwNbGBED9aACQENkAphFMSE7CQCLq8wXjbTgs:1rOisq:tAVeJRDJGWrQM8sH9A_9XQYE9FfBOlFIBnjZDFjac0A','2024-01-27 18:37:28.916364');

/*Table structure for table `games` */

DROP TABLE IF EXISTS `games`;

CREATE TABLE `games` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `type` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `region` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `games` */

insert  into `games`(`id`,`type`,`name`,`region`) values 
(1,'loto','Bao lô','bac'),
(2,'loxien','Lô xiên','bac'),
(3,'dauduoi','Đầu đuôi','bac'),
(4,'de','Đánh đề','bac'),
(5,'3cang','3 càng','bac'),
(6,'loto','Bao lô','trung'),
(7,'loxien','Lô xiên','trung'),
(8,'dauduoi','Đầu đuôi','trung'),
(9,'de','Đánh đề','trung'),
(10,'3cang','3 càng','trung'),
(11,'loto','Bao lô','nam'),
(12,'loda','Lô đá','nam'),
(13,'de','Đánh đề','nam'),
(14,'dauduoi','Đầu đuôi','nam'),
(15,'xiuchu','Xỉu chủ','nam');

/*Table structure for table `rates` */

DROP TABLE IF EXISTS `rates`;

CREATE TABLE `rates` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rate` decimal(5,2) NOT NULL,
  `group_id` int NOT NULL,
  `category_id` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=89 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `rates` */

insert  into `rates`(`id`,`rate`,`group_id`,`category_id`,`created_at`,`updated_at`) values 
(45,99.00,1,1,'2019-08-17 17:40:47.000000','2019-09-03 03:20:13.000000'),
(46,900.00,1,2,'2019-08-17 17:40:47.000000','2020-05-06 04:05:33.000000'),
(47,17.00,1,3,'2019-08-17 17:40:47.000000','2020-05-06 04:05:33.000000'),
(48,65.00,1,4,'2019-08-17 17:40:47.000000','2020-05-06 04:05:33.000000'),
(49,250.00,1,5,'2019-08-17 17:40:47.000000','2020-05-06 04:05:33.000000'),
(50,9.50,1,6,'2019-08-17 17:40:47.000000','2020-05-06 04:05:33.000000'),
(51,9.50,1,7,'2019-08-17 17:40:47.000000','2020-05-06 04:05:33.000000'),
(52,95.00,1,8,'2019-08-17 17:40:47.000000','2020-05-06 04:05:33.000000'),
(53,95.00,1,9,'2019-08-17 17:40:47.000000','2020-05-06 04:05:33.000000'),
(54,98.00,1,10,'2019-08-17 17:40:47.000000','2020-05-06 04:10:04.000000'),
(55,900.00,1,11,'2019-08-17 17:40:47.000000','2020-05-06 04:10:04.000000'),
(56,34.00,1,12,'2019-08-17 17:40:47.000000','2020-05-06 04:10:04.000000'),
(57,185.00,1,13,'2019-08-17 17:40:47.000000','2020-05-06 04:10:04.000000'),
(58,970.00,1,14,'2019-08-17 17:40:47.000000','2020-05-06 04:10:04.000000'),
(59,9.50,1,15,'2019-08-17 17:40:47.000000','2020-05-06 04:10:04.000000'),
(60,9.50,1,16,'2019-08-17 17:40:47.000000','2020-05-06 04:10:04.000000'),
(61,95.00,1,17,'2019-08-17 17:40:47.000000','2020-05-06 04:10:04.000000'),
(62,95.00,1,18,'2019-08-17 17:40:47.000000','2020-05-06 04:10:04.000000'),
(63,900.00,1,19,'2019-08-17 17:40:47.000000','2020-05-06 04:10:04.000000'),
(64,900.00,1,20,'2019-08-17 17:40:47.000000','2020-05-06 04:10:04.000000'),
(65,900.00,1,21,'2019-08-17 17:40:47.000000','2020-05-06 04:10:04.000000'),
(66,98.00,1,22,'2019-08-17 17:40:47.000000','2020-05-06 04:13:23.000000'),
(67,900.00,1,23,'2019-08-17 17:40:47.000000','2020-05-06 04:13:23.000000'),
(68,34.00,1,24,'2019-08-17 17:40:47.000000','2020-05-06 04:13:23.000000'),
(69,185.00,1,25,'2019-08-17 17:40:47.000000','2020-05-06 04:13:23.000000'),
(70,970.00,1,26,'2019-08-17 17:40:47.000000','2020-05-06 04:13:23.000000'),
(71,95.00,1,27,'2019-08-17 17:40:47.000000','2020-05-06 04:13:23.000000'),
(72,9.50,1,28,'2019-08-17 17:40:47.000000','2020-05-06 04:13:23.000000'),
(73,9.50,1,29,'2019-08-17 17:40:47.000000','2020-05-06 04:13:23.000000'),
(74,95.00,1,30,'2019-08-17 17:40:47.000000','2020-05-06 04:13:23.000000'),
(75,95.00,1,31,'2019-08-17 17:40:47.000000','2020-05-06 04:13:23.000000'),
(76,900.00,1,32,'2019-08-17 17:40:47.000000','2020-05-06 04:13:23.000000'),
(77,900.00,1,33,'2019-08-17 17:40:47.000000','2020-05-06 04:13:23.000000'),
(78,900.00,1,34,'2019-08-17 17:40:47.000000','2020-05-06 04:13:23.000000'),
(79,900.00,1,35,'2019-08-17 17:40:47.000000','2020-05-06 04:05:33.000000'),
(80,2.80,1,36,'2019-08-17 17:40:47.000000','2020-05-06 04:02:59.000000'),
(81,9.00,1,37,'2019-08-17 17:40:47.000000','2020-05-06 04:05:33.000000'),
(82,16.00,1,38,'2019-08-17 17:40:47.000000','2020-05-06 04:05:33.000000'),
(83,2.00,1,39,'2019-08-17 17:40:47.000000','2019-08-17 17:40:47.000000'),
(84,4.30,1,40,'2019-08-17 17:40:47.000000','2020-05-06 04:16:29.000000'),
(85,6.30,1,41,'2019-08-17 17:40:47.000000','2020-05-06 04:10:04.000000'),
(86,2.00,1,42,'2019-08-17 17:40:47.000000','2019-08-17 17:40:47.000000'),
(87,4.30,1,43,'2019-08-17 17:40:47.000000','2020-05-06 04:13:23.000000'),
(88,6.30,1,44,'2019-08-17 17:40:47.000000','2020-05-06 04:13:23.000000');

/*Table structure for table `subgames` */

DROP TABLE IF EXISTS `subgames`;

CREATE TABLE `subgames` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `region` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `guide` longtext NOT NULL,
  `rate` int NOT NULL,
  `pay_number` int NOT NULL,
  `min_amount` int NOT NULL,
  `max_amount` bigint NOT NULL,
  `multi` int NOT NULL,
  `code` varchar(255) NOT NULL,
  `max` int NOT NULL,
  `active` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `max_number` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `subgames` */

insert  into `subgames`(`id`,`name`,`region`,`type`,`guide`,`rate`,`pay_number`,`min_amount`,`max_amount`,`multi`,`code`,`max`,`active`,`created_at`,`updated_at`,`max_number`) values 
(1,'Lô 2 số','bac','loto','Đánh 2 chữ số cuối trong lô 27 giải. Thắng gấp {{ODDS}} lần, nếu số đó về N lần thì tính kết quả x N lần. Ví dụ: đánh lô 79 - 1 con 1k, Tổng thanh toán: 1k x 27 = 27k. Nếu trong lô có 2 chữ số cuối là 79 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k, nếu có N lần 2 chữ số cuối là 79 thì Tiền thắng là: 1k x {{ODDS}} x N',99,27,1000,10000000000,1,'loto_2so',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',0),
(2,'Lô 3 số','bac','loto','Đánh 3 chữ số cuối trong lô 23 giải. Thắng gấp {{ODDS}} lần, nếu số đó về N lần thì tính kết quả x N lần. Ví dụ: đánh lô 789 - 1 con 1k, Tổng thanh toán: 1k x 23 = 23k. Nếu trong lô có 3 chữ số cuối là 789 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k, nếu có N lần 3 chữ số cuối là 789 thì Tiền thắng là: 1k x {{ODDS}} x N',800,23,1000,10000000000,1,'loto_3so',1000,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',0),
(3,'Xiên 2','bac','loxien','Xiên 2 của 2 chữ số cuối trong lô 27 giải. Thắng gấp {{ODDS}} lần. Ví dụ : đánh 1k cho xiên 11+13, Tổng thanh toán: 1k. Nếu trong lô có 2 chữ số cuối là 11, 13 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',15,1,1000,10000000000,0,'loxien_2so',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',2),
(4,'Xiên 3','bac','loxien','Xiên 3 của 2 chữ số cuối trong lô 27 giải. Thắng gấp {{ODDS}} lần. Ví dụ : đánh 1k cho xiên 11+13+15, Tổng thanh toán: 1k. Nếu trong lô có 2 chữ số cuối là 11,13,15 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',50,1,1000,10000000000,0,'loxien_3so',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',3),
(5,'Xiên 4','bac','loxien','Xiên 4 của 2 chữ số cuối trong lô 27 giải. Thắng gấp {{ODDS}} lần. Ví dụ : đánh 1k cho xiên 11+13+15+20, Tổng thanh toán: 1k. Nếu trong lô có 2 chữ số cuối là 11,13,15,20 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',150,1,1000,10000000000,0,'loxien_4so',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',4),
(6,'Đầu','bac','dauduoi','Đánh 1 chữ số ở hàng chục của giải ĐB. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 7. Tổng thanh toán: 1K. Nếu giải ĐB là xxx7x thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',9,1,1000,10000000000,1,'dauduoi_dau',10,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',0),
(7,'Đuôi','bac','dauduoi','Đánh 1 chữ số cuối của giải ĐB. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 7. Tổng thanh toán: 1K. Nếu giải ĐB là xxxx7 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',9,1,1000,10000000000,1,'dauduoi_duoi',10,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',0),
(8,'Đề đầu','bac','de','Đánh lô giải 7 ( có 4 giải, thanh toán đủ ). Thắng gấp {{ODDS}} lần. Ví dụ : đánh 1k cho số 79, Tổng thanh toán: 1k x 4 =4k. Nếu trong lô giải 7 có 1 số 79 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k.',83,4,1000,10000000000,1,'de_dau',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',0),
(9,'Đề đặc biệt','bac','de','Đánh 2 chữ số cuối trong giải ĐB. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 79. Tổng thanh toán: 1k. Nếu giải ĐB là xxx79 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',83,1,1000,10000000000,1,'de_dacbiet',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',0),
(10,'Lô 2 số','trung','loto','Đánh 2 chữ số cuối trong lô 18 giải. Thắng gấp {{ODDS}} lần, nếu số đó về N lần thì tính kết quả x N lần. Ví dụ: đánh lô số 39 - 1 con 1k, Tổng thanh toán: 1k x 18 = 18k. Nếu trong lô có 1 lần 2 chữ số cuối là 39 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k, nếu có N lần 2 chữ số cuối là 39 thì Tiền thắng là: 1k x {{ODDS}} x N',81,18,1000,10000000000,1,'loto_2so',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',0),
(11,'Lô 3 số','trung','loto','Đánh 3 chữ số cuối trong lô 17 giải. Thắng gấp {{ODDS}} lần, nếu số đó về N lần thì tính kết quả x N lần. Ví dụ: đánh lô 789 - 1 con 1k, Tổng thanh toán: 1k x 17 = 17k. Nếu trong lô có 3 chữ số cuối là 789 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k, nếu có N lần 3 chữ số cuối là 789 thì Tiền thắng là: 1k x {{ODDS}} x N',800,17,1000,10000000000,1,'loto_3so',1000,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',0),
(12,'Xiên 2','trung','loxien','Xiên 2 của 2 chữ số cuối trong lô 18 giải. Thắng gấp {{ODDS}} lần. Ví dụ : đánh 1k cho xiên 11+13, Tổng thanh toán: 1k. Nếu trong lô có 2 chữ số cuối là 11,13 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',28,1,1000,10000000000,0,'da_2so',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',2),
(13,'Xiên 3','trung','loxien','	Xiên 3 của 2 chữ số cuối trong lô 18 giải. Thắng gấp {{ODDS}} lần. Ví dụ : đánh 1k cho xiên 11+13+15, Tổng thanh toán: 1k. Nếu trong lô có 2 chữ số cuối là 11,13,15 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',150,1,1000,10000000000,0,'da_3so',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',3),
(14,'Xiên 4','trung','loxien','Xiên 4 của 2 chữ số cuối trong lô 18 giải. Thắng gấp {{ODDS}} lần. Ví dụ : đánh 1k cho xiên 11+13+15+20, Tổng thanh toán: 1k. Nếu trong lô có 2 chữ số cuối là 11,13,15,20 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',700,1,1000,10000000000,0,'da_4so',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',4),
(15,'Đầu','trung','dauduoi','Đánh 1 chữ số ở hàng chục của giải ĐB. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 7. Tổng thanh toán: 1K. Nếu giải ĐB là xxx7x thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',9,1,1000,10000000000,1,'dauduoi_dau',10,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',0),
(16,'Đuôi','trung','dauduoi','Đánh 1 chữ số cuối của giải ĐB. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 9. Tổng thanh toán: 1k. Nếu giải ĐB là xxxx9 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',9,1,1000,10000000000,1,'dauduoi_duoi',10,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',0),
(17,'Đề đầu','trung','de','Đánh giải 8. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 79. Tổng thanh toán: 1k. Nếu giải 8 là 79 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',82,1,1000,10000000000,1,'de_dau',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',0),
(18,'Đề đặc biệt','trung','de','Đánh 2 chữ số cuối trong giải ĐB. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 79. Tổng thanh toán: 1k. Nếu giải ĐB là xxx79 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',83,1,1000,10000000000,1,'de_dacbiet',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',0),
(19,'3 càng đầu','trung','3cang','Đánh giải 7. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 879, Tổng thanh toán: 1k. Nếu giải 7 là 879 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}K',710,1,1000,10000000000,1,'xiuchu_dau',1000,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',0),
(20,' 3 càng đuôi','trung','3cang','Đánh 3 chữ số cuối của giải ĐB. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 879, Tổng thanh toán: 1k. Nếu giải ĐB là xx879 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}K',710,1,1000,10000000000,1,'xiuchu_duoi',1000,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',0),
(21,'3 càng đầu - đuôi','trung','3cang','Đánh 3 chữ số cuối của giải ĐB và giải 7. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 879, Tổng thanh toán: 2k. Nếu giải ĐB hoặc giải 7 có 3 chữ số cuối là 879 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',710,2,1000,10000000000,1,'xiuchu_dauduoi',1000,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',0),
(22,'Lô 2 số','nam','loto','Đánh 2 chữ số cuối trong lô 18 giải. Thắng gấp {{ODDS}} lần, nếu số đó về N lần thì tính kết quả x N lần. Ví dụ: bao lô 39 - 1 con 1k, Tổng thanh toán: 1k x 18 = 18k. Nếu trong lô có 1 lần 2 chữ số cuối là 39 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k, nếu có N lần 2 chữ số cuối là 39 thì Tiền thắng là: 1k x {{ODDS}} x N',81,18,1000,10000000000,1,'loto_2so',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',0),
(23,'Lô 3 số','nam','loto','Đánh 3 chữ số cuối trong lô 17 giải. Thắng gấp {{ODDS}} lần, nếu số đó về N lần thì tính kết quả x N lần. Ví dụ: bao lô 789 - 1 con 1k, Tổng thanh toán: 1k x 17 = 17k. Nếu trong lô có 3 chữ số cuối là 789 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k, nếu có N lần 3 chữ số cuối là 789 thì Tiền thắng là: 1k x {{ODDS}} x N',800,17,1000,10000000000,1,'loto_3so',1000,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',0),
(24,'Đá 2','nam','loda','Đá 2 của 2 chữ số cuối trong lô 18 giải. Thắng gấp {{ODDS}} lần. Ví dụ : đánh 1k cho đá 11+13. Tổng thanh toán: 1k. Nếu trong lô có \"1 số mà 2 chữ số cuối là 11 và 1 số mà 2 chữ số cuối là 13\" thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',28,1,1000,10000000000,0,'da_2so',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',2),
(25,'Đá 3','nam','loda','Đá 3 của 2 chữ số cuối trong lô 18 giải. Thắng gấp {{ODDS}} lần. Ví dụ : đánh 1k cho đá 11+13+15, Tổng thanh toán: 1k. Nếu trong lô có 2 chữ số cuối là 11,13,15 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',150,1,1000,10000000000,0,'da_3so',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',3),
(26,'Đá 4','nam','loda','Đá 4 của 2 chữ số cuối trong lô 18 giải. Thắng gấp {{ODDS}} lần. Ví dụ : đánh 1k cho đá 11+13+15+20, Tổng thanh toán: 1k. Nếu trong lô có 2 chữ số cuối là 11,13,15,20 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',700,1,1000,10000000000,0,'da_4so',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',4),
(27,'Đánh đầu đuôi','nam','de','Đánh 2 chữ số cuối trong giải ĐB và Giải 8. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 79. Tổng thanh toán: 2k. Nếu giải ĐB hoặc giải 8 có 2 chữ số cuối là 79 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',85,2,1000,10000000000,2,'de_dauduoi',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',0),
(28,'Đầu','nam','dauduoi','	Đánh 1 chữ số hàng chục của giải ĐB. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 6. Tổng thanh toán: 1k. Nếu giải ĐB là xxxx6x thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',9,1,1000,10000000000,1,'dauduoi_dau',10,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',0),
(29,'Đuôi','nam','dauduoi','Đánh 1 chữ số cuối của giải ĐB. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 9. Tổng thanh toán: 1k. Nếu giải ĐB là xxxxx9 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',9,1,1000,10000000000,1,'dauduoi_duoi',10,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',0),
(30,'Đề đầu','nam','de','Đánh giải 8. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 79. Tổng thanh toán: 1k. Nếu giải 8 là 79 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',83,1,1000,10000000000,1,'de_dau',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',0),
(31,'Đề đặc biệt','nam','de','Đánh 2 chữ số cuối trong giải ĐB. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 79. Tổng thanh toán: 1k. Nếu giải ĐB là xxx79 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',83,1,1000,10000000000,1,'de_dacbiet',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',0),
(32,'Xỉu chủ đầu','nam','xiuchu','Đánh giải 7. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 879, Tổng thanh toán: 1k. Nếu giải 7 là 879 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}K',710,1,1000,10000000000,1,'xiuchu_dau',1000,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',0),
(33,'Xỉu chủ đuôi','nam','xiuchu','Đánh 3 chữ số cuối của giải ĐB. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 879, Tổng thanh toán: 1k. Nếu giải ĐB là xx879 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}K',710,1,1000,10000000000,1,'xiuchu_duoi',1000,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',0),
(34,'Xỉu chủ đầu - đuôi','nam','xiuchu','Đánh 3 chữ số cuối của giải ĐB và giải 7. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 879, Tổng thanh toán: 2k. Nếu giải ĐB hoặc giải 7 có 3 chữ số cuối là 879 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',710,2,1000,10000000000,1,'xiuchu_dauduoi',1000,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',0),
(35,'3 càng','bac','3cang','Đánh 3 chữ số cuối của giải ĐB. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 879, Tổng thanh toán: 1k. Nếu giải ĐB là xx879 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}K',710,1,1000,10000000000,1,'3cang',1000,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',0);

/*Table structure for table `token_blacklist_blacklistedtoken` */

DROP TABLE IF EXISTS `token_blacklist_blacklistedtoken`;

CREATE TABLE `token_blacklist_blacklistedtoken` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `blacklisted_at` datetime(6) NOT NULL,
  `token_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token_id` (`token_id`),
  CONSTRAINT `token_blacklist_blacklistedtoken_token_id_3cc7fe56_fk` FOREIGN KEY (`token_id`) REFERENCES `token_blacklist_outstandingtoken` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `token_blacklist_blacklistedtoken` */

/*Table structure for table `token_blacklist_outstandingtoken` */

DROP TABLE IF EXISTS `token_blacklist_outstandingtoken`;

CREATE TABLE `token_blacklist_outstandingtoken` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `token` longtext NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `expires_at` datetime(6) NOT NULL,
  `user_id` int DEFAULT NULL,
  `jti` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token_blacklist_outstandingtoken_jti_hex_d9bdf6f7_uniq` (`jti`),
  KEY `token_blacklist_outs_user_id_83bc629a_fk_auth_user` (`user_id`),
  CONSTRAINT `token_blacklist_outs_user_id_83bc629a_fk_auth_user` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `token_blacklist_outstandingtoken` */

insert  into `token_blacklist_outstandingtoken`(`id`,`token`,`created_at`,`expires_at`,`user_id`,`jti`) values 
(1,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjc2MDU1NSwiaWF0IjoxNzA0OTg0NTU1LCJqdGkiOiI3NTE4Mjc1ZWFkOGM0YTRjOWMxZWYzMDczYmFhODViYSIsInVzZXJfaWQiOjF9.3wSZF-ls-EZ76BTEGqhz3qK3ViPHX-UxIClEDNeabsA','2024-01-11 14:49:15.228434','2024-04-10 14:49:15.000000',1,'7518275ead8c4a4c9c1ef3073baa85ba'),
(2,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjc2MTAzNCwiaWF0IjoxNzA0OTg1MDM0LCJqdGkiOiI5MGNmZjZlNDU2YWQ0MTVjYWYzOTMzZWJlNTgxNGUzZiIsInVzZXJfaWQiOjJ9.RqCfrBJoJykcvI48FG1Mx1x-wJsS9aEq7vvyeEoSjAQ','2024-01-11 14:57:14.676074','2024-04-10 14:57:14.000000',2,'90cff6e456ad415caf3933ebe5814e3f'),
(3,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjc2Mzk3MSwiaWF0IjoxNzA0OTg3OTcxLCJqdGkiOiIwNGIyZDkxMzMyNjM0YWJlYjAyODgxNjQ0YzNkNjM2OSIsInVzZXJfaWQiOjF9.LR_IgArCHMPhyiAtVm6_yFJadr6CUbMDcpRp-W4hAyI','2024-01-11 15:46:11.809016','2024-04-10 15:46:11.000000',1,'04b2d91332634abeb02881644c3d6369'),
(4,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjc2NDI1MSwiaWF0IjoxNzA0OTg4MjUxLCJqdGkiOiI3ZTM3MjE5MGNiY2I0MWRmOTU0NGI0NjI5YjA5Njc1ZSIsInVzZXJfaWQiOjF9.LoD440jdCwzq3C3UYR2D7w_ivpUemtwufLaBYwgDsxI','2024-01-11 15:50:51.970844','2024-04-10 15:50:51.000000',1,'7e372190cbcb41df9544b4629b09675e'),
(5,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjc3MTE0MywiaWF0IjoxNzA0OTk1MTQzLCJqdGkiOiI5NjhhZjg0NDc3MjU0ODY1OWU5YWY5MTQzYjYzMDQyMCIsInVzZXJfaWQiOjF9.x32OS_dTWXV6N6Euwm_qsGcQlS-BrHO1eXINrSGpa40','2024-01-11 17:45:43.723930','2024-04-10 17:45:43.000000',1,'968af844772548659e9af9143b630420'),
(6,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjkxMzk0NiwiaWF0IjoxNzA1MTM3OTQ2LCJqdGkiOiIyMjJhNTQ2NTdhM2E0ZmJjYTgwMzhlODRjMDgzMWM4YyIsInVzZXJfaWQiOjF9.PFTsKqthZBx8WmMa0smk_7EatlcsbISHQAetmq-V_kw','2024-01-13 09:25:46.376445','2024-04-12 09:25:46.000000',1,'222a54657a3a4fbca8038e84c0831c8c'),
(7,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjkxNDEyMywiaWF0IjoxNzA1MTM4MTIzLCJqdGkiOiIyOTE0NzRhNzFkNTk0OWYxYjZiN2IxOTAxYTlmNzdiNCIsInVzZXJfaWQiOjF9.NZnjBNQZlqv8Psv-V8UjHS7COha5g8CH1WQfKF_ClqQ','2024-01-13 09:28:43.247559','2024-04-12 09:28:43.000000',1,'291474a71d5949f1b6b7b1901a9f77b4'),
(8,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjkxNDg2NiwiaWF0IjoxNzA1MTM4ODY2LCJqdGkiOiJhMWJkMWEwYzE4NjY0NmE2YmVhODRiMDdjMmJmMDgyMiIsInVzZXJfaWQiOjF9.NJU1evnBBhGEDPzdTZHXpOYwsTFAD05JvIrJYKSp60I','2024-01-13 09:41:06.433849','2024-04-12 09:41:06.000000',1,'a1bd1a0c186646a6bea84b07c2bf0822'),
(9,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjkxNTQxNCwiaWF0IjoxNzA1MTM5NDE0LCJqdGkiOiJiNmRkNWZhNDc4MDE0OWE4YTJlMjc1MTE3N2IzMzQ4MyIsInVzZXJfaWQiOjF9.N8Yn0NUes0uUW9HCtLWMQsX7zMmjJp_UgS1ktD0P6_4','2024-01-13 09:50:14.181433','2024-04-12 09:50:14.000000',1,'b6dd5fa4780149a8a2e2751177b33483'),
(10,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjkzNTA5OCwiaWF0IjoxNzA1MTU5MDk4LCJqdGkiOiJjYjlhMzgwZTJiOTI0YjMwYmU4ZDNiNzVjNDk3NTkxMyIsInVzZXJfaWQiOjF9.8uSMK9fsAh9W-2UIC0jVrxzWyWdKLRpVb0BMblsWuKs','2024-01-13 15:18:18.808175','2024-04-12 15:18:18.000000',1,'cb9a380e2b924b30be8d3b75c4975913'),
(11,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjk0Mjg0MSwiaWF0IjoxNzA1MTY2ODQxLCJqdGkiOiJlOWU5MGZhMzJmYWM0ZTVmODA2N2RkZGNiM2VmNTVlNSIsInVzZXJfaWQiOjF9.MTTEzot90hIeegOQMaXC2a40woOhcTHq_Hueri00VOQ','2024-01-13 17:27:21.969378','2024-04-12 17:27:21.000000',1,'e9e90fa32fac4e5f8067dddcb3ef55e5'),
(12,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjk0NjAyNywiaWF0IjoxNzA1MTcwMDI3LCJqdGkiOiI3OTVmYzAzNmM4NjE0ZjQ5ODE3NGFjZDU0MGVjMzVhNCIsInVzZXJfaWQiOjF9.W6io0fNmDAM74790j0rGaE0MUS_I8tzzr0-GA7MJzdE','2024-01-13 18:20:27.120570','2024-04-12 18:20:27.000000',1,'795fc036c8614f498174acd540ec35a4'),
(13,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjk0NjAzOCwiaWF0IjoxNzA1MTcwMDM4LCJqdGkiOiIxNDU4ZWU0OTljMTU0N2QzYTcwYjg0Mzg5OGM3NGVmOSIsInVzZXJfaWQiOjF9.LS658qlKjUV1hEPRONSD4xYD48TjabN6dM3WqaonBV4','2024-01-13 18:20:38.645865','2024-04-12 18:20:38.000000',1,'1458ee499c1547d3a70b843898c74ef9'),
(14,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjk0NjA1OSwiaWF0IjoxNzA1MTcwMDU5LCJqdGkiOiJmOGZjYjAzOTQyYzY0OWQwOTk0MTZkYjExMTczZGYwYyIsInVzZXJfaWQiOjF9.jtXjTe79DGsMe3dFbGD5bC8HsejEKjZHfytssMLyN3M','2024-01-13 18:20:59.012267','2024-04-12 18:20:59.000000',1,'f8fcb03942c649d099416db11173df0c'),
(15,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjk0NjExNCwiaWF0IjoxNzA1MTcwMTE0LCJqdGkiOiI3OWMwNjczYjRhMjg0NmU2YjE1ZmVmOWVhOTJiNmZmZiIsInVzZXJfaWQiOjF9._HeVLoxgTQc5TiXpCQnn2DKgm4dBqAVY98QimfMlSvs','2024-01-13 18:21:54.034902','2024-04-12 18:21:54.000000',1,'79c0673b4a2846e6b15fef9ea92b6fff'),
(16,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjk0NjI3MywiaWF0IjoxNzA1MTcwMjczLCJqdGkiOiI3YWU5ZGEzNzNhZTI0NmVmYmE5ODRkMDY5MDhmNTExMyIsInVzZXJfaWQiOjF9.yey-v7-xpXk2t4kNdYGD2R0vu-INi3vxwVwOk9pZg20','2024-01-13 18:24:33.369156','2024-04-12 18:24:33.000000',1,'7ae9da373ae246efba984d06908f5113'),
(17,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjk0NjI5OSwiaWF0IjoxNzA1MTcwMjk5LCJqdGkiOiIzMjA1MzdiZWNkNjY0NjM4YmFjNTQ2OWZiYzZlNTVmNCIsInVzZXJfaWQiOjF9.h8RtE2TjXb2a_OYXst8fH1bpiyClkEHOAlirne5vGJs','2024-01-13 18:24:59.203673','2024-04-12 18:24:59.000000',1,'320537becd664638bac5469fbc6e55f4'),
(18,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjk0NjU2MSwiaWF0IjoxNzA1MTcwNTYxLCJqdGkiOiI2MzBiODY3Yzc2ZjM0MzM2YWEyMzhmZTg2ZDJkYjZmMiIsInVzZXJfaWQiOjF9.9OVyN5GQpIcfKtphn9WZVPzIYBLJmFiabhj_0baf5YM','2024-01-13 18:29:21.868380','2024-04-12 18:29:21.000000',1,'630b867c76f34336aa238fe86d2db6f2'),
(19,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjk0NjYwOSwiaWF0IjoxNzA1MTcwNjA5LCJqdGkiOiJhZTkxODFmZjNlMzA0NGE0YmVkZjBhY2M3ZTZlNmRiMSIsInVzZXJfaWQiOjF9.wIJwdlhb7SGqvInhGPjqM7rDLDUcg32hE421-G2nXNc','2024-01-13 18:30:09.251708','2024-04-12 18:30:09.000000',1,'ae9181ff3e3044a4bedf0acc7e6e6db1'),
(20,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjk0Njc3NywiaWF0IjoxNzA1MTcwNzc3LCJqdGkiOiI3ODIzYmI4MTI3MDg0N2E1OGFiMGFmZmUyYTBkNWE0ZiIsInVzZXJfaWQiOjF9.oa7iynrWb_RwfpWTxz0tavh1yNZIlD-vqVv0uQ6eOt4','2024-01-13 18:32:57.284457','2024-04-12 18:32:57.000000',1,'7823bb81270847a58ab0affe2a0d5a4f'),
(21,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjk0NjgzNCwiaWF0IjoxNzA1MTcwODM0LCJqdGkiOiIxZTJkZjU4MGQ3MDM0NjJhOTFlZmNlMjVhYTEzZjY4MyIsInVzZXJfaWQiOjF9.ZTCckurdnpfBC9q5tHhdOodhaGoLUV15h1K01s9GDfU','2024-01-13 18:33:54.790980','2024-04-12 18:33:54.000000',1,'1e2df580d703462a91efce25aa13f683'),
(22,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjk0Njg5OCwiaWF0IjoxNzA1MTcwODk4LCJqdGkiOiIwMDY2ZmI2NGY2NmE0ZmRjYmQ4YjdmMzdlNmVmZjRkYyIsInVzZXJfaWQiOjF9.CKMvfoXxpz0tS90BdVw8b6lYQKUBgsfE3eKmgY6wFFA','2024-01-13 18:34:58.817716','2024-04-12 18:34:58.000000',1,'0066fb64f66a4fdcbd8b7f37e6eff4dc'),
(23,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjk0NjkzOSwiaWF0IjoxNzA1MTcwOTM5LCJqdGkiOiJjMTMzOGJkNzQ5OGY0NTYzYjQ0ZWE2NzBjYmQ3NzI2YiIsInVzZXJfaWQiOjF9.kK37m3RRnA12xwJy7cAkp9cXgIMGgu69zlA9rQstLws','2024-01-13 18:35:39.928435','2024-04-12 18:35:39.000000',1,'c1338bd7498f4563b44ea670cbd7726b'),
(24,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjk0Njk2NiwiaWF0IjoxNzA1MTcwOTY2LCJqdGkiOiJmYThkMDliYmQ0MmI0M2EyYTFkNTA0MDZmMzcxZjY3MyIsInVzZXJfaWQiOjF9.H_wA5JA2uHLNA3aZ5TcDZQ_tZRZaQoHQr6l8YUI6T1U','2024-01-13 18:36:06.009170','2024-04-12 18:36:06.000000',1,'fa8d09bbd42b43a2a1d50406f371f673'),
(25,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjk0NzAwNSwiaWF0IjoxNzA1MTcxMDA1LCJqdGkiOiI2OGNiMmE2YWVjNGQ0ZWEyOTVmNWEyMzYxZGIyNzdlOCIsInVzZXJfaWQiOjF9.bxOeEfzv2D0NZ2bA4qIs81dlCjWe9ZdeN_SmCeXUZzE','2024-01-13 18:36:45.574411','2024-04-12 18:36:45.000000',1,'68cb2a6aec4d4ea295f5a2361db277e8'),
(26,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjk0NzA0OCwiaWF0IjoxNzA1MTcxMDQ4LCJqdGkiOiJjZDU0NzIxMjNkMjg0MDM3YWY0NTQ2MmQ5N2ZmZjQyZCIsInVzZXJfaWQiOjF9.6R3I_He4OrPb6cLPqhaRTXt1UwWQP-lYeS4LjBmy8Oc','2024-01-13 18:37:28.913372','2024-04-12 18:37:28.000000',1,'cd5472123d284037af45462d97fff42d'),
(27,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjk0NzExNiwiaWF0IjoxNzA1MTcxMTE2LCJqdGkiOiJhNzdkYTljODZlNWM0OWUyYWU1NGYyNjRjNDEwYWEwMyIsInVzZXJfaWQiOjF9.ETtBFTz1yqTk1q59PbXw4aLfsO8xokEHmlcBnnPj_FI','2024-01-13 18:38:36.272065','2024-04-12 18:38:36.000000',1,'a77da9c86e5c49e2ae54f264c410aa03'),
(28,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjk0NzIyMCwiaWF0IjoxNzA1MTcxMjIwLCJqdGkiOiI5MjU2YjY1MGQ1MWQ0ZGMwYThhY2Y0NWM3OWNhM2Y5ZiIsInVzZXJfaWQiOjF9.2A-YfCanLNAZWtQrNqiHmR1_2JQW-F5oSMGnhbYTBeM','2024-01-13 18:40:20.578930','2024-04-12 18:40:20.000000',1,'9256b650d51d4dc0a8acf45c79ca3f9f'),
(29,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjk0NzIyMywiaWF0IjoxNzA1MTcxMjIzLCJqdGkiOiJmMmJjZWRkMzE2NmU0ZDIwYjIxYzZiNWNkMTQyMTQzZSIsInVzZXJfaWQiOjF9.2ctKthNNrmxtg3vkgjl98xyyTI17QvtRLBvLD-Tj8Cw','2024-01-13 18:40:23.487657','2024-04-12 18:40:23.000000',1,'f2bcedd3166e4d20b21c6b5cd142143e'),
(30,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjk0NzIzNiwiaWF0IjoxNzA1MTcxMjM2LCJqdGkiOiJkMGEwOTU1MGRjNzY0ZTJlYjNiYmQ3OTM0NmYzZWE5YiIsInVzZXJfaWQiOjF9.nFifcmUQdlUernIPQwOzB1TawDVnEHPU3SGUbB1b1_4','2024-01-13 18:40:36.068625','2024-04-12 18:40:36.000000',1,'d0a09550dc764e2eb3bbd79346f3ea9b'),
(31,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjk0NzMwMCwiaWF0IjoxNzA1MTcxMzAwLCJqdGkiOiI5MmMyMTU4NTU2YjM0ODY4ODE2MTlmMGE0MDRhN2RjZiIsInVzZXJfaWQiOjF9.RGYY4DlEbqnAAFbUjTagBF0UDR2B3EMdvcp1w8yxsJ0','2024-01-13 18:41:40.399718','2024-04-12 18:41:40.000000',1,'92c2158556b3486881619f0a404a7dcf'),
(32,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjk0NzMxOCwiaWF0IjoxNzA1MTcxMzE4LCJqdGkiOiJhMDU0NzQ3N2YyZjI0NTM5OTFmNTdmODhlMGIzMmM1NSIsInVzZXJfaWQiOjF9.9sLce7efIE8bFlGdzheT0pSbZXPAmYFP4vd2sBElspk','2024-01-13 18:41:58.094301','2024-04-12 18:41:58.000000',1,'a0547477f2f2453991f57f88e0b32c55'),
(33,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjk0NzMzOSwiaWF0IjoxNzA1MTcxMzM5LCJqdGkiOiJmYWYwNTg5YmQxNTM0MjMyYmE1NzdkMDEzNzJjYzNmYiIsInVzZXJfaWQiOjF9.TQ_mFgr09IlXzIFP8GpF8UGavycfFwsuNLxBpQWhaSw','2024-01-13 18:42:19.732791','2024-04-12 18:42:19.000000',1,'faf0589bd1534232ba577d01372cc3fb'),
(34,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjk0NzM0NiwiaWF0IjoxNzA1MTcxMzQ2LCJqdGkiOiI1NmVlMjM0NDE3ZTk0MjFiODIyOTg3NDY0MDlmNDU5MyIsInVzZXJfaWQiOjF9.WxUNAqE8etXU2N8J6DeKc4eh4Lt-WWfZhqNFWzqXK0E','2024-01-13 18:42:26.263244','2024-04-12 18:42:26.000000',1,'56ee234417e9421b82298746409f4593'),
(35,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjk0NzM2OSwiaWF0IjoxNzA1MTcxMzY5LCJqdGkiOiJmMThiYjBlNmRlNmY0MTI5ODgzNWQ3N2IyMjNkMDNmNyIsInVzZXJfaWQiOjF9.07iXyPNbXrqjFTcBd5VB3nzj08w_0oLxhymPkE0enCc','2024-01-13 18:42:49.709688','2024-04-12 18:42:49.000000',1,'f18bb0e6de6f41298835d77b223d03f7'),
(36,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMzAyMjI2MywiaWF0IjoxNzA1MjQ2MjYzLCJqdGkiOiIwZjExODgxZjhhNzk0ZTc4OGQzYWJjNjc0YTk3MGZkYiIsInVzZXJfaWQiOjF9.I2OlhFU8rrOkA27muprCYU9H2A41OhzkjaIcstnZsgQ','2024-01-14 15:31:03.985957','2024-04-13 15:31:03.000000',1,'0f11881f8a794e788d3abc674a970fdb');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
