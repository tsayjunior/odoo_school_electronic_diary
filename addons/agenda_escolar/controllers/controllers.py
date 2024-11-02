# -*- coding: utf-8 -*-
# from odoo import http


# class AgendaEscolar(http.Controller):
#     @http.route('/agenda_escolar/agenda_escolar', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

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

