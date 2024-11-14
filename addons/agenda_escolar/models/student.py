# -*- coding: utf-8 -*-

from odoo import models, fields, api

class student(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    
    # Campo Many2many para los cursos en los que está inscrito el estudiante
    course_ids = fields.Many2many(
        'agenda_escolar.course',  # Modelo de destino
        'student_course_rel',     # Nombre de la tabla intermedia
        'student_id',             # Campo que apunta a 'res.partner' (este modelo)
        'course_id',              # Campo que apunta a 'agenda_escolar.course' (modelo relacionado)
        string='Cursos'
    )
      # Relación de muchos a muchos con los tutores
    tutor_ids = fields.Many2many(
        'res.partner',           # Modelo de destino (tutors y students son ambos 'res.partner')
        'student_tutor_rel',      # Nombre de la tabla intermedia
        'student_id',             # Campo que apunta a este modelo (student)
        'tutor_id',               # Campo que apunta al modelo relacionado (tutor)
        string='Tutores',
        domain=[('is_tutor', '=', True)]  # Filtra para mostrar solo los tutores
    )

    # Campo transitorio para la contraseña
    password = fields.Char(string="Contraseña", help="Contraseña para el usuario Estudiante", store=False)

    @api.model
    def create(self, vals):
        # Crea el registro de `res.partner`
        partner = super(student, self).create(vals)
        
        # Si `is_student` es True, crear o actualizar automáticamente el usuario
        if vals.get('is_student') and vals.get('password'):
            password = vals.get('password')
            self._create_or_update_user_for_student(partner, password)
        
        return partner

    def write(self, vals):
        res = super(student, self).write(vals)
        
        # Si `is_student` se marca o actualiza, crear o actualizar el usuario
        if vals.get('is_student') or vals.get('password'):
            for partner in self:
                password = vals.get('password')
                self._create_or_update_user_for_student(partner, password)
        
        return res

    def _create_or_update_user_for_student(self, partner, password=None):
        # Verifica si ya existe un usuario para este partner
        user = self.env['res.users'].search([('partner_id', '=', partner.id)], limit=1)
        
        # Si no existe el usuario, crearlo
        if not user:
            user_vals = {
                'name': partner.name,
                'login': partner.email,
                'partner_id': partner.id,
                'groups_id': [(6, 0, [self.env.ref('base.group_user').id, self.env.ref('agenda_escolar.group_student').id])],  # Grupo básico de usuario
                'password': password or '12345678',  # Contraseña predeterminada si no se especifica
            }
            user = self.env['res.users'].create(user_vals)
            partner.user_id = user  # Asocia el usuario creado al partner

        else:
            # Si el usuario ya existe, actualizar la contraseña
            user.write({'password': password or user.password, 
                        'groups_id': [(6, 0, [self.env.ref('base.group_user').id, self.env.ref('agenda_escolar.group_student').id])]
                    })
        
        # En caso de que el partner no tenga un usuario asociado, lo asociamos
        if not partner.user_id:
            partner.user_id = user