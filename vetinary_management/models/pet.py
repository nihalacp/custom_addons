from odoo import api, fields, models,_



class VetinaryPet(models.Model):
    _name = 'vetinary.pet'
    _inherit = ['mail.thread']
    _description = 'Pet Master'


    name = fields.Char(string="Name", required=True, tracking=True)
    name = fields.Char(string='Name', required=True)
    species = fields.Char(string='Species', required=True)
    breed = fields.Char(string='Breed')
    age = fields.Integer(string='Age')
    weight = fields.Float(string='Weight')
    image = fields.Binary(string='Image')
    owner_id = fields.Many2one('vetinary.owner', string="Owner", required=True)