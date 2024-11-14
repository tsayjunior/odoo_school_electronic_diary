# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_student = fields.Boolean(string='Es estudiante')
    is_teacher = fields.Boolean(string='Es profesor')
    is_admin = fields.Boolean(string='Es admin')
    is_tutor = fields.Boolean(string='Es tutor')
    # Relación Many2one con el modelo res.users
    user_id = fields.Many2one('res.users', string="Usuario", help="Usuario asociado al administrador")

