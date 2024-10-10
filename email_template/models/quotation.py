from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    quotation_expiry_notification = fields.Boolean(string="Quotation Expiry Notification",config_parameter="email_template.quotation_expiry_notification")
    quotation_expiry_days = fields.Integer(string="Quotation Expiry Days", config_parameter="email_template.quotation_expiry_days", default=5)
    quotation_expiry_manager = fields.Many2one('res.users', string="Quotation Expiry Manager", config_parameter="email_template.quotation_expiry_manager")

 

    @api.model
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        # Save the values to system parameters
        self.env['ir.config_parameter'].sudo().set_param('sale.quotation_expiry_notification', self.quotation_expiry_notification)
        self.env['ir.config_parameter'].sudo().set_param('sale.quotation_expiry_days', self.quotation_expiry_days)
        self.env['ir.config_parameter'].sudo().set_param('sale.quotation_expiry_manager', self.quotation_expiry_manager.id)




    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        # Retrieve the values from system parameters
        res.update({
            'quotation_expiry_notification': self.env['ir.config_parameter'].sudo().get_param('sale.quotation_expiry_notification', default=False),
            'quotation_expiry_days': int(self.env['ir.config_parameter'].sudo().get_param('sale.quotation_expiry_days', default=5)),
            'quotation_expiry_manager': int(self.env['ir.config_parameter'].sudo().get_param('sale.quotation_expiry_manager', default=False)),
        })
        return res


    