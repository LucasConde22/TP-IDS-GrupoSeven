-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 05-06-2024 a las 03:01:10
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `tp_ids`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `habitaciones`
--

CREATE TABLE `habitaciones` (
  `numero` int(11) NOT NULL,
  `tipo` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `habitaciones`
--

INSERT INTO `habitaciones` (`numero`, `tipo`) VALUES
(301, 'deluxe'),
(302, 'deluxe'),
(201, 'master'),
(202, 'master'),
(203, 'master'),
(204, 'master'),
(205, 'master'),
(101, 'simple'),
(102, 'simple'),
(103, 'simple'),
(104, 'simple'),
(105, 'simple'),
(106, 'simple'),
(107, 'simple'),
(108, 'simple');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservas`
--

CREATE TABLE `reservas` (
  `numero` int(11) NOT NULL,
  `usuario` int(11) NOT NULL,
  `habitacion` int(11) NOT NULL,
  `entrada` date NOT NULL,
  `salida` date NOT NULL,
  `valor` int(11) NOT NULL,
  `huespedes` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `reservas`
--

INSERT INTO `reservas` (`numero`, `usuario`, `habitacion`, `entrada`, `salida`, `valor`, `huespedes`) VALUES
(14, 1, 101, '2024-10-01', '2024-10-10', 25, 0),
(15, 1, 102, '2024-10-01', '2024-10-10', 25, 0),
(16, 1, 301, '2024-10-20', '2024-10-30', 80, 0),
(17, 1, 302, '2024-10-20', '2024-10-30', 80, 0),
(21, 1, 201, '2024-10-15', '2024-10-25', 350, 0),
(22, 1, 202, '2024-10-15', '2024-10-25', 350, 0),
(23, 1, 101, '2024-06-24', '2024-06-30', 150, 0),
(24, 1, 201, '2024-07-10', '2024-07-17', 245, 0),
(25, 1, 101, '2024-05-30', '2024-06-05', 150, 0),
(26, 2, 103, '2024-09-13', '2024-10-16', 825, 0),
(27, 2, 301, '2024-06-05', '2024-06-07', 160, 0),
(28, 2, 201, '2024-06-12', '2024-07-04', 770, 2),
(29, 2, 202, '2024-06-06', '2024-06-22', 560, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipos_habitaciones`
--

CREATE TABLE `tipos_habitaciones` (
  `tipo` varchar(20) NOT NULL,
  `caracteristicas` text NOT NULL,
  `capacidad` int(11) NOT NULL,
  `precio` int(11) NOT NULL,
  `foto1` text DEFAULT NULL,
  `foto2` text DEFAULT NULL,
  `foto3` text DEFAULT NULL,
  `foto4` text DEFAULT NULL,
  `video` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tipos_habitaciones`
--

INSERT INTO `tipos_habitaciones` (`tipo`, `caracteristicas`, `capacidad`, `precio`, `foto1`, `foto2`, `foto3`, `foto4`, `video`) VALUES
('deluxe', 'Nuestras lujosas Habitaciones Deluxe ofrecen todo lo que necesita para unas vacaciones de ensueño. Con capacidad para hasta 6 personas, estas habitaciones incluyen todas las comodidades que puede necesitar, como baño privado, televisión por cable, Wi-Fi Gratis, teléfono, microondas y aire acondicionado. Además ofrecen impresionantes vistas al lago desde dos balcones privados. Disfrute de una cocina completa, jacuzzi privado y acceso exclusivo al cerro, donde podrá practicar deportes de nieve. Sumérjase en la experiencia definitiva de lujo y comodidad durante su estancia con nosotros. ', 6, 80, 'room-2.jpg', 'bathroom-2.jpg', 'room-6.jpg', 'room-2.jpg', 'video-hab.mp4'),
('master', 'Nuestra exclusiva Habitación Master es perfecta para hasta cuatro personas, con la flexibilidad de contar con 2 camas matrimoniales o 4 individuales. Este espacio excepcional ofrece todas las comodidades que puede necesitar, como baño privado, televisión por cable, Wi-Fi Gratis, teléfono, microondas y aire acondicionado. Además, las habitaciones Master poseen un balcón privado que brinda una vista impresionante al lago. Disfrute de una estancia inolvidable con acceso completo a todas las ammenities del complejo, como el gimnasio y la piscina.', 4, 35, 'room-8.jpg', 'room-9.jpg', 'bathroom-3.jpg', 'images/room-3.jpg', 'video-hab.mp4'),
('simple', 'Estas habitaciones, adecuadas para hasta dos personas, ofrecen una cama matrimonial o dos individuales. Son consideradas las habitaciones estándar del complejo, equipadas con baño privado, televisión por cable, teléfono, WI-FI, aire acondicionado y microondas. Además, los huéspedes tienen acceso a todas las comodidades del complejo, desayuno incluido, el gimnasio, la piscina, la sala de juegos, entre otros. Nexus Hotel cuenta con un total de ocho habitaciones de este tipo.', 2, 25, 'room-7.jpg', 'room-1.jpg', 'bathroom-1.jpg', 'images/room-5.jpg', 'video-hab.mp4');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `usuario` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `contra` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `usuario`, `email`, `contra`) VALUES
(1, 'Usuario De Prueba', 'test_usuario1', 'test_usuario1@ids.com', '12345678'),
(2, 'Usuario De Prueba 2', 'test_usuario2', 'abcd@qwerty.com', '12345678');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `habitaciones`
--
ALTER TABLE `habitaciones`
  ADD PRIMARY KEY (`numero`),
  ADD KEY `tipo_fk` (`tipo`);

--
-- Indices de la tabla `reservas`
--
ALTER TABLE `reservas`
  ADD PRIMARY KEY (`numero`),
  ADD KEY `id_usuario` (`usuario`),
  ADD KEY `numero_habitacion` (`habitacion`);

--
-- Indices de la tabla `tipos_habitaciones`
--
ALTER TABLE `tipos_habitaciones`
  ADD PRIMARY KEY (`tipo`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `reservas`
--
ALTER TABLE `reservas`
  MODIFY `numero` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `habitaciones`
--
ALTER TABLE `habitaciones`
  ADD CONSTRAINT `habitaciones_ibfk_1` FOREIGN KEY (`tipo`) REFERENCES `tipos_habitaciones` (`tipo`);

--
-- Filtros para la tabla `reservas`
--
ALTER TABLE `reservas`
  ADD CONSTRAINT `reservas_ibfk_1` FOREIGN KEY (`usuario`) REFERENCES `usuarios` (`id`),
  ADD CONSTRAINT `reservas_ibfk_2` FOREIGN KEY (`habitacion`) REFERENCES `habitaciones` (`numero`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
