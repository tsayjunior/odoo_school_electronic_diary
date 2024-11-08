# -*- coding: utf-8 -*-

from odoo import models, fields, api

class assign_schedules(models.Model):
    _name = 'agenda_escolar.assign_schedules'
    _description = 'agenda_escolar.assign_schedules'
    
    
    day_id = fields.Many2one('agenda_escolar.day', string="dia", help="Seleccione el dia")
    schedules_id = fields.Many2one('agenda_escolar.schedules', string="Horario", help="Seleccione horario")
    assign_subject_id = fields.Many2one('agenda_escolar.assign_subject', string="materia asignada", help="Seleccione materia")

