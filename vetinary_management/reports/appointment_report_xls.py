import io
import xlsxwriter
from odoo import models

class AppointmentReportXlsx(models.AbstractModel):
    _name = 'report.vetinary_management.appointment_excel_report_xls'
    _inherit = 'report.report_xlsx.abstract'


    def generate_xlsx_report(self, workbook, data, records):
        sheet = workbook.add_worksheet('Appointments')
        bold = workbook.add_format({'bold': True})
        bold_format = workbook.add_format({'bold': True, 'font_size': 16, 'align': 'center', 'border': 2})
        header_format = workbook.add_format({'bold': True, 'border': 1, 'bg_color': 'yellow'})
        cell_format = workbook.add_format({'border': 1})
        date_format = workbook.add_format({'num_format': 'dd/mm/yyyy', 'border': 1})
        sheet.set_row(0, 25)
        sheet.merge_range('A1:D1', 'Appointment Details', bold_format)
        sheet.set_column('A:A', 20)
        sheet.set_column('B:B', 20)
        sheet.set_column('C:C', 20)
        sheet.set_column('D:D', 20)

        row = 1
        col = 0

        sheet.write(row, col, 'Appointment No',bold)
        sheet.write(row, col+1, 'Appointment Date' ,bold)
        sheet.write(row, col+2, 'Pet Name' , bold)

        for appointment in data['appointments']:
            row += 1
            sheet.write(row, col, appointment['ref'])
            sheet.write(row, col+1, appointment['date'])
            sheet.write(row, col+2, appointment['pet_id'][1])
