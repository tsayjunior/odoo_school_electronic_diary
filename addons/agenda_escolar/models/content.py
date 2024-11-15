# -*- coding: utf-8 -*-

from odoo import models, fields, api
import base64
from openai import OpenAI
import os

class content(models.Model):
    _name = 'agenda_escolar.content'
    _description = 'agenda_escolar.content'
    
    name = fields.Char(string="Nombre", readonly=False, required=True, help='Introduzca el Nombre')
    description = fields.Text(string="Descripcion", readonly=False, required=False, help='Introduzca la descripcion')
    audio = fields.Binary(string="Audio", help="Archivo de audio")
    audio_filename = fields.Char(string="Nombre del archivo", help="Nombre del archivo de audio")
    audio_summary = fields.Text(string="Resumen de audio", help="Resumen del contenido del audio")
    subject_id = fields.Many2one('agenda_escolar.subject', string="Materia", help="Seleccione la Materia", compute="_compute_name", store=True)

    @api.model
    def create(self, values):
        record = super(content, self).create(values)
        if values.get('audio'):
            record.audio_summary = self._get_audio_summary(values.get('audio'))
        return record
    
    def write(self, values):
        if 'audio' in values and values.get('audio'):
            values['audio_summary'] = self._get_audio_summary(values['audio'])
        return super(content, self).write(values)

    def _get_audio_summary(self, audio):
        try:
            openai_api_key = self.env['ir.config_parameter'].sudo().get_param('openai_api_key')
            client = OpenAI(api_key = openai_api_key)
            # Decodificar el audio desde base64
            audio_data = base64.b64decode(audio)
            
            # Usar 'with' para asegurarse de que el archivo se cierra correctamente
            with open("temp_audio.mp3", "wb") as temp_file:
                temp_file.write(audio_data)

            # Abrir el archivo temporal en modo binario
            with open("temp_audio.mp3", "rb") as audio_file:
                transcription = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file
                )

            # Eliminar el archivo temporal después de usarlo
            os.remove("temp_audio.mp3")

            response = client.chat.completions.create(
                model="gpt-4o-mini-2024-07-18",
                messages = [
                    {
                        "role": "user",
                        "content": "Realiza un resumen resaltando los puntos mas importantes o criticos si es que los tiene, " +
                        "esquematizandolo con titulos o subtitulos de acuerdo al contenido del tema, con el objetivo de " + 
                        "ayudar a comprender a una estudiante de colegio o universidad el siguiente tema o contenido: " +
                        transcription.text
                    }
                ],
            )

            return response.choices[0].message.content
        except Exception as e:
            return f"Error de conexión: {str(e)}"
    
    def convert_audio_to_binary(audio_file_path):
        with open(audio_file_path, 'rb') as audio_file:
            audio_binary = base64.b64encode(audio_file.read())
        return audio_binary