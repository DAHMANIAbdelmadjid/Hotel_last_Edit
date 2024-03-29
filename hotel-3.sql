-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 29, 2024 at 01:03 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotel`
--

-- --------------------------------------------------------

--
-- Table structure for table `client`
--

CREATE TABLE `client` (
  `c_id` int(20) NOT NULL,
  `iden_num` int(20) NOT NULL,
  `c_name` varchar(60) NOT NULL,
  `c_ph_numer` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `client`
--

INSERT INTO `client` (`c_id`, `iden_num`, `c_name`, `c_ph_numer`) VALUES
(5, 938472, 'Morsli', 347829),
(6, 9283746, 'Rachid', 675744),
(8, 292983765, 'Dehmani Abdelmadjid', 867352);

-- --------------------------------------------------------

--
-- Table structure for table `consumption`
--

CREATE TABLE `consumption` (
  `cons_id` int(20) NOT NULL,
  `cnt` int(20) DEFAULT NULL,
  `ser_id` int(20) DEFAULT NULL,
  `c_id` int(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `reservation`
--

CREATE TABLE `reservation` (
  `res_id` int(20) NOT NULL,
  `check_in` datetime DEFAULT current_timestamp(),
  `check_out` date DEFAULT NULL,
  `c_id` int(20) DEFAULT NULL,
  `room_num` int(20) DEFAULT NULL,
  `payment` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reservation`
--

INSERT INTO `reservation` (`res_id`, `check_in`, `check_out`, `c_id`, `room_num`, `payment`) VALUES
(1, '2024-03-28 00:00:00', '2024-04-02', 5, 1, 49000),
(4, '2024-03-28 00:00:00', '2024-04-04', 8, 2, 68600),
(5, '2024-03-28 00:00:00', '2024-04-05', 6, 2, 78400);

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE `room` (
  `room_num` int(20) NOT NULL,
  `type` varchar(50) DEFAULT NULL,
  `price` int(30) DEFAULT NULL,
  `stat` varchar(50) DEFAULT NULL,
  `discount` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `room`
--

INSERT INTO `room` (`room_num`, `type`, `price`, `stat`, `discount`) VALUES
(1, 'Single bed', 9800, 'Available', '0%'),
(2, 'Single bed', 9800, 'Occupied', '0%');

-- --------------------------------------------------------

--
-- Table structure for table `service`
--

CREATE TABLE `service` (
  `ser_id` int(20) NOT NULL,
  `descp` varchar(50) DEFAULT NULL,
  `ser_price` int(60) DEFAULT NULL,
  `ser_discount` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `service`
--

INSERT INTO `service` (`ser_id`, `descp`, `ser_price`, `ser_discount`) VALUES
(1, 'Breakfast', 1000, '0%'),
(2, 'Lunch', 2500, '0%'),
(3, 'Dinner', 2500, '0%');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`c_id`),
  ADD UNIQUE KEY `iden_num` (`iden_num`);

--
-- Indexes for table `consumption`
--
ALTER TABLE `consumption`
  ADD PRIMARY KEY (`cons_id`),
  ADD KEY `c_id` (`c_id`),
  ADD KEY `ser_id` (`ser_id`);

--
-- Indexes for table `reservation`
--
ALTER TABLE `reservation`
  ADD PRIMARY KEY (`res_id`),
  ADD KEY `room_num` (`room_num`),
  ADD KEY `c_id` (`c_id`);

--
-- Indexes for table `room`
--
ALTER TABLE `room`
  ADD PRIMARY KEY (`room_num`);

--
-- Indexes for table `service`
--
ALTER TABLE `service`
  ADD PRIMARY KEY (`ser_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `client`
--
ALTER TABLE `client`
  MODIFY `c_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `consumption`
--
ALTER TABLE `consumption`
  MODIFY `cons_id` int(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `reservation`
--
ALTER TABLE `reservation`
  MODIFY `res_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `room`
--
ALTER TABLE `room`
  MODIFY `room_num` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `service`
--
ALTER TABLE `service`
  MODIFY `ser_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `consumption`
--
ALTER TABLE `consumption`
  ADD CONSTRAINT `consumption_ibfk_1` FOREIGN KEY (`c_id`) REFERENCES `client` (`c_id`),
  ADD CONSTRAINT `consumption_ibfk_2` FOREIGN KEY (`ser_id`) REFERENCES `service` (`ser_id`);

--
-- Constraints for table `reservation`
--
ALTER TABLE `reservation`
  ADD CONSTRAINT `reservation_ibfk_1` FOREIGN KEY (`room_num`) REFERENCES `room` (`room_num`),
  ADD CONSTRAINT `reservation_ibfk_2` FOREIGN KEY (`c_id`) REFERENCES `client` (`c_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
