# -*- coding: utf-8 -*-

from odoo import api, fields, models


class HelloWorld(models.TransientModel):
    _name = 'example.wizard.helloworld'
    _description = "Example Wizard"

    user_id = fields.Many2one('res.users', string='User', required=True)

    @api.multi
    def check_report(self):
        data = {}
        data['form'] = self.read(['user_id'])[0]
        return self._print_report(data)

    def _print_report(self, data):
        data['form'].update(self.read(['user_id'])[0])
        return self.env['report'].get_action(self, 'example_wizard_report.report_helloworld', data=data)
