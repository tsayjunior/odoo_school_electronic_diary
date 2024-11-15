# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_student = fields.Boolean(string='Es estudiante')
    is_teacher = fields.Boolean(string='Es profesor')
    is_admin = fields.Boolean(string='Es admin')
    is_tutor = fields.Boolean(string='Es tutor') 
    # token = fields.Boolean(string='Token') 
    # Relación Many2one con el modelo res.users
    user_id = fields.Many2one('res.users', string="Usuario", help="Usuario asociado al administrador")

    # Definir la relación inversa
    assign_subject_ids = fields.One2many(
        'agenda_escolar.assign_subject',  # Modelo relacionado
        'teacher_id',                     # Campo en agenda_escolar.assign_subject que hace referencia a res.partner
        string="Asignaturas asignadas"    # Etiqueta del campo
    )
    course_ids = fields.Many2many(
        'agenda_escolar.course',  # Modelo relacionado
        'course_partner_rel',      # Nombre de la tabla relacional
        'partner_id',              # Nombre del campo en la tabla relacional que referencia al otro modelo
        'course_id',               # Nombre del campo en la tabla relacional que referencia a este modelo
        string="Cursos"
    )

class teacher(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    # Campo transitorio para la contraseña
    password = fields.Char(string="Contraseña", help="Contraseña para el usuario Docente", store=False)

    @api.model
    def create(self, vals):
        # Crea el registro de `res.partner`
        partner = super(teacher, self).create(vals)

        # Si `is_teacher` es True, crear o actualizar automáticamente el usuario
        if vals.get('is_teacher') and vals.get('password'):
            password = vals.get('password')
            self._create_or_update_user_for_teacher(partner, password)
        return partner

    def write(self, vals):
        res = super(teacher, self).write(vals)
        # Si `is_teacher` se marca o actualiza, crear o actualizar el usuario
        if vals.get('is_teacher') or vals.get('password'):
            for partner in self:
                password = vals.get('password')
                self._create_or_update_user_for_teacher(partner, password)
        return res

    def _create_or_update_user_for_teacher(self, partner, password=None):
        # Verifica si ya existe un usuario para este partner
        user = self.env['res.users'].search([('partner_id', '=', partner.id)], limit=1)

        # Si no existe el usuario, crearlo
        if not user:
            user_vals = {
                'name': partner.name,
                'login': partner.email,
                'partner_id': partner.id,
                'groups_id': [(6, 0, [self.env.ref('base.group_user').id, self.env.ref('agenda_escolar.group_teacher').id])],  # Grupo básico de usuario
                'password': password or '12345678',  # Contraseña predeterminada si no se especifica
            }
            user = self.env['res.users'].create(user_vals)
            partner.user_id = user  # Asocia el usuario creado al partner

        else:
            # Si el usuario ya existe, actualizar la contraseña
            user.write({'password': password or user.password, 
                        'groups_id': [(6, 0, [self.env.ref('base.group_user').id, self.env.ref('agenda_escolar.group_teacher').id])]
                    })

        # En caso de que el partner no tenga un usuario asociado, lo asociamos
        if not partner.user_id:
            partner.user_id = user
            