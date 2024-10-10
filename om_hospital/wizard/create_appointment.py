from odoo import api, fields, models,_
from odoo.exceptions import ValidationError


class CreateAppointmentWizard(models.TransientModel):
    _name = 'create.appointment.wizard'
    _description = 'Create Appointment Wizard'

    name = fields.Char(string="Name", required=True)
    patient_id = fields.Many2one('hospital.patient', string="Patient",required=False)

    def action_create_appointment(self):
        print("Button Is Clicked")