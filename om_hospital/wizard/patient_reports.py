from odoo import api, fields, models,_
from odoo.exceptions import ValidationError


class ExcelReportWizard(models.TransientModel):
    _name = 'patient.report.wizard'
    _description = 'patient Report Wizard'

    patient_id = fields.Many2one('hospital.patient', string="Patient")
    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")

    def action_print_excel_report(self):
        domain = []
        patient_id = self.patient_id
        
        if patient_id:
            domain += [('patient_id', '=', patient_id.id)]
        date_from = self.date_from
        if date_from:
            domain += [('date_appointment', '>=', date_from)]
        date_to = self.date_to
        if date_to:
            domain += [('date_appointment', '', date_to)]
        appointments = self.env['hospital.appointment'].search_read(domain)
        print("appointments",appointments)
        data = {
            'appointments': appointments,
            'form_data': self.read()[0]
        }
        return self.env.ref('om_hospital.action_patient_excel_report_xlsx').report_action(self, data=data)