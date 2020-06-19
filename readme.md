# ¿Cómo crear el ambiente de desarrollo?

1. Deberas tener instalado python 3.6 y pip3.
2. Clonar el repositorio.
3. Dentro del directorio del proyecto ejecutar pip3 install -r requirements.txt.
4. python3 manage.py makemigrations categorias gestion seguimiento usuarios.
5. python3 manage.py migrate.

# Deploy con Nginx.

### Instalar y configurar Gunicorn para crear un servicio de nuestro proyecto.
``` bash
$:\ pip3 install -r requirements.txt
$:\ pip3 install gunicorn
```
### Crear el archivo ultra.service /etc/systemd/system/
``` bash
[Unit]
Description=Ultra daemon
After=network.target

[Service]
User=root
Group=nginx
WorkingDirectory=/applications/pyUltra
ExecStart=/usr/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/applications/ultra.sock \
          pyPartyou.wsgi:application

[Install]
WantedBy=multi-user.target
```
### Ahora vamos iniciar nuestro servicio.
``` bash
$:\ systemctl start ultra.service
```

### Configuramos Nginx
Tenemos que entrar en el directorio /etc/nginx/conf.d/ e cria o arquivo ultra.conf
``` bash
server {
    listen 80;
    server_name ultra.angelbejarano.dev;
    
   
    location /media/ {
        root /applications/pyPartyou;
    }

    location /static/ {
        root /applications/pyPartyou;
    }
    location / {
        include proxy_params;
        proxy_pass http://unix:/applications/ultra.sock;
        include fastcgi_params;
        fastcgi_cache_valid 200 60m;
    }
    
}
```

# Crear un usuario de prueba para el administrador y ejecutar el sistema en desarrollo

```
$:\ python3 manage.py createsuperuser
```

```
$:\ python3 manage.py runserver
```

