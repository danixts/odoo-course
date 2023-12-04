# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    database_id = fields.Many2one('admin.database', 'Database')
    lang_id = fields.Many2one('res.lang', 'Lang')

    field_a = fields.Float('A', related='database_id.field_a')
    field_b = fields.Float('B', related='database_id.field_b')
    field_result = fields.Char('Result', related='database_id.field_result')