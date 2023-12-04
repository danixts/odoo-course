# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AdminServer(models.Model):
    _name = 'admin.server'
    _description = 'Admin server'

    ip = fields.Char('IP')
    name = fields.Char('Name')
    description = fields.Char('Description')

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, "%s (%s)" % (rec.ip, rec.name)))
        return res