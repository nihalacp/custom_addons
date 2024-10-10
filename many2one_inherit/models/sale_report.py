from odoo import models, fields, api



class SaleReport(models.Model):
    _inherit = 'sale.report'

    patient_id = fields.Many2one('hospital.patient', string='Patient')



    

    def _select_additional_fields(self):
        res = super()._select_additional_fields()
        res['patient_id'] = "s.patient_id"
        return res

