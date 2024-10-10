from odoo import api, models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'


    approver_id = fields.Many2one('res.users', string='Approver')


    @api.model
    def create(self, vals):
        record = super(SaleOrder, self).create(vals)
        if record.approver_id:
            # Create activity for approval
            activity_type = self.env.ref('mail.mail_activity_data_todo', raise_if_not_found=False)
            self.env['mail.activity'].create({
                'res_model_id': self.env['ir.model'].search([('model', '=', 'sale.order')], limit=1).id,
                'res_id': record.id,
                'activity_type_id': activity_type.id if activity_type else False,
                'user_id': record.approver_id.id,
                'summary': 'Approve Sale Order %s' % record.name,
                'note': 'Please review and approve the sale order.',
            })
        return record

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        # Update activity status to 'Done'
        activity_type_done = self.env.ref('mail.mail_activity_data_done', raise_if_not_found=False)
        activities = self.env['mail.activity'].search([
            ('res_model_id', '=', self.env['ir.model'].search([('model', '=', 'sale.order')], limit=1).id),
            ('res_id', 'in', self.ids),
            ('activity_type_id', '=', self.env.ref('mail.mail_activity_data_todo').id)
        ])
        if activity_type_done:
            activities.write({'activity_type_id': activity_type_done.id})
        return res
