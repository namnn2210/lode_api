/*
SQLyog Community v13.2.0 (64 bit)
MySQL - 8.0.35-0ubuntu0.22.04.1 : Database - lode_com
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
/*Data for the table `banking` */

insert  into `banking`(`id`,`bank_name`,`bank_number`,`user_name`,`created_at`,`status`,`updated_at`) values 
(2,'VIB','563633686','DO VAN NINH','2024-01-18 17:30:47.220145',1,'2024-01-18 17:30:47.220145');

/*Data for the table `cities` */

insert  into `cities`(`id`,`name`,`date`,`region`,`feature`,`time_release`,`status`,`created_at`,`updated_at`) values 
(1,'Miền Bắc','','bac',0,'18:15:00',1,'2019-08-16 09:14:40.000000','2019-08-16 23:00:36.000000'),
(6,'Gia Lai','5','trung',0,'17:15:00',1,'2019-08-16 09:14:40.000000','2019-08-16 09:14:40.000000'),
(9,'Ninh Thuận','5','trung',0,'17:15:00',1,'2019-08-16 09:14:40.000000','2019-08-16 09:14:40.000000'),
(19,'Bình Dương','5','nam',0,'16:15:00',1,'2019-08-16 09:14:40.000000','2019-08-16 09:14:40.000000'),
(33,'Trà Vinh','5','nam',0,'16:15:00',1,'2019-08-16 09:14:40.000000','2019-08-16 09:14:40.000000'),
(34,'Vĩnh Long','5','nam',0,'16:15:00',1,'2019-08-16 09:14:40.000000','2019-08-16 09:14:40.000000');

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

/*Data for the table `subgames` */

