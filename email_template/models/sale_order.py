from odoo import models, fields, api
from datetime import datetime, timedelta
import logging

# Initialize the logger
_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'


    def _check_quotation_expiry(self):
        # _logger.info('Executing _check_quotation_expiry method.')
        # Get the configured number of expiry days
        expiry_days = int(self.env['ir.config_parameter'].sudo().get_param('sale.quotation_expiry_days', default=5))

        # Get the quotation expiry manager
        manager_id = self.env['ir.config_parameter'].sudo().get_param('sale.quotation_expiry_manager', default=False)
        if not manager_id:
            return False  # No manager configured

        # Fetch the manager (res.users)
        quotation_expiry_manager = self.env['res.users'].browse(int(manager_id))
        if not quotation_expiry_manager.exists():
            return False  # Invalid manager

        # Calculate the expiry date (today + expiry_days)
        expiry_date = (datetime.today() + timedelta(days=expiry_days)).date()

        # Find quotations that expire within the next `expiry_days` days
        sale_orders = self.search([
            ('state', 'in', ['draft', 'sent']),
            ('validity_date', '=', expiry_date)
        ])

        _logger.info('Orders fetched: %s', sale_orders)
        
        product_list = []
        for order in sale_orders:
            product_list.append({
                'name': order.name,
                'date_order': order.date_order.strftime('%Y-%m-%d'),  # Convert to string
                'partner_id': order.partner_id.name,
                'amount_total': order.amount_total,
                'currency_id': order.currency_id,
            })

        # If there are quotations to send
        if product_list:
            template = self.env.ref('email_template.quotation_mail_template')  # Adjust with your module's name
            email_values = {
                'email_to': quotation_expiry_manager.email,
                'email_from': self.env.user.email or 'noreply@example.com',
            }
            # Pass the product_list to the template context
            template.with_context(product_list=product_list).send_mail(self.id, email_values=email_values, force_send=True)


        