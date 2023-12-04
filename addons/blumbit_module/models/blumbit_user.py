# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BlumbitUser(models.Model):
    _name = 'blumbit.user'
    _description = 'Blumbit User'
    # _rec_name = 'first_name'

    first_name = fields.Char('First Name')
    last_name = fields.Char('Last Name')
    email = fields.Char('Email', size=80)
    phone = fields.Char('Phone')
    nit = fields.Char('Nit')
    status = fields.Boolean('Status', default=True)
    image = fields.Image('Image')
    birth_date = fields.Date('Birth Date')
    gen = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    comment = fields.Text('Comment')

    partner_id = fields.Many2one('res.partner')
    currency_id = fields.Many2one('res.currency')

    rel_id = fields.One2many('blumbit.relations', 'user_id')

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, "%s %s / (%s)" % (rec.first_name, rec.last_name, rec.nit)))
        return res
