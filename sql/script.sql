USE tornillo_feliz;

CREATE TABLE productos
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    unidad VARCHAR(255) NOT NULL,
    precio DECIMAL(8, 2) NOT NULL,
    stock INT NOT NULL
);
DROP TABLE clientes;
CREATE TABLE clientes
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    dni CHAR(8),
    nombre VARCHAR(255) NOT NULL,
    telefono VARCHAR(20),
    direccion VARCHAR(255),
    fecha DATETIME NOT NULL
);