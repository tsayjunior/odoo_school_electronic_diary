# -*- coding: utf-8 -*-

from odoo import models, fields, api

class schedules(models.Model):
    _name = 'agenda_escolar.schedules'
    _description = 'agenda_escolar.schedules'

    date_init = fields.Datetime(string="Hora de inicio", required=True, help="Hora de inicio (formato: YYYY-MM-DD HH:MM:SS)")
    date_finish = fields.Datetime(string="Hora de finalización", required=True, help="Hora de finalización (formato: YYYY-MM-DD HH:MM:SS)")