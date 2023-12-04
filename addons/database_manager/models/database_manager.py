# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

ENVIRONMENT_TYPES = [
    ('dev', 'Development'),
    ('qa', 'Testing'),
    ('stating', 'Pre Production'),
    ('prod', 'Production'),
]


class AdminDatabase(models.Model):
    _name = 'admin.database'
    _description = 'Database Admin'
    _inherit = ['mail.thread']

    name = fields.Char('Name', tracking=True, translate=True)
    description = fields.Char('Description', tracking=True)
    instance = fields.Char('Instance', tracking=True)
    is_backup = fields.Boolean('Is Backup', default=False, tracking=True)

    type_environment = fields.Selection(ENVIRONMENT_TYPES, string='Type Environment', tracking=True)
    type_software = fields.Char('Type Software', tracking=True)
    server_id = fields.Many2one('admin.server', 'Server', tracking=True)
    frequency_ids = fields.Many2many('admin.frequency', tracking=True)

    field_a = fields.Float('A')
    field_b = fields.Float('B')
    field_result = fields.Char('Result', compute='_onchange_calculate_sum', store=True)

    table_ids = fields.Many2many('admin.table')

    @api.onchange('is_backup')
    def _onchange_change_text(self):
        if self.is_backup:
            self.type_software = 'Cambiamos de software'
            self.type_environment = 'prod'
            self.field_a = 5
            self.field_b = 5
        else:
            self.type_software = 'Field Default'
            self.type_environment = 'stating'

    @api.onchange('field_a', 'field_b')
    def _onchange_calculate_sum(self):
        a = self.field_a or 0
        b = self.field_b or 0
        self.field_result = f'{a + b}'

    @api.constrains('field_a')
    def _valid_field_a(self):
        if self.field_a < 0:
            raise ValidationError('Field not zero')
