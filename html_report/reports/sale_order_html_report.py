import io
import xlsxwriter
from odoo import models

class SaleOrderReportXlsx(models.AbstractModel):
    _name = 'report.html_report.html_report_sale_order'
    _inherit = 'report.report_xlsx.abstract'


    def _get_report_values(self, docids, data=None):
        # Retrieve parameters from data
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        confirmed = data.get('confirmed')
        
        domain = []
        if confirmed:
            domain += [('state', '=', 'sale')]
        if start_date:
            domain += [('date_order', '>=', start_date)]
        if end_date:
            domain += [('date_order', '<=', end_date)]
        
        # Search sale orders based on domain
        sale_orders = self.env['sale.order'].search(domain)
        
        # Return the values to the report template
        return {
            'docs': sale_orders,
            'start_date': start_date,
            'end_date': end_date,
            'confirmed': confirmed,
        }