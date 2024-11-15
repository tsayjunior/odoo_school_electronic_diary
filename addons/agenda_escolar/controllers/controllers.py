# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json
from werkzeug.exceptions import BadRequest, Unauthorized
import logging


class AgendaEscolar(http.Controller):
    @http.route('/agenda_escolar/agenda_escolar', auth='public')
    def index(self, **kw):
        return "hello"

    @http.route('/agenda_escolar/other_route1/<int:number>', auth='public', methods=['GET'])
    def other_route(self, number, **kw):
        return f"El número que enviaste es: {number}"


    @http.route('/agenda_escolar/get_first_user', auth='public', methods=['GET'])
    def other_route(self, **kw):
        # Buscar el primer usuario que se encuentre (sin importar el número que se pase)
        user = request.env['res.users'].search([], limit=1)
        
        if user:
            # Si el usuario existe, devolver su información
            return request.make_json_response({
                'status': 'ok',
                'user': {
                    'id': user.id,
                    'name': user.name,
                    'email': user.email,
                }
            })
        else:
            # Si no se encuentra ningún usuario, devolver un mensaje de error
            return request.make_json_response({
                'status': 'error',
                'message': 'No hay usuarios disponibles',
            })
    

    @http.route('/agenda_escolar/agenda_escolar/objects', auth='public')
    def list(self, **kw):
        return http.request.render('agenda_escolar.listing', {
            'root': '/agenda_escolar/agenda_escolar',
            'objects': http.request.env['agenda_escolar.agenda_escolar'].search([]),
        })

    @http.route('/agenda_escolar/agenda_escolar/objects/<model("agenda_escolar.agenda_escolar"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('agenda_escolar.object', {
            'object': obj
        })



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


class UserController(http.Controller):

    @http.route(['/user/<int:user_id>'], type='http', auth='public', methods=['GET'])
    def get_user_by_id(self, user_id):
        """
        Devuelve el usuario correspondiente al ID proporcionado.
        """
        # Obtener el usuario con el ID dado
        user = request.env['res.users'].sudo().search([('id', '=', user_id)], limit=1)

        # Si no se encuentra el usuario, retornar error
        if not user:
            return request.make_json_response({
                'status': 'error',
                'code': 404,
                'message': 'Usuario no encontrado',
            }, 404)

        # Preparar los datos del usuario
        user_data = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'login': user.login,
            'is_active': user.active,
        }

        # Retornar respuesta en formato JSON
        return request.make_json_response({
            'status': 'ok',
            'code': 200,
            'data': user_data,
        })