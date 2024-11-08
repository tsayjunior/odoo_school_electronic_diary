# -*- coding: utf-8 -*-

from odoo import models, fields, api

class schedules(models.Model):
    _name = 'agenda_escolar.schedules'
    _description = 'agenda_escolar.schedules'

    
    date_init = fields.Float(string="Hora de inicio", required=True, help="Hora de inicio en formato decimal (Ej: 8.5 para 8:30 AM)")
    date_finish = fields.Float(string="Hora de finalización", required=True, help="Hora de finalización en formato decimal (Ej: 17.0 para 5:00 PM)")
    turn_id = fields.Many2one('agenda_escolar.turn', string="Turno", help="Seleccione el turno asociado")