# Librerias

* Python 3.6
* Django 3
* mysqlclient 1.4.6
* WeasyPrint

# ¿Cómo crear el ambiente de desarrollo?

1. Deberas tener instalado python 3.6 y pip3.
2. Clonar el repositorio.
3. Dentro del directorio del proyecto ejecutar pip3 install -r requirements.txt.
4. python3 manage.py makemigrations categorias gestion seguimiento usuarios.
5. python3 manage.py migrate.

# Crear un usuario de prueba para el administrador y ejecutar el sistema en desarrollo

```
$:\ python3 manage.py createsuperuser
```

```
$:\ python3 manage.py runserver
```