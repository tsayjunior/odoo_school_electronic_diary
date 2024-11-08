# -*- coding: utf-8 -*-

from odoo import models, fields, api

class level(models.Model):
    _name = 'agenda_escolar.level'
    _description = 'agenda_escolar.level'
    
    name = fields.Char(string="Nombre", readonly=False, required=True, help='Introduzca el Nombre del nivel')

    course_ids = fields.One2many('agenda_escolar.course', 'level_id', string="Cursos")

