-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Sep 20, 2023 at 11:59 AM
-- Server version: 8.0.31
-- PHP Version: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `qlbhdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `cthd`
--

DROP TABLE IF EXISTS `cthd`;
CREATE TABLE IF NOT EXISTS `cthd` (
  `SOHD` int DEFAULT NULL,
  `MASP` varchar(4) DEFAULT NULL,
  `SL` int DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `cthd`
--

INSERT INTO `cthd` (`SOHD`, `MASP`, `SL`) VALUES
(1001, 'BC01', 5),
(1001, 'BC02', 10),
(1001, 'ST01', 5),
(1001, 'ST08', 10),
(1001, 'TV02', 10),
(1002, 'BB01', 20),
(1002, 'BB02', 20),
(1002, 'BC04', 20),
(1003, 'BB03', 10),
(1004, 'TV01', 20),
(1004, 'TV02', 10),
(1004, 'TV03', 10),
(1004, 'TV04', 10),
(1005, 'TV05', 50),
(1005, 'TV06', 50),
(1006, 'ST01', 30),
(1006, 'ST02', 10),
(1006, 'TV07', 20),
(1007, 'ST03', 10),
(1008, 'ST04', 8),
(1009, 'ST05', 10),
(1010, 'ST04', 50),
(1010, 'ST07', 50),
(1010, 'ST08', 100),
(1010, 'TV03', 100),
(1010, 'TV07', 50),
(1011, 'ST06', 50),
(1012, 'ST07', 3),
(1013, 'ST08', 5),
(1014, 'BB01', 50),
(1014, 'BB02', 100),
(1014, 'BC02', 80),
(1014, 'BC04', 60),
(1015, 'BB02', 30),
(1015, 'BB03', 7),
(1016, 'TV01', 5),
(1017, 'TV02', 1),
(1017, 'TV03', 1),
(1017, 'TV04', 5),
(1018, 'ST04', 6),
(1019, 'ST05', 1),
(1019, 'ST06', 2),
(1020, 'ST07', 10),
(1021, 'ST08', 5),
(1021, 'TV01', 7),
(1021, 'TV02', 10),
(1022, 'ST07', 1),
(1023, 'ST04', 6);

-- --------------------------------------------------------

--
-- Table structure for table `hoadon`
--

DROP TABLE IF EXISTS `hoadon`;
CREATE TABLE IF NOT EXISTS `hoadon` (
  `SOHD` int DEFAULT NULL,
  `NGHD` varchar(10) DEFAULT NULL,
  `MAKH` varchar(4) DEFAULT NULL,
  `MANV` varchar(4) DEFAULT NULL,
  `TRIGIA` int DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `hoadon`
--

INSERT INTO `hoadon` (`SOHD`, `NGHD`, `MAKH`, `MANV`, `TRIGIA`) VALUES
(1001, '2006-07-23', 'KH01', 'NV01', 320000),
(1002, '2006-08-12', 'KH01', 'NV02', 840000),
(1003, '2006-08-23', 'KH02', 'NV01', 100000),
(1004, '2006-09-01', 'KH02', 'NV01', 180000),
(1005, '2006-10-20', 'KH01', 'NV02', 3800000),
(1006, '2006-10-16', 'KH01', 'NV03', 2430000),
(1007, '2006-10-28', 'KH03', 'NV03', 510000),
(1008, '2006-10-28', 'KH01', 'NV03', 440000),
(1009, '2006-10-28', 'KH03', 'NV04', 200000),
(1010, '2006-11-01', 'KH01', 'NV01', 5200000),
(1011, '2006-11-04', 'KH04', 'NV03', 250000),
(1012, '2006-11-30', 'KH05', 'NV03', 21000),
(1013, '2006-12-12', 'KH06', 'NV01', 5000),
(1014, '2006-12-31', 'KH03', 'NV02', 3150000),
(1015, '2007-01-01', 'KH06', 'NV01', 910000),
(1016, '2007-01-01', 'KH07', 'NV02', 12500),
(1017, '2007-01-02', 'KH08', 'NV03', 35000),
(1018, '2007-01-13', 'KH08', 'NV03', 330000),
(1019, '2007-01-13', 'KH01', 'NV03', 30000),
(1020, '2007-01-14', 'KH09', 'NV04', 70000),
(1021, '2007-01-16', 'KH10', 'NV03', 67500),
(1022, '2007-01-16', 'KH10', 'NV03', 7000),
(1023, '2007-01-17', 'KH09', 'NV01', 330000);

-- --------------------------------------------------------

--
-- Table structure for table `khachhang`
--

DROP TABLE IF EXISTS `khachhang`;
CREATE TABLE IF NOT EXISTS `khachhang` (
  `MAKH` varchar(4) DEFAULT NULL,
  `HOTEN` varchar(14) DEFAULT NULL,
  `DCHI` varchar(31) DEFAULT NULL,
  `SODT` int DEFAULT NULL,
  `NGSINH` varchar(10) DEFAULT NULL,
  `NGDK` varchar(10) DEFAULT NULL,
  `DOANHSO` int DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `khachhang`
--

INSERT INTO `khachhang` (`MAKH`, `HOTEN`, `DCHI`, `SODT`, `NGSINH`, `NGDK`, `DOANHSO`) VALUES
('KH01', 'Nguyễn Văn A', '731 Trần Hưng Đạo, Q5, TpHCM', 8823451, '1960-10-22', '2006-07-22', 13060000),
('KH02', 'Trần Ngọc Hân', '23/5 Nguyễn Trãi, Q5, TpHCM', 908256478, '1974-04-03', '2006-07-30', 280000),
('KH03', 'Trần Ngọc Linh', '45 Nguyễn Cảnh Chân, Q1, TpHCM', 938776266, '1980-06-12', '2006-05-08', 3860000),
('KH04', 'Trần Minh Long', '50/34 Lê Đại Hành, Q10, TpHCM', 917325476, '1965-03-09', '2006-02-10', 250000),
('KH05', 'Lê Nhật Minh', '34 Trương Định, Q3, TpHCM', 8246108, '1950-03-10', '2006-10-28', 21000),
('KH06', 'Lê Hoài Thương', '227 Nguyễn Văn Cừ, Q5, TpHCM', 8631738, '1981-12-31', '2006-11-24', 915000),
('KH07', 'Nguyễn Văn Tâm', '32/3 Trần Bình Trọng, Q5, TpHCM', 916783565, '1971-04-06', '2006-01-12', 12500),
('KH08', 'Phan Thị Thanh', '45/2 An Dương Vương, Q5, TpHCM', 938435756, '1971-01-10', '2006-12-13', 365000),
('KH09', 'Lê Hà Vinh', '873 Lê Hồng Phong, Q5, TpHCM', 8654763, '1979-09-03', '2007-01-14', 70000),
('KH10', 'Hà Duy Lập', '34/34B Nguyễn Trãi, Q1, TpHCM', 8768904, '1983-05-02', '2007-01-16', 67500);

-- --------------------------------------------------------

--
-- Table structure for table `nhanvien`
--

DROP TABLE IF EXISTS `nhanvien`;
CREATE TABLE IF NOT EXISTS `nhanvien` (
  `MANV` varchar(4) DEFAULT NULL,
  `HOTEN` varchar(21) DEFAULT NULL,
  `SODT` int DEFAULT NULL,
  `NGVL` varchar(10) DEFAULT NULL,
  `MATKHAU` int DEFAULT NULL,
  `VAITRO` varchar(9) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `nhanvien`
--

INSERT INTO `nhanvien` (`MANV`, `HOTEN`, `SODT`, `NGVL`, `MATKHAU`, `VAITRO`) VALUES
('NV01', 'Nguyễn Như Nhựt', 927345678, '2006-04-13', 123456, 'Quản lý'),
('NV02', 'Lê Thị Phi Yến', 987567390, '2006-04-21', 123456, 'Nhân viên'),
('NV03', 'Nguyễn Văn B', 997047382, '2006-04-27', 123456, 'Nhân viên'),
('NV04', 'Ngô Thanh Tuấn', 913758498, '2006-06-24', 123456, 'Nhân viên'),
('NV05', 'Nguyễn Thị Trúc Thanh', 918590387, '2006-07-20', 123456, 'Nhân viên');

-- --------------------------------------------------------

--
-- Table structure for table `sanpham`
--

DROP TABLE IF EXISTS `sanpham`;
CREATE TABLE IF NOT EXISTS `sanpham` (
  `MASP` varchar(4) DEFAULT NULL,
  `TENSP` varchar(17) DEFAULT NULL,
  `DVT` varchar(5) DEFAULT NULL,
  `NUOCSX` varchar(10) DEFAULT NULL,
  `GIA` int DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `sanpham`
--

INSERT INTO `sanpham` (`MASP`, `TENSP`, `DVT`, `NUOCSX`, `GIA`) VALUES
('BB01', 'Bút bi', 'cây', 'Việt Nam', 5000),
('BB02', 'Bút bi', 'cây', 'Trung Quốc', 7000),
('BB03', 'Bút bi', 'hộp', 'Thái Lan', 100000),
('BC01', 'Bút chì', 'cây', 'Singapore', 3000),
('BC02', 'Bút chì', 'cây', 'Singapore', 5000),
('BC03', 'Bút chì', 'cây', 'Việt Nam', 3500),
('BC04', 'Bút chì', 'hộp', 'Việt Nam', 30000),
('ST01', 'Sổ tay 500 trang', 'quyển', 'Trung Quốc', 40000),
('ST02', 'Sổ tay loại 1', 'quyển', 'Việt Nam', 55000),
('ST03', 'Sổ tay loại 2', 'quyển', 'Việt Nam', 51000),
('ST04', 'Sổ tay', 'quyển', 'Thái Lan', 55000),
('ST05', 'Sổ tay mỏng', 'quyển', 'Thái Lan', 20000),
('ST06', 'Phấn viết bảng', 'hộp', 'Việt Nam', 5000),
('ST07', 'Phấn không bụi', 'hộp', 'Việt Nam', 7000),
('ST08', 'Bông bảng', 'cái', 'Việt Nam', 1000),
('ST09', 'Bút long', 'cây', 'Việt Nam', 5000),
('ST10', 'Bút long', 'cây', 'Trung Quốc', 7000),
('TV01', 'Tập 100 giấy mỏng', 'quyển', 'Trung Quốc', 2500),
('TV02', 'Tập 200 giấy mỏng', 'quyển', 'Trung Quốc', 4500),
('TV03', 'Tập 100 giấy tốt', 'quyển', 'Việt Nam', 3000),
('TV04', 'Tập 200 giấy tốt', 'quyển', 'Việt Nam', 5500),
('TV05', 'Tập 100 trang', 'chục', 'Việt Nam', 23000),
('TV06', 'Tập 200 trang', 'chục', 'Việt Nam', 53000),
('TV07', 'Tập 100 trang', 'chục', 'Trung Quốc', 34000);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
