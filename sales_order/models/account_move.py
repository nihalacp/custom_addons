from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    new_customer_sales_description = fields.Text(string='Customer Sales Description')



    