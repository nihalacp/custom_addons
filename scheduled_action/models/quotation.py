from odoo import models, fields, api
from datetime import datetime, timedelta

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def delete_old_quotations(self):
        threshold_date = datetime.now() - timedelta(days=15)
        old_quotations = self.search([('state', '=', 'draft'), ('create_date', '<', threshold_date)])
        old_quotations.unlink()