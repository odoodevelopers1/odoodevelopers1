# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,manifest-required-author
{
    'name': 'Ultimate Solution Work Center custom',
    'author': 'Sameer Mustafa Fathy',
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
    'depends': ['base', 'document','mrp','maintenance'],
    'data': [
        # 'security/ir.model.access.csv',
        # 'report/',
        # 'wizard/',
         'views/work_center_view.xml',
         'data/sequence.xml',
    ],
    'demo': [],
}