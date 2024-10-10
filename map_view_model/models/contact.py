from odoo import models, fields


class MapContact(models.Model):
    _name = "map.contact"
    _description = "Map Contacts"

    name = fields.Char()
    age = fields.Integer()