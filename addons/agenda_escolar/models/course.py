# -*- coding: utf-8 -*-

from odoo import models, fields, api

class course(models.Model):
    _name = 'agenda_escolar.course'
    _description = 'agenda_escolar.course'
    
    name = fields.Char(string="Nombre", readonly=False, required=True, help='Introduzca el Nombre')
    description = fields.Text(string="Descripcion", readonly=False, required=False, help='Introduzca la descripcion')
    parallel = fields.Char(string="Paralelo", readonly=False, required=True, help='Introduzca el paralelo')

    level_id = fields.Many2one('agenda_escolar.level', string="Nivel", help="Seleccione el Nivel")

    def action_open_subjects(self):
            """Abre la vista de lista de materias"""
            return {
                'name': 'Asignacion Materias',
                'type': 'ir.actions.act_window',
                'res_model': 'agenda_escolar.assign_subject',
                'view_mode': 'list,form',
                'target': 'current',
                'domain': [('course_id', '=', self.id)],  # Filtra la vista de lista por course_id actual
                'context': {
                    'default_course_id': self.id,  # Establece el course_id por defecto en el formulario de creación
            }
            }