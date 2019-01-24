# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.http import request

import odoo


class Website(models.Model):
    _inherit = 'website'

    @api.model
    @odoo.tools.ormcache()
    def _get_languages_dir(self):
        website = self
        return dict([(lg.code, lg.direction) for lg in website.language_ids])

    @api.multi
    def get_languages_dir(self):
        return self._get_languages_dir()

    @api.multi
    def write(self, vals):
        self._get_languages_dir.clear_cache(self)
        return super(Website, self).write(vals)
