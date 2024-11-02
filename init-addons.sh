#!/bin/bash

# Esperar a que el contenedor de base de datos esté listo
echo "Esperando a que el contenedor de base de datos esté listo..."
until pg_isready -h db -U $USER; do
    sleep 2
done

# Asegúrate de que el directorio de configuración existe
CONFIG_DIR="/etc/odoo"
mkdir -p $CONFIG_DIR

# Generar el archivo de configuración odoo.conf con la ruta de addons
echo "Creando el archivo de configuración odoo.conf..."
cat <<EOL > $CONFIG_DIR/odoo.conf
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

# Asegúrate de que el archivo se creó correctamente
if [[ -f "$CONFIG_DIR/odoo.conf" ]]; then
    echo "El archivo de configuración odoo.conf se creó correctamente."
else
    echo "Error: No se pudo crear el archivo de configuración odoo.conf."
    exit 1
fi

# Ejecutar el servidor de Odoo
echo "Iniciando Odoo..."
exec /entrypoint.sh odoo
