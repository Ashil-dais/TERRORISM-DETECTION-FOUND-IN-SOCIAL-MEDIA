-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 03, 2021 at 05:19 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `honorcloud`
--

-- --------------------------------------------------------

--
-- Table structure for table `action`
--

CREATE TABLE IF NOT EXISTS `action` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL,
  `actions` varchar(50) NOT NULL,
  `sid` int(11) NOT NULL,
  `reason` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `action`
--

INSERT INTO `action` (`id`, `uid`, `actions`, `sid`, `reason`) VALUES
(11, 2, 'warn', 1, 'message');

-- --------------------------------------------------------

--
-- Table structure for table `comment`
--

CREATE TABLE IF NOT EXISTS `comment` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `cuid` int(11) NOT NULL,
  `date` varchar(20) NOT NULL,
  `comment` varchar(200) NOT NULL,
  `sid` int(11) NOT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `comment`
--

INSERT INTO `comment` (`cid`, `cuid`, `date`, `comment`, `sid`) VALUES
(1, 1, '2021-03-22 14:25:14.', 'pubg', 9),
(2, 1, '2021-03-22 14:25:49.', 'dark soul', 1),
(3, 1, '2021-03-22 14:30:06.', 'dark soul', 1),
(4, 1, '2021-03-22 14:34:24.', 'hi anonymus', 10),
(5, 1, '2021-03-22 16:06:40.', 'well', 10),
(6, 2, '2021-03-22 16:09:15.', 'hi', 10),
(7, 1, '2021-03-22 16:12:39.', 'good oone\r\n', 10),
(8, 6, '2021-11-02 15:53:40.', 'hello world , today i created magic with my voice in sima awards', 12);

-- --------------------------------------------------------

--
-- Table structure for table `complaints`
--

CREATE TABLE IF NOT EXISTS `complaints` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(200) NOT NULL,
  `date` varchar(20) NOT NULL,
  `userid` int(11) NOT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `complaints`
--

INSERT INTO `complaints` (`cid`, `description`, `date`, `userid`) VALUES
(1, 'its seems slow', '2021-03-26 15:42:56.', 1),
(2, 'I like it.', '2021-11-02 15:57:05.', 6),
(3, 'NO COMPLAINTS', '2021-11-03 09:56:00.', 6);

-- --------------------------------------------------------

--
-- Table structure for table `friends`
--

CREATE TABLE IF NOT EXISTS `friends` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `user1` varchar(30) NOT NULL,
  `user2` varchar(30) NOT NULL,
  `date` varchar(30) NOT NULL,
  `status` varchar(30) NOT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=14 ;

--
-- Dumping data for table `friends`
--

INSERT INTO `friends` (`fid`, `user1`, `user2`, `date`, `status`) VALUES
(1, 'x', 'y', '2021-12-15', 'accepted'),
(4, 'shyam@gmail.com', 'sonu@gmail.com', '2021-02-18 17:07:19.473609', 'accepted'),
(5, 'sonu@gmail.com', 'ma@gmail.com', '2021-12-15', 'accepted'),
(6, 'anu@gmail.com', 'sonu@gmail.com', '2021-03-06 13:01:28.290684', 'accepted'),
(7, 'anu@gmail.com', 'shyam@gmail.com', '2021-03-06 13:02:05.892756', 'accepted'),
(8, 'manu@gmail.com', 'sonu@gmail.com', '2021-03-30 16:42:40.440922', 'rejected'),
(9, 'manu@gmail.com', 'anu@gmail.com', '2021-03-30 16:42:45.506822', 'accepted'),
(10, 'manu@gmail.com', 'shyam@gmail.com', '2021-03-30 16:42:49.787878', 'accepted'),
(11, 'hari@gmail.com', 'shyam@gmail.com', '2021-11-02 15:55:34.043557', 'accepted'),
(12, 'hari@gmail.com', 'sonu@gmail.com', '2021-11-02 15:55:39.884295', 'pending'),
(13, 'hari@gmail.com', 'anu@gmail.com', '2021-11-02 15:55:59.453339', 'accepted');

-- --------------------------------------------------------

--
-- Table structure for table `likes`
--

CREATE TABLE IF NOT EXISTS `likes` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `luid` int(11) NOT NULL,
  `date` varchar(20) NOT NULL,
  `sid` int(11) NOT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `likes`
--


-- --------------------------------------------------------

--
-- Table structure for table `message`
--

