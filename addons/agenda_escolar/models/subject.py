# -*- coding: utf-8 -*-

from odoo import models, fields, api

class subject(models.Model):
    _name = 'agenda_escolar.subject'
    _description = 'agenda_escolar.subject'
    
    name = fields.Char(string="Nombre", readonly=False, required=True, help='Introduzca el Nombre')
    description = fields.Text(string="Descripcion", readonly=False, required=False, help='Introduzca la descripcion')
    code = fields.Char(string="Codigo", readonly=False, required=True, help='Introduzca el codigo')
