# -*- coding: utf-8 -*-

from odoo import models, fields, api

class teacher(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    type_for_school = fields.Char(default='Docente', string='Tipo')

