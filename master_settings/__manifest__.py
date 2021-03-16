# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,manifest-required-author
{
    'name': 'Master Settings for Ultimate Solutions',
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
    'depends': ['base', 'document'],
    'data': [
         'security/ir.model.access.csv',
        # 'report/',
        # 'wizard/',
         'views/master_setting_view.xml',
        'views/settings.xml'
        # 'data/',
    ],
    'demo': [],
}