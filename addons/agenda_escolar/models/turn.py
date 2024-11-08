# -*- coding: utf-8 -*-

from odoo import models, fields, api

class turn(models.Model):
    _name = 'agenda_escolar.turn'
    _description = 'agenda_escolar.turn'
    
    name = fields.Char(string="Nombre", readonly=False, required=True, help='Introduzca el Nombre del turno')
    description = fields.Text(string="Descripcion", readonly=False, required=False, help='Introduzca la descripcion del turno')
    schedule_ids = fields.One2many('agenda_escolar.schedules', 'turn_id', string="Horarios")