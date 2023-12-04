# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AdminTable(models.Model):
    _name = 'admin.table'
    _description = 'Database table'
    _rec_name = 'name'

    name = fields.Char('Name')
    field = fields.Char('Field')
    type = fields.Char('Type')
    description = fields.Char('Description')
    file = fields.Binary('File')
    file_name = fields.Char('File name')