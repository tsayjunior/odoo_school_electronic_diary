# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json
from werkzeug.exceptions import BadRequest, Unauthorized
import logging


class AgendaEscolar(http.Controller):
    @http.route('/agenda_escolar/agenda_escolar', auth='public')
    def index(self, **kw):
        return "Hello, world"

#     @http.route('/agenda_escolar/agenda_escolar/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('agenda_escolar.listing', {
#             'root': '/agenda_escolar/agenda_escolar',
#             'objects': http.request.env['agenda_escolar.agenda_escolar'].search([]),
#         })

#     @http.route('/agenda_escolar/agenda_escolar/objects/<model("agenda_escolar.agenda_escolar"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('agenda_escolar.object', {
#             'object': obj
#         })



class AuthController(http.Controller):
    @http.route('/api/authenticate', type='json', auth='public', methods=['POST'])
    def authenticate_user(self, **post):
        # Registrar el contenido de `post` para ver qué se está recibiendo
        _logger = logging.getLogger(__name__)
        _logger.info("Datos recibidos en la solicitud: %s", post)
        username = post.get('username', None)  # Proporciona un valor predeterminado de None
        password = post.get('password', None)  # Lo mismo para el password
        if username is None or password is None:
            return {
                "jsonrpc": "2.0",
                "id": None,
                "result": {
                    "error": "username o password faltantes"
                }
            }
        # Verifica que los valores estén presentes
        if not username or not password:
            return {"error": "Username and password are required"}
        
        # Lógica de autenticación
        user = request.env['res.users'].search([('login', '=', 'estudiante3@example.com')], limit=1)
        users = request.env['res.users'].search([])
        # Convertimos los usuarios en una lista de diccionarios
        user_data = [{
            "id": user.id,
            "name": user.name,
            "login": user.login,
            "email": user.email,
        } for user in users]

        return {
            "message": "Authenticated successfully",
            "users": user_data,
        }
        _logger.info("**************************************************")
        _logger.info("Nombre usuario: %s", user.name)
        if user and user.check_credentials(password):
            return {
                "message": "Authenticated successfully",
                "user_id": user.id,
                "username": user.login
            }
        else:
            return {"error": "Invalid credentials"}