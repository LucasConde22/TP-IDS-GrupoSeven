FROM python:3.9

# establece el directorio de trabajo en /app
WORKDIR /app

# copia todos los archivos del directorio TP_IDS
COPY . .

# instala los requisitos del proyecto
RUN pip install -r frontend/src/requirements.txt

# copia el archivo start que corre la app.py y la api.py y le da permisos
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

# Expone los puertos necesarios
EXPOSE 8000
EXPOSE 5001

# se corre la pagina
CMD ["/app/start.sh"]
