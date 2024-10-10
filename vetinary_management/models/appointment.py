from odoo import api, fields, models,_
import logging

_logger = logging.getLogger(__name__)

class VetinaryAppointment(models.Model):
    _name = 'vetinary.appointments'
    _inherit = ['mail.thread']
    _description = 'Appointment Master'


    ref = fields.Char(string="Reference", default='New')
    date = fields.Datetime(string="Appointment Date", required=True)
    pet_id = fields.Many2one('vetinary.pet', string="Pet", required=True)
    owner_id = fields.Many2one('vetinary.owner', string="Owner", related='pet_id.owner_id', store=True)
    doctor_id = fields.Many2one('hr.employee', string="Doctor", required=True)
    diagnosis = fields.Html(string="Diagnosis")
    prescription_line_ids = fields.One2many('vet.prescription.line', 'appointment_id', string='Prescription Lines')
    state = fields.Selection([('draft','Draft'),('confirmed','Confirmed'),('ongoing','Ongoing'),
                                ('done','Done'),('cancel','Cancelled')], default='draft', tracking=True)


    @api.model
    def create(self, vals):
        if vals.get('pet_id'):
            pet = self.env['vetinary.pet'].browse(vals['pet_id'])
            if not pet.owner_id:
                raise ValidationError("Selected pet does not have an associated owner.")
        return super(VetinaryAppointment, self).create(vals)


    @api.onchange('pet_id')
    def _onchange_pet_id(self):
        if self.pet_id:
            self.owner_id = self.pet_id.owner_id
        else:
            self.owner_id = False


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('ref') or vals['ref'] == 'New':
                vals['ref'] = self.env['ir.sequence'].next_by_code('vetinary.appointments')
        return super().create(vals_list)


    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'

        
    def action_ongoing(self):
        for rec in self:
            rec.state = 'ongoing'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'




class PrescriptionLine(models.Model):
    _name = 'vet.prescription.line'
    _description = 'Prescription Line'

    appointment_id = fields.Many2one('vetinary.appointments', string='Appointment', required=True)
    medicine = fields.Char(string='Medicine', required=True)
    quantity = fields.Integer(string='Quantity', required=True)
    dosage = fields.Char(string='Dosage', required=True)
    