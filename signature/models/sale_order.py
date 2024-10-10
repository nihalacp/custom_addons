from odoo import api, models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'


    signature = fields.Binary("Signature")