from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    image_1920 = fields.Binary(string="Product Image")
