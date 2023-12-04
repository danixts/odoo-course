# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AdminFrequency(models.Model):
    _name = 'admin.frequency'
    _description = 'Admin Frequency'
    _rec_name = 'code'

    code = fields.Char('Code')
    description = fields.Char('Description')
