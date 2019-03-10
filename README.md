# Envio Click test

## Instalación

Clonar repositorio

`git clone https://github.com/RedYaafte/envio_click.git`

Crear entorno virtual (linux)

`python3 -m venv myvenv`

Activar entorno virtual y entrar a la carpeta `envio_click`

Instalar `requirements.txt`

`pip install -r requirements.txt`

Entrar a la `carpeta envio_click` y ejecutar comando `./manage.py runserver` linux o `python manage.py runserver` en windows.

### Test A

API se encuentra en `http://localhost:8000/api/messagess/`

En esa ruta podras hacer un post para agregar un mensaje o con postman.

En la siguente ruta `http://localhost:8000/messagess/id/` podras descifrar el mensaje enviado. Deberas agegar el id de tu mensaje en la ruta.

### Test B

Se encuentra en `http://localhost:8000/xml-score/create/` ahí podras cargar tu archivo xml para posteriormente caulcular el número de lineas.