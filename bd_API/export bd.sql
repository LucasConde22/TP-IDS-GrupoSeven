-- phpMyAdmin SQL Dump
-- version 4.7.1
-- https://www.phpmyadmin.net/
--
-- Servidor: sql10.freemysqlhosting.net
-- Tiempo de generación: 18-06-2024 a las 12:53:02
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
-- Estructura de tabla para la tabla `administradores`
--

CREATE TABLE `administradores` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `usuario` varchar(30) CHARACTER SET utf8mb4 NOT NULL,
  `email` varchar(254) CHARACTER SET utf8mb4 NOT NULL,
  `contra` varchar(128) CHARACTER SET utf8mb4 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `administradores`
--

INSERT INTO `administradores` (`id`, `nombre`, `usuario`, `email`, `contra`) VALUES
(1, 'Administrador 1', 'admin1', 'administrador1@nexus.com', '12345678');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contacto`
--

CREATE TABLE `contacto` (
  `nombre` varchar(50) NOT NULL,
  `email` varchar(254) NOT NULL,
  `asunto` text NOT NULL,
  `mensaje` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `contacto`
--

INSERT INTO `contacto` (`nombre`, `email`, `asunto`, `mensaje`) VALUES
('Lucas Ariel Conde Cardó', 'lconde@fi.uba.ar', 'Consuta', 'Cómo hago una reserva?'),
('Lucas Ariel Conde Cardó', 'conde.cardo.lucas@gmail.com', 'Consulta sobre cómo llegar', 'Cómo llego al hotel?'),
('Juan', 'Juanma@gmail.com', 'Consulta', 'ejemplo consulta'),
('fsfsdfsd', 'fqfwqfqwf', 'wfqwfs', 'fsdfsdf'),
('Juan', 'Juanma@gmail.com', 'Consulta', 'gagassga'),
('Juanafas', 'Juanma@gmfsaail.com', 'fasConsulta', 'gagassga'),
('Juanafas', 'Juanma@gmfsaail.com', 'fasConsulta', 'gagassga'),
('Juanafas', 'Juanma@gmfsaail.com', 'fasConsulta', 'gagassga'),
('Juanafas', 'Juanma@gmfsaail.com', 'fasConsulta', 'asfas'),
('ll', 'll', 'll', 'llll'),
('Lola', 'lola@gmail.com', 'll', 'll'),
('', '', '', 'll'),
('', '', '', 'll'),
('', '', '', 'f'),
('', '', '', 'f'),
('', '', '', 'f'),
('', '', '', 'f'),
('', '', '', 'f'),
('', '', '', 'f'),
('', '', '', 'f'),
('', '', '', 'f'),
('', '', '', 'f'),
('', '', '', 'f'),
('', '', '', 'f'),
('', '', '', 'f'),
('', '', '', 'f'),
('', '', '', 'f'),
('', '', '', 'f'),
('', '', '', ''),
('', '', '', ''),
('', '', '', ''),
('', '', '', ''),
('', '', '', ''),
('', '', '', ''),
('', '', '', ''),
('', '', '', ''),
('', '', '', ''),
('', '', '', ''),
('Daniela', 'unemail@de.prueba.com', 'Una consultita', 'Hola! pregunta....'),
('', '', '', ''),
('', '', '', ''),
('', '', '', ''),
('', '', '', ''),
('', '345678', '3ertyui', 'dfghjk'),
('', '345678', '3ertyui', 'dfghjk'),
('', 'hola@gmail.com', '', 'ygOSIABC'),
('carlos', 'carlos123@gmail.com', '', 'hola'),
('Lola', 'llola@l', 'll', ''),
('Daniela Costa', 'unmail@de.prueba.com', 'Una consultita', 'Hola, quería consultar por ...'),
('Daniela Costa', 'unmail@de.prueba.com', 'Una consultita', 'LLLLLLLLLLLLL'),
('Daniela Costa', 'unmail@de.prueba.com', 'Una consultita', 'Un mensaje de consulta'),
('Juanafas', 'Juanma@gmfsaail.com', 'fasConsulta', 'sdg'),
('sdfsdg', 'sdgsdg@fdfs', 'sdgsdg', 'sdgsdg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `habitaciones`
--

CREATE TABLE `habitaciones` (
  `numero` int(11) NOT NULL,
  `tipo` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `opiniones`
--

CREATE TABLE `opiniones` (
  `id_opin` int(11) NOT NULL,
  `usuario` varchar(30) NOT NULL,
  `resena` varchar(400) NOT NULL,
  `rating` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `opiniones`
--

INSERT INTO `opiniones` (`id_opin`, `usuario`, `resena`, `rating`) VALUES
(1, 'test_usuario1', 'El hotel es muy lindo', 4),
(2, 'test_usuario2', 'Hermosa experiencia muy lindo lugar.', 5),
(3, 'test_usuario1', 'muy bueno el hotel', 5),
(5, 'Usuario De Prueba', 'buenisimoooo', 5),
(6, 'Usuario De Prueba', 'Muy lindo el hotel pero la comida es un poco cara', 4),
(7, 'Usuario De Prueba', 'prueba', 4),
(8, 'Lola', 'muy bueno!', 5),
(9, 'Usuario De Prueba', 'trhr', 3),
(10, 'Usuario De Prueba', 'muy bueno', 3),
(11, 'Usuario De Prueba', 'muy bueno', 3),
(12, 'Usuario De Prueba', 'eth', 3),
(13, 'Usuario De Prueba', 'bueno', 4),
(14, 'Usuario De Prueba', 'trj', 4),
(15, 'Usuario De Prueba', 'ydk', 3),
(16, 'Usuario De Prueba', 'muy buen hotel', 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `promociones`
--

CREATE TABLE `promociones` (
  `codigo` varchar(15) CHARACTER SET utf8mb4 NOT NULL,
  `tipo_habitacion` varchar(20) CHARACTER SET utf8mb4 NOT NULL,
  `descuento` int(11) NOT NULL,
  `inicio` datetime NOT NULL,
  `fin` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `promociones`
--

INSERT INTO `promociones` (`codigo`, `tipo_habitacion`, `descuento`, `inicio`, `fin`) VALUES
('IDS', 'simple', 10, '2024-06-12 00:00:00', '2024-06-30 00:00:00'),
('IDS', 'master', 10, '2024-06-12 00:00:00', '2024-06-30 00:00:00'),
('IDS', 'deluxe', 10, '2024-06-12 00:00:00', '2024-06-30 00:00:00'),
('NEXUS', 'deluxe', 25, '2024-06-12 00:00:00', '2024-06-30 00:00:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservas`
--

