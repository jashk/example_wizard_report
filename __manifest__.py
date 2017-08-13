# -*- coding: utf-8 -*-
# Copyright 2017 Fidel Aquino
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Example Wizard Report',
    'category': 'Examples',
    'description': """
Wizard PDF Report Example
=================================================================
Odoo examples
    - Wizard PDF Report
        """,
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Fidel Aquino <fidel.aquino.dev@gmail.com>',
    'website': 'www.jashk.me',
    'depends': [
        'base_setup', 'report'
    ],
    'data': [
        'wizards/example_wizard_report.xml',
        'views/helloworld_example_report.xml',
        'views/report_helloworld.xml'
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
