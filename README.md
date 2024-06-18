# Nexus Hotel

Trabajo práctico grupal de la materia Introducción al Desarrollo de Software - Cátedra Lanzillotta - Grupo Seven

## Descripción del proyecto
Nexus Hotel es un sitio web destinado a un servicio de hospedaje; la página permite a los usuarios registrarse, o en caso de tener cuenta hacer un _login_, realizar reservas, enviar consultas al staff, dejar una reseña de su estadía y ver todos los servicios que ofrece el hotel. 

**Consigna:** Ver en [Consigna](Consigna.pdf)

## Informe

Para más detalles ver [Informe](Informe.pdf)

## Instalación de dependencias

### Requisitos
- Python 3
- Flask
- Pip
- Pipenv
- Docker (opcional)
- Docker compose (opcional)

### Crear y activar Entorno Virtual

Para crear un entorno virtual utilizamos:
```bash
python3 -m venv .venv
```
Para activar el entorno virtual utilizamos:
```bash
source .venv/bin/activate
```
Si python 3 no se encuentra instalado, ejecutar los siguientes comandos:
```bash
sudo apt-get update
sudo apt-get install python3
```

### Instalar flask y librerías

Para instalar flask y las librerias necesarias ejecutar el siguiente comando dentro del E.V:
```bash
sh init.sh
```
Si pip no se encuentra instalado, ejecutar los siguientes comandos:
```bash
sudo apt-get update
sudo apt-get install python3-pip
```
Luego, para instalar pipenv, ejecutar los siguientes comandos:
```bash
pip install --upgrade pip
pip install pipenv
```

## Iniciar Página Web

**OBSERVACIÓN:** Para el correcto funcionamiento del comando debe estar posicionado en el directorio del proyecto

Para iniciar la  página web sin Docker ejecutar el siguiente comando:
```bash
sh start.sh
```

Para iniciar la página web con Docker ejecutar el siguiente comando:
```bash
docker-compose up
```
