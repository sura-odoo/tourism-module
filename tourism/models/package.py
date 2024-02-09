from odoo import models,fields

class package(models.Model):
    _name = "package"
    _description = "Holiday Package"

    name = fields.Char(required=True, string="Title")
    description = fields.Text()
    price = fields.Integer(string="Price (Rs.)")
    # destination = 
    duration = fields.Integer(string="Duration in Days")
    participants = fields.Integer()
    # availability
    # tags
