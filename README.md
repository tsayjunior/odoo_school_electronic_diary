# Proyecto Odoo con Docker

Este repositorio configura Odoo usando Docker y Docker Compose, con módulos personalizados en `addons`.

## Requisitos

- Docker
- Docker Compose

## Instalación

1. Clona el repositorio:

para crear proyecto odoo, en docker, usando docker-compose

es necesario que tenga instalado docker
1. primero debe crear el archivo .env, copiando el archivo .env.example, donde solo quedará .env como nombre del archivo
luego los datos se deben modificar a gusto

2. luego estando en el proyecto, abrir cmd, y ejecutar 
    
    - docker-compose up -d

donde -d es para que se ejecute en segundo plano

esto anterior es para cuando se quiere ejecutar los contenedores con todos los servicios ya definidos,

o si se quiere indicar a docker compose que primero debe construir las imagenes de los contenedores antes de iniciar los servicios. Esto es especialmente útil si has realizado cambios en tu Dockerfile o en los archivos que se copian a la imagen (por ejemplo, el código fuente de tu aplicación). Sin esta opción, Docker Compose usaría las imágenes existentes en caché, lo que significa que no verías tus cambios reflejados en los contenedores a menos que fueras explícitamente a reconstruir las imágenes.
por lo que se debe ejecutar la siguiente linea es para ejecutar con el dockerfile ingresado
    
    - docker-compose up -d --build


nota: al momento de crear un modulo, tienes que estar como desarrollador en odoo, por que si no, no te aparece el modulo para seleccionar o instalar en oddo
nota: es necesario añadir en odoo.conf

			addons_path = /mnt/extra-addons

para que se instale los nuevos modulos, para que asi sepa donde encontrar los nuevos modulos, esto en caso que no esté en la carpeta

para empezar a crear modulo, desde la terminal de docker, en su parte web, nos dirigimos a la carpeta addons
	cd /mnt/extra-addons
luego ponemos los codigos
	odoo scaffold manage
donde manage, es el nombre del modulo o nombre de la carpeta, y esto me generara una carpeta con nombre manage, con todas las carpetas para desarrollar


//////////////////////////////////////
otras configuraciones para config/odoo.config
logfile = /var/log/odoo/odoo-server.log => sirve para mostrar los logs del sistema, en un archivo de ruta especifica, en este caso en la carpeta log/odoo-server.log

log_handler = :DEBUG => sirve para iniciar el modo debug del sistema, para mostrar todos los mensaje en log, ya que odoo tiene como 5 tipos de mensajes, y en log solo muestra los de tipo importante, y si ponemos este codigo estará mostrando los 5 tipos
para el modo debug, de lo tiene que activar desde el sistema, entrando en ajustes y luego en activar modo desarrollador (con activo), el cual se encuentra casi en lo ultimo de ajustes

log_level = debug   => tambien sirve para mostrar el modo debug del sistema






para reiniciar el contenedor docker, solo la parte web, se ejecuta
        docker-compose restart web

ESTANDO EN LA RAIZ DEL PROYECTO