from odoo import api, fields, models,_
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread']
    _description = 'Patient Master'
    _rec_names_search = ['name', 'email']
    

    name = fields.Char(string="Name", required=True, tracking=True)
    ref = fields.Char(string="Reference")
    date_of_birth = fields.Date(string="DOB", tracking=True)
    gender = fields.Selection([('male', 'Male'),('female', 'Female')],string="Gender", tracking=True)
    image = fields.Image(string="Image")
    documents = fields.Binary(string="Documents")
    document_name = fields.Char(string="File Name")
    tag_ids = fields.Many2many('patient.tag','patient_tag_rel','patient_id','tag_id',string="Tags")
    active = fields.Boolean(string="Active", default=True)
    # patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    email = fields.Char(string='Email')

    @api.ondelete(at_uninstall=False)
    def _check_patient_appointments(self):
        for rec in self:
            domain = [('patient_id','=',rec.id)]
            appointments = self.env['hospital.appointment'].search(domain)
            if appointments:
                raise ValidationError(_('you cannot delete the patient now.\nAppointments existing for this patient:'))
        return super().unlink()



    # odoo 16
    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, order=None):
        args = list(args or [])
        if name :         
            args += ['|', ('name', operator, name),    
                        ('email',operator, name)]       
        return self._search(args, limit=limit,order=order)


    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, '%s - %s' % (rec.name, rec.email)))
        return res
