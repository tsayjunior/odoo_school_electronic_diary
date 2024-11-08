# -*- coding: utf-8 -*-

from odoo import models, fields, api

class assign_subject(models.Model):
    _name = 'agenda_escolar.assign_subject'
    _description = 'agenda_escolar.assign_subject'
    
    
    course_id = fields.Many2one('agenda_escolar.course', string="curso", help="Seleccione el curso")
    subject_id = fields.Many2one('agenda_escolar.subject', string="materia", help="Seleccione materia")
    # teacher_id = fields.Many2one('agenda_escolar.teacher', string="docente", help="Seleccione docente")
    # Relación directa con res.partner en lugar de agenda_escolar.teacher
    teacher_id = fields.Many2one('res.partner', string="docente", domain=[('is_teacher', '=', True)], help="Seleccione docente")

    def action_open_schedules(self):
            """Abre la vista de lista de horarios"""
            return {
                'name': 'Asignacion Horarios',
                'type': 'ir.actions.act_window',
                'res_model': 'agenda_escolar.assign_schedules',
                'view_mode': 'list,form',
                'target': 'current',
                'domain': [('assign_subject_id', '=', self.id)],  # Filtra la vista de lista por assign_subject_id actual
                'context': {
                    'default_assign_subject_id': self.id,  # Establece el assign_subject_id por defecto en el formulario de creación
            }
            }
