# -*- coding: utf-8 -*-

from odoo import models, fields, api

class day(models.Model):
    _name = 'agenda_escolar.day'
    _description = 'agenda_escolar.day'
    
    name = fields.Char(string="Nombre", readonly=False, required=True, help='Introduzca el Nombre del dia')
