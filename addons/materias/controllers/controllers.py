# -*- coding: utf-8 -*-
# from odoo import http


# class Materias(http.Controller):
#     @http.route('/materias/materias', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/materias/materias/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('materias.listing', {
#             'root': '/materias/materias',
#             'objects': http.request.env['materias.materias'].search([]),
#         })

#     @http.route('/materias/materias/objects/<model("materias.materias"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('materias.object', {
#             'object': obj
#         })