insert  into `subgames`(`id`,`name`,`region`,`type`,`guide`,`rate`,`pay_number`,`min_amount`,`max_amount`,`multi`,`code`,`max`,`active`,`created_at`,`updated_at`,`max_number`) values 
(1,'Lô 2 số','bac','loto','Đánh 2 chữ số cuối trong lô 27 giải. Thắng gấp {{ODDS}} lần, nếu số đó về N lần thì tính kết quả x N lần. Ví dụ: đánh lô 79 - 1 con 1k, Tổng thanh toán: 1k x 27 = 27k. Nếu trong lô có 2 chữ số cuối là 79 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k, nếu có N lần 2 chữ số cuối là 79 thì Tiền thắng là: 1k x {{ODDS}} x N',99,27,1000,10000000000,1,'loto_2so',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',10),
(2,'Lô 3 số','bac','loto','Đánh 3 chữ số cuối trong lô 23 giải. Thắng gấp {{ODDS}} lần, nếu số đó về N lần thì tính kết quả x N lần. Ví dụ: đánh lô 789 - 1 con 1k, Tổng thanh toán: 1k x 23 = 23k. Nếu trong lô có 3 chữ số cuối là 789 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k, nếu có N lần 3 chữ số cuối là 789 thì Tiền thắng là: 1k x {{ODDS}} x N',800,23,1000,10000000000,1,'loto_3so',1000,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',10),
(3,'Xiên 2','bac','loxien','Xiên 2 của 2 chữ số cuối trong lô 27 giải. Thắng gấp {{ODDS}} lần. Ví dụ : đánh 1k cho xiên 11+13, Tổng thanh toán: 1k. Nếu trong lô có 2 chữ số cuối là 11, 13 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',15,1,1000,10000000000,0,'loxien_2so',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',2),
(4,'Xiên 3','bac','loxien','Xiên 3 của 2 chữ số cuối trong lô 27 giải. Thắng gấp {{ODDS}} lần. Ví dụ : đánh 1k cho xiên 11+13+15, Tổng thanh toán: 1k. Nếu trong lô có 2 chữ số cuối là 11,13,15 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',50,1,1000,10000000000,0,'loxien_3so',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',3),
(5,'Xiên 4','bac','loxien','Xiên 4 của 2 chữ số cuối trong lô 27 giải. Thắng gấp {{ODDS}} lần. Ví dụ : đánh 1k cho xiên 11+13+15+20, Tổng thanh toán: 1k. Nếu trong lô có 2 chữ số cuối là 11,13,15,20 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',150,1,1000,10000000000,0,'loxien_4so',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',4),
(6,'Đầu','bac','dauduoi','Đánh 1 chữ số ở hàng chục của giải ĐB. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 7. Tổng thanh toán: 1K. Nếu giải ĐB là xxx7x thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',9,1,1000,10000000000,1,'dauduoi_dau',10,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',10),
(7,'Đuôi','bac','dauduoi','Đánh 1 chữ số cuối của giải ĐB. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 7. Tổng thanh toán: 1K. Nếu giải ĐB là xxxx7 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',9,1,1000,10000000000,1,'dauduoi_duoi',10,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',10),
(8,'Đề đầu','bac','de','Đánh lô giải 7 ( có 4 giải, thanh toán đủ ). Thắng gấp {{ODDS}} lần. Ví dụ : đánh 1k cho số 79, Tổng thanh toán: 1k x 4 =4k. Nếu trong lô giải 7 có 1 số 79 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k.',83,4,1000,10000000000,1,'de_dau',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',10),
(9,'Đề đặc biệt','bac','de','Đánh 2 chữ số cuối trong giải ĐB. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 79. Tổng thanh toán: 1k. Nếu giải ĐB là xxx79 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',83,1,1000,10000000000,1,'de_dacbiet',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',10),
(10,'Lô 2 số','trung','loto','Đánh 2 chữ số cuối trong lô 18 giải. Thắng gấp {{ODDS}} lần, nếu số đó về N lần thì tính kết quả x N lần. Ví dụ: đánh lô số 39 - 1 con 1k, Tổng thanh toán: 1k x 18 = 18k. Nếu trong lô có 1 lần 2 chữ số cuối là 39 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k, nếu có N lần 2 chữ số cuối là 39 thì Tiền thắng là: 1k x {{ODDS}} x N',81,18,1000,10000000000,1,'loto_2so',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',10),
(11,'Lô 3 số','trung','loto','Đánh 3 chữ số cuối trong lô 17 giải. Thắng gấp {{ODDS}} lần, nếu số đó về N lần thì tính kết quả x N lần. Ví dụ: đánh lô 789 - 1 con 1k, Tổng thanh toán: 1k x 17 = 17k. Nếu trong lô có 3 chữ số cuối là 789 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k, nếu có N lần 3 chữ số cuối là 789 thì Tiền thắng là: 1k x {{ODDS}} x N',800,17,1000,10000000000,1,'loto_3so',1000,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',10),
(12,'Xiên 2','trung','loxien','Xiên 2 của 2 chữ số cuối trong lô 18 giải. Thắng gấp {{ODDS}} lần. Ví dụ : đánh 1k cho xiên 11+13, Tổng thanh toán: 1k. Nếu trong lô có 2 chữ số cuối là 11,13 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',28,1,1000,10000000000,0,'da_2so',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',2),
(13,'Xiên 3','trung','loxien','	Xiên 3 của 2 chữ số cuối trong lô 18 giải. Thắng gấp {{ODDS}} lần. Ví dụ : đánh 1k cho xiên 11+13+15, Tổng thanh toán: 1k. Nếu trong lô có 2 chữ số cuối là 11,13,15 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',150,1,1000,10000000000,0,'da_3so',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',3),
(14,'Xiên 4','trung','loxien','Xiên 4 của 2 chữ số cuối trong lô 18 giải. Thắng gấp {{ODDS}} lần. Ví dụ : đánh 1k cho xiên 11+13+15+20, Tổng thanh toán: 1k. Nếu trong lô có 2 chữ số cuối là 11,13,15,20 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',700,1,1000,10000000000,0,'da_4so',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',4),
(15,'Đầu','trung','dauduoi','Đánh 1 chữ số ở hàng chục của giải ĐB. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 7. Tổng thanh toán: 1K. Nếu giải ĐB là xxx7x thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',9,1,1000,10000000000,1,'dauduoi_dau',10,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',10),
(16,'Đuôi','trung','dauduoi','Đánh 1 chữ số cuối của giải ĐB. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 9. Tổng thanh toán: 1k. Nếu giải ĐB là xxxx9 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',9,1,1000,10000000000,1,'dauduoi_duoi',10,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',10),
(17,'Đề đầu','trung','de','Đánh giải 8. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 79. Tổng thanh toán: 1k. Nếu giải 8 là 79 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',82,1,1000,10000000000,1,'de_dau',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',10),
(18,'Đề đặc biệt','trung','de','Đánh 2 chữ số cuối trong giải ĐB. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 79. Tổng thanh toán: 1k. Nếu giải ĐB là xxx79 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',83,1,1000,10000000000,1,'de_dacbiet',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',10),
(19,'3 càng đầu','trung','3cang','Đánh giải 7. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 879, Tổng thanh toán: 1k. Nếu giải 7 là 879 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}K',710,1,1000,10000000000,1,'xiuchu_dau',1000,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',10),
(20,' 3 càng đuôi','trung','3cang','Đánh 3 chữ số cuối của giải ĐB. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 879, Tổng thanh toán: 1k. Nếu giải ĐB là xx879 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}K',710,1,1000,10000000000,1,'xiuchu_duoi',1000,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',10),
(21,'3 càng đầu - đuôi','trung','3cang','Đánh 3 chữ số cuối của giải ĐB và giải 7. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 879, Tổng thanh toán: 2k. Nếu giải ĐB hoặc giải 7 có 3 chữ số cuối là 879 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',710,2,1000,10000000000,1,'xiuchu_dauduoi',1000,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',10),
(22,'Lô 2 số','nam','loto','Đánh 2 chữ số cuối trong lô 18 giải. Thắng gấp {{ODDS}} lần, nếu số đó về N lần thì tính kết quả x N lần. Ví dụ: bao lô 39 - 1 con 1k, Tổng thanh toán: 1k x 18 = 18k. Nếu trong lô có 1 lần 2 chữ số cuối là 39 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k, nếu có N lần 2 chữ số cuối là 39 thì Tiền thắng là: 1k x {{ODDS}} x N',81,18,1000,10000000000,1,'loto_2so',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',10),
(23,'Lô 3 số','nam','loto','Đánh 3 chữ số cuối trong lô 17 giải. Thắng gấp {{ODDS}} lần, nếu số đó về N lần thì tính kết quả x N lần. Ví dụ: bao lô 789 - 1 con 1k, Tổng thanh toán: 1k x 17 = 17k. Nếu trong lô có 3 chữ số cuối là 789 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k, nếu có N lần 3 chữ số cuối là 789 thì Tiền thắng là: 1k x {{ODDS}} x N',800,17,1000,10000000000,1,'loto_3so',1000,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',10),
(24,'Đá 2','nam','loda','Đá 2 của 2 chữ số cuối trong lô 18 giải. Thắng gấp {{ODDS}} lần. Ví dụ : đánh 1k cho đá 11+13. Tổng thanh toán: 1k. Nếu trong lô có \"1 số mà 2 chữ số cuối là 11 và 1 số mà 2 chữ số cuối là 13\" thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',28,1,1000,10000000000,0,'da_2so',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',2),
(25,'Đá 3','nam','loda','Đá 3 của 2 chữ số cuối trong lô 18 giải. Thắng gấp {{ODDS}} lần. Ví dụ : đánh 1k cho đá 11+13+15, Tổng thanh toán: 1k. Nếu trong lô có 2 chữ số cuối là 11,13,15 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',150,1,1000,10000000000,0,'da_3so',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',3),
(26,'Đá 4','nam','loda','Đá 4 của 2 chữ số cuối trong lô 18 giải. Thắng gấp {{ODDS}} lần. Ví dụ : đánh 1k cho đá 11+13+15+20, Tổng thanh toán: 1k. Nếu trong lô có 2 chữ số cuối là 11,13,15,20 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',700,1,1000,10000000000,0,'da_4so',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',4),
(27,'Đánh đầu đuôi','nam','de','Đánh 2 chữ số cuối trong giải ĐB và Giải 8. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 79. Tổng thanh toán: 2k. Nếu giải ĐB hoặc giải 8 có 2 chữ số cuối là 79 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',85,2,1000,10000000000,2,'de_dauduoi',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',10),
(28,'Đầu','nam','dauduoi','	Đánh 1 chữ số hàng chục của giải ĐB. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 6. Tổng thanh toán: 1k. Nếu giải ĐB là xxxx6x thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',9,1,1000,10000000000,1,'dauduoi_dau',10,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',10),
(29,'Đuôi','nam','dauduoi','Đánh 1 chữ số cuối của giải ĐB. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 9. Tổng thanh toán: 1k. Nếu giải ĐB là xxxxx9 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',9,1,1000,10000000000,1,'dauduoi_duoi',10,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',10),
(30,'Đề đầu','nam','de','Đánh giải 8. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 79. Tổng thanh toán: 1k. Nếu giải 8 là 79 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',83,1,1000,10000000000,1,'de_dau',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',10),
(31,'Đề đặc biệt','nam','de','Đánh 2 chữ số cuối trong giải ĐB. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 79. Tổng thanh toán: 1k. Nếu giải ĐB là xxx79 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',83,1,1000,10000000000,1,'de_dacbiet',100,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',10),
(32,'Xỉu chủ đầu','nam','xiuchu','Đánh giải 7. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 879, Tổng thanh toán: 1k. Nếu giải 7 là 879 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}K',710,1,1000,10000000000,1,'xiuchu_dau',1000,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',10),
(33,'Xỉu chủ đuôi','nam','xiuchu','Đánh 3 chữ số cuối của giải ĐB. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 879, Tổng thanh toán: 1k. Nếu giải ĐB là xx879 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}K',710,1,1000,10000000000,1,'xiuchu_duoi',1000,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',10),
(34,'Xỉu chủ đầu - đuôi','nam','xiuchu','Đánh 3 chữ số cuối của giải ĐB và giải 7. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 879, Tổng thanh toán: 2k. Nếu giải ĐB hoặc giải 7 có 3 chữ số cuối là 879 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}k',710,2,1000,10000000000,1,'xiuchu_dauduoi',1000,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',10),
(35,'3 càng','bac','3cang','Đánh 3 chữ số cuối của giải ĐB. Thắng gấp {{ODDS}} lần. Ví dụ: đánh 1k cho số 879, Tổng thanh toán: 1k. Nếu giải ĐB là xx879 thì Tiền thắng: 1k x {{ODDS}} = {{ODDS}}K',710,1,1000,10000000000,1,'3cang',1000,1,'2019-08-18 00:40:12.000000','2019-08-18 00:40:12.000000',10);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
