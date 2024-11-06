# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class agenda_escolar(models.Model):
#     _name = 'agenda_escolar.agenda_escolar'
#     _description = 'agenda_escolar.agenda_escolar'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class teacher(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    type_for_school = fields.Char(default='Docente', string='Tipo')


class subject(models.Model):
    _name = 'agenda_escolar.subject'
    _description = 'agenda_escolar.subject'
    
    name = fields.Char(string="Nombre", readonly=False, required=True, help='Introduzca el Nombre')
    description = fields.Text(string="Descripcion", readonly=False, required=False, help='Introduzca la descripcion')
    code = fields.Char(string="Codigo", readonly=False, required=True, help='Introduzca el codigo')
