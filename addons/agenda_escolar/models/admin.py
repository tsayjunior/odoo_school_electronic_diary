# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class admin(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    
    # Campo transitorio para la contraseña
    password = fields.Char(string="Contraseña", help="Contraseña para el usuario administrador", store=False)

    @api.model
    def create(self, vals):
        partner = super(admin, self).create(vals)
        
        if vals.get('is_admin') and vals.get('password'):
            password = vals.get('password')
            self._create_or_update_user_for_admin(partner, password)
        
        return partner

    def write(self, vals):
        res = super(admin, self).write(vals)
        
        if vals.get('is_admin') or vals.get('password'):
            for partner in self:
                password = vals.get('password')
                self._create_or_update_user_for_admin(partner, password)
        
        return res

    def _create_or_update_user_for_admin(self, partner, password=None):
        # Verifica si ya existe un usuario para este partner
        user = self.env['res.users'].search([('partner_id', '=', partner.id)], limit=1)
        
        internal_user_group = self.env.ref('base.group_user')  # Grupo de usuario interno
        # Obtiene el grupo de administrador de agenda
        admin_group = self.env.ref('agenda_escolar.group_admin_partner')

        groups_to_assign = [internal_user_group.id, admin_group.id]
        # Si no existe el usuario, crearlo
        if not user:
            user_vals = {
                'name': partner.name,
                'login': partner.email,
                'partner_id': partner.id,
                # 'groups_id': [(6, 0, [internal_user_group.id])],
                'groups_id': [(6, 0, [self.env.ref('base.group_user').id])],  # Grupo básico de usuario
                'password': password or '12345678',  # Contraseña predeterminada si no se especifica
            }
            user = self.env['res.users'].create(user_vals)
            partner.user_id = user
            # Si el partner es administrador, agregarle el grupo de administrador después de crear el usuario
                # if partner.is_admin:
            # user.write({'groups_id': [(4, admin_group.id)]})

        else:
            groups_to_update = [internal_user_group.id, admin_group.id] 
            user.write({
                'password': password or user.password,
                # 'groups_id': [(6, 0, groups_to_update)]  # Actualizar grupos
            })

        if not partner.user_id:
            partner.user_id = user