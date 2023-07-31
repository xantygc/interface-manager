FROM python:3.9.17

RUN apt-get update && apt-get install -y graphviz

COPY . .

# Instala las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt


WORKDIR /interface_manager

# Expone el puerto 8000 (el puerto en el que se ejecutará el servidor Django)
EXPOSE 8000

# Ejecuta el comando para iniciar el servidor Django
 CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#CMD ["ls", "-altr"]
