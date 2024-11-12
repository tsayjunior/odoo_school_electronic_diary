# -*- coding: utf-8 -*-

from odoo import models, fields, api

class activity(models.Model):
    _name = 'agenda_escolar.activity'
    _description = 'agenda_escolar.activity'

    name = fields.Char(string="Nombre", readonly=False, required=True, help='Introduzca el Nombre')
    description = fields.Text(string="Descripcion", readonly=False, required=False, help='Introduzca la descripcion')
    date_activity = fields.Datetime(
        string="Fecha y hora de actividad ",
        required=True,
        help="Fecha y hora de actividad"
    )
    type = fields.Selection([
        ('0', 'Examen'),
        ('1', 'Tarea'),
        ('2', 'Otro')
    ], string='Tipo', default='0')

    state = fields.Selection([
        ('0', 'En curso'),
        ('1', 'Finalizado')
    ], string='Estado', default='0')
    
    has_note = fields.Selection([
        ('0', 'Con calificación'),
        ('1', 'Sin calificación')
    ], string='Calificación', default='0')
    
    teacher_id = fields.Many2one(
        'res.partner',
        string="Profesor",
        domain=[('is_teacher', '=', True)],
        help="Seleccione el Profesor"
    )
    
    course_id = fields.Many2one(
        'agenda_escolar.course',
        string="Curso",
        help="Seleccione el Curso"
    )

    @api.model
    def create(self, vals):
        # Crear la actividad
        activity = super(activity, self).create(vals)
        
        # Obtener el curso y los estudiantes asociados
        course = activity.course_id
        if course:
            students = course.students_ids  # Asegúrate de que `students_ids` sea el campo correcto en `agenda_escolar.course`
            # Aquí puedes lanzar una excepción para inspeccionar los valores
            raise Exception(f"Curso: {course}, Estudiantes: {students}")
            
            for student in students:
                self.env['agenda_escolar.activity_student'].create({
                    'activity_id': activity.id,
                    'estudent_id': student.id,
                    'state': '0',  # Estado inicial
                    'view': '1',   # Vista inicial
                    'has_note': activity.has_note  # O la configuración deseada para has_note
                })
        return activity