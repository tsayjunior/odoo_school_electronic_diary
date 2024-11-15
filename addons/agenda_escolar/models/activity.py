# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
import pprint

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
    def default_get(self, fields_list):
        defaults = super(activity, self).default_get(fields_list)
        user = self.env.user

        _logger = logging.getLogger(__name__)
        _logger.info("Este es un mensaje informativo.")
        _logger.debug("Este es un mensaje que se verá inmediatamente en los logs.")
        _logger.debug("User => %s", user)
        # Usar pprint para imprimir todo el diccionario de 'user'
        # _logger.debug("User full details:\n%s", pprint.pformat(user.read()))
        # user_data = user.read()  # Esto devuelve un diccionario con los campos del usuario
        # _logger.debug("User details: %s", user_data)
        _logger.debug("partner_id => %s", user.partner_id)

        if user.partner_id.is_teacher:
            defaults['teacher_id'] = user.partner_id.id
        return defaults
    
    @api.onchange('teacher_id')
    def _onchange_teacher(self):
        _logger = logging.getLogger(__name__)

        if self.teacher_id:
            # Obtener las asignaturas asociadas al docente
            assign_subjects = self.teacher_id.assign_subject_ids
            _logger.debug("Asignaturas del docente: %s", assign_subjects)
            
            # Obtener los cursos relacionados con las asignaturas
            course_ids = assign_subjects.mapped('course_id').ids
            _logger.debug("Cursos asociados al docente: %s", course_ids)
            
            if course_ids:
                _logger.debug(" tiene cursos ")
                
                domain = [('id', 'in', course_ids)]
                readonly = False  # El campo es editable si hay cursos
            else:
                _logger.debug("no tiene cursos ")

                domain = [('id', '=', False)]  # Especifica que no hay cursos para mostrar
                readonly = True  # Hacer el campo readonly si no hay cursos

            _logger.debug("Dominio para course_id: %s", domain)
            return {'domain': {'course_id': domain}, 'readonly': {'course_id': readonly}}
        return {'domain': {'course_id': [('id', '=', False)]}, 'readonly': {'course_id': True}}  # Si no hay docente, no mostrar cursos

    @api.model
    def create(self, vals):
        # Crear la actividad normalmente
        new_activity = super(activity, self).create(vals)

        _logger = logging.getLogger(__name__)
        _logger.info("*************************** ingresa a crear actividad ---------------------------------")
        # Obtener el curso asociado
        course = new_activity.course_id
        _logger.info(course.name)
        if course:
            _logger.info(" Tiene curso ")
            # Obtener estudiantes asociados al curso (ejemplo: campo Many2many o One2many en el curso)
            students = course.student_ids  # Ajustar según el campo que tengas en el modelo course

            # Crear un registro en activity_student para cada estudiante
            for student in students:
                _logger.info(student.name)

                self.env['agenda_escolar.activity_student'].create({
                    'activity_id': new_activity.id,
                    'estudent_id': student.id,
                    'note': 0,
                    'state': new_activity.state,  # Estado inicial "En curso"
                    'view': '1',   # Vista inicial "Sin visualización"
                })
        else:
            _logger.info("no tiene curso ")
            
        return new_activity
    
    
    @api.model
    def get_user_partner_activities(self):
        partner_id = self.env.user.partner_id.id
        return [('teacher_id', '=', partner_id)]
    
    def action_open_activity_student(self):
            """Abre la vista de lista de actividades de estudiantes"""
            return {
                'name': 'Actividad estudiantes',
                'type': 'ir.actions.act_window',
                'res_model': 'agenda_escolar.activity_student',
                'view_mode': 'list,form',
                'target': 'current',
                'domain': [('activity_id', '=', self.id)],  # Filtra la vista de lista por activity_id actual
                'context': {
                    'default_activity_id': self.id,  # Establece el course_id por defecto en el formulario de creación
            }
            }