FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia todos los archivos 
COPY . .

# Instala los requisitos del proyecto
RUN pip install -r frontend/src/requirements.txt

COPY frontend/start.sh /app/start.sh
RUN chmod +x /app/start.sh

# Expone los puertos necesarios
EXPOSE 8000
EXPOSE 5001

RUN ls -l /app

CMD ["/app/start.sh"]
