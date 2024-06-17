-- phpMyAdmin SQL Dump
-- version 4.7.1
-- https://www.phpmyadmin.net/
--
-- Servidor: sql10.freemysqlhosting.net
-- Tiempo de generación: 17-06-2024 a las 16:22:10
-- Versión del servidor: 5.5.62-0ubuntu0.14.04.1
-- Versión de PHP: 7.0.33-0ubuntu0.16.04.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sql10712305`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `menu`
--

CREATE TABLE `menu` (
  `plato` varchar(60) NOT NULL DEFAULT '',
  `descripcion` varchar(160) DEFAULT NULL,
  `precio` float DEFAULT NULL,
  `imagenes` varchar(80) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `menu`
--

INSERT INTO `menu` (`plato`, `descripcion`, `precio`, `imagenes`) VALUES
('Bife a la Parrilla con Papas', 'Un suculento corte de carne a la parrilla, cocido a la perfección, acompañado de papas doradas y sazonadas con hierbas frescas', 30, 'menu-2.jpg'),
('Cheesecake Frutos Rojos', 'Suave y cremoso cheesecake sobre una base crujiente, coronado con una mezcla de frutos rojos frescos y una ligera salsa de frambuesa', 20, 'menu-1.jpg'),
('Crème Brûlée', 'Un clásico postre francés con una base de crema suave y sabor a vainilla, cubierto con una capa crujiente de azúcar caramelizado', 24, 'menu-10.jpg'),
('Crêpes de Dulce de Leche', 'Delicados crepes finos y esponjosos, rellenos con dulce de leche artesanal, servidos con una pizca de azúcar impalpable', 15, 'menu-6.jpg'),
('Filete Mignon con Salsa de Trufas', 'Un jugoso filete mignon, perfectamente cocido y cubierto con una rica salsa de trufas, acompañado de un puré de papas cremoso', 60, 'menu-2.jpg'),
('Mousse de Malbec', 'Una suave mousse de Malbec, acompañada de una reducción de frutos rojos frescos, que aporta un toque de acidez y dulzura perfectamente equilibrados', 20, 'menu-7.jpg'),
('Pescado a la Parrilla con Ensalada', 'Un filete de pescado fresco a la parrilla, acompañado de una ensalada crujiente con verduras de temporada y aderezo de limón', 20, 'menu-5.jpg'),
('Ravioles de Langosta', 'Ravioles hechos a mano, rellenos de langosta fresca y servidos con una salsa de mantequilla y limón, decorados con hierbas frescas', 30, 'menu-9.jpg');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `menu`
--
ALTER TABLE `menu`
  ADD PRIMARY KEY (`plato`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
