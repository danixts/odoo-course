# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DatabaseFields(models.Model):
    _inherit = 'admin.database'
    _description = 'Database fields'

    account_id = fields.Many2many('account.move')
