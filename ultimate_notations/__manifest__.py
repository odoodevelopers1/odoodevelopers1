# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,manifest-required-author
{
    'name': 'The Notations  ',
    'author': 'Sameer Mustafa',
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
         'views/notations_views.xml',
         'views/notation_selection_view.xml',
        'views/notations_line.xml',
          'data/sequence.xml',
    ],
    'demo': [],
}