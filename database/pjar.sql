-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jul 14, 2026 at 07:10 PM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pjar`
--

-- --------------------------------------------------------

--
-- Table structure for table `files`
--

CREATE TABLE `files` (
  `id` int NOT NULL,
  `filename` varchar(255) DEFAULT NULL,
  `filepath` varchar(255) DEFAULT NULL,
  `owner` varchar(100) DEFAULT NULL,
  `upload_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `files`
--

INSERT INTO `files` (`id`, `filename`, `filepath`, `owner`, `upload_time`) VALUES
(1, 'Screenshot 2026-06-30 161300.png', 'D:\\semester 8\\JARINGAN\\NetworkProgramming_Project\\storage\\files\\Screenshot 2026-06-30 161300.png', 'vrohim1907@gmail.com', '2026-07-14 09:51:34'),
(2, 'Soal_UAS_ATA_2026.pdf', 'D:\\semester 8\\JARINGAN\\NetworkProgramming_Project\\storage\\files\\Soal_UAS_ATA_2026.pdf', 'vrohim1907@gmail.com', '2026-07-14 09:53:02'),
(3, 'Screenshot 2026-06-30 161300.png', 'D:\\semester 8\\JARINGAN\\NetworkProgramming_Project\\storage\\files\\Screenshot 2026-06-30 161300.png', 'vrohim1907@gmail.com', '2026-07-14 09:58:14'),
(4, 'Screenshot 2026-06-30 161300.png', 'D:\\semester 8\\JARINGAN\\NetworkProgramming_Project\\storage\\files\\Screenshot 2026-06-30 161300.png', 'vrohim1907@gmail.com', '2026-07-14 10:01:11'),
(5, 'Screenshot 2026-06-30 161300.png', 'D:\\semester 8\\JARINGAN\\NetworkProgramming_Project\\storage\\files\\Screenshot 2026-06-30 161300.png', 'vrohim1907@gmail.com', '2026-07-14 10:02:19'),
(6, 'Screenshot 2026-06-30 161300.png', 'D:\\semester 8\\JARINGAN\\NetworkProgramming_Project\\storage\\files\\Screenshot 2026-06-30 161300.png', 'vrohim1907@gmail.com', '2026-07-14 10:09:29'),
(7, 'Screenshot 2026-06-30 161300.png', 'D:\\semester 8\\JARINGAN\\NetworkProgramming_Project\\storage\\files\\Screenshot 2026-06-30 161300.png', 'vrohim1907@gmail.com', '2026-07-14 10:10:16'),
(8, 'Screenshot 2026-06-30 161300.png', 'D:\\semester 8\\JARINGAN\\NetworkProgramming_Project\\storage\\files\\Screenshot 2026-06-30 161300.png', 'vrohim1907@gmail.com', '2026-07-14 10:25:12'),
(9, 'Screenshot 2026-06-30 161300.png', 'D:\\semester 8\\JARINGAN\\NetworkProgramming_Project\\storage\\files\\Screenshot 2026-06-30 161300.png', 'vrohim1907@gmail.com', '2026-07-14 10:25:41'),
(10, 'Screenshot 2026-06-30 161300.png', 'D:\\semester 8\\JARINGAN\\NetworkProgramming_Project\\storage\\files\\Screenshot 2026-06-30 161300.png', 'vrohim1907@gmail.com', '2026-07-14 11:35:14'),
(11, 'Screenshot 2026-06-30 161300.png', 'D:\\semester 8\\JARINGAN\\NetworkProgramming_Project\\storage\\files\\Screenshot 2026-06-30 161300.png', 'vrohim1907@gmail.com', '2026-07-14 16:59:34');

-- --------------------------------------------------------

--
-- Table structure for table `media`
--

CREATE TABLE `media` (
  `id` int NOT NULL,
  `filename` varchar(255) DEFAULT NULL,
  `filepath` varchar(255) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `owner` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `permission` tinyint(1) DEFAULT '0',
  `otp` varchar(10) DEFAULT NULL,
  `verified` tinyint(1) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `email`, `password`, `permission`, `otp`, `verified`) VALUES
(1, 'vrohim1907@gmail.com', '12345678', 1, NULL, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `files`
--
ALTER TABLE `files`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `media`
--
ALTER TABLE `media`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `files`
--
ALTER TABLE `files`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `media`
--
ALTER TABLE `media`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
