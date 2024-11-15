# -*- coding: utf-8 -*-

from odoo import models, fields, api

class schedules(models.Model):
    _name = 'agenda_escolar.schedules'
    _description = 'agenda_escolar.schedules'

    date_init = fields.Float(string="Hora de inicio", required=True, help="Hora de inicio en formato decimal (Ej: 8.5 para 8:30 AM)")
    date_finish = fields.Float(string="Hora de finalización", required=True, help="Hora de finalización en formato decimal (Ej: 17.0 para 5:00 PM)")
    turn_id = fields.Many2one('agenda_escolar.turn', string="Turno", help="Seleccione el turno asociado")

    name = fields.Char(string="Horario", compute="_compute_name", store=True)

    def _float_to_time_string(self, float_hour):
        """Convierte un número decimal a una cadena de hora en formato HH:MM."""
        hours = int(float_hour)
        minutes = int((float_hour - hours) * 60)
        return f"{hours:02d}:{minutes:02d}"

    @api.depends('date_init', 'date_finish', 'turn_id.name')
    def _compute_name(self):
        for record in self:
            turno_name = record.turn_id.name if record.turn_id else "Sin turno"
            start_time = self._float_to_time_string(record.date_init)
            end_time = self._float_to_time_string(record.date_finish)
            record.name = f"{turno_name}: {start_time} - {end_time}"