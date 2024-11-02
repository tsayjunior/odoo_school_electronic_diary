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
ESTANDO EN LA RAIZ DEL PROYECTO
        
        docker-compose restart web
        docker-compose restart db



----------------------------------------------------------------------------------------------
eliminar todos los contenedores de docker y sus volumenes, desde servidor

Para eliminar todos los contenedores y volúmenes en Docker, puedes usar los siguientes comandos:

Detener y eliminar todos los contenedores: Este comando detiene y elimina todos los contenedores en ejecución y detenidos:

docker rm -f $(docker ps -aq)

* docker ps -aq lista los ID de todos los contenedores.
* docker rm -f elimina cada contenedor listado, y el flag -f fuerza la eliminación.
Eliminar todos los volúmenes: Este comando elimina todos los volúmenes no utilizados, liberando espacio en disco:

docker volume rm $(docker volume ls -q)
* docker volume ls -q lista todos los volúmenes.
* docker volume rm elimina cada volumen listado.
Eliminar redes y otros recursos adicionales (opcional): Si deseas limpiar aún más el sistema, puedes eliminar también todas las redes no utilizadas y otros recursos con:

docker network prune -f
docker system prune -a --volumes -f
* docker network prune -f elimina todas las redes no utilizadas.
* docker system prune -a --volumes -f elimina contenedores detenidos, imágenes no usadas y volúmenes.
Con estos comandos, podrás liberar espacio y limpiar tu entorno Docker por completo.

////// para iniciar docker, desde comando en linux
Iniciar el servicio Docker: Ejecuta el siguiente comando para iniciar Docker:

    sudo systemctl start docker
* Habilitar Docker para que se inicie al arranque (opcional):

    sudo systemctl enable docker

* Verificar que Docker está corriendo:

    sudo systemctl status docker

* Confirmar que Docker está funcionando correctamente:

    docker info

Nota:
Asegúrate de tener los permisos necesarios para ejecutar estos comandos, especialmente en Linux, donde necesitas usar sudo.
Los comandos para iniciar Docker Desktop solo son aplicables si tienes Docker Desktop instalado; de lo contrario, en Linux solo necesitas iniciar el servicio.


***************** eliminar contendedores y volumenes en docker
    docker-compose down -v


*************** para dar permisos de escritura y lectura a init-addons.sh
    chmod +x init-addons.sh

    

