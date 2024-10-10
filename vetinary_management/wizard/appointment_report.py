from odoo import api, fields, models,_
from odoo.exceptions import ValidationError


class ExcelReportWizard(models.TransientModel):
    _name = 'appointment.report.wizard'
    _description = 'Appointment Report Wizard'


    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")


    def action_print_excel_report(self):
        domain = []
        date_from = self.date_from
        if date_from:
            domain += [('date', '>=', date_from)]
        date_to = self.date_to
        if date_to:
            domain += [('date', '<=', date_to)]
        appointments = self.env['vetinary.appointments'].search_read(domain)
        print("appointments",appointments)
        data = {
            'appointments': appointments,
            'form_data': self.read()[0]
        }
        return self.env.ref('vetinary_management.action_appointment_excel_report_xlsx').report_action(self, data=data)
