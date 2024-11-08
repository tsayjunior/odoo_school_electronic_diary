# -*- coding: utf-8 -*-

from odoo import models, fields, api

class admin(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    # is_admin = fields.Boolean()

    # Modificamos el campo existente `type_for_school` si ya está definido en el modelo base
    # def _modify_type_for_school(self):
    #     if hasattr(self, 'type_for_school'):
    #         self._fields['type_for_school'].string = 'Tipo'
    #         self._fields['type_for_school'].default = 'Estudiante'

    # # Llamamos a la modificación al inicializar el modelo
    # def __init__(self, pool, cr):
    #     super(admin, self).__init__(pool, cr)
    #     self._modify_type_for_school()