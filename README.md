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
    docker-compose up -d

nota: al momento de crear un modulo, tienes que estar como desarrollador en odoo, por que si no, no te aparece el modulo para seleccionar o instalar en oddo
nota: es necesario añadir en odoo.conf 

			addons_path = /mnt/extra-addons

para que se instale los nuevos modulos, para que asi sepa donde encontrar los nuevos modulos

para empezar a crear modulo, desde la terminal de docker, en su parte web, nos dirigimos a la carpeta addons
	cd /mnt/extra-addons
luego ponemos los codigos
	odoo scaffold manage
donde manage, es el nombre del modulo o nombre de la carpeta, y esto me generara una carpeta con nombre manage, con todas las carpetas para desarrollar

