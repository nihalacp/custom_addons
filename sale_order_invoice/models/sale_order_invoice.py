from odoo import models, api, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'



    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        
        for order in self:
            # Create invoices for the sale order
            invoice_ids = order._create_invoices()
            
            for invoice in invoice_ids:
                # Only attempt to post the invoice if it's in draft state
                if invoice.state == 'draft':
                    try:
                        invoice.action_post()
                    except Exception as e:
                        _logger.error('Failed to post invoice %s: %s', invoice.id, str(e))

                if order.picking_ids:
                    for picking in order.picking_ids:
                        if picking.state != 'done':
                            picking.button_validate()
        
        return res



