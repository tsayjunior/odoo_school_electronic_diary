# -*- coding: utf-8 -*-

from odoo import models, fields, api
from openai import OpenAI
from odoo.exceptions import UserError

class comment(models.Model):
    _name = 'agenda_escolar.comment'
    _description = 'agenda_escolar.comment'
    
    text = fields.Char(string="Comentario", readonly=False, required=True, help='Introduzca un Comentario')
    event_id = fields.Many2one('agenda_escolar.event', string="Evento", help="Seleccione un evento", compute="_compute_name", store=True)
    #user_id = fields.Many2one('res.partner', string="Usuarios", domain=[('is_student', '=', True)], help="Seleccione el estudiante")
    user_id = fields.Many2one('res.partner', string="Usuarios", help="Seleccione el estudiante", compute="_compute_name", store=True)

    @api.model
    def create(self, vals):
        text = super(comment, self).create(vals)
        text.user_id = self.env.user.partner_id
        b = self._validate_obscene_text(text.text)
        if(b == "True" or b == "true"):
            text.unlink()
            raise UserError("Actualización no permitida, el texto contiene palabras obscenas")
        return text
    
    def write(self, vals):
        if 'text' in vals:
            b = self._validate_obscene_text(vals['text'])
            if b.lower() == "true":
                raise UserError("Actualización no permitida, el texto contiene palabras obscenas")
        return super(comment, self).write(vals)
    
    def _validate_obscene_text(self, text):
        try:
            openai_api_key = self.env['ir.config_parameter'].sudo().get_param('openai_api_key')
            client = OpenAI(api_key = openai_api_key)
            response = client.chat.completions.create(
                model="gpt-4o-mini-2024-07-18",
                messages = [
                    {
                        "role": "user",
                        "content": "la siguiente frase o comentario que te indique necesito que validez si tiene" +
                        "o esta compuesta por una o mas palabra obscena prohibida en el area del colegio o la universidad," +
                        "responde solo true o false, donde true es una palabra obscena o false no lo es:" +
                        text
                    }
                ],
            )

            return response.choices[0].message.content
        except Exception as e:
            return f"Error de conexión: {str(e)}"