from odoo import api, models, fields
import io
import xlsxwriter
from odoo import models

class SaleOrderSQLReportXlsx(models.AbstractModel):
    _name = 'report.sql_query_report.sale_order_sql_report'
    _inherit = 'report.report_xlsx.abstract'


    def generate_xlsx_report(self, workbook, data, docs):
        sheet = workbook.add_worksheet('Sales Report')
        bold = workbook.add_format({'bold': True})

        # Define headers
        headers = ['Quotation', 'Customer Name', 'Order Date', 'Total Amount', 'Product ID', 'Quantity', 'Price', 'Subtotal']
        for col_num, header in enumerate(headers):
            sheet.write(0, col_num, header, bold)

        # Fetch sales data
        self.env.cr.execute("""
            WITH sales_data AS (
                SELECT
                    so.id AS sale_order_id,
                    so.name AS quotation,
                    rp.name AS customer_name,
                    so.date_order AS order_date,
                    so.amount_total AS total_amount,
                    sol.product_id AS product_id,
                    sol.product_uom_qty AS quantity,
                    sol.price_unit AS price,
                    (sol.product_uom_qty * sol.price_unit) AS subtotal
                FROM
                    sale_order AS so
                JOIN
                    res_partner AS rp ON so.partner_id = rp.id
                JOIN
                    sale_order_line AS sol ON so.id = sol.order_id
                WHERE
                    so.state IN ('sale', 'done')
            )
            SELECT
                sd1.quotation,
                sd1.customer_name,
                sd1.order_date,
                sd1.total_amount,
                sd1.product_id,
                sd1.quantity,
                sd1.price,
                sd1.subtotal
            FROM
                sales_data sd1
        """)
        sales_data = self.env.cr.dictfetchall()

        # Write data to Excel
        row = 1
        for sales in sales_data:
            sheet.write(row, 0, sales['quotation'])
            sheet.write(row, 1, sales['customer_name'])
            sheet.write(row, 2, sales['order_date'].strftime('%Y-%m-%d'))
            sheet.write(row, 3, sales['total_amount'])
            sheet.write(row, 4, sales['product_id'])
            sheet.write(row, 5, sales['quantity'])
            sheet.write(row, 6, sales['price'])
            sheet.write(row, 7, sales['subtotal'])
            row += 1



    # in case of pdf report 
    # @api.model
    # def _get_report_values(self, docids, data=None):
    #     # Execute SQL query
    #     self.env.cr.execute("""
    #         WITH sales_data AS (
    #             SELECT
    #                 so.id AS sale_order_id,
    #                 so.name AS quotation,
    #                 rp.name AS customer_name,
    #                 so.date_order AS order_date,
    #                 so.amount_total AS total_amount,
    #                 sol.product_id AS product_id,
    #                 sol.product_uom_qty AS quantity,
    #                 sol.price_unit AS price,
    #                 (sol.product_uom_qty * sol.price_unit) AS subtotal
    #             FROM
    #                 sale_order AS so
    #             JOIN
    #                 res_partner AS rp ON so.partner_id = rp.id
    #             JOIN
    #                 sale_order_line AS sol ON so.id = sol.order_id
    #             WHERE
    #                 so.state IN ('sale', 'done')
    #         )
    #         SELECT
    #             sd1.quotation,
    #             sd1.customer_name,
    #             sd1.order_date,
    #             sd1.total_amount,
    #             sd1.product_id,
    #             sd1.quantity,
    #             sd1.price,
    #             sd1.subtotal
    #         FROM
    #             sales_data sd1
    #     """)
    #     sales_data = self.env.cr.dictfetchall()

        # Organize data
        # customer_sales = {}
        # for sales in sales_data:
        #     customer_name = sales.get('customer_name')
        #     if customer_name not in customer_sales:
        #         customer_sales[customer_name] = {
        #             'customer_name': customer_name,
        #             'sales': []
        #         }
        #     customer_sales[customer_name]['sales'].append(sales)

        # # Calculate totals
        # total_customers = len(customer_sales)
        # total_sales_count = len(sales_data)
        # total_sales = sum([s['total_amount'] for s in sales_data])

        # return {
        #     'doc_ids': docids,
        #     'doc_model': 'sale.order',
        #     'docs': customer_sales,
        #     'total_customers': total_customers,
        #     'total_sales_count': total_sales_count,
        #     'total_sales': total_sales,
        # }