from odoo import api, fields, models
from odoo.exceptions import UserError

class Prescription(models.Model):
    _name = 'hospital.prescription'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient Prescription'



    appointment_id = fields.Many2one('hospital.appointment',string="Appointment")
    description = fields.Html(string='Description')
    date = fields.Date(string='Date', required=True, default=fields.Date.context_today)
    quantity = fields.Float(string='Quantity', required=True)
    dosage = fields.Char(string='Dosage')
    prescription_line_ids = fields.One2many('hospital.prescription.line','prescription_id',string="Order Lines")
    medication_ids = fields.One2many('hospital.prescription.line', 'prescription_id', string='Medications')
    approver_id = fields.Many2one('res.users', string='Approver')
    patient_id = fields.Many2one('hospital.patient', string="Patient",required=False,ondelete='restrict')
    

    state = fields.Selection([
        ('draft', 'Draft'),
        ('waiting_approval', 'Waiting Approval'),
        ('approved', 'Approved'),
    ], string='Status', tracking=True, default='draft')

    def action_submit(self):
        self.write({'state': 'waiting_approval'})

        
        # Create an activity for the approver
        if self.approver_id:
            activity_type = self.env.ref('mail.mail_activity_data_todo', raise_if_not_found=False)
            self.env['mail.activity'].create({
                'res_model_id': self.env['ir.model'].search([('model', '=', 'hospital.prescription')], limit=1).id,
                'res_id': self.id,
                'activity_type_id': activity_type.id if activity_type else False,
                'user_id': self.approver_id.id,
                'summary': 'Approve Prescription',
                'note': 'Please review and approve the prescription.',
            })
        
        return  True

    def action_approve(self):
        self.write({'state': 'approved'})


    def action_revise(self):
        self.write({'state': 'draft'})


    def action_send_mail(self):
        template = self.env.ref('om_hospital.prescription_email_template')
        for rec in self:
            if rec.patient_id.email:
                email_values = {'subject': 'Test OM'}
                template.send_mail(rec.id, force_send=True, email_values=email_values)
        




class PrescriptionLine(models.Model):
    _name = 'hospital.prescription.line'
    _description = 'Prescription Line'

    prescription_id = fields.Many2one('hospital.prescription', string='Prescription', ondelete='cascade')
    medication_id = fields.Many2one('product.product', string='Medication', required=True)
    qty = fields.Float(string='Quantity', required=True)
    dosage = fields.Char(string='Dosage')
    description = fields.Char(string='Description')
    