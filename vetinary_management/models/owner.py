from odoo import api, fields, models,_



class VetinaryOwner(models.Model):
    _name = 'vetinary.owner'
    _inherit = ['mail.thread']
    _description = 'Owner Master'


    name = fields.Char(string='Owner Name', required=True)
    phone_no = fields.Char(string='Phone Number')
    id_no = fields.Char(string='ID Number')
    # pet_ids = fields.One2many('vetinary.pet', 'owner_id', string="Pets")

