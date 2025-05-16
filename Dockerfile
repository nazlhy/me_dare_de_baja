# Usamos imagen oficial Python 3.10 ligera
FROM python:3.10-slim

# Establecemos directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos archivos de la app al contenedor
COPY operaciones.py .

# Instalamos Flask
RUN pip install flask

# Exponemos el puerto 5000 (el que usa Flask)
EXPOSE 5000

# Comando para arrancar la app
CMD ["python", "operaciones.py"]
