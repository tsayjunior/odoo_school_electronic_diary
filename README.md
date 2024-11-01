# Proyecto Odoo con Docker

Este repositorio configura Odoo usando Docker y Docker Compose, con módulos personalizados en `addons`.

## Requisitos

- Docker
- Docker Compose

## Instalación

1. Clona el repositorio:
2. añadir dos carpetas al inicio proyecto, con nombre
    config
    log

para crear proyecto odoo, en docker, usando docker-compose

es necesario que tenga instalado docker
estando en el proyecto, abrir cmd, y ejecutar 
    docker-compose up -d

para empezar a crear modulo, desde la terminal de docker, en su parte web, nos dirigimos a la carpeta addons
	cd /mnt/extra-addons
luego ponemos los codigos
	odoo scaffold manage
donde manage, es el nombre del modulo o nombre de la carpeta, y esto me generara una carpeta con nombre manage, con todas las carpetas para desarrollar

nota: al momento de crear un modulo, tienes que estar como desarrollador en odoo, por que si no, no te aparece el modulo para seleccionar o instalar en oddo
nota: es necesario añadir en odoo.conf 

			addons_path = /mnt/extra-addons

para que se instale los nuevos modulos