from odoo import api, models, fields, tools

class SaleSQlView(models.Model):
    _name = 'sale.sql.view'
    _description = 'Sale SQl View'
    _auto = False

    sale_number = fields.Char('Quotation')
    customer = fields.Char('Customer')
    order_date = fields.Datetime('Order Date')
    amount = fields.Monetary('Amount')
    currency_id = fields.Many2one('res.currency', string='Currency')

    
    def init(self):
        tools.drop_view_if_exists(self._cr,'sale_sql_view')
        self._cr.execute("""
            CREATE OR REPLACE VIEW sale_sql_view AS (
                SELECT row_number() OVER() as id,
                so.name as sale_number,
                rp.name as customer,
                so.date_order as order_date,
                so.amount_total as amount,
                rc.id as currency_id
                FROM sale_order so
                JOIN res_partner rp ON so.partner_id = rp.id
                JOIN res_currency rc ON so.currency_id = rc.id
            )
        """)

    def action_print(self):
        for rec in self:
            rec.state = 'print'