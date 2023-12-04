# -*- coding: utf-8 -*-
import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class BlumbitModel(models.Model):
    _name = 'blumbit.model'
    _description = 'Blumbit Model'

    # Tipos de datos basicos
    name = fields.Char('Name', required=True, help='Name help')
    last_name = fields.Char('Last Name')
    is_active = fields.Boolean('Is Active', default=True)
    age = fields.Integer('Age', required=True)
    amount = fields.Float('Amount')

    blumbit_user_id = fields.Many2many('blumbit.user')

    def press_button(self):
        users = []
        if self.blumbit_user_id:
            for rec in self.blumbit_user_id:
                users.append({
                    "first_name": rec.first_name,
                    "last_name": rec.last_name,
                    "email": rec.email,
                    "phone": rec.phone,
                    "currency": rec.currency_id.name
                })
        res = {
            "name": self.name,
            "last_name": self.last_name,
            "is_active": self.is_active,
            "amount": self.amount,
            "users": users
        }
        _logger.warning(res)
        # self.env['res.lang']._activate_lang('it_IT')

