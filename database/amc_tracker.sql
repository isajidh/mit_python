-- phpMyAdmin SQL Dump
-- version 3.5.2.2
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Feb 06, 2025 at 05:03 PM
-- Server version: 5.5.27
-- PHP Version: 5.4.7

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `amc_tracker`
--

-- --------------------------------------------------------

--
-- Table structure for table `amc`
--

CREATE TABLE IF NOT EXISTS `amc` (
  `auto_inc` int(10) NOT NULL AUTO_INCREMENT,
  `asset_serial` bigint(20) NOT NULL,
  `amc_signed_date` date NOT NULL,
  `amc_start_date` date NOT NULL,
  `amc_end_date` date NOT NULL,
  `charge_amount` double NOT NULL,
  `remarks` varchar(100) NOT NULL,
  `amc_signed_by` varchar(100) NOT NULL,
  `entered_on` datetime NOT NULL,
  `entered_by` varchar(10) NOT NULL,
  `approved_on` datetime NOT NULL,
  `approved_by` int(11) NOT NULL,
  `is_current` int(1) NOT NULL,
  PRIMARY KEY (`auto_inc`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=16 ;

--
-- Dumping data for table `amc`
--

INSERT INTO `amc` (`auto_inc`, `asset_serial`, `amc_signed_date`, `amc_start_date`, `amc_end_date`, `charge_amount`, `remarks`, `amc_signed_by`, `entered_on`, `entered_by`, `approved_on`, `approved_by`, `is_current`) VALUES
(1, 10, '2025-02-04', '2025-02-04', '2025-02-04', 15000, 'test', 'asff', '2025-02-04 18:14:40', '1294', '0000-00-00 00:00:00', 0, 0),
(2, 10, '2025-02-04', '2025-02-04', '2025-02-04', 458966, '154', '2454', '2025-02-04 18:26:42', '1294', '0000-00-00 00:00:00', 0, 0),
(3, 10, '2023-02-05', '2023-02-05', '2024-02-05', 12588, 'dfdsf', 'fsdf', '2025-02-05 18:38:30', '1294', '0000-00-00 00:00:00', 0, 0),
(4, 10, '2023-02-05', '2023-02-05', '2024-02-05', 12588, 'dfdsf', 'fsdf', '2025-02-05 18:38:33', '1294', '0000-00-00 00:00:00', 0, 0),
(5, 10, '2023-02-05', '2023-02-05', '2024-02-05', 12588, 'dfdsf', 'fsdf', '2025-02-05 18:38:39', '1294', '0000-00-00 00:00:00', 0, 0),
(6, 10, '2025-02-05', '2025-02-05', '2025-02-05', 243243, 'sdsds', 'dsf', '2025-02-05 18:42:57', '1294', '0000-00-00 00:00:00', 0, 0),
(7, 10, '2025-02-05', '2025-02-05', '2025-02-05', 243243, 'sdsds', 'dsf', '2025-02-05 18:43:29', '1294', '0000-00-00 00:00:00', 0, 0),
(8, 10, '2025-02-05', '2025-02-05', '2025-02-05', 34543543, '43534', '345435', '2025-02-05 18:49:03', '1294', '0000-00-00 00:00:00', 0, 0),
(9, 10, '2025-02-05', '2025-02-05', '2025-02-05', 3454354345, '43534', '345435', '2025-02-05 18:49:17', '1294', '0000-00-00 00:00:00', 0, 0),
(10, 10, '2025-02-05', '2025-02-05', '2025-02-05', 54335, '453543', '4535', '2025-02-05 18:55:46', '1294', '0000-00-00 00:00:00', 0, 0),
(11, 10, '2025-02-05', '2025-02-05', '2025-02-05', 54335, '453543', '4535', '2025-02-05 18:56:36', '1294', '0000-00-00 00:00:00', 0, 0),
(12, 10, '2025-02-05', '2025-02-05', '2025-02-05', 0, '', '', '2025-02-05 20:15:37', '1294', '0000-00-00 00:00:00', 0, 0),
(13, 10, '2025-02-05', '2025-02-05', '2025-02-05', 3335, '5435', '455', '2025-02-05 21:01:06', '1294', '0000-00-00 00:00:00', 0, 0),
(14, 27, '2025-02-06', '2023-02-06', '2024-02-06', 150000, '434', '43545', '2025-02-06 17:41:32', '2222', '0000-00-00 00:00:00', 0, 1),
(15, 10, '2025-02-06', '2025-02-06', '2025-02-06', 343, '243', '3434', '2025-02-06 21:24:32', '2222', '0000-00-00 00:00:00', 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `asset`
--

CREATE TABLE IF NOT EXISTS `asset` (
  `auto_inc` int(10) NOT NULL AUTO_INCREMENT,
  `asset_type` varchar(2) NOT NULL,
  `asset_sub_type` varchar(10) NOT NULL,
  `description` varchar(100) NOT NULL,
  `inventory_number` varchar(100) NOT NULL,
  `date_purchase` date NOT NULL,
  `purchase_price` decimal(10,0) NOT NULL,
  `vender_name` varchar(100) NOT NULL,
  `vender_address` varchar(200) NOT NULL,
  `vender_phone` varchar(20) NOT NULL,
  `asset_location` varchar(200) NOT NULL,
  `asset_owner` varchar(100) NOT NULL,
  `asset_custodian` varchar(100) NOT NULL,
  `depreciation_rate` decimal(10,0) NOT NULL,
  `entered_on` datetime NOT NULL,
  `entered_by` varchar(10) NOT NULL,
  `approved_on` datetime NOT NULL,
  `approved_by` int(11) NOT NULL,
  `deleted_on` datetime NOT NULL,
  `deleted_by` varchar(10) NOT NULL,
  `deleted` int(1) NOT NULL,
  `asset_serial` bigint(20) NOT NULL,
  PRIMARY KEY (`auto_inc`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=42 ;

--
-- Dumping data for table `asset`
--

INSERT INTO `asset` (`auto_inc`, `asset_type`, `asset_sub_type`, `description`, `inventory_number`, `date_purchase`, `purchase_price`, `vender_name`, `vender_address`, `vender_phone`, `asset_location`, `asset_owner`, `asset_custodian`, `depreciation_rate`, `entered_on`, `entered_by`, `approved_on`, `approved_by`, `deleted_on`, `deleted_by`, `deleted`, `asset_serial`) VALUES
(1, '12', '12-004', '45435', '5454', '0000-00-00', 45821, '4535', '4543', '43554', '43545', '435', '45435', 50, '0000-00-00 00:00:00', '', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 0),
(2, '12', '12-006', 'sfdsf', '3435dfd', '0000-00-00', 5446453, 'fdsf', 'dfdsf', 'df', 'dsf', 'fds', 'sdf', 33, '0000-00-00 00:00:00', '', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 0),
(3, '12', '12-006', 'sfdsf', '3435dfd', '0000-00-00', 5446453, 'fdsf', 'dfdsf', 'df', 'dsf', 'fds', 'sdf', 33, '0000-00-00 00:00:00', '', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 0),
(4, '12', '12-004', 'dfsfdsf', '3543545', '0000-00-00', 34, 'sfsf', 'dfdsf', 'sfds', 'asff', 'dsf', 'dsfds', 34, '0000-00-00 00:00:00', '', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 0),
(5, '12', '12-006', 'sfdsfsd', '435435', '0000-00-00', 35525245, 'dsfds', 'dfsdsf', 'dfsf', 'dsfsd', 'sdf', 'dsf', 34, '0000-00-00 00:00:00', '', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 0),
(6, '12', '12-004', 'sdfdsfds', '56465645', '0000-00-00', 4354545, 'fdsf', 'dsfdsf', 'dfsds', 'asdfa', 'afdd', 'fdfs', 5454, '0000-00-00 00:00:00', '', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 0),
(7, '13', '13-004', 'dfdsf', 'rerrdrdr', '0000-00-00', 455877, 'dfdsf', 'dsfd', '0708000749', 'dfdf', 'dsf', 'fsdf', 33, '0000-00-00 00:00:00', '', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 0),
(8, '13', '13-004', 'ewrwerew', '5435', '0000-00-00', 3435454, '5435', '435', '435', '43', '435', '254', 4554, '0000-00-00 00:00:00', '', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 0),
(9, '12', '12-006', 'ewr', '32343', '0000-00-00', 3424, '234', '242', '243', '24', '24', '24', 24, '0000-00-00 00:00:00', '', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 1),
(10, '12', '12-005', '324324', '34324', '0000-00-00', 23432, '32432', '23432', '4324', '243', '243', '2432', 2423, '2025-02-04 08:17:06', '1294', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 2),
(11, '12', '12-005', '324324', '34324', '0000-00-00', 23432, '32432', '23432', '4324', '243', '243', '2432', 2423, '2025-02-04 08:18:14', '1294', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 3),
(12, '13', '13-005', '2432', '4324', '0000-00-00', 23432, '234324', '34234', '3242', '234', '234', '234', 243, '2025-02-04 08:28:36', '1294', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 4),
(13, '12', '12-005', '3453', '4354', '2025-02-04', 43543, '3453', '245', '345', '345', '345', '35', 345, '2025-02-04 08:37:25', '1294', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 5),
(14, '12', '12-005', 'fdsfs', '564656454', '2025-02-04', 234324, '32432', '324', '234', '234', '234', '234', 234, '2025-02-04 09:04:25', '1294', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 6),
(15, '12', '12-005', 'werr', '354', '2025-02-04', 4324, '34232', '324', '324', '234', '234', '243', 23, '2025-02-04 10:11:10', '1294', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 7),
(16, '12', '12-002', 'fsdf', '45896', '2024-02-04', 2424, 'dfsf', 'dfsdf', '3255645', 'wrewr', 'ewrer', 'erwerwe', 34, '2025-02-04 10:32:55', '1294', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 8),
(17, '12', '12-002', 'fsdf', '458965', '2024-02-04', 2424, 'dfsf', 'dfsdf', '3255645', 'wrewr', 'ewrer', 'erwerwe', 34, '2025-02-04 10:33:18', '1294', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 9),
(18, '12', '12-003', '6564', '45656', '2025-02-04', 456, '456456', '54', '456', '456', '456', '456', 56, '2025-02-04 11:00:35', '1294', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 10),
(19, '13', '13-005', '5435', '543534', '2025-02-04', 45, '453', '435', '345', '435', '345', '345', 45, '2025-02-04 11:02:36', '1294', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 11),
(20, '12', '12-003', '43543', '4543', '2025-02-04', 345, '', '', '', '', '', '', 34, '2025-02-04 12:10:58', '1294', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 12),
(21, '12', '12-008', '5434', '3434', '2025-02-12', 2566, 'rtr', 'rete', '454544', 'retert', 'rtrre', 'rttetr', 35, '2025-02-05 17:51:45', '1294', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 13),
(22, '13', '13-004', 'etrtre', '546565', '2024-02-16', 45453, 'retret', 'treterte', '0718000749', 'gdfgg', 'gfdgfg', 'fgdfg', 36, '2025-02-05 17:56:20', '1294', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 14),
(23, '13', '13-004', 'etrtre', '5465655', '2024-02-16', 45453, 'retret', 'treterte', '0718000749', 'gdfgg', 'gfdgfg', 'fgdfg', 36, '2025-02-05 17:57:16', '1294', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 15),
(24, '13', '13-004', 'etrtre', '54656556', '2024-02-16', 45453, 'retret', 'treterte', '0718000749', 'gdfgg', 'gfdgfg', 'fgdfg', 36, '2025-02-05 17:57:23', '1294', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 16),
(25, '13', '13-004', 'etrtre', '546565564', '2024-02-16', 45453, 'retret', 'treterte', '0718000749', 'gdfgg', 'gfdgfg', 'fgdfg', 36, '2025-02-05 17:58:49', '1294', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 17),
(26, '13', '13-005', 'dsfs', '15454', '2023-02-05', 124545, 'sfdsdf', 'sdfdf', '12548', 'df', 'sdf', 'sdf', 15, '2025-02-05 18:05:38', '1294', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 18),
(27, '12', '12-003', '345345', '543535', '2022-02-05', 435345, '3454534', '45435', '4353435', '435435', '43543', '34534', 34, '2025-02-05 18:09:33', '1294', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 19),
(28, '13', '13-004', '45435', '543556', '2022-12-12', 345435, '34543', '34534', '345', '345', '435', '43543', 34, '2025-02-05 18:30:58', '1294', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '2025-02-06', 1, 20),
(29, '12', '12-003', '4555', '2556', '2025-02-05', 12568, 'fsdfsf', 'sdfsdf', '54545', 'dsffds', 'sdfsdf', 'dsfdsf', 36, '2025-02-05 18:35:20', '1294', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 21),
(30, '12', '12-009', '45435', '543556', '2022-12-12', 345435, '34543', '34534', '345', '345', '435', '43543', 34, '2025-02-06 04:45:35', '1294', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 22),
(31, '13', '13-004', '45435', '543556', '2022-12-12', 345435, '34543', '34534', '345', '345', '435', '43543', 34, '2025-02-06 04:47:00', '1294', '0000-00-00 00:00:00', 0, '2025-02-06 21:23:22', '2222', 1, 23),
(32, '11', '11-006', '45435', '543556', '2020-12-11', 345435, '34543', '34534', '345', '345', '435', '43543', 34, '2025-02-06 04:49:16', '1294', '0000-00-00 00:00:00', 0, '2025-02-06 04:51:29', '1294', 1, 20),
(33, '11', '11-006', '45435', '543556', '2018-12-20', 345435, '34543', '34534', '345', '345', '435', '43543', 34, '2025-02-06 04:51:29', '1294', '0000-00-00 00:00:00', 0, '2025-02-06 04:54:18', '1294', 1, 20),
(34, '17', '17-004', '45435', '543556', '2018-12-20', 345435, '34543', '34534', '345', '345', '435', '43543', 34, '2025-02-06 04:54:18', '1294', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 20),
(35, '12', '12-004', '45878', '45896565', '2025-02-06', 458966, '4587', '454', '45454', '45445', '45454', '4588', 12, '2025-02-06 10:25:11', '2222', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 24),
(36, '12', '12-003', '4345', 'we344', '2025-02-06', 453, '34543', '55', '53535', '345435', '3453535', '435345', 45, '2025-02-06 10:40:03', '2222', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 25),
(37, '12', '12-004', '344', 'sfdsf125', '2025-02-06', 35, '43534', '435', '435', '4353', '4354', '35', 45, '2025-02-06 10:44:49', '2222', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 26),
(38, '17', '17-005', '545', '34554455', '2025-02-06', 43435, 'ewrr', 'rewr', '334453', '3545', '4342', '432', 33, '2025-02-06 17:38:57', '2222', '0000-00-00 00:00:00', 0, '2025-02-06 17:40:09', '2222', 1, 27),
(39, '17', '17-004', '545', '34554455', '2023-02-10', 43435, 'ewrr', 'rewr', '334453', '3545', '4342', '432', 30, '2025-02-06 17:40:09', '2222', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 27),
(40, '13', '13-005', '4354', '353', '2025-02-06', 455, '453', '435', '453', '435', '4535', '435', 33, '2025-02-06 21:23:03', '2222', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 28),
(41, '13', '13-004', '45435', '543556', '2022-12-12', 345435, '34543', '34534', '345', '345', '435', '43543', 35, '2025-02-06 21:23:22', '2222', '0000-00-00 00:00:00', 0, '0000-00-00 00:00:00', '', 0, 23);

-- --------------------------------------------------------

--
-- Table structure for table `asset_sub_type`
--

CREATE TABLE IF NOT EXISTS `asset_sub_type` (
  `auto_inc` int(10) NOT NULL AUTO_INCREMENT,
  `type` varchar(2) NOT NULL,
  `sub_type` varchar(10) NOT NULL,
  `description` varchar(100) NOT NULL,
  PRIMARY KEY (`auto_inc`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=91 ;

--
-- Dumping data for table `asset_sub_type`
--

INSERT INTO `asset_sub_type` (`auto_inc`, `type`, `sub_type`, `description`) VALUES
(9, '11', '11-001', 'Computers (Desktops, Laptops,Workstations)'),
(10, '11', '11-001', 'Computers (Desktops, Laptops, Workstations)'),
(11, '11', '11-002', 'Servers (Physical and Virtual)'),
(12, '11', '11-003', 'Network Equipment:'),
(13, '11', '11-004', 'Routers'),
(14, '11', '11-005', 'Switches'),
(15, '11', '11-006', 'Firewalls'),
(16, '11', '11-007', 'Load Balancers'),
(17, '11', '11-008', 'Storage Devices:'),
(18, '11', '11-009', 'External Hard Drives'),
(19, '11', '11-010', 'NAS (Network Attached Storage)'),
(20, '11', '11-011', 'SAN (Storage Area Network)'),
(21, '11', '11-012', 'Peripheral Devices:'),
(22, '11', '11-013', 'Monitors'),
(23, '11', '11-014', 'Keyboards'),
(24, '11', '11-015', 'Mice'),
(25, '11', '11-016', 'Printers'),
(26, '11', '11-017', 'Scanners'),
(27, '11', '11-018', 'Mobile Devices:'),
(28, '11', '11-019', 'Smartphones'),
(29, '11', '11-020', 'Tablets'),
(30, '11', '11-021', 'Backup Devices:'),
(31, '11', '11-022', 'Tape Drives'),
(32, '11', '11-023', 'Backup Servers'),
(33, '11', '11-024', 'Data Center Equipment:'),
(34, '11', '11-025', 'Power Distribution Units (PDUs)'),
(35, '11', '11-026', 'Cooling Systems'),
(36, '11', '11-027', 'Racks and Enclosures'),
(37, '11', '11-028', 'Audio/Video Equipment:'),
(38, '11', '11-029', 'Projectors'),
(39, '11', '11-030', 'Video Conferencing Systems'),
(40, '11', '11-031', 'Televisions'),
(42, '12', '12-002', 'Operating Systems (Windows, Linux, macOS)'),
(43, '12', '12-003', 'Productivity Tools (Microsoft Office, Google Workspace)'),
(44, '12', '12-004', 'Development Tools (IDEs, Code Editors, Debugging Tools)'),
(45, '12', '12-005', 'Database Management Systems (MySQL, Oracle, MongoDB)'),
(46, '12', '12-006', 'Virtualization Software (VMware, Hyper-V, VirtualBox)'),
(47, '12', '12-007', 'IT Management Software:'),
(48, '12', '12-008', 'Asset Management Tools'),
(49, '12', '12-009', 'Help Desk Software'),
(50, '12', '12-010', 'Network Monitoring Tools (Nagios, SolarWinds)'),
(51, '12', '12-011', 'Cybersecurity Tools:'),
(52, '12', '12-012', 'Antivirus/Anti-malware'),
(53, '12', '12-013', 'Endpoint Protection Software'),
(54, '12', '12-014', 'SIEM (Security Information and Event Management) Tools'),
(55, '12', '12-015', 'Collaboration Tools (Slack, Microsoft Teams, Zoom)'),
(56, '12', '12-016', 'Licensed Applications (ERP, CRM, HR Software)'),
(58, '13', '13-002', 'IP Addresses (Assigned to devices)'),
(59, '13', '13-003', 'Subnets'),
(60, '13', '13-004', 'VLANs (Virtual LANs)'),
(61, '13', '13-005', 'Domain Names'),
(62, '13', '13-006', 'DNS Records'),
(64, '14', '14-002', 'Virtual Machines'),
(65, '14', '14-003', 'Cloud Storage (AWS S3, Google Drive, Azure Blob Storage)'),
(66, '14', '14-004', 'SaaS Applications'),
(67, '14', '14-005', 'Cloud Databases'),
(68, '14', '14-006', 'Cloud Networking (VPNs, Virtual Routers)'),
(70, '15', '15-002', 'Firewalls (Physical and Software-based)'),
(71, '15', '15-003', 'Intrusion Detection and Prevention Systems (IDS/IPS)'),
(72, '15', '15-004', 'Encryption Tools (SSL/TLS Certificates, VPNs)'),
(73, '15', '15-005', 'Multi-Factor Authentication (MFA) Tools'),
(74, '15', '15-006', 'Access Control Systems (Physical and Digital)'),
(76, '16', '16-002', 'User Data'),
(77, '16', '16-003', 'Backups and Archives'),
(78, '16', '16-004', 'Configuration Files'),
(79, '16', '16-005', 'Logs (System Logs, Application Logs)'),
(80, '16', '16-006', 'Documentation (Technical Manuals, Policies)'),
(82, '17', '17-002', 'Toner and Ink Cartridges'),
(83, '17', '17-003', 'Network Cables'),
(84, '17', '17-004', 'Spare Components (e.g., RAM, Hard Drives)'),
(85, '17', '17-005', 'Batteries (For Laptops, UPS)'),
(87, '18', '18-002', 'Licenses (Software, Hardware, Cloud Services)'),
(88, '18', '18-003', 'IT Furniture (Server Racks, Cable Management Systems)'),
(89, '18', '18-004', 'Test and Diagnostic Tools (Network Analyzers, Multimeters)'),
(90, '18', '18-005', 'SSL Certificate');

-- --------------------------------------------------------

--
-- Table structure for table `asset_type`
--

CREATE TABLE IF NOT EXISTS `asset_type` (
  `auto_inc` int(10) NOT NULL AUTO_INCREMENT,
  `type` varchar(2) NOT NULL,
  `description` varchar(100) NOT NULL,
  PRIMARY KEY (`auto_inc`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `asset_type`
--

INSERT INTO `asset_type` (`auto_inc`, `type`, `description`) VALUES
(1, '11', 'Hardware Assets'),
(2, '12', 'Software Assets'),
(3, '13', 'Network Assets'),
(4, '14', 'Cloud-Based Assets'),
(5, '15', 'Security Assets'),
(6, '16', 'Data Assets'),
(7, '17', 'Consumables'),
(8, '18', 'Miscellaneous Assets');

-- --------------------------------------------------------

--
-- Table structure for table `serial`
--

CREATE TABLE IF NOT EXISTS `serial` (
  `code` varchar(2) NOT NULL,
  `serial` bigint(20) NOT NULL,
  `description` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `serial`
--

INSERT INTO `serial` (`code`, `serial`, `description`) VALUES
('1', 28, 'Asset Serial');

-- --------------------------------------------------------

--
-- Table structure for table `user_account`
--

CREATE TABLE IF NOT EXISTS `user_account` (
  `auto_inc` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(10) NOT NULL,
  `user_name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `role` int(11) NOT NULL,
  `created_by` varchar(10) NOT NULL,
  `created_on` date NOT NULL,
  `is_current` int(1) NOT NULL,
  `pw_expiry_date` date NOT NULL,
  `pw_period` int(11) NOT NULL,
  `pw_type` int(1) NOT NULL,
  `password` varchar(256) NOT NULL,
  PRIMARY KEY (`auto_inc`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `user_account`
--

INSERT INTO `user_account` (`auto_inc`, `user_id`, `user_name`, `email`, `phone`, `role`, `created_by`, `created_on`, `is_current`, `pw_expiry_date`, `pw_period`, `pw_type`, `password`) VALUES
(1, '1294', 'Karunarathna', 'madakala@gmail.com', '0718000749', 1, '1294', '2025-01-29', 1, '2025-07-28', 180, 0, '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'),
(2, '1111', 'Karunarathna', '', '', 1, '', '0000-00-00', 0, '0000-00-00', 0, 0, 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'),
(3, '2222', 'Samana', 'madakala@gmail.com', '12584', 1, '1294', '2025-02-05', 1, '2025-08-04', 180, 0, 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3');

-- --------------------------------------------------------

--
-- Table structure for table `user_login`
--

CREATE TABLE IF NOT EXISTS `user_login` (
  `Auto_Inc` int(11) NOT NULL AUTO_INCREMENT,
  `USER_ID` varchar(10) NOT NULL,
  `LOGIN_IP` varchar(20) NOT NULL,
  `LOGIN_TIME` datetime NOT NULL,
  `LOGIN_STATUS` varchar(1) NOT NULL,
  `LOGIN_ERR` int(2) DEFAULT NULL,
  `LOGOUT_TIME` datetime NOT NULL,
  PRIMARY KEY (`Auto_Inc`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
