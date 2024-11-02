#!/bin/bash

# para darle permiso de superusario para el servidor
# sudo su

# Esperar a que el contenedor de base de datos esté listo
echo "Esperando a que el contenedor de base de datos esté listo..."
until pg_isready -h db -U $USER; do
    sleep 2
done

# Generar el archivo de configuración odoo.conf con la ruta de addons
echo "Creando el archivo de configuración odoo.conf..."
cat <<EOL > /etc/odoo/odoo.conf
[options]
; This is the default configuration file for Odoo
addons_path = /mnt/extra-addons
dbhost = db
dbport = 5432
dbuser = $USER
db_password = $PASSWORD
logfile = /var/log/odoo/odoo-server.log
log_handler = :DEBUG
log_level = debug
EOL

# Ejecutar el servidor de Odoo
echo "Iniciando Odoo..."
exec /entrypoint.sh odoo
