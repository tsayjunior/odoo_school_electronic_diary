FROM odoo:18.0

# Cambia a root para asegurarte de que tengas los permisos adecuados
# Declarar la variable ARG
ARG ENVIRONMENT

# Cambiar a root si estamos en el entorno de producción
# si la variable ENVIRONMENT que está en mi archivo .env es igual a production, se ejecutará el codigo USER root 
RUN if [ "$ENVIRONMENT" = "production" ]; then \
        echo "Setting user to root"; \
        USER root; \
    fi

# Copiar el script al contenedor
COPY ./init-addons.sh /init-addons.sh

# No cambiar permisos, solo copiar
CMD ["bash", "/init-addons.sh"]
