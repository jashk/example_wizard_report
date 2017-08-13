# -*- coding: utf-8 -*-

from odoo import api, models
from odoo.exceptions import UserError


class ReportHelloworld(models.AbstractModel):
    _name = 'report.example_wizard_report.report_helloworld'

    @api.model
    def render_html(self, docids, data=None):
        self.model = self.env.context.get('active_model')
        docs = self.env[self.model].browse(self.env.context.get('active_id'))
        
        docargs = {
            'doc_ids': self.ids,
            'doc_model': self.model,
            'docs': docs,
        }
        
        return self.env['report'].render('example_wizard_report.report_helloworld', docargs)
