from odoo import models, fields, api

class SaleCompare(models.TransientModel):
    _name = 'sale.compare'
    _description = 'Sale Compare Wizard'

    name = fields.Char(string='Name', required=True)
    comparison_data = fields.Text(string='Comparison Data')

    @api.model
    def default_get(self, fields):
        res = super(SaleCompare, self).default_get(fields)
        # Populate any default values for the wizard here
        return res

    def action_confirm(self):
        # Logic for what happens when the wizard is confirmed
        # Example: self.env['sale.order'].create({...})
        return {'type': 'ir.actions.act_window_close'}