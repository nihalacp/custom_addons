from odoo import models, fields, api

class SaleReport(models.Model):
    _inherit = 'sale.report'


    delivery_charge = fields.Float(string="Delivery Charge")

    

    def _select_additional_fields(self):
        res = super()._select_additional_fields()
        res['delivery_charge'] = "s.delivery_charge"
        return res


    def _group_by_sale(self):
        res = super()._group_by_sale()
        res += """,
            s.delivery_charge
            """
        return res


    