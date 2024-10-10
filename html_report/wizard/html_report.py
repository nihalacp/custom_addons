from odoo import api, fields, models,_
from odoo.exceptions import ValidationError


class HtmlReportWizard(models.TransientModel):
    _name = 'sales.html.report.wizard'
    _description = 'sales Html Report Wizard'


    start_date = fields.Date('Start Date', required=True)
    end_date = fields.Date('End Date', required=True)
    confirmed = fields.Boolean('Confirmed Orders', default=True)


    def action_view_html_report(self):
        self.ensure_one()
        domain = [('date_order', '>=', self.start_date), ('date_order', '<=', self.end_date)]
        if self.confirmed:
            domain.append(('state', '=', 'sale'))  # Only include confirmed orders

        return self.env.ref('html_report.action_html_report_sale_order').report_action(self, data={
        
        })