CREATE TABLE `reservas` (
  `numero` int(11) NOT NULL,
  `usuario` int(11) NOT NULL,
  `tipo_habitacion` varchar(20) NOT NULL,
  `habitacion` int(11) NOT NULL,
  `entrada` date NOT NULL,
  `salida` date NOT NULL,
  `valor` int(11) NOT NULL,
  `huespedes` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `reservas`
--

INSERT INTO `reservas` (`numero`, `usuario`, `tipo_habitacion`, `habitacion`, `entrada`, `salida`, `valor`, `huespedes`) VALUES
(33, 1, 'deluxe', 301, '2024-06-24', '2024-06-30', 480, 2),
(58, 1, 'master', 201, '2024-10-15', '2024-10-25', 350, 4),
(59, 1, 'master', 202, '2024-10-15', '2024-10-25', 350, 4),
(60, 1, 'master', 203, '2024-10-15', '2024-10-25', 315, 4),
(61, 2, 'deluxe', 301, '2024-10-20', '2024-10-25', 400, 4),
(62, 2, 'deluxe', 302, '2024-10-20', '2024-10-25', 300, 4),
(66, 1, 'deluxe', 301, '2024-06-13', '2024-06-24', 660, 6),
(68, 1, 'simple', 101, '2024-09-19', '2024-08-23', -608, 1),
(69, 1, 'simple', 102, '2024-09-19', '2024-09-23', 90, 1),
(70, 1, 'simple', 101, '2024-06-13', '2024-06-19', 150, 1),
(71, 9, 'simple', 102, '2024-06-13', '2024-06-14', 23, 1),
(76, 1, 'deluxe', 302, '2024-06-16', '2024-06-20', 320, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipos_habitaciones`
--

CREATE TABLE `tipos_habitaciones` (
  `tipo` varchar(20) NOT NULL,
  `caracteristicas` text NOT NULL,
  `capacidad` int(11) NOT NULL,
  `precio` int(11) NOT NULL,
  `foto1` text,
  `foto2` text,
  `foto3` text,
  `foto4` text,
  `video` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `usuario`, `email`, `contra`) VALUES
(1, 'Usuario De Prueba', 'test_usuario1', 'test_usuario1@ids.com', '12345678'),
(2, 'Usuario De Prueba 2', 'test_usuario2', 'abcd@qwerty.com', '12345678'),
(3, 'Lucas Ariel Conde Cardó', 'lucasconde_22', 'lconde@fi.uba.ar', '12345678'),
(8, 'Usuario de Prueba 3', 'test_usuario3', '123456789@abc.com', 'qwerty123'),
(9, 'Lola', 'Lola', 'lola@gmail.com', '123'),
(12, 'prueba2', 'prueba2', 'prueba@ll', '123'),
(13, '', '', 'hola@gmail.com', ''),
(14, 'Daniela Costa', 'un_usuario', 'unmail@de.prueba.com', '12345678'),
(15, 'Hugo Mendez', 'un_usuario2', 'unmail2@de.prueba.com', '12345678'),
(22, 'Brenda Fernández', 'un_usuario3', 'unmail3@de.prueba.com', '13245678'),
(24, 'Franco Pérez', 'un_usuario4', 'unmail4@de.prueba.com', '12345678'),
(25, 'Franco Pérez', 'un_usuario5', 'unmail5@de.prueba.com', '12345678'),
(26, 'Martina Riccardi', 'Martina_', 'martina@gmail.com', '12345678');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `administradores`
--
ALTER TABLE `administradores`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `habitaciones`
--
ALTER TABLE `habitaciones`
  ADD PRIMARY KEY (`numero`),
  ADD KEY `tipo_fk` (`tipo`);

--
-- Indices de la tabla `menu`
--
ALTER TABLE `menu`
  ADD PRIMARY KEY (`plato`);

--
-- Indices de la tabla `opiniones`
--
ALTER TABLE `opiniones`
  ADD PRIMARY KEY (`id_opin`);

--
-- Indices de la tabla `promociones`
--
ALTER TABLE `promociones`
  ADD KEY `tipo` (`tipo_habitacion`);

--
-- Indices de la tabla `reservas`
--
ALTER TABLE `reservas`
  ADD PRIMARY KEY (`numero`),
  ADD KEY `id_usuario` (`usuario`),
  ADD KEY `numero_habitacion` (`habitacion`),
  ADD KEY `tipo` (`tipo_habitacion`);

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
-- AUTO_INCREMENT de la tabla `administradores`
--
ALTER TABLE `administradores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT de la tabla `opiniones`
--
ALTER TABLE `opiniones`
  MODIFY `id_opin` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
--
-- AUTO_INCREMENT de la tabla `reservas`
--
ALTER TABLE `reservas`
  MODIFY `numero` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=79;
--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;
--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `habitaciones`
--
ALTER TABLE `habitaciones`
  ADD CONSTRAINT `habitaciones_ibfk_1` FOREIGN KEY (`tipo`) REFERENCES `tipos_habitaciones` (`tipo`);

--
-- Filtros para la tabla `promociones`
--
ALTER TABLE `promociones`
  ADD CONSTRAINT `promociones_ibfk_1` FOREIGN KEY (`tipo_habitacion`) REFERENCES `tipos_habitaciones` (`tipo`);

--
-- Filtros para la tabla `reservas`
--
ALTER TABLE `reservas`
  ADD CONSTRAINT `reservas_ibfk_1` FOREIGN KEY (`usuario`) REFERENCES `usuarios` (`id`),
  ADD CONSTRAINT `reservas_ibfk_2` FOREIGN KEY (`habitacion`) REFERENCES `habitaciones` (`numero`),
  ADD CONSTRAINT `reservas_ibfk_3` FOREIGN KEY (`tipo_habitacion`) REFERENCES `tipos_habitaciones` (`tipo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
