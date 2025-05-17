# API de Operaciones Matemáticas

Este proyecto es una pequeña API creada con Flask que permite realizar operaciones matemáticas básicas (suma, resta, multiplicación y división) 

1. Instala Flask:

ejecutar con python operaciones.py

Accede a la API en postman
POST = http://localhost:5000/operacion.
ejemplo de json
{
  "num1": 10,
  "num2": 5,
  "operacion": "suma" (resta, multiplicacion o division)
}

GET = http://localhost:5000/operacion?num1=10&num2=5&operacion=division (suma, resta, multiplicacion)


ejecutar con Docker
imagen:
docker build -t operaciones-api .

contenedor:
docker run -p 5000:5000 operaciones-api


