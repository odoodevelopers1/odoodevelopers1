# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,manifest-required-author
{
    'name': 'Bom and stock Customization By Ultimate Solutions',
    'author': 'Sameer mustafa',
    'website': '',
    'version': '1.0',
    'summary': '',
    'category': '',
    'license': '',
    'price': 0.0,
    'currency': '',
    'sequence': 1,
    'installable': True,
    'application': True,
    'auto_install': False,
    'depends': ['base', 'document','product','mrp', 'stock'],
    'data': [
        # 'security/ir.model.access.csv',
        'reports/reports.xml',
        'reports/bom_reports.xml',
         'views/bom_stock_view.xml',
        # 'views/',
         'data/sequence.xml',
    ],
    'demo': [],
}