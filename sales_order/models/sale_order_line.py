from odoo import api, models, fields

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    image_field = fields.Binary(related='product_template_id.image_1920', string="Product Image")
    

    