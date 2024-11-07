# -*- coding: utf-8 -*-

from odoo import models, fields, api

class class_school(models.Model):
    _name = 'agenda_escolar.class_school'
    _description = 'agenda_escolar.class_school'
    
    name = fields.Char(string="Nombre", readonly=False, required=True, help='Introduzca el Nombre')
    description = fields.Text(string="Descripcion", readonly=False, required=False, help='Introduzca la descripcion')
    parallel = fields.Char(string="Paralelo", readonly=False, required=True, help='Introduzca el paralelo')
