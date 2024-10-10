from odoo import api, models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    new_customer_sales_description = fields.Text(string='Customer Sales Description')
    additional_description = fields.Html(string='Additional description')
    delivery_charge = fields.Float(string="Delivery Charge")
    

    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['new_customer_sales_description'] = self.new_customer_sales_description
        return invoice_vals


    @api.onchange('delivery_charge')
    def _onchange_delivery_charge(self):
        product = self.env['product.template'].search([('name', '=', 'delivery charge')])
        if product:
            self.order_line=[(0, 0, {
                    'name': 'delivery_charge',
                    'product_id': product.id,
                    'product_uom':1,
                    'product_uom_qty': 1,
                    'price_unit': self.delivery_charge,
                })]
        else:
            self.order_line = []
        

    