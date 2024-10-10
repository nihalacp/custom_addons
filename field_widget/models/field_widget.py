from odoo import models,fields
import uuid

YOUTUBE = "https://www.youtube.com/@ajscriptmedia"
WEBSITE = "https://ajscript.com"
NOTES = """Note 1
Note 2
Note 3"""

class FieldsWidget(models.Model):
    _name = "fields.widget"
    _description = "Fields Widget"

    name = fields.Char()
    state = fields.Selection([('draft','Draft'),('confirm','Confirm'),('done','Done')])
    priority = fields.Selection([('0','Normal'),('1','Good'),('2','Very Good'),('3','Excellent')])
    kanban_state = fields.Selection([('normal','Normal'),('blocked','Blocked'),('done','Done')])
    is_active = fields.Boolean()
    is_favorite = fields.Boolean()
    is_subscribed = fields.Boolean()
    is_present = fields.Boolean()
    pdf = fields.Binary()
    youtube = fields.Char(default=YOUTUBE)
    website = fields.Char(default=WEBSITE)
    token = fields.Char(default=uuid.uuid4())
    notes = fields.Text(default=NOTES)
    signature = fields.Binary()