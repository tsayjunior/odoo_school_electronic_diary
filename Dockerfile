FROM odoo:18.0

# Copiar el script al contenedor
COPY ./init-addons.sh /init-addons.sh

# No cambiar permisos, solo copiar
CMD ["bash", "/init-addons.sh"]
