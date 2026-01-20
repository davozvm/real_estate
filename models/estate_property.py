from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Property"

    name = fields.Char(required=True)
    description = fields.Text()
    active =  fields.Boolean(default = True)
    estate = fields.Selection([
        {"new", "New"},
        {"offer_received", "Offer Received"},
        {"offer_accepted", "Offer Accepted"},
        {"sold", "Sold"},
        {"canceled", "Canceled"},
        {"bloq", "Bloqueado"}
    ], string= "Status", copy=False, required=True, default="new")

    postcode = fields.Char()
    date_availability = fields.Date(
        copy= False, default = lambda self: fields.Date.add(fields.Date.today(), months= 5))
    expected_price = fields.Float(required = True)
    selling_price = fields.Float(readonly= True, copy= False)
    bedrooms = fields.Integer(default = 2)
    living_area = fields.Integer(string= "Living Area (sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ("north", "North"),
        ("south", "South"),
        ("east", "East"),
        ("west", "West"),
        ("NA", "NA"),
    ])