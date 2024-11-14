# -*- coding: utf-8 -*-

from odoo import models, fields, api

class activity_student(models.Model):
    _name = 'agenda_escolar.activity_student'
    _description = 'agenda_escolar.activity_student'
    
    # Define el campo que acepta números flotantes
    note = fields.Integer(string="Calificacion", digits=(6, 2))  # Puedes ajustar los dígitos según sea necesario

    view = fields.Selection([
        ('0', 'Visto'),
        ('1', 'Sin visualizacion')
    ], string='Vista', default='0')

    state = fields.Selection([
        ('0', 'En curso'),
        ('1', 'realizado')
    ], string='Estado', default='0')

    activity_id = fields.Many2one(
        'agenda_escolar.activity',
        string="Actividad",
        help="Seleccione la actividad"
    )

    estudent_id = fields.Many2one(
        'res.partner',
        string="Estidantes",
        domain=[('is_student', '=', True)],
        help="Seleccione el Profesor"
    )