CREATE TABLE IF NOT EXISTS `message` (
  `mid` int(11) NOT NULL AUTO_INCREMENT,
  `sent` varchar(100) NOT NULL,
  `receiver` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `msg` varchar(300) NOT NULL,
  PRIMARY KEY (`mid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=24 ;

--
-- Dumping data for table `message`
--

INSERT INTO `message` (`mid`, `sent`, `receiver`, `date`, `msg`) VALUES
(1, 'shyam@gmail.com', 'sonu@gmail.com', '2021-03-04', 'hai sonu'),
(2, 'shyam@gmail.com', 'sonu@gmail.com', '2021-03-04 16:44:25.667156', 'welcome'),
(3, 'sonu@gmail.com', 'shyam@gmail.com', '2021-03-04 16:44:36.075652', 'hi shyam'),
(4, 'shyam@gmail.com', 'sonu@gmail.com', '2021-03-04 17:33:42.791277', 'its nice to see you'),
(5, 'shyam@gmail.com', 'sonu@gmail.com', '2021-03-05 09:36:11.782408', 'welcome'),
(6, 'shyam@gmail.com', 'sonu@gmail.com', '2021-03-05 09:38:57.560530', 'hieooo'),
(7, 'shyam@gmail.com', 'sonu@gmail.com', '2021-03-05 09:40:48.366261', 'test'),
(8, 'shyam@gmail.com', 'sonu@gmail.com', '2021-03-05 09:41:23.044690', 'test22'),
(9, 'shyam@gmail.com', 'sonu@gmail.com', '2021-03-05 09:41:28.520885', 'test33'),
(10, 'sonu@gmail.com', 'shyam@gmail.com', '2021-03-05 11:23:27.554240', 'its good to see you'),
(11, 'shyam@gmail.com', 'sonu@gmail.com', '2021-03-06 10:30:25.417117', 'hello dr'),
(12, 'anu@gmail.com', 'shyam@gmail.com', '2021-03-09 12:45:12.675404', 'hi dr'),
(13, 'anu@gmail.com', 'sonu@gmail.com', '2021-03-09 12:45:19.387169', 'hi hubb'),
(14, 'shyam@gmail.com', 'anu@gmail.com', '2021-03-09 12:45:43.635003', 'hi lo'),
(15, 'sonu@gmail.com', 'shyam@gmail.com', '2021-03-17 16:03:40.214426', 'good morning'),
(16, 'sonu@gmail.com', 'shyam@gmail.com', '2021-03-17 16:03:48.802074', 'good morning'),
(17, 'sonu@gmail.com', 'shyam@gmail.com', '2021-03-31 14:28:42.332606', 'hi'),
(18, 'sonu@gmail.com', 'anu@gmail.com', '2021-03-31 14:28:57.190929', 'hi'),
(19, 'hari@gmail.com', 'shyam@gmail.com', '2021-11-03 09:53:32.437202', 'hai'),
(20, 'hari@gmail.com', 'shyam@gmail.com', '2021-11-03 09:53:40.692905', 'hello'),
(21, 'shyam@gmail.com', 'hari@gmail.com', '2021-11-03 09:54:23.000277', 'HAI'),
(22, 'hari@gmail.com', 'anu@gmail.com', '2021-11-03 10:17:11.044915', 'hai'),
(23, 'hari@gmail.com', 'anu@gmail.com', '2021-11-03 10:18:11.014837', 'hello');

-- --------------------------------------------------------

--
-- Table structure for table `messagereport`
--

CREATE TABLE IF NOT EXISTS `messagereport` (
  `rmid` int(11) NOT NULL AUTO_INCREMENT,
  `user` varchar(50) NOT NULL,
  `reportedid` varchar(50) NOT NULL,
  `date` varchar(30) NOT NULL,
  `status` varchar(90) NOT NULL,
  PRIMARY KEY (`rmid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `messagereport`
--

INSERT INTO `messagereport` (`rmid`, `user`, `reportedid`, `date`, `status`) VALUES
(1, 'shyam@gmail.com', 'sonu@gmail.com', '2021-03-05 10:14:07.128384', ''),
(2, 'hari@gmail.com', 'anu@gmail.com', '2021-11-03 10:38:59.149559', 'action');

-- --------------------------------------------------------

--
-- Table structure for table `profile`
--

CREATE TABLE IF NOT EXISTS `profile` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(30) NOT NULL,
  `propic` varchar(100) NOT NULL,
  `address` varchar(30) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `dob` varchar(20) NOT NULL,
  `school` varchar(30) NOT NULL,
  `college` varchar(30) NOT NULL,
  `work` varchar(20) NOT NULL,
  `phone` varchar(15) NOT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `profile`
--

INSERT INTO `profile` (`pid`, `email`, `propic`, `address`, `gender`, `dob`, `school`, `college`, `work`, `phone`) VALUES
(1, '', '/media/du1.jpg', '', '', '', '', '', '', ''),
(2, 'sonu@gmail.com', '/media/118015626_1629663280572774_6096566250673353166_o.jpg', 'acadcad', 'Male', '1995-02-17', 'ihrd', 'icet', 'lcc', '7012228523'),
(3, 'shyam@gmail.com', '/media/wall-decal-bumper-sticker-car-png-favpng-jC83v5n1YAzWBT2HumbLZF0yj.jpg', 'adb', 'Female', '2000-02-11', 'sdac', 'as', 'asdcac', 'adcadv'),
(4, 'anu@gmail.com', '/media/asd%20(1)_T5TEkKi.jpg', 'ad', 'Female', '2021-03-02', 'mbits', 'baselious', 'ovrsearer', '09633710717'),
(5, 'manu@gmail.com', '/media/abt4.jpg', 'dhcbfc', 'Male', '2021-03-18', 'ise', 'ise', 'lcc', '7856932140'),
(6, 'hari@gmail.com', '/media/download_g6NiO0I.jfif', 'haris villa', 'Male', '2021-11-01', 'GHSS', 'CHMM', 'singer', '9061986542');

-- --------------------------------------------------------

--
-- Table structure for table `slikes`
--

CREATE TABLE IF NOT EXISTS `slikes` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `luid` int(11) NOT NULL,
  `date` varchar(100) NOT NULL,
  `sid` int(11) NOT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=21 ;

--
-- Dumping data for table `slikes`
--

INSERT INTO `slikes` (`lid`, `luid`, `date`, `sid`) VALUES
(3, 1, '2021-03-10 17:38:14.399119', 1),
(5, 1, '2021-03-10 17:42:57.112219', 8),
(6, 2, '2021-03-17 16:02:57.858311', 9),
(14, 2, '2021-03-22 16:11:39.604326', 10),
(15, 1, '2021-03-22 16:12:07.862821', 10),
(16, 1, '2021-03-24 09:30:16.539880', 11),
(17, 6, '2021-11-02 15:52:27.927172', 12),
(18, 6, '2021-11-02 15:52:32.363103', 8),
(19, 6, '2021-11-02 15:52:35.062754', 9),
(20, 6, '2021-11-02 15:52:39.483787', 7);

-- --------------------------------------------------------

--
-- Table structure for table `status`
--

CREATE TABLE IF NOT EXISTS `status` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `text` varchar(100) NOT NULL,
  `date` varchar(20) NOT NULL,
  `image` varchar(100) NOT NULL,
  `uid` int(11) NOT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `status`
--

INSERT INTO `status` (`sid`, `text`, `date`, `image`, `uid`) VALUES
(1, 'hi its', '2021-02-12 12:48:59.', '/media/4598812-minimalism-quote-usa-anonymous-guy-fawkes-mask-hoods-freedom-typography_hCMvvex.jpg', 1),
(3, 'random', '2021-02-15 12:50:10.', '/media/d1.jpg', 0),
(4, 'random', '2021-02-15 12:50:10.', '/media/d2.jpg', 0),
(5, 'random', '2021-02-15 12:50:10.', '/media/d3.webp', 0),
(6, 'random', '2021-02-15 12:50:10.', '/media/d4.jpg', 0),
(7, 'test for 3 its  very 3rd image', '2021-03-05 10:20:08.', '/media/asd%20(1)_eQ3XnQm.jpg', 1),
(8, 'great wall papers', '2021-03-05 10:21:50.', '/media/astronaut-wallpaper-hd-4k-101409.jpg', 1),
(9, 'sports', '2021-03-05 10:22:05.', '/media/1245700.jpg', 1),
(10, 'hi world', '2021-03-08 15:13:17.', '/media/40178256-anonymous-wallpapers.jpg', 2),
(11, 'hi', '2021-03-22 16:17:58.', '', 1),
(12, 'Wonderful Day in My Life', '2021-11-02 15:51:57.', '/media/download%20(1)_UcKbSeA.jfif', 6);

-- --------------------------------------------------------

--
-- Table structure for table `statusreport`
--

CREATE TABLE IF NOT EXISTS `statusreport` (
  `srid` int(11) NOT NULL AUTO_INCREMENT,
  `sid` int(11) NOT NULL,
  `reporterid` int(11) NOT NULL,
  `date` varchar(20) NOT NULL,
  PRIMARY KEY (`srid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `statusreport`
--

INSERT INTO `statusreport` (`srid`, `sid`, `reporterid`, `date`) VALUES
(1, 10, 1, '2021-03-24 09:48:51.'),
(3, 10, 1, '2021-03-24 09:53:55.'),
(4, 10, 1, '2021-03-24 09:54:30.'),
(5, 10, 1, '2021-03-24 09:55:26.'),
(6, 8, 6, '2021-11-03 10:45:49.'),
(7, 11, 6, '2021-11-03 10:46:34.');

-- --------------------------------------------------------

--
-- Table structure for table `userreg`
--

CREATE TABLE IF NOT EXISTS `userreg` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `fname` varchar(40) NOT NULL,
  `lname` varchar(40) NOT NULL,
  `email` varchar(40) NOT NULL,
  `password` varchar(40) NOT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `userreg`
--

INSERT INTO `userreg` (`uid`, `fname`, `lname`, `email`, `password`) VALUES
(1, 'shyam', 'Sasi', 'shyam@gmail.com', 'sa'),
(2, 'sonu', 'Sasi', 'sonu@gmail.com', 'sa'),
(3, 'anu', 'varghese', 'anu@gmail.com', 'anu'),
(4, 'anju', 'r', 'anju@gmail.com', 'anju'),
(5, 'manu', 'm', 'manu@gmail.com', 'manu'),
(6, 'Hari', 'Shankar', 'hari@gmail.com', 'hari');
