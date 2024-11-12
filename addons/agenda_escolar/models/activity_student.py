# -*- coding: utf-8 -*-

from odoo import models, fields, api

class activity_student(models.Model):
    _name = 'agenda_escolar.activity_student'
    _description = 'agenda_escolar.activity_student'
    
    view = fields.Selection([
        ('0', 'Visto'),
        ('1', 'Sin visualizacion')
    ], string='Vista', default='0')

    has_note = fields.Selection([
        ('0', 'Con calificación'),
        ('1', 'Sin calificación')
    ], string='Calificación', default='0')

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
        domain=[('is_teacher', '=', True)],
        help="Seleccione el Profesor"
    )
