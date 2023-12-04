# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AdminUser(models.Model):
    _name = 'admin.user'
    _description = 'Database user'
    _rec_name = 'name'

    name = fields.Char('Name')
    description = fields.Char('Description')
    position = fields.Char('Instance')

    admin_database_ids = fields.Many2many('admin.database', string='Admin Database')
    admin_access_ids = fields.Many2many('admin.access', string='Admin Access')


class AdminAccess(models.Model):
    _name = 'admin.access'
    _description = 'Database Access'
    _rec_name = 'name'

    name = fields.Char('Name')
    description = fields.Char('Description')
