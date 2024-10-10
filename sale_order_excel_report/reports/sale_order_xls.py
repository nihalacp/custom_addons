import io
import xlsxwriter
from odoo import models

class SaleOrderReportXlsx(models.AbstractModel):
    _name = 'report.sale_order_excel_report.sales_report_xls'
    _inherit = 'report.report_xlsx.abstract'


    def generate_xlsx_report(self, workbook, data, records):
        sheet = workbook.add_worksheet('Sale Orders')
        bold = workbook.add_format({'bold': True})
        bold_format = workbook.add_format({'bold': True, 'font_size': 16, 'align': 'center', 'border': 2})
        header_format = workbook.add_format({'bold': True, 'border': 1, 'align': 'center','bg_color': 'yellow'})
        cell_format = workbook.add_format({'border': 1, 'bold': True})
        date_format = workbook.add_format({'num_format': 'dd/mm/yyyy', 'border': 1})

        sheet.set_column('D:D', 30)
        sheet.set_column('E:E', 20)
        # Set up worksheet
        sheet.set_row(0, 25)
        
        
        row = 3
        col = 3
        sheet.set_row(row, 25)

        # Get data
        sales_data = data.get('sales', [])
        if not sales_data:
            print("No sales data to write.")
        
    
        customer_sales = {}
        for sales in sales_data:
            customer_id = sales.get('partner_id', [])[0]
            customer_name = sales.get('partner_id', [])[1] if len(sales.get('partner_id', [])) > 1 else 'N/A'
            if customer_id not in customer_sales:
                customer_sales[customer_id] = {
                    'customer_name': customer_name,
                    'sales': []
                }
            customer_sales[customer_id]['sales'].append(sales)
        
        # Write report for each customer
        for customer_id, customer_data in customer_sales.items():
            # Write customer name at the top of the section
            sheet.merge_range(row, 3, row, 6, f"Customer: {customer_data['customer_name']}", header_format)
            row += 2  # Leave space after the customer name


            for sales in sales_data:
                # Write a header for each sales order
                row += 1
                sheet.merge_range(row, col, row, col + 1, f"Sale Order: {sales.get('name', 'N/A')}", bold)
                row += 1
                sheet.write(row, col, 'Quotation' ,bold)
                sheet.write(row, col + 1, sales.get('name', 'N/A'))
                row += 1
                sheet.write(row, col, 'Order date' , bold)
                sheet.write(row, col + 1, sales.get('date_order', ''))
                row += 1
                
                sheet.write(row, col, 'Product', cell_format)
                sheet.write(row, col + 1, 'Quantity', cell_format)
                sheet.write(row, col + 2, 'Price', cell_format)
                sheet.write(row, col + 3, 'Subtotal', cell_format)
                row += 1

                for line in sales.get('order_lines', []):
                    sheet.write(row, col, line.get('product_id', 'N/A'))
                    sheet.write(row, col + 1, line.get('quantity', 0))
                    sheet.write(row, col + 2, line.get('price', 0))
                    sheet.write(row, col + 3, line.get('subtotal', 0))
                    row += 1
                    
                sheet.write(row, col, 'Total Amount' , bold)
                sheet.write(row, col + 1, sales.get('amount_total', 0), header_format)
                row += 1
                row += 1  # Add a blank row between orders

                    
                    

                # Add a blank row for separation between orders
            row += 2

        row += 2
        sheet.merge_range(row, col, row, col + 3, 'Summary', bold_format)
        
        total_customers = data.get('total_customers', 0)
        total_sales_count = data.get('total_sales_count', 0)
        total_sales = data.get('total_sales', 0)

        row += 1
        sheet.write(row, col, 'Total Sales Orders:', bold)
        sheet.write(row, col + 1, total_sales_count)
        
        row += 1
        sheet.write(row, col, 'Total Customers:', bold)
        sheet.write(row, col + 1, total_customers)
        
        row += 1
        sheet.write(row, col, 'Total Sales:', bold)
        sheet.write(row, col + 1, total_sales)





    # def generate_xlsx_report(self, workbook, data, records):
    #     sheet = workbook.add_worksheet('Sale Order')
    #     bold = workbook.add_format({'bold': True})
    #     bold_format = workbook.add_format({'bold': True, 'font_size': 16, 'align': 'center', 'border': 2})
    #     header_format = workbook.add_format({'bold': True, 'border': 1, 'bg_color': 'yellow'})
    #     cell_format = workbook.add_format({'border': 1})
    #     date_format = workbook.add_format({'num_format': 'dd/mm/yyyy', 'border': 1})
    #     sheet.set_row(0, 25)
    #     sheet.merge_range('A1:D1', 'Sale Order', bold_format)
    #     sheet.set_column('A:A', 20)
    #     sheet.set_column('B:B', 20)
    #     sheet.set_column('C:C', 20)
    #     sheet.set_column('D:D', 20)

    #     row = 1
    #     col = 0

    #     sheet.write(row, col, 'Quotation',bold)
    #     sheet.write(row, col+1, 'Customer' ,bold)
    #     sheet.write(row, col+2, 'Order date' , bold)
    #     sheet.write(row, col+3, 'Total Amount' , bold)
    
        
    #     print("Sales data received:", data['sales'])  # Check the content of sales data
    #     sales_data = data.get('sales', [])
    #     if not sales_data:
    #         print("No sales data to write.")
    #     for sales in sales_data:
    #         if isinstance(sales, dict):  # Ensure each item is a dictionary
    #             row += 1
    #             sheet.write(row, col, sales.get('name', 'N/A'))
    #             partner_id = sales.get('partner_id', [])
    #             sheet.write(row, col + 1, partner_id[1] if len(partner_id) > 1 else 'N/A')
    #             sheet.write(row, col + 2, sales.get('date_order', ''), date_format)
    #             sheet.write(row, col + 3, sales.get('amount_total', 0))


        
    #     row += 2  # Add a few rows before summary for spacing
    #     sheet.merge_range(row, col, row, col + 3, 'Summary', bold_format)
        
    #     # Write total customers and total sales
    #     total_customers = data.get('total_customers', 0)
    #     total_sales_count = data.get('total_sales_count', 0)
    #     total_sales = data.get('total_sales', 0)

    #     row += 1
    #     sheet.write(row, col, 'Total Sales Orders:', bold)
    #     sheet.write(row, col + 1, total_sales_count)
        
    #     row += 1
    #     sheet.write(row, col, 'Total Customers:', bold)
    #     sheet.write(row, col + 1, total_customers)
        
    #     row += 1
    #     sheet.write(row, col, 'Total Sales:', bold)
    #     sheet.write(row, col + 1, total_sales)



class SaleOrderReportHtml(models.AbstractModel):
    _name = 'report.sale_order_excel_report.report_html_sale_order'
    _inherit = 'report.report_xlsx.abstract'


    def _get_report_values(self, docids, data=None):
        # Retrieve parameters from data
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        confirmed = data.get('confirmed')
        
        # Build the domain based on parameters
        domain = []
        if start_date:
            domain.append(('date_order', '>=', start_date))
        if end_date:
            domain.append(('date_order', '<=', end_date))
        if confirmed:
            domain.append(('state', '=', 'sale'))
        
        # Search sale orders based on domain
        sale_orders = self.env['sale.order'].search(domain)
        
        # Return the values to the report template
        return {
            'docs': sale_orders,
            'start_date': start_date,
            'end_date': end_date,
            'confirmed': confirmed,
        }
