-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.32-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para bddelivery
CREATE DATABASE IF NOT EXISTS `bddelivery` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */;
USE `bddelivery`;

-- Volcando estructura para tabla bddelivery.categoria
CREATE TABLE IF NOT EXISTS `categoria` (
  `idCategoria` int(11) NOT NULL AUTO_INCREMENT,
  `nombreCategoria` varchar(255) NOT NULL,
  PRIMARY KEY (`idCategoria`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- Volcando datos para la tabla bddelivery.categoria: ~11 rows (aproximadamente)
INSERT INTO `categoria` (`idCategoria`, `nombreCategoria`) VALUES
	(1, 'Ceramica'),
	(2, 'Textiles'),
	(3, 'Joyería'),
	(4, 'Madera'),
	(5, 'Cuero'),
	(6, 'Piedra'),
	(7, 'Tejidos'),
	(8, 'Cestas'),
	(9, 'Pinturas'),
	(10, 'Brocados'),
	(11, 'Instrumentos Musicales');

-- Volcando estructura para tabla bddelivery.cliente
CREATE TABLE IF NOT EXISTS `cliente` (
  `idCliente` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `direccion` varchar(255) DEFAULT NULL,
  `telefono` int(11) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`idCliente`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- Volcando datos para la tabla bddelivery.cliente: ~0 rows (aproximadamente)
INSERT INTO `cliente` (`idCliente`, `nombre`, `direccion`, `telefono`, `email`, `password`) VALUES
	(1, 'Juan Perez', 'Calle Falsa 123', 123456789, 'juan.perez@example.com', 'contraseña123'),
	(2, 'Ana Lopez', 'Av. Libertad 456', 987654321, 'ana.lopez@example.com', 'contraseña456'),
	(3, 'Carlos Ramirez', 'Calle 5 #789', 567123456, 'carlos.ramirez@example.com', 'contraseña789'),
	(4, 'Maria Fernandez', 'Calle Real 12', 345678901, 'maria.fernandez@example.com', 'contraseña321'),
	(5, 'Pedro Gomez', 'Calle Nueva 34', 234567890, 'pedro.gomez@example.com', 'contraseña654');

-- Volcando estructura para tabla bddelivery.delivery
CREATE TABLE IF NOT EXISTS `delivery` (
  `idDelivery` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `turno` varchar(50) NOT NULL,
  `email` varchar(255) NOT NULL,
  `estado` varchar(50) NOT NULL,
  `ubicacion` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`idDelivery`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- Volcando datos para la tabla bddelivery.delivery: ~0 rows (aproximadamente)
INSERT INTO `delivery` (`idDelivery`, `nombre`, `turno`, `email`, `estado`, `ubicacion`, `password`) VALUES
	(1, 'Luis Castro', 'Mañana', 'luis.castro@example.com', 'Activo', 'Zona 1', 'passwordluis'),
	(2, 'Sofia Martinez', 'Tarde', 'sofia.martinez@example.com', 'Activo', 'Zona 2', 'passwordsofia'),
	(3, 'Gabriel Soto', 'Noche', 'gabriel.soto@example.com', 'Inactivo', 'Zona 3', 'passwordgabriel'),
	(4, 'Elena Alvarez', 'Mañana', 'elena.alvarez@example.com', 'Activo', 'Zona 4', 'passwordelena'),
	(5, 'Javier Ruiz', 'Tarde', 'javier.ruiz@example.com', 'Inactivo', 'Zona 5', 'passwordjavier');

-- Volcando estructura para tabla bddelivery.detallepedido
CREATE TABLE IF NOT EXISTS `detallepedido` (
  `idDetalle` int(11) NOT NULL AUTO_INCREMENT,
  `idPedido` int(11) NOT NULL,
  `idProducto` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `subtotal` float NOT NULL,
  PRIMARY KEY (`idDetalle`),
  KEY `idPedido` (`idPedido`),
  KEY `idProducto` (`idProducto`),
  CONSTRAINT `detallepedido_ibfk_1` FOREIGN KEY (`idPedido`) REFERENCES `pedido` (`idPedido`),
  CONSTRAINT `detallepedido_ibfk_2` FOREIGN KEY (`idProducto`) REFERENCES `producto` (`idProducto`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- Volcando datos para la tabla bddelivery.detallepedido: ~0 rows (aproximadamente)
INSERT INTO `detallepedido` (`idDetalle`, `idPedido`, `idProducto`, `cantidad`, `subtotal`) VALUES
	(1, 1, 1, 2, 51),
	(2, 1, 4, 1, 60),
	(3, 2, 3, 1, 75),
	(4, 2, 8, 1, 20),
	(5, 3, 5, 3, 135),
	(6, 4, 7, 2, 110),
	(7, 5, 9, 1, 60),
	(8, 5, 10, 1, 80);

-- Volcando estructura para tabla bddelivery.pedido
CREATE TABLE IF NOT EXISTS `pedido` (
  `idPedido` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `estado` varchar(50) NOT NULL,
  `total` float NOT NULL,
  `idCliente` int(11) NOT NULL,
  PRIMARY KEY (`idPedido`),
  KEY `idCliente` (`idCliente`),
  CONSTRAINT `pedido_ibfk_1` FOREIGN KEY (`idCliente`) REFERENCES `cliente` (`idCliente`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- Volcando datos para la tabla bddelivery.pedido: ~0 rows (aproximadamente)
INSERT INTO `pedido` (`idPedido`, `fecha`, `estado`, `total`, `idCliente`) VALUES
	(1, '2024-11-01', 'Pendiente', 120, 1),
	(2, '2024-11-02', 'Completado', 80, 2),
	(3, '2024-11-03', 'Pendiente', 200, 3),
	(4, '2024-11-04', 'Completado', 150, 4),
	(5, '2024-11-05', 'Pendiente', 50, 5);

-- Volcando estructura para tabla bddelivery.producto
CREATE TABLE IF NOT EXISTS `producto` (
  `idProducto` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `descripcion` text NOT NULL,
  `precio` float NOT NULL,
  `descuento` float NOT NULL,
  `imagen` blob DEFAULT NULL,
  `stock` int(11) NOT NULL,
  `idCategoria` int(11) DEFAULT NULL,
  PRIMARY KEY (`idProducto`),
  KEY `idCategoria` (`idCategoria`),
  CONSTRAINT `producto_ibfk_1` FOREIGN KEY (`idCategoria`) REFERENCES `categoria` (`idCategoria`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- Volcando datos para la tabla bddelivery.producto: ~11 rows (aproximadamente)
INSERT INTO `producto` (`idProducto`, `nombre`, `descripcion`, `precio`, `descuento`, `imagen`, `stock`, `idCategoria`) VALUES
	(1, 'Vaso de Ceramica', 'Vaso hecho a mano con diseño artesanal', 25.5, 0, _binary '', 50, 1),
	(2, 'Manta Andina', 'Manta tejida con lana de alpaca', 40, 5, _binary '', 30, 2),
	(3, 'Anillo de Plata', 'Anillo artesanal con diseño unico en plata', 75, 10, _binary '', 20, 3),
	(4, 'Bolso de Cuero', 'Bolso elaborado a mano con cuero natural', 60, 0, _binary '', 15, 4),
	(5, 'Figura de Madera', 'Escultura tallada en madera de roble', 45, 0, _binary '', 25, 5),
	(6, 'Collar de Piedra', 'Collar con piedras semipreciosas de la region', 35, 0, _binary '', 40, 6),
	(7, 'Tejido en Telar', 'Frazada tejida a mano en telar tradicional', 55, 0, _binary '', 35, 7),
	(8, 'Cesta de Mimbre', 'Cesta tejida a mano con fibras naturales', 20, 0, _binary '', 50, 8),
	(9, 'Cuadro Pintado a Mano', 'Cuadro con pintura tradicional de la region', 60, 0, _binary '', 10, 9),
	(10, 'Brocado Andino', 'Prenda tejida a mano con brocado tradicional', 80, 0, _binary '', 20, 10),
	(11, 'Charango Artesanal', 'Instrumento musical hecho a mano de madera y cuerdas', 120, 0, _binary '', 5, 11);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
