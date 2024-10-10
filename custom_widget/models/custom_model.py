from odoo import models, fields

class CustomModel(models.Model):
    _name = 'custom.model'
    _description = 'Custom Model'

    name = fields.Char(string='Name')
    color = fields.Char(string='Color Picker')
    