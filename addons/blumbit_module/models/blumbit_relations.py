# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BlumbitRelations(models.Model):
    _name = 'blumbit.relations'
    _description = 'Blumbit Relations'
    _rec_name = 'code'

    name = fields.Char('Name', required=True)
    code = fields.Char('Code')
    currency_id = fields.Many2one('res.currency')
    user_id = fields.Many2one('blumbit.user', 'User')