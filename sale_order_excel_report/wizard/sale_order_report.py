from odoo import api, fields, models,_
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError

class ExcelReportWizard(models.TransientModel):
    _name = 'sales.report.wizard'
    _description = 'sales Report Wizard'

    customer_name = fields.Many2one('res.partner', string='Customer')
    start_date = fields.Date('Start Date', required=True)
    end_date = fields.Date('End Date', required=True)
    confirmed = fields.Boolean('Confirmed Orders', default=True)
    product_id = fields.Many2one('product.product', string='Product')

    
    def action_print_excel_report(self):
        if self.product_id and not self.product_id.exists():
            raise UserError('The selected product does not exist anymore.')

        domain = []
        customer_name = self.customer_name
        if customer_name:
            domain += [('partner_id', '=', customer_name.id)]
        if self.product_id:
            domain += [('order_line.product_id', '=', self.product_id.id)]
        confirmed = self.confirmed
        if confirmed:
            domain += [('state', '=', 'sale')]       
        start_date = self.start_date
        if start_date:
            domain += [('date_order', '>=', start_date)]
        end_date = self.end_date
        if end_date:
            domain += [('date_order', '<=', end_date)]
        sales = self.env['sale.order'].search_read(domain)
        print("sales",sales)
        sales_orders = self.env['sale.order'].search(domain)

        total_sales = sum(order.amount_total for order in sales_orders)
        total_sales_count = len(sales_orders)
        customer_ids = sales_orders.mapped('partner_id')
        total_customers = len(set(customer_ids.mapped('id')))

        sales_data = []
        for order in sales_orders:
            order_lines = []
            for line in order.order_line:
                if self.product_id and line.product_id.id != self.product_id.id:
                    continue
                order_lines.append({
                    'product_id': line.product_id.name,
                    'quantity': line.product_uom_qty,
                    'price': line.price_unit,
                    'subtotal': line.price_subtotal
                })

            sales_data.append({
                'name': order.name,
                'partner_id': [order.partner_id.id, order.partner_id.name],
                'date_order': order.date_order,
                'amount_total': order.amount_total,
                'order_lines': order_lines 
            })


        data = {
            'sales': sales_data,
            'total_sales': total_sales,
            'total_customers': total_customers,
            'total_sales_count': total_sales_count,
            'form_data': self.read()[0]
        }
        return self.env.ref('sale_order_excel_report.action_sales_report_xlsx').report_action(self, data=data)





    def action_html_report_view(self):
        self.ensure_one()
        domain = [('date_order', '>=', self.start_date), ('date_order', '<=', self.end_date)]
        if self.confirmed:
            domain.append(('state', '=', 'sale'))  # Only include confirmed orders

        return self.env.ref('sale_order_excel_report.action_report_html_sale_order').report_action(self, data={
            
        })





        