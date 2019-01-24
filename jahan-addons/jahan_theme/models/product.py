# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    website_description = fields.Html('Description for the website', sanitize_attributes=False, translate=False)
    website_description_fa = fields.Html('Description for the website in Persion', sanitize_attributes=False, translate=False)
