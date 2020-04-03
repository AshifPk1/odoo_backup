# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    bottom_line_price = fields.Float('Bottom Line Price')