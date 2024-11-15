# -*- coding: utf-8 -*-
from odoo import models, fields, api

class event(models.Model):
    _name = 'agenda_escolar.event'
    _description = 'agenda_escolar.event'
    
    name = fields.Char(string="Nombre", readonly=False, required=True, help='Introduzca el Nombre')
    description = fields.Text(string="Descripcion", readonly=False, required=False, help='Introduzca la descripcion')
    capacity = fields.Integer(string="Capacidad de Personas", help="Capacidad de Personas")
    place = fields.Text(string="Nombre del Lugar del Evento", help="Nombre del Lugar del Evento")
    date = fields.Date(string="Fecha del Evento", help="Fecha del Evento")
    start_time = fields.Float(string="Hora de inicio", required=True, help="Hora de inicio en formato decimal (Ej: 8.5 para 8:30 AM)")
    end_time = fields.Float(string="Hora de finalización", required=True, help="Hora de finalización en formato decimal (Ej: 17.0 para 5:00 PM)")
    state = fields.Selection([
        ('0', 'No Empezado'),
        ('1', 'Empezado'),
        ('2', 'Terminado')
    ], string='Estado', default='0')
    name_time = fields.Char(string="Horario", compute="_compute_name", store=True)
    image = fields.Binary("Imagen del Evento", help="Imagen relacionada con el evento", attachment=True)


    def action_open_comments(self):
            """Abre la vista de lista de materias"""
            return {
                'name': 'Comentarios',
                'type': 'ir.actions.act_window',
                'res_model': 'agenda_escolar.comment',
                'view_mode': 'list,form',
                'target': 'current',
                'domain': [('event_id', '=', self.id)],  # Filtra la vista de lista por course_id actual
                'context': {
                    'default_event_id': self.id,  # Establece el course_id por defecto en el formulario de creación
                }
            }
    
    def _float_to_time_string(self, float_hour):
        """Convierte un número decimal a una cadena de hora en formato HH:MM."""
        hours = int(float_hour)
        minutes = int((float_hour - hours) * 60)
        return f"{hours:02d}:{minutes:02d}"

    @api.depends('start_time', 'end_time')
    def _compute_name(self):
        for record in self:
            start_time = self._float_to_time_string(record.start_time)
            end_time = self._float_to_time_string(record.end_time)
            record.name_time = f"{start_time} - {end_time}"