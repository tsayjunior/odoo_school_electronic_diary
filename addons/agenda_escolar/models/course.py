# -*- coding: utf-8 -*-

from odoo import models, fields, api

class course(models.Model):
    _name = 'agenda_escolar.course'
    _description = 'agenda_escolar.course'
    
    name = fields.Char(string="Nombre", readonly=False, required=True, help='Introduzca el Nombre')
    description = fields.Text(string="Descripcion", readonly=False, required=False, help='Introduzca la descripcion')
    parallel = fields.Char(string="Paralelo", readonly=False, required=True, help='Introduzca el paralelo')
    state = fields.Selection([
        ('0', 'En curso'),
        ('1', 'Finalizado')
    ], string='State', default='0')

    level_id = fields.Many2one('agenda_escolar.level', string="Nivel", help="Seleccione el Nivel")

    # Campo Many2many para los estudiantes inscritos en el curso
    student_ids = fields.Many2many(
        'res.partner',          # Modelo de destino
        'student_course_rel',   # Nombre de la tabla intermedia
        'course_id',            # Campo que apunta a 'agenda_escolar.course' (este modelo)
        'student_id',           # Campo que apunta a 'res.partner' (modelo relacionado)
        string='Estudiantes',
        domain=[('is_student', '=', True)]
    )

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