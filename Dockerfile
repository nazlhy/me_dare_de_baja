
FROM python:3.10-slim

#  directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos archivos de la app al contenedor
COPY operaciones.py .

# Instalamos Flask
RUN pip install flask

# puerto 5000  usa Flask
EXPOSE 5000

# Comando para arrancar la app
CMD ["python", "operaciones.py"]
