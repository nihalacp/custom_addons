from odoo import models, fields, api



class SaleOrder(models.Model):
    _inherit = 'sale.order'

    patient_id = fields.Many2one('hospital.patient', string='Patient')